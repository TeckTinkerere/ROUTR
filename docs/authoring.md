# Authoring ROUTR skills

How to add or update a `routr-*` skill. Based on the [Agent Skills spec](https://agentskills.io) and Anthropic skill-creator patterns.

## Skill types

| Type | Purpose | Max SKILL.md |
|------|---------|--------------|
| Router (`routr-{domain}`) | Match situation → order child skills | ~150 lines |
| Catalog (`routr-catalog`) | Install registry, resolution | ~50 lines |
| Depth fallback (`routr-depth-{domain}`) | Minimum expertise when child missing | ~200 lines |

Routers **route**. They do not duplicate full child skill content.

## Folder layout

```
skills/routr-debug/
├── SKILL.md
└── references/
    ├── workflow.md      # Phased steps when child present
    ├── fallback.md      # Minimum process if children missing
    ├── gotchas.md       # Failure modes
    ├── examples.md      # Input → expected behavior
    └── boundaries.md    # Do not activate + precedence
```

## SKILL.md template

```markdown
---
name: routr-example
description: "One line WHAT. Use when: trigger1, trigger2, user phrases."
---

# routr-example

**Goal:** one sentence.

## When to activate
- Bullet triggers

## Do not activate
- Adjacent skill owns this: `routr-other`

## Iron law
One non-negotiable rule.

## 0. Bootstrap
| Order | Skill | Tier |
If missing required child → read `routr-depth-example` OR `references/fallback.md`.

## 1–N. Workflow steps
Checklists, freedom levels (high/medium/low).

## Handoff
| Next | Skill |

## Anti-patterns

## References
- [workflow](./references/workflow.md)
```

## Freedom levels

| Level | When |
|-------|------|
| High | Multiple valid approaches |
| Medium | Preferred pattern, some variation OK |
| Low | Fragile sequence — follow exactly |

## Child skill references

Always use **canonical** names from `skill-registry.md`. Never invent aliases in router bodies.

## Checklist before PR

- [ ] `name` matches folder name
- [ ] Description is third person with `Use when:`
- [ ] Description ≤ 280 chars (hard fail at 320)
- [ ] Situational routers include `Not for:` with at least one concrete redirect
- [ ] `SKILL.md` ≤ 150 lines for routers, ≤ 200 lines for `routr-depth-*`
- [ ] Registered in `routr-router`
- [ ] Entry in `skills/routr-catalog/references/routes.json` (`routers.<name>` with `handoff`, `companions`, `owns_domain_failures`); add a chain or companion pairing if the router belongs to one
- [ ] `handoff` in `routes.json` matches the router's `## Handoff` section (the validator WARNs on drift); chains stay at 3 steps or fewer
- [ ] A companion `section` anchor points at a real heading (e.g. a short "Companion checklist" section)
- [ ] Row in `skill-registry.md`
- [ ] `references/boundaries.md` if overlaps siblings
- [ ] Deprecated redirect if renaming existing skill
- [ ] Eval prompt required for every router — not just high-traffic ones; `evals/*.eval.json` must include at least one `expected_router` entry
- [ ] Run `python scripts/run-evals.py` and check it reports your router's prompts scoring as expected
- [ ] `bash scripts/validate-skills.sh` passes locally — CI runs it on every PR

The validator mechanically checks 12 items: name/folder match, `Use when:` presence, referenced child skills resolving to a `skill-registry.md` row, no duplicate registry rows, router-tree + resolution.md listing, description length budget, `Not for:` presence, SKILL.md line caps, broken relative links in `references/`, eval JSON validity, eval coverage per router, and `routes.json` integrity (see [routing.md](routing.md)). It cannot check design quality — boundaries, eval prompt quality, and redirect correctness are still a human review job. See [architecture.md](architecture.md#quality-loop) for the full list.
