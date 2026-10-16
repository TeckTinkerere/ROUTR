#!/usr/bin/env python3
"""Fake `claude` CLI for testing run-evals.py --mode host. No network, no model.

Reads the prompt from stdin and prints a stream-json sequence like the real
CLI's `-p --output-format stream-json --verbose`: optional hook event, an init
event listing skills from <cwd>/.claude/skills (plus a couple of bundled
ones), assistant Skill tool_use events, and a result event.

Environment:
    FAKE_CLAUDE_SCRIPT   path to a JSON map {prompt substring: ["routr-x", ...]}.
                         The first matching key decides which skills are invoked.
                         Names are emitted verbatim (use "ns:routr-x" to test prefixes).
    FAKE_CLAUDE_MODE     "auth"    -> authentication_failed stream, exit 1
                         "noskill" -> never invoke a skill
                         unset     -> follow FAKE_CLAUDE_SCRIPT, else invoke nothing
    FAKE_CLAUDE_HOOK     "1" -> print a hook_started event before init
    FAKE_CLAUDE_USER_SKILLS  comma list added to the skills list when the
                         --setting-sources argument includes "user"
    FAKE_CLAUDE_ARGS_LOG path; append one line of JSON {argv, cwd} per call
"""
import json
import os
import sys
from pathlib import Path


def emit(obj):
    print(json.dumps(obj), flush=True)


def main():
    argv = sys.argv[1:]
    prompt = sys.stdin.read()
    log = os.environ.get("FAKE_CLAUDE_ARGS_LOG")
    if log:
        with open(log, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"argv": argv, "cwd": os.getcwd()}) + "\n")

    sources = ""
    if "--setting-sources" in argv:
        sources = argv[argv.index("--setting-sources") + 1]

    if os.environ.get("FAKE_CLAUDE_HOOK") == "1":
        emit({"type": "system", "subtype": "hook_started", "hook_name": "SessionStart"})

    skills_dir = Path(os.getcwd()) / ".claude" / "skills"
    skills = sorted(d.name for d in skills_dir.iterdir() if d.is_dir()) if skills_dir.is_dir() else []
    skills += ["update-config", "simplify"]  # bundled
    if "user" in sources.split(","):
        skills += [s for s in os.environ.get("FAKE_CLAUDE_USER_SKILLS", "").split(",") if s]

    mode = os.environ.get("FAKE_CLAUDE_MODE", "")
    if mode == "auth":
        emit({"type": "system", "subtype": "init", "skills": skills, "tools": ["Skill"],
              "model": "fake-model", "apiKeySource": "none"})
        emit({"type": "assistant", "error": "authentication_failed",
              "message": {"role": "assistant",
                          "content": [{"type": "text", "text": "Not logged in - Please run /login"}]}})
        emit({"type": "result", "subtype": "success", "is_error": True,
              "result": "Not logged in - Please run /login"})
        return 1

    emit({"type": "system", "subtype": "init", "skills": skills, "tools": ["Skill"],
          "model": "fake-model", "apiKeySource": "fake", "cwd": os.getcwd()})

    invoked = []
    script_path = os.environ.get("FAKE_CLAUDE_SCRIPT")
    if script_path and mode != "noskill":
        with open(script_path, encoding="utf-8") as fh:
            script = json.load(fh)
        for needle, names in script.items():
            if needle in prompt:
                invoked = names
                break

    if not invoked:
        emit({"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "ok"}]}})
    for n, name in enumerate(invoked):
        emit({"type": "assistant", "message": {"role": "assistant", "content": [
            {"type": "tool_use", "id": f"toolu_{n}", "name": "Skill", "input": {"skill": name}}]}})
        emit({"type": "user", "message": {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": f"toolu_{n}", "content": "Launching skill"}]}})
    emit({"type": "result", "subtype": "success", "is_error": False, "result": "done", "num_turns": 1 + len(invoked)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
