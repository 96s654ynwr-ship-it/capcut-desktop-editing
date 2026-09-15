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
8. **Scripted punch-ins (executed + agent-verified 2026-09-15):** `punch_cap16.py`, exit 0 in
   **67 s**.
   - 14 segments punched (seg 14 skipped as already done), each field verified to change **only**
     its target segment.
   - **FINAL** non-default segments **[2, 4, 6, 8, 12, 14, 21, 23, 25, 30, 32, 34, 36, 38, 47]**
     equal the plan.
   - **Draft diff** `draft-08-gaps-tightened.json` → `draft-09-punched.json` (`diff-punch.txt`):
     **45 lines, all `.clip.`** (15 segments × scale x / scale y / transform.y), nothing else.
     Still 56 segments, 403.300 s.
   - **Undo/redo gate** on the last field edit (seg 47 Position Y), with timeline focus via an
     empty click (1500,760):
     - **Ctrl+Z** → seg 47 transform.y **−0.05556 → 0.0**, scale stays 1.1; the other 14 are
       untouched
     - **Ctrl+Shift+Z** → **−0.05556** again; all 15 match the plan
     - Each field edit is its own undo step, as in rung 6.

### I. Stage 4b: eased push-in, rung 7 (2026-09-15)
1. **Segment:** **seg 15**, 100.600 → 135.367 s (34.767 s). It's the longest unpunched clip,
   between punched segs 14 and 16, so the push-in runs inside a wide-framed stretch. Values are
   the rung-7 approved **100 % → 108 %**, **Easing** (ease in-out).
2. **Playhead to the first frame:** click empty (1500,760), Home, `down ×15` → **00:01:40:18**
   (`22-tc-seg15-start.png`). Then click the clip body (611,830), which doesn't move the playhead
   (the timecode stays 00:01:40:18, `22-tc-after-select.png`). The inspector reads Scale 100 %,
   X 0 / Y 0 (`22-seg15-selected.png`).
