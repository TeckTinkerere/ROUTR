---
name: routr-security
description: "Security pass on code, auth, and cloud rules. Use when: security audit, vulnerabilities, RLS, secrets in code, 'is this secure'. Not for: non-security bugs (→ routr-debug)."
---

# routr-security

**Goal:** catch obvious security mistakes before ship.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `semgrep` | Static analysis |
| `firebase-security-rules-auditor` | Firebase & Firestore rules |
| `requesting-code-review` | Review discipline |

## 1. Scope

- [ ] AuthN/AuthZ paths
- [ ] Input validation & injection (SQL, XSS, command)
- [ ] Secrets in code/env
- [ ] Dependency CVEs (`npm audit`, etc.)

## 2. Static analysis

Read `semgrep` — run on changed paths.

## 3. Data layer

Supabase/Postgres → `routr-database` + RLS. Firebase → rules auditors.

## 4. Output

Severity-ranked findings with exploit scenario + fix.

## Handoff

- Fix findings → `routr-ship`
- General PR → `routr-review`
