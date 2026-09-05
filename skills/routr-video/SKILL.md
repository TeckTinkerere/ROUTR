---
name: routr-video
description: "Pick and run the right video workflow — launch, product marketing, data-driven, Remotion, or HyperFrames. Use when: make a video, promo, explainer, launch clip, /brag, render MP4, motion graphic, captions, avatar video, Remotion, product video. Not for: in-app UI animation (→ routr-motion)."
---

# routr-video

**Goal:** route to the best **code-rendered** MP4 workflow — not Sora/Runway generative footage.

## When to activate

- User wants a video, promo, launch clip, explainer, deck, or captions
- `/brag`, Remotion, HyperFrames, MP4 export, alpha overlay
- PR video, site tour, product promo, data recap, avatar presenter

## Do not activate

- In-app UI animation (not exported video) → `routr-motion`
- Marketing copy only → `routr-marketing`
- Screen recording → `agent-browser` / manual capture

## Iron law

**One workflow owns the deliverable; capability skills are loaded mid-flight, never in parallel with a second workflow.** Never load Remotion + HyperFrames for the same clip.

## 0. Bootstrap

Install missing from `routr-catalog/references/skill-registry.md` (Video table).

| Order | Skill | Tier |
|-------|-------|------|
| 1 | `brag` | required — same-workspace launch clip |
| 2 | `remotion-best-practices` | required — React/parametric video |
| 3 | `hyperframes` | recommended — HTML stack entry once selected |
| 4 | `media-use` | recommended — voice, BGM, SFX, captions, HeyGen credential |
| 5 | `product-launch-video` | optional — external product URL/brief |
| 6 | `pr-to-video` | optional — GitHub PR / changelog |

If `brag` and `hyperframes` are both missing → read [references/fallback.md](./references/fallback.md).

`hyperframes` may describe itself as the default for any video request. That claim covers stack execution once selected, not workflow selection — see [references/boundaries.md](./references/boundaries.md#precedence-over-self-declared-entry-points). Route from this file first.

**Pre-flight gate (low freedom) — before any render:**

- [ ] Node 22+, FFmpeg on `PATH`
- [ ] HyperFrames path: `npx hyperframes doctor --json` payload `ok` is true (the command exits 0 even when broken — gate on the field, not the exit code)
- [ ] Audio needed: `npx hyperframes auth status` run and its output relayed verbatim before generating voice or music — see [references/media.md](./references/media.md)
- [ ] A 3–5s smoke render succeeds before the full-length render

Skipping this is the most common way a video task fails late instead of early.

## 1. Quick route

Pick **one** row, then read only that reference.

| User intent | Reference | Workflow |
|-------------|-----------|----------|
| Brag / launch for **this repo** | [launch](./references/launch.md) | `brag` |
| Sell a product from URL, brief, or script | [product-marketing](./references/product-marketing.md) | `product-launch-video` |
| Tour a non-commercial site | [launch](./references/launch.md) | `website-to-video` |
| PR / changelog video | [launch](./references/launch.md) | `pr-to-video` |
| Explain a topic, no product | [launch](./references/launch.md) | `faceless-explainer` |
| Numbers, metrics, recap, per-record variants | [data-video](./references/data-video.md) | Remotion or HyperFrames |
| React/parametric video codebase | [remotion](./references/remotion.md) | `remotion-best-practices` |
| Custom HTML composition, deck, music, footage | [hyperframes](./references/hyperframes.md) | `hyperframes` |
| Voice, music, SFX, captions, avatar presenter | [media](./references/media.md) | `media-use` |

Leaderboard: `routr-catalog/references/video-skills-leaderboard.md`

## 2. Clarify (max 2 questions)

If unclear:

1. **Input** — repo, product URL, PR, topic text, dataset, footage, music track, or Remotion project?
2. **Output** — launch clip (~15–25s), promo (30–90s), navigable deck, or maintained video codebase?

Defaults — **state them, don't ask**: 16:9 (9:16 only for a named vertical destination), the user's language, burned-in captions when the audience may watch muted.

If there's a hard deadline (demo day, hackathon judging, live event), ask it as a third question and let it override defaults — see [references/gotchas.md](./references/gotchas.md) for the low-time path.

## 3. Execute

Follow the matched reference only. Capability skills (`media-use`, `hyperframes-creative`, `hyperframes-animation`, `hyperframes-registry`) are pulled in mid-flight by the workflow; they never own the task.

## 4. Verify (low freedom)

- [ ] Duration and aspect match the destination
- [ ] Captions present if the audience may be muted
- [ ] Sub-compositions used → a seek-based smoke check ran (`hyperframes snapshot`); lint/validate alone cannot catch mount failures
- [ ] Output file exists and is non-empty; duration confirmed with `ffprobe`
- [ ] Every number, quote, and claim on screen traces to a real source — see [references/data-video.md](./references/data-video.md)

## Output format

```markdown
## Video report
**Workflow:** brag / product-launch-video / pr-to-video / hyperframes / remotion-best-practices / …
**Capability layers used:** media-use (voice/BGM), creative preset, registry blocks
**Output:** path to rendered file(s)
**Duration / aspect / captions:** …
**Verified:** yes/no — smoke render + full render + file check
```

## Handoff

| Need | Router |
|------|--------|
| Share copy, positioning, distribution | `routr-marketing` |
| Landing page with embedded video | `routr-frontend` |
| Remotion Lambda / cloud render deploy | `routr-deploy` |
| Render kept failing | `routr-debug` |

## References

- [launch](./references/launch.md) — brag, PR, site tour, explainer
- [product-marketing](./references/product-marketing.md) — promos that sell
- [data-video](./references/data-video.md) — metrics, recaps, per-record variants
- [remotion](./references/remotion.md) — React programmatic video
- [hyperframes](./references/hyperframes.md) — HTML stack config, CLI, cloud render
- [media](./references/media.md) — HeyGen credential, voice, BGM, SFX, captions, avatars
- [fallback](./references/fallback.md) — when child skills are missing
- [gotchas](./references/gotchas.md) · [examples](./references/examples.md) · [boundaries](./references/boundaries.md)

## Anti-patterns

- `remotion-best-practices` + `hyperframes` for the same one-off launch
- Sora/Runway when the user wants version-controlled video code
- Auto-rendering the deliverable without pausing for user approval
- Generating voice or music before relaying the sign-in status
- Full-length render before a smoke render confirms the pipeline