3. **Start keyframe:** click the Scale ◇ (1872,257). The draft saved on the first poll.
   - `draft_inspect.py keyframes`: seg 15 has **KFTypeScaleX @ 100.600 s = [1.0] Line**.
   - The ◇ is now filled cyan. **No first-use tip** appeared this time (rung 7's tip was one-off),
     and no new window (`23-kf-start.png`).
4. **End keyframe:**
   - Click empty (1500,760), Home, `down ×16` (→ join 135.367), then `left` for the last frame
     (`24-tc-seg15-end.png`).
   - Reselect the clip body (611,830). In the Scale box (1792,257): `ctrl+a`, type `108`, Enter.
     Changing the value auto-adds the keyframe (rung 7).
   - **Draft (first poll):** seg 15 has 2 keyframes: **+0.000 s @ 100.600 = [1.0] Line** and
     **+34.733 s @ 135.333 (00:02:15:10) = [1.08] Line** (`24-kf-end.png`).
   - **Scope check:** `common_keyframes` exist on **seg 15 only**. The clip list shows seg 15 at
     scale 1.08 (it mirrors the last-edited keyframe, per rung 7). The 15 punched segments are
     unchanged at 1.1 / −60.
5. **Keyframe markers on the selected clip strip** (`25-strip-markers.png`, crop of
   (530,780)–(690,880)): small diamonds just inside the clip edges at **≈(556,828)** (start) and
   **≈(662,828)** (end).
6. **Right-click the start marker** (556,828). A full-screen menu window opens
   (`Qt622QWindowIcon` (0,0)–(1920,1031)); the draft is unchanged (`26-kf-menu.png`).
   - Items: **Ease in** (621,756), **Ease out** (628,791), **Easing** (621,826), **✓ Linear**
     (620,861), Show all presets (652,896), Show variable speed animation Alt+K (699,931), Copy
     Ctrl+C (617,972), Delete ⌫ (621,1007).
   - This is the same menu as rung 7. Here it opened upward-right from the marker, because the
     marker sits low on the screen.
7. **Click "Easing"** (621,826). The draft saved on the first poll, and **both** keyframes changed:
   - **+0.000 s @ 100.600 = [1.0] `FreeCurveInOut` L(0,0) R(1.46e+07,0)**
   - **+34.733 s @ 135.333 = [1.08] `FreeCurveInOut` L(−1.46e+07,0) R(0,0)**
   - 14.6 s / 34.733 s = **0.42 / 0.58**, the same `cubic-bezier(0.42, 0, 0.58, 1)` ease in-out
     as rung 7. Handles scale with segment length.
   - ⚠ **Playback started again, as in rung 7.** Two timecode crops 1.2 s apart differed
     (`27-tc-a.png` 00:01:42:20 → `27-tc-b.png` 00:01:44:13, audio meter active).
8. **Stopping the auto-playback:**
   - **Space did NOT pause it.** After `key space` the timecode kept running: 00:02:16:28 →
     00:02:18:20 (`28-tc-c/d.png`), and timecode-only crops (615–790 px, excluding the animating
     audio meter) still differed (`29-tc-e/f.png`).
     - **Cause:** keyboard focus was still in the inspector **Scale value box** from typing
       `108`, so Space never reached the player.
     - The draft was unchanged by the stray Space; the keyframes were re-checked intact.
   - **Fix:** click the player's own **▶/⏸ button (1024,541)**. It works regardless of focus.
     Two timecode-only crops 1.2 s apart were then **identical** (`30-tc-g/h.png`), and the draft
     was unchanged (`30-after-pause.png`).
   - **Rules:**
     - Hash **timecode-only** crops. The audio meter keeps animating after a pause and gives
       false "still playing" results.
     - After typing in an inspector box, pause with the player button, or click the timeline
       before any shortcut.
9. **Easing checkpoints (agent-verified, rung-7 method):**
   - At fit zoom, ruler click at x 583 / 611 / 639, then reselect the clip body (611,830), which
     doesn't move the playhead.
   - Crops of the timecode, the inspector Scale box (1740,240)–(1860,275) and the player
     (`easing/q1–q3-*.png`).
   - Still paused afterwards; the draft is unchanged by the checkpoints.

   | Point | Timecode | Fraction of seg 15 | Inspector Scale | Eased predicts | Linear predicts |
   |---|---|---|---|---|---|
   | ¼ | 00:01:49:24 | 0.265 | **101 %** | 101.2 | 102.1 |
   | ½ | 00:01:58:14 | 0.514 | **104 %** | 104.1 | 104.1 |
   | ¾ | 00:02:07:04 | 0.764 | **107 %** | 107.1 | 106.1 |

   - The readouts match the eased curve at ¼ and ¾, where eased and linear differ.
   - **Visual:** at ¾ (`q3-frame.png`) the speaker's head and shoulders are visibly larger and the
     chair edge has moved outward compared with ¼ (`q1-frame.png`). No border is exposed at 108 %.
10. **Stage 4 summary:** **15 static punch-ins** (110 %, Y −60) on the planned single-segment
    runs, plus **1 eased push-in** (seg 15, 100 → 108 %, 34.7 s). Duration and segment count are
    unchanged (56 / 403.300 s).
    - **Push-in diff** `draft-09-punched.json` → `draft-10-pushin.json` (`diff-pushin.txt`,
      29 lines):
      - **25 lines on seg 15 only:** clip scale 1.0 → 1.08, which mirrors the last keyframe, plus
        `common_keyframes` with 2 `FreeCurveInOut` keyframes (right handle 14 587 999 µs,
        time_offset on the source clock, e.g. 129 800 000)
      - **4 top-level lines:** a new `keyframe_graph_list[0]` entry `resource_name` **"Ease"**,
        `resource_id` 7418178875479298577, i.e. CapCut registering the easing preset used
      - No other segment or track changed.

### J. Stage 5: house-style captions, rungs 8–9 (2026-09-15)
1. **Final Auto captions** on the finished cut (403.300 s):
   - No text track before; the form crop confirmed **Arabic / Bilingual None**, Delete current
     captions unticked (`31-captions-form-final.png`).
   - **Generate** (539,544). Only the known loading dialog appeared (no cost, credit or upsell
     prompt).
   - A `subtitle` track was in the draft after **64 s**.
   - **Agent-verified** (`draft-11-captions-final.json`): **1 text track, 252 captions**. Video is
     still 56 segments / 403.300 s, and the diff has **no `.tracks[0]` lines**, so cuts, punch-ins
     and the push-in are untouched.
   - The caption row sits at y≈763 above the video (`31-captions-final.png`).
   - First caption «بسم الله» 0.200 s; last «السلام عليكم» ends 403.133 s
     (`words-final.txt`/`.json`).
2. **Text review (read-only).** Captions needing a decision, per house style "digits instead of
   words, English brand names, dialect words":
   - **Digits:** «النهارده 25» (1.967), «4 2,000 26» (3.467, a garbled spoken date), «او الافكار
     ال2» (17.4), «ده التحديث بتاع 25» (322.967), «عشان مطلوب مننا يوم 27» (332.8).
   - **Likely misrecognitions:**
     - «وراحت لجيمراي» (228.067), probably «لجيميناي»
     - «اعملي تطبيق شرعي… تطبيق شرعي» (229.167), probably «تدقيق»
     - «الراديو ابلكيشن» (264.933), probably «الراج»
     - «نستخلص التاتا دي» (283.3), probably «الداتا»
     - «والداة والكلام ده» (381.567), probably «والداتا»
     - «فجمة او» (338.733), probably «فيجما»
   - A text-only digit scan (`digit_scan.py` on `words-final.json`) confirmed **exactly 5** digit
     captions. The first PowerShell filter matched every row because the timecodes contain
     digits, so always filter the text field.
3. **User choices (2026-09-15):**
   - **Digits:** "Write dates as numbers (Recommended)":
     - «النهارده 25» (1.967) → **kept**
     - «4 2,000 26» (3.467) → **«25/4/2026»**
     - «ده التحديث بتاع 25» and «عشان مطلوب مننا يوم 27» → **kept** (day numbers)
     - «وايه ممكن نضيف عليها او الافكار ال2» (17.4) → **«…او الافكار التانية»**
   - **Words:** "Brand/tech terms (Recommended)":
     - «وراحت لجيمراي» → «وراحت لجيميناي»
     - «الراديو ابلكيشن» → «الراج ابلكيشن»
     - «…نستخلص التاتا دي» → «…نستخلص الداتا دي»
     - «والداة والكلام ده» → «والداتا والكلام ده»
     - «فجمة او» → «فيجما او»
     - «تطبيق شرعي» (229.167) is **not** chosen, so it stays as generated.
   - Order, per the house-style recipe: apply the **Classic: black box** template to all main
     captions first, then make the 7 text fixes, then verify frames.
4. **Select a caption and open the template grid** (draft unchanged throughout;
   `draft-12-before-template.json` taken first):
   - At the Ctrl+= ×4 zoom (≈51.6 px/s, 00:15 at x≈166, 00:20 at x≈424; `32-caption-zoom.png`),
     caption pills with **A☰** icons sit on the TT row y≈763.
   - **Click the pill** «وايه ممكن نضيف عليها او الافكار ال2» (345,763). It gets a white border
     (`33-pill-selected.png`). The inspector becomes **Captions / Text / Animation / Tracking /
     Text to sp…**, on Text ▸ **Basic** with Apply to all main captions ✓, the caption's text,
     Font System, size 7, Pattern B/U/I and Case TT/tt/Tt.
   - **Text ▸ Templates** (1623,127), then the **Classic** chip (1653,271) (`33-templates-classic.png`):
     - Apply to all main captions ✓ stays ticked.
     - Search "Search for text templates"; chips ★ / Trending / **Classic** / NEW / H…
     - The Classic grid is **4 columns × 2 rows**, tiles ≈98 px apart: row 1 y≈370, row 2 y≈468,
       columns x≈1500 / 1597 / 1695 / 1792. Each tile has ☆ and ⬇ at its bottom-right, and
       several carry a Pro diamond.
     - Footer buttons: Save as preset / **Reset**.
   - The thumbnails are too small to identify "black box" by eye at this size, so a full-size crop
     is checked before clicking (`34-classic-grid-crop.png`).
     - **Row 1 left** shows white "THE QUICK BROWN FOX" on a **solid black bar** with a Pro
       diamond, the black-box look, in the same position as rung 8.
     - Tiles 2, 3 and 6 had not rendered thumbnails yet (tiny placeholders).
5. **Apply the template:** click the row-1-left tile **body** (1490,360), away from its ☆ and ⬇.
   The draft saved after ≈2 s.
   - **Agent-verified** (`template_check.py`, `draft-12-before-template.json` →
     `draft-13-template.json`):
     - **252 → 252 captions**, all **`text_templates` "边框弹出黑色", resource
       7331662668685774086**, the house-style "Classic: black box"
     - **y −0.73 for all 252** (lower third; a single-language track keeps its position, as in
       rung 8)
     - **start, duration and text identical for 252 of 252**
     - materials: text_templates 252, effects 252, texts 252
     - **video track byte-identical** (56 segments, 403.300 s)
   - No new windows; the tile applied to all main captions in one click, because Apply to all
     main captions was ticked.
   - **Observed after applying** (`35-template-applied.png`):
     - The applied tile has a cyan border; the grid and inspector stay on Templates.
     - The **timeline view scrolled back to 00:00** (00:00–00:30 visible at the same zoom), so
       re-read pill positions before clicking. Pills now carry text plus A☰, e.g. «النهارده 25»
       ≈(365,763) and «4 2,000 26» ≈(455,763).
     - The player at 00:00:17:08 shows no caption (a gap between captions).
6. **Text ▸ Basic on a templated caption** (1516,127) (`36-basic-tab-templated.png`; draft
   unchanged):
   - The selection survived the view scroll: the text box still shows «وايه ممكن نضيف عليها او
     الافكار ال2».
   - Layout: Apply to all main captions ✓ (1470,167); **text box ≈ x 1461–1893, y 205–285**
     (click ≈1680,230); Font **System**; Font size **7**; Pattern B/U/I; Case TT/tt/Tt; Save as
     preset.
   - As in rung 8, a template adds no Bubble conflict here: the sub-tabs are Basic / Templates /
     Bubble / Effects.
7. **Text fix 1, first attempt: FAILED safely** (`37-fix1.png`, `37-fix1-inspector.png`):
   - The sequence was: click (1680,230) in the empty lower part of the text box, `key ctrl+a`,
     `type "وايه ممكن نضيف عليها او الافكار التانية"`, then poll the caption text for 30 s
     (`caption_texts.py wait`).
   - **Result:** the text stayed «…الافكار ال2» and no caption changed. The inspector box still
     shows the old text with no caret.
   - **Integrity check:** draft mtime **unchanged** (12:30:05.066, the template save), and diff vs
     `draft-13-template.json` = **0 lines**, still 56 video + 252 text segments. Nothing typed
     reached CapCut, and the stray Ctrl+A selected nothing that is saved.
   - `cc.py type` sends each UTF-16 unit as a `KEYEVENTF_UNICODE` key event (`type_unicode`), not
     through the clipboard. Only `cc.py paste` uses Set-Clipboard + Ctrl+V. So no clipboard content
     could have been pasted onto the timeline.
   - **Likely cause:** the click landed in the text area's padding below the single text line and
     didn't give the QML text field keyboard focus. The follow-up ruler click (1500,628) only
     moved the playhead to 00:00:24:19.
   - **Next:** click on the text line itself (≈1800,220), confirm a caret by crop, confirm the Ctrl+A
     highlight by crop, and only then type.
8. **Diagnosis: stale inspector plus a playhead outside the caption** (no draft change in any
   step):
   - Clicking on the text line (1800,220) with the playhead **outside** the caption (00:24:19)
     changed nothing: the crops before and after were identical (`38-textbox-*.png`).
   - **Put the playhead inside the caption, then reselect:**
     - Ruler click at **x 1185** = 18.5 s (≈51.6 px/s, 00:00 at x≈230), 57 px from either
       caption edge so no snap. Timecode **00:00:18:16** (`39-tc-inside-caption.png`).
     - Click the pill (1185,763). The pre-click pill map (`39-ruler-and-pills.png`) shows it
       spanning x≈1127–1245.
   - **Result:**
     - The **player shows the caption** «وايه ممكن نضيف عليها» in the black-box style, with its
       selection box and handles (`39-player-inside-caption.png`).
     - The inspector's sub-tabs changed to **Basic / Templates / Effects, with Bubble gone**
       (`39-inspector-reselected.png`), the templated-caption layout rung 8 recorded.
     - Before reselecting, the panel still showed **Bubble**: it was a **stale pre-template
       inspector**, the likely reason typing never reached a live text field.
   - **Rule for text fixes after applying a template:** ruler-click inside the target caption,
     re-click its pill, confirm the caption shows in the player and the sub-tabs read Basic /
     Templates / Effects, then edit.
   - No caret was visible in two crops 600 ms apart (it may blink off in both). Focus is
     therefore confirmed by the **Ctrl+A selection highlight** before typing
     (`40-box-*-ctrla.png`).
9. **Focus confirmed** (no draft change):
   - Click on the text line (1800,220): the crop shows a **caret** inside the line
     (`40-box-before-ctrla.png`).
   - `key ctrl+a`: the **whole text is highlighted** (`40-box-after-ctrla.png`).
   - On the full screen (`40-after-ctrla-full.png`), only the target pill has a white border, so
     Ctrl+A went to the text field and not the timeline.
   - The live template inspector reads Font **Staatliches-Regular**, size **11** (the template's
     font). The player shows the black-box caption with its bounding box.
   - The inline pixel-count check failed on PowerShell 5.1 quote stripping (the rung-14 failure
     mode), so the crops were judged visually instead.
   - **Type immediately after Ctrl+A.** Any click in between would drop the selection.
10. **Text fix 1 (executed + agent-verified 2026-09-15):**
    - With the text selected, `type "وايه ممكن نضيف عليها او الافكار التانية"`.
    - `caption_texts.py wait` matched after **7.2 s**, and a re-poll 1.5 s later was still
      matching (fully saved, no partial autosave).
    - **Changed vs `texts-before-fixes.json`:** exactly **1** caption, 17.4 s «…الافكار ال2» →
      «…الافكار التانية». Still 252 captions.
    - Video track byte-identical to `draft-13-template.json` (`draft-15-fix1.json`).
    - Focus released with a ruler click inside the caption (1185,628).
    - The template stays on the edited caption, as in rung 8.
    - Frames: `41-fix1-player.png`, `41-fix1-inspector.png`.
11. **Driver for the remaining fixes:** `cap16/fix_caption.py --x <pill x> --start <s> --old <text>
    --new <text> --baseline texts-before-fixes.json` runs the proven steps 8–10. It adds a
    **gate before typing**:
    - After Ctrl+A it presses **Ctrl+C** and reads the clipboard (`Get-Clipboard`). It types only
      if that equals `--old`. A wrong or unfocused selection aborts with nothing typed.
    - It also refuses to start if the draft's caption at `--start` doesn't read `--old`.
    - After typing: exactly one caption changed, 252 captions, and the video track byte-identical.
    - ⚠ It overwrites the Windows clipboard.
12. **Text fix 2, the garbled date (executed + agent-verified 2026-09-15):**
    `fix_caption.py --x 455 --start 3.467 --old "4 2,000 26" --new "25/4/2026"`, exit 0.
    - Pill x 455 in the 00:00–00:30 view is 4.36 s, inside the caption (3.467–5.3 s).
    - **Gate:** the clipboard after Ctrl+A / Ctrl+C read exactly `'4 2,000 26'`, so the copy
      check works in CapCut's QML text field and confirms both focus and the right caption.
    - Saved after **4.5 s**.
    - **Cumulative changes vs `texts-before-fixes.json`: exactly 2**, fix 1 (17.4 s) and fix 2
      (3.467 s → «25/4/2026»). Still 252 captions, video track byte-identical
      (`draft-16-fix2.json`).
    - Frames: `42-fix2-player.png`, `42-fix2-inspector.png`, `42-fix2-tc.png`.
    - **Rendering (agent-verified):** at 00:00:04:11 (inside the caption) the player shows
      **«25/4/2026» left-to-right**, bold white on the template's black box, with no bidi reversal.
      A digits-only caption is laid out as a left-to-right run. The inspector box reads
      `25/4/2026`.
13. **Locating the remaining five pills** (no draft change):
    - Per target: click empty timeline (1500,690) (not y 760, which is now the caption row),
      **Shift+Z**, ruler click at fit x = 232 + t × 3.216, **Ctrl+= ×4**. The zoom keeps the
      playhead's screen x, which the fix-1 observation confirmed.
    - Then crop the ruler + TT row (160,615)–(1910,780) and the timecode (`locate/t*-row.png`,
      `t*-tc.png`).
    - Targets and fit x: 228.067 → 966, 264.933 → 1084, 283.3 → 1143, 338.733 → 1321,
      381.567 → 1459.
    - `fix_caption.py --nav-x <fit x>` replays the same sequence before editing, so pill x values
      read from these crops stay valid.
    - **Pill x from each crop** (crop x + 160 = screen x; 51.6 px/s; the playhead line and
      timecode give the anchor):

      | Target | Nav x | Playhead after zoom | Caption mid | Pill x | Pill seen in crop |
      |---|---|---|---|---|---|
      | 228.067 «وراحت لجيمراي» | 966 | 227.2 s @ x 962 | 228.57 s | **1031** | «وراحـ» ≈1008–1055 |
      | 264.933 «الراديو ابلكيشن» | 1084 | 264.8 s @ x 1082 | 265.45 s | **1116** | «الراديو» ≈1090–1142 |
      | 283.3 «…التاتا دي» | 1143 | 281.267 s @ x 1136 | 284.7 s | **1313** | «وعندها مقالات…» ≈1242–1385 |
      | 338.733 «فجمة او» | 1321 | 336.967 s @ x 1316 | 339.13 s | **1428** | «فجـ» ≈1408–1447 |
      | 381.567 «والداة والكلام ده» | 1459 | 382.967 s @ x 1464 | 382.18 s | **1424** | «والداة وال» ≈1392–1453 |

      - Across all five, the playhead stayed at the ruler-click x after Ctrl+= ×4 (±5 px), which
        confirms the zoom anchor.
14. **Text fixes 3–7 (executed + agent-verified 2026-09-15):** one sequential run of
    `fix_caption.py --nav-x … --x … --start … --old … --new …`, **all exit 0**.

    | Fix | Caption | Gate (clipboard) | Saved after | New text |
    |---|---|---|---|---|
    | 3 | 228.067 | «وراحت لجيمراي» ✓ | 5.1 s | «وراحت لجيميناي» |
    | 4 | 264.933 | «الراديو ابلكيشن» ✓ | 5.4 s | «الراج ابلكيشن» |
    | 5 | 283.3 | «…نستخلص التاتا دي» ✓ | 12.8 s | «…نستخلص الداتا دي» |
    | 6 | 338.733 | «فجمة او» ✓ | 4.4 s | «فيجما او» |
    | 7 | 381.567 | «والداة والكلام ده» ✓ | 6.0 s | «والداتا والكلام ده» |

    - After each fix, the cumulative changes vs `texts-before-fixes.json` grew by exactly one:
      3, 4, 5, 6, 7.
    - Every run reported 252 captions and a byte-identical video track.
    - The longest caption (fix 5, 55 characters) took the longest to save (12.8 s), consistent
      with typing time plus autosave.
    - Frames and inspector crops: `43-fix3…7-player.png`, `43-fix3…7-textbox.png`.
    - Final draft: `draft-17-fixes-done.json`.
15. **Stage 5 final check (agent-verified, `stage5_check.py`, `draft-13-template.json` →
    `draft-17-fixes-done.json`):**
    - **252 → 252 captions**, all **"边框弹出黑色" / 7331662668685774086**, all at **y −0.73**
    - **timing identical** for every caption
    - **exactly 7 text changes**, the user-chosen fixes: 3.467, 17.4, 228.067, 264.933, 283.3,
      338.733, 381.567
    - **video track byte-identical** (56 segments, 403.300 s); tracks `video 56, text 252`;
      **no material-count changes**
    - **Visual:**
      - The inspector boxes read «وراحت لجيميناي», «الراج ابلكيشن», «…نستخلص الداتا دي»,
        «فيجما او» and «والداتا والكلام ده».
      - The player renders «وراحت لجيميناي» and «والداتا والكلام ده» (current word on the black
        box) in the lower third, inside the frame (`43-fix3-player.png`, `43-fix7-player.png`).
    - Captions stay one track, so the house-style verify list applies: one text track, every
      caption on the template, Arabic, frames inside captions checked.
16. **Undo/redo gate on a caption text edit (agent-verified):** timeline focus came from fix 7's
    closing ruler click.
    - **Ctrl+Z** → caption 381.567 reads «والداتا والكلام **د**», exactly one character removed on
      the first poll. Text undo is **per character**, as in rung 8.
    - **Ctrl+Shift+Z** → «والداتا والكلام ده» on the first poll.
    - Diff vs `draft-17-fixes-done.json` after the gate: **0 lines** (`draft-18-text-gate.json`).

### K. Stage 6 title and stage 7 B-roll: user choices (2026-09-15)
- **Title:** «مدقق شرعي بالذكاء الاصطناعي» ("An AI Sharia auditor"), with the approved rung-9
  Arabic text template (#3 yellow bold, type-on in-animation), 3 s near the start.
  - **Framing caveat:** this take is tighter than rung 9's. The speaker's head reaches close to the
    top of the frame, so placement is decided from a frame, not copied from rung 9's Y 800.
- **B-roll:** `E:\videos\VID_20260416_203431.mp4` (office, 3 people), muted PiP in the upper-left
  corner, 4 s, while he says «قعدنا انا والفريق». Current captions: «قعدنا انا» 12.067–12.867,
  «والفريق» 13.667–14.467, «كنا بنتكلم على الفكرة…» 14.7–17.1, so the window is ≈12.067 → 16.067 s.

### L. Stage 6: opening title, rung 9 (2026-09-15)
1. **Frame for placement** (`44-frame-2s.png`; click empty (1500,690), Home, `right ×60` →
   **00:00:02:00** confirmed by `44-tc-2s.png`):
   - The speaker's **head top is only ≈20 of 383 player px from the top** (≈5 %), head at player
     x≈335–435. There is **no room above the head**, unlike rung 9's framing (head at ≈225–320).
   - **Clear plain wall:** **upper-left** player x≈10–215, y≈10–175 (canvas ≈28–606 × 28–493); a
     narrower strip right of the wall corner (player x≈540–670).
   - The house caption «النهارده 25» sits in the lower third, as expected.
   - **Placement decision:** the title goes in the **upper-left wall area**. Its 1–4 s window never
     meets the B-roll PiP (upper-left, 12–16 s).
2. **Playhead for the title start:** Home, `right ×30` → **00:00:01:00** (`44-tc-1s.png`).
3. **Text tab** (163,70) (`45-text-tab.png`):
   - Left list: **Add text**, Yours ▾, Text effects ▾, **Text template ▾ ≈(85,251)**, Auto
     captions, Local captions.
   - The main area shows a "Default text" card. The timeline view had scrolled to ≈06:00–06:30,
     but the playhead is still at 1:00, and the + adds at the playhead.
   - Draft unchanged. The yellow "Layers can be reordered in…" tip reappeared near Modify and is
     harmless.
4. **Text template ▾** (85,251) (`46-text-template-open.png`): the categories expand (Trending,
   Whimsical, KATSEYE, Pixel Bead, Classic, NEW), with a 3-column Trending grid (Chapter End, The
   Story Begins, FINAL, BAM!, CLOUD, LOCATION, KEEP GOING, CREATIVE, NĂNG ĐỘNG).
5. **Search «عربي»:** click the search box (370,127), `type "عربي"`, Enter, wait ≈7 s
   (`46-arabic-search.png`, grid crop `46-arabic-grid.png`).
   - The categories are hidden while the search is active.
   - Grid rows: «الفرح في البساطة», "It's simple", calligraphy / "Một ngày đơn giản", **«يوم عادي،
     حياة عادية»**, "A simple life" / «الحياة تستمر», «حياة صغيرة», «بسم الله…».
   - **Template #3** (yellow bold, rung 9) is **row 2, middle ≈(357,340)**. It shows a **⬇**
     ≈(395,378), not yet downloaded in this session.
   - The playhead is still **00:00:01:00** (`46-tc.png`); draft unchanged.
6. **Preview/download template #3:** click the tile body up-left of centre (342,325), away from
   the icons, and wait 5 s. Draft unchanged (`47-tile3-preview.png`).
   - The tile gets a **cyan border**. Its ⬇ becomes a **cyan +** at crop (106,98) → **screen
     ≈(396,378)**, with ☆ beside it (`47-tile3-icons.png`).
   - The player header reads **"Previewing — Text template ⓘ"** (`47-player-header.png`). The
     timecode shows the template's own clock, **00:00:00:00 / 00:00:03:00** (`47-tc.png`).
   - As in rung 9, a click previews and only **+** adds.
7. **Add at 1.0 s with a timecode gate:**
   - Click empty timeline (1500,690) to leave the preview (this moves the playhead), then Home and
     `right ×30`.
   - **Gate:** the timecode crop (615,528)–(790,555) must be byte-identical to the earlier
     00:00:01:00 crop `44-tc-1s.png` before **+** is clicked. The region excludes the animating
     audio meter, so an identical hash means the same timecode display.
   - Then hover the tile (357,340) and click + (396,378). `title_state.py` prints the new title
     segment's template, start, duration, texts, scale, transform and animations.
8. **First gated add: STOPPED by a false negative; nothing added.**
   - The gate printed `False` and the script stopped before hovering or clicking +. Draft mtime
     unchanged (12:48:59).
   - The crops show the navigation had actually worked:
     - `48-tc-before-add.png` reads **00:00:01:00 / 00:06:43:0**, visibly identical to the
       reference.
     - `48-header-before-add.png` reads **"Player-Timeline 01"**, so the empty-timeline click did
       leave the preview.
   - **Cause:** a **byte-exact hash** of two captures of the same timecode isn't stable
     (sub-pixel or anti-aliasing differences between captures).
   - **Fix:** gate on a **tolerant pixel difference** (`img_diff.py`, mean absolute difference and
     count of pixels > 15) calibrated against a real 1:00 vs 2:00 difference. The failure is safe
     either way: a strict gate can only block, never mis-add.
   - **Calibration** (`img_diff.py`, timecode crop 175 × 27):

     | Pair | mean abs | max | pixels > 15 |
     |---|---|---|---|
     | 1:00 vs 1:00 (two captures) | 0.001 | 1 | **0** |
     | 1:00 vs 1:00 (`46-tc` vs `44-tc-1s`) | 0.001 | 1 | **0** |
     | 1:00 vs 2:00 | 2.584 | 96 | **203** |

     **Gate rule:** pass only when **pixels > 15 == 0**.
9. **Gated add (executed + agent-verified 2026-09-15):**
   - The gate passed against `44-tc-1s.png` (0 pixels > 15) (`50-tc-gate.png`).
   - Hover the tile (357,340) (`50-tile3-hover.png`), then click **+** (396,378). The draft saved
     on the first poll.
   - **`title_state.py`:**
     - tracks are now `video 56 / text(flag 1) 252 / text(flag 0) 1`, a **new text track** for the
       title
     - segment **start 1.000 s, duration 3.000 s**
     - template **"Arabic An ordinary day, an ordinary life" / 7659823758919699730**, the rung-9
       template
     - placeholder text «يوم عادي،\nحياة عادية»
     - scale 1.0, transform (0, 0)
     - **in-animation 0 → 1 000 000 µs**
   - **Video track and the 252-caption track are byte-identical** to `draft-18-text-gate.json`
     (`draft-19-title-added.json`).
   - **Observed** (`50-title-added.png`):
     - A new TT row y≈731 holds the title block (x≈279–437, 1–4 s, selected) above the caption
       row y≈763.
     - The inspector reads **Text / Tracking / Text to speech / AI avatars◆** ▸ Basic / Templates /
       Effects.
     - **"The 1 paragraph"** text box ≈(1655,227) shows the placeholder right-aligned ≈(1818,227)
       with a ▾ ≈(1878,227).
     - Transform: Scale **100 %** ≈(1790,349); Position **X ≈(1647,444) / Y ≈(1768,444)**; Plane
       rotation.
     - The player's dashed guides mark the title box (x≈758–1289), as in rung 9.
10. **Title text (executed + agent-verified 2026-09-15)** with `title_text.py`:
    - It checks that the title's draft text is the placeholder.
    - Click the placeholder line (1815,222), Ctrl+A, Ctrl+C. **Gate:** the clipboard equals
      «يوم عادي،\nحياة عادية» (matched, including the newline).
    - Then type «مدقق شرعي بالذكاء الاصطناعي» (it replaces both placeholder lines with one).
    - **Draft:** saved after **6.4 s**, texts == ["مدقق شرعي بالذكاء الاصطناعي"]. Start 1.0 s /
      3.0 s, scale 1, transform (0,0), all unchanged.
    - **Video and caption tracks byte-identical.**
    - Frames: `51-title-text.png`, `51-title-text-inspector.png`.
    - With one line, the inspector rows move up ≈16 px, as in rung 9: Transform ≈269, **Scale box
      ≈(1790,333)**, **Position X ≈(1647,428) / Y ≈(1768,428)**, plus an alignment row.
11. **Default frame** (click empty timeline (1000,690), Home, `right ×75` → **00:00:02:15**,
    after the 1 s type-on; `52-title-hold-default.png`, `52-tc-hold.png`):
    - At **scale 100 %, position (0,0)** the title is one huge heavy yellow line, **far wider
      than the frame** (clipped at both edges, only «…رعي بالذكاء الا…» visible).
    - Its band sits at player y≈235–340, across the speaker's chest and over the caption
      «النهارده 25».
    - **Not acceptable.** It needs a much smaller scale and a move into the upper-left wall area
      (§L.1). The scale is measured from a frame, not guessed.
12. **Scale 30 % trial (executed + agent-verified 2026-09-15):**
    - Click the title block (356,731); the playhead stays put, and the timecode crop is identical
      before and after (0 pixels > 15).
    - Scale box (1790,333): `ctrl+a`, type `30`, Enter. The draft saved on the first poll:
      **scale 0.3**, transform (0,0), text, start, duration and in-animation unchanged; video and
      captions byte-identical.
    - **Measured** with `yellow_bbox.py` (pixels R > 200, G > 160, B < 90) on the 2:15 frame
      `53-title-scale30.png`:
      - yellow bbox **player x 133–547, y 201–239 (415 × 39 px)**, centre **(340.0, 220.0)**
      - it no longer touches the frame edges, but is still **61 % of the frame width**
      - it still crosses the chest line
    - **Anchor model** (checked against two scales):
      - The template's text centre sits below frame centre (191.5) by an offset proportional to
        scale: ≈ +96 px at 100 %, ≈ +28.5 px at 30 %.
      - Horizontally it is centred (340 ≈ 340.5).
13. **Placement computation** for the upper-left wall (player x≈10–320 left of the head at
    x≈335; wall y≈10–175):
    - **Scale 22 %:** width ≈ 415 × 22/30 ≈ **304 px**, height ≈ **29 px** (≈7.5 % of the
      frame height, legible).
    - Default centre at 22 %: (340.5, 191.5 + 96 × 0.22 ≈ 212.6).
    - **Target centre** player **(170, 60)**: text x≈18–322 (clear of the head at 335), band
      y≈45–75.
    - Delta: (−170.5, −152.6) player px × 2.819 = **(−481, −430) canvas px**.
    - Typed Position = 2 × canvas px, positive Y = up (rung 10), giving **X −961, Y +860**,
      i.e. transform (−0.5005, 0.7963).
14. **Scale and placement applied (executed + agent-verified 2026-09-15):** three inspector
    boxes, each `ctrl+a` / type / Enter, **gated on the draft after each field** (`title_clip.py`):
    - Scale (1790,333) `22` → **0.22 0.0 0.0**
    - Position X (1647,428) `-961` → **0.22 −0.50052 0.0**
    - Position Y (1768,428) `860` → **0.22 −0.50052 0.7963**
    - start 1.0 / duration 3.0 unchanged at every step; the playhead didn't move (timecode crop
      0 pixels > 15 vs `52-tc-hold.png`)
    - **Measured** on `54-title-placed.png`: yellow bbox **x 18–322, y 46–73 (305 × 28 px)**,
      centre **(170.0, 59.5)**, vs predicted x 18–322 / centre (170, 60). The anchor model and
      the half-canvas Position rule hold for text templates too.
    - Video and 252-caption tracks byte-identical to `draft-19-title-added.json`
      (`draft-20-title-placed.json`).
15. **Frames across the title's life** (deselected via empty timeline click (1000,690), so no
    selection box; Home + `right ×N`; timecodes confirmed by crop; `title_life/`):

    | Timecode | Yellow bbox (player px) | Observed |
    |---|---|---|
    | 00:00:01:10 | x 200–322, y 46–73 (123 × 28) | type-on in progress: «مدقق شرعي» shown, the rest not yet typed; caption «تمام» below |
    | 00:00:02:15 | x 18–322, y 46–73 (305 × 28) | full title, hold |
    | 00:00:03:29 | x 18–322, y 46–73 (305 × 28) | full title on the last frame; caption «25/4/2026» below |
    | 00:00:04:00 | none | title gone (segment end is exclusive, as in rungs 9–10) |

    - The Arabic is correctly joined and right-to-left. It types on from the right (the first
      words appear at the right end, x 200–322) and sits on the plain wall.
    - It **never touches the head** (head x≈335–435) or the lower-third caption.
    - The draft was unchanged by the frame checks.
