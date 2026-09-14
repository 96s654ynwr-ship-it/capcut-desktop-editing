# Capability 04: Bad-take removal via transcript

## Status
- **Ladder status:** approved (user, 2026-09-14: "Approve, start Cap 5")
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. Footage: `VID_20260720_190542.mp4` in practice
  project `0914 (4)`. Two earlier footage scans are recorded below: one had no retakes, the other
  was superseded.
- **Approved:** —
- **Consent:** the user said "Approve, try Cap 4 on 152759". Scan
  `E:\videos\VID_20260623_152759.mp4` (3:30, 1280×720) with Transcript. **If no repeated lines
  show up, stop and report.**
- **Practice project:** a new blank agent-owned project made with Create project (name recorded
  below).
- **Evidence:** `evidence/2026-09-14/cap4/`

## Goal
Find a line the speaker said more than once (a retake) in CapCut's transcript. Remove the bad
version natively and keep the good one. Name which take was kept, and confirm the removed range
with a draft diff.

## Preconditions
- Rungs 0–3 approved.
- Route from rung 3 reused as-is:
  1. Create project.
  2. Ctrl+I import.
  3. Drag the media card to the timeline.
  4. Select the clip.
  5. Click the Transcript toolbar icon.
  6. Wait for `RoughCutWindow` ("Remove filler words").

## Candidate native routes to test
1. **Repeats tab.** CapCut's own repeat detection. Items come pre-ticked; check what each item
   covers before pressing Delete.
2. **All tab, sentence rows.** Tick the transcript sentence(s) of the bad take and press Delete.
   This is text-based removal.
3. **Fallback without detection:** find the retake's timecodes in the All tab, then use the
   rung 1–2 tools on the timeline: split at start/end (Ctrl+B) and Backspace (ripple).

## Procedure

### A. Scan of `VID_20260623_152759.mp4` (executed 2026-09-14): no retakes, stopped as instructed
1. **Setup** reused the rung 3 route without changes:
   - Back to home page, then Create project. The new project is **`0914 (2)`**, found as the
     newest draft folder by creation time.
   - Ctrl+I → file dialog → set-value id 1148 → invoke Open.
   - Drag the media card (335,217) → (700,840). Draft: 1 segment, 0 → **209.533 s** (00:03:29:16),
     canvas 1920×1080.
2. **Transcript:** select the clip (700,830), click the Transcript icon (592,598).
   `RoughCutWindow` appeared after about **30 s** for a 3:30 clip. The draft was unchanged by the
   analysis.
3. **Result:**
   - **Repeats:** "No repeats identified".
   - **Filler words:** "No filler words identified".
   - **Pauses:** 1 item, **11.33 s at 00:00:25:00**, pre-ticked.
   - **All:** only **3 rows**, because the take is mostly gym footage with little speech:
     - an Arabic sentence at 00:00:11:20
     - the pause row
     - "Halo Makhluk Bumi" at 00:00:36:11, likely a misrecognised fragment
   - Nothing else across 5 scroll pages; the list doesn't scroll.
   - Footer Total duration preview: 00:03:18:06 (with the pause ticked).
4. **No repeated lines → stopped** per the user's instruction. Closed with **Cancel**; the
   pre-ticked pause was *not* removed. The draft was unchanged (diff against after-add: No
   differences).
5. **User follow-up (2026-09-14):** scan **`E:\videos\VID_20260622_140555.mp4`** (18:10,
   1280×720, 649 MB). The user says it contains bad takes and lines said twice. It's large, so the
   analysis runs as a background job with a 30 min timeout. Evidence: `evidence/2026-09-14/cap4/take2/`.
