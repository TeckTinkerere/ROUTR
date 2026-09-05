# Video Remotion workflow

Remotion workflow for `routr-video` — React programmatic video. Per-record batches live in [data-video.md](./data-video.md).

## Bootstrap

| Priority | Skill | When |
|----------|-------|------|
| **1** | `remotion-best-practices` | Always |
| 2 | `remotion-video-toolkit` | Only if the official skill is missing |
| 3 | `media-use` | Voice, music, SFX, captions — see [media.md](./media.md) |
| 4 | `find-docs` | API edge cases |

```bash
npx skills add remotion-dev/skills@remotion-best-practices -g -y --copy
```

## When Remotion (not launch or HyperFrames)

| Signal | Remotion |
|--------|----------|
| Remotion already in the repo | Yes |
| Thousands of renders from JSON props | Yes |
| Wrapped-style per-user recap | Yes |
| User says Remotion or create-video | Yes |
| One-shot launch clip from the current app | No → [launch.md](./launch.md) → `brag` |

## New project

```bash
npx create-video@latest --yes --blank --no-tailwind my-video
```

Load rules **progressively** — the skill ships 40 of them; reading them all at once is the failure mode.

**Layout first:** open the video-layout rule before writing scenes. Video is not a web page — text sizing and density differ.

## Non-negotiables

- Animate with the current-frame hook and the interpolate helper. Prefer interpolate over spring unless the motion is genuinely physics-like; customize timing with bezier easing.
- **CSS transitions, CSS animations, and Tailwind animation classes are forbidden** — they do not render correctly.
- Keep the interpolate call inline in the style prop and use individual transform properties rather than composing a transform string, so the animation stays editable in Studio.
- Assets live in the public folder and are referenced through the static-file helper. Use the framework's own image, video, and audio components, not raw HTML tags.
- Delay with a sequence and its from prop; limit with its duration prop. Sequences are absolute-fill by default — pass the no-layout option for inline content.

## Composition configuration

Width, height, fps, and duration are declared on the composition in the project root file. When any of them depend on the data, use a metadata function instead of hardcoding: it can fetch (with the abort signal it is handed), then return duration, dimensions, and merged props together. Add a schema to the props to make a parametrized composition safe and Studio-editable.

## Rule index — load only what the task needs

| Task | Rule |
|------|------|
| Scene layout and text sizing | video-layout |
| Dynamic duration, dimensions, props | calculate-metadata |
| Parametrized props schema | parameters |
| Stills, folders, nested compositions | compositions |
| Delay, trim, limit | sequencing, trimming, timing |
| Scene transitions | transitions |
| Captions and subtitles | subtitles, display-captions, import-srt-captions, transcribe-captions |
| Voiceover | voiceover |
| Audio trim, volume, speed, pitch | audio |
| Waveforms, spectrum, bass-reactive | audio-visualization |
| Sound effects | sfx |
| Silence trimming, FFmpeg operations | silence-detection, ffmpeg |
| Fonts | google-fonts, local-fonts |
| Images, GIFs, Lottie, 3D, maps | images, gifs, lottie, 3d, maplibre |
| Measuring DOM nodes or text | measuring-dom-nodes, measuring-text |
| Transparent output | transparent-videos |
| Visual and pixel effects | effects, light-leaks, html-in-canvas |
| Tailwind | tailwind |

Effect preference order: plain CSS/SVG/filter/blend/mask first, then a listed effect, then a custom effect factory when the user wants it reusable, and only then a custom canvas paint hook.

## Build pass

1. Load only the rules matching the current step
2. Composition, props schema, metadata function if anything is dynamic
3. Preview: `npx remotion studio`
4. Optional cheap check: `npx remotion still <id> --scale=0.25 --frame=30` (frame is zero-based, so at 30fps that is the one-second mark)
5. Render: `npx remotion render`, or Lambda for batches

## Port to HyperFrames

Migration only, and only when the user explicitly asks → `remotion-to-hyperframes`. A passing mention of Remotion is not a trigger.

## Ship

- Batch or pipeline deploy → `routr-deploy`
- Marketing page embed → `routr-frontend`
- Launch clip from a product site → [launch.md](./launch.md)
