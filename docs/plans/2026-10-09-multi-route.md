# ROUTR — multi-route routing and open-source readiness (2026-10-09)

Branch: `feat/exploring-and-implementing-new-stuff`. This builds on [2026-09-25-routr-v2.1.md](2026-09-25-routr-v2.1.md).

## Why

- **Real requests span several routers.** "Fix the 500 and ship it to prod" needs debug → ship → deploy. Today chains live in prose tables in `routr-router`, and nothing measures whether an agent plans them.
- **Some evals have more than one right answer.** "Build a whole new onboarding flow with three screens" missed in all 4 blind runs because it legitimately starts at plan *or* frontend.
- **Domain failures go to `routr-debug` when the domain router knows better.** Examples: "agent loop drifting", "useChat stuck loading".
- **The repo is missing what makes contributing easy:** no CONTRIBUTING guide, issue templates, changelog or line-ending policy, and no way for users to report a misroute.

## Design

### 1. Route plans: one router active, the whole route announced upfront

The iron law stays: **one router active at a time.** What changes is that the agent plans the full route before starting and re-checks it at each handoff.

```
ROUTR plan: routr-debug → routr-ship → routr-deploy
Now: routr-debug — 500 on checkout, root cause unknown
Next: routr-ship once root cause is fixed and verified
```

Rules:
- A plan has at most 3 steps. Anything longer goes to `routr-plan` first.
- Each step has an **exit condition**: the point where the agent hands off and re-routes.
- Mid-task, the user can say "skip", "stop after debug" or "just ship".
- When a step ends, check the next step still applies. If it doesn't, drop it.

### 2. Companions: a second router's checklist, not a second owner

A **companion** contributes one checklist section to the active router without taking over the task. At most one companion runs per step, and it starts only on a named signal:

| Active | Companion | Signal |
|--------|-----------|--------|
| `routr-ship` | `routr-security` | diff touches auth, sessions, RLS, secrets, payments |
| `routr-frontend` | `routr-perf` | stated perf budget, LCP/INP complaint, heavy media |
| `routr-ai` | `routr-agents` | output-quality scoring or an eval harness |
| `routr-database` | `routr-security` | RLS policies, grants, multi-tenant data |
| `routr-deploy` | `routr-qa` | the user asks to verify the deployed preview |
| `routr-mobile` | `routr-perf` | jank, slow startup, list performance |

The companion reads only the section its `routes.json` entry names. It never runs bootstrap, and it never loads its own children.

### 3. `routes.json`: the machine-readable source of truth

The file is `skills/routr-catalog/references/routes.json`:

```json
{
  "version": 1,
  "max_chain": 3,
  "routers": {
    "routr-debug": {
      "handoff": ["routr-ship"],
      "companions": [],
      "owns_domain_failures": false
    }
  },
  "companions": [
    {
      "active": "routr-ship",
      "companion": "routr-security",
      "signal": "diff touches auth, sessions, RLS, secrets, payments",
      "section": "skills/routr-security/SKILL.md#..."
    }
  ],
  "chains": [
    {
      "id": "prod-bugfix",
      "when": "bug in production",
      "steps": ["routr-debug", "routr-ship", "routr-deploy"],
      "exits": ["root cause fixed + verified", "PR merged / commit pushed"]
    }
  ]
}
```

The validator checks that:
- every name exists;
- every situational router has an entry;
- chains are no longer than `max_chain`;
- `handoff` targets appear in that router's `## Handoff` section (WARN if not).

### 4. Tie-break: the domain's own machinery beats generic debug

If the thing failing is the domain's **own machinery**, the domain router owns it and uses its own gotchas. Examples:
- a render pipeline
- an agent loop
- an AI SDK stream
- an EAS build
- a migration runner

It hands to `routr-debug` only if the root cause turns out to be outside the domain.

If the failure is in **application logic** that merely uses the domain, it goes to `routr-debug`. Example: a query that returns the wrong rows.

This goes into `resolution.md` and the `routr-router` decision tree.

### 5. Evals understand chains and alternatives

- New `acceptable_routers` field: a prompt is a hit if the chosen router is `expected_router` or any entry in this list.
- Chain scoring: the eval modes ask for a route plan. The runner reports three numbers:
  - router accuracy
  - chain exact-match on prompts with `expected_chain`
  - chain prefix-match: the plan starts with the expected first two steps
- The predictions format accepts `"id": "routr-x"` or `"id": {"router": "routr-x", "chain": [...]}`.
- New `evals/multi-route.eval.json`: 15–20 multi-intent prompts.

### 6. Open-source readiness

- **Community files:** CONTRIBUTING, CODE_OF_CONDUCT (Contributor Covenant 2.1), SECURITY, CHANGELOG (Keep a Changelog).
- **Issue templates:** misroute report, new router proposal, bug, and a template config. Plus a PR template.
- **Line endings and release:** `.gitattributes` (LF) and `.editorconfig`, plus a release workflow that turns a `v*` tag into a GitHub Release with the changelog section.
- **README:** CI badge, a routing diagram (Mermaid), multi-route section, eval scores, contributing links.

## Verification

- `bash scripts/validate-skills.sh` passes.
- Static evals run.
- Two blind Haiku runs use `--export-prompts` and `--mode predictions`. Report router accuracy plus chain metrics.

## Results (2026-10-09)

Two blind Haiku 4.5 runs against the 176-prompt export, with a menu of descriptions only:

| Run | Router accuracy | Chain exact | Chain prefix | must_not_load violations |
|-----|-----------------|-------------|--------------|--------------------------|
| A | 173/176 (98.3%) | 21/28 (75.0%) | 23/28 (82.1%) | 1 |
| B | 172/176 (97.7%) | 21/28 (75.0%) | 22/28 (78.6%) | 1 |

`multi-route.eval.json` scored 20/20 on router choice in both runs.

The chain misses shared by both runs had three causes:
- **Handoffs not visible.** The model stopped after `routr-ai` on "streaming chat", because nothing in the menu said ai hands off to frontend.
- **Companions scored as steps.** "RAG + score answer quality" became ai → agents, though agents is ai's companion.
- **Two contested labels.** The onboarding flow, and the landing page with an embedded demo video.

Fixes made:
- Model-facing menus (`--mode claude` and `--export-prompts`) now include each router's `next` handoffs and `companions` from `routes.json`.
- Added an `acceptable_chains` eval field, checked by the validator.
- Fixed `--mode predictions` to accept a list of `{id, router, chain}` records, plus an f-string crash in its error path.

Re-measured with the richer menu:

| Run | Router accuracy | Chain exact | Chain prefix | must_not_load violations |
|-----|-----------------|-------------|--------------|--------------------------|
| C | 166/176 (94.3%) | 21/28 (75.0%) | 22/28 (78.6%) | 4 |
| D | 174/176 (98.9%) | 22/28 (78.6%) | 22/28 (78.6%) | 0 |

- The richer menu moved chain exact-match by about one prompt, which is within noise.
- Both runs routed "hero animation drops frames … then smooth it out" to `routr-motion` instead of `routr-perf`.

### Next
- **Implicit follow-on steps.** "Streaming chat" implies a UI step. Teach this with chain examples in the menu, or treat the step as optional in scoring.
- **perf vs motion.** Check this boundary when frame drops come with a request to fix them.
- **Run variance.** Run C's 94.3% shows the noise. Gate CI on the mean of three runs, never on one.
