# routr-refactor boundaries

| Situation | Use instead |
|-----------|-------------|
| Fixing a bug — behavior must change | `routr-debug` then `routr-ship` |
| Feature work mixed in with the structure change | Split it — do the feature in `routr-ship`/`routr-frontend` separately |
| Reviewing someone else's refactor PR | `routr-review` |
