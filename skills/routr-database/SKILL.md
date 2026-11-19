---
name: routr-database
description: "SQL, Postgres, Supabase schema and queries. Use when: migrations, RLS, slow queries, database design, Supabase. Not for: ORM or client-library setup (→ routr-integrate); wrong query results, cause unknown (→ routr-debug)."
---

# routr-database

**Goal:** correct, performant, secure data layer.

## When to activate

- Migrations, schema design, RLS policies
- Slow queries, indexing, connection pooling
- Supabase/Postgres setup or troubleshooting

## Do not activate

- ORM or client-library setup only, no schema/query work → `routr-integrate`
- Query bug with unknown cause → `routr-debug`

## Iron law

**Every multi-tenant table ships with an RLS policy — no exceptions without a stated reason.**

## 0. Bootstrap

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `supabase-postgres-best-practices` | recommended — query perf, indexes |
| 2 | `symdex-code-search` | recommended — find models, migrations |
| 3 | `lean-ctx` | recommended — narrow schema reads |
| 4 | `supabase` | optional — Supabase projects only (auth, storage, SDK) |
| 5 | `find-docs` | optional — an ORM or driver API you can't verify |

**Budget gate:** rows 1–3 cover routine schema and query work. Pull `supabase` only when the repo is a Supabase project, and `find-docs` only for a specific unverified ORM or driver call.

**Skip:** `systematic-debugging` (wrong rows, cause unknown → `routr-debug`), `semgrep`, `firebase-security-rules-auditor` (audit beyond RLS → `routr-security`), `webapp-testing`, `vercel-react-best-practices` (app-level N+1 or latency → `routr-perf`).

## 1. Discover

SymDex for repositories/models; locate migrations; note RLS.

## 2. Schema & migrations

Backward-compatible when possible; indexes for new queries; RLS for multi-tenant.

Destructive or production changes stop for approval: before a `DROP`, column drop or rename, `TRUNCATE`, bulk `UPDATE`/`DELETE`, disabling RLS, or any migration run against a production database, show the exact SQL and wait for the user's go-ahead. Prefer a branch or staging database first.

## 3. Query work

Explain analyze for slow queries; N+1 detection; connection pooling.

## 4. Security

Escalate policy audit → `routr-security`

## Output format

```markdown
## Database report
**Change:** schema / migration / query
**RLS reviewed:** yes/no
**Verified:** explain analyze run, or test query confirmed
```

## Handoff

- API endpoints → `routr-integrate`
- Query bug → `routr-debug`
- Ship migration → `routr-ship`

## References

- [boundaries](./references/boundaries.md)
