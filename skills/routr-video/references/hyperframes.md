# HyperFrames stack configuration

Read this **after** `routr-video` picks a HyperFrames workflow. HyperFrames renders video from HTML: a composition is an HTML file whose DOM declares timing with `data-*` attributes, whose animation runtime is seekable, and whose media playback is owned by the framework.

## Layer map — load on demand, never all at once

| You need | Skill |
|----------|-------|
| Composition contract: clips, tracks, sub-compositions, variables, determinism | `hyperframes-core` |
| Motion: atomic rules, scene blueprints, transitions, runtime adapters | `hyperframes-animation` |
| Seek-safe keyframes: timelines, FLIP, paths, masks, SVG morph, 3D | `hyperframes-keyframes` |
| Brand direction: frame presets, palettes, typography, narration, beat plan | `hyperframes-creative` |
| Voice, BGM, SFX, transcription, captions, background removal | `media-use` — see [media.md](./media.md) |
| CLI dev loop and cloud render | `hyperframes-cli` |
| Prebuilt blocks and components | `hyperframes-registry` |

A **workflow** (`product-launch-video`, `pr-to-video`, `general-video`, …) owns the deliverable end to end. These layers are capabilities it pulls in — they never own the task.

## Workflow selection inside the stack

| Input | Workflow |
|-------|----------|
| Product / SaaS / company URL, brief, or script | `product-launch-video` |
| Non-commercial site shown as-is (portfolio, docs, event) | `website-to-video` |
| Topic or article text, no product and no URL | `faceless-explainer` |
| GitHub PR or code change | `pr-to-video` |
| Existing talking-head MP4 + plain subtitles | `embedded-captions` |
| Existing talking-head MP4 + designed overlay cards | `talking-head-recut` |
| Under ~10s, unnarrated, the motion is the message | `motion-graphics` |
| A music track drives the pacing | `music-to-video` |
| Discrete slides, fragments, presenter mode — a deck, not an MP4 | `slideshow` |
| Anything else, multi-scene, longer than ~3 min, static loop | `general-video` |
| Porting an existing Remotion composition | `remotion-to-hyperframes` |

If the matched workflow isn't installed, don't improvise a substitute:

```bash
npx skills add heygen-com/hyperframes --skill pr-to-video
```

`npx skills add heygen-com/hyperframes --all` installs core plus every workflow.

## CLI dev loop

Everything runs through `npx hyperframes` unless the project defines a local wrapper — obey the wrapper exactly. Requires Node.js 22+ and FFmpeg.

| Step | Command | Catches |
|------|---------|---------|
| Scaffold | `npx hyperframes init my-video` | also refreshes the installed skill set from GitHub |
| Lint | `npx hyperframes lint` | missing composition id, overlapping tracks, unregistered timelines |
| Validate | `npx hyperframes validate` | runtime console errors + WCAG contrast, in headless Chrome |
| Inspect | `npx hyperframes inspect` | text spilling out of containers or off canvas across the seek |
| Snapshot | `npx hyperframes snapshot --frames 9` | cross-file sub-composition mount failures |
| Preview | `npx hyperframes preview` | opens Studio — the user can edit, not just watch |
| Render | `npx hyperframes render --quality draft` | iteration |
| Deliver | `npx hyperframes render --quality high --output out.mp4` | final |
| Reproducible | `npx hyperframes render --docker --strict --output out.mp4` | CI / cross-host |

**Render is user-gated.** Passing checks is not permission. Pause at preview, say the video is editable in Studio, render only after the user approves.

## Configuration flags worth knowing

| Flag | Effect |
|------|--------|
| `--json` | Available on every command except render, preview, and play server modes; wraps output in a `_meta` envelope and redacts `$HOME` from paths |
| `--strict` | Render fails on lint errors |
| `--strict-all` | Render fails on warnings too |
| `--strict-variables` | Render fails on undeclared variables keys |
| `--variables` | Parametrized render; keys must be declared via the composition-variables attribute on the root element |
| `--non-interactive` | Force CI mode on a TTY; non-TTY auto-detects, and scaffolding then requires an example |
| `--quality draft` / `--quality high` | Iteration vs delivery encode |
| `--at 2,7,14` / `--frames 9` | Snapshot at sub-composition midpoints, or evenly spaced |

Environment: `HYPERFRAMES_SKIP_SKILLS=1` opts CI out of the skills freshness check.

## Registry blocks and components

`hyperframes add <name>` installs reusable pieces. **Blocks** are standalone sub-compositions with their own dimensions and timeline, included via a composition-src attribute. **Components** are effect snippets pasted inline. Paths are configurable in the project's HyperFrames JSON config — a registry URL plus block, component, and asset directories. The printed snippet is a starting point — you still wire the composition id, start, duration, and track index yourself. Details: `hyperframes-registry`.

## Cloud rendering

Use Lambda when a render is too long or too large for one host — multi-minute pieces, 4K, large parallel batches — and AWS credentials are configured. Stay on local render for the dev loop.

```bash
npx hyperframes lambda deploy
npx hyperframes lambda render ./my-project --width 1920 --height 1080 --wait
npx hyperframes lambda destroy
```

Six subcommands: deploy, sites create, render, progress, destroy, policies. Tearing the stack down retains the S3 bucket — clean it up explicitly. Deploy touches cloud infrastructure and costs money: confirm with the user first. Handoff to `routr-deploy` if this becomes a maintained pipeline.

## Completion gate

Static gates (lint + validate) evaluate each composition **in isolation** — they never mount sub-compositions, so they cannot catch cross-file failures. When the project uses sub-compositions, a seek-based snapshot pass is mandatory. Read `snapshots/frame-NN-at-Xs.png` against the scene plan:

| What you see | Root cause |
|--------------|------------|
| Tiny unstyled text top-left | style block left outside the template — no CSS reached the live DOM |
| SVG blown up to canvas size | same — no width/height constraints applied |
| Hero element missing, only background visible | host id does not match template id — the timeline never ran |
| "Sub-composition timelines not registered" in the log | same, direct confirmation |

After render exits 0, confirm the file exists and is non-empty, and sanity-check duration with `ffprobe`. Then report feedback once per task: `npx hyperframes feedback --rating 5 --comment "..."`, lower rating when you hit friction, with the failing pattern in the comment.

## Creative direction

Before choosing colors or writing HTML for anything non-trivial, `hyperframes-creative` wants two of its references read first — its house style and video-composition guides. They exist because web instincts produce web-page-looking video: video wants higher density, larger scale, and foreground metadata. A project design spec (frame, design, or DESIGN markdown, in that precedence) is brand truth — frontmatter tokens are normative, prose is context. Ready-made frame presets can be adopted as the project spec when the user has no brand.
