---
name: routr-ai
description: "Build AI features with Vercel AI SDK (chat, agents, RAG, tools). Use when: chatbot, LLM, streaming, embeddings, tool calling, AI SDK, RAG. Not for: multi-agent architecture or eval harness (→ routr-agents); chat UI styling only (→ routr-frontend)."
---

# routr-ai

**Goal:** production AI features — streaming, tools, providers.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Role |
|-------|-------|------|
| 1 | `ai-sdk` | generateText, streamText, useChat, tools |
| 2 | `migrate-ai-sdk-v6-to-v7` | SDK upgrades |
| 3 | `find-docs` | Provider API docs |
| 4 | `routr-agents` | Multi-agent architecture |
| 5 | `routr-integrate` | Provider setup |

Chat UI → pair with `routr-frontend`.

## 1. Patterns

| Pattern | Stack |
|---------|-------|
| Chat UI | useChat + streamText + routr-frontend |
| Agents + tools | ToolLoopAgent + tool-design |
| RAG | embeddings + vector store |

## 2. Safety

API keys server-side; rate limits; prompt injection awareness.

## Handoff

- SDK upgrade errors → `migrate-ai-sdk-v6-to-v7`
- Stream bug → `routr-debug`
- Multi-agent → `routr-agents`
- Chat UI polish → `routr-frontend`
- Deploy → `routr-deploy`
- Marketing → `routr-marketing`

## Anti-patterns

- Client-side API keys
- Production agents without `routr-agents`
