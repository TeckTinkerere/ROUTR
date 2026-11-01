---
name: routr-depth-frontend
description: "Distinctive UI design when frontend-design is not installed. Use when: routr-frontend bootstrap fails, building UI without Anthropic frontend-design skill, or output looks like generic AI template."
---

# routr-depth-frontend

Fallback depth for `routr-frontend`. Load only when `frontend-design` is not installed.

## Iron law

**Design plan before code — self-critique against generic AI defaults.**

## Ground in the subject

Name: concrete subject, audience, page's single job. Pull distinctive choices from the subject's world — not default palettes.

## Avoid default AI clusters (unless brief requires)

1. Warm cream + terracotta + serif display
2. Near-black + acid-green accent
3. Newspaper columns + hairline rules everywhere

## Design plan (required before code)

```markdown
### Tokens
- Colors: [name #hex] × 4–6 with roles
- Display + body typefaces (paired deliberately)
- Layout concept (one sentence + wireframe if helpful)
### Signature
One memorable element tied to this brief
### Self-critique
[ ] Not interchangeable with generic SaaS template
```

## Build rules

1. Derive every color and font from plan
2. Responsive mobile required
3. Visible keyboard focus; `prefers-reduced-motion` respected
4. One orchestrated motion moment max — defer detail to `routr-motion`

## CSS discipline

Avoid competing selector specificities (`.section` vs `.cta` padding wars).

## Install full skill

```bash
npx skills@1.7.4 add anthropics/skills@frontend-design -g -y --copy
```
