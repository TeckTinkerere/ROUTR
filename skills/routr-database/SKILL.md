---
name: routr-database
description: "SQL, Postgres, Supabase schema and queries. Use when: migrations, RLS, slow queries, database design, Supabase. Not for: ORM or client-library setup (→ routr-integrate)."
---

# routr-database

**Goal:** correct, performant, secure data layer.

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

## Handoff

- API endpoints → `routr-integrate`
- Query bug → `routr-debug`
- Ship migration → `routr-ship`
