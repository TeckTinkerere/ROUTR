---
name: routr-explore
description: "Explain how the codebase works without changing code. Use when: 'how does X work', architecture, onboarding, where is this defined, walk me through. Not for: a specific bug (→ routr-debug); changing code (→ routr-ship)."
---

# routr-explore

**Goal:** accurate mental model with minimal file reads.

## 0. Bootstrap

1. `symdex-code-search`
2. `lean-ctx`
3. `context-fundamentals` — only if agent/context implications

**Skip:** `caveman`, `frontend-design` unless UI structure is the subject.

## 1. Frame question

Restate goal; identify entry points (routes, main, CLI).

## 2. Map (SymDex)

Index → summary → `build_context_pack` → callers/callees

## 3. Read (lean-ctx)

`map` → `signatures` → `lines:N-M` → full only if needed

## 4. Explain

Overview → Flow → Key files → Extension points

## 5. Frontend architecture

Component tree, state, styling — defer design opinions → `routr-frontend`

## Handoff

- Build UI → `routr-frontend`
- Bug while exploring → `routr-debug`
