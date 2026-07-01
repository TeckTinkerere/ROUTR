---
name: code-review-playbook
description: "Review a PR or diff for bugs, style, and React best practices. Use when: code review, 'review my changes', before merge."
---

# Code review playbook

**Goal:** actionable, verified feedback — not performative praise or blind nitpicks.

## 0. Bootstrap

| Skill | When |
|-------|------|
| `requesting-code-review` | You authored the change; pre-merge self-review |
| `receiving-code-review` | Addressing review comments from others |
| `code-review-excellence` | Structured review rubric |
| `vercel-react-best-practices` | React/Next.js performance & patterns |
| `review-animations` | PR touches motion/CSS transitions |
| `caveman-review` | User wants one-line terse review comments |

Matt Pocock `review-since` — when user says "review since commit X" or branch vs spec.

## 1. Scope the diff

- [ ] Identify base branch / commit range
- [ ] SymDex: blast radius on changed public APIs
- [ ] lean-ctx: read changed files (signatures → hot hunks only)

## 2. Review axes

1. **Correctness** — bugs, edge cases, error handling
2. **Spec** — does it match issue/PRD? (`review-since` spec axis)
3. **Standards** — repo conventions (`review-since` standards axis)
4. **Security** — auth, input validation, secrets (escalate → `security-review-playbook`)
5. **Performance** — React/Next: `vercel-react-best-practices`
6. **UX/a11y** — if UI: `web-design-guidelines`, `ui-ux-pro-max`

## 3. Output format

Per finding: `path:line — severity — issue — suggested fix`

Prioritize: must-fix → should-fix → nit

## 4. After review

- Author fixing findings → `fix-and-ship-playbook`
- Review comments unclear → `receiving-code-review` before implementing

## Anti-patterns

- Style-only comments without consistency argument
- Approving without reading tests
- Suggesting rewrites unrelated to PR scope
