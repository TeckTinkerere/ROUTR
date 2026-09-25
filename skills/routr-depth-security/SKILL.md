---
name: routr-depth-security
description: "Minimum OWASP-style security audit process when semgrep and rules-auditor skills are not installed. Use when: routr-security bootstrap fails, child security skill missing, or agent about to ship a security opinion with no structured process behind it."
---

# routr-depth-security

Fallback depth for `routr-security`. Load only when `semgrep` and any rules-auditor skill (e.g. `firebase-security-rules-auditor`) are both unavailable.

## Iron law

```
EVERY FINDING SHIPS WITH A CONCRETE EXPLOIT SCENARIO AND A FIX
```

A severity label with no exploit path is a guess, not a finding.

## Audit process (complete each phase before the next)

### Phase 1: Scope and threat model

1. State what's in scope: which paths/endpoints/files, and who the assumed attacker is (anonymous internet user, authenticated low-privilege user, insider)
2. List trust boundaries the code crosses: client → server, server → DB, server → third-party API, user input → rendered HTML/shell/SQL
3. Note what's explicitly out of scope (e.g. infra/network security if this is an app-code review)

### Phase 2: AuthN / AuthZ and IDOR

1. Trace how identity is established (session, JWT, API key) and where it's checked
2. For every endpoint that reads/writes a resource by ID: can the caller substitute another user's ID and get their data? (IDOR)
3. Check role/permission checks happen server-side, not just hidden in the UI
4. Check for missing checks on secondary actions (e.g. delete/export endpoints that skip the auth check the main read endpoint has)

### Phase 3: Injection (SQL / NoSQL / command / XSS)

1. Find every place user input reaches a query, shell command, or HTML/JS output
2. SQL/NoSQL: parameterized queries or ORM used correctly? Any string-concatenated queries?
3. Command injection: any shell-out call (e.g. a process-spawn or exec-style API) with user-controlled arguments?
4. XSS: any unescaped user input rendered as HTML, or `dangerouslySetInnerHTML`/`innerHTML` with user data?
5. For each hit, write the actual input that would trigger it — not just "could be vulnerable"

### Phase 4: Secrets in code and env

1. Grep changed files and git history for API keys, tokens, passwords, connection strings
2. Confirm `.env*` files are gitignored and not committed
3. Check secrets aren't logged, returned in API responses, or exposed to the client bundle (env vars without a framework's public-prefix convention)

### Phase 5: Supabase RLS / Firebase rules

1. Supabase/Postgres: every multi-tenant table has RLS enabled with a policy matching the tenancy model — can tenant A's session read/write tenant B's rows under any policy gap?
2. Firebase/Firestore: security rules deny by default; check rules aren't `allow read, write: if true` anywhere reachable
3. Hand off the schema/policy read itself to `routr-database` if it's a large schema — apply the security lens on top

### Phase 6: SSRF and open redirects

1. Any endpoint that fetches a URL supplied by the user (webhooks, image proxies, URL previews)? Can it be pointed at internal/private IP ranges or cloud metadata endpoints?
2. Any redirect that takes a user-supplied destination? Can it be pointed off-domain for phishing?

### Phase 7: Dependency audit

1. Run `npm audit` (or the ecosystem equivalent) on the changed package manifest
2. Flag any dependency with a known critical/high CVE that's actually reachable from application code, not just present in the tree

## Severity rating

Rate each finding by actual exploitability, not OWASP category alone:

| Severity | Criteria |
|----------|----------|
| Critical | Unauthenticated, remote, full data/account compromise |
| High | Authenticated but low-privilege, or requires user interaction, significant impact |
| Medium | Requires specific conditions or limited impact |
| Low | Theoretical or requires attacker to already have significant access |

## Report format

```markdown
## Security report
**Scope:** files/paths audited, assumed attacker
**Findings** (severity-ranked):
- [severity] path:line — issue — exploit scenario — fix
**Verified:** yes/no — how (manual trace, npm audit, RLS policy read)
```

## Install full skills

```bash
npx skills add trailofbits/skills -g --skill semgrep -y --copy
npx skills add firebase/agent-skills -g --skill firebase-security-rules-auditor -y --copy
```

Then follow those skills' own instructions in addition to this process — this fallback does not replace static analysis tooling once installed.
