## What and why

<!-- One or two sentences. Link the issue (misroute / new router / bug) if there is one. -->

## Type

- [ ] Description change (routing behaviour)
- [ ] New or changed router
- [ ] Scripts / tooling / CI
- [ ] Docs only

## Checklist

- [ ] `bash scripts/validate-skills.sh` passes with no new FAIL or WARN
- [ ] `python scripts/run-evals.py` run before and after; router accuracy did not regress (paste both numbers below)
- [ ] New or changed behaviour has eval prompts in `evals/` (misroutes: the reported prompt is added)
- [ ] `routes.json` updated if handoffs, companions or chains changed
- [ ] New router is registered in `routr-router`, `resolution.md` and `skill-registry.md`
- [ ] `CHANGELOG.md` updated under the unreleased section
- [ ] Commit messages follow Conventional Commits

## Eval results

```
before:
after:
```

<!-- For description changes, also note whether you ran --mode claude or a blind --mode predictions run. -->
