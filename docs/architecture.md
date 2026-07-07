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

Single entry: `routr-video` with `references/launch.md` and `references/remotion.md`. Old `video-*-playbook` folders were removed in v2.

## Naming

All ROUTR-owned skills use `routr-` prefix. See [naming.md](naming.md). Old `*-playbook` names were removed in v2 (see the rename map).

## Progressive disclosure

Top routers include `references/` (workflow, fallback, gotchas, examples, boundaries). Keep `SKILL.md` ≤150 lines.

## Quality loop

Eval prompts in `evals/` for `routr-router`, `routr-debug`, `routr-frontend`. Run before releases.

## Compatibility

Works anywhere the [Agent Skills](https://skills.sh) format is supported: Cursor, Claude Code, Codex, Kiro, OpenCode, Windsurf, and 70+ agents via `npx skills add`.

## Authoring new routers

See [authoring.md](authoring.md):

1. Name: `routr-{domain}`
2. Register in `routr-router`
3. Add row to `skill-registry.md`
4. Add `references/` if overlaps siblings
