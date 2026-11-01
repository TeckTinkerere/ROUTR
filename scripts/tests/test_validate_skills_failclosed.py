"""validate-skills.sh must fail closed when a Python checker crashes. Stdlib only.

    python -m unittest discover -s scripts/tests -v
"""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
BASH = shutil.which("bash")

# Stands in for python3/python: every _validate_helpers.py call dies the way an
# uncaught exception does (traceback on stderr, exit 1, no FAIL line).
CRASHING_PYTHON = """#!/bin/sh
echo "Traceback (most recent call last):" >&2
echo "RuntimeError: simulated checker crash" >&2
exit 1
"""


@unittest.skipUnless(BASH, "bash not on PATH")
class ValidatorFailsClosedTests(unittest.TestCase):
    def setUp(self):
        self.bin = Path(tempfile.mkdtemp(prefix="routr-fakepy-"))
        self.addCleanup(shutil.rmtree, self.bin, True)
        for name in ("python3", "python"):
            exe = self.bin / name
            exe.write_text(CRASHING_PYTHON, encoding="utf-8", newline="\n")
            exe.chmod(0o755)

    def test_crashing_checker_fails_the_run(self):
        env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ.get("PATH", ""))
        proc = subprocess.run(
            [BASH, "scripts/validate-skills.sh"], cwd=REPO, env=env,
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300,
        )
        self.assertIn("simulated checker crash", proc.stdout, "fake python was not picked up")
        self.assertEqual(proc.returncode, 1, proc.stdout[-2000:])
        self.assertNotIn("All checks passed", proc.stdout)
        # One crash FAIL per helper call: skills, links, evals, routes, plugin.
        self.assertEqual(proc.stdout.count("(it likely crashed)"), 5, proc.stdout[-2000:])


if __name__ == "__main__":
    unittest.main()
