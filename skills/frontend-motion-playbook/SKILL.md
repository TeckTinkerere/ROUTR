---
name: frontend-motion-playbook
description: "Add or polish animations (Framer Motion, scroll, transitions). Use when: animate, motion, micro-interactions — UI already exists."
---

# Frontend motion playbook

**Goal:** motion that feels intentional, performant, and accessible.

## 0. Bootstrap

Read if present (see `playbook-common/references/skill-catalog.md`):

| Skill | When |
|-------|------|
| `framer-motion-animator` | React + Framer Motion (`motion`, `AnimatePresence`, layout) |
| `review-animations` | **Before ship** — critique timing, easing, distraction |
| `motion-design` | Principles: staging, follow-through, hierarchy |
| `ui-animation` | CSS / cross-framework motion patterns |
| `gsap-framer-scroll-animation` | Scroll-scrubbed or complex scroll timelines |
| `frontend-design` | Ensure motion serves the page thesis (one orchestrated moment) |
| `find-docs` | Motion.dev / Framer Motion API version accuracy |

## 1. Audit existing UI

- [ ] What should move vs stay static?
- [ ] Entry: page load, scroll-in, hover, route transition?
- [ ] `prefers-reduced-motion` strategy defined upfront

## 2. Choose stack

| Context | Prefer |
|---------|--------|
| React component motion | Framer Motion (`framer-motion-animator`) |
| Scroll storytelling | GSAP skill or Framer `useScroll` |
| Simple hover/focus | CSS transitions (`ui-animation`) |
| Icon/illustration loops | Lottie (`motion-design` guidance) |

Verify APIs with `find-docs` — Motion v11+ patterns differ from older examples.

## 3. Implement

Follow `framer-motion-animator` for:

- `initial` / `animate` / `exit` with `AnimatePresence`
- Layout animations only when they aid comprehension
- `useReducedMotion()` hook — mandatory

Principles from `motion-design`:

- Stagger children; one focal animation per viewport
- Easing: avoid linear for UI; springs for organic feel
- Duration: micro 150–250ms, reveals 400–600ms

## 4. Review pass

Read `review-animations` and check:

- [ ] Nothing animates without purpose
- [ ] No layout shift / jank (prefer `transform` + `opacity`)
- [ ] Mobile performance acceptable
- [ ] Reduced motion path tested

## 5. Performance

- Avoid animating `width`/`height`/`top`/`left` at scale
- `will-change` sparingly
- Lazy mount off-screen sequences

## Handoff

- Building the page from scratch → `frontend-feature-playbook` first
- Motion bug / jank debug → `debugging-playbook`

## Anti-patterns

- Parallax on every section
- Infinite attention-grabbing loops
- Copy-paste animation snippets without reduced-motion guard
