---
name: routr-refactor
description: "Improve code structure without changing behavior. Use when: refactor, tech debt, extract module, clean up code, restructure. Not for: fixing bugs or changing behavior (→ routr-debug / routr-ship)."
---

# routr-refactor

**Goal:** safer structure — behavior preserved, diff reviewable.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `improve-codebase-architecture` | Deep modules, seams, deepening opportunities |
| `vercel-composition-patterns` | React composition refactors |
| `vercel-react-best-practices` | Performance-safe refactors |
| `symdex-code-search` | Callers before moves |
| `tdd` / `test-driven-development` | Safety net |

## 1. Safety net

- [ ] Tests green OR characterization tests first
- [ ] SymDex: map callers of symbols you'll move/rename

## 2. Plan refactor

Small steps — one seam at a time. No behavior + feature mix.

## 3. React-specific

`vercel-composition-patterns` for component API redesign.

## 4. Verify

- [ ] Tests pass
- [ ] Public API changes documented

## Handoff

- Review PR → `routr-review`
- Bug uncovered → `routr-debug`

## Anti-patterns

- Big-bang rewrite without tests
- 50-file rename in one commit without tooling
