# Capability 11: Audio Pro (vocal isolation, enhance voice, noise reduction, music + ducking)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0914 (4)-copy`. It is the agent-owned duplicate of `0914 (4)`, 7:30.533 of
  Egyptian-Arabic talking head on 7 main-track clips of `VID_20260720_190542.mp4`. It carries the
  approved rung 4–10 edits: cuts, punch-ins, push-in, house captions, title, and the PiP B-roll
  (muted).
- **Evidence:** `evidence/2026-09-14/cap11/`

## Goal
Improve the talking head's sound with CapCut's native audio tools, and optionally add background
music that sits under the voice. Every change must be verified two ways:
- **in the draft:** which audio materials and flags each tool writes
- **by measurement:** before and after loudness/noise stats from an audio render. The agent can't
  listen, so numbers stand in for ears.

## Preconditions
- Rungs 0–10 approved. House style (`references/house-style.md`) is unaffected by audio.
- Known routes (rung 0, unverified runs):
  - Inspector **Audio ▸ Basic**: Volume (dB), Fade in/out, **Normalize loudness** (Pro), **Enhance
    voice** (Pro, ▾), Video translator (Pro)
  - **Audio ▸ Voice changer** sub-tab (not wanted here)
  - Clip right-click **Isolate voice ›** (Keep vocal / Remove vocal), marked "Free"
  - Asset **Audio ▸ Music ▾** library (categories Summer, Phonk, Vlog, Tense, …; ⬇ download per
    track)
- Not yet located: a dedicated **Reduce noise** control and **auto ducking**.
- Credits: none of the Pro tools run so far showed a credit prompt. Follow the user's credit answer
  below, and stop at any cost or upsell dialog (`pro-features.md` rules).
- **Measurement plan:** the agent cannot hear the timeline. Options:
  - export a short section (rung 15 is not approved yet, so only if the user agrees)
  - analyse CapCut's processed audio caches, if the tools write files
  - otherwise rely on the draft plus the waveform on screen

  Decide with evidence and record the choice.

## Plan
1. **Baseline:** draft summary; list the audio-related fields per main clip (volume, `sound_channel_mappings`,
   `vocal_separations`, any `audio_effects` / loudness / enhance flags). Screenshot the main track
   waveform.
2. **Map before running:** select a main clip, open Audio ▸ Basic, expand **Enhance voice ▾**, and
   screenshot every option. Look for noise reduction, then for ducking in the music clip's
   inspector. Right-click ▸ Isolate voice › submenu. No clicks that apply anything yet.
3. **Run each chosen treatment** on the chosen scope, one at a time. After each:
   - wait for processing (loading window or progress in the tree / screenshot)
   - diff the draft, and check the inspector state
   - run an undo/redo gate
4. **Music (if chosen):**
   - Audio ▸ Music: show candidates, and the user picks one.
   - Download it, then add it to its own audio track under the talk.
   - Set volume and ducking, trim to the talk length, add a fade out.
   - Verify in the draft: audio track, segment timing, volume, ducking flag.
5. **Verify:** the draft (materials and flags per clip), waveform screenshots before and after,
   and measurements per the plan above. Captions, title, B-roll and keyframes unchanged. Save,
   scope check.

## Procedure

### A. Baseline (executed 2026-09-14, read-only)
- **Draft:** `cap11/baseline.json`
  - 4 tracks, 248 segments, draft 21:17:23
  - `diff` vs rung-10 `final.json` = No differences
- **Audio fields per main clip** (`audio_check.py "0914 (4)-copy" --track 0` → `audio-before.json`):
  - All **7** segments have volume **1.0**, `last_nonzero_volume` 1.0, `enable_adjust` true.
  - Refs: `sound_channel_mappings` (type `none`, mapping 0) and `vocal_separations` (`choice` 0,
    `removed_sounds` [], `production_path` "", `final_algorithm` ""). Five segments also carry an
    empty `material_animations`.
  - **No** loudness, enhance or noise material exists anywhere. The project's material categories
    are canvases, effects, material_animations, material_colors, placeholder_infos,
    sound_channel_mappings, speeds, text_templates, texts, videos, vocal_separations.
- **Project folder:** `folder-before.txt`, 38 files, **no `Resources` folder** and no audio files.
- **Source audio:** `VID_20260720_190542.mp4` has AAC LC stereo, 48 kHz, 96 kb/s.
- **Measurements** (bundled ffmpeg, clip 0's source range `-ss 46.933 -t 122.2`):
  - EBU R128: **I −14.2 LUFS**, LRA 4.7 LU (−17.8…−13.1), **true peak −1.4 dBFS**.
  - Per-second RMS (123 windows): p05 **−26.2**, p10 −23.7, p25 −19.5, **median −17.0**, p75
    −15.9, p95 −14.2 dBFS. Quietest seconds −32.5, −28.8, −28.5 dBFS. These gaps between phrases
    serve as the noise-floor proxy. Output: `rms-before-clip0.txt`.
  - **Command pitfall:** writing ametadata to a `file=` path failed silently, because
    PowerShell/ffmpeg path escaping lost it. Use `ametadata=mode=print:key=lavfi.astats.Overall.RMS_level`
    and regex `RMS_level=` out of captured stderr instead.
- **Where processed audio may land (lead, read-only):**
  - The user's own `0914 (6)` has `Resources\audioAlg\<hash>_0_3000000.mp3` (written 20:02:47).
    CapCut's audio algorithms appear to write per-clip results into the project's
    `Resources\audioAlg`, which is measurable after a treatment.
  - `Cache\recognize\*.m4a(.pcm)` holds transcription audio from captions and transcript.
  - `0914 (6)` is the user's and is **not** touched: listing only.

## Wait conditions

## Verification

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes

## User choices (2026-09-14)
- **Treatments:** **Enhance voice (Pro)**, **Noise reduction** (control still to find in 9.4), and
  **Normalize loudness (Pro)**. User's words: "Enhance voice (Pro), Noise reduction, Normalize
  loudness (Pro)". Isolate voice was not chosen.
- **Music:** **none**. User's words: "No music". Ducking is out of scope for this demonstration.
  The ladder title keeps it for a later request.
- **Credits:** "Run them; stop if a cost appears (Recommended)". Run the Pro audio tools, but stop
  and ask at any dialog showing a credit cost or upsell.
- **Scope:** "Whole talk, all 7 clips (Recommended)". All 7 main-track clips.

## Open questions for the user
