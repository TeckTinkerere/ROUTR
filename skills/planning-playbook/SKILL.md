---
name: planning-playbook
description: "Plan before coding: brainstorm, PRD, stress-test ideas. Use when: new feature, spec, 'grill my plan', before big implementation."
---

# Planning playbook

**Goal:** aligned requirements before expensive implementation.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `brainstorming` | Obra: **required** before creative/feature work |
| `to-prd` | Synthesize conversation into published PRD |
| `grill-me` / `grilling` | Stress-test plan via adversarial questions |
| `grill-with-docs` | Grill against uploaded specs/docs |
| `improve-codebase-architecture` | Scan repo for deepening opportunities before big changes |

Optional: `find-skills` (vercel-labs) — discover installable skills for the planned stack.

## 1. Intake

- [ ] What problem, for whom, success metric?
- [ ] Constraints: timeline, stack, non-goals
- [ ] Frontend involved? Flag for `frontend-feature-playbook` later

## 2. Brainstorm (Obra)

Read `brainstorming` and explore:

- User intent vs stated request
- 2–3 approaches with trade-offs
- Explicit risks and open questions

## 3. Stress-test

If plan is non-trivial:

1. `grill-me` — challenge assumptions before build
2. User approves revised plan or answers open questions

## 4. Document

1. `to-prd` — publish PRD to issue tracker when ready
2. Break into issues (`tdd` skill for tracer-bullet slices if using Matt Pocock flow)

## 5. Architecture preview

Large change? Run `improve-codebase-architecture` scan or `explore-codebase-playbook` for affected areas.

## Handoff

| Next step | Playbook |
|-----------|----------|
| Build feature | `frontend-feature-playbook` or `fix-and-ship-playbook` |
| Agent system | `agent-design-playbook` |
| Execute written plan | `executing-plans` (Obra) — read skill directly |

## Anti-patterns

- Coding before brainstorm on greenfield features
- PRD without measurable acceptance criteria
- Skipping grill on high-risk architectural bets
