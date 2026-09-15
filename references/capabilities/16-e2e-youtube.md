# Capability 16: End-to-end talking-head YouTube edit

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** a new agent-owned project for the chosen raw take (to be created). No
  existing project is touched.
- **Evidence:** `evidence/2026-09-15/cap16/`

## Goal
Take one raw, unused talking-head take all the way to a finished YouTube video, using **only
approved rungs** and their documented procedures, then export it. Every stage is verified in the
draft and in frames, and the final file is checked with ffmpeg.

## User choices (2026-09-15)
- **Footage:** "New talk take (Recommended)", an unused raw take. Show frames of candidates first.
- **Steps:** all of them:
  - "Cleanup (Recommended)": rungs 3–5, i.e. Transcript pauses/filler removal, bad takes, and a
    waveform tidy-up
  - "Jump cuts + push-ins (Recommended)": rungs 6–7
  - "Captions + title (Recommended)": rungs 8–9, using the house style (Arabic-only, Classic black
    box, lower third) and an animated Arabic title
  - "B-roll + audio + logo": rung 10 PiP B-roll, rung 11 Reduce noise + Enhance voice, rung 14
    Yousef AI logo top-right
- **Loudness:** "Skip normalize (Recommended)". Don't apply Normalize loudness (−23 LUFS); measure
  the exported file instead.
- **Export:** "1080p30 H.264 → exports (Recommended)", the rung-15 route: `E:\videos\exports`,
  cloud sync off, ffmpeg verification.
- **Standing rules still apply:**
  - credits OK for Transcript and Auto captions
  - Pro tools: "run; stop if a cost appears"
  - never touch the user's projects
  - native UI only, draft JSON read-only
  - confirm purchases, cloud, deletes and downloads

## Plan (stage gates, each verified before the next)
1. **Pick the take:** a read-only frame sheet of unused talk candidates; the user picks.
2. **New project + import** (rung 13 B route), then drop the take on the main track (baseline
   duration).
3. **Cleanup:**
   - rung 3: Transcript ▸ Remove filler words (pauses/repeats/fillers) ▸ Delete
   - rung 4: bad takes via the transcript / captions
   - rung 5: the waveform/gap pass with `scripts/tighten_gaps.py`
4. **Jump cuts / push-ins** (rungs 6–7): punch-in scale on alternate segments, plus a few eased
   push-ins.
5. **Captions + title** (rungs 8–9): Auto captions in Arabic, the Classic black box template in the
   lower third, text fixes; then an Arabic text-template title near the start.
6. **B-roll** (rung 10): a muted PiP at a stated moment, from the unused footage.
7. **Audio** (rung 11): Reduce noise + Enhance voice on all main clips (async; wait for results).
   **No Normalize.**
8. **Logo** (rung 14): `public/brand/logo-ink-tight.png` on the top overlay track, full length,
   12 % top-right. Check legibility over the footage.
9. **Save**, undo/redo spot gates, scope check.
10. **Export** (rung 15) and verify the file: streams, duration vs the draft, loudness, and frames
    at captions/title/B-roll/logo points.
11. Write up, contact sheet, ask for approval.

## Procedure

### A. Unused take candidates (read-only, 2026-09-15)
- **Durations:** `ffmpeg -i` over all 48 `E:\videos` mp4s.
- **Already used** in earlier projects (excluded): 223643, 190542, 233809, 152043, 152759, 140555,
  plus the B-roll clips.
- **Frames** at 20/40/60/80 % for 8 unused long clips, 320 px wide
  (`cap16/candidates/`, sheet `cap16/take-candidates.png`):

  | # | Clip | Duration | Content |
  |---|---|---|---|
  | 1 | VID_20260425_174820 | 8:04 | solo talking head, grey "MELON" tee, mic, chest-up on a plain wall |
  | 2 | VID_20260721_110250 | 10:42 | wide office shot, speaker far away, walks to camera: **not a talking head** |
  | 3 | VID_20260425_180557 | 15:00 | same setup as #1, holding a pen |
  | 4 | VID_20260416_202252 | 7:28 | 3–4 people in an office: **not solo** |
  | 5 | VID_20260312_163740 | 9:53 | dark / covered lens: **unusable** |
  | 6 | VID_20260415_132742 | 4:15 | solo talking head, Diesel tee, tight framing, warm wall |
  | 7 | VID_20260415_135101 | 4:06 | solo talking head, Diesel tee, light wall |
  | 8 | VID_20260415_143819 | 22:12 | wide desk shot with headphones and laptop, small in frame |

