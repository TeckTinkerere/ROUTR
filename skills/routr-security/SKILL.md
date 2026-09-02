---
name: routr-security
description: "Security pass on code, auth, and cloud rules. Use when: security audit, vulnerabilities, RLS, secrets in code, 'is this secure'. Not for: non-security bugs (→ routr-debug)."
---

# routr-security

**Goal:** catch obvious security mistakes before ship — ranked by exploitability, not volume.

## When to activate

- "Is this secure", security audit, vulnerability check
- Auth/authorization paths, RLS policies, secrets handling
- Before a public launch or handling new user-supplied input

## Do not activate

- Non-security bug or crash → `routr-debug`
- General PR feedback with no security angle → `routr-review`
- Database schema/perf work with no security question → `routr-database`

## Iron law

**Every finding ships with a concrete exploit scenario and a fix — a severity label with no exploit path is not a finding.**

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `semgrep` | recommended — static analysis |
| 2 | `firebase-security-rules-auditor` | optional — Firebase & Firestore rules |
| 3 | `requesting-code-review` | recommended — review discipline |

If `semgrep` missing → [references/fallback.md](./references/fallback.md).

Data layer → `routr-database` (Postgres/Supabase RLS). Firebase → rules auditors above.

## 1. Scope (low freedom)

- [ ] AuthN/AuthZ paths
- [ ] Input validation & injection (SQL, XSS, command)
- [ ] Secrets in code/env
- [ ] Dependency CVEs (`npm audit`, etc.)

## 2. Static analysis (medium freedom)

Read `semgrep` — run on changed paths, not the whole repo, unless this is a full audit.

## 3. Data layer (medium freedom)

Supabase/Postgres → `routr-database` + RLS. Firebase → rules auditors.

## 4. Verify (low freedom)

- [ ] Every finding has an exploit scenario, not just a category label
- [ ] Severity reflects actual exploitability, not just OWASP category
- [ ] Fix suggested is the smallest change that closes the hole

## Output format

```markdown
## Security report
**Scope:** files/paths audited
**Findings** (severity-ranked):
- [severity] path:line — issue — exploit scenario — fix
**Verified:** yes/no — static analysis run, manual review of auth paths
```

## Handoff

| Need | Router |
|------|--------|
| Fix findings | `routr-ship` |
| General PR review alongside | `routr-review` |
| RLS/schema work | `routr-database` |

## References

- [fallback](./references/fallback.md) — when `semgrep` is missing
- [gotchas](./references/gotchas.md)
- [examples](./references/examples.md)
- [boundaries](./references/boundaries.md)

## Anti-patterns

- Severity labels with no concrete exploit scenario
- Full-repo scan when only changed paths are in scope
- Treating a lint warning as a security finding to pad the report
- Fixing findings from within this skill instead of handing off to `routr-ship`
