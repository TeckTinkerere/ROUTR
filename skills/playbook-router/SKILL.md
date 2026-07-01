---
name: playbook-router
description: >
  Meta-router for situational agent workflows. Use when the task type is unclear,
  the user asks which approach to take, or multiple playbooks could apply. Routes to
  debugging-playbook, fix-and-ship-playbook, explore-codebase-playbook,
  library-integration-playbook, agent-design-playbook, frontend-feature-playbook,
  or frontend-motion-playbook. Prefer a specific playbook over this when the
  situation is obvious.
---

# Playbook router

Pick **one** playbook, announce it in one line, then read and follow that playbook's `SKILL.md` exclusively.

## Decision tree

```
User intent?
├─ Bug / error / crash / "why does X fail?"     → debugging-playbook
├─ "Fix this" / patch / make tests pass         → fix-and-ship-playbook
├─ "How does X work?" / onboard / architecture  → explore-codebase-playbook
├─ Library API / "how do I use Prisma/Next…"    → library-integration-playbook
├─ Build agent / multi-agent / context design   → agent-design-playbook
├─ New page / UI / component / landing / design → frontend-feature-playbook
└─ Animate / motion / scroll / micro-interaction → frontend-motion-playbook
```

## Frontend detection

Treat as **frontend** when the work touches: `.tsx`, `.jsx`, `.vue`, `.svelte`, CSS/Tailwind, design tokens, layout, components, pages, or the user mentions UI/UX/design.

- Building or redesigning UI → `frontend-feature-playbook`
- UI exists; add/polish motion only → `frontend-motion-playbook`
- Frontend bug → `debugging-playbook` (it will pull design context if needed)

## After routing

1. Read `playbook-common/references/resolution.md` if child skills may be missing.
2. Load the chosen playbook skill from skills root (see resolution.md).
3. Do not load unrelated playbooks in parallel.

## Quick reference

| Playbook | Trigger words |
|----------|----------------|
| `debugging-playbook` | debug, trace, root cause, error, failing, broken |
| `fix-and-ship-playbook` | fix, patch, ship, commit, PR, tests green |
| `explore-codebase-playbook` | how does, explain, architecture, where is |
| `library-integration-playbook` | docs for, API, migrate, configure library |
| `agent-design-playbook` | agent system, harness, eval, context window |
| `frontend-feature-playbook` | build UI, page, component, redesign, landing |
| `frontend-motion-playbook` | animate, motion, framer, scroll reveal, transition |
