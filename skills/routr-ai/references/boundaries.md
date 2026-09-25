# routr-ai boundaries

| Situation | Use instead |
|-----------|-------------|
| Multi-agent architecture or eval harness | `routr-agents` |
| Chat UI styling only, no logic change | `routr-frontend` |
| SDK version-upgrade errors specifically | `migrate-ai-sdk-v6-to-v7` (child skill directly) |
| Eval harness / scoring answer quality, even for a RAG pipeline | `routr-agents` — wiring the RAG pipeline itself stays here |

See [routr-agents boundaries](../../routr-agents/references/boundaries.md#routr-agents-vs-routr-ai) for the canonical statement of the routr-ai/routr-agents split.
