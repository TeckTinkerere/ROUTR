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
- [ ] Registered in `routr-router`
- [ ] Row in `skill-registry.md`
- [ ] `references/boundaries.md` if overlaps siblings
- [ ] Deprecated redirect if renaming existing skill
- [ ] Eval prompt in `evals/` for high-traffic routers
- [ ] `bash scripts/validate-skills.sh` passes locally — CI runs it on every PR

The validator mechanically checks the first four items above (name/folder match, `Use when:` presence, router-tree + resolution.md listing, every referenced child skill resolving to a `skill-registry.md` row). It cannot check design quality — boundaries, evals, and redirect correctness are still a human review job.
