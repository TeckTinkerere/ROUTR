# Architecture

## Problem

Installing dozens of agent skills creates **discovery noise**: the model picks the wrong skill, loads too many at once, or skips the right workflow order.

## Solution

**Router skills** (playbooks) are thin `SKILL.md` files that:

1. Match a **situation** (debug, ship, frontend, motion, …)
2. **Order** child skills to read
3. **Skip** irrelevant skills explicitly
4. Point to a **catalog** for installing missing dependencies

Routers do **not** duplicate child skill content — they preserve progressive disclosure.

## Layers

```
┌─────────────────────────────────────────────────────────────┐
│  playbook-router          Meta: pick a situation            │
├─────────────────────────────────────────────────────────────┤
│  Situational playbooks    debug | fix | explore | …         │
├─────────────────────────────────────────────────────────────┤
│  Child skills             symdex, lean-ctx, frontend-design │
│  (installed separately)   framer-motion, context-fundamentals│
└─────────────────────────────────────────────────────────────┘
```

## Frontend stack

Two playbooks split UI work:

| Playbook | Scope |
|----------|--------|
| `frontend-feature-playbook` | Layout, typography, components, design system |
| `frontend-motion-playbook` | Framer Motion, scroll, micro-interactions, review |

Child skills include Anthropic `frontend-design`, `ui-ux-pro-max`, `shadcn`, Tailwind design system, and motion skills (`framer-motion-animator`, `review-animations`, Lottie `motion-design`).

## Compatibility

Works anywhere the [Agent Skills](https://skills.sh) format is supported: Cursor, Claude Code, Codex, Kiro, OpenCode, Windsurf, and 70+ agents via `npx skills add`.

## Authoring new playbooks

1. Copy an existing `skills/*-playbook/SKILL.md`
2. Write a description with **WHAT** + **WHEN** (third person)
3. List child skills in order with skip rules
4. Add entries to `skills/playbook-common/references/skill-catalog.md`
5. Register in `playbook-router` decision tree
