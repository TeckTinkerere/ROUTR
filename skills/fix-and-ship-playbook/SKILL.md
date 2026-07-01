---
name: fix-and-ship-playbook
description: >
  Implement a targeted fix, verify it works, and prepare to ship (commit/PR).
  Use when the user says fix, patch, make it work, get tests passing, prepare
  commit, or open PR — and the problem is already understood or narrowly scoped.
  Routes to symdex-code-search for impact analysis, lean-ctx for minimal reads,
  caveman-commit for messages, optional caveman-review for diffs. Not for
  open-ended debugging — use debugging-playbook first if root cause is unknown.
---

# Fix and ship playbook

**Goal:** minimal correct diff → verified → commit-ready.

## 0. Bootstrap

Read if present:

1. `symdex-code-search` — impact / callers before editing public APIs
2. `lean-ctx` — read only files you will touch
3. `test-driven-development` — add regression test when fixing bugs
4. `finishing-a-development-branch` — merge vs PR when done
5. `caveman-commit` — when writing commit message
6. `requesting-code-review` — before opening PR
7. `caveman-review` — optional terse self-review

If root cause unclear → **stop** and switch to `debugging-playbook`.

## 1. Impact check

- [ ] SymDex: who calls the symbol/route you're changing?
- [ ] List files you expect to edit (aim ≤ 3 for typical fixes)

## 2. Implement

- Match existing project conventions
- Smallest diff; no unrelated formatting
- Frontend fix touching layout? Skim `frontend-design` only if visual regression risk

## 3. Verify

- [ ] Tests or manual repro steps pass
- [ ] No new linter errors in touched files
- [ ] If React UI: quick check responsive + `prefers-reduced-motion` not broken

## 4. Ship artifacts

- Commit: follow `caveman-commit` or project convention
- PR: follow `caveman-review` one-line comment style if reviewing own diff

## 5. Frontend ship extras

If change is UI-facing, optional polish pass:

- Motion feels wrong? → `frontend-motion-playbook` (short pass, not full redesign)

## Anti-patterns

- Large refactor bundled with bugfix
- Commit without verification
- Reading entire codebase "for context"
