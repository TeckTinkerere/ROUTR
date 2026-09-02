---
name: routr-database
description: "SQL, Postgres, Supabase schema and queries. Use when: migrations, RLS, slow queries, database design, Supabase. Not for: ORM or client-library setup (→ routr-integrate)."
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

| Skill | Role |
|-------|------|
| `supabase-postgres-best-practices` | Query perf, indexes |
| `supabase` | Auth, storage, SDK |
| `symdex-code-search` | Find models, migrations |
| `lean-ctx` | Narrow schema reads |
| `find-docs` | ORM API docs |

## 1. Discover

SymDex for repositories/models; locate migrations; note RLS.

## 2. Schema & migrations

Backward-compatible when possible; indexes for new queries; RLS for multi-tenant.

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
