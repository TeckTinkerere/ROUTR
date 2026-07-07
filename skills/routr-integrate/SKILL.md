---
name: routr-integrate
description: "Integrate a third-party library using up-to-date docs. Use when: 'how do I use X', SDK setup, API syntax, version migration, configure library. Not for: internal codebase exploration (→ routr-explore); debugging a library error (→ routr-debug)."
---

# routr-integrate

**Goal:** version-aware integration matching repo patterns.

## 0. Bootstrap

1. `find-docs` — **always** for API details
2. `symdex-code-search` — existing usage in repo
3. `lean-ctx` — narrow reads

UI libs: `shadcn`, `framer-motion-animator` as needed.

## 1. Verify docs

Never guess APIs. Check `package.json` version vs docs.

## 2. Repo alignment

SymDex for imports/config; match conventions.

## 3. Implement

Minimal working example; types compile; linter clean.

## 4. Frontend libraries

| Type | Also read |
|------|-----------|
| Component UI | `shadcn`, `tailwind-design-system` |
| Motion | `framer-motion-animator` |
| General UI | `frontend-design` for layout |

## Handoff

- Full new page → `routr-frontend`
- Motion polish → `routr-motion`
