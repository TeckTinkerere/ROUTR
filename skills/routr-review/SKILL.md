---
name: routr-review
description: "Review a PR or diff for bugs, style, and React best practices. Use when: code review, 'review my changes', before merge, PR feedback. Not for: writing the fix yourself (→ routr-ship)."
---

# routr-review

**Goal:** actionable, verified feedback.

## When to activate

- Code review, "review my changes", before merge, PR feedback

## Do not activate

- Writing the fix yourself → `routr-ship`
- Reconcile current product behavior with original requirements or update product history → `routr-spec`

## Iron law

**Every review comment ships with a suggested fix — a flagged issue with no fix is half a review.**

## 0. Bootstrap

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `requesting-code-review` | recommended — author pre-merge self-review |
| 2 | `receiving-code-review` | optional — addressing others' comments |
| 3 | `vercel-react-best-practices` | optional — React/Next diffs only |
| 4 | `review-animations` | optional — motion/CSS in the PR |
| 5 | `caveman-review` | optional — terse one-line comments |

`review-since` — "review since commit X".

**Budget gate:** `requesting-code-review` for every review; pull rows 2–5 only when their trigger is in the diff or the request (reviewer comments to answer, React files, motion/CSS, terse output asked for).

**Skip:** `semgrep`, `firebase-security-rules-auditor` (dedicated security pass → `routr-security`), `systematic-debugging` (a suspected bug is a finding to report, not a debug session → `routr-debug`), `test-driven-development` (writing the fix → `routr-ship`).

## 1. Scope diff

- [ ] Base branch / commit range
- [ ] SymDex blast radius on public APIs
- [ ] lean-ctx: changed files only

## 2. Review axes

Correctness → Spec → Standards → Security → Performance → UX/a11y

Security escalate → `routr-security`

## 3. Output format

`path:line — severity — issue — suggested fix`

## Handoff

- Fix findings → `routr-ship`
- Unclear comments → `receiving-code-review`
- Security-shaped finding → `routr-security`

## References

- [boundaries](./references/boundaries.md)
