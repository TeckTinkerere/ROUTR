---
name: agent-design-playbook
description: "Design multi-agent systems, context windows, and eval harnesses. Use when: building agents, memory, tools, or context engineering."
---

# Agent design playbook

**Goal:** principled agent architecture — not ad-hoc prompt stacking.

## 0. Bootstrap

Read `playbook-common/references/skill-catalog.md` and install context-engineering bundle if missing.

Load by sub-task (read only what applies):

| Sub-task | Skill |
|----------|-------|
| Concepts / onboarding | `context-fundamentals` |
| Agent degrading mid-session | `context-degradation` |
| Long session handoff | `context-compression` |
| Token budget / caching | `context-optimization` |
| Multiple agents | `multi-agent-patterns` |
| Persistent knowledge | `memory-systems` |
| Tool schemas / MCP | `tool-design` |
| File-based context | `filesystem-context` |
| Production loops | `harness-engineering` |
| Quality measurement | `evaluation`, `advanced-evaluation` |
| LLM product shape | `project-development` |

Runtime layer (when implementing, not just designing):

- `lean-ctx` — compression, routing, memory at execution time

**Skip:** `frontend-design`, `caveman` unless user explicitly wants terse agent docs.

## 1. Clarify the system

- [ ] Single agent or multi-agent?
- [ ] Human-in-the-loop or autonomous?
- [ ] Context budget constraint (model, cost, latency)?
- [ ] Eval criteria defined?

## 2. Design pass

1. Read `context-fundamentals` if team lacks shared vocabulary
2. Pick coordination pattern (`multi-agent-patterns`) if >1 agent
3. Define tool surface (`tool-design`) — fewer, better tools
4. Define memory boundaries (`memory-systems`, `filesystem-context`)

## 3. Operational loop

For production agents:

1. `harness-engineering` — locked metrics, rollback, approval gates
2. `evaluation` — deterministic checks + regression suite

## 4. Implement

- Prototype harness before scaling prompts
- Use `lean-ctx setup` if deploying context compression layer

## Handoff

- Debugging a coding agent's wrong file reads → `debugging-playbook` + `symdex-code-search`
- Building user-facing UI for the agent → `frontend-feature-playbook`
