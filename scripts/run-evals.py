#!/usr/bin/env python3
"""run-evals.py — run ROUTR's evals/*.eval.json against the router menu.

This is a SMOKE TEST, not ground truth. `--mode static` is a deterministic
lexical scorer over each router's frontmatter `description:` (no LLM calls,
no cost, always available) — it estimates whether a router's description
gives enough signal to win the right prompts, not whether an LLM would
actually pick it. `--mode claude` shells out to the real `claude -p` CLI and
is a closer (but slower, non-free, non-deterministic) approximation of real
routing behavior. `--mode predictions` scores a predictions file you (or an
external model) produced out-of-band — see `--export-prompts` below. `--mode host` goes furthest: it runs real Claude Code sessions and records
which skills they actually invoke. Treat
all of these as regression smoke tests for description quality, not as a
certification that routing is "correct".

Usage:
    python scripts/run-evals.py                         # static mode, all evals
    python scripts/run-evals.py --mode claude            # shells out to claude -p
    python scripts/run-evals.py --mode claude --model claude-haiku-4-5-20251001
    python scripts/run-evals.py --mode host --host-env isolated   # real Claude Code sessions
    python scripts/run-evals.py --file evals/routr-router.eval.json
    python scripts/run-evals.py --json out.json --min-accuracy 0.8

    # Score with an external model when the `claude` CLI isn't usable:
    python scripts/run-evals.py --export-prompts prompts.json
    #   -> hand prompts.json's "menu" + "prompts" to any model, collect its
    #      routing choice per prompt id, then:
    python scripts/run-evals.py --mode predictions --predictions preds.json

--mode host  (real Claude Code sessions)
    Measures what an actual `claude` session does with the ROUTR skills it can
    see: which skill(s) it invokes for each eval prompt. Needs the `claude`
    CLI signed in, and costs one real session per prompt. No results are
    claimed anywhere until you run it; treat the numbers as yours.
      * One temp sandbox per run with .claude/skills/ = copies of every
        skills/routr-* folder. Each prompt runs in a fresh session
        (`claude -p --output-format stream-json --verbose --no-session-persistence
        --tools Skill --strict-mcp-config --settings '{"disableAllHooks": true}'`),
        so nothing can edit files, run commands, call MCP servers or fire your
        hooks. The prompt goes to stdin.
      * --host-env isolated (default): `--setting-sources project`, so the agent
        sees only the sandbox's skills plus Claude Code's bundled ones.
        --host-env user: `--setting-sources user,project`, so your installed
        ~/.claude skills crowd the list too (the realistic case).
      * --noise-dir DIR: copy every non-routr-* skill folder from DIR into the
        sandbox, to simulate a crowded list reproducibly.
      * --claude-bin PATH (also used by --mode claude), --max-turns N (default 3),
        --model, --concurrency, --timeout (default 180s here), --keep-sandbox.
      * Chain = situational routr-* skills in the order invoked, de-duplicated.
        If routr-router was the first routr skill invoked, the prompt counts as
        "via router" and the next situational skill is the router. No routr
        skill invoked -> got=None with reason no-skill (or error).
      * A preflight session runs first; a signed-out CLI exits 2 instead of
        scoring zeros. Extra report lines: skills visible to the agent, % of
        prompts with no ROUTR skill, % routed via routr-router, top other
        skills invoked instead. --json adds a `host` summary and per-prompt
        `host` details.
    Example:
        python scripts/run-evals.py --mode host --host-env isolated --file evals/multi-route-holdout.eval.json
        python scripts/run-evals.py --mode host --host-env user --concurrency 2

Only prompts carrying an `expected_router` field are scored for routing
accuracy; prompts that test in-skill behavior only (`expected_behaviors`,
`expected_router_handoff`, etc.) are skipped and counted separately, since
this script judges router *selection*, not in-skill behavior adherence.

Candidate routers = skills/routr-*/SKILL.md, EXCLUDING routr-catalog,
routr-depth-*, and routr-router itself (evals expect the concrete situational
router, not the meta-router that would dispatch to it).

--export-prompts PATH
    Write a JSON file `{"menu": [{"name","description"}...], "prompts":
    [{"id": "<eval-file>#<prompt-index>", "prompt": "..."}...]}` covering
    every scorable prompt (i.e. every prompt with an `expected_router`)
    across the selected eval files (respects `--file`), with NO expected
    answers included, then exits 0 without running any scoring. Feed this
    to an external model/judge to produce a predictions file.

Route plans and alternatives (multi-route design, docs/routing.md):
    * `acceptable_routers: [...]` on a prompt: the prompt is a hit if the chosen
      router is `expected_router` OR any listed alternative (all modes).
    * `expected_chain: [...]`: besides router accuracy, the runner reports
      chain exact-match (predicted chain == expected_chain) and chain
      prefix-match (first min(2, len) steps agree) over prompts that carry
      `expected_chain`. In claude mode the model is asked for one line
      `routr-a > routr-b > routr-c`; the first item is the chosen router.
    * `acceptable_chains: [[...], ...]`: alternative route plans that also
      count as exact/prefix matches for genuinely contested prompts.
    * Model-facing menus (claude mode and --export-prompts) carry each
      router's `next` handoffs and `companions` from routes.json, matching
      what an agent sees after routr-router loads the route map.
    * Predictions values may be `"routr-x"` (chain = [routr-x]) or
      `{"router": "routr-x", "chain": ["routr-x", "routr-y"]}`.
    * Static mode is a baseline: chain = [router] plus the first `handoff`
      from skills/routr-catalog/references/routes.json when the prompt
      contains a multi-intent connector (" and then ", " then ", " and ship"...).

--mode predictions --predictions PATH
    Read a JSON object `{"<id>": "routr-xxx" | {"router","chain"}, ...}` (ids matching
    `--export-prompts`'s `<eval-file>#<prompt-index>` scheme) and score it
    exactly like `--mode static`/`--mode claude`: same results table, same
    misses list, same `must_not_load` violation counting, same `--json` and
    `--min-accuracy` behavior. An id missing from the predictions file is
    scored as a miss with got=None.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
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

ROUTES_JSON = SKILLS_DIR / "routr-catalog" / "references" / "routes.json"

# Connectors that signal a multi-intent request (static-mode chain baseline).
MULTI_INTENT_MARKERS = (
    " and then ", " then ", " and ship", " and deploy", " and commit",
    " and open a pr", " and release", " and publish", " and verify",
    " and make a video", " and write tests",
)

EXPORT_INSTRUCTIONS = (
    "For each prompt, choose exactly one router from `menu` as the FIRST router to load. "
    "If the request clearly spans several routers, you may also give a route plan of at "
    "most 3 routers in order. Write predictions as {\"<id>\": \"routr-x\"} or "
    "{\"<id>\": {\"router\": \"routr-x\", \"chain\": [\"routr-x\", \"routr-y\"]}}. "
    "The chain's first item must equal `router`. A plain string means a single-router plan. "
    "Each menu entry lists `next` (routers it usually hands off to) and `companions` "
    "(checklists that run INSIDE that router's step when their signal fires). Add a `next` "
    "router to the chain only when the request also asks for that job; never add a "
    "companion as a chain step. If the file has a `route_guide`, compose chains with its "
    "`composition_rules` and `step_signals`, and reuse a matching entry in `plans`."
)

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


def load_route_hints() -> dict:
    """{router: {"next": [...], "companions": [{"name", "signal"}]}} from routes.json.

    Mirrors what an agent sees after routr-router loads routes.json, so model
    evals can judge chains with the same information a real agent has.
    """
    try:
        data = json.loads(ROUTES_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    hints = {
        k: {"next": v.get("handoff", []), "companions": []}
        for k, v in (data.get("routers") or {}).items()
        if isinstance(v, dict)
    }
    for c in data.get("companions") or []:
        if isinstance(c, dict) and c.get("active") in hints:
            hints[c["active"]]["companions"].append(
                {"name": c.get("companion"), "signal": c.get("signal", "")}
            )
    return hints


def load_route_guide() -> dict:
    """Composition rules, step signals and known plans from routes.json.

    This is what routr-router reads when it composes a multi-router plan, so
    model evals see the same guidance (disable with --no-route-guide to
    measure its effect).
    """
    try:
        data = json.loads(ROUTES_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {
        "composition_rules": data.get("composition_rules", []),
        "step_signals": data.get("step_signals", []),
        "plans": [
            {"when": c.get("when", ""), "steps": c.get("steps", [])}
            for c in data.get("chains", []) or []
            if isinstance(c, dict)
        ],
    }


def format_route_guide(guide: dict) -> str:
    if not guide:
        return ""
    lines = ["Composing a route plan:"]
    lines += [f"- {r}" for r in guide.get("composition_rules", [])]
    if guide.get("step_signals"):
        lines.append("Step signals (job -> router):")
        lines += [f"- {x['signal']} -> {x['router']}" for x in guide["step_signals"]]
    if guide.get("plans"):
        lines.append("Known plans:")
        lines += [f"- {x['when']}: {' > '.join(x['steps'])}" for x in guide["plans"]]
    return "\n".join(lines)


def load_handoffs() -> dict:
    try:
        data = json.loads(ROUTES_JSON.read_text(encoding="utf-8"))
        return {k: v.get("handoff", []) for k, v in data.get("routers", {}).items()}
    except (OSError, json.JSONDecodeError, AttributeError):
        return {}


def static_chain(prompt: str, router: str, handoffs: dict) -> list:
    padded = f" {prompt.lower()} "
    if any(m in padded for m in MULTI_INTENT_MARKERS):
        nxt = handoffs.get(router) or []
        if nxt:
            return [router, nxt[0]]
    return [router]


def normalize_prediction(value) -> tuple:
    """Return (router, chain) from a string or {"router","chain"} prediction."""
    if isinstance(value, str):
        return value, [value]
    if isinstance(value, dict):
        chain = value.get("chain")
        router = value.get("router") or (chain[0] if isinstance(chain, list) and chain else None)
        if not isinstance(chain, list) or not chain:
            chain = [router] if router else None
        return router, chain
    return None, None


def chain_scores(expected: list, got, acceptable: list | None = None) -> tuple:
    """(exact, prefix) booleans; prefix compares the first min(2, len) steps.

    `acceptable` holds alternative chains (eval `acceptable_chains`) that also
    count as correct for genuinely contested prompts.
    """
    if not got:
        return False, False
    got = list(got)
    exact = prefix = False
    for chain in [expected] + [c for c in (acceptable or []) if isinstance(c, list) and c]:
        n = min(2, len(chain))
        exact = exact or got == list(chain)
        prefix = prefix or got[:n] == list(chain)[:n]
    return exact, prefix


# --------------------------------------------------------------------------
# claude mode
# --------------------------------------------------------------------------

def build_menu(routers: list, route_guide: bool = True) -> str:
    hints = load_route_hints()
    lines = []
    for r in routers:
        line = f"- {r.name}: {r.description}"
        h = hints.get(r.name)
        if h and h["next"]:
            line += f" [next: {', '.join(h['next'])}]"
        if h and h["companions"]:
            line += " [companions: " + "; ".join(
                f"{c['name']} when {c['signal']}" for c in h["companions"]
            ) + "]"
        lines.append(line)
    if route_guide:
        guide_text = format_route_guide(load_route_guide())
        if guide_text:
            lines += ["", guide_text]
    return "\n".join(lines)


def ask_claude(
    prompt: str, menu: str, model: str, timeout: int, claude_bin: str | None = None
) -> tuple | None:
    claude_prompt = (
        "You are a router that picks exactly one workflow skill for a coding "
        "agent to load, given a user request.\n\n"
        "Available routers (name: description):\n"
        f"{menu}\n\n"
        f'User request: "{prompt}"\n\n'
        "Pick the router to load FIRST. If the request clearly spans several "
        "routers, give the whole route plan of at most 3 routers in order. "
        "[next: ...] lists usual follow-on routers; include one only if the request "
        "asks for that job too. [companions: ...] run inside a step and are never "
        "chain steps. "
        "Reply with ONE line only: routers separated by ' > ' "
        "(e.g. routr-debug > routr-ship > routr-deploy; a single router is just routr-debug). "
        "No explanation, nothing else."
    )
    try:
        result = subprocess.run(
            claude_command(claude_bin) + ["-p", "--model", model],
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
    for line in out.splitlines():
        names = re.findall(r"\broutr-[a-z-]+\b", line)
        if names:
            return names[0], names
    return None


def pick_claude_batch(
    prompts: list, routers: list, model: str, concurrency: int, timeout: int, route_guide: bool = True,
    claude_bin: str | None = None,
) -> dict:
    menu = build_menu(routers, route_guide=route_guide)
    results = {}
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
        futures = {
            ex.submit(ask_claude, p, menu, model, timeout, claude_bin): p for p in prompts
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
# host mode: what a real Claude Code session does
# --------------------------------------------------------------------------

HOST_PREFLIGHT_PROMPT = "Reply with only the word: ok"


def claude_command(claude_bin: str | None = None) -> list:
    """argv prefix for the claude CLI. A `.py` path runs under this Python."""
    path = claude_bin or shutil.which("claude") or "claude"
    if claude_bin and Path(claude_bin).exists():
        path = str(Path(claude_bin).resolve())  # sessions run with cwd=sandbox, so no relative paths
    if str(path).lower().endswith(".py"):
        return [sys.executable, str(path)]
    return [str(path)]


def normalize_skill_name(raw) -> str | None:
    """'/routr:routr-debug args' -> 'routr-debug'."""
    if not isinstance(raw, str):
        return None
    tokens = raw.strip().lstrip("/").split()
    if not tokens:
        return None
    return tokens[0].rsplit(":", 1)[-1].strip() or None


def skill_name_from_input(tool_input) -> str | None:
    """Skill name from a Skill tool_use input; the key is not verified, so be liberal."""
    if not isinstance(tool_input, dict):
        return None
    for key in ("skill", "name", "command"):
        name = normalize_skill_name(tool_input.get(key))
        if name:
            return name
    return None


@dataclass
class HostParse:
    saw_init: bool = False
    skills_seen: int | None = None
    routr_seen: int | None = None
    model: str | None = None
    invoked: list = field(default_factory=list)  # every Skill invocation, in order
    error: str | None = None


def parse_host_stream(lines) -> HostParse:
    """Parse `claude -p --output-format stream-json --verbose` output (one JSON event per line).

    The init event need not be first (hook events can precede it). Unparseable
    lines are ignored.
    """
    out = HostParse()
    seen_tool_ids = set()
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(ev, dict):
            continue
        etype = ev.get("type")
        if etype == "system" and ev.get("subtype") == "init" and not out.saw_init:
            out.saw_init = True
            names = []
            for s in ev.get("skills") or []:
                n = normalize_skill_name(s.get("name") if isinstance(s, dict) else s)
                if n:
                    names.append(n)
            out.skills_seen = len(names)
            out.routr_seen = sum(1 for n in names if n.startswith("routr-"))
            out.model = ev.get("model")
        elif etype == "assistant":
            if ev.get("error") and not out.error:
                out.error = str(ev["error"])
            content = (ev.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if not (isinstance(block, dict) and block.get("type") == "tool_use"
                        and block.get("name") == "Skill"):
                    continue
                tid = block.get("id")
                if tid:
                    if tid in seen_tool_ids:
                        continue
                    seen_tool_ids.add(tid)
                name = skill_name_from_input(block.get("input"))
                if name:
                    out.invoked.append(name)
        elif etype == "result":
            if ev.get("is_error") and not out.error:
                out.error = str(ev.get("result") or ev.get("subtype") or "error")
    return out


@dataclass
class HostResult:
    router: str | None
    chain: list | None
    reason: str | None = None  # why router is None: no-skill | no-situational | error
    via_router: bool = False
    routr_invoked: list = field(default_factory=list)
    other_skills: list = field(default_factory=list)
    skills_seen: int | None = None
    routr_seen: int | None = None
    error: str | None = None


def interpret_host(parse: HostParse, situational: set) -> HostResult:
    """Turn a parsed stream into the router/chain the session actually chose.

    Chain = situational routr-* skills in invocation order, de-duplicated.
    routr-router, routr-catalog and routr-depth-* are recorded but are not
    chain steps; `via_router` is set when routr-router was the first routr
    skill invoked.
    """
    routr = []
    for n in parse.invoked:
        if n.startswith("routr-") and n not in routr:
            routr.append(n)
    others = []
    for n in parse.invoked:
        if not n.startswith("routr-") and n not in others:
            others.append(n)
    chain = [n for n in routr if n in situational]
    res = HostResult(
        router=chain[0] if chain else None,
        chain=chain or None,
        via_router=bool(routr) and routr[0] == "routr-router",
        routr_invoked=routr,
        other_skills=others,
        skills_seen=parse.skills_seen,
        routr_seen=parse.routr_seen,
        error=parse.error,
    )
    if not chain:
        if parse.error and not routr:
            res.reason = "error"
        elif routr:
            res.reason = "no-situational"
        else:
            res.reason = "no-skill"
    return res


def build_host_sandbox(noise_dir: Path | None = None) -> tuple:
    """Temp project with .claude/skills = every repo routr-* skill (+ noise). Returns (path, noise_count)."""
    import tempfile
    sandbox = Path(tempfile.mkdtemp(prefix="routr-host-"))
    skills = sandbox / ".claude" / "skills"
    skills.mkdir(parents=True)
    for d in sorted(SKILLS_DIR.glob("routr-*")):
        if d.is_dir():
            shutil.copytree(d, skills / d.name)
    noise = 0
    if noise_dir:
        for d in sorted(Path(noise_dir).iterdir()):
            if d.is_dir() and not d.name.startswith("routr-") and not (skills / d.name).exists():
                shutil.copytree(d, skills / d.name)
                noise += 1
    return sandbox, noise


def host_command(claude_bin: str | None, host_env: str, max_turns: int, model: str | None) -> list:
    cmd = claude_command(claude_bin) + [
        "-p",
        "--output-format", "stream-json",
        "--verbose",
        "--no-session-persistence",
        "--tools", "Skill",
        # --tools limits only built-in tools; without this, MCP servers from
        # user settings or plugins stay callable in --host-env user.
        "--strict-mcp-config",
        "--settings", '{"disableAllHooks": true}',
        "--permission-mode", "default",
        "--setting-sources", "user,project" if host_env == "user" else "project",
        "--max-turns", str(max_turns),
    ]
    if model:
        cmd += ["--model", model]
    return cmd


def run_host_session(prompt: str, sandbox: Path, cmd: list, timeout: int) -> HostParse:
    """Run one fresh session in the sandbox. A failure is recorded in .error, never raised."""
    try:
        proc = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout, cwd=str(sandbox),
        )
    except subprocess.TimeoutExpired:
        return HostParse(error=f"timeout after {timeout}s")
    except (FileNotFoundError, OSError) as exc:
        return HostParse(error=f"could not run claude CLI: {exc}")
    parse = parse_host_stream((proc.stdout or "").splitlines())
    if proc.returncode != 0 and not parse.error:
        detail = ((proc.stderr or proc.stdout or "").strip().splitlines() or ["no output"])[0]
        parse.error = f"claude exited {proc.returncode}: {detail[:200]}"
    return parse


def pick_host_batch(
    prompts: list, sandbox: Path, cmd: list, situational: set, concurrency: int, timeout: int
) -> dict:
    results = {}
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
        futures = {
            ex.submit(run_host_session, p, sandbox, cmd, timeout): p for p in dict.fromkeys(prompts)
        }
        for fut in as_completed(futures):
            p = futures[fut]
            try:
                results[p] = interpret_host(fut.result(), situational)
            except Exception as exc:  # pragma: no cover - defensive
                print(f"  ! error running prompt: {exc}", file=sys.stderr)
                results[p] = HostResult(None, None, reason="error", error=str(exc))
    return results


def summarize_host(host_results: list) -> dict:
    """Aggregate per-prompt host dicts (results[].host) for the report."""
    seen = [h["skills_seen"] for h in host_results if h.get("skills_seen") is not None]
    other: dict = {}
    for h in host_results:
        for s in h.get("other_skills") or []:
            other[s] = other.get(s, 0) + 1
    top = sorted(other.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    return {
        "prompts": len(host_results),
        "skills_visible_min": min(seen) if seen else None,
        "skills_visible_max": max(seen) if seen else None,
        "no_routr_skill": sum(1 for h in host_results if h.get("reason") in ("no-skill", "error")),
        "no_skill": sum(1 for h in host_results if h.get("reason") == "no-skill"),
        "errors": sum(1 for h in host_results if h.get("reason") == "error"),
        "via_router": sum(1 for h in host_results if h.get("via_router")),
        "other_skills_top": [{"skill": k, "prompts": v} for k, v in top],
    }


def host_preflight(cmd: list, sandbox: Path, timeout: int) -> str | None:
    """Return an error message when a session cannot run (signed out, bad CLI), else None."""
    parse = run_host_session(HOST_PREFLIGHT_PROMPT, sandbox, cmd, timeout)
    if parse.error:
        return (
            f"claude CLI preflight failed: {parse.error}\n"
            "Run `claude` interactively to sign in, then retry."
        )
    if not parse.saw_init:
        return (
            "claude CLI preflight failed: no init event in the stream-json output "
            "(is this a claude CLI that supports --output-format stream-json --verbose?)"
        )
    return None


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    cleanup: list = []
    try:
        return _main(cleanup)
    finally:
        for fn in cleanup:
            fn()


def _main(cleanup: list) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--mode", choices=["static", "claude", "predictions", "host"], default="static")
    parser.add_argument(
        "--model", default=None,
        help=f"model for --mode claude (default {DEFAULT_MODEL}) and --mode host (default: the CLI's own default)",
    )
    parser.add_argument("--concurrency", type=int, default=4, help="parallel claude -p calls")
    parser.add_argument(
        "--timeout", type=int, default=None,
        help="per-call timeout in seconds (default 60 for --mode claude, 180 for --mode host)",
    )
    parser.add_argument("--claude-bin", dest="claude_bin", default=None,
                        help="claude CLI to run (default: `claude` on PATH; a .py path runs under this Python)")
    parser.add_argument("--host-env", dest="host_env", choices=["isolated", "user"], default="isolated",
                        help="--mode host: isolated = only the sandbox's project skills; "
                        "user = also your installed ~/.claude skills")
    parser.add_argument("--noise-dir", dest="noise_dir", default=None,
                        help="--mode host: copy every non-routr-* skill folder from this directory into the "
                        "sandbox to simulate a crowded skill list")
    parser.add_argument("--max-turns", dest="max_turns", type=int, default=3,
                        help="--mode host: --max-turns passed to each session (default 3)")
    parser.add_argument("--keep-sandbox", dest="keep_sandbox", action="store_true",
                        help="--mode host: do not delete the temp sandbox afterwards (for debugging)")
    parser.add_argument("--file", help="run only this eval file")
    parser.add_argument(
        "--no-route-guide",
        action="store_true",
        help="omit routes.json composition rules, step signals and plans from model-facing menus (ablation)",
    )
    parser.add_argument("--json", dest="json_path", help="write machine-readable results here")
    parser.add_argument("--min-accuracy", type=float, default=None, help="exit 1 if overall accuracy is below this")
    parser.add_argument(
        "--export-prompts",
        dest="export_prompts",
        help="write {menu, prompts} JSON (no expected answers) for every scorable "
        "prompt and exit, for scoring by an external model (respects --file)",
    )
    parser.add_argument(
        "--predictions",
        dest="predictions_path",
        help="with --mode predictions: JSON file {\"<id>\": \"routr-xxx\", ...} "
        "mapping prompt ids (as produced by --export-prompts) to predicted routers",
    )
    args = parser.parse_args()
    if args.mode == "claude" and not args.model:
        args.model = DEFAULT_MODEL
    if args.timeout is None:
        args.timeout = 180 if args.mode == "host" else 60

    if args.mode == "predictions" and not args.predictions_path:
        print("--mode predictions requires --predictions PATH", file=sys.stderr)
        return 2

    routers = load_candidate_routers()
    if not routers:
        print("No candidate routers found under skills/routr-*", file=sys.stderr)
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

    if args.export_prompts:
        hints = load_route_hints()
        menu = [
            {
                "name": r.name,
                "description": r.description,
                "next": hints.get(r.name, {}).get("next", []),
                "companions": hints.get(r.name, {}).get("companions", []),
            }
            for r in routers
        ]
        export_prompts = []
        for ef in eval_files:
            try:
                data = json.loads(ef.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                print(f"SKIP {ef}: invalid JSON ({exc})", file=sys.stderr)
                continue
            prompts = data.get("prompts", [])
            for i, p in enumerate(prompts):
                if isinstance(p, dict) and p.get("expected_router"):
                    export_prompts.append({"id": f"{ef.name}#{i}", "prompt": p["prompt"]})
        Path(args.export_prompts).write_text(
            json.dumps(
                {
                    "instructions": EXPORT_INSTRUCTIONS,
                    "menu": menu,
                    **({} if args.no_route_guide else {"route_guide": load_route_guide()}),
                    "prompts": export_prompts,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"Wrote {len(export_prompts)} prompt(s) and a {len(menu)}-router menu to {args.export_prompts}")
        return 0

    predictions_by_id: dict = {}
    if args.mode == "predictions":
        try:
            raw = json.loads(Path(args.predictions_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Could not read --predictions {args.predictions_path}: {exc}", file=sys.stderr)
            return 2
        # Models often return a list of {"id", "router", "chain"} records
        # instead of an id-keyed object; accept both.
        if isinstance(raw, list) and all(isinstance(r, dict) and "id" in r for r in raw):
            raw = {r["id"]: {k: v for k, v in r.items() if k != "id"} for r in raw}
        if not isinstance(raw, dict):
            print(
                f"--predictions {args.predictions_path} must be a JSON object of "
                "id -> router name or {router, chain}, or a list of {id, router, chain}",
                file=sys.stderr,
            )
            return 2
        predictions_by_id = raw

    if args.mode == "claude":
        # Preflight: a signed-out or broken CLI would otherwise score every
        # prompt as a silent miss (got=None).
        try:
            probe = subprocess.run(
                claude_command(args.claude_bin) + ["-p", "--model", args.model],
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

    host_sandbox = None
    host_cmd: list = []
    host_noise = 0
    situational = {r.name for r in routers}
    if args.mode == "host":
        noise_dir = None
        if args.noise_dir:
            noise_dir = Path(args.noise_dir)
            if not noise_dir.is_dir():
                print(f"--noise-dir {args.noise_dir} is not a directory", file=sys.stderr)
                return 2
        host_sandbox, host_noise = build_host_sandbox(noise_dir)
        if not args.keep_sandbox:
            cleanup.append(lambda: shutil.rmtree(host_sandbox, ignore_errors=True))
        host_cmd = host_command(args.claude_bin, args.host_env, args.max_turns, args.model)
        problem = host_preflight(host_cmd, host_sandbox, args.timeout)
        if problem:
            print(problem, file=sys.stderr)
            return 2

    all_results = []
    total_scored = 0
    total_correct = 0
    total_skipped = 0
    total_violations = 0
    total_chain = 0
    chain_exact = 0
    chain_prefix = 0
    handoffs = load_handoffs()
    misses = []
    chain_misses = []

    per_file_rows = []

    for ef in eval_files:
        try:
            data = json.loads(ef.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"SKIP {ef}: invalid JSON ({exc})")
            continue

        prompts = data.get("prompts", [])
        scorable = [(i, p) for i, p in enumerate(prompts) if isinstance(p, dict) and p.get("expected_router")]
        skipped = len(prompts) - len(scorable)
        total_skipped += skipped

        if not scorable:
            per_file_rows.append((ef.name, 0, 0, skipped, 0))
            continue

        if args.mode == "static":
            predictions = {}
            for i, p in scorable:
                pred, _scores = pick_static(p["prompt"], routers)
                predictions[i] = (pred, static_chain(p["prompt"], pred, handoffs))
        elif args.mode == "claude":
            by_prompt_text = pick_claude_batch(
                [p["prompt"] for _, p in scorable], routers, args.model, args.concurrency, args.timeout,
                    route_guide=not args.no_route_guide, claude_bin=args.claude_bin,
            )
            predictions = {i: by_prompt_text.get(p["prompt"]) for i, p in scorable}
        elif args.mode == "host":
            by_prompt_text = pick_host_batch(
                [p["prompt"] for _, p in scorable], host_sandbox, host_cmd, situational,
                args.concurrency, args.timeout,
            )
            host_by_index = {i: by_prompt_text[p["prompt"]] for i, p in scorable}
            predictions = {i: (h.router, h.chain) for i, h in host_by_index.items()}
        else:  # predictions
            predictions = {
                i: (normalize_prediction(predictions_by_id[f"{ef.name}#{i}"])
                    if f"{ef.name}#{i}" in predictions_by_id else None)
                for i, p in scorable
            }

        file_correct = 0
        file_violations = 0
        for i, p in scorable:
            expected = p["expected_router"]
            got, got_chain = predictions.get(i) or (None, None)
            host = host_by_index[i] if args.mode == "host" else None
            must_not_load = set(p.get("must_not_load", []) or [])
            acceptable = {expected} | set(p.get("acceptable_routers", []) or [])
            hit = got in acceptable
            expected_chain = p.get("expected_chain")
            exact = prefix = None
            if isinstance(expected_chain, list) and expected_chain:
                exact, prefix = chain_scores(expected_chain, got_chain, p.get("acceptable_chains"))
                total_chain += 1
                chain_exact += int(exact)
                chain_prefix += int(prefix)
            violation = got in must_not_load if got else False
            if exact is False:
                chain_misses.append(
                    {"file": ef.name, "prompt": p["prompt"], "expected": expected_chain, "got": got_chain}
                )

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
                        **({"reason": host.reason} if host and host.reason else {}),
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
                    "acceptable_routers": p.get("acceptable_routers"),
                    "expected_chain": expected_chain,
                    "predicted_chain": got_chain,
                    "chain_exact": exact,
                    "chain_prefix": prefix,
                    "must_not_load_violation": violation,
                    "boundary": p.get("boundary"),
                    **({"host": asdict(host)} if host else {}),
                }
            )

        total_scored += len(scorable)
        total_correct += file_correct
        total_violations += file_violations
        per_file_rows.append((ef.name, file_correct, len(scorable), skipped, file_violations))

    # ---- report ----
    if args.mode == "host":
        print(f"Mode: host (env={args.host_env}, model={args.model or 'CLI default'}, "
              f"max-turns={args.max_turns}, noise skills={host_noise})")
        if args.keep_sandbox:
            print(f"Sandbox kept at: {host_sandbox}")
    else:
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
    if total_chain:
        print(
            f"Chain exact-match:  {chain_exact}/{total_chain} ({chain_exact / total_chain * 100:.1f}%)"
            f"  (prompts with expected_chain)"
        )
        print(f"Chain prefix-match: {chain_prefix}/{total_chain} ({chain_prefix / total_chain * 100:.1f}%)")
    print(f"Prompts skipped (no expected_router): {total_skipped}")
    print(f"must_not_load violations: {total_violations}")

    host_summary = None
    host_rows = [r["host"] for r in all_results if r.get("host")]
    if args.mode == "host" and host_rows:
        host_summary = summarize_host(host_rows)
        n = host_summary["prompts"]
        lo, hi = host_summary["skills_visible_min"], host_summary["skills_visible_max"]
        print()
        print("Host session details:")
        if lo is None:
            print("  Skills visible to the agent: unknown (no init event)")
        else:
            print(f"  Skills visible to the agent: min {lo}, max {hi} (per prompt)")
        print(f"  No ROUTR skill invoked: {host_summary['no_routr_skill']}/{n} "
              f"({host_summary['no_routr_skill'] / n * 100:.1f}%)"
              + (f", of which {host_summary['errors']} errored" if host_summary["errors"] else ""))
        print(f"  Routed via routr-router: {host_summary['via_router']}/{n} "
              f"({host_summary['via_router'] / n * 100:.1f}%)")
        if host_summary["other_skills_top"]:
            print("  Other skills invoked instead (top 5, by prompts): "
                  + ", ".join(f"{o['skill']} x{o['prompts']}" for o in host_summary["other_skills_top"]))
        else:
            print("  Other skills invoked instead: none")

    if chain_misses:
        print()
        print("Chain misses:")
        for m in chain_misses:
            got_txt = " > ".join(m["got"]) if m["got"] else None
            print(f"  - {m['file']}: \"{m['prompt']}\" expected={' > '.join(m['expected'])} got={got_txt}")

    if misses:
        print()
        print("Misses:")
        for m in misses:
            boundary = f" [boundary: {m['boundary']}]" if m.get("boundary") else ""
            reason = f" [{m['reason']}]" if m.get("reason") else ""
            print(f"  - {m['file']}: \"{m['prompt']}\" expected={m['expected']} got={m['got']}{reason}{boundary}")

    if args.json_path:
        Path(args.json_path).write_text(
            json.dumps(
                {
                    "mode": args.mode,
                    "model": args.model if args.mode in ("claude", "host") else None,
                    **(
                        {"host_env": args.host_env, "noise_skills": host_noise, "max_turns": args.max_turns,
                         "host": host_summary}
                        if args.mode == "host" else {}
                    ),
                    "overall_accuracy": overall_acc,
                    "total_scored": total_scored,
                    "total_correct": total_correct,
                    "total_skipped": total_skipped,
                    "total_violations": total_violations,
                    "chain_scored": total_chain,
                    "chain_exact": chain_exact,
                    "chain_prefix": chain_prefix,
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