6. **Scan of `VID_20260622_140555.mp4` (executed 2026-09-14):**
   - **Setup:** new practice project **`0914 (3)`**, 1 segment 0 → **1090.267 s** (00:18:10:08),
     1920×1080.
   - **Analysis time:** `RoughCutWindow` appeared after about **155 s** for 18 min of footage
     (roughly 8.5 s per minute).
   - **Repeats:** **"No repeats identified"**, even though the user says the take contains lines
     said twice. CapCut's repeat detection didn't catch them. It may not support Arabic or
     paraphrased retakes. Don't rely on the Repeats tab alone.
   - **Filler words:** none.
   - **Pauses:** many, all pre-ticked (0.57–3.23 s each, starting 00:01:04:12). The footer preview
     with all pauses ticked shows **00:17:00:26**, about 70 s of pauses.
   - **All:** full Arabic transcript, one row per sentence, with pause rows interleaved.
   - **No transcript cache on disk.** Files written during analysis were only draft/meta, media
     info, the waveform, tracking DBs and prefs. The transcript text is only readable on screen.
   - **Reading the transcript:** scrolling the All list with `cc.py scroll 1440 450 -5` moved
     about 3 rows per step. 10 pages only reached 00:02:32. A full read needs paging the whole list
     (a background job saves pages until two identical captures in a row).
   - **Fallback plan:** find the duplicate sentences by reading the transcript, with hints from the
     user. Then remove the bad take either by ticking its sentence rows in All → Delete, or by
     timeline split + Backspace at the timecodes.
   - **Superseded:** asked where the retakes were, the user switched footage instead. Nothing was
     removed from `0914 (3)`; the window was closed with Cancel.
