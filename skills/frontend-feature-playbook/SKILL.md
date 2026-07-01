---
name: frontend-feature-playbook
description: >
  Build or redesign user-facing UI with intentional visual design. Use when
  creating pages, components, landing pages, dashboards, design systems, layouts,
  styling, Tailwind/CSS work, or the user mentions frontend, UI, UX, or design.
  Routes to frontend-design, ui-ux-pro-max, tailwind-design-system, shadcn,
  and framer-motion-animator when motion is part of the feature. Uses symdex and
  lean-ctx for codebase discovery. Not for animation-only polish on existing UI
  — use frontend-motion-playbook.
---

# Frontend feature playbook

**Goal:** distinctive, accessible UI that fits the product — not generic AI slop.

## 0. Bootstrap (read in order)

Install missing skills from `playbook-common/references/skill-catalog.md`.

| Order | Skill | Role |
|-------|-------|------|
| 1 | `frontend-design` | Aesthetic direction, typography, layout thesis |
| 2 | `ui-ux-pro-max` | UX patterns, accessibility, design-system thinking |
| 3 | `tailwind-design-system` | Tailwind tokens, spacing, responsive scale |
| 4 | `shadcn` | If project uses shadcn/ui |
| 5 | `symdex-code-search` | Find existing components, routes, patterns |
| 6 | `lean-ctx` | Read related files without dumping whole components |
| 7 | `find-docs` | Current API docs for UI libraries in stack |
| 8 | `framer-motion-animator` | If feature includes motion (hero, transitions) |

Optional: `react-best-practices` for React/Next.js performance.

**Skip:** `caveman` during design exploration (clarity over brevity).

## 1. Discover

- [ ] SymDex: existing components, design tokens, route for this page
- [ ] lean-ctx: read design system / `globals.css` / theme files (signatures first)
- [ ] Note stack: React/Next/Vue, Tailwind v3/v4, shadcn, etc.

## 2. Design plan (before code)

Follow `frontend-design` process:

1. Subject, audience, single job of the page
2. Token system: 4–6 colors, type pairing, layout concept, **one signature element**
3. Self-critique: does this look like default AI template? Revise if yes.
4. Motion intent: list 1–2 orchestrated moments max (defer detail to motion playbook)

Use `ui-ux-pro-max` for:

- Accessibility checklist (focus, contrast, touch targets)
- Information hierarchy validation

## 3. Build

1. `shadcn` + `tailwind-design-system` for component primitives
2. Implement revised plan exactly — no drift to generic palette
3. Responsive down to mobile; respect `prefers-reduced-motion`
4. Avoid competing CSS specificity (see `frontend-design` notes)

## 4. Library docs

For Framer Motion, Radix, Next.js App Router, etc. → `find-docs` before API usage.

## 5. Verify

- [ ] Keyboard navigation works
- [ ] Reduced motion: animations degrade gracefully
- [ ] Visual self-critique against design plan

## 6. Motion pass

If motion feels weak or excessive → hand off to `frontend-motion-playbook` for dedicated pass.

## Handoff

- Bug in UI behavior → `debugging-playbook`
- Ship commit → `fix-and-ship-playbook`

## Anti-patterns

- Starting code before design plan
- Default cream/terracotta or acid-green-on-black without brief justification
- Animating everything — motion should serve the subject
