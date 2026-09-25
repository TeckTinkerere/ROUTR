# Architecture

## Problem

Installing dozens of agent skills creates **discovery noise**: the model picks the wrong skill, loads too many at once, or skips the right workflow order. When child skills are missing, thin routers feel weak.

## Solution

**ROUTR v2** uses standardized `routr-*` router skills that:

1. Match a **situation** (debug, ship, frontend, motion, …)
2. **Order** child skills to read (canonical names from registry)
3. **Skip** irrelevant skills explicitly
4. **Fallback** via `routr-depth-*` or `references/fallback.md` when children missing
5. Point to **`routr-catalog`** for install bundles and aliases

Routers route. They do not replace child skills — but they stay useful without them.

## Layers

```
┌─────────────────────────────────────────────────────────────┐
│  routr-router             Meta: pick a situation            │
├─────────────────────────────────────────────────────────────┤
│  routr-* routers          debug | ship | frontend | …       │
│  routr-depth-*            Fallback when child missing       │
├─────────────────────────────────────────────────────────────┤
│  routr-catalog            Registry, bundles, resolution     │
├─────────────────────────────────────────────────────────────┤
│  Child skills             frontend-design, systematic-debug │
│  (installed separately)   ai-sdk, symdex, lean-ctx, …      │
└─────────────────────────────────────────────────────────────┘
```

## Two-layer model

| Layer | Role | Example |
|-------|------|---------|
| ROUTR routers | Situation → ordered children + iron laws | `routr-debug` |
| Child skills | Domain depth | `systematic-debugging`, `frontend-design` |
| Depth fallbacks | Minimum expertise if child not installed | `routr-depth-debug` |

**ROUTR without child bundles feels weak** — install `routr-bundle-core` / `routr-bundle-frontend` from [skill-registry.md](../skills/routr-catalog/references/skill-registry.md).

## Frontend stack

| Router | Scope |
|--------|--------|
| `routr-frontend` | Layout, typography, components, design system |
| `routr-motion` | Framer Motion, scroll, micro-interactions |

## Video stack (v2)

Single entry: `routr-video`. It routes on two axes:

- **Workflow** — owns the deliverable end to end (`brag`, `product-launch-video`, `pr-to-video`, `website-to-video`, `faceless-explainer`, `motion-graphics`, `music-to-video`, `talking-head-recut`, `embedded-captions`, `slideshow`, `general-video`, or a Remotion project). Exactly one per task.
- **Capability layer** — pulled in mid-flight, never owns the task (`media-use`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-creative`, `hyperframes-registry`). Several per task is normal.

References: `launch.md`, `product-marketing.md`, `data-video.md`, `remotion.md`, `hyperframes.md`, `media.md`, plus the standard fallback/gotchas/examples/boundaries set. Old `video-*-playbook` folders were removed in v2.

## Naming

All ROUTR-owned skills use `routr-` prefix. See [naming.md](naming.md). Old `*-playbook` names were removed in v2 (see the rename map).

## Progressive disclosure

Top routers include `references/` (workflow, fallback, gotchas, examples, boundaries). Keep `SKILL.md` ≤150 lines.

## Quality loop

Two mechanical gates run before release, both callable from CI:

**Validator** (`scripts/validate-skills.sh`), 11 checks:

1. Frontmatter `name:` matches folder name
2. Router description contains `Use when:`
3. Every backticked child-skill reference resolves to a `skill-registry.md` row (canonical name or alias)
4. No duplicate canonical rows in the registry
5. Every situational router is listed in `routr-router`'s decision tree and `resolution.md`'s precedence list
6. Description ≤ 320 chars (FAIL), > 280 chars (WARN)
7. Situational routers include `Not for:` (FAIL); depth/catalog skills exempt
8. `SKILL.md` ≤ 150 lines for routers, ≤ 200 lines for `routr-depth-*` (FAIL)
9. Every relative markdown link under `skills/**.md` resolves to a real file (FAIL)
10. Every `evals/*.eval.json` parses, and every `expected_router`/`expected_chain`/`must_not_load` entry names an existing `skills/routr-*` folder (FAIL)
11. Every situational router has at least one eval prompt as `expected_router` somewhere in `evals/` (WARN)

**Eval runner** (`scripts/run-evals.py`, stdlib only): builds the router menu from each `SKILL.md` frontmatter, then scores every prompt in `evals/`.

- `--mode static` (default): offline, deterministic — a lexical scorer over `Use when:` triggers minus `Not for:` phrases. A smoke test for description overlap, no model call.
- `--mode claude`: shells out to `claude -p --model <model>` with the router menu + prompt, parses the chosen router, scores against `expected_router`/`expected_chain`.
- Reports accuracy per file, per-boundary failures, and `must_not_load` violations. `--json` for machine output; non-zero exit under `--min-accuracy` gates CI.

Evals in `evals/` now cover every situational router (one `*.eval.json` file per router, plus `routr-router` for cross-cutting chain tests) — not just the original three.

## Compatibility

Works anywhere the [Agent Skills](https://skills.sh) format is supported: Cursor, Claude Code, Codex, Kiro, OpenCode, Windsurf, and 70+ agents via `npx skills add`.

## Authoring new routers

See [authoring.md](authoring.md):

1. Name: `routr-{domain}`
2. Register in `routr-router`
3. Add row to `skill-registry.md`
4. Add `references/` if overlaps siblings
