# Video gotchas

## Routing

1. **Wrong stack.** A 15s brag clip beats spinning up a Remotion project. Same workspace → `brag`; external product URL → `product-launch-video`.
2. **Parallel loads.** Remotion plus HyperFrames for one clip wastes context and produces two half-finished pipelines. Pick one.
3. **Toolkit duplication.** Don't install `remotion-video-toolkit` alongside the official Remotion skill.
4. **In-app vs export.** Framer Motion inside the running app is `routr-motion`, not this router.
5. **Deck vs video.** "Slides", "presentation", "pitch deck" → `slideshow`; the deliverable is navigable, not an MP4. Confirm before authoring if the wording is ambiguous.

## Pipeline

6. **Missing doctor.** HyperFrames fails mysteriously without a clean environment check — and `doctor --json` exits 0 even when broken, so gate on the payload field, not the exit code.
7. **Static gates miss sub-compositions.** Lint, validate, and inspect each composition in isolation and never mount sub-compositions. Only a seek-based snapshot pass catches a mount failure — the symptom is a scene rendering as background-only, or unstyled text in the top-left corner.
8. **Silent success.** Exit code 0 is not a rendered video. Check the file exists, is non-empty, and has the expected duration.
9. **Auto-rendering.** Passing checks is not user approval. Pause at preview and let the user edit in Studio first.
10. **Cloud render without consent.** Lambda deploy provisions billable AWS infrastructure and its teardown retains the S3 bucket. Confirm before deploying, clean up after.

## Audio and media

11. **Generating audio before the sign-in preflight.** No credential is not a green light for silent local fallback — relay the status output verbatim and stop for the user's choice.
12. **Voice drift.** Voice ids are provider-specific. Pin the provider whenever you pin a voice, or the voice silently changes with the environment.
13. **Silent translation.** The transcription default translates non-English audio instead of transcribing it. Always pass the model explicitly.
14. **Vague effect queries.** "Dramatic sound" retrieves nothing useful; "glass shatter" does. A miss skips rather than failing, so a vague query loses the cue without an error.
15. **Editing generated captions.** Preset caption HTML is build output. Fix the skin source or use the workflow's override — editing the generated file gets overwritten on the next build.

## Content

16. **Invented numbers.** A statistic, customer quote, or logo wall added to fill a beat is a real-world claim. Cut the beat instead — see [data-video.md](./data-video.md) and [product-marketing.md](./product-marketing.md).
17. **Vertical as a crop.** A 9:16 cut is a different composition, not a center-crop of the 16:9. Plan for the tighter frame or budget a second pass.
18. **Publishing on the user's behalf.** Render and hand over the file. Posting to a public channel is always the user's call.

## Deadline

19. **Under ~15 minutes to a demo or judging deadline:** skip clarifying questions, take all defaults (16:9, burned-in captions, ~15–25s), go straight to `brag`, and run the smoke render before anything else. A failed full render with three minutes left has no recovery path; a failed smoke render at minute two does.
20. **Failed render near the deadline:** fall back to a screen capture plus `embedded-captions`, or ship stills. Don't spend the last ten minutes debugging FFmpeg.
21. **Muted judging.** Demo-day and hackathon judges frequently watch with sound off. Burn in captions by default for anything judged or social, not only when asked.
