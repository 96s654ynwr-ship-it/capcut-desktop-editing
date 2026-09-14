# Capability 11: Audio Pro (vocal isolation, enhance voice, noise reduction, music + ducking)

## Status
- **Ladder status:** demonstrated
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14 (Claude Code). Reduce noise, Enhance voice (Intensity 75) and
  Normalize loudness (target -23 LUFS) are on all 7 main clips. Verified in the draft, the
  processing artefacts, the undo/redo gate and the save. The sound itself is not measured
  (needs an export).
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

### B. Open the copy, select a main clip, Audio tab (executed 2026-09-14, no changes)
1. Home: `scroll 1100 700 -5`, then a grid screenshot. The first card is **0914 (4)-copy**
   (≈383,682).
   - Click it; `MainWindow` shows on the first poll.
   - After ≈5 s, `focus --maximize`.
   - Title bar: **0914 (4)-copy**. The overlay row shows its **muted** speaker in cyan, from rung 10.
2. Click main clip 0's body (≈400,891). It is **selected** (white border, x 229–569) and the
   playhead stays at 00:00:00:00.
3. Inspector top tabs for a main clip: **Video · Audio · Speed · Animation · Adjust · A…›**. Click
   **Audio** (≈1553,70).
4. **Audio ▸ Basic** (`02-clip0-audio.png`):
   - Basic ✓ with reset and ◇, then **Volume** 0.0dB (≈1790,257), **Fade in** 0.0s (≈1790,311),
     **Fade out** 0.0s (≈1790,365).
   - **Normalize loudness** checkbox ≈(1468,433), Pro diamond, "Normalize the loudness of the
     selected clip or clips to a target level."
   - **Enhance voice** checkbox ≈(1468,523), ⓘ ≈(1590,523), Pro diamond, **▾** ≈(1629,523), reset
     ⟲ ≈(1880,523).
   - The draft mtime is unchanged by opening and selecting.
5. **Enhance voice ⓘ:** hovering (≈1590,523) for 1.5 s showed **no tooltip**
   (`03-enhance-info-tooltip.png`).
6. **Enhance voice ▾** (≈1629,523):
   - It **expands inline** below the row. The arrow turns to ▴, and an **"Intensity"** row appears,
     cut off by the inspector bottom (`04-enhance-dropdown.png`).
   - The checkbox stays **unticked**, and the draft is unchanged, so expanding does not apply
     anything.
   - A tool-type window (`Qt622QWindowToolSaveBits`) appeared in `cc.py windows` at the same time.
   - Scroll the inspector to see the expanded controls.
7. **Scroll the inspector** with the pointer on the label column (`scroll 1480 450 -3`, then `-4`).
   The second `-4` changed nothing, so that is the bottom. Draft unchanged. Full **Audio ▸ Basic**
   list for a main clip (`05/06/07-audio-scroll*.png`):

   | Control | Badge | Extras |
   |---|---|---|
   | Normalize loudness | Pro | description line only, no options |
   | Enhance voice | Pro | ⓘ, ▾/▴ → **Intensity** slider + stepper, default **75** (greyed until ticked), reset ⟲ |
   | Video translator | Pro | ⓘ, ▾, reset (not in scope) |
   | **Reduce noise** | Pro | **plain checkbox, no options.** This is the 9.4 noise-reduction control. |
   | Isolate voice | **Free** | ▾ (the same feature as right-click ▸ Isolate voice ›; not chosen) |
   | Fill channel | — | ⓘ, ▾, reset, keyframe ◇ (not in scope) |

   - At the bottom scroll position (inspector region origin 1446,40): Enhance voice checkbox
     ≈(1468,180), Intensity box ≈(1837,245), Video translator ≈(1468,312), **Reduce noise
     ≈(1468,382)**, Isolate voice ≈(1468,450), Fill channel ≈(1468,519).
   - Hovering near the bottom showed a "Show" tooltip. Normalize loudness is scrolled above view
     there.
