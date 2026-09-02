# QA gotchas

1. **Verification by reading code**: "the logic looks right so it works" is not QA — drive the browser and see the actual render/behavior.
2. **Silent failure on missing preview**: if there's no running app or deployed preview, say so — don't fabricate a "checked and it works" report.
3. **Permanent spec for a one-off check**: a quick "does this work" pass doesn't need a Playwright file left in the repo — that's `routr-test`'s job if coverage is wanted going forward.
4. **Fixing bugs found mid-QA**: report and hand off to `routr-debug` instead of patching inline — QA's job is to find and evidence, not silently fix.
5. **Vague checklist items**: "looks fine" isn't a pass/fail — every checklist item needs concrete evidence (screenshot, console log, network response).
