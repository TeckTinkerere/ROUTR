---
name: routr-depth-plan
description: "Brainstorm and PRD gate when brainstorming skill is not installed. Use when: routr-plan bootstrap fails, greenfield feature without Obra brainstorming, or user wants plan before code."
---

# routr-depth-plan

Fallback depth for `routr-plan`. Load only when `brainstorming` is not installed.

## Iron law

**No implementation until approach approved or open questions explicit.**

## Brainstorm minimum

1. Restate user goal (one paragraph)
2. User intent vs stated request
3. Two approaches with trade-offs
4. Risks and open questions
5. Recommended approach + why

## Grill minimum (non-trivial plans)

Challenge before build:

- Who is the user really?
- What fails at scale?
- What's explicitly out of scope?
- What would make us rollback?

## PRD gate

Before coding:

```markdown
## Success metrics
- [ ] Measurable …

## Acceptance criteria
- [ ] Given … when … then …

## Non-goals
- …
```

## Install full skills

```bash
npx skills@1.7.4 add obra/superpowers -g --skill brainstorming -y --copy
npx skills@1.7.4 add mattpocock/skills -g --skill grill-me --skill to-prd -y --copy
```
