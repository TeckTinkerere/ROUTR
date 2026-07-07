---
name: routr-debug
description: "Find and fix bugs step by step (reproduce → locate → fix). Use when: errors, crashes, test failures, 'debug this', 'why is this broken', stack trace, root cause, flaky test. Not for: a known fix ready to commit (→ routr-ship); understanding code with no bug (→ routr-explore)."
---

# routr-debug

**Goal:** reproduce → localize → hypothesize → verify fix. Minimize tokens while maximizing signal.

## When to activate

- Errors, crashes, exceptions, stack traces
- Failing or flaky tests
- Unexpected behavior or regressions
- User says debug, trace, investigate, root cause

## Do not activate

- Ready to commit a known fix → `routr-ship`
- Open-ended "how does X work" → `routr-explore`
- Security audit → `routr-security`
- Visual redesign → `routr-frontend`

## Iron law

**No fixes without root cause investigation first.**

## 0. Bootstrap

Read if present (install from `routr-catalog/references/skill-registry.md`):

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `systematic-debugging` | required |
| 2 | `diagnosing-bugs` | recommended |
| 3 | `symdex-code-search` | recommended |
| 4 | `lean-ctx` | recommended |
| 5 | `context-degradation` | optional — agent confused mid-session |

**Budget gate:** read `required` + `recommended` only for routine bugs. Pull an `optional` child solely when its stated signal fires (e.g. `context-degradation` only if the agent is mid-session confused). Never load all five for a simple fix.

If `systematic-debugging` missing → read `routr-depth-debug` OR [references/fallback.md](./references/fallback.md).

Optional: `caveman` at **lite** intensity for terse progress only.

**Skip:** `frontend-design`, `caveman-compress`, open-ended exploration without a symptom.

## 1. Symptom lock (low freedom)

- [ ] Exact error message, stack trace, or failing test name recorded
- [ ] Reproduction steps confirmed (or stated as unable to reproduce)
- [ ] Scope: backend / frontend / full-stack

## 2. Locate (medium freedom)

Before whole-file reads — see [workflow.md](./references/workflow.md):

1. SymDex: symbol search, routes, callers/callees
2. lean-ctx: `signatures` or `map` → `lines:N-M` for hot paths only

## 3. Hypothesis loop (medium freedom)

For each hypothesis:

1. State prediction in one sentence
2. Read minimal evidence
3. Confirm or eliminate
4. Max 3 parallel hypotheses; prune dead ends

## 4. Fix discipline (low freedom)

- Smallest change addressing root cause
- No drive-by refactors
- Frontend visual bug: `routr-frontend` CSS sections only

## 5. Verify

- Re-run reproduction or failing test
- SymDex callers graph for blast radius

## Output format

```markdown
## Debug report
**Symptom:** …
**Root cause:** …
**Fix:** …
**Verified:** yes/no — how
```

## Handoff

**Root cause fixed → STOP here.** Do not commit from within routr-debug — re-route to `routr-ship` (fresh) so shipping runs its own verification. Chain: `routr-debug` → `routr-ship` → `routr-deploy`.

## References

- [workflow](./references/workflow.md) — phased debug process
- [fallback](./references/fallback.md) — when child skills missing
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Reading entire large files before SymDex/lean-ctx narrow pass
- Fixing without reproduction
- Loading all context-engineering skills for a simple null-pointer fix
