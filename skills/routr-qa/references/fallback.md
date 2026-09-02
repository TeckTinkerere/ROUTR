# QA fallback (no browser-automation skill installed)

Use when both `agent-browser` and `webapp-testing` are unavailable and there's no `routr-depth-qa` to fall back to.

## Iron law

```
CLAIM NOTHING WORKS UNTIL YOU'VE ACTUALLY DRIVEN THE BROWSER AND SEEN IT
```

## Minimum process

1. **Confirm there's something to drive** — a local dev server, a deployed preview, or a running app. If none exists, say so; don't fabricate a result.
2. **Use whatever browser tool the host provides directly** — most agent hosts expose a browser/computer-use tool even without a dedicated QA skill loaded. Use it plainly: navigate, click, read the page, screenshot on failure.
3. **Define the checklist before starting** — the critical paths that must work (load, primary action, one write operation). Don't wander without a target.
4. **Evidence per item** — screenshot, console error, or network response for every pass/fail, not a summary judgment.
5. **Report and hand off** — bugs found go to `routr-debug`, not fixed inline here.

## When stuck

- No host browser tool at all → ask the user to run the check themselves and report back what to look for
- Preview URL requires auth you don't have → ask the user rather than guessing credentials

## Escalate to install

```bash
npx skills add vercel-labs/agent-browser -g -y --copy
npx skills add anthropics/skills@webapp-testing -g -y --copy
```
