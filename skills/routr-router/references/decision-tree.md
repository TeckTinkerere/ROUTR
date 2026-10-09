# Extended decision tree

## Overlap resolution

### "Fix the UI" — bug or design?

- Error in console / wrong data → `routr-debug`
- Looks ugly / layout wrong, logic OK → `routr-frontend`
- Animation janky → `routr-motion`

### "Ship the feature"

- Still planning → `routr-plan`
- Building UI → `routr-frontend`
- Tests needed → `routr-test`
- Ready to commit → `routr-ship`
- Go live → `routr-deploy`

### Video vs frontend

- Exported MP4 file → `routr-video`
- Animation inside web app → `routr-motion`
- Landing page with embedded video → `routr-frontend` then `routr-video` for asset

### AI feature

- SDK wiring, streaming, tools → `routr-ai`
- Multi-agent architecture, eval harness → `routr-agents`
- Chat UI → `routr-ai` + `routr-frontend`

### Slow vs broken

- Wrong output, crash, exception → `routr-debug`
- Correct output but slow (page load, API, render) → `routr-perf`
- One specific slow query / index design → `routr-database`
- App-level N+1, connection-pool exhaustion, latency across many queries → `routr-perf`
- Janky/dropped-frame animation: diagnose the cause → `routr-perf`; author/polish the fix → `routr-motion`
- Layout/visual only, no speed complaint → `routr-frontend`

## Domain machinery vs generic debug

The domain's own machinery beats generic debug; the domain router uses its own gotchas and hands to `routr-debug` only if the root cause turns out to be outside the domain.

- Agent loop drifting or stalling → `routr-agents`
- AI SDK stream or `useChat` stuck/looping → `routr-ai`
- Blank or failed video render → `routr-video`
- EAS build or Expo config failing → `routr-mobile`
- Migration runner or RLS policy misbehaving → `routr-database`
- Application logic merely using the domain (a query returning wrong rows, a component with a bad prop) → `routr-debug`

## Multi-intent requests

Plan the route (max 3 steps) per [SKILL.md](../SKILL.md#route-plans). Chains: [routes.json](../../routr-catalog/references/routes.json). "Feature with a planning gap and a build" starts at `routr-plan`; a contested start (plan vs frontend) is acceptable either way as long as the plan is announced.

## Deprecated names

If a user references an old `*-playbook` name (removed in v2), use the `routr-*` equivalent. See [docs/naming.md](../../../docs/naming.md).
