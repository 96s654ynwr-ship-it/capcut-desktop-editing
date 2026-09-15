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

### F. Auto captions for word timings (executed + agent-verified 2026-09-15)
1. Asset tab **Captions** ≈(424,73) opens Auto captions with the form **remembering Arabic /
   Bilingual None** from rung 8 (`09-captions-form.png`). There are no captions yet, so Delete
   current captions is irrelevant.
2. **Generate** ≈(539,544):
   - The only new window is the known "Generating captions… N%" loading dialog (760,400)–(1160,630)
     (`10-generating.png`). **No cost, credit or upsell dialog.**
   - Polled the draft text every 3 s for a `text` track containing `subtitle`: present after
     **≈70 s** for 7:42 of timeline (≈9 s per minute).
3. **Agent-verified** (`draft-03-captions.json`): **1 text track, 259 captions**; video still
   **24 segments / 462.700 s**, so generation didn't touch the cuts. The loading dialog is gone
   (`11-captions-done.png`).
4. **Read the transcript** (read-only): `draft_inspect.py words "0915 (1)" --json words-all.json`
   (259 caption rows + word lines, `words-all.txt`) and `gaps --min 0.6 --keep 0.125`
   (`gaps-0.6.txt`: **68 real gaps ≥ 0.6 s**, 54.5 s removable, +5 flagged as spanning edit joins).
   - **Topic:** a hackathon progress update (the 25th) about a Sharia-compliance audit AI
     assistant for small companies, an MCP-server idea, a RAG app on AAOIFI data, and the Next.js
     + FastAPI stack.
   - **Candidates found by reading** (timeline clock after the pause removal):

     | # | Where | What | Recommendation |
     |---|---|---|---|
     | 1 | 0 → 9.733 | empty chair before «بسم الله» | cut |
     | 2 | 455.267 → 462.700 | tail after «السلام عليكم» | cut |
     | 3 | 11.567 → 14.167 | false start «النهارده 25», restarted as «النهارده 25 4» | cut |
     | 4 | 62.600 → 63.400 | stammer «او او او» | cut |
     | 5 | 199.200 → 201.500 | «زي اللي مستخدم ال مثلا بتاع اي حاجة», re-said at 202.700 as «زي لما بتستخدم ال بتاع اي حاجة» | cut the first |
     | 6 | 142.867 → 144.367 | repeated «من الشباب» + unclear «المعاين الفري» before «في الفريق» | optional |
     | 7 | 424.533 → 425.967 | «واليعني هو بايسون», repeating «يعني بايسون» | optional |
     | 8 | 446.733 → 447.533 | extra «تمام» after «بس تمام» | optional |

   - Kept as natural speech: the enumerations «المعاملات…», the rephrase «مدقق شرعي», and the
     self-correction «الكومبتتوف ايدج / او الكومبتتوف».
   - The agent can't hear the audio, so the user chooses the cuts.
   - **User choice (2026-09-15):** "Opening + ending dead air (Recommended), False start +
     stammer (Recommended), Rephrased line at 3:19 (Recommended)". So candidates **1–5** are cut,
     and the optional 6–8 are kept.
5. **Captions undone before cutting** (rung 4 rule):
   - Click empty timeline (1500,690), then **Ctrl+Z**. The `subtitle` text is gone on the first
     poll.
   - Diff vs `draft-02-pauses-removed.json` shows **no differences**: tracks `['video']`, 24
     segments, 462.700 s (`draft-04-captions-undone.json`).
   - The word timings stay usable from `words-all.json`, since it was the same timeline clock.
