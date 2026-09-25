#!/usr/bin/env python3
"""Stdlib-only helpers for scripts/validate-skills.sh.

Bash is unpleasant at JSON parsing and multi-line link resolution, so the
heavier checks (9 and 10/11) live here. Every line this script prints that
starts with "FAIL:" or "WARN:" is counted by validate-skills.sh toward its
fail/warn totals — keep that prefix contract when editing.

Subcommands:
  links <skills_dir>                 -- check 9: relative md links resolve
  evals <evals_dir> <skills_dir>     -- checks 10 and 11: eval JSON validity
                                         and router-name references
  skills <skills_dir> <router_tree> <resolution_md>
                                      -- checks 1, 2, 5, 6, 7, 8 (per-skill
                                         loops that would otherwise fork
                                         grep/sed/wc/basename per skill).
                                         Emits "N:FAIL: msg" / "N:WARN: msg"
                                         lines, one per finding, prefixed
                                         with the check number so the bash
                                         caller can bucket them under the
                                         matching "== N. ... ==" header.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r'^name:\s*(.*)$', re.M)
DESC_RE = re.compile(r'^description:\s*(.*)$', re.M)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target)) or target.startswith("//")


def cmd_links(skills_dir: str) -> int:
    root = Path(skills_dir)
    fails = 0
    for md in sorted(root.rglob("*.md")):
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"FAIL: {md}: could not read file ({exc})")
            fails += 1
            continue
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or is_external(target):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            # strip a trailing "title" if present, e.g. (./x.md "title")
            target = target.split(" ", 1)[0]
            # strip anchor fragment
            path_part = target.split("#", 1)[0]
            if path_part == "":
                continue  # pure in-page anchor
            if path_part.startswith("/"):
                # repo-root-relative — resolve from cwd (script runs from repo root)
                resolved = Path(".") / path_part.lstrip("/")
            else:
                resolved = md.parent / path_part
            if not resolved.exists():
                print(f"FAIL: {md}: broken relative link '{target}' -> {resolved} does not exist")
                fails += 1
    return fails


def cmd_evals(evals_dir: str, skills_dir: str) -> int:
    evals_root = Path(evals_dir)
    skills_root = Path(skills_dir)

    known_routers = {p.name for p in skills_root.glob("routr-*") if p.is_dir()}
    situational = {
        n
        for n in known_routers
        if n not in ("routr-router", "routr-catalog") and not n.startswith("routr-depth-")
    }

    # must_not_load may also exclude child skills (e.g. routr-video evals forbid
    # `hyperframes` for a brag request), so accept any canonical registry name there.
    registry = skills_root / "routr-catalog" / "references" / "skill-registry.md"
    registry_names: set[str] = set()
    if registry.is_file():
        registry_names = set(
            re.findall(r"^\|\s*`([a-z0-9._-]+)`", registry.read_text(encoding="utf-8"), re.M)
        )

    fails = 0
    mentioned: set[str] = set()

    eval_files = sorted(evals_root.glob("*.eval.json"))
    if not eval_files:
        print(f"WARN: no *.eval.json files found under {evals_dir}")

    for ef in eval_files:
        try:
            raw = ef.read_text(encoding="utf-8")
            data = json.loads(raw)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL: {ef}: does not parse as JSON ({exc})")
            fails += 1
            continue

        prompts = data.get("prompts", [])
        if not isinstance(prompts, list):
            print(f"FAIL: {ef}: 'prompts' is not a list")
            fails += 1
            continue

        for i, prompt in enumerate(prompts):
            if not isinstance(prompt, dict):
                print(f"FAIL: {ef}: prompts[{i}] is not an object")
                fails += 1
                continue

            expected_router = prompt.get("expected_router")
            if expected_router is not None:
                if expected_router not in known_routers:
                    print(
                        f"FAIL: {ef}: prompts[{i}].expected_router '{expected_router}' "
                        f"does not name an existing skills/routr-* folder"
                    )
                    fails += 1
                else:
                    mentioned.add(expected_router)

            for field in ("expected_chain", "must_not_load"):
                values = prompt.get(field)
                if values is None:
                    continue
                if not isinstance(values, list):
                    print(f"FAIL: {ef}: prompts[{i}].{field} is not a list")
                    fails += 1
                    continue
                for v in values:
                    allowed = known_routers | registry_names if field == "must_not_load" else known_routers
                    if v not in allowed:
                        what = "routr-* folder or registry skill" if field == "must_not_load" else "skills/routr-* folder"
                        print(
                            f"FAIL: {ef}: prompts[{i}].{field} entry '{v}' does not name "
                            f"an existing {what}"
                        )
                        fails += 1
                    else:
                        if field == "expected_chain":
                            mentioned.add(v)

    for router in sorted(situational - mentioned):
        print(f"WARN: {router}: no eval prompt anywhere in {evals_dir} names it as expected_router")

    return fails


def _strip_one_quote(s: str) -> str:
    # mirrors the bash: desc="${desc%\"}"; desc="${desc#\"}"
    if s.endswith('"'):
        s = s[:-1]
    if s.startswith('"'):
        s = s[1:]
    return s


def cmd_skills(skills_dir: str, router_tree: str, resolution_md: str) -> int:
    root = Path(skills_dir)
    fails = 0

    router_tree_text = ""
    router_tree_path = Path(router_tree)
    if router_tree_path.is_file():
        router_tree_text = router_tree_path.read_text(encoding="utf-8", errors="replace")

    resolution_text = ""
    resolution_path = Path(resolution_md)
    if resolution_path.is_file():
        resolution_text = resolution_path.read_text(encoding="utf-8", errors="replace")

    # -- check 1: frontmatter name == folder name (all skills/*/) --
    for dirpath in sorted(root.glob("*/")):
        if not dirpath.is_dir():
            continue
        name = dirpath.name
        skill_md = dirpath / "SKILL.md"
        if not skill_md.is_file():
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        m = NAME_RE.search(text)
        fm_name = m.group(1) if m else ""
        # mirrors bash: sed strips only a leading run of spaces after "name:",
        # then `tr -d '"'` removes every double-quote char, `tr -d '\r'` every CR.
        fm_name = fm_name.lstrip(" \t").replace('"', "").replace("\r", "")
        if fm_name != name:
            print(f"1:FAIL: {skill_md.as_posix()}: frontmatter name '{fm_name}' != folder name '{name}'")
            fails += 1

    # -- checks 2, 5, 6, 7, 8: routr-* skills only --
    for dirpath in sorted(root.glob("routr-*/")):
        if not dirpath.is_dir():
            continue
        name = dirpath.name
        skill_md = dirpath / "SKILL.md"
        if not skill_md.is_file():
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        is_catalog = name == "routr-catalog"
        is_depth = name.startswith("routr-depth-")
        is_situational = not is_catalog and name != "routr-router" and not is_depth

        # check 2: router descriptions contain 'Use when:' (excludes routr-catalog)
        if not is_catalog:
            if "Use when:" not in text:
                print(f"2:FAIL: {skill_md.as_posix()}: description missing 'Use when:' trigger phrase")
                fails += 1

        # check 5: every situational router is in routr-router's tree + resolution.md
        if is_situational:
            if name not in router_tree_text:
                print(f"5:FAIL: {name}: not referenced anywhere in {router_tree} decision tree")
                fails += 1
            if f"`{name}`" not in resolution_text:
                print(f"5:WARN: {name}: not listed in {resolution_md} router precedence list")

        # check 6: description length budget (FAIL > 320, WARN > 280)
        m = DESC_RE.search(text)
        desc = m.group(1).strip() if m else ""
        desc = desc.replace("\r", "")
        desc = _strip_one_quote(desc)
        length = len(desc)
        if length > 320:
            print(f"6:FAIL: {skill_md.as_posix()}: description is {length} chars (> 320 limit)")
            fails += 1
        elif length > 280:
            print(f"6:WARN: {skill_md.as_posix()}: description is {length} chars (> 280 soft budget)")

        # check 7: situational router descriptions contain 'Not for:'
        if is_situational:
            if "Not for:" not in text:
                print(f"7:FAIL: {skill_md.as_posix()}: description missing 'Not for:' boundary phrase")
                fails += 1

        # check 8: SKILL.md line cap (routers <= 150, depth fallbacks <= 200); catalog exempt
        if not is_catalog:
            lines = text.count("\n")  # matches `wc -l`: counts newline chars only
            if is_depth:
                if lines > 200:
                    print(f"8:FAIL: {skill_md.as_posix()}: {lines} lines (> 200 line cap for depth fallbacks)")
                    fails += 1
            else:
                if lines > 150:
                    print(f"8:FAIL: {skill_md.as_posix()}: {lines} lines (> 150 line cap for routers)")
                    fails += 1

    return fails


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "links" and len(argv) == 3:
        return 1 if cmd_links(argv[2]) else 0
    if cmd == "evals" and len(argv) == 4:
        return 1 if cmd_evals(argv[2], argv[3]) else 0
    if cmd == "skills" and len(argv) == 5:
        return 1 if cmd_skills(argv[2], argv[3], argv[4]) else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
