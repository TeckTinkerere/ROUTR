---
name: database-playbook
description: >
  Design queries, schema, migrations, and Postgres/Supabase best practices. Use
  when working with SQL, Postgres, Supabase, RLS policies, migrations, query
  performance, database schema, or backend data layer. Routes to supabase and
  supabase-postgres-best-practices skills. Use symdex for locating data access
  code in the repo.
---

# Database playbook

**Goal:** correct, performant, secure data layer.

## 0. Bootstrap

| Skill | Role |
|-------|------|
| `supabase-postgres-best-practices` | Query perf, indexes, Postgres patterns (260K+ installs) |
| `supabase` | Supabase auth, storage, client SDK, project setup |
| `symdex-code-search` | Find models, migrations, repositories in repo |
| `lean-ctx` | Read schema/migration files narrowly |
| `find-docs` | Current Supabase/Prisma/Drizzle API docs |

## 1. Discover existing data layer

1. SymDex: search symbols for repositories, models, `supabase`, `prisma`, `drizzle`
2. Locate migrations folder and latest schema
3. Note RLS / auth boundaries

## 2. Schema & migrations

- [ ] Backward-compatible migration when possible
- [ ] Indexes for new query patterns (`supabase-postgres-best-practices`)
- [ ] RLS policies for Supabase multi-tenant data

## 3. Query work

- Explain analyze for slow queries
- N+1 detection in ORM usage
- Connection pooling awareness

## 4. Security

- No secrets in client bundles
- Escalate policy audit → `security-review-playbook` (Firebase/Firestore rules skills if applicable)

## Handoff

- API exposing new endpoints → `library-integration-playbook`
- Bug in query results → `debugging-playbook`
- Ship migration → `fix-and-ship-playbook`
