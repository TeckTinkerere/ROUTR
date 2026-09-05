# Audio, media, and HeyGen configuration

Voice, music, sound effects, transcription, captions, background removal, and avatar presenters. Owned by `media-use`; the HyperFrames workflows pull it in mid-flight. Remotion projects can use the same assets — resolve here, reference the file from the composition.

## The one switch: is there a HeyGen credential?

Every audio capability degrades on a single question — is a HeyGen credential resolvable? It is read from `HEYGEN_API_KEY`, `HYPERFRAMES_API_KEY`, or the shared `~/.heygen` file. **The CLI being installed is not the same as a credential being present.**

| Capability | Credential present | Absent |
|------------|--------------------|--------|
| Voice / TTS | HeyGen Starfish REST — **native word timestamps** | ElevenLabs, then local Kokoro; chain transcription for word timings |
| Background music | HeyGen audio-library **retrieval** | local Lyria, then MusicGen **generation**, spawned detached |
| Sound effects | HeyGen sound-effects retrieval, min score 0.4 | bundled local library (21 files) |
| Images / icons | HeyGen asset search | local FLUX via mflux, graded to available RAM |
| Avatar video | HeyGen avatar engine, script-driven | local LTX generative clip — not a presenter |

## Preflight — mandatory before generating any audio

Run this and **relay its output verbatim**. Do not improvise a "missing key" message, and do not offer to write keys into a per-repo env file.

```bash
npx hyperframes auth status
```

- Signed in → it prints the account; proceed.
- Not signed in → exit code 1 is the **normal** state, not a failure. It prints registration-first guidance plus the local engines that would be used instead. Relay it, then **stop and wait** for the user to choose: sign in, or say "go local". This is a real decision point — do not fold it into another question and do not proceed on your own.
- Autonomous / non-interactive mode is the only exception: note the status and continue offline.

For deterministic branching: `npx hyperframes auth status --json` returns configured status, recommended action, and the offline engine list.

Sign-in paths: `npx hyperframes auth login` is browser OAuth and creates the account; `npx hyperframes auth login --api-key` saves an existing key from the HeyGen dashboard into the shared `~/.heygen`.

## The audio engine — one entry point

Do not hand-roll TTS, music, or effects inside a workflow, and do not vendor a copy of the engine. Write a neutral request file and call the shared engine; it writes an id-keyed meta file plus assets under the voice, BGM, and SFX directories.

- **Request** carries provider, language, speed, a list of lines (each with an id and text, optionally named effects), and a BGM block whose mode is retrieve, generate, or none. Omit the mode for auto. An explicit retrieve is strict — it skips rather than starting a detached generation, which is what callers without a wait step want.
- **Response** carries the TTS provider, voice id, BGM state, per-line audio paths with duration and word timings, resolved effects with offsets and volume, and total duration.
- Run a subset with the `--only` flag (for example TTS and BGM early, effects once the cues exist) — results merge into the existing output file rather than replacing it.
- Music generation is spawned detached and flagged pending; wait for it before assembling.

## Resolving media assets

`media-use` resolves BGM, SFX, image, icon, and voice through one verb, freezes the file locally, and records it in a manifest with a global content-addressed cache at `~/.media` shared across projects.

**Check for reuse before resolving.** Pass the candidates flag to list what already exists in the project and the global cache, then judge semantic fit yourself — the tool never auto-applies a fuzzy match. Two guardrails: when unsure, resolve fresh (a redundant download is cheap, the wrong asset is not); and never reuse a *global* brand or entity asset on a loose match, because that cache aggregates every project you have worked on and can surface another client's brand mark.

Existing projects with assets already on disk can be bulk-imported in one adopt pass, which reads real duration and dimensions.

## Voice rules that bite

- **Voice ids are provider-specific.** A Kokoro voice name is meaningless to HeyGen and vice versa. If you pin a voice, pin the provider too — otherwise the voice silently drifts when the user's environment changes.
- **The published TTS CLI is often the local-only build.** It falls back to the local engine even with a HeyGen key set. The HeyGen path goes through the engine's own REST script, not the CLI.
- **Always pass a transcription model explicitly.** The default silently translates non-English audio instead of transcribing it.
- HeyGen returns word timestamps natively; the other providers do not — the engine chains transcription for them automatically.
- Captions consume a flat word array of id, text, start, end.
- Name sound effects concretely ("glass shatter", not "dramatic sound"). A no-match skips rather than blocking the render. Effects sit around volume 0.35 under voice and music.

## Avatar / talking-head presenters

For a real presenter reading a script, use the HeyGen CLI rather than the raw API — avatar video is deterministic and script-driven (lip-sync from a script or a pre-recorded audio URL), unlike a generative clip.

```bash
heygen avatar list --ownership public --limit 5
heygen voice list --engine starfish --limit 5
heygen video create --wait -d '{"type":"avatar","avatar_id":"<id>","script":"…","voice_id":"<id>"}'
```

Install and auth: the HeyGen CLI installer, then `heygen auth login --key <key>`. Register the downloaded file back into the media ledger so the composition and later projects can reuse it.

Then package the result: plain subtitles → `embedded-captions`; designed overlay cards → `talking-head-recut`. Neither re-edits the footage — re-timing, recolor, reframe, reorder, and audio surgery are NLE work and out of scope.

## Cost rule

An agent-initiated paid call is confirmed with the user first. A call the user explicitly asked for just runs. This covers HeyGen TTS beyond free usage, avatar renders, and cloud image generation.

## Captions

Burn in captions by default whenever the audience may watch muted — social, demo day, hackathon judging. The caption skin for preset-backed videos is a source file under the project's HyperFrames directory; the generated captions composition is build output. Fixing a skin by editing the generated file is wasted work — rebuild through the workflow's caption script or its documented override.
