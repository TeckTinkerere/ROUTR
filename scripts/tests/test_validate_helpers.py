"""Unit tests for scripts/_validate_helpers.py check 13 (plugin manifests). Stdlib only.

    python -m unittest discover -s scripts/tests -v
"""
import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

_spec = importlib.util.spec_from_file_location("validate_helpers", HERE.parent / "_validate_helpers.py")
validate_helpers = importlib.util.module_from_spec(_spec)
sys.modules["validate_helpers"] = validate_helpers
_spec.loader.exec_module(validate_helpers)

CHANGELOG = """# Changelog

## [Unreleased]

## [1.4.0] - 2026-01-01

## [1.3.0] - 2025-12-01
"""


class PluginManifestTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="routr-plugin-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.write(".plugin/plugin.json", {"name": "routr", "version": "1.4.0", "skills": "./skills/"})
        self.write(".claude-plugin/plugin.json", {"name": "routr", "version": "1.4.0"})
        self.write(".claude-plugin/marketplace.json", {
            "name": "routr",
            "owner": {"name": "Owner"},
            "plugins": [{"name": "routr", "source": "./"}],
        })
        (self.root / "CHANGELOG.md").write_text(CHANGELOG, encoding="utf-8")
        skill = self.root / "skills" / "routr-debug" / "SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: routr-debug\n---\n", encoding="utf-8")

    def write(self, rel, obj):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(obj if isinstance(obj, str) else json.dumps(obj), encoding="utf-8")

    def edit(self, rel, **changes):
        path = self.root / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        data.update(changes)
        path.write_text(json.dumps(data), encoding="utf-8")

    def run_check(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fails = validate_helpers.cmd_plugin(str(self.root))
        return fails, out.getvalue()

    def assert_fails(self, needle):
        fails, out = self.run_check()
        self.assertGreater(fails, 0, out)
        self.assertIn(needle, out)

    def test_consistent_manifests_pass(self):
        fails, out = self.run_check()
        self.assertEqual(fails, 0, out)
        self.assertEqual(out, "")

    def test_real_repo_passes(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fails = validate_helpers.cmd_plugin(str(REPO))
        self.assertEqual(fails, 0, out.getvalue())

    def test_invalid_json_fails(self):
        self.write(".claude-plugin/marketplace.json", '{"name": "routr",')
        self.assert_fails("does not parse as JSON")

    def test_missing_manifest_fails(self):
        (self.root / ".claude-plugin" / "plugin.json").unlink()
        self.assert_fails(".claude-plugin/plugin.json: missing")

    def test_version_drift_between_manifests_fails(self):
        self.edit(".claude-plugin/plugin.json", version="1.5.0")
        self.assert_fails("plugin version drift")

    def test_version_ahead_of_changelog_fails(self):
        self.edit(".plugin/plugin.json", version="1.5.0")
        self.edit(".claude-plugin/plugin.json", version="1.5.0")
        self.assert_fails("CHANGELOG.md (latest release)='1.4.0'")

    def test_unreleased_version_heading_is_skipped(self):
        changelog = CHANGELOG.replace("## [Unreleased]", "## [1.5.0] - Unreleased")
        (self.root / "CHANGELOG.md").write_text(changelog, encoding="utf-8")
        fails, out = self.run_check()
        self.assertEqual(fails, 0, out)

    def test_marketplace_entry_name_mismatch_fails(self):
        self.edit(".claude-plugin/marketplace.json", plugins=[{"name": "other", "source": "./"}])
        self.assert_fails("expected exactly one plugins[] entry named 'routr'")

    def test_marketplace_entry_wrong_source_fails(self):
        self.edit(".claude-plugin/marketplace.json", plugins=[{"name": "routr", "source": "./skills"}])
        self.assert_fails("must use source")

    def test_marketplace_entry_version_mismatch_fails(self):
        self.edit(".claude-plugin/marketplace.json",
                  plugins=[{"name": "routr", "source": "./", "version": "9.9.9"}])
        self.assert_fails("version '9.9.9' differs")

    def test_marketplace_owner_required(self):
        self.edit(".claude-plugin/marketplace.json", owner={})
        self.assert_fails("'owner.name' must be a non-empty string")


if __name__ == "__main__":
    unittest.main()
