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

## Deprecated names

If a user references an old `*-playbook` name (removed in v2), use the `routr-*` equivalent. See [docs/naming.md](../../../docs/naming.md).
