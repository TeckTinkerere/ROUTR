# Debug fallback (no child skills installed)

Use when `systematic-debugging` and `routr-depth-debug` are both unavailable.

## Iron law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## Minimum process

1. **Capture symptom** — exact error text, test name, steps
2. **Reproduce** — if cannot reproduce, gather logs; do not guess
3. **Localize** — narrow to file/line via stack trace or binary search
4. **One hypothesis** — predict cause; read only evidence for that hypothesis
5. **Fix smallest diff** — address cause, not symptom
6. **Verify** — re-run reproduction

## When stuck

- Read git diff for recent changes
- Add temporary logging at component boundaries
- Ask user for environment details (OS, node version, env vars)

## Escalate to install

```bash
npx skills@1.7.4 add obra/superpowers -g --skill systematic-debugging -y --copy
npx skills@1.7.4 add mattpocock/skills -g --skill diagnosing-bugs -y --copy
```
