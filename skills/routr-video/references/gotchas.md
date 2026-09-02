# Video gotchas

1. **Wrong stack**: 15s brag clip → `brag` beats spinning up Remotion project.
2. **Parallel loads**: Loading Remotion + HyperFrames wastes context — pick one path.
3. **Toolkit duplication**: Don't install `remotion-video-toolkit` alongside official skill.
4. **Missing doctor**: HyperFrames fails mysteriously without `npx hyperframes doctor`.
5. **In-app vs export**: Framer Motion in web app is `routr-motion`, not this skill.
6. **Deadline pressure**: under ~15 min to a demo/judging deadline, skip clarifying questions — take all defaults (16:9, burned-in captions, ~15–25s), go straight to `brag`, and run the smoke render before anything else. A failed full render with 3 minutes left has no recovery path; a failed smoke render at minute 2 does.
7. **Failed render near deadline**: no time to debug a broken composition → fall back to a screen capture of the working app + `embedded-captions`, or ship stills. Don't spend the last 10 minutes debugging FFmpeg.
8. **Muted judging**: demo-day and hackathon judges frequently watch with sound off — burn in captions by default for any judged/social deliverable, not just when explicitly requested.