6. **Exact cut ranges from word timings**, snapped to 30 fps frames. Each keeps 0.125 s of silence
   next to the kept words, or takes the silence midpoint. Order: latest first, so earlier
   timecodes never shift.

   | Order | Cut | Range (s) | Removes | Word evidence |
   |---|---|---|---|---|
   | 1 | tail | 455.400 → 462.700 (end) | 7.300 | «عليكم» ends 455.267 |
   | 2 | rephrased line | 198.867 → 202.100 | 3.233 | «تدفع» ends 198.533; «زي…حاجة» 199.200–201.480; kept «زي لما…» starts 202.700 (both cuts at silence midpoints) |
   | 3 | stammer | 61.500 → 64.600 | 3.100 | «استشارات» ends 61.380; «او او او» 62.600–63.400; «هتشترك» starts 64.733 |
   | 4 | false start | 11.567 → 14.033 | 2.467 | «تمام» ends 11.567 = first «النهارده» start (no silence); «25» ends 13.007; second «النهارده» starts 14.167 |
   | 5 | opening | 0.000 → 9.600 | 9.600 | «بسم» starts 9.733 |

   - **Expected:** 462.700 → 455.400 → 452.167 → 449.067 → 446.600 → **437.000 s**.
   - The nearest existing joins (38.6, 51.867, 67.1, 184.8, 238.4, 454.433) are all at least
     0.9 s from the cut points. Cut 1 lies inside the last segment (454.433 → end).
7. **Driver:** `cap16/cut_bad_takes.py` reuses `scripts/tighten_gaps.py`'s verified primitives
   (`place_exact` measuring split, `remove_range` = exact split + W with duration and
   resume-source checks). It adds two edge cases:
   - **tail:** exact playhead, select the last segment, **W**; verify the timeline ends at the
     target
   - **head:** exact playhead, select the first segment, **Q**; verify the duration drops by t, the
     first segment starts at 0 and its source moves by t

   It refuses to run while a text track exists and aborts on any mismatch.
   - **Dry run:** 24 segments, 462.700 s → 5 planned cuts → **expected 437.000 s**, matching the
     table.
8. **First real run aborted safely, with nothing cut** (`cut_bad_takes-035637.json`,
   `13-after-abort.png`):
   - "ABORT: no draft save after a measuring split" on the **tail** cut after 125 s. The draft
     stayed at 24 segments / 462.700 s.
   - **Cause (observed):**
     - At fit zoom (≈2.81 px/s) the last segment 454.433 → 462.700 is only ≈23 px wide.
     - `place_exact`'s snap-avoid moves the ruler click 4.5 s away from the 454.433 join, but it
       clamps inside the segment, so the click still lands within a few px of the join and
       **snaps onto it**: the playhead is at 00:07:34:13 = 454.433, selected clip = the last one.
     - **Ctrl+B with the playhead exactly on an existing boundary does nothing**, so no save.
   - **Rule:** the measuring-split placement only works when the containing segment is wider than
     ≈2 × snap-avoid (≈9 s) at fit zoom. For narrow segments, step with arrows from a known
     boundary (or zoom in) and verify the timecode before cutting.
   - **Recovery:**
     - The playhead is known to be exactly on the join 454.433, so `key right --repeat 29`
       (0.967 s at 30 fps) targets 455.400 = **00:07:35:12**. Check the timecode crop, then **W**
       on the selected last segment.
     - `trim_tail` now **skips** when the timeline already ends at the target, so the script can
       re-run for the other four cuts.
9. **Tail cut by hand (executed + agent-verified 2026-09-15):**
   - Timecode crop at the join: **00:07:34:13** (`14-tc-at-join.png`).
   - `key right --repeat 29 --gap 0.1` → **00:07:35:12** (`14-tc-tail-target.png`). All 29 presses
     registered at a 0.1 s gap; compare the 390-press run in rung 13 that dropped frames.
   - The last segment was still selected (`14-tail-selection.png`), then **W**.
   - **Draft (first poll):**
     - duration **462.700 → 455.400 s**, still **24 segments**
     - last segment 454.433 + **0.967 s** (src 475.967)
     - diff (`diff-tail-trim.txt`) = only `.duration`, that segment's source/target duration
       8.267 → 0.967, and CapCut's usual empty `material_animations` helper with its ref (as in
       rung 10)
