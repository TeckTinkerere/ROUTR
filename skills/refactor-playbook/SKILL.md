---
name: refactor-playbook
description: "Improve code structure without changing behavior. Use when: refactor, tech debt, extract module, clean up code."
---

# Refactor playbook

**Goal:** safer structure — behavior preserved, diff reviewable.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `improve-codebase-architecture` | Find deepening opportunities in repo |
| `codebase-design` | Deep modules, seams, testable interfaces |
| `vercel-composition-patterns` | React boolean-prop → composition refactors |
| `vercel-react-best-practices` | Performance-safe React refactors |
| `symdex-code-search` | Callers/callees before moving symbols |
| `tdd` / `test-driven-development` | Tests as safety net |

## 1. Safety net

- [ ] Existing tests green OR add characterization tests first
- [ ] SymDex: map callers of symbols you'll move/rename

## 2. Plan refactor

1. `improve-codebase-architecture` or `codebase-design` for target shape
2. Small commits / steps — one seam at a time
3. No behavior change mixed with feature work

## 3. React-specific

- `vercel-composition-patterns` for component API redesign
- Avoid re-render regressions (`vercel-react-best-practices`)

## 4. Verify

- [ ] Tests still pass
- [ ] Public API changes documented
- [ ] lean-ctx re-read only changed modules for final check

## Handoff

- Review structural PR → `code-review-playbook`
- Refactor uncovered a bug → `debugging-playbook`

## Anti-patterns

- Big-bang rewrite without tests
- Renaming across 50 files in one commit without tooling
