# Security fallback (no child skills installed)

Use when `semgrep` and any rules-auditor skill are both unavailable.

## Iron law

```
EVERY FINDING SHIPS WITH A CONCRETE EXPLOIT SCENARIO AND A FIX
```

## Minimum process

1. **Scope** — authN/authZ paths, input validation & injection surfaces, secrets in code/env, dependency CVEs. List them before reading code.
2. **Manual pass over changed paths** — trace every place user input crosses a trust boundary (DB query, shell command, HTML render, file path). For each: can an attacker control this input, and what happens if they do?
3. **Secrets check** — grep changed files and diffs for API keys, tokens, connection strings; check `.env*` files aren't committed.
4. **Dependency check** — `npm audit` / equivalent for the changed package manifest.
5. **Data layer** — if Postgres/Supabase, verify RLS policies exist and match the tenancy model (`routr-database` for the schema read).
6. **Report** — severity-ranked, each finding: path:line, issue, concrete exploit input, smallest fix.

## When stuck

- Can't tell if an endpoint is actually reachable unauthenticated → trace the route/middleware chain rather than assuming from the file name
- Uncertain about a framework's default protections (CSRF, escaping) → check the framework's own security docs before flagging a false positive

## Escalate to install

```bash
npx skills add trailofbits/skills -g --skill semgrep -y --copy
npx skills add firebase/agent-skills -g --skill firebase-security-rules-auditor -y --copy
```
