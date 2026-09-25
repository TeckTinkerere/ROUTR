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
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

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


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "links" and len(argv) == 3:
        return 1 if cmd_links(argv[2]) else 0
    if cmd == "evals" and len(argv) == 4:
        return 1 if cmd_evals(argv[2], argv[3]) else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
