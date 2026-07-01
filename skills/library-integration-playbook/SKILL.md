---
name: library-integration-playbook
description: >
  Integrate or configure third-party libraries using current documentation.
  Use when the user asks how to use a named library, framework, SDK, CLI tool,
  or cloud service API; migration between versions; or setup/configuration for
  dependencies like React, Next.js, Prisma, Tailwind, Framer Motion, etc. Routes
  to find-docs (Context7) before relying on training data. Combines with symdex
  to find existing usage patterns in the user's repo.
---

# Library integration playbook

**Goal:** correct, version-aware integration aligned with this repo's patterns.

## 0. Bootstrap

Read if present:

1. `find-docs` (Context7) — **always** for API details
2. `symdex-code-search` — find how this repo already uses the library
3. `lean-ctx` — read existing integration files narrowly

For UI libraries also load:

4. `shadcn` — if shadcn/ui stack
5. `framer-motion-animator` — if integrating Motion / Framer Motion

## 1. Verify docs (Context7)

Never guess API signatures from memory.

1. Ensure Context7 CLI: `npm install -g ctx7@latest` if needed
2. Query current docs for exact version user mentioned (or latest stable)
3. Note breaking changes vs user's installed version (`package.json`, lockfile)

## 2. Repo alignment (SymDex)

1. Search repo for existing imports / config of this library
2. Match conventions: file location, naming, env vars, test patterns

## 3. Implement

- [ ] Minimal working example in project's style
- [ ] Config files updated (env example if secrets)
- [ ] Types compile / linter clean

## 4. Frontend libraries

| Library type | Also read |
|--------------|-----------|
| Component UI | `shadcn`, `tailwind-design-system` |
| Motion | `framer-motion-animator`, `motion-design` |
| General UI | `frontend-design` for layout that uses the library |

## 5. Verify

- Run build or relevant test
- If docs conflict with repo patterns, prefer repo conventions and note the delta

## Handoff

- Building a full new page with this library → `frontend-feature-playbook`
- Animation polish only → `frontend-motion-playbook`
