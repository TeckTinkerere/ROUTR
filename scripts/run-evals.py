#!/usr/bin/env python3
"""run-evals.py — run ROUTR's evals/*.eval.json against the router menu.

This is a SMOKE TEST, not ground truth. `--mode static` is a deterministic
lexical scorer over each router's frontmatter `description:` (no LLM calls,
no cost, always available) — it estimates whether a router's description
gives enough signal to win the right prompts, not whether an LLM would
actually pick it. `--mode claude` shells out to the real `claude -p` CLI and
is a closer (but slower, non-free, non-deterministic) approximation of real
routing behavior. Treat both as regression smoke tests for description
quality, not as a certification that routing is "correct".

Usage:
    python scripts/run-evals.py                         # static mode, all evals
    python scripts/run-evals.py --mode claude            # shells out to claude -p
    python scripts/run-evals.py --mode claude --model claude-haiku-4-5-20251001
    python scripts/run-evals.py --file evals/routr-router.eval.json
    python scripts/run-evals.py --json out.json --min-accuracy 0.8

Only prompts carrying an `expected_router` field are scored for routing
accuracy; prompts that test in-skill behavior only (`expected_behaviors`,
`expected_router_handoff`, etc.) are skipped and counted separately, since
this script judges router *selection*, not in-skill behavior adherence.

Candidate routers = skills/routr-*/SKILL.md, EXCLUDING routr-catalog,
routr-depth-*, and routr-router itself (evals expect the concrete situational
router, not the meta-router that would dispatch to it).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

# Windows consoles often default to a cp1252-family encoding that can't
# encode arrows/quotes in eval prompt text; force UTF-8 with a safe fallback
# so this never crashes mid-report on Windows terminals.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
EVALS_DIR = REPO_ROOT / "evals"

DEFAULT_MODEL = "claude-haiku-4-5-20251001"

STOPWORDS = {
    "a", "an", "the", "to", "for", "in", "of", "on", "and", "or", "is", "it",
    "this", "that", "with", "as", "at", "by", "from", "your", "you", "i",
    "use", "when", "not", "no", "do", "does", "doesn't", "don't", "step",
    "steps", "before", "after", "without", "into", "if", "so", "be", "are",
    "was", "were", "will", "can", "just", "about", "what", "how", "why",
    "where", "which", "who",
}

ROUTR_NAME_RE = re.compile(r"\brouter?-[a-z-]+\b")


# --------------------------------------------------------------------------
# Router menu
# --------------------------------------------------------------------------

@dataclass
class Router:
    name: str
    description: str
    what_tokens: set = field(default_factory=set)
    use_when_tokens: set = field(default_factory=set)
    not_for_tokens: set = field(default_factory=set)
    quoted_phrases: list = field(default_factory=list)
    child_mentions: set = field(default_factory=set)  # backticked names / slash-commands in body


def stem(word: str) -> str:
    w = word.lower()
    if len(w) > 5 and w.endswith("ing"):
        return w[:-3]
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    if len(w) > 4 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def tokenize(text: str) -> set:
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {stem(w) for w in words if w not in STOPWORDS and len(w) > 1}


def parse_description(skill_md_text: str) -> str:
    for line in skill_md_text.splitlines():
        if line.startswith("description:"):
            desc = line[len("description:"):].strip()
            desc = desc.strip('"').strip()
            return desc
    return ""


def load_router(dirpath: Path) -> Router | None:
    skill_md = dirpath / "SKILL.md"
    if not skill_md.exists():
        return None
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    desc = parse_description(text)
    if not desc:
        return None

    quoted_phrases = [m.group(1) for m in re.finditer(r"'([^']{4,})'", desc)]

    # Split WHAT / Use when: / Not for:
    use_when_part = ""
    not_for_part = ""
    what_part = desc
    m = re.search(r"Use when:(.*?)(?:Not for:|$)", desc, re.IGNORECASE | re.DOTALL)
    if m:
        use_when_part = m.group(1)
        what_part = desc[: m.start()]
    m2 = re.search(r"Not for:(.*)$", desc, re.IGNORECASE | re.DOTALL)
    if m2:
        not_for_part = m2.group(1)

    # Child skill / slash-command mentions in the body (skip the routr-* self
    # references so they don't inflate scoring for meta-mentions).
    child_mentions = set()
    for m3 in re.finditer(r"`([a-zA-Z][a-zA-Z0-9_/-]{2,})`", text):
        name = m3.group(1)
        if name.startswith("routr-"):
            continue
        child_mentions.add(name.lower())
    for m4 in re.finditer(r"(?<![\w`])(/[a-z][a-z-]{2,})\b", text):
        child_mentions.add(m4.group(1).lower())

    return Router(
        name=dirpath.name,
        description=desc,
        what_tokens=tokenize(what_part),
        use_when_tokens=tokenize(use_when_part),
        not_for_tokens=tokenize(not_for_part),
        quoted_phrases=quoted_phrases,
        child_mentions=child_mentions,
    )


def load_candidate_routers() -> list:
    routers = []
    for dirpath in sorted(SKILLS_DIR.glob("routr-*")):
        if not dirpath.is_dir():
            continue
        name = dirpath.name
        if name in ("routr-router", "routr-catalog") or name.startswith("routr-depth-"):
            continue
        router = load_router(dirpath)
        if router:
            routers.append(router)
    return routers


# --------------------------------------------------------------------------
# static mode scorer
# --------------------------------------------------------------------------

def score_static(prompt: str, router: Router) -> float:
    prompt_tokens = tokenize(prompt)
    prompt_lower = prompt.lower()

    score = 0.0
    score += 2.0 * len(prompt_tokens & router.use_when_tokens)
    score += 1.0 * len(prompt_tokens & router.what_tokens)

    for phrase in router.quoted_phrases:
        if phrase.lower() in prompt_lower:
            score += 3.0

    for mention in router.child_mentions:
        m = mention.lstrip("/")
        if len(m) > 2 and m in prompt_lower:
            score += 4.0

    penalty_tokens = prompt_tokens & router.not_for_tokens
    score -= 1.5 * len(penalty_tokens)

    return score


def pick_static(prompt: str, routers: list) -> tuple:
    scored = [(score_static(prompt, r), r.name) for r in routers]
    scored.sort(key=lambda t: (-t[0], t[1]))
    best_score, best_name = scored[0]
    return best_name, {name: s for s, name in scored}


# --------------------------------------------------------------------------
# claude mode
# --------------------------------------------------------------------------

def build_menu(routers: list) -> str:
    lines = [f"- {r.name}: {r.description}" for r in routers]
    return "\n".join(lines)


def ask_claude(prompt: str, menu: str, model: str, timeout: int) -> str | None:
    claude_prompt = (
        "You are a router that picks exactly one workflow skill for a coding "
        "agent to load, given a user request.\n\n"
        "Available routers (name: description):\n"
        f"{menu}\n\n"
        f'User request: "{prompt}"\n\n'
        "Reply with ONLY the chosen router's name (e.g. routr-debug). "
        "No explanation, no punctuation, nothing else."
    )
    try:
        result = subprocess.run(
            [shutil.which("claude") or "claude", "-p", "--model", model],
            input=claude_prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        print(f"  ! claude CLI call failed: {exc}", file=sys.stderr)
        return None
    if result.returncode != 0:
        first = ((result.stdout or result.stderr or "").strip().splitlines() or ["no output"])[0]
        print(f"  ! claude CLI exited {result.returncode}: {first}", file=sys.stderr)
        return None
    out =(result.stdout or "") + " " + (result.stderr or "")
    m = re.search(r"\broutr-[a-z-]+\b", out)
    return m.group(0) if m else None


def pick_claude_batch(prompts: list, routers: list, model: str, concurrency: int, timeout: int) -> dict:
    menu = build_menu(routers)
    results = {}
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
        futures = {
            ex.submit(ask_claude, p, menu, model, timeout): p for p in prompts
        }
        for fut in as_completed(futures):
            p = futures[fut]
            try:
                results[p] = fut.result()
            except Exception as exc:  # pragma: no cover - defensive
                print(f"  ! error scoring prompt: {exc}", file=sys.stderr)
                results[p] = None
    return results


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--mode", choices=["static", "claude"], default="static")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="model for --mode claude")
    parser.add_argument("--concurrency", type=int, default=4, help="parallel claude -p calls")
    parser.add_argument("--timeout", type=int, default=60, help="per-call timeout (seconds) for --mode claude")
    parser.add_argument("--file", help="run only this eval file")
    parser.add_argument("--json", dest="json_path", help="write machine-readable results here")
    parser.add_argument("--min-accuracy", type=float, default=None, help="exit 1 if overall accuracy is below this")
    args = parser.parse_args()

    routers = load_candidate_routers()
    if not routers:
        print("No candidate routers found under skills/routr-*", file=sys.stderr)
        return 2

    if args.mode == "claude":
        # Preflight: a signed-out or broken CLI would otherwise score every
        # prompt as a silent miss (got=None).
        try:
            probe = subprocess.run(
                [shutil.which("claude") or "claude", "-p", "--model", args.model],
                input="Reply with only the word: ok",
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=args.timeout,
            )
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
            print(f"claude CLI preflight failed: {exc}", file=sys.stderr)
            return 2
        if probe.returncode != 0:
            detail = (probe.stdout or probe.stderr or "").strip().splitlines()
            print(
                "claude CLI preflight failed (exit "
                f"{probe.returncode}): {detail[0] if detail else 'no output'}\n"
                "Run `claude` interactively to sign in, then retry.",
                file=sys.stderr,
            )
            return 2

    if args.file:
        candidate = Path(args.file)
        if not candidate.exists():
            candidate = EVALS_DIR / Path(args.file).name
        eval_files = [candidate]
    else:
        eval_files = sorted(EVALS_DIR.glob("*.eval.json"))

    if not eval_files:
        print("No eval files found.", file=sys.stderr)
        return 2

    all_results = []
    total_scored = 0
    total_correct = 0
    total_skipped = 0
    total_violations = 0
    misses = []

    per_file_rows = []

    for ef in eval_files:
        try:
            data = json.loads(ef.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"SKIP {ef}: invalid JSON ({exc})")
            continue

        prompts = data.get("prompts", [])
        scorable = [p for p in prompts if isinstance(p, dict) and p.get("expected_router")]
        skipped = len(prompts) - len(scorable)
        total_skipped += skipped

        if not scorable:
            per_file_rows.append((ef.name, 0, 0, skipped, 0))
            continue

        if args.mode == "static":
            predictions = {}
            for p in scorable:
                pred, _scores = pick_static(p["prompt"], routers)
                predictions[p["prompt"]] = pred
        else:
            predictions = pick_claude_batch(
                [p["prompt"] for p in scorable], routers, args.model, args.concurrency, args.timeout
            )

        file_correct = 0
        file_violations = 0
        for p in scorable:
            expected = p["expected_router"]
            got = predictions.get(p["prompt"])
            must_not_load = set(p.get("must_not_load", []) or [])
            hit = got == expected
            violation = got in must_not_load if got else False

            if hit:
                file_correct += 1
            else:
                misses.append(
                    {
                        "file": ef.name,
                        "prompt": p["prompt"],
                        "expected": expected,
                        "got": got,
                        "boundary": p.get("boundary"),
                    }
                )
            if violation:
                file_violations += 1

            all_results.append(
                {
                    "file": ef.name,
                    "prompt": p["prompt"],
                    "expected_router": expected,
                    "predicted_router": got,
                    "hit": hit,
                    "must_not_load_violation": violation,
                    "boundary": p.get("boundary"),
                }
            )

        total_scored += len(scorable)
        total_correct += file_correct
        total_violations += file_violations
        per_file_rows.append((ef.name, file_correct, len(scorable), skipped, file_violations))

    # ---- report ----
    print(f"Mode: {args.mode}" + (f" (model={args.model})" if args.mode == "claude" else ""))
    print(f"Candidate routers: {len(routers)} ({', '.join(r.name for r in routers)})")
    print()
    print(f"{'file':35} {'correct/scored':16} {'accuracy':>9} {'skipped':>8} {'violations':>11}")
    for name, correct, scored, skipped, violations in per_file_rows:
        acc = f"{(correct / scored * 100):.0f}%" if scored else "n/a"
        print(f"{name:35} {f'{correct}/{scored}':16} {acc:>9} {skipped:>8} {violations:>11}")

    overall_acc = (total_correct / total_scored) if total_scored else 0.0
    print()
    print(f"Overall accuracy: {total_correct}/{total_scored} ({overall_acc * 100:.1f}%)")
    print(f"Prompts skipped (no expected_router): {total_skipped}")
    print(f"must_not_load violations: {total_violations}")

    if misses:
        print()
        print("Misses:")
        for m in misses:
            boundary = f" [boundary: {m['boundary']}]" if m.get("boundary") else ""
            print(f"  - {m['file']}: \"{m['prompt']}\" expected={m['expected']} got={m['got']}{boundary}")

    if args.json_path:
        Path(args.json_path).write_text(
            json.dumps(
                {
                    "mode": args.mode,
                    "model": args.model if args.mode == "claude" else None,
                    "overall_accuracy": overall_acc,
                    "total_scored": total_scored,
                    "total_correct": total_correct,
                    "total_skipped": total_skipped,
                    "total_violations": total_violations,
                    "results": all_results,
                    "misses": misses,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nWrote machine-readable results to {args.json_path}")

    if args.min_accuracy is not None and overall_acc < args.min_accuracy:
        print(f"\nFAIL: accuracy {overall_acc:.3f} < --min-accuracy {args.min_accuracy:.3f}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
