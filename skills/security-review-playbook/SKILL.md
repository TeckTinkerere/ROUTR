---
name: security-review-playbook
description: "Security pass on code, auth, and cloud rules. Use when: security audit, vulnerabilities, RLS, secrets in code."
---

# Security review playbook

**Goal:** catch obvious security mistakes before ship.

## 0. Bootstrap

| Skill | Source | Role |
|-------|--------|------|
| `semgrep` | trailofbits/skills | Static analysis patterns |
| `firebase-security-rules-auditor` | firebase/agent-skills | Firebase rules |
| `firestore-security-rules-auditor` | firebase/agent-skills | Firestore rules |
| `requesting-code-review` | obra/superpowers | Structured review discipline |

## 1. Scope

- [ ] AuthN/AuthZ paths
- [ ] Input validation & injection (SQL, XSS, command)
- [ ] Secrets in code/env
- [ ] Dependency known CVEs (`npm audit`, etc.)

## 2. Static analysis

Read `semgrep` — run recommended rules on changed paths.

## 3. Data layer

- Supabase/Postgres → `database-playbook` + RLS review
- Firebase → security rules auditor skills

## 4. Output

Severity-ranked findings with exploit scenario + fix.

## Handoff

- Fix findings → `fix-and-ship-playbook`
- General PR review → `code-review-playbook`
