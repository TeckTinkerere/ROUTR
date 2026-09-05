# Video generation skills — ROUTR leaderboard

Ranked for **agent coding workflows** (not generative AI video like Sora). Scores blend [skills.sh](https://skills.sh) installs, workflow quality, and how often agents pick the right tool.

**Last reviewed:** September 2026

---

## Top 10

| # | Skill | Installs | Stack | Best for |
|---|-------|----------|-------|----------|
| 1 | `remotion-best-practices` | **401K+** | Remotion | React/TS video code, captions, charts, Lambda scale |
| 2 | `brag` | 61+ · 716★ | HyperFrames | **One-command launch video from the repo you just built** |
| 3 | `hyperframes` | bundle | HyperFrames | Entry router — HTML compositions, all workflows |
| 4 | `product-launch-video` | bundle | HyperFrames | Product URL / brief → 30–90s promo |
| 5 | `pr-to-video` | bundle | HyperFrames | GitHub PR → changelog / feature video |
| 6 | `website-to-video` | bundle | HyperFrames | Site tour, portfolio, homepage social clip |
| 7 | `remotion-video-toolkit` | 671 | Remotion | Alternate Remotion rules — fallback only |
| 8 | `faceless-explainer` | bundle | HyperFrames | Explain a topic from text — no product URL |
| 9 | `motion-graphics` | bundle | HyperFrames | Short unnarrated kinetic type / stat hit |
| 10 | `embedded-captions` | bundle | HyperFrames | Subtitles on existing talking-head footage |

---

## Honorable mentions

| Skill | When to use |
|-------|-------------|
| `media-use` | **The media layer for every stack** — voice/TTS, BGM, SFX, transcription, captions, background removal, avatar upsell, cross-project asset cache |
| `talking-head-recut` | Overlays on interview footage (lower-thirds, callouts) |
| `music-to-video` | Beat-synced lyric / slideshow from a track |
| `slideshow` | Interactive deck — output is navigable slides, not MP4 |
| `general-video` | Multi-scene or custom HyperFrames when nothing else fits |
| `remotion-to-hyperframes` | **Port** Remotion → HyperFrames (migration only) |
| `hyperframes-core` / `hyperframes-animation` / `hyperframes-keyframes` / `hyperframes-creative` / `hyperframes-cli` / `hyperframes-registry` | Capability layers — load on demand after `hyperframes` routes you, never as a workflow |

---

## Stack decision (30 seconds)

```
Need a video?
├─ "Brag about this project" / just shipped        → brag
├─ Product launch / SaaS promo from URL or brief   → product-launch-video
├─ PR / changelog / release notes                  → pr-to-video
├─ Site tour / portfolio clip                      → website-to-video
├─ Explain a concept (no product)                  → faceless-explainer
├─ Parametric / data-driven / React codebase       → remotion-best-practices
├─ Custom HTML composition / edit existing HF work → hyperframes entry skill
├─ Captions on existing MP4                        → embedded-captions
├─ Music track drives the pacing                   → music-to-video
├─ Navigable deck, presenter mode                  → slideshow
└─ Anything else / multi-scene / long / loop       → general-video
```

**Two axes, not one.** A *workflow* owns the deliverable; a *capability layer* (`media-use`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-creative`, `hyperframes-registry`) is pulled in mid-flight. Loading two workflows for one video is the mistake; loading three layers under one workflow is normal.

**Default for "I built it, make a share video":** `brag` → hands off to HyperFrames.

**Default for "video as code in our repo":** `remotion-best-practices`.

---

## Install bundles

```bash
# ROUTR routers
npx skills add TeckTinkerere/ROUTR -g --all -y --copy

# #1 Remotion (skills.sh)
npx skills add remotion-dev/skills@remotion-best-practices -g -y --copy

# #2 Launch video from current project
npx skills add latent-spaces/brag@brag -g -y --copy

# HyperFrames core + all workflows (brag, product-launch, pr-to-video, …)
npx skills add heygen-com/hyperframes -g --all -y --copy

# Optional Remotion alternate
npx skills add shreefentsar/remotion-video-toolkit@remotion-video-toolkit -g -y --copy
```

**Prerequisites (HyperFrames / brag):** Node.js 22+, FFmpeg on `PATH`, and a clean `npx hyperframes doctor --json` payload (the command exits 0 even when the environment is broken — gate on the payload field).

**Audio quality is one switch.** Voice, music, sound effects, images, and avatar presenters all degrade based on whether a HeyGen credential resolves. Run `npx hyperframes auth status` and relay it before generating audio — full table in `routr-video/references/media.md`.

---

## Why brag ranks #2 overall but #1 for launch

`remotion-best-practices` wins on **installs** (401K+) and is the right default when the deliverable is a **maintained Remotion project**.

`brag` wins when the user wants a **finished MP4 + share copy** from the **current codebase** with minimal decisions — it plans the story, briefs HyperFrames, and renders. Low skills.sh installs (new); high GitHub stars and benchmark quality.

---

## Sources

| Skill | Repository |
|-------|------------|
| `remotion-best-practices` | [remotion-dev/skills](https://github.com/remotion-dev/skills) |
| `brag` | [latent-spaces/brag](https://github.com/latent-spaces/brag) |
| HyperFrames bundle | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| `remotion-video-toolkit` | [shreefentsar/remotion-video-toolkit](https://github.com/shreefentsar/remotion-video-toolkit) |
