# routr-spec boundaries

| User's deliverable | Owner |
|--------------------|-------|
| PRD for a feature that has not been built | `routr-plan` — intended future |
| Existing app as an as-built PRD, compared with old requirements | `routr-spec` — current product reality and drift |
| Explain authentication's code flow | `routr-explore` — codebase understanding |
| Current authentication contract versus original requirements | `routr-spec` |
| Review a PR for correctness/style | `routr-review` |
| Product behavior changed since the last specification checkpoint | `routr-spec` |
| Implement known missing PRD requirements | `routr-ship`; unresolved scope first goes to `routr-plan` |
| Refactor internals while preserving behavior | `routr-refactor` |
| Product spec for a shipped Electron app with insufficient source | `routr-spec`, with optional `reverse-engineer-anything` for the evidence gap |
| Decompile a binary / inspect an APK method, without product-spec work | Direct `reverse-engineer-anything`; ROUTR need not insert a domain selector |

PRD is a document format, not proof of future planning. "Reverse engineer" describes an approach, not proof that artifact tooling is needed. Route by the requested result and available evidence.

An as-built spec alone also belongs here; a missing baseline is recorded rather than invented. Code exploration inside reconciliation is a source-gathering phase, not an automatic second router. Assessing whether implementation matches original intent is reconciliation; judging whether a diff is good is review.

## Handoffs and scope

Only `routr-plan` and `routr-ship` are outgoing handoffs: after recording drift, the user may request a decision about desired behavior or a known implementation. Do not add review/explore steps merely because reading code or checking evidence occurred. A separate requested review can be re-routed as a new job when needed.

Incoming `routr-ship` → `routr-spec` is for explicitly requested post-implementation reconciliation. The optional plan → ship → spec chain requires all three deliverables and a change suitable for ship. Keep max three steps, one active router, and re-route after each exit. Do not infer permission to commit/push from a request to update specification artifacts.
