---
name: routr-plan
description: "Plan before coding: brainstorm, PRD, stress-test ideas. Use when: new feature, spec, PRD, 'grill my plan', brainstorm, architecture decision, before big implementation. Not for: writing code now (→ routr-ship or routr-frontend)."
---

# routr-plan

**Goal:** aligned requirements before expensive implementation.

## When to activate

- Greenfield feature or large change
- User wants spec, PRD, or plan before code
- Stress-test or "grill" an idea

## Do not activate

- Ready to implement small fix → `routr-ship`
- Explore existing code only → `routr-explore`
- Agent system design → `routr-agents`

## Iron law

**No implementation until brainstorm output is approved or open questions are explicit.**

## 0. Bootstrap

| Skill | Tier |
|-------|------|
| `brainstorming` | required |
| `to-prd` | recommended |
| `grill-me` | recommended — canonical; not `grilling` |
| `grill-with-docs` | optional |
| `improve-codebase-architecture` | optional — large changes |
| `find-skills` | optional |

**Budget gate:** `brainstorming` first; add `to-prd` only when writing the doc and `grill-me` only for non-trivial plans. `improve-codebase-architecture` / `find-skills` are exception-only.

If `brainstorming` missing → read `routr-depth-plan` OR [references/fallback.md](./references/fallback.md).

## 1. Intake

- [ ] Problem, audience, success metric
- [ ] Constraints: timeline, stack, non-goals
- [ ] Frontend? Flag `routr-frontend` for later

## 2. Brainstorm (medium freedom)

Read `brainstorming` — see [workflow.md](./references/workflow.md).

## 3. Stress-test (medium freedom)

Non-trivial plan → `grill-me` before build.

## 4. Document (low freedom)

`to-prd` when ready — measurable acceptance criteria required.

## Output format

See PRD template in [workflow.md](./references/workflow.md).

## Handoff

**Plan approved → STOP.** Do not implement from within routr-plan — re-route to the build skill below (fresh context, its own bootstrap):

| Next | Skill |
|------|-------|
| Build UI | `routr-frontend` |
| Implement fix | `routr-ship` |
| Agent system | `routr-agents` |
| Execute written plan | `executing-plans` (Obra) |

## References

- [workflow](./references/workflow.md)
- [fallback](./references/fallback.md)
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Coding before brainstorm on greenfield
- PRD without acceptance criteria
- Skipping grill on high-risk architecture