16. **Undo/redo gate on the title Y edit (agent-verified):** start `0.22 −0.50052 0.7963`.
    - **Ctrl+Z** → `… 0.0` (only Y reverted; each field is its own undo step).
    - **Ctrl+Shift+Z** → `… 0.7963`.
    - Diff vs `draft-20-title-placed.json`: **0 lines** (`draft-21-title-gate.json`).

### M. Stage 7: B-roll picture-in-picture, rung 10 (2026-09-15)
1. **B-roll clip info** (read-only `ffmpeg -i`): `VID_20260416_203431.mp4`, **4:21.88**,
   1280×720 h264, 29.89 fps, **displaymatrix rotation −180°** (recorded upside down; CapCut
   should apply the rotation on import, to be checked on the player).
   - Frames at 5/20/40/60/90/120/150/180/210/240 s: `broll/b*.jpg`, sheet `broll/broll-sheet.png`.
2. **Import** (rung 3 route):
   - Click empty timeline (1000,690), `key ctrl+i`, `wait-for --id 1148` (2.0 s),
     `act set-value --id 1148 --value "E:\videos\VID_20260416_203431.mp4"`,
     `act invoke --id 1 --name Open`, wait 6 s.
   - **Agent-verified:** `draft_meta_info.json` lists `203431`, and `draft_content.json` diff vs
     `draft-22-before-import.json` = **0 lines** (importing never touches the timeline, as in
     rung 10). No extra windows (`55-broll-imported.png`).
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
