---
name: debugging-playbook
description: >
  Structured debugging workflow for software defects. Use when the user reports
  bugs, errors, exceptions, test failures, unexpected behavior, regressions, or
  asks to debug, trace, or find root cause. Routes to symdex-code-search and
  lean-ctx before broad file reads. Uses caveman-lite for status updates in long
  sessions. Escalates to frontend-motion or design skills only if the bug is
  visual/CSS/animation-related.
---

# Debugging playbook

**Goal:** reproduce → localize → hypothesize → verify fix. Minimize tokens while maximizing signal.

## 0. Bootstrap

Read if present (install from `playbook-common/references/skill-catalog.md` if missing):

1. `symdex-code-search`
2. `lean-ctx`
3. `context-degradation` — if the agent seems confused or contradicts earlier facts

Optional: `caveman` at **lite** intensity for terse progress updates only.

**Skip:** `frontend-design`, `caveman-compress`, open-ended exploration without a symptom.

## 1. Symptom lock

- [ ] Exact error message, stack trace, or failing test name recorded
- [ ] Reproduction steps confirmed (or stated as unable to reproduce)
- [ ] Scope: backend / frontend / full-stack

## 2. Locate (SymDex first)

Before `Read` / `Grep` / `Glob` on whole files:

1. `symdex index` if repo not indexed
2. SymDex: symbol search, routes, callers/callees, `build_context_pack` for feature-level questions
3. lean-ctx: `signatures` or `map` mode → expand to `lines:N-M` only for hot paths

## 3. Hypothesis loop

For each hypothesis:

1. State prediction in one sentence
2. Read minimal evidence (lean-ctx narrow read)
3. Confirm or eliminate
4. Max 3 parallel hypotheses; prune dead ends

## 4. Fix discipline

- Smallest change that addresses root cause (not symptom masking)
- No drive-by refactors
- If frontend visual bug: read `frontend-feature-playbook` sections on CSS specificity only

## 5. Verify

- Re-run reproduction steps or failing test
- Check adjacent callers (SymDex callers graph) for blast radius

## 6. Handoff

If user wants commit/PR next → switch to `fix-and-ship-playbook`.

## Anti-patterns

- Reading entire large files before SymDex/lean-ctx narrow pass
- Fixing without reproduction
- Loading all context-engineering skills during a simple null-pointer fix
