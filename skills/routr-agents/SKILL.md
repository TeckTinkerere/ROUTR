---
name: routr-agents
description: "Design multi-agent systems, agent loops, and eval harnesses. Use when: building agents, agent operating loop, research/self-correction loop, harness, memory, tools, context engineering, eval loop. Not for: a single AI SDK chat/RAG feature (→ routr-ai)."
---

# routr-agents

**Goal:** principled agent architecture — not ad-hoc prompt stacking.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`. **Load by sub-task only — never read the whole cluster.**

**Context engineering**

| Sub-task | Skill |
|----------|-------|
| Concepts | `context-fundamentals` |
| Degrading mid-session | `context-degradation` |
| Long handoff | `context-compression` |
| Token budget | `context-optimization` |
| File-based context | `filesystem-context` |
| Memory | `memory-systems` |
| Tools / MCP | `tool-design` |

**Loop engineering** (the operating loop — growing fast, pick per symptom)

| Sub-task | Skill |
|----------|-------|
| Design the agent operating / research loop | `harness-engineering` |
| Robust research loop (validation, error recovery) | `comprehensive-research-agent` |
| Debug a misbehaving loop (drift, tool confusion, repeat failures) | `reasoning-trace-optimizer` |
| Eval loop / quality gate | `evaluation`, `advanced-evaluation` |
| Multiple agents / handoffs | `multi-agent-patterns` |
| Subagent delegation loop | `subagent-driven-development` |
| Background / hosted / self-spawning loop | `hosted-agents` |
| Cross-agent memory briefing | `latent-briefing` |

Runtime: `lean-ctx` when implementing.

**Budget gate:** read one row per active symptom. Do not preload the context + loop clusters together.

**Skip:** `frontend-design`, `caveman` unless terse docs requested.

## 1. Clarify

Single vs multi-agent; human-in-loop; context budget; eval criteria.

## 2. Design

Pattern → tools → memory → harness.

## 3. Implement

Prototype harness before scaling prompts.

## Handoff

- Wrong file reads → `routr-debug` + symdex
- Agent UI → `routr-frontend`
