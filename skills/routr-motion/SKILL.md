---
name: routr-motion
description: "Add or polish animations (Framer Motion, scroll, transitions). Use when: animate, motion, micro-interactions on UI that already exists. Not for: building new pages or components (→ routr-frontend)."
---

# routr-motion

**Goal:** intentional, performant, accessible motion.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Skill | When |
|-------|------|
| `framer-motion-animator` | React + Framer Motion |
| `review-animations` | Pre-ship critique |
| `motion-design` | Staging principles |
| `ui-animation` | CSS motion |
| `frontend-design` | Motion serves page thesis |
| `find-docs` | Motion.dev API version |

## 1. Audit

What moves? Entry triggers? `prefers-reduced-motion` upfront.

## 2. Implement

`useReducedMotion()` mandatory. Stagger; one focal animation per viewport.

## 3. Review pass

`review-animations` — purpose, jank, mobile, reduced motion.

## Handoff

- Page from scratch → `routr-frontend` first
- Jank debug → `routr-debug`

## Anti-patterns

- Parallax everywhere
- No reduced-motion guard
- Copy-paste snippets without purpose