- Suitable solo talking heads: #1, #3, #6, #7.
- **User choice:** "#1 174820, grey tee (Recommended)" → **`E:\videos\VID_20260425_174820.mp4`**
  (8:04, 1280×720, 236 MB).

### B. Leave `0915-copy` (after the rung-15 export)
- Menu ≈(140,22), checked by screenshot (`01-menu-open.png`), then **Back to home page**
  ≈(183,303). `HomeWindow` appeared after 3 s.
- ⚠ **Leaving re-saved `0915-copy`** (mtime 02:59:12 → 03:36:55) even though nothing was edited
  after the export. The diff vs the rung-15 baseline (`diff-0915-copy-home.txt`, 10 lines) is
  **housekeeping only**:
  - a new `materials.loudnesses[0]` with **`enable` false, `target_loudness` 0.0**, referenced by
    the logo segment (a disabled placeholder, likely created when the export analysed audio)
  - `vocal_separations[3].id` regenerated, with the logo segment's ref updated to match
  - a `sound_channel_mappings[3].type` "" → "none" normalisation
  - float noise on the logo scale (0.11999999999999997 → …95)
  - No timing, transform, effect or visibility change. The approved rung-14 edit is intact.
- **Lesson for scope checks:** opening and exporting a project can trigger a benign re-save on
  exit. Judge by **content diff**, not by mtime alone.

### C. New project and import (executed + agent-verified 2026-09-15)
1. **Home top:** `scroll 1000 500 10` (`02-home-top.png`), then **Create project** ≈(1102,144).
   - `MainWindow` appeared after 3 s.
   - New draft folder **`0915 (1)`**, auto-named by date since `0915` exists.
   - Then `focus --maximize`.
2. **Import:**
   - `key ctrl+i`; `wait-for --type Edit --id 1148` matched after 1.4 s.
   - `act set-value --id 1148 --value "E:\videos\VID_20260425_174820.mp4"`, then
     `act invoke --id 1 --name Open`.
   - **Agent-verified:** `draft_meta_info.json` of `0915 (1)` lists `174820`, and no extra windows
     remain (`03-imported.png`).
   - **Observed:** the media card "VID_20260425_174820.mp4" is at ≈(382,216), selected. The player
     shows "Previewing — video" at **00:08:04:07**; its first frame is an empty chair before the
     speaker sits down. The timeline is empty ("Drag material here and start to create",
     y≈829). A yellow "Layers can be reordered in…" onboarding tip sits near Modify.
3. **Drop on the main track:** `drag 382 216 700 829 --steps 40 --hold 0.4`.
   - **Agent-verified (first poll):** 1 main-track segment, **0 → 484.233 s**, source 0, canvas
     `original` **1920×1080** (set by this first clip), one set of helper materials. Baseline saved
     as `draft-00-dropped.json`.

### D. Stage 3, rung 3: Transcript analysis (executed 2026-09-15)
1. The clip is auto-selected after the drop (`04-take-dropped.png`). At this layout the timeline
   toolbar's **Transcript** icon is at ≈(590,596); hovering shows "Transcript ◆"
   (`05-transcript-icon-hover.png`).
2. **Click it** (standing consent: credits OK for Transcript).
   - The loading window (`Qt622QWindowIcon` (840,386)–(1080,645)) appears within 3 s, with no
     dialog.
   - `wait-for --cls RoughCutWindow --timeout 420` matched after **58.6 s** (63 s including the
     click) for 8:04, ≈7.8 s per minute.
   - The draft is **unchanged** by the analysis (`diff-analysis.txt` is empty).
3. **"Remove filler words" window** (`06-roughcut-open.png`):
   - It opens on the **All** tab with the full Arabic transcript. Rows start at 00:00:09:29 «بسم
     الله», 00:00:10:19, 00:00:16:07, …
   - Footer **Total duration: 00:07:42:21**, i.e. the preview with the pre-ticked detections
     removed: 484.233 → 462.7 s, **≈21.5 s pre-ticked**.
   - The mini-timeline is empty; Create compound clip is unticked; **Delete** (Pro) and Cancel.