10. **Re-run `cut_bad_takes.py` for the other four cuts (executed 2026-09-15, exit 0, 108 s,
    log `cut_bad_takes-*.json`):**
    - Tail detected as already trimmed and skipped.
    - Each exact placement converged on the **2nd measuring split**. The first split landed
      −19…+38 frames off.

      | Cut | Duration after | Join resumes src | Checks |
      |---|---|---|---|
      | rephrased 198.867 → 202.100 | 455.400 → **452.167** | 214.067 (expected 214.067) | ok |
      | stammer 61.500 → 64.600 | → **449.067** | 66.633 (expected 66.633) | ok |
      | false start 11.567 → 14.033 | → **446.600** | 14.033 (expected 14.033) | ok |
      | opening 0 → 9.600 (Q) | → **437.000** | first segment start 0.000, src 9.600 | ok |

    - **FINAL: 27 segments, 437.000 s**, exactly as predicted. Player at 00:07:35:12 after the
      tail cut (`15-after-tail-trim.png`).
11. **Independent draft check** (`verify_cuts.py` on `draft-06-bad-takes-cut.json`):
    - tracks `['video']`, **27 segments, 437.000 s**, timeline contiguous (no gaps)
    - the first segment starts at 0.000 with **src 9.600** (opening removed); the last segment's
      src ends at **476.933** (tail removed)
    - **source skipped at each of the 26 joins:**
      - the 3 chosen cuts: **2.466** (11.567 → 14.033), **3.100** (63.533 → 66.633), **3.234**
        (210.833 → 214.067)
      - the 23 rung-3 pauses, unchanged (0.5–1.434 s)
    - sum of kept source durations = **437.000 s** = the timeline duration
    - Rounding differences are ≤ 1 ms (µs float storage).

### G. Stage 3c: gap tightening, rung 5 (2026-09-15)
1. **Regenerate the captions** on the cut timeline: the Captions form still read Arabic / None
   (`16-captions-form-before-regen.png`); click Generate ≈(539,544).
   - Only the known loading dialog appeared (no cost prompt).
   - A `subtitle` text track was in the draft after **61 s**.
   - **1 text track, 251 captions** (259 before the bad-take cuts); video still **27 segments /
     437.000 s**, with no `.tracks[0]` change in the diff (`draft-07-captions-regen.json`).
   - A small extra window `Qt622QWindowToolSaveBits` (635,471)–(823,569) appeared afterwards
     (`17-extra-window.png`); it is checked before any further input.
2. **Dry run:** `tighten_gaps.py --project "0915 (1)" --all --min 0.6 --keep 0.125 --dry-run`
   (log `tighten-dryrun-all.json`):
   - **62 real gaps ≥ 0.6 s**; joins are excluded automatically
   - removing all of them: **437.000 → 387.063 s (−49.937 s)**
   - the subset of gaps ≥ 1.0 s (remove ≥ 0.75 s) is **27 gaps, ≈ −32.2 s**
   - the longest single removals are 1.867 s (386.5, «الداتا» | «وحد») and 1.800 s (224.133,
     «اصلا» | «الكومبتتوف»)
   - rung 5 recorded "ask the user how aggressive to go", so the question went to the user
3. **User choice (2026-09-15):** "Gaps ≥ 1.0 s (Recommended)", i.e. `--min 1.0 --keep 0.125`.
4. **The extra window** from step 1 is CapCut's yellow onboarding tip **"One-click to help you cut
   long videos apart" [OK]**, anchored over the player timecode (`17-extra-window.png`,
   `17-after-regen.png`). It is dismissed with its **OK** ≈(795,540) before the scripted run.
5. **Narrow-segment risk for the scripted pass.** One ≥ 1.0 s gap, at 158.3 s, lies in the
   **5.0 s segment 156.133 → 161.1**, the same geometry that aborted the tail cut. The runner
   `cap16/tighten_cap16.py` reuses `tighten_gaps.py` unchanged and replaces only `place_exact`:
   - When the clamped snap-avoid ruler click would land < 1.5 s from a boundary, it **clicks the
     ruler on the segment's start join instead**. The snap there is an exact, known time.
   - It then steps with arrow keys by the frame delta, and the usual measuring split
     verifies/corrects.
   - A measuring split that doesn't save within 20 s aborts immediately, instead of after 120 s.
   - The dry run flags narrow segments with `[narrow segment]`.
