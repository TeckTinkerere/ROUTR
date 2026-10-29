---
name: routr-depth-ship
description: "Commit and PR discipline when caveman-commit is not installed. Use when: routr-ship needs commit message format, or user asks to ship without commit helper skill."
---

# routr-depth-ship

Fallback depth for `routr-ship`. Load only when `caveman-commit` is not installed.

## Iron law

**No commit without verification.**

## Verify gate

- [ ] Re-run reproduction or project test command
- [ ] Review `git diff` — no accidental files
- [ ] Linter clean on touched files

## Commit format

```
<type>(<scope>): <imperative summary>

<optional body: why, 1-2 sentences>
```

Types: `fix`, `feat`, `refactor`, `test`, `chore`, `docs`

## PR minimum

```markdown
## Summary
…

## Test plan
- [ ] …
```

## Scope

Typical fix ≤ 3 files. Escalate scope with user if larger.

## Install full skill

```bash
npx skills@1.7.4 add JuliusBrussee/caveman -g --skill caveman-commit -y --copy
npx skills@1.7.4 add obra/superpowers -g --skill requesting-code-review -y --copy
```
