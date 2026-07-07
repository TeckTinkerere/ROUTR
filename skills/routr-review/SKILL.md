---
name: routr-review
description: "Review a PR or diff for bugs, style, and React best practices. Use when: code review, 'review my changes', before merge, PR feedback. Not for: writing the fix yourself (→ routr-ship)."
---

# routr-review

**Goal:** actionable, verified feedback.

## 0. Bootstrap

| Skill | When |
|-------|------|
| `requesting-code-review` | Author pre-merge self-review |
| `receiving-code-review` | Addressing others' comments |
| `vercel-react-best-practices` | React/Next patterns |
| `review-animations` | Motion/CSS in PR |
| `caveman-review` | Terse one-line comments |

`review-since` — "review since commit X".

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
