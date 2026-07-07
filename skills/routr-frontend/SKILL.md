---
name: routr-frontend
description: "Build or redesign UI (pages, components, design system). Use when: new screen, landing page, layout, Tailwind, shadcn, 'make it look good', redesign, hero section, dashboard UI. Not for: animating existing UI (→ routr-motion); a visual bug from broken logic (→ routr-debug)."
---

# routr-frontend

**Goal:** distinctive, accessible UI that fits the product — not generic AI slop.

## When to activate

- New page, screen, component, or landing page
- UI redesign or "make it look better"
- Design system, tokens, Tailwind, shadcn work

## Do not activate

- Motion-only polish on existing UI → `routr-motion`
- Logic bug in UI → `routr-debug`
- Mobile Expo/RN → `routr-mobile`
- Marketing copy only → `routr-marketing`

## Iron law

**No code before a written design plan that passes self-critique.**

## 0. Bootstrap

Install missing from `routr-catalog/references/skill-registry.md`.

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `frontend-design` | required |
| 2 | `web-design-guidelines` | recommended |
| 3 | `ui-ux-pro-max` | recommended |
| 4 | `vercel-react-best-practices` | recommended |
| 5 | `tailwind-design-system` | optional |
| 6 | `shadcn` | optional — if project uses shadcn |
| 7 | `symdex-code-search` | recommended |
| 8 | `lean-ctx` | recommended |
| 9 | `find-docs` | optional |

If `frontend-design` missing → read `routr-depth-frontend` OR [references/fallback.md](./references/fallback.md).

**Skip:** `caveman` during design exploration.

## 1. Discover (medium freedom)

- [ ] SymDex: existing components, tokens, route
- [ ] lean-ctx: design system / `globals.css` (signatures first)
- [ ] Note stack: React/Next/Vue, Tailwind v3/v4, shadcn

## 2. Design plan (low freedom)

Follow [workflow.md](./references/workflow.md):

1. Subject, audience, single job of the page
2. Token system: 4–6 colors, type pairing, layout concept, **one signature element**
3. Self-critique: default AI template? Revise if yes.
4. Motion intent: 1–2 orchestrated moments max → defer to `routr-motion`

## 3. Build (medium freedom)

1. `shadcn` + `tailwind-design-system` for primitives
2. Implement plan exactly — no drift to generic palette
3. Responsive mobile; `prefers-reduced-motion`
4. `find-docs` before unfamiliar library APIs

## 4. Verify (low freedom)

- [ ] Keyboard navigation
- [ ] Reduced motion degrades gracefully
- [ ] Visual self-critique against design plan

## Output format

See design brief template in [workflow.md](./references/workflow.md).

## Handoff

- Motion weak → `routr-motion`
- Bug → `routr-debug`
- Ship → `routr-ship`

## References

- [workflow](./references/workflow.md)
- [fallback](./references/fallback.md)
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Code before design plan
- Default cream/terracotta or acid-green-on-black without brief justification
- Animating everything