8. **Select all 7 main clips** (whole-talk scope):
   - Click clip 0 (≈400,891), then `click <x> 891 --mod ctrl` on clips 1–6 at x = 740, 921, 945,
     1095, 1323, 1450 (fit zoom; clips 2 and 3 are only ≈17 and ≈30 px wide).
   - **Observed** (`09-multiselect.png`, `09-multiselect-track.png`): every main segment carries a
     white selection border, narrow ones included.
   - The inspector tabs shrink to **Video · Audio · Speed · Adjust** (Animation disappears for a
     multi-selection).
   - Audio ▸ Basic shows the same controls, **scrolled back to the top**, and the Enhance voice ▴
     expansion persists.
   - The toolbar greys out single-clip tools.
   - Draft unchanged (a selection isn't saved).
9. **Checkbox positions** with the 7-clip selection after `scroll 1480 450 -3`
   (`10-multi-audio-scrolled.png`, inspector origin 1446,40):
   - **Normalize loudness ≈(1468,232)**
   - **Enhance voice ≈(1468,323)**, with Intensity box ≈(1837,386)
   - Video translator ≈(1468,455)
   - **Reduce noise ≈(1468,524)**

### C. Reduce noise on all 7 clips (executed + agent-verified 2026-09-14)
1. With the 7-clip selection and the inspector scrolled `-3`, run
   `apply_watch.py reduce-noise 1468 524 --watch 90 --settle 4`. It clicks the **Reduce noise**
   checkbox once, then watches.
2. **Observed** (`reduce-noise/t0p5.png`, `final.png`):
   - The checkbox is **ticked** (cyan), and a **"Noise reduced"** toast appears over the timeline.
   - Title bar: "Auto saved: 21:41:46".
   - **No credit, cost, upsell or loading dialog.** The only new top-level window was a tooltip.
   - The 7-clip selection stays intact.
3. **Timing:** the draft saved **0.6 s** after the click, and the watcher settled at 8.9 s. There
   is no processing wait: it is a real-time filter.
4. **Agent-verified draft:**
   - New material category **`realtime_denoises`**, 0 → **7**, one per main segment, each added to
     that segment's `extra_material_refs`.
   - Fields: `type` "realtime_denoise", **`is_denoise` true**, `denoise_mode` 1.0, **`denoise_rate`
     0.85**, `sami_name` **"denoise_v2"** v1.0, `sami_type` 2, `is_from_hd_sounds` false.
   - Model: `D:/Bytedance/CapCut/Apps/9.4.0.4015/Resources/audiosami/unet_denoise_44k_music_model_v1.0.model`.
   - `diff` vs baseline: only `materials.realtime_denoises 0 → 7` plus `+ref realtime_denoises` on
     each of the 7 main segments. Volume stays 1.0, and nothing else changed.
   - **No new files** in the project folder (14 existing files re-saved). Nothing processed lands
     on disk, because the denoise runs at playback/export time. A before/after measurement
     therefore needs a rendered section; see Open questions.

### D. Enhance voice on all 7 clips (executed 2026-09-14)
1. With the same 7-clip selection (Reduce noise already ticked), run
   `apply_watch.py enhance-voice 1468 323 --watch 240 --settle 6`. It clicks the **Enhance voice**
   checkbox once. **Intensity was left at the default 75.**
2. **Observed immediately** (`enhance-voice/t2.png`, `t5.png`, `final.png`):
   - The checkbox is ticked, and the Intensity slider becomes active (75).
   - Right of the row: **"Enhancing voice… N%"** (36.7% at 2 s, 55.7% at 5 s, 74.4% at 12 s). That
     percentage is per current clip, not overall.
   - Player header: **"Applying 7 features… ▾"** with a spinner.
   - Every main clip's label is prefixed **"Waiting to enhance voice…"**.
   - **No credit, cost or upsell dialog** appeared.
3. **Draft, saved 0.6 s after the click, before processing:**
   - New category **`vocal_beautifys`**, one per main segment: `enable` true, **`ambient_sound_level`
     75** (the Intensity value), `voice_change_mode` null, `time_range` = that segment's source
     range.
   - `production_path` = `##_draftpath_placeholder_…_##/Resources/audioAlg/<hashB>_<srcStartµs>_<srcDurµs>.wav`,
     i.e. the result file each segment will play.
4. **Processing pipeline**, observed in the project's `Resources/audioAlg/`. Clips are handled **one
   at a time**, apparently shortest-first (the 10.6 s clip finished before the 6.1 s one). Per clip:
   1. `<hashA>_<start>_<dur>_upload.wav`: the source range extracted at 48 kHz stereo. Its size
      matches the enhanced output.
   2. `<hashC>_<start>_<dur>_vocal.wav` + `_background.wav`: a voice/background separation step,
      each about half the upload size.
   3. `<hashB>_<start>_<dur>.wav`: the enhanced result. It appears as a **0-byte placeholder
      first**, then is filled.
   - **Timings seen:**
     - 10.6 s clip done at +85 s
     - 6.1 s clip at +166 s
     - 122.2 s clip at +276 s
     - 97.0 s clip still 0 B at +377 s
     - The draft re-saved once mid-run (21:45:23).
   - About 1–2 min per clip including upload, so **allow ≈10–15 min for a 7:30 talk**.
5. **Completion (agent-verified):**
   - All **7** `<hashB>_<start>_<dur>.wav` results were non-empty and size-stable by **21:54:23**,
     ≈11 min after the click.
   - Final sizes: 1.88 MB (10.6 s) … 21.8 MB (123.5 s), which is 48 kHz stereo PCM.
   - The draft kept its 21:45:23 save; no further write happened at completion.
6. **UI during processing:** a frame at ~+4.5 min showed **"Applying 4 features…"**, the 7-clip
   selection **gone** (Details panel) and the playhead at **00:00:01:00**. The agent sent no input
   in that window. It was either CapCut clearing the selection on the mid-run re-save or the user
   touching the app.
   - `after-processing.png`: header back to "Player-Timeline 01", nothing selected, "Auto saved:
     21:45:23".
   - Top-level windows: MainWindow plus a tooltip only.
7. **Draft after processing** (`audio-after-enhance.json`, `diff` vs baseline):
   - **only** `materials.realtime_denoises 0→7`, `materials.vocal_beautifys 0→7`, and
     `+ref realtime_denoises; +ref vocal_beautifys` on each of the 7 main segments
   - every segment: volume 1.0, denoise `is_denoise` true / rate 0.85, enhance `enable` true /
     `ambient_sound_level` 75
   - rung-7 keyframes (2), title (1) and the overlay PiP (1) are unchanged
8. **Can the processed audio be measured from disk? No, not directly (agent-verified):**
   - `*_upload.wav` is a real RIFF/WAVE file (PCM s16le, 44.1 kHz stereo, `Lavf61.1`), the
     extracted source.
   - The **enhanced result** `<hashB>_…wav` and the separation outputs `_vocal.wav` /
     `_background.wav` are **not WAV**. Their first bytes are `2d 36 39 39 …` ("-699…"), which looks
     obfuscated or encrypted, and ffmpeg reports "Invalid data found when processing input".
   - So a before/after measurement of Enhance voice (and of the real-time Reduce noise, which writes
     nothing) needs an **export of a short section**. That is rung 15's area and not approved yet, so
     it goes to the user as an open question. Never decode CapCut's cache files.
9. **Source reference numbers** (bundled ffmpeg, `ebur128` **Summary block** + per-second astats RMS):

   | Range | Integrated | LRA | True peak | RMS/s p05 / p50 / p95 | Quietest second |
   |---|---|---|---|---|---|
   | clip 0 (src 46.933 + 122.2 s) | −14.2 LUFS | 4.7 LU | −1.4 dBFS | −26.2 / −17.0 / −14.2 | −32.5 |
   | clip 6 (src 499.8 + 23.667 s) | −16.9 LUFS | 15.5 LU | −1.5 dBFS | −29.9 / −24.9 / −17.1 | −30.0 |

   These are the "before" values for any export-based check.

### E. Normalize loudness on all 7 clips (executed + agent-verified 2026-09-14)
1. **Reselect:** processing had cleared the selection. Click clip 0 (≈400,891), Ctrl+click the other
   6 (x 740/921/945/1095/1323/1450), then Audio tab (≈1553,70), then `scroll 1480 450 -3`.
   - `12-reselect-track.png`: all 7 bordered.
   - `12-reselect-audio-scrolled.png`: Enhance voice ✓ 75 and Reduce noise ✓ shown as the shared
     state of the selection, Normalize loudness unticked at ≈(1468,232).
   - The draft is unchanged by reselecting.
2. Run `apply_watch.py normalize-loudness 1468 232 --watch 120 --settle 8`.
   - The draft saved at **0.7 s** (21:58:04), and the watcher settled at 14.2 s.
   - Top-level windows: MainWindow plus a tooltip. **No credit, cost or upsell dialog.**
3. **Agent-verified draft** (`normalize-loudness/audio.json`, `diff` vs baseline):
   - New category **`loudnesses`**, 0 → **7**, plus `+ref loudnesses` on each main segment. Together
     with the earlier two, the full diff is loudnesses / realtime_denoises / vocal_beautifys 0→7 each
     and three +refs per main segment. Nothing else changed, and volume stays 1.0.
   - Per segment: `enable` true, `time_range` = source range, **`file_id` = the Enhance-voice result
     name** (`bb701707…_<start>_<dur>`), so loudness is analysed *after* enhancement.
   - **`target_loudness` −23.0** (LUFS). There was no target control in the UI.
   - `loudness_param`: `avg_loudness` **−11.34 … −13.81** and `peak_loudness` −0.02 (dB).

     | Seg | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
     |---|---|---|---|---|---|---|---|
     | avg | −11.67 | −12.63 | −12.62 | −11.41 | −11.34 | −13.81 | −13.71 |

   - Implied gain = target − avg ≈ **−9.3 to −11.7 dB** per clip. The enhanced voice is ≈2–3 LU hotter
     than the raw source (−14.2 / −16.9 LUFS on clips 0 / 6), and normalizing pulls every clip down to
     broadcast level (−23 LUFS).
   - That makes clips consistent, but **≈9 LU quieter than the common YouTube level (−14 LUFS)**.
     Flag this to the user.
   - **New project files:** `loudness/<hash>` × 7, 19 B each. They are **plain text `avg,peak`**,
     e.g. `-11.4109,-0.0213952`, and match the draft's `loudness_param` exactly. No processing wait.
4. **Observed UI** (`normalize-loudness/t2.png`, `final.png`):
   - Normalize loudness ✓, and its description line changes to **"Normalized loudness to -23
     LUFS"**. The fixed target is shown, with no control to change it.
   - "Auto saved: 21:58:04". The 7-clip selection stays, and there is no toast.

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

### F. Save and final on-disk state (executed + agent-verified 2026-09-14)
- Menu (≈140,22) → **Back to home page** (≈183,303).
  - `HomeWindow` appears on the first poll.
  - Copy draft mtime 22:00:00 → **22:00:40**.
- **`diff` vs `cap11/baseline.json`** is exactly `materials.loudnesses`, `realtime_denoises` and
  `vocal_beautifys` 0 → 7, plus `+ref loudnesses; +ref realtime_denoises; +ref vocal_beautifys`
  on each of the 7 main segments. Nothing else changed.
- **Per clip** (`audio-final.json`):
  - volume 1.0
  - denoise True / 0.85
  - enhance True / 75
  - loudness target −23.0, avg −11.34 … −13.81
- **Enhanced results:** 7 non-empty files in `Resources/audioAlg/`.
- **Other layers unchanged:**
  - 239 house captions at y −0.73
  - the title (y 0.7407)
  - the overlay PiP (1 segment, muted track)
  - rung-7 keyframes (2)
- `final.json` summary saved.
- **Scope:** every other project's mtime is unchanged, including 0707, 0720, 0728, the
  Arabic-titled one, 0914 (4), 0914 (5) and 0914 (6).

## Wait conditions
- **Reduce noise / Normalize loudness:** synchronous. The draft saves within ≈0.7 s, with no
  processing. Poll `audio_check.py` for the new `realtime_denoises` / `loudnesses` refs.
- **Enhance voice:** **asynchronous**, ≈1–2 min per clip, **≈11 min for 7 clips / 7:30**.
  - The draft saves immediately, so it is **not** a completion signal.
  - Done when all `<hashB>_<srcStart>_<srcDur>.wav` files in the project's `Resources/audioAlg/`
    are non-empty and size-stable (4 polls × 3 s), **and** the player header no longer reads
    "Applying N features…".
  - Progress is drawn inside MainWindow ("Enhancing voice… N%", clip labels "Waiting to enhance
    voice…"), not as an `LVLoadingDialog`.
  - Don't edit the timeline while it runs. The selection was cleared mid-run.

## Verification
- **Draft (authoritative):**
  - one `realtime_denoises` (`is_denoise` true), one `vocal_beautifys` (`enable` true,
    `ambient_sound_level` = Intensity) and one `loudnesses` (`enable` true, target −23) ref per
    treated segment
  - `diff` vs the pre-treatment baseline shows only those
  - volume, timing, captions, title, overlay and keyframes unchanged
- **Processing artefacts:** 7 enhanced results in `Resources/audioAlg/`; 7 `loudness/<hash>` text
  files whose `avg,peak` equal the draft.
- **UI:** checkboxes ticked for the selection, "Noise reduced" toast, "Normalized loudness to -23
  LUFS" description.
- **Sound itself, not verified:** the agent can't listen. The processed caches aren't readable WAV,
  and Reduce noise is applied only at playback/export. A true before/after needs a short export,
  which is rung 15 and needs the user's OK. Source reference numbers are in section D.9.
- **Gate:** one Ctrl+Z / Ctrl+Shift+Z per treatment, applied to the whole selection (tested on
  Normalize).

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Scope | All 7 main clips, via Ctrl+click multi-select | User choice | Treat every clip of the same take identically |
| Reduce noise | On (no options; `denoise_rate` 0.85, model denoise_v2) | Universal for room-noise talking heads | Draft ref present; export check if the user wants proof |
| Enhance voice Intensity | 75 (default) | Default; lower if the voice sounds processed | Needs listening or export; not judged by the agent |
| Normalize loudness | On; target −23 LUFS (fixed) | Consistency across clips; level is broadcast, not YouTube | avg −11.3…−13.8 → −23 means ≈−10 dB. Consider a final export loudness of about −14 LUFS for YouTube (open question). |
| Music / ducking | None | User choice | — |

## Undo / recovery
- **Gate executed 2026-09-14** on Normalize loudness (7-clip selection, focus left on the
  inspector checkbox; shortcuts still reached the timeline):
  1. `key ctrl+z` → first poll: `loudnesses` on **0/7** segments, while `realtime_denoises` 7 and
     `vocal_beautifys` 7 are untouched. One undo step covers all 7 clips.
  2. `key ctrl+shift+z` → first poll: `loudnesses` **7/7** with identical `avg_loudness` values
     (−11.67 … −13.81). `diff` vs baseline is again exactly loudnesses / realtime_denoises /
     vocal_beautifys 0→7 plus 3 refs per main segment.
  - Inspector crops: `13-gate-undo-inspector.png`, `14-gate-redo-inspector.png`.
- **Each treatment is one checkbox, and one undo step for the whole selection.** To remove one
  later, select the clips and untick it. For Enhance voice, expect the results in
  `Resources/audioAlg/` to stay on disk. Removal was not tested.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| A loudness helper named `Measure` threw "Measure-Object: A positional parameter cannot be found". | `Measure` is a built-in PowerShell alias for `Measure-Object`, and it shadows a user function of that name. | Name helpers with a verb-noun that isn't an alias (`Get-Loud`). Like the `$home` pitfall, avoid PowerShell's reserved or alias names. |
| The source loudness came out as **I −70.0 LUFS, LRA 0.0**. | The `I:` regex matched ffmpeg's first *running* ebur128 log line (−70 at t=0), not the final summary. | Split stderr on `Summary:` and parse only the last block. Re-measured: clip 0 −14.2 LUFS, clip 6 −16.9 LUFS. |
| ffmpeg on an Enhance-voice result `.wav` failed with "Invalid data found when processing input" (exit 183). | CapCut's processed audio caches aren't real WAV (header `2d 36 39 39…`); only `_upload.wav` is RIFF. | Don't measure caches. Measure the source ranges, and measure processed audio only from a user-approved export. |
| `apply_watch.py enhance-voice` reported settled at 11.9 s, but the frames at 2, 5 and 12 s still showed **"Applying 7 features…"** in the player header, "Enhancing voice… 36.7% → 74.4%" beside the checkbox, and "Waiting to enhance voice…" on each clip. | Enhance voice is **asynchronous server/AI processing**. Its progress is drawn *inside* MainWindow, not as a separate `LVLoadingDialog`. The draft saves at once (0.6 s), with the `vocal_beautifys` refs already pointing at not-yet-written `.wav` result paths. | Don't treat "draft saved + no loading window" as done for Enhance voice. Poll until **all 7 result `.wav` files exist in `Resources/audioAlg/` with stable sizes**, and confirm with a screenshot that the header no longer reads "Applying … features". |

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
- **Proof by export?** A short export (e.g. 00:00:00-00:00:30) would let the agent measure
  loudness and noise floor before and after against the section D.9 source numbers. Export is
  rung 15 (not approved), so the user must say yes.
- **Loudness target:** Normalize loudness is fixed at **-23 LUFS** (broadcast). YouTube talking
  heads usually sit near -14 LUFS, so the result may play about 9 LU quieter. Options: keep it,
  untick Normalize, or raise volume or set export loudness later.
- **Enhance voice intensity:** the default 75 was used. It can be lowered if the voice sounds
  processed.
- **Isolate voice (Free)** and music/ducking were not demonstrated (not chosen).