8. **Scripted gap pass (executed + agent-verified 2026-09-15):**
   `tighten_cap16.py --min 1.0 --keep 0.125`, background run, exit 0 after **959 s** (≈33 s per
   cut, slower than the ≈15 min estimate). Captured output: task `b17tw7mlm`.
   - Captions were undone first with one Ctrl+Z; the video segments were checked unchanged before
     any cut.
   - **29 of 29 removals** passed both checks (duration delta and join resume source), with **0
     failed checks and 0 aborts**.
   - **Anchor-and-step was used 16 times.** The ruler-click route alone would have risked the tail
     abort on every one of them. Each removal shortens later segments, so more segments become
     narrow as the pass proceeds.
   - **Independent draft check** (`draft-08-gaps-tightened.json`):
     - tracks `['video']`, **56 segments, 403.300 s**, timeline contiguous
     - kept source sum **403.300 s** = duration; the plan's 403.299 differs only by float rounding
     - first segment src **9.600**, last src end **476.933**, so the bad-take opening and tail
       cuts are intact
     - shortest segments 0.833 / 0.933 / 0.967 / 1.0 / 1.0 s
   - **Stage 3 total:** 484.233 → **403.300 s (−80.9 s, −16.7 %)**, split as pauses −21.5 s,
     bad takes −25.7 s and gaps −33.7 s.
   - ⚠ **For stage 4:** with 56 segments, several under 1 s, punching every other segment would
     flicker on the shortest ones. Choose punch-in joins by segment length rather than strict
     alternation.
   - **Promotion candidate:** port `place_exact_anchor` into `scripts/tighten_gaps.py` after
     approval. It fixed a real geometry limit found in this rung.

### H. Stage 4: jump-cut punch-ins, rung 6 (2026-09-15)
1. **State after the gap pass** (`19-after-gaps.png`): 1 video track, 56 segments, 00:06:43:09, no
   popups; at fit zoom ≈3.22 px/s.
2. **Why not strict alternation** (`punch_plan.py`):
   - Alternating at every join where both neighbours are ≥ 2.5 s punches **34** segments,
     including 12 clips under 2.5 s. These are 3–8 px wide at fit zoom, unreliable to click, and
     a framing change on a 1 s clip reads as flicker.
3. **Chosen pattern** (`punch_plan2.py`, `punch_plan2.json`):
   - Group segments into **runs** separated by joins whose neighbours are both ≥ 2.5 s (34 runs).
   - Alternate wide ↔ punched over the runs, but **only single-segment runs may be punched**. A
     multi-segment run always holds a short clip, so it stays wide and the next run gets the
     punch.
   - **Result:** **15 punched segments** (indices 2, 4, 6, 8, 12, 14, 21, 23, 25, 30, 32, 34, 36,
     38, 47), every one ≥ 3.2 s (≥ 10 px at fit zoom), giving **30 framing changes** over 55
     joins, with no short clip ever edited.
   - The longest stretch without a framing change is ≈ 41 s; stage 4b push-ins (rung 7) can cover
     one long unpunched segment (e.g. seg 15, 100.6 + 34.8 s, or seg 42, 336.967 + 26.9 s).