4. **Detection tabs** (`07-tab-*.png`):
   - **Pauses** ≈(1297,103): Select all ✓ and a list of short pauses, **all pre-ticked**. The first
     page shows 0.87 s @00:00:38:18, 1.17 s @00:52:22, 1.30 s @01:09:04, 1.33 s @01:16:06, 1.23 s
     @01:20:28, 1.30 s @01:23:00, 0.90 s @01:27:00, 0.73 s @02:44:17, … (the full list is paged
     in `pauses/`).
   - **Repeats** ≈(1383,103): **"No repeats identified"**.
   - **Filler words** ≈(1485,103): **"No filler words identified"**. Arabic filler detection found
     nothing, as in rungs 3–4.
   - Not detected as a pause: the **opening ≈10 s of empty chair** before «بسم الله» @00:00:09:29.
     Stage 3b (bad takes / opening trim) has to remove it.
5. **Full pause list:** paged with `scroll 1440 450 -5` until two identical crops, giving 6 pages
   (`pauses/p001–p006.png`). There are **23 pauses, all pre-ticked**, totalling **21.51 s**, which
   matches the footer preview (484.233 − 462.7):

   | Start | s | Start | s | Start | s |
   |---|---|---|---|---|---|
   | 00:38:18 | 0.87 | 03:00:04 | 1.00 | 05:33:03 | 0.60 |
   | 00:52:22 | 1.17 | 03:06:03 | 0.90 | 05:57:23 | 0.77 |
   | 01:09:04 | 1.30 | 03:08:00 | 0.73 | 06:31:27 | 0.53 |
   | 01:16:06 | 1.33 | 03:16:08 | 0.50 | 07:06:27 | 1.03 |
   | 01:20:28 | 1.23 | 04:10:11 | 1.13 | 07:42:17 | 0.80 |
   | 01:23:00 | 1.30 | 04:58:09 | 0.77 | 07:52:05 | 0.83 |
   | 01:27:00 | 0.90 | 05:05:18 | 0.73 | 07:54:16 | 1.43 |
   | 02:44:17 | 0.73 | 05:28:29 | 0.93 | | |

   All are short breath and thinking pauses (0.50–1.43 s) with nothing else detected, so the
   approved rung-3 action is to keep all pre-ticked and press **Delete**.
6. **Delete** ≈(1516,969): the RoughCutWindow closed after **2.4 s**.
   - **Agent-verified (first poll)** (`after-pause-delete.txt`, `draft-02-pauses-removed.json`):
     duration **484.233 → 462.700 s**; **1 → 24 segments**.
   - Each of the 23 joins skips exactly one detected pause in the source: 0.867, 1.167, 1.3,
     1.333, 1.233, 1.3, 0.9, 0.733, 1.0, 0.9, 0.733, 0.5, 1.133, 0.767, 0.733, 0.933, 0.6, 0.767,
     0.533, 1.033, 0.8, 0.833 and 1.433 s. **Sum 21.531 s.**
   - Joins on the timeline: 38.6, 51.867, 67.1, 72.867, 76.267, 77.1, 79.8, 156.467, 171.3,
     176.267, 177.267, 184.8, 238.4, 285.2, 291.733, 314.367, 317.567, 341.633, 375.0, 409.467,
     444.1, 452.9 and 454.433 s.
   - As in rung 3, this is one undo step, and no compound clip is created.

### E. Stage 3b/3c plan: bad takes, opening trim, gap tightening (rungs 4–5)
- Rung 4 showed that the **Repeats tab misses Arabic retakes**, and Transcript text can only be
  read on screen. So use **Auto captions word timings**, which are readable from the draft, as the
  finder:
  1. Captions ▸ Auto captions, Arabic, Bilingual None → Generate. Standing consent: credits OK.
  2. `draft_inspect.py words "0915 (1)" --json` reads every caption and word timing. From it, find:
     - the opening dead air (empty chair before «بسم الله», ≈0–9.9 s source)
     - the tail after the sign-off
     - repeated lines or false starts
  3. Undo the captions with one Ctrl+Z (rung 4) so the cuts aren't entangled with a caption track.
  4. Cut the bad takes latest-first with exact splits + Backspace/W (rungs 1, 2, 4, 5), verifying
     each in the draft.
  5. Regenerate the captions (the recognition is cached and deterministic), then run
     `tighten_gaps.py --project "0915 (1)" --dry-run`, show the plan, and run it with
     `--undo-captions`.
- Captions are generated again at stage 5 for the final house style, after all timing edits.

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

## Open questions for the user
- Which raw take (frame sheet pending).
