---
name: routr-motion
description: "Add or polish animations (Framer Motion, scroll, transitions). Use when: animate, motion, micro-interactions on UI that already exists. Not for: building new pages or components (→ routr-frontend)."
---

# routr-motion

**Goal:** intentional, performant, accessible motion.

## When to activate

- Animate, motion, micro-interactions on UI that already exists

## Do not activate

- Building new pages or components → `routr-frontend`

## Iron law

**`useReducedMotion()` is mandatory — no animation ships without a reduced-motion guard.**

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `framer-motion-animator` | recommended — React + Framer Motion stack |
| 2 | `ui-animation` | recommended — CSS motion; use instead of row 1 on a non-Framer stack |
| 3 | `review-animations` | recommended — pre-ship critique (§3) |
| 4 | `motion-design` | optional — staging principles |
| 5 | `frontend-design` | optional — only when motion must serve a page thesis |
| 6 | `find-docs` | optional — Motion.dev API version check |

**Budget gate:** one stack skill (row 1 or 2) plus `review-animations` covers a routine polish pass. Pull `motion-design` only for choreography questions, and `find-docs` only for an unverified Motion.dev API.

**Skip:** `shadcn`, `ui-ux-pro-max` (new pages or components → `routr-frontend`), `remotion-best-practices`, `hyperframes` (exported MP4 → `routr-video`), `vercel-react-best-practices` (profiling why frames drop → `routr-perf`).

## 1. Audit

What moves? Entry triggers? `prefers-reduced-motion` upfront.

## 2. Implement

`useReducedMotion()` mandatory. Stagger; one focal animation per viewport.

## 3. Review pass

`review-animations` — purpose, jank, mobile, reduced motion.

## Output format

```markdown
## Motion report
**What moves / entry triggers:** …
**Reduced-motion guard:** yes/no
**Review pass:** purpose, jank, mobile checked
```

## Handoff

- Page from scratch → `routr-frontend` first
- Jank debug → `routr-debug`

## References

- [boundaries](./references/boundaries.md)

## Anti-patterns

- Parallax everywhere
- No reduced-motion guard
- Copy-paste snippets without purpose
