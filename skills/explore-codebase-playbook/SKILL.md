---
name: explore-codebase-playbook
description: >
  Understand how a repository works without fixing a specific bug. Use when the
  user asks how something works, wants architecture explanation, onboarding,
  where is X defined, data flow, or system overview. Routes to symdex-code-search
  and lean-ctx for token-efficient discovery. Uses normal prose (not caveman).
  Does not load frontend design skills unless explaining UI architecture.
---

# Explore codebase playbook

**Goal:** accurate mental model with minimal file reads.

## 0. Bootstrap

Read if present:

1. `symdex-code-search`
2. `lean-ctx`
3. `context-fundamentals` — only if explaining context/agent implications

**Skip:** `caveman` (use clear prose for teaching), `frontend-design` unless UI structure is the subject.

## 1. Frame the question

- [ ] Restate what the user wants to understand (one paragraph max)
- [ ] Identify entry points: routes, main(), CLI commands, key modules

## 2. Map (SymDex)

1. Index if needed: `symdex index`
2. `repo summary` / file outlines / route list
3. For "how does feature X flow": `build_context_pack` with tight token budget
4. Callers/callees for critical symbols

## 3. Read (lean-ctx)

Progressive disclosure:

1. `map` or `signatures` on relevant files
2. `lines:N-M` for implementation detail
3. Full read only when signatures insufficient

## 4. Explain

Structure answer as:

1. **Overview** — what it does in plain language
2. **Flow** — numbered steps or diagram (mermaid if helpful)
3. **Key files** — with paths and one-line roles
4. **Extension points** — where a developer would plug in

## 5. Frontend architecture

If exploring UI layer:

- Note component tree, state management, styling approach
- Defer visual design opinions → `frontend-feature-playbook`

## Handoff

- User wants to build UI → `frontend-feature-playbook`
- User found a bug while exploring → `debugging-playbook`
