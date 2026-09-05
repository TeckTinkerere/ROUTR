# Video launch workflow

Launch, PR, site-tour, and explainer workflows for `routr-video`. Product promos have their own file — [product-marketing.md](./product-marketing.md). Stack configuration lives in [hyperframes.md](./hyperframes.md).

## Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `brag` | Launch clip for **this workspace** |
| 2 | `product-launch-video` | External product URL, brief, or script |
| 3 | `pr-to-video` | GitHub PR or code change |
| 4 | `website-to-video` | Site tour, portfolio, homepage clip |
| 5 | `faceless-explainer` | Topic text only, no product, no URL |
| 6 | `motion-graphics` | Short kinetic piece, under ~10s, unnarrated |
| 7 | `music-to-video` | A music track drives the pacing |
| 8 | `talking-head-recut` | Designed overlay cards on existing footage |
| 9 | `embedded-captions` | Plain subtitles on existing footage |
| 10 | `slideshow` | Navigable deck, not an MP4 |
| 11 | `general-video` | Multi-scene, over ~3 min, static loop, or custom |

```bash
npx skills add latent-spaces/brag@brag heygen-com/hyperframes -g -y --copy
```

Prereqs: Node 22+, FFmpeg, and a clean `npx hyperframes doctor --json` payload.

## Route tree

```
Input?
├─ Current repo / "brag" / just shipped     → brag
├─ Commercial product URL, brief, script    → product-marketing.md
├─ Non-commercial site, shown as-is         → website-to-video
├─ GitHub PR                                → pr-to-video
├─ Topic text, no product                   → faceless-explainer
├─ Dataset, metrics, per-record variants    → data-video.md
├─ Music track, no narration                → music-to-video
├─ Existing MP4 → plain subtitles           → embedded-captions
├─ Existing MP4 → designed overlays         → talking-head-recut
├─ Discrete slides, presenter mode          → slideshow
├─ Motion-only graphic under ~10s           → motion-graphics
└─ None of the above                        → general-video
```

**Disambiguation, only where genuinely confusable:**

- **Same workspace → `brag`. External product URL → `product-launch-video`.** This is the split that gets it wrong most often.
- **A URL** — is the site selling a product? Yes → promo. No, or the user wants the site shown as-is → tour.
- **Existing footage** — plain spoken subtitles → captions; designed cards → recut. Neither re-edits the footage itself.
- **Length is a guide, not a gate.** Intent picks the workflow; go to `general-video` only when the piece is clearly long, static, or a custom format.

## brag pass

1. Read `brag/SKILL.md`
2. Parse tone, format, duration
3. Output → `brag-output/` (plan, brief, rendered MP4, share copy)

## HyperFrames pass

Read `hyperframes/SKILL.md` for workflow selection, then [hyperframes.md](./hyperframes.md) for the CLI dev loop, flags, gates, and cloud render. Load capability skills only as the workflow calls for them.

Audio is a decision point, not a step: run the sign-in preflight and relay it before generating voice or music — [media.md](./media.md).

## Share and ship

1. Share copy comes out of the workflow — refine with `routr-marketing`
2. Landing page embed → `routr-frontend`
3. Posting to a public channel is the user's call, not yours