7. **Third footage (user choice, 2026-09-14): `E:\videos\VID_20260720_190542.mp4`.** Scanned in a
   new practice project with the same pipeline, and the whole transcript was paged to screenshots.
   Evidence: `evidence/2026-09-14/cap4/take3/`. The user's own project `0720` is not touched.
   - **Setup:** new practice project **`0914 (4)`**, 1 segment 0 → **523.467 s** (00:08:43:14).
   - **Analysis:** about **47 s**. The analysis didn't change the draft.
   - **Repeats tab:** **1 item**, a struck-through pill labelled "Repeats" (no duration shown) at
     **00:08:41:22**, pre-ticked.
   - **Pauses:** many short ones (0.50–2.10 s), pre-ticked.
   - **Filler words:** none.
   - **Footer:** with everything pre-ticked, "Total duration" previews **00:08:07:03**.
   - **All tab:** the transcript was paged to **22 screenshots**
     (`transcript/p001–p022.png`, `scroll -12` per page) to look for duplicate lines by eye.
   - `0914 (3)` was re-checked after the switch: unchanged (No differences).
   - **Duplicate lines found by reading the transcript** (the agent can't hear the audio):
     1. **Opening said about 3 times.**
        - First attempt: 00:00:04:04 «بسم الله» → 00:00:05:27 «الرحمن الرحيم اللهم صل…» →
          00:00:11:25 «…انا زهقت من التاجيل وجالي فترة كبيرة…» → … → about 00:00:31:05.
        - Restart: 00:00:37:23 «زهجت من التاجيل خلاص خلاص زهجت من التاجيل وعايز».
        - Final take: the 00:00:45:05 row «بقى لي فترة كبيرة بسم», then 00:00:47:23 «الله الرحمن
          الرحيم زهقت من التاجيل وخلاص» → 00:00:53:23 «بقى لي فترة عايز اعمل براند…», continuous
          from there.
        - The row boundary doesn't match the take boundary: the good take's «بسم» starts inside
          the 00:00:45:05 row.
     2. **Phrase repeated:** 00:04:52:25 «…فانا لو هاشترك في حاجة واحدة بس» → 00:04:58:01 «فانا
        لو هاشترك في حاجة واحدة بس هاشترك في كلود…».
     3. **CapCut's detected "Repeats"** at 00:08:41:22 comes after the sign-off «…السلام عليكم»
        (00:08:25:07) and a 9.60 s pause, so it's a tail after the real ending.
   - **User decision (2026-09-14): "Opening + 4:52 phrase".** Two cuts:
     - Remove the opening false starts from 00:00:00:00 to 00:00:47:23 (the kept take starts at
       «الله الرحمن الرحيم زهقت من التاجيل…»).
     - Remove the first «فانا لو هاشترك في حاجة واحدة بس».
     - **Order:** do the **later cut first**. With the main track magnet on, the opening cut
       ripples everything left and would shift the 4:52 timecodes.
     - **Precision caveat:** the first «فانا لو هاشترك…» sits at the *end* of the 00:04:52:25 row,
       after «شامل وبشكل كويس خالص». Cutting the whole row would also remove that. Locate the
       phrase start inside the row using the waveform gap, and report the chosen frame.
   - **Zooming for frame precision (agent-verified 2026-09-14):**
     - At default zoom the 8:43 clip filled x 228–782: **≈1.05 px/s** (≈28 frames/px), which is
       useless for exact cuts.
     - Click the ruler near the target (x=536 for 04:52 gave **00:04:51:12**).
     - Press `cc.py key ctrl+=` **×6**. The zoom centres on the playhead and the zoom slider moves
       right.
     - New scale: 04:45 → x 410, 04:50 → 748, 04:55 → 1085, 05:00 → 1422 = **≈67.4 px/s** (≈2.2 px
       per frame).
     - Always re-measure from the ruler labels after zooming.
     - The waveform is a thin strip under the thumbnails (y ≈ 855–875). Crop it with
       `screenshot --region` to read speech gaps.
   - **Waveform limitation (observed 2026-09-14):** even at ≈67 px/s, the main-track waveform is
     only a ~15 px strip under the thumbnails. From 04:45 to 05:05 it looked uniformly dense, with
     no readable speech gaps. CapCut detected no pause between 04:52 and 04:58, so the phrases
     run on. The agent **cannot locate a sub-row word boundary** from the waveform at the default
     track height, and it can't hear audio. Options:
     - **(a)** Ask the user for the time: they know their footage.
     - **(b)** Get word-level timings from Auto captions. The draft's `texts[].words` store
       per-word `start_time`/`end_time` (seen in project 0728). That's a Pro feature and needs
       consent.
     - **(c)** Enlarge the track height or waveform view (route not yet mapped).
     - **(d)** Proportional estimate inside the sentence row. Imprecise; last resort.
   - **User decision (2026-09-14): "Use captions for word timing".** The user consents to
     generating Auto captions (Pro, may use credits) on practice project `0914 (4)`. Plan:
     1. Read the per-word timings with `draft_inspect.py words <project> --around 295`.
     2. Cut at the word boundaries.
     3. Remove the generated captions again.
   - **Auto captions for word timing (executed + agent-verified 2026-09-14):**
     - **Route:** Asset tab **Captions** (≈423,65) → Auto captions panel. Defaults: Spoken language
       *Auto detect*, Bilingual *None*, *Identify filler words* ON, *Delete current captions*
       unticked. Click **Generate** (Pro tag, ≈445,544).
     - **No confirmation/credit dialog.** A named loading window appears in the tree:
       `Window id="Generating captions... 0%"` (cls `LVLoadingDialog_QMLTYPE_*`, 400×230 centred).
       The percentage is in the AutomationId, so it can be polled.
     - **Duration:** captions appeared in the draft (non-empty `text` track) after **≈122 s**
       for 8:43 of Arabic speech.
     - **Word timings:** `draft_inspect.py words "0914 (4)" --around 295 --window 9` (saved to
       `words-around-295.json` / `words-around-45.json`). Per-word start/end sit on the timeline
       clock. Caption sentence splits differ from the Transcript rows, and captions are more
       precise.
   - **Exact cut points from word timings:**
     - **4:5x repeat:**
       - «خالص» ends 294.707 s
       - 1st «فانا لو هاشترك في حاجة 1 بس» 295.900 → 297.980
       - 2nd «فانا لو هاشترك في حاجة 1 بس» 298.800 → 300.200
       - then «هاشترك في كلود…» at 300.300

       Remove the 1st occurrence, cutting in the middle of the silences: **295.300 s
       (00:04:55:09) → 298.400 s (00:04:58:12)**, 3.100 s.
     - **Opening:**
       - last bad-take words «…بقالي فترة كبيرة» end 46.333 s
       - kept take «بسم الله الرحمن الرحيم» starts **47.533 s**, followed by «زهجت من التاجيل
         وخلاص» at 50.733

       The captions show «بسم» *is* recoverable, so cut **00:00:00:00 → 46.933 s (00:00:46:28)**,
       the silence midpoint. That refines the user-approved 0:47:23, which would have clipped
       «الله». Report this refinement.
     - **Order:** 4:55 cut first, then the opening (ripple would otherwise shift 4:55 by 46.933 s).
     - **Captions removed** before cutting by **Ctrl+Z** (the generation is one undo step), so the
       video cuts aren't entangled with a caption track.
       - Verified: 290 caption segments were gone after one Ctrl+Z; diff against pre-caption
         state was No differences.
     - **Execution plan (splits don't move anything; only deletes ripple):**
       1. Zoom to fit (**Shift+Z**).
       2. For each cut frame: click the ruler near it, zoom into the timecode, step with ←/→ to
          the exact frame, re-read, then **Ctrl+B** with the clip selected.
       3. Split at 00:04:58:12, 00:04:55:09 and 00:00:46:28.
       4. Select the 04:55:09–04:58:12 piece → **Backspace** (ripple).
       5. Select the 00:00:00–00:00:46:28 piece → **Backspace** (ripple).
       6. Diff: expect 2 segments, [0 → 248.367 s, src 46.933] + [248.367 → 473.433 s, src 298.400].
          Total 523.467 − 3.100 − 46.933 = **473.433 s**.
     - After zooming in, the timeline view **scrolled back to 00:00** once the captions were
       undone. Re-read the ruler before every click.
     - **Zoom to fit (Shift+Z, verified):** the 8:43 clip spans x 230 → 1527. Ruler: 00:00 = 230,
       02:00 = 527, 04:00 = 824, 06:00 = 1121, 08:00 = 1418, so **≈2.475 px/s** (≈12 frames/px).
     - **Ruler-click accuracy at fit zoom:** clicking x = 230 + 298.4 × 2.475 = 969 for 04:58:12
       landed on **04:57:24**, 18 frames early. Correct with `cc.py key right --repeat 18`, then
       confirm by the draft split time (authoritative).
     - **Split 1 (agent-verified 2026-09-14):**
       - → ×18, then select the clip by clicking its body at x=400 (far from the playhead).
       - **Ctrl+B**, saved about 2 s later.
       - Draft: `[0] 0 → 298.400 s, src 0` + `[1] 298.400 → 523.467 s, src 298.400`. Exactly
         00:04:58:12.
       - **Calibration for later clicks:** the effective ruler offset is about −0.79 s, so aim at
         x = 230 + (t + 0.79) × 2.475.
     - **Split 2 (agent-verified 2026-09-14):**
       - A calibrated ruler click at x=963 landed on 04:55:11, then ← ×2.
       - Selected the clip at x=400 and pressed **Ctrl+B**.
       - Draft: 3 segments, `[0] 0 → 295.300`, `[1] 295.300 → 298.400 (src 295.300)`,
         `[2] 298.400 → 523.467`.
       - The middle 3.100 s piece is exactly the first «فانا لو هاشترك في حاجة 1 بس» plus half of
         each surrounding silence.
       - With the calibration, the click landed within 2 frames.
     - **Split 3 (agent-verified 2026-09-14):**
       - A calibrated ruler click at x=348 landed on 00:00:47:29, then ← ×31 to 00:00:46:28.
       - Selected the clip at x=700 and pressed **Ctrl+B**.
       - Draft: **4 segments**, `[0] 0 → 46.933` · `[1] 46.933 → 295.300` · `[2] 295.300 →
         298.400` · `[3] 298.400 → 523.467`. Each segment's src matches its start (no deletes
         yet).
       - A PowerShell gate parsed the summary JSON and checked all three boundaries (±1 frame)
         before continuing.
       - **Small pieces:** at fit zoom segment 2 (3.1 s) is only about 8 px wide. Place the
         playhead inside it and press **Ctrl+= ×6** so it becomes wide enough to click safely.
       - **Observed:** a ruler click at x=967 snapped to the **boundary** (04:58:12) instead of
         landing inside the piece. Snapping is on, so ruler clicks within a few px of a cut snap
         to it.
       - After Ctrl+= ×6 the scale was about 159 px/s (04:54 = 270, 04:56 = 590, 04:58 = 908,
         05:00 = 1227). Segment 2, labelled `00:00:03:03`, spanned x ≈ 478 → 972.
       - A **yellow CapCut tip bubble** ("…cut long videos…") appeared over the timecode area near
         the top of the timeline panel. It was harmless and didn't cover the tracks.
     - **Delete 1, the repeated phrase (agent-verified 2026-09-14):**
       - Clicked segment 2's centre (x=725 at ≈159 px/s), then pressed **Backspace**. Ripple
         closed the gap.
       - Draft: 3 segments, `[2] 295.300 → 520.367 s, src 298.400`. Duration 523.467 → 520.367.
       - A structure gate (count, start, src) confirmed it before continuing.
     - **Delete 2, the opening (agent-verified 2026-09-14):**
       - **Shift+Z** (fit), clicked segment 0's centre (x=288; the segment spans ≈230–347), then
         **Backspace**.
       - Draft: **2 segments**, `[0] 0 → 248.367 s, src 46.933` · `[1] 248.367 → 473.433 s, src
         298.400`.
       - **Duration 523.467 → 473.433 s** (−46.933 opening, −3.100 repeat).
       - The result now opens on «بسم الله الرحمن الرحيم زهجت من التاجيل وخلاص…» and says
         «فانا لو هاشترك في حاجة 1 بس هاشترك في كلود» once.
     - **Script pitfall hit:** PowerShell `$s` overwrote `$S`, so the first delete-2 attempt
       aborted safely at a gate before any click. See platform-claude-code.md.
     - **Verification (agent-verified 2026-09-14):**
       - **Spot-check:**
         - Home → **00:00:00:00**, total **00:07:53:13**.
         - ↓ (next cut point) → **00:04:08:11**, exactly the join.
         - ← gives 04:08:10 and → → gives 04:08:12. The frames either side show the same shot
           with a small pose/hand jump, a normal talking-head jump cut.
       - **Undo/redo of delete 2:**
         - Ctrl+Z, then diff against `after-del1.json`: **No differences**.
         - Ctrl+Shift+Z, then diff against `after-del2.json`: **No differences**. Each delete is
           one undo step.
       - **Saved:** Menu ▸ Back to home page (tree root `HomeWindow`), then diff against
         `after-del2.json`: **No differences** on disk.
       - **Scope:** the user's projects (0707, 0720, 0728, the Arabic-titled one) have unchanged
         mtimes. Only agent-owned practice projects were touched.
     - **Final result in practice project `0914 (4)`:** 473.433 s. The false-start opening and the
       first repeated phrase are removed. The captions used for timing were removed again.
       - **Not removed**, because they weren't requested: CapCut's pre-ticked pauses, and its
         "Repeats" tail at the old 08:41:22, now ≈07:51.
   - **Lesson:** CapCut's Repeats tab missed the obvious spoken retakes in Arabic. Read the All
     transcript and compare sentences. Transcript rows are *sentence starts*, not take
     boundaries, so a precise cut may need timeline split/trim (or the waveform, rung 5) rather
     than row deletion alone.
8. **What rung 4 needs:** a talking-head take where the same line is said at least twice. CapCut's
   **Repeats** tab should list those. Otherwise use the All tab's sentence rows to find duplicate
   text and the timecodes to cut.

## Wait conditions
- Analysis: `cc.py wait-for --cls RoughCutWindow --timeout 900`. Expect roughly 15–40 s for 3:30.

## Verification
- **Draft diff:** the duration shrinks by the removed take's length, and the new segment's
  `src_start` equals the end of the removed range.
- **Visual:** ↓ lands on the cut, and the frames or lines on either side show the kept take
  continuing.
- **Undo** returns to the pre-delete draft.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery
Ctrl+Z, verified by a diff against the pre-delete summary.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes
Same as rung 3: `RoughCutWindow`, `RollingLoading.qml` and the native file dialog are named in
the tree. Everything else is screenshot-driven.

## Open questions for the user
