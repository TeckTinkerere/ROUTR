# routr-video boundaries

| Situation | Use instead |
|-----------|-------------|
| CSS or Framer Motion animation in the live app | `routr-motion` |
| Landing page copy, positioning, distribution | `routr-marketing` |
| Build the marketing page itself | `routr-frontend` |
| The query or export feeding a data video | `routr-database` |
| Batch render pipeline, cloud deploy | `routr-deploy` |
| Manual screen recording | Out of scope — no router |
| Re-editing footage: re-timing, recolor, reframe, reorder, audio surgery | Out of scope — that is NLE work |
| Unclear video vs design | Ask two questions max, then pick a reference |

## Internal splits

| Confusion | Resolution |
|-----------|------------|
| brag vs product-launch-video | Same workspace → `brag`. External product URL or brief → `product-launch-video` |
| promo vs tour | Site is selling something → promo. Site shown as-is → tour |
| captions vs recut | Plain spoken subtitles → `embedded-captions`. Designed overlay cards → `talking-head-recut` |
| one data video vs a batch | Does the *render* repeat? No → HyperFrames. Yes → Remotion |
| video vs deck | Navigable slides with presenter mode → `slideshow`, output is not an MP4 |

## Workflows vs capability layers

A **workflow** owns the deliverable end to end — its own project directory, gated steps, and final artifact. A **capability layer** (`media-use`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-creative`, `hyperframes-registry`) is pulled in mid-flight and never owns the task. Loading two workflows for one deliverable is the iron-law violation; loading three capability layers under one workflow is normal.

## Precedence over self-declared entry points

The installed `hyperframes` skill may describe itself as the default for "any video request." That claim covers stack execution once HyperFrames is selected — it does not skip `routr-video`'s workflow selection (brag vs product-launch-video vs pr-to-video vs Remotion vs a data batch). Route here first; see [resolution.md](../../routr-catalog/references/resolution.md#stack-entry-points-vs-workflow-selectors).

## Actions that need the user, not the agent

- Rendering the final deliverable — pause at preview, let the user edit in Studio, render on approval
- Any paid call the agent initiated (HeyGen TTS beyond free usage, avatar renders, cloud image generation)
- Provisioning cloud render infrastructure
- Publishing or posting the video anywhere public
