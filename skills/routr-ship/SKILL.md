---
name: routr-ship
description: "Make a small fix, verify it, and commit or open a PR. Use when: 'fix this', known change, patch, tests must pass, ready to ship, commit, open PR, merge this change. Not for: unknown root cause (→ routr-debug); building new UI (→ routr-frontend)."
---

# routr-ship

**Goal:** minimal correct diff → verified → commit-ready.

## When to activate

- User wants fix committed or PR opened
- Small scoped change with known direction
- "Ship it", "commit this", "open a PR"

## Do not activate

- Root cause unknown → `routr-debug`
- Large feature from scratch → `routr-plan` then domain router
- Deploy only → `routr-deploy`
- Reconcile an existing product's specification without code changes → `routr-spec`

## Iron law

**No commit without verification on the changed behavior.**

## 0. Bootstrap

| Skill | Tier |
|-------|------|
| `symdex-code-search` | recommended |
| `lean-ctx` | recommended |
| `test-driven-development` | recommended — bugfixes |
| `finishing-a-development-branch` | optional |
| `caveman-commit` | optional |
| `requesting-code-review` | optional — before PR |

**Budget gate:** `symdex` + `lean-ctx` to locate the change; add `test-driven-development` for bugfixes only, and `requesting-code-review` only when opening a PR. Skip the rest.

If root cause unclear → **stop**, switch to `routr-debug`.

If `caveman-commit` missing → `routr-depth-ship` for commit format.

## 1. Impact check (low freedom)

- [ ] SymDex: callers of changed symbols
- [ ] Files to edit ≤ 3 for typical fixes — see [workflow.md](./references/workflow.md)

## 2. Implement (medium freedom)

- Match project conventions
- Smallest diff; no unrelated formatting

## 3. Verify (low freedom)

- [ ] Tests or manual repro pass
- [ ] No new linter errors in touched files

## 4. Ship artifacts (low freedom)

Commit or PR per project convention — templates in [workflow.md](./references/workflow.md).

Push, merge or open a PR only when the user asked for that step. Never force-push a shared branch or merge into the default branch on your own initiative.

## Handoff

Committed → **STOP and re-route** for the next stage (do not deploy or polish from here):

- Motion polish → `routr-motion` (short pass)
- Deploy → `routr-deploy`
- Launch or brag video → `routr-video`
- Explicitly requested as-built spec / product-drift update after implementation → `routr-spec` (also after verified implementation when committing was not requested)

## References

- [workflow](./references/workflow.md)
- [fallback](./references/fallback.md)
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Large refactor bundled with bugfix
- Commit without verification
- Reading entire codebase for context
