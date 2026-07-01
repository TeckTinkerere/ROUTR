# Video generation skills — ROUTR leaderboard

Ranked for **agent coding workflows** (not generative AI video like Sora). Scores blend [skills.sh](https://skills.sh) installs, workflow quality, and how often agents pick the right tool.

**Last reviewed:** July 2026

---

## Top 10

| # | Skill | Installs | Stack | Best for | Playbook |
|---|-------|----------|-------|----------|----------|
| 1 | `remotion-best-practices` | **401K+** | Remotion | React/TS video code, captions, charts, Lambda scale | `video-remotion-playbook` |
| 2 | `brag` | 61+ · 716★ | HyperFrames | **One-command launch video from the repo you just built** | `video-launch-playbook` |
| 3 | `hyperframes` | bundle | HyperFrames | Entry router — HTML compositions, all workflows | `video-generation-playbook` |
| 4 | `product-launch-video` | bundle | HyperFrames | Product URL / brief → 30–90s promo | `video-launch-playbook` |
| 5 | `pr-to-video` | bundle | HyperFrames | GitHub PR → changelog / feature video | `video-launch-playbook` |
| 6 | `website-to-video` | bundle | HyperFrames | Site tour, portfolio, homepage social clip | `video-launch-playbook` |
| 7 | `remotion-video-toolkit` | 671 | Remotion | Alternate Remotion rules — fallback only | `video-remotion-playbook` |
| 8 | `faceless-explainer` | bundle | HyperFrames | Explain a topic from text — no product URL | `video-launch-playbook` |
| 9 | `motion-graphics` | bundle | HyperFrames | Short unnarrated kinetic type / stat hit | `video-launch-playbook` |
| 10 | `embedded-captions` | bundle | HyperFrames | Subtitles on existing talking-head footage | `video-launch-playbook` |

---

## Honorable mentions

| Skill | When to use |
|-------|-------------|
| `talking-head-recut` | Overlays on interview footage (lower-thirds, callouts) |
| `music-to-video` | Beat-synced lyric / slideshow from a track |
| `slideshow` | Interactive deck — output is navigable slides, not MP4 |
| `general-video` | Multi-scene or custom HyperFrames when nothing else fits |
| `remotion-to-hyperframes` | **Port** Remotion → HyperFrames (migration only) |
| `hyperframes-core` / `hyperframes-animation` / `hyperframes-media` / `hyperframes-cli` | Load on demand after `hyperframes` routes you |

---

## Stack decision (30 seconds)

```
Need a video?
├─ "Brag about this project" / just shipped        → brag (video-launch-playbook)
├─ Product launch / SaaS promo from URL or brief   → product-launch-video
├─ PR / changelog / release notes                  → pr-to-video
├─ Site tour / portfolio clip                      → website-to-video
├─ Explain a concept (no product)                  → faceless-explainer
├─ Parametric / data-driven / React codebase       → remotion-best-practices (video-remotion-playbook)
├─ Custom HTML composition / edit existing HF work → hyperframes entry skill
└─ Captions on existing MP4                        → embedded-captions
```

**Default for "I built it, make a share video":** `brag` → hands off to HyperFrames.

**Default for "video as code in our repo":** `remotion-best-practices`.

---

## Install bundles

```bash
# ROUTR playbooks
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

**Prerequisites (HyperFrames / brag):** Node.js 22+, FFmpeg on `PATH`, `npx hyperframes doctor`.

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
