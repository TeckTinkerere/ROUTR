# routr-agents boundaries

| Situation | Use instead |
|-----------|-------------|
| Single AI SDK chat/RAG feature, no architecture question | `routr-ai` |
| Agent UI (chat window, controls, transcript view) | `routr-frontend` |
| Wrong file reads mid-implementation | `routr-debug` |

## routr-agents vs routr-ai

`routr-ai` builds one production feature on the Vercel AI SDK. `routr-agents` is for the architecture question underneath it — pattern, harness, memory, eval loop — that applies once the feature involves more than one agent, a self-correction loop, or a context/memory design decision. A single `streamText` + `useChat` chatbot is `routr-ai`; a research agent that plans, calls tools, and self-corrects is `routr-agents`.