4. **Eye line** (`20-eye-frame-0513.png`, player crop 681 × 383 = 0.3547 px per canvas px):
   - eyes at crop y≈80 vs centre 191.5 → **≈314 canvas px above centre**; speaker ≈ centred
     horizontally
   - a 110 % punch-in raises the eyes by 314 × 0.10 ≈ **31 canvas px**
   - correction ≈ 31 px down → typed **Position Y −60** (typed unit = ½ canvas px, negative =
     down; rung 10); X 0
   - 110 % overflows 54 px top/bottom, so a 30 px shift still exposes no border
   - **Values:** Scale **110 %**, Position **X 0 / Y −60** (shot-specific, re-derived from this
     frame; rung 6's approved −10 was for a different shot)
5. **Trial on seg 14** (75.400 + 25.200 s, the widest punched clip, 81 px at fit zoom), executed +
   agent-verified:
   - click empty timeline (1500,760), then **Shift+Z**, then click the clip body (513,830).
     Selection alone didn't change the draft (`seg_state.py`: no non-default clips).
   - Scale box (1792,257): `ctrl+a`, type `110`, Enter. Draft: **only seg 14**, scale **1.1**.
   - Position Y box (1787,352): `ctrl+a`, type `-60`, Enter. Draft: **only seg 14**,
     transform.y **−0.05556** (= −60/1080), x 0.
   - The inspector reads **110 %** and **X 0 / Y −60**, with seg 14 bordered
     (`21-seg14-punched.png`). Duration and segment count are unchanged (56, 403.3 s).
6. **Driver** `cap16/punch_cap16.py` does the same three steps per planned segment:
   - it verifies after each field that **only** the target segment changed, and aborts otherwise
   - it skips segments already at 1.1 / −60, so it is safe to re-run
   - it re-checks each planned start time against the draft before sending input
   - the final check is that the non-default segments equal the plan
   - **Dry run:** 56 segments / 403.300 s, 15 to punch, all planned starts unchanged; click x
     268.5 (seg 2) … 1455.7 (seg 47).
7. **Eye-line check at seg 14's joins** (`joins14/`; click empty, Home, `down ×14` → join at
   75.400, capture, `left`, capture; then `right`, `down` → 100.600, capture, `left`, capture):

   | Join | Frame before | Frame after | Eyes (crop y) before → after |
   |---|---|---|---|
   | 75.400 wide → punched | 00:01:15:11 | 00:01:15:12 | ≈88 → ≈90 |
   | 100.600 punched → wide | 00:01:40:17 | 00:01:40:18 | ≈92 → ≈90 |

   - The eye line stays within ≈2 px across both cuts, so Y −60 compensates the 110 % lift.
   - The framing change is clearly visible (shoulders and chair wider when punched), reading as a
     deliberate jump cut. No black border is exposed.
   - The white vertical lines in the "after/before punched" crops are the selected clip's
     selection box, not picture edges.
6. **Tip dismissed:** OK ≈(795,540). The window is gone from `cc.py windows`, and the **draft mtime
   is unchanged** by the click (`18-tip-dismissed.png`).
7. **Official dry run for the chosen setting:**
   `tighten_gaps.py --project "0915 (1)" --all --min 1.0 --keep 0.125 --dry-run`
   (`tighten-dryrun-1s.json`): **29 gaps ≥ 1.0 s**, **437.000 → 403.299 s (−33.701 s)**.
   - This corrects the estimate given to the user (27 gaps, ≈ −32.2 s). `--min` filters on the
     *gap* length, so two 1.0-s gaps (429.267 «تمام» | «ده» and 394.333 «عليه» | «الراج») each
     remove only 0.733 s after keeping 0.125 s either side, and they were missed in the
     hand count.
   - The largest removals are 1.867 s (386.500), 1.800 s (224.133) and 1.567 s (426.633, 404.433,
     186.667). The earliest is 5.433 → 6.400 («26» | «امبارح»).

### Plan note: selecting all main clips for the audio stage (stage 7, rung 11)
- After the gap pass the main track will hold ≈56 segments, many only a few px wide at fit zoom.
  Rung 11's Ctrl+click of each clip (7 clips) doesn't scale.
- **Planned route, from approved and verified behaviour:**
  1. **Lock** every non-main track (captions, title, B-roll overlay, logo) with each row's lock
     icon (≈x 59). Locked tracks can't be selected (rung 2 Op 6); verify `attribute` 4 in the
     draft.
  2. Press **`]`** (Select rightward tool mode, verified in rung 12). Click the **first** main clip
     body: everything from the click point rightward on the unlocked track gets selected.
  3. **Gate:** the inspector shows the multi-selection tabs (Video / Audio / Speed / Adjust) and
     every main segment has a white border. The draft doesn't change on selection.
  4. Audio ▸ Basic: **Reduce noise** ✓ and **Enhance voice** ✓ (Intensity 75); no Normalize (user
     choice). Verify `realtime_denoises` and `vocal_beautifys` counts = main segment count.
  5. Press **A** at once, back to the Select tool, so later clicks don't become range selections
     (rung 12 failure mode). Unlock the tracks.
- **Risk:** Enhance voice processes clip by clip (rung 11: ≈11 min for 7 clips). With ≈56 short
  clips, allow ≥ 30 min, poll the result files, and don't export before every `<hash>_…wav` is
  non-empty and size-stable.

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
