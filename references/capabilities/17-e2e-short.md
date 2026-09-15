# Capability 17: End-to-end vertical short

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** a CapCut **Duplicate** of the approved rung-16 project `0915 (1)` (the
  original stays untouched)
- **Evidence:** `evidence/2026-09-15/cap17/`

## Goal
Turn one 30–60 s highlight of the approved YouTube edit into a finished 9:16 short, using only
approved rungs, and export it verified.

## User choices (2026-09-15)
- **Source:** "Highlight of 0915 (1) (Recommended)". Duplicate the approved edit; the agent
  proposes highlight ranges from the captions and the user picks one.
- **Length:** "30–60 s (Recommended)".
- **Steps:**
  - "Captions 9:16 + hook title (Recommended)": house-style captions resized for 9:16 (rung 12:
    size 22, `transform.y` −0.4) and an Arabic hook title in the first 3 s
  - "Tighter pacing (Recommended)": an extra gap pass for short-form pace
  - "Logo (Recommended)": re-placed for the 9:16 frame
  - "Punch-ins": scale punch-ins at joins on top of the Auto reframe crop
- **Export:** "1080×1920 30fps H.264 → exports (Recommended)": the rung-15 route, cloud sync
  off, ffmpeg verification.
- **Standing rules still apply:**
  - credits OK for Transcript and Auto captions
  - Pro tools: "run; stop if a cost appears"
  - never touch the user's projects
  - native UI only, draft JSON read-only
  - confirm purchases, cloud, deletes and downloads

## Preconditions
- Rungs 1–16 approved. Routes reused:
  - rung 14 Duplicate
  - rung 12 trim-to-section, 9:16 and Auto reframe
  - rung 5 gap pass
  - rung 6 punch-ins
  - rungs 8–9 captions and title
  - rung 14 logo
  - rung 15 export
- `0915 (1)`: 403.300 s, 56 main segments, 252 captions, title, B-roll PiP (12.067–16.067 s),
  logo track, Enhance voice results cached.

## Plan (stage gates, each verified before the next)
1. **Highlight candidates (read-only):** caption dump of `0915 (1)`; propose 30–60 s ranges that
   start and end on sentence boundaries; the user picks.
2. **Duplicate** `0915 (1)` from Home (card right-click ▸ Duplicate, rung 14) and open the copy.
3. **Trim to the highlight:** split all at the range end and delete right, then split all at the
   range start and delete left (rung 12 §C–E, main-track magnet ripples). Verify duration,
   captions, and that the audio effects stay referenced.
4. **Tighter pacing:** a gap pass on the short only (dry run first, then the chosen threshold).
5. **9:16 + Auto reframe** (rung 12 §F–H): Ratio ▸ 9:16, then Auto reframe on the main clips.
   Verify `smart_crops` and frames.
6. **Punch-ins** at selected joins, derived for the reframed shot. Check the eye line in frames.
7. **Captions for 9:16:** size 22, `transform.y` −0.4 (rung 12 §I), check in frames. **Hook
   title** in the first 3 s. **Logo** re-placed for 9:16; the old title and B-roll are removed or
   refit if they fall inside the range.
8. **Save**, undo/redo spot gates, scope check.
9. **Export** 1080×1920 30 fps H.264 to `E:\videos\exports`; verify streams, frame count vs the
   draft, loudness and frames.
10. Write up, contact sheet, ask for approval.

## Procedure

### A. Highlight candidates (read-only, 2026-09-15)
- Caption dump of `0915 (1)` (`draft_inspect.py words "0915 (1)" --json`, 252 captions,
  `cap17/words-0915-1.txt`). Baselines: `scope-before.txt`, `draft-source-0915-1.json`.
- Candidates on sentence boundaries:

  | # | Range (s) | Length | Content | Hook title offered |
  |---|---|---|---|---|
  | A | 19.8 → 54.0 | 34 s | the idea: an AI Sharia auditor instead of hiring one (has a «مش فاكره دلوقتي» stumble) | «مدقق شرعي بالذكاء الاصطناعي» |
  | **B** | **215.1 → 249.2** | **34 s** | why the product must offer what Gemini can't, or nobody pays | «ليه لازم نتميز عن جيميناي؟» |
  | C | 254.9 → 300.8 | 46 s | how to build it: a RAG app on AAOIFI data over Gemini | «هنبنيه ازاي؟» |

  (The MCP-server section, 120–175 s, was left out: an unclear «المعاين الفري» and no clean ending.)
- **User choice:** "B: Beat Gemini 3:35–4:09 (Recommended)".
- **Exact range, snapped to 30 fps:** **215.133 → 249.200 s (34.067 s)**
  - start = 0.125 s before «الحتة» (215.267); previous caption «او ال» ends 214.467
  - end = 0.2 s after «سبسكرايبشن» (249.000); next caption «تمام دي حتة دي كده» starts 250.333
  - The title (1–4 s) and B-roll (12.067–16.067 s) fall outside, so the trim removes them; the hook
    title is new.
- **Range check** (`range_check17.py` on the source copy, `range-check-source.txt`):
  - **Main track:**
    - Start 215.133 lies inside seg 29 (211.633 → 217.067), 58 frames before its join.
    - **End 249.200 is only 5 frames before the join 249.367.** A ruler click there would snap onto
      the join or the caption end at 249.000, and Ctrl+B on a boundary does nothing (rung 16).
    - **Revised end = the join 249.367** (still silence; the next caption starts 250.333), so only
      the full-length logo needs splitting there.
    - **Final range: 215.133 → 249.367 (34.233 s).**
  - **In range:**
    - main segs 29 (part, wide), **30 (punched 110 % / Y −60)**, 31 (wide), **32 (punched)**; no
      keyframes
    - captions 128–144 (17), `transform.y` −0.73
    - the logo (0 → 403.3) crosses both cut points
  - Title track 2 and B-roll track 3 have nothing in range.

### B. Leave `0915 (1)` for Home (executed + agent-verified 2026-09-15)
- Menu (140,22) checked by screenshot (`02-menu-open.png`), then **Back to home page** (183,303).
  `wait-for --cls HomeWindow` timed out (20 s), but the screenshot shows Home (`03-home.png`).
  Confirm Home by screenshot, not by that wait.
- ⚠ **Leaving re-saved `0915 (1)`** (mtime → 17:11:40, SHA-256 changed), as in rung 16 §B.
  - The diff vs `draft-source-0915-1.json` (`diff-source-leave.txt`, 145 lines) is
    **housekeeping only**:
    - the disabled `loudnesses[0]` placeholder plus the logo's refs to it, and a regenerated
      `vocal_separations[57].id`
    - `sound_channel_mappings[*].type` "" → "none"
    - float/µs rounding: scale 1.0999… → 1.1, ±1 µs on source ranges, text-template width digits
  - No timing, transform, text or visibility change. The approved rung-16 edit is intact.
- **Home** after `scroll 1000 700 -3` (`04-home-projects.png`): the first card is **`0915 (1)`
  454.5M | 06:44** at ≈(383,793). 17 project folders before duplicating.

### C. Duplicate `0915 (1)` (executed + agent-verified 2026-09-15)
1. Right-click the card (383,793) (`05-card-menu.png`): **Upload** ≈(423,816) (cloud, never click) /
   **Rename** ≈(426,856) / **Duplicate** ≈(430,902) / **Delete ←Backspace** ≈(421,942), the same
   menu as rung 14. ⚠ Delete sits directly under Duplicate.
2. Click **Duplicate** (430,902):
   - The new folder **`0915 (1)-copy`** appeared on the first 0.5 s poll (18 folders).
   - A "Copied" toast appears at the top (`06-after-duplicate.png`).
   - The new card **`0915 (1)-copy` 454.5M | 06:44** is **first** at ≈(383,793); `0915 (1)`
     moves to second ≈(566,793).
3. **Agent-verified:**
   - the copy's `draft_content.json` is **SHA-256 identical** to the source (`draft_diff` 0 lines;
     baseline `copy-baseline.json`)
   - the copy's mtime equals the source's (17:11:40.757, copied, as in rung 14)
   - the source hash is unchanged by the duplicate

### D. Open the copy (executed 2026-09-15)
- Click the `0915 (1)-copy` card (383,793), wait 6 s, then `focus --maximize`.
- At 7 s the editor still showed **"Interface is being loaded. Wait a minute."** over empty
  panels (`07-copy-opened.png`). That's longer than rung 16's reopen, probably because of 252
  captions plus 56 enhanced clips. Loaded by +17 s (`08-copy-loaded.png`).
  - Title bar **"0915 (1)-copy"**; Details Name/Path are the copy's.
  - Timeline identical to the source.
  - Draft hash unchanged by opening.
- **Layout at fit zoom:** ruler 00:00 x≈229, 02:00 x≈601, 04:00 x≈974 (**≈3.111 px/s**).
  - Rows: logo y≈680 (top), B-roll ≈748, title ≈798, captions ≈830, main ≈895.
  - The tool icon is the plain arrow (Select).

### E. Trim to the highlight: end cut at 249.367 (2026-09-15)
1. **Playhead to 00:04:09:11** (frame 7481):
   - Click empty B-roll row (1650,748), then ruler click x **1005** (= 229 + 249.367 × 3.111).
   - It snapped to **00:04:07:08** (247.267, the end of caption 143) (`09-tc-end.png`).
   - `key right --repeat 63 --gap 0.1` got only to **00:04:08:07**: the "Couldn't output sound"
     modal opened mid-run (see Failure modes). **Hide**, then the remaining **34** frames in
     batches of 10, checking `cc.py windows` for the modal after each batch. No modal came back →
     **00:04:09:11** (`13-tc-end-stepped.png`). Draft unchanged throughout.
2. **Pre-split gate** (`split_check17.py 249.367`, `split-end-before.txt`):
   - 5 tracks, 311 segments
   - main 33 before / 23 after / 0 straddling (249.367 is an existing join)
   - captions 145 / 107 / 0; title 1 / 0; B-roll 1 / 0
   - **only the logo (0 → 403.3) straddles**
3. **Split all** `ctrl+shift+b` (nothing selected). The draft saved on the first 0.5 s poll
   (`split-end-after.txt`, snapshot `draft-01-split-end.json`):
   - **312 segments** (+1); **logo 1 before / 1 after / 0 straddling**
   - main 33 / 23, captions 145 / 107, title 1 / 0, B-roll 1 / 0, all unchanged
   - duration 403.300 s; no sound modal
   - Split all on an existing main join just leaves the main track alone and splits only what
     crosses the playhead, as in rung 12.
4. **Zoom for the selection:** `key "ctrl+=" --repeat 4 --gap 0.3`. The playhead stays at
   00:04:09:11, screen x≈1004 (`14-zoomed-end.png`, `14-tc-zoomed.png`). The draft is unchanged.
   - **≈49.8 px/s** (ruler 04:05 at x≈786, 04:10 at x≈1035).
   - Logo row y≈680: the right piece "logo-ink-tight.png 00:02:33:28" starts at the playhead.
   - Captions y≈831: the first one right of the cut, «تمام دي حتة دي كده», starts at x≈1050
     (250.333).
   - Main y≈900: seg 33 "00:00:06:16" at x≈1006–1328. The title and B-roll rows are empty here.
5. **Select rightward mode:** the first `]` was lost (foreground warning, see Failure modes). After
   `cc.py focus` and `]`, the tool icon crop (10,578)–(170,614) shows the **double-arrow glyph**
   (`18-tool-icon-after-bracket.png`). The draft is unchanged.
6. **Rightward selection:** click main seg 33 at **(1020,900)**, 0.3 s right of the cut
   (`19-selected-rightward.png`). White borders mark:
   - the **right logo piece** (from the cut), **main seg 33 and every clip after it**, and **every
     caption from «تمام دي حتة دي كده» (250.333) on**
   - nothing left of the cut: the left logo piece, seg 32 and the captions up to «او سبسكرايبشن»
     are not bordered
   - So a segment that **starts before the click point but after the cut** (seg 33 and the logo
     piece both start at 249.367, the click is at ≈249.69) **is included**. The mode selects
     segments that extend right of the click, not only those starting after it.
   - Inspector: **Properties** (Transform with mixed "-" values) (`19-inspector.png`). The
     playhead stays at 00:04:10:02; the draft is unchanged.
7. **Delete** (`key delete`). The draft saved on the first 0.5 s poll (`delete-right-after.txt`,
   snapshot `draft-02-right-deleted.json`):
   - **duration 403.300 → 249.367 s**, segments 312 → **181**
   - after 249.367: main **0**, captions **0**, title 0, B-roll 0, logo **0**
   - before: main **33**, captions **145**, title 1, B-roll 1, logo **1**, all unchanged
   - one key, one save; no sound modal
   - Then **A** to return to the Select tool (`20-tool-icon-after-A.png`).
   - **After the delete** (`20-after-delete-right.png`):
     - the player reads **00:04:09:11 / 00:04:09:11**, with the playhead at the new end
       (x≈1380 at this zoom)
     - the header shows "Auto saved: 17:23:44"
     - the view stays zoomed: ruler 03:45 x≈170 … 04:05 x≈1165 (49.8 px/s), so 215.133 is
       off-screen left
8. **Undo/redo gate** (after an empty-timeline click (1650,748)):
   - **Ctrl+Z** saved within 0.5 s → **403.300 s, 312 segments**, main 33 / 23, captions 145 / 107,
     logo 1 / 1. That is exactly the post-split state, and one undo step restored all 131
     segments.
   - **Ctrl+Shift+Z** saved within 1 s → **249.367 s, 181 segments**, all "after" counts 0.
     **Byte-identical to `draft-02-right-deleted.json`.**
   - Then **Shift+Z** to fit the shorter timeline (`21-fit-after-gate.png`). No sound modal.

### F. Trim to the highlight: start cut at 215.133 (2026-09-15)
1. **Pre-split gate** (`split_check17.py 215.133`, `split-start-before.txt`):
   - 249.367 s, 181 segments
   - **main straddling 1 (seg 29, 211.633 → 217.067)**, 29 before / 3 after
   - captions 128 before / **17 after** / 0 straddling (the gap between «او ال» 214.467 and «الحتة»
     215.267)
   - title 1 before; B-roll 1 before
   - **logo straddling 1 (0 → 249.367)**
2. **Fit layout for the 249.367 s timeline** (`21-fit-after-gate.png`):
   - ruler 00:00 x≈229, 01:00 x≈541, 02:00 x≈853, 03:00 x≈1166, 04:00 x≈1479 (**≈5.208 px/s**)
   - rows as before; main clips end, and the playhead sits, at x≈1529
   - target 215.133 → x≈**1350**, between the «او ال» caption end (214.467, x≈1346) and «الحتة»
     start (215.267, x≈1350), so a ruler click is expected to snap to one of them
3. **Playhead to 00:03:35:04** (frame 6454):
   - Empty click (1650,748), then ruler click (1350,628).
   - It snapped to **00:03:33:20** (213.667, the **start** of «او ال», not a nearer edge)
     (`22-tc-start-ruler.png`). The draft is unchanged.
   - Then **+44 frames** in batches of 10 with a modal check after each (`23-tc-start-stepped.png`).
   - All 44 presses registered: the crop reads **00:03:35:04**. No warning or modal; the draft is
     still byte-identical to `draft-02-right-deleted.json`.
4. **Split all** `ctrl+shift+b`. The draft saved on the first 0.5 s poll (`split-start-after.txt`,
   snapshot `draft-03-split-start.json`):
   - **183 segments** (+2: main seg 29 and the logo each split)
   - **0 straddling on every track**
   - main 30 before / **4 after**, captions 128 / **17**, logo 1 / **1**, title 1 / 0, B-roll 1 / 0
   - duration still 249.367 s; no sound modal
5. **Open question before deleting left:** rung 2 only proved that a delete **within the main
   track** ripples with the magnet on. Rungs 4 and 16 undid captions before cutting, and no rung
   has shown whether **captions and overlay tracks shift too** when a multi-track selection left of
   the cut is deleted.
   - **Plan:** Select leftward + Delete, then `left_delete_check17.py`. It matches every kept
     segment by `id` against `draft-03-split-start.json` and requires a start shift of exactly
     **−215.133 s** on every track and unchanged durations.
   - Anything else → **Ctrl+Z** (one step) and change the approach.
6. **Select leftward mode:** `cc.py focus`, then `key "["` with no foreground warning. The tool icon
   crop shows the **mirrored double-arrow glyph** (`24-tool-icon-leftward.png`). The draft is
   unchanged.
   - Click target: inside the **left piece of seg 29** (211.633 → 215.133, x≈1331–1349 at fit)
     at **(1340,895)** ≈ 214.4 s.
7. **Observed: Select leftward + clip click selected ONLY the clicked clip.**
   - `25-leftward-near-cut.png` / `25-leftward-full.png`: a white border on the seg-29 left piece
     only. No border on earlier main clips, captions, the left logo piece, the title or the B-roll.
   - The toolbar switched to the single-clip tool set.
   - The inspector shows the single-clip **Video / Audio / Speed / Animation / Adjust** tabs, Basic
     Scale 100 %, X 0 / Y 0 (`26-inspector-after-left-click.png`).
   - The tool icon is still the leftward glyph (`26-tool-icon-after-left-click.png`); the playhead
     stays 00:03:35:04; the draft is unchanged.
   - **Not symmetric with Select rightward** (§E.6). Not deleted; testing an empty-row click
     next.
8. **Select leftward + click on an EMPTY row selects everything left of the click x.** Still in
   leftward mode, a click on the empty B-roll row at **(1340,748)** (`27-leftward-empty-click-full.png`)
   put white borders on:
   - the left logo piece (0 → 215.133), the B-roll clip and the title
   - **every caption up to «او ال»** and **every main clip up to the cut**
   - **Nothing right of the cut:** not the logo right piece, the 17 kept captions or the 4 main
     pieces.
   - Inspector **Properties** (multi, mixed "-") (`27-inspector.png`); the tool is still leftward;
     the playhead is 00:03:35:04; the draft is unchanged.
   - **Rule:** in Select leftward mode, click **empty track space** just left of the cut. A click
     on a clip selects only that clip. (Select rightward with a clip click selected everything
     rightward in §E.6.)
9. **Delete** (`key delete`). The draft saved on the first 0.5 s poll (`left_delete_check17.py` →
   `delete-left-check.txt`, snapshot `draft-04-left-deleted.json`). Segments are matched by id vs
   `draft-03`:

   | Track | Kept | Removed | Start shift of kept |
   |---|---|---|---|
   | 0 main | 4 | 30 | **−215.133 ×4** (magnet ripple) |
   | 1 captions | 17 | 128 | **−215.133 ×17**: the caption track **rippled with the main track** |
   | 2 title | 0 | 1 | track removed |
   | 3 B-roll | 0 | 1 | track removed |
   | 4 logo (overlay) | 1 | 1 | **0.0**: **overlay tracks do NOT ripple** |

   - 3 tracks, 22 segments, no new ids, durations unchanged.
   - ⚠ **Duration still 249.367 s** because the kept logo piece stays at 215.133 → 249.367.
   - **Fix:** drag the logo piece to start 0 (Select tool), then re-check. Undo isn't needed; the
     main and caption result is exactly as intended.
   - Then **A** (`28-tool-icon-after-A.png`); no sound modal.
   - **Observed after the delete** (`28-after-delete-left.png`, fit zoom unchanged, 5.208 px/s):
     - rows are now logo (overlay) **y≈744**, captions **y≈794**, main **y≈860**
     - main clips and captions at x≈229–405 (0 → 34.233)
     - the logo piece alone at x≈1352–1528 (215.133 → 249.367)
     - the player is black at the playhead 00:03:35:04 (no footage there any more); the tool is
       the plain arrow
10. **Move the logo piece to 0:** `drag 1440 744 317 744 --steps 60 --hold 0.4` (−1123 px ≈
    −215.6 s, slightly past 0 so it clamps or snaps to the timeline start), then
    `left_delete_check17.py` again (`logo-drag-check.txt`).
    - The draft saved on the first 0.5 s poll. **RESULT: all kept segments shifted by exactly
      −215.133 s**: main 4, captions 17, **logo 1** (it clamped exactly to 0), no new ids,
      durations unchanged.
    - **Trimmed: duration 34.233 s, 3 tracks (main / captions / logo), 22 segments**;
      `split_check17.py 34.233` shows every track ends at or before 34.233 (snapshot
      `draft-05-trimmed.json`).
    - **Trim recipe (proven):**
      1. Split all at the end cut → `]` + clip click right of the cut → Delete
      2. Split all at the start cut → `[` + **empty-row** click left of the cut → Delete (the
         main and caption tracks ripple)
      3. Drag each overlay piece left past 0 (they don't ripple)
      4. Verify by segment id
11. **Trimmed content check** (`range_check17.py` on `draft-05-trimmed.json` → `trimmed-content.txt`):
    - **main 4 segments:**
      - 0 → 1.933 wide
      - **1.933 → 9.400 punched** (1.1 / Y −0.0556)
      - 9.400 → 24.167 wide
      - **24.167 → 34.233 punched**
      - no keyframes
    - **captions 17**, first 0.133 («الحتة…»), last 32.933 → 33.867, all `transform.y` −0.73
    - **logo 0 → 34.233**, scale 0.12, tf (0.83854, 0.80926), unchanged
    - **audio:** materials realtime_denoises 4 / vocal_beautifys 4 / loudnesses 1 (the disabled
      placeholder); **each of the 4 main segments references one denoise and one enhance**, so the
      Enhance-voice results carried through the trim
    - **Observed** (`29-after-logo-drag.png`): the logo is selected after the drag (inspector 12 %,
      X 1610 / Y 874); the player shows speaker + logo at 00:00:34:07, the end
12. **Undo/redo gate on the logo drag** (after an empty click (1650,950)):
    - Ctrl+Z → **249.367 s**, logo after 34.233 again
    - Ctrl+Shift+Z → **34.233 s**, **byte-identical to `draft-05-trimmed.json`**
    - each step saved within 0.5 s; no modal

### G. Tighter pacing: gap pass on the short (2026-09-15)
1. **Dry run** `tighten_gaps.py --project "0915 (1)-copy" --all --min 0.6 --keep 0.125 --dry-run`
   (`tighten-dryrun-0.6.txt`): 4 video segments, **6 real gaps ≥ 0.6 s**, **34.233 → 31.367 s
   (−2.866 s)**:

   | Remove | s | Words |
   |---|---|---|
   | 32.267 → 32.800 | 0.533 | «دي» \| «او» |
   | 27.633 → 28.033 | 0.400 | «عندنا» \| «انت» |
   | 21.667 → 22.100 | 0.433 | «لازمة» \| «لازم» |
   | 17.133 → 17.500 | 0.367 | «شرعي» \| «زي» |
   | 12.200 → 12.800 | 0.600 | «شركة» \| «وراحت» |
   | 6.533 → 7.067 | 0.533 | «دي» \| «ما» |

   - The result stays ≥ 30 s, so the user's "Tighter pacing (Recommended)" at the suggested
     0.6 s threshold is used as is.
   - **Every removal lies between two captions**, e.g. 12.200–12.800 between caption 6 (ends
     12.067) and caption 7 (starts 12.933). No caption is cut.
   - **Unlike rung 16, the captions must survive the cuts** (template, the «لجيميناي» fix). After
     the run, `caption_shift_check17.py` checks that every caption kept its id, text, duration and
     transform and moved by exactly the removed total before it, and that the logo still starts
     at 0.
2. ⚠ **`tighten_gaps.py` can't run here unchanged.**
   - It aborts with "captions are still on the timeline; re-run with --undo-captions" when a
     caption track exists.
   - `--undo-captions` presses Ctrl+Z and expects exactly the captions to disappear. Here the last
     action is the logo drag, so it would undo that (the script's own check would then abort).
   - Its layout defaults (`--clip-y 830`, `--empty 1500,760`) are for the 4-track rung-16
     layout; the main row is now **y≈860**.
   - **Route:** a cap17 runner reusing its verified primitives (`place_exact`, `remove_range`) the
     way `cap16/tighten_cap16.py` did, **without** the caption guard, with the current layout,
     and checking captions after the first cut before continuing.
3. **Runner `cap17/tighten_cap17.py`** imports `tighten_gaps` and cap16's `place_exact_anchor`
   (shared module object), and changes four things:
   - **Captions kept:** after every W it re-reads the caption track and requires captions after the
     cut to have moved by exactly −gap, earlier ones unchanged, with the same ids, durations and
     text. Otherwise it aborts. The plan also aborts if any removal overlaps a caption.
   - **Logo pins the project duration:** the full-length overlay doesn't ripple (§F.9), so the
     project duration can't drop. The "removed exactly the gap" check uses the **main track end**
     instead. The logo end is trimmed afterwards.
   - **Layout:** `clip_y` 860, empty focus point (1600,960) below the tracks. Fit geometry stays
     x0 230 / span 1297; Shift+Z fits the project duration, which the logo holds at 34.233
     throughout.
   - **Sound modal:** after every key or click it looks for the (760,421) 400×188 window and aborts
     if found, rather than re-sending keys that may already have been processed. A re-run
     recomputes the gaps, and completed ones drop out.
   - `--max-cuts N` runs only the N latest removals: **first run `--max-cuts 1`** to prove caption
     ripple under W before the rest. `save_timeout` is 20 s.
4. **Fit geometry check** (empty click (1600,960), Shift+Z; `30-fit-34s.png`; draft unchanged):
   - ruler 00:00 x≈230, 00:05 x≈419, 00:10 x≈609, 00:30 x≈1369 (**≈38.0 px/s**); clips and the
     logo end at x≈1529, matching the runner's `x_of` (232 + t × 1297 / 34.233)
   - rows: logo y≈715–775, captions y≈780–808, **main y≈815–905** (clip_y 860); (1600,960) is empty
5. **Runner dry run** (`tighten-cap17-dryrun.txt`):
   - imports OK; 4 main segments, main end = project = 34.233 s, 17 captions
   - the same 6 removals as §G.1 and **no caption overlaps**; expected main end 34.233 → 31.367 s
6. **First cut alone** `tighten_cap17.py --max-cuts 1` (exit 0, `tighten-cap17-run1.txt`):
   - **Split at 32.800:** measure#0 landed 32.933 (−4 frames), measure#1 exact.
   - **Placement at 32.267:** measure#0 landed **28.167**. The ruler click snapped to a caption
     start 4 s away, and 123 arrow presses corrected it; measure#1 exact. No sound modal.
   - **W:**
     - main end **34.233 → 33.700** (−0.533, exact)
     - the join resumes at src **296.867** (expected 296.867)
     - **captions rippled ok=True**: all 17 kept id, text and duration, and those after the cut
       moved by exactly −0.533 s
   - **W on the main track ripples the caption track too** (like Delete in §F.9). The project
     duration stays 34.233 s, pinned by the logo.
   - 5 main segments.
7. **Remaining 5 cuts** `tighten_cap17.py` (exit 0, `tighten-cap17-run2.txt`): the done gap dropped
   out of the recomputed plan.

   | Remove | Main end after | Join resumes src | Placement |
   |---|---|---|---|
   | 27.633 → 28.033 | 33.300 | 292.100 ✓ | split 2 measures; start **anchor-and-step** (segment 24.167 → 28.033 too narrow), exact first try |
   | 21.667 → 22.100 | 32.867 | 284.867 ✓ | 2 + 2 measures (first landings snapped 76 / 121 frames away onto caption edges) |
   | 17.133 → 17.500 | 32.500 | 280.267 ✓ | 2 + 2 measures |
   | 12.200 → 12.800 | 31.900 | 275.567 ✓ | split 2; start anchor-and-step (9.400 → 12.800), 2 measures |
   | 6.533 → 7.067 | **31.367** | 269.033 ✓ | split 2; start anchor-and-step (1.933 → 7.067), 2 measures |

   - **Every W:** main-end delta exact, join source exact, **captions rippled ok**. No modal.
   - **FINAL: 10 main segments, main end 31.367 s, 17 captions**. The project is still 34.233 s
     because of the logo.
   - At fit zoom the first ruler landing often snaps to a caption edge several seconds away.
     The measuring loop absorbs it with 60–126 arrow presses.
8. **Independent check** `caption_shift_check17.py draft-05-trimmed.json draft-06-gaps.json`
   (`gaps-caption-check.txt`) → **RESULT: CAPTIONS AND LOGO OK**:
   - all **17 captions** kept id, text, duration and transform
   - each moved by exactly the removed total before it: 0 for the first 4, −0.533 from 7.200,
     −1.133 from 12.933, −1.500 from 17.633, −1.933 from 22.233, −2.333 from 28.167, −2.867 for the
     last. Rounding ≤ 1 ms.
   - the logo is still one segment 0 → 34.233 (to trim)
9. **Content after the pass** (`gaps-content.txt`, snapshot `draft-06-gaps.json`):
   - **10 main segments**, main end 31.367
   - punch-ins carried into the W pieces: **segs 1–2 punched** (1.933 → 8.867, split by the
     6.533 cut), 3–6 wide, **segs 7–9 punched** (22.233 → 31.367)
   - The gap cuts inside punched clips now join two punched pieces (6.533, 25.700, 29.933), so
     those joins have **no framing change**. Handled in the punch-in stage.
   - captions 0.133 → 31.000, all y −0.73; no keyframes anywhere
10. **Trim the logo end to the new main end.**
    - Before (`31-after-gaps.png`, fit unchanged at 34.233 s): main clips end x≈1419; the logo
      spans x≈229–1528 at y≈715–775; a punched piece was left selected by the runner (inspector
      110 % / Y −60).
    - `drag 1527 744 1420 744 --steps 50 --hold 0.4`, grabbing 1 px inside the logo's right edge
      and releasing at the main end x (232 + 31.367 × 37.89). The draft saved on the first 0.5 s
      poll (`logo-trim-check.txt`).
    - **logo 0 → 31.367 exactly** (it snapped to the main end), scale 0.12, tf (0.83854, 0.80926)
      unchanged
    - **project duration 31.367 s**, 3 tracks, 28 segments (10 main + 17 captions + 1 logo); nothing
      after 31.367
    - Snapshot `draft-07-logo-trimmed.json`.
    - **Stage G result: 34.233 → 31.367 s (−2.866 s), 6 gaps removed, captions and punch-ins
      intact.**
11. **Undo/redo gate on the logo trim** (empty click (1600,960)):
    - Ctrl+Z → 34.233 s (logo straddling 31.367 again)
    - Ctrl+Shift+Z → **31.367 s, byte-identical to `draft-07-logo-trimmed.json`**
    - each step saved within 0.5 s; no modal
    - **Observed** (`32-after-logo-trim.png`): the logo stays selected (inspector 12 %,
      1610 / 874) and spans x≈229–1421 with the main clips. The player reads 00:00:06:16 /
      00:00:31:11; the fit view is still the 34.233 s scale.

### H. Canvas 9:16 and Auto reframe (rung 12 route, 2026-09-15)
- Plan:
  1. Player **Ratio** (≈1371,541) ▸ **9:16** (≈1427,810). Verify `canvas_config` 9:16 1080×1920.
  2. **Lock the caption and logo tracks** so a clip click selects only the clip (rung 12 §G.6).
  3. Per main clip: Video ▸ Basic, scroll to **Auto reframe** (Pro), tick it, set Aspect ratio
     **9:16**, then **Apply** (rung 12 §G.7–H). Verify `smart_crops`.
- ⚠ There are now **10 main clips** (rung 12 had one). Do the first by hand to measure this
  layout, then decide how to cover the rest.
1. **Ratio menu** (empty click (1600,960), then Ratio (1371,541); `33-ratio-menu.png`; draft
   unchanged):
   - It drops down from ≈(1372,545) over the timeline's right side.
   - Rows: **Original ✓** (1438,563), Custom (1438,598), 16:9 (1427,634), 4:3, 2.35:1, 2:1, 1.85:1,
     **9:16 (1427,810)**, 3:4, 5.8-inch, 1:1 (1422,915).
   - Identical to rung 12 §F.1.
2. **Click 9:16** (1427,810). The draft saved on the first 0.5 s poll (snapshot `draft-08-916.json`,
   `diff-916.txt` vs `draft-07`):
   - `canvas_config` **original 1920×1080 → 9:16 1080×1920**
   - plus `config.subtitle_keywords_config`: `is_change_font_size` False → True and its sample
     style size 10.5 → 16. That's CapCut's keyword-highlight preset rescaling for the new ratio;
     the caption segments and texts are unchanged.
   - Duration 31.367 s, 3 tracks, 28 segments unchanged; clip transforms unchanged (the ratio change
     doesn't reframe). No modal.
   - **Observed** (`34-after-916.png`):
     - the player shows a **portrait canvas** x≈916–1131, y≈99–482, with the 16:9 video
       **letterboxed** in the middle (y≈235–368) and black bars above and below
     - the logo's normalised transform now puts it tiny at the canvas top-right (player
       ≈1110,133), outside the video band
     - the Ratio button reads **9:16** (≈1373,541); Details ▸ Aspect ratio **9:16**
     - the **TikTok icon** with a cyan dot appears at ≈(1227,541) (rung 12); not clicked
     - track headers unchanged: logo lock ≈(59,744), captions lock ≈(59,794), main ≈(59,859)
3. **Lock the caption and logo tracks** (rung 12 §G.6 lesson: with auto captions, a clip click can
   pull in captions): click the lock icons at (59,794) and (59,744), gated on the draft after each.
   - Each click saved on the first 0.5 s poll: **caption track `attribute` 0 → 4**, then **logo
     track 0 → 4**. The main track stays 0.
   - Diff `draft-08-916.json` → `draft-09-locked.json` without the per-segment `track_attribute`
     lines: **only `.tracks[1].attribute` and `.tracks[2].attribute`** (`diff-locks-nonattr.txt`).
   - No modal. Unlock both before the caption, title and logo work.
   - **Observed** (`35-headers-locked.png`): the logo and caption rows show **cyan lock icons and
     diagonal hatching**; the main row's lock stays white.
4. **Select one main clip:** click **seg 4** (11.667 → 16.000, unpunched) at **(756,860)**.
   - `36-tracks-seg4.png`: **only that clip** has a white border (screen x≈670–838); the locked
     captions and logo are not selected.
   - `36-inspector-seg4.png`: the single-clip **Video · Audio · Speed · Animation · Adjust · A…›**
     inspector, Basic ▸ Scale 100 %, X 0 / Y 0, Blend ✓.
   - The draft is unchanged.
5. **Video ▸ Basic scrolled** (`scroll 1480 450 -4` × 3; `36-inspector-seg4-scroll3.png`):
   - top row **Auto reframe ◆ ▾**, checkbox **≈(1468,173)**, ▾ **≈(1603,173)**, the same spot as
     rung 12 §G.7
   - below it Remove flickers ◆, AI movement ◆, Camera tracking ◆, Motion blur ⓘ ◆, and **Canvas ✓
     ▾ [Apply to all]** at the bottom
   - **Auto reframe has no "Apply to all"**
6. **Expand ▾ (1603,173), then tick (1468,173)** (Pro; standing rule "run; stop if a cost
   appears"):
   - Expanding changed nothing in the draft (`37-reframe-expanded.png`).
   - The tick saved on the first 0.5 s poll. Diff `draft-09-locked` → `draft-10-reframe-ticked`
     (`diff-reframe-tick.txt`) is exactly **`.materials.videos[4].check_flag` 62978047 → 63043327**:
     the same +0xFF00 feature bit as rung 12 §G.9, and only on seg 4's material.
   - **Windows after the tick:** MainWindow, the known player overlay (621,99), a tooltip, and a new
     `Qt622QWindowToolSaveBits` **(860,576)–(1058,730)** (toast; see the screenshot). **No cost,
     credit or upsell dialog.**
   - **Observed** (`37-reframe-ticked.png`, `37-full-after-tick.png`):
     - The new window is the **"Auto reframe applied"** toast over the timeline (≈958,689). The
       player header also reads **"✓ Auto reframe applied ▾"**.
     - The expanded fields went from greyed to active: **Aspect ratio Original ▾ ≈(1751,221)**,
       **Image stabilization Default ▾ ≈(1751,268)**, **Camera moving speed Default ▾
       ≈(1751,316)**, **Apply ≈(1844,395)** now enabled.
     - The player is still letterboxed: Original ratio means no reframe yet, as in rung 12.
     - Seg 4 stays selected; the locked rows stay hatched; "Auto saved: 17:48:50".
7. **Aspect ratio dropdown** (click (1751,221); `38-aspect-dropdown.png`; draft unchanged):
   - An inline popup under the field with rows **Original ✓** (1653,261), 16:9 (1667,300), 4:3,
     2.35:1, 2:1, 1.85:1 (1672,437), **9:16 (1667,474)**, 3:4 (1664,509), 5.8-inch, 1:1 (1662,578).
   - Separators after Original and after 1.85:1. Same set as rung 12 §G.10.
   - Pick in the next command without a `cc.py focus` call in between (rung 12 pitfall).
8. **Pick 9:16** (1667,474), then capture at +1.2 s and +8 s (`39-aspect-916-1s.png`,
   `39-aspect-916-8s.png`, `39-full-8s.png`):
   - **Draft unchanged** (still `draft-10`): the analysis doesn't write the draft until Apply,
     as in rung 12.
   - **Analysis cache** in the project's `smart_crop/2EE2762D-…/`:
     - `0/2_1/vid_timerange` (56 B) was written at **17:48:50**, the tick
     - `1/2_1/{config, totalCache 1 056 B, vid_timerange, e29bed…_272566666_10333333}` was written
       at **17:50:33**, the 9:16 pick
     - The analysed source range **272.567 s + 10.333 s** covers seg 4 (source ≈275.6 → 279.9)
       with ≈3 s padding either side, as in rung 12 §H.5.
   - Windows at +8 s: MainWindow, the player overlay and a tooltip only. **No cost, credit or
     upsell dialog**; the tick toast has gone.
   - **Panel** at +1.2 s and +8 s: Aspect ratio **9:16**, Image stabilization Default, Camera moving
     speed Default, **Apply enabled**. No "Processing N%" was visible even at +1.2 s; analysing
     4.3 s of clip is near-instant.
   - **Player** (`39-full-8s.png`): a **cyan 9:16 preview box** (player x≈997–1065, y≈231–350)
     centred on the speaker inside the still-letterboxed frame.
   - The **playhead moved to 00:00:15:29**, inside seg 4, with no input sent. It is the preview
     scrub rung 12 §G.12 also saw.
9. **Apply** (1844,395). The draft saved on the first 0.5 s poll (snapshot
   `draft-11-reframe-seg4.json`, `diff-reframe-apply.txt` vs `draft-10`):
   - **new `materials.smart_crops[0]`** = `{type: smart_crop, crop_ratio: "9:16", stability: 2,
     track_speed: 1, cache_path: "##_draftpath_placeholder_…_##/smart_crop/2EE2762D-…/1/2_1",
     apply_source: 1}`
   - **seg 4 `extra_material_refs`** gains its id, inserted at index 7 (the later refs shift by one)
   - nothing else changed: no other segment, and no clip scale or transform
   - windows: MainWindow, player overlay, tooltip. **No cost, credit or upsell dialog.**
   - This matches rung 12 §H.3 exactly. **Auto reframe is per clip; 9 main clips remain.**
   - **Observed after Apply** (`40-after-apply.png`, `40-panel-after-apply.png`, playhead 00:00:15:29
     inside seg 4):
     - **The player fills the whole 9:16 canvas with the reframed shot**: the speaker is centred,
       head in the upper third, the mic and "MELON AUSTRALIA" shirt visible, no black bars
     - the logo shows tiny at the canvas top-right (≈1112,135); it's re-placed later
     - the panel stays expanded: Auto reframe ✓, 9:16 / Default / Default, **Apply greyed**
       (committed)
     - seg 4 stays selected; "Auto saved: 17:51:39"
10. **Second clip probe:** click **seg 5** (16.000 → 20.167) at **(917,860)** (`41-seg5-*.png`; draft
    unchanged):
    - only seg 5 is selected (x≈835–996); the locked captions and logo are not
    - **the inspector keeps its scroll position and the expanded Auto reframe section**, now for
      seg 5: **unticked**, fields greyed at Original / Default / Default, Apply greyed
    - the player still shows seg 4's reframed frame (the playhead 00:00:15:29 is in seg 4)
    - **So every remaining clip uses the same coordinates:** tick (1468,173) → dropdown (1751,221) →
      9:16 (1667,474) → wait → Apply (1844,395).
11. **Runner `cap17/reframe_cap17.py`** loops over the clips without a `smart_crops` ref, gating
    each step on the draft:
    - **selecting** changes nothing
    - the **tick** changes only that clip's video material `check_flag` (from the unticked
      62978047)
    - the **9:16 pick** leaves tracks and materials unchanged; it waits ≤ 15 s for new files under
      `smart_crop/`
    - **Apply** adds exactly one `smart_crops` with crop_ratio 9:16, referenced by that clip only,
      and changes nothing else in tracks or materials
    - Preconditions checked: canvas 9:16, non-main tracks locked (attribute 4).
    - It aborts on a missing save, the sound modal or any window other than the main window, player
      overlay, tooltips and the bottom toast row.
    - Click x = 230 + centre × 37.967 (the current 34.233 s fit view: 00:00 x≈230, 00:30 x≈1369).
12. **Runner dry run** (`reframe-cap17-dryrun.txt`):
    - 10 main clips; **seg 4 REFRAMED** (flag 63043327); **9 to do**, all with the unticked flag
      62978047
    - locks: track 1 text 4, track 2 video 4
    - click x: seg 0 267, 1 391, 2 522, 3 620, 5 917 (the same point as the manual probe), 6 1035,
      7 1140, 8 1286, 9 1394
    - First real run: `--max 1` (seg 0, the narrowest at ≈73 px).
13. **`reframe_cap17.py --max 1`** (exit 0, `reframe-cap17-run1.txt`): **seg 0** at x 267 passed
    every gate:
    - tick: check_flag 62978047 → 63043327 on this clip only
    - 9:16 pick: 4 new cache files, draft unchanged
    - Apply: +1 smart_crop 9:16 (stability 2, track_speed 1) referenced by seg 0 only
    - **2/10 reframed.** No unexpected window.
14. **`reframe_cap17.py`** for the rest (exit 0, `reframe-cap17-run2.txt`): segs **1, 2, 3, 5, 6, 7,
    8, 9** in order, every one passing all three gates:
    - tick: only its own `check_flag`
    - 9:16 pick: 4 new cache files each, draft unchanged
    - Apply: exactly one new 9:16 smart_crop referenced by it alone
    - **FINAL: 10/10 main clips reframed**, smart_crops total 10. No modal, no cost, credit or upsell
      window.
    - Auto reframe on 10 clips took about 3 minutes of scripted input.
15. **Scope of the whole reframe** (snapshot `draft-12-reframed.json`; `diff-reframe-all.txt` vs
    `draft-09-locked.json`):
    - **110 diff lines, 0 outside `check_flag` / `smart_crops` / `extra_material_refs`**
    - duration 31.367 s, canvas 9:16 1080×1920, 3 tracks, 28 segments; captions and logo still
      locked (attribute 4)
    - No timing, transform, caption or logo change.
16. **Player frames after the reframe** (ruler clicks x 391 / 620 / 1140; `frames-916/`; no modal):

    | Timecode | Clip | Observed |
    |---|---|---|
    | 00:00:04:10 | seg 1, punched 110 % / Y −60 | **fills the 9:16 canvas**; speaker slightly larger, head in the upper third, no border; no caption at that instant (gap) |
    | 00:00:10:09 | seg 3, wide | fills the canvas, speaker centred; caption **tiny** at the bottom |
    | 00:00:23:29 | seg 7, punched | fills the canvas, visibly tighter than seg 3; caption tiny |

    - **Auto reframe: good on every clip checked**, and a punch-in on top of the reframe exposes no
      border.
    - **Still to fix:** captions are unreadably small in 9:16 (rung 12 §H.6); the logo is tiny at
      the top-right.

### I. Punch-ins for the short (rung 6 rules, 2026-09-15)
1. **Pattern after the gap pass.** Clip lengths (s): 1.933, 4.600, 2.333, 2.800, 4.333, 4.167,
   2.067, 3.467, 4.233, 1.433.
   - Current framing is P at 1, 2, 7, 8, 9 (carried from rung 16 and split by the gap cuts), W
     elsewhere. **5 of 9 joins have no framing change** (6.533, 11.667, 16.000, 25.700, 29.933).
   - **Target:** alternate, punching only clips ≥ 2.5 s (rung 6/16). Punch **1, 3, 5, 7**; wide
     **0, 2, 4, 6, 8, 9** (seg 9 is 1.433 s, too short to punch). That gives **8 of 9 joins with a
     framing change**; only 29.933 (seg 8 W | seg 9 W) has none.
   - **Edits:** seg 2 P→W, **seg 3 W→P**, **seg 5 W→P**, seg 8 P→W, seg 9 P→W. Values are rung 16's
     110 % / Y −60 (frames above show that it keeps the head in the upper third after the
     reframe).
2. **Inspector back to the top** (`scroll 1480 300 5` × 4; `42-inspector-top.png`; draft
   unchanged):
   - Video ▸ Basic ▸ Transform: **Scale box ≈(1792,257)**, **Position Y ≈(1788,352)**, the same
     places as rung 16
   - the selected clip was seg 9 (punched), and it reads **Scale 110 % / X 0 / Y −107**
3. ⚠ **Typed Y in 9:16:** the stored `transform.y` −0.05556 (typed −60 on the 1080-high canvas in
   rung 16) displays as **−107 = −0.05556 × 1920**.
   - Typed Y always scales with the current canvas height (rung 12 §I.12), so the same punch is
     typed **110 / −107** here.
   - −107 stores −0.05573, 0.3 canvas px from the carried-over punches, within tolerance.
4. **Runner `cap17/punch_cap17.py`** (imports `reframe_cap17` for draft I/O, the window guard and
   foreground):
   - Per clip whose framing differs from the plan: click the body, then Scale box → Ctrl+A, type,
     Enter.
   - After each field it checks that **only that clip's** values changed, to the target (P = 1.1 ±
     0.001 / −0.05556 ± 0.0004; W = 1.0 / 0).
   - Preconditions: 9:16 canvas, locks. It uses the current fit view without Shift+Z.
5. **Probe:** click seg 1 (391,860) (`43-seg1-*.png`; draft unchanged).
   - Only seg 1 is selected (x≈300–478).
   - The inspector stays at the top and reads **110 % / X 0 / Y −107**, so the box positions hold
     across selections.
6. **Runner dry run** (`punch-cap17-dryrun.txt`):
   - **EDIT** seg 2 (P→W, x 522), **3** (W→P, x 620), **5** (W→P, x 917), 8 (P→W, x 1286), 9 (P→W,
     x 1394)
   - **ok** 0, 1, 4, 6, 7
   - 5 clips, 10 field edits.
7. **`punch_cap17.py`** (exit 0, `punch-cap17-run.txt`); every field edit changed **only** its
   clip:

   | Seg | Scale | Position Y | Result |
   |---|---|---|---|
   | 2 | 100 → 1.0 (ty still −0.05556) | 0 → ty 0 | wide |
   | 3 | 110 → 1.1 | −107 → **ty −0.05573** | punched |
   | 5 | 110 → 1.1 | −107 → ty −0.05573 | punched |
   | 8 | 100 → 1.0 | 0 → ty 0 | wide |
   | 9 | 100 → 1.0 | 0 → ty 0 | wide |

   - **FINAL punched [1, 3, 5, 7] = plan** (1 and 7 keep −0.05556 from rung 16; 3 and 5 at
     −0.05573, a 0.3 px difference).
   - Framing now alternates W P W P W P W P W W over the 10 clips. No modal.
8. **Scope and gate** (snapshot `draft-13-punched.json`):
   - diff vs `draft-12-reframed.json` (`diff-punch17.txt`) is **15 lines, all `.clip.scale.x/y` and
     `.clip.transform.y` on segs 2, 3, 5, 8, 9**; nothing else changed
   - **undo/redo gate** on the last field (seg 9 Position Y), after an empty timeline click
     (1600,960):
     - Ctrl+Z → seg 9 ty **−0.05556** (only the Y edit reverted; scale stays 1.0)
     - Ctrl+Shift+Z → **0.0**, byte-identical to `draft-13`
     - each saved within 0.5 s
   - Frames of the new seg 3 punch and the new seg 8 wide: `frames-916/seg3-now-punched-*`,
     `seg8-now-wide-*`.
   - **00:00:10:09 (seg 3, now punched):** visibly tighter than the wide frame at the same
     timecode in §H.16. The head stays in the upper third and no border is exposed.
   - **00:00:27:27 (seg 8, now wide):** the wider framing, speaker centred.
   - The alternation reads as deliberate jump cuts on top of the reframe.

### J. Captions, hook title and logo for 9:16 (2026-09-15)
1. **Unlock the caption and logo tracks** (click (59,794), then (59,744)):
   - each saved on the first 0.5 s poll: **track 1 and track 2 `attribute` 4 → 0**
   - non-attribute diff vs `draft-13` (`diff-unlock-nonattr.txt`): only those two lines
   - snapshot `draft-14-unlocked.json`; no modal
   - `44-headers-unlocked.png`: white lock icons, no hatching on the logo and caption rows.
2. **Select one caption:** click the first caption block «الحتة…» at **(262,794)** with the Select
   tool (plain arrow, `45-tool-icon.png`). Draft unchanged.
   - `45-caption-tracks.png`: **only that caption** has a white border; no clips or other captions
     are selected. (Rung 12's select-everything came from Select rightward mode, not linkage.)
   - `45-caption-inspector.png`: tabs **Captions · Text · Animation · Tracking · Text to sp…›**;
     Text ▸ **Basic** / Templates / Effects.
     - **Apply to all main captions ✓** ≈(1470,167)
     - text box «الحتة اللي احنا هنافس بيها»
     - Font **Staatliches-Regular**; **Font size 11** box **≈(1838,395)** (the stored 10.5 shows as
       11, rung 12)
     - Pattern B/U/I; Case TT/tt/Tt; Save as preset
3. **Hook title route to reuse** (rung 16 §L): Text tab (163,70) ▸ Text template ▾ (85,251) ▸ search
   «عربي» (370,127) ▸ template #3 «يوم عادي، حياة عادية» row 2 middle (357,340); click the tile body
   to preview, then **+** (396,378) at a timecode-gated playhead. Replace the placeholder text via
   the clipboard gate, then measure scale and position from frames.
4. **Caption font size 22** (rung 12 §I.10), with Apply to all main captions ✓:
   - Font size box (1838,395), then `ctrl+a`, `type "22"`, Enter. The draft saved on the first
     0.5 s poll (snapshot `draft-15-font22.json`, `diff-font22.txt` vs `draft-14`).
   - **font_size 22.0 on all 17** text materials. Diff 68 lines:
     - 34 on `texts[*].font_size` / `content` (the style size), 17 × 2
     - 34 on **`text_templates[*]…attach_info.original_size_width/height`**, 17 × 2: the
       template's measured text box, re-laid-out for the bigger font (e.g. 452 × 163 → 787 × 342)
   - Transforms, timings, template ids and the video and logo tracks are unchanged.
   - **Scope confirmed:** 0 diff lines outside those two groups.
   - The inspector reads **22** (`46-caption-font22-inspector.png`).
   - Template box heights after re-layout: **342 ×8, 312 ×2, 435 ×6, 529 ×1**. The taller boxes
     suggest multi-line wraps at size 22; checked in frames before moving the captions.
5. **Frames at size 22** (ruler clicks x 777 / 587; `frames-916/cap-*`; draft unchanged):

   | Timecode | Caption | Observed |
   |---|---|---|
   | 00:00:14:13 | long, «…قالتله اعملي تطبيق شرعي للعقد ده اعملي تطبيق شرعي» (the template shows a chunk) | ⚠ **wraps to 2 lines and splits a word**: «للعقد ده اعملي تطبيق شر» / «عي». Box ≈82 % down, nearly full canvas width |
   | 00:00:09:13 | short «بمعنى» | one line, readable, ≈86 % down |

   - The template **wraps by character, not by word**, so any caption wider than its max box
     (≈787 px) breaks mid-word. The 7 tall boxes (435 / 529) are the wrapped captions.
   - Both frames sit **too low** for Shorts/Reels/TikTok (bottom ≈20 % is platform UI).
   - **Fix:** a font size small enough that no box wraps (every height back to one line), then
     raise with Position Y. Trying **18**.
6. **Size 18** (same box, snapshot `draft-16-font18.json`; diff 68 lines, 0 outside the text sizes
   and template box sizes):
   - template heights **280 ×10, 255 ×2** (one line) and **356 ×5** (two lines, the same 1.27×
     ratio as 342 → 435 at size 22)
   - max width 754
   - **5 captions still wrap.** Trying **16** (≈4 % of frame height, still in the usual range for
     vertical captions).
7. **Size 16** (snapshot `draft-17-font16.json`; diff 68 lines, 0 outside the text sizes and
   template box sizes):
   - heights **249 ×13, 227 ×2** (one line), **317 ×2** (two lines)
   - widths 214 … 736
   - **2 captions still wrap.** Trying **15**, with `caption_boxes17.py` to name the wrapped
     captions.
8. **Size 15** (snapshot `draft-18-font15.json`; diff 68 lines, 0 outside the text sizes and
   template box sizes):
   - heights **233 ×13, 212 ×2, 297 ×2**: the **same 2 captions still wrap**
   - Shrinking further gives little and costs legibility.
   - **Decision:** go back to **16** (≈4 % of frame height) and fix the 2 long captions
     individually, so their wrap falls at a word boundary.
9. **Back to 16:** typed `16` in the same box. Saved on the first poll (snapshot
   `draft-19-font16-again.json`).
   - **diff vs `draft-17-font16.json`: 0 lines**, so the size edits are fully reversible by value.
   - heights 249 ×13, 227 ×2, 317 ×2
   - `caption_boxes17.py` (`caption-boxes-16.txt`) flags the 2 wrapped captions as the two longest:
     - **12.900 s** (735 × 317): «قالتله اعملي تطبيق شرعي للعقد ده اعملي تطبيق شرعي»
     - **22.333 s** (736 × 317): «التراجت اودينس بتوعنا ما يقدروش يلاقوها غير عندنا»
   - Text matched from the transcript; the helper's text lookup came back empty for templated
     captions.
   - The size-22 frame showed the template **pages** a long caption into chunks over time, so the
     box height may overstate what renders. Rendered frames inside both captions decide whether
     a fix is needed.
10. **Rendered at size 16** (ruler clicks x 735 / 807 / 1096 / 1175; `frames-916/size16-*`; draft
    unchanged):

    | Timecode | Caption | Page on screen |
    |---|---|---|
    | 00:00:13:10 | 12.900 | «قالتله اعملي تطبيق شرعي», **one line**, word highlight on «اعملي» |
    | 00:00:15:06 | 12.900 | «للعقد ده اعملي تطبيق شرعي», one line |
    | 00:00:22:24 | 22.333 | «التراجت اودينس بتوعنا ما», one line, highlight on «التراجت» |
    | 00:00:24:27 | 22.333 | «يقدروش يلاقوها غير عندنا», one line |

    - **No page wraps or splits a word at size 16.** The two-line `original_size_height` measures
      the whole caption text, not the rendered page, so it over-reports.
    - **Rule:** judge caption wrapping from rendered frames. The box height is only a hint.
    - Each page spans about half the canvas width, readable. **Keep size 16 for all captions**;
      no per-caption edits.
    - Still too low (≈86 % down). Next: Transform ▸ Position Y.
11. **Caption Text ▸ Basic, scrolled** (`scroll 1600 450 -3` per step; `48-cap-inspector-s0..s4.png`;
    the first caption stays selected (`48-cap-tracks.png`); draft unchanged). The text box and
    **Apply to all main captions ✓** stay pinned at the top.

    | Step | Visible |
    |---|---|
    | s0 | Font Staatliches-Regular, **Font size 16**, Pattern, Case |
    | s1 (−3) | **Alignment** (6 buttons), **Preset style** tiles (⃠ selected, white/outlined/yellow/red …) |
    | s2 (−6) | Scale 100 %, Uniform scale ✓, **Position X 0 / Y −1402** (Y box **≈(1758,367)**), Plane rotation 0.00°, alignment row |
    | s3 (−9) | Stroke (off), **Background ✓** with 2 style tiles |
    | s4 (−12) | Background sliders: Rounded rectangle 0 %, Height 100 %, Width 100 %, **Y-offset 50 %**, X-offset |

    - **Y −1402 = −0.73 × 1920**, as rung 12 §I.12 predicted. Target **−768** (`transform.y` −0.4,
      ≈70 % down), rung 12's approved value.
12. **Raise the captions:** `scroll 1600 450 3` × 2 back to s2 (`49-cap-inspector-back-s2.png`
    confirms Position Y at (1758,367)). Then click Y, `ctrl+a`, `type "-768"`, Enter.
    - The draft saved on the first 0.5 s poll (snapshot `draft-20-caption-y.json`,
      `diff-caption-y.txt`).
    - **all 17 captions `clip.transform` (0, −0.4)**
    - **diff exactly 17 lines, all `.tracks[1].segments[*].clip.transform.y`**; nothing else
    - no modal; Apply to all main captions covered every caption in one edit
    - The inspector reads **Y −768** (`50-cap-inspector-y768.png`).
    - **Frames** (`frames-916/y768-*`):
      - **00:00:09:13** «بمعنى» at ≈70 % down (player y≈272 of 390)
      - **00:00:13:10** «قالتله اعملي تطبيق شرعي» at ≈72 %
      - Both clear the bottom ≈20 % platform-UI zone and are readable.
    - ⚠ **Trade-off:** at 70 % the captions sit over the shirt's **"MELON AUSTRALIA" print**
      (≈62–82 % of the height). The template's non-highlighted words are white with a shadow, so
      they read less crisply over the black lettering than the boxed word.
    - No clean band exists nearby: above it the hand and mic come into frame; below it is the
      platform UI.
    - **Kept rung 12's approved −768**; flagged for the user's review of the export.
13. **Frames for the hook title** (ruler clicks x 287 / 325; `frames-916/hook-*`; draft unchanged):
    - **00:00:01:16** (seg 0, wide): the first caption is still selected (selection box and handles
      over the shirt). Head top at player-crop y≈30 (≈8 % down), eyes ≈24 %.
    - **00:00:02:16** (seg 1, punched): head top ≈6 %, face larger; caption «لازم» at ≈70 %.
    - **No large clear area in 9:16:**
      - the wall strips left and right of the head are only ≈15 % of the width
      - the chest holds the mic, the hand and the shirt print
    - **Candidate:** a one-line title in the **top band (≈8–15 % down)**, over the wall and hair
      line, above the eyes. Measured after adding the template (rung 16 §L yellow-bbox method).
    - Canvas mapping for measurement: the player canvas is screen x 916–1131, y 99–482, so
      **5.013 canvas px per player px**.
    - **Deselect before measuring** (selection boxes draw over frames).
14. **Playhead to the start and open Text** (empty click (1600,960) deselects the caption, **Home**,
    Text tab (163,70); `51-tc-home.png`, `51-text-tab.png`; draft unchanged):
    - timecode crop (615,528)–(790,555) reads **00:00:00:00 / 00:00:31:11**. This is the
      tolerant-diff gate reference before **+** (rung 16 §L.8: pass only when pixels > 15 == 0).
    - left list: Add text (85,131), Yours ▾, Text effects ▾, **Text template ▾ (85,251)**, Auto
      captions, Local captions, same as rung 16; the main area shows a "Default text" card
    - the player shows seg 0 (wide) at 0:00 with no selection box
15. **Text template ▾ (85,251)** (`52-text-template-open.png`):
    - categories Trending / Whimsical / KATSEYE / Pixel Bead / Classic / NEW
    - search box "Search for text templates" ≈(370,127)
    - a 3-column Trending grid (Chapter End, FINAL, BAM!, CREATIVE, Get Ready…, ติดตาม, KEEP GOING,
      Últimas noticias, NĂNG ĐỘNG), several with Pro diamonds
16. **Search «عربي»** (click (370,127), `type "عربي"`, Enter, wait 7 s; `52-arabic-search.png`): the same
    grid as rung 16 §L.5.
    - Row 1: «الفرح في البساطة», "It's simple", calligraphy.
    - Row 2: "Một ngày đơn giản", **«يوم عادي، حياة عادية» (template #3, yellow bold) ≈(357,340)
      with ⬇ ≈(395,378)**, "A simple life".
    - Row 3: «الحياة تستمر», «حياة صغيرة», «وبشر الصابرين».
    - The playhead is still 00:00:00:00 (`52-tc.png`); draft unchanged.
17. **Preview template #3** (click the tile body (342,325), wait 5 s):
    - `53-tile3-icons.png`: cyan tile border; ⬇ became a **cyan + ≈(396,378)** with ☆ beside it
    - `53-player-header.png`: **"Previewing — Text template ⓘ"**
    - `53-tc.png`: the template clock **00:00:00:00 / 00:00:03:0…**
    - the preview frame at 0:00 shows no text yet (type-on starts empty)
    - draft unchanged; no modal
    - As in rungs 9 and 16, a click previews and only **+** adds.
18. **Timecode-gated add at 0.0 s** (one command):
    - Click empty (1600,960) to leave the preview, then **Home**.
    - **Gate:** `img_diff.py 51-tc-home.png 54-tc-gate.png` → **pixels > 15: 0 of 4725**, passed.
      In preview mode the crop would show the template's 00:00:03 total instead of 00:00:31:11, so
      this gate also proves the preview was left.
    - Hover the tile (357,340), then click **+ (396,378)**. The draft saved on the first 0.5 s poll
      (snapshot `draft-21-title-added.json`).
    - **New track 3 `text` flag 0** with one segment:
      - **start 0.0, duration 3.0**
      - template **"Arabic An ordinary day, an ordinary life" / 7659823758919699730**, rung 9's
        template
      - scale 1.0, transform (0, 0)
    - Tracks 0–2 are unchanged in count (10 / 17 / 1); duration 31.367 s; no modal.
    - **Scope** (`diff-title-added.txt`, 301 lines): **0 lines on tracks 0–2**. The rest are the
      new track's fields and segment, plus added `texts`, `text_templates` and
      `material_animations`.
    - **Observed** (`54-title-added.png`):
      - A **new TT row at the top, y≈727**, holds the title block (x≈229–343, 0–3 s, selected). The
        other rows shift down: **logo y≈777, captions y≈827, main y≈891** (use these for later
        clicks).
      - Inspector **Text · Tracking · Text to speech · AI avatars◆** ▸ Basic / Templates / Effects:
        - **"The 1 paragraph"** box with the placeholder «يوم عادي، / حياة عادية» right-aligned
          at ≈(1815,222), ▾ (1878,227)
        - Transform: **Scale 100 % ≈(1790,349)**, **Position X ≈(1647,444) / Y ≈(1768,444)**,
          Plane rotation
        - the same layout as rung 16 §L.9
      - Player: dashed title guides at player ≈(940–1108, 225–355), over the chest; no text at
        0:00 (type-on).
19. **Title text:** `cap17/title_text17.py`, the rung-16 clipboard gate:
    - The draft title text must be the placeholder.
    - Click (1815,222), Ctrl+A, Ctrl+C; the clipboard must equal the placeholder, else abort with
      nothing typed.
    - Type «ليه لازم نتميز عن جيميناي؟».
    - Then verify: texts == [new]; start, duration and clip unchanged; all other tracks unchanged.
    - **Dry run** (`title-text17-dryrun.txt`): title start 0.000, dur 3.000, texts
      `['يوم عادي،\nحياة عادية']`, the placeholder, so the draft-side precondition holds.
    - **Run** (exit 0, `title-text17-run.txt`, snapshot `draft-22-title-text.json`):
      - **Gate:** the clipboard after Ctrl+A / Ctrl+C was exactly `'يوم عادي،\nحياة عادية'`
        (newline included)
      - **texts == ['ليه لازم نتميز عن جيميناي؟']**; start, duration and clip unchanged; **all other
        tracks unchanged**; no unexpected window
      - The Arabic question mark «؟» typed correctly through KEYEVENTF_UNICODE.
    - **Inspector after the edit** (`55-title-text-inspector.png`): the paragraph box reads
      «ليه لازم نتميز عن جيميناي؟» on one line. As in rung 16, a one-line title moves the rows up:
      **Scale ≈(1792,333)**, **Position X ≈(1646,428) / Y ≈(1766,428)**, Plane rotation.
20. **Default size, measured** (empty click (1600,960), ruler click (314,628) into the hold after the
    1 s type-on; `56-title-default-player.png`; `yellow_bbox.py` on the 250 × 400 player crop; draft
    unchanged):
    - At **scale 100 %** the yellow bbox is **x 16–230, y 215–246 (215 × 32)**, centre (123, 230.5).
    - The canvas in that crop spans **x 16–231, y 9–392** (215 × 383 player px for 1080 × 1920), so
      the title **fills the full canvas width** (probably clipped) at ≈54–62 % down, over the chest.
    - `yellow_bbox.py`'s printed "canvas" numbers use the rung-16 16:9 scale factor; ignore them
      here.
    - **Not usable.** Measure at a second scale to get the unclipped width and the anchor offset
      (rung 16 §L.12 model), then place it.
    - The 100 % frame was at **00:00:02:04** (`56-tc-title-hold.png`): the ruler snapped to the
      caption start at 2.133, inside the hold phase.
21. **Scale 50 % trial:** click the title block (286,727), then Scale box (1792,333): `ctrl+a`,
    type `50`, Enter.
    - The draft saved on the first 0.5 s poll (snapshot `draft-23-title-scale50.json`).
    - **diff exactly 2 lines: `.tracks[3].segments[0].clip.scale.x/y` 1.0 → 0.5**; transform
      (0,0), start 0, duration 3 unchanged
    - ⚠ The measurement after an empty click (1600,960) found **no yellow pixels**, so the frame
      is checked before re-measuring.
    - **Cause:** the playhead was at **00:00:31:11**, the timeline end (`57-tc-scale50.png`), and
      the frame shows no title (`57-title-scale50-player.png`). It moved during the select, type,
      deselect sequence (not seen with the same empty click earlier), so the frame was outside
      the title's 0–3 s.
    - **Rule:** after any inspector edit, re-seat the playhead with a ruler click and check the
      timecode crop before capturing a measurement frame.
22. **Scale 50 % measured** (empty click, then ruler (314,628); timecode crop vs `56-tc-title-hold.png`
    **0 px > 15**, so the same 00:00:02:04; `58-title-scale50-player.png`):
    - yellow bbox **x 32–214, y 208–225 (183 × 18)**, centre **(123.0, 216.5)**; not clipped
23. **Anchor model and placement** (player crop px; canvas x 16–231 / y 9–392, centre (123.5, 200.5),
    **5.013 canvas px per player px** vertically):

    | Scale | Width | Height | Centre y | Offset below canvas centre |
    |---|---|---|---|---|
    | 100 % | 215 (clipped; unclipped ≈ 366) | 32 | 230.5 | +30 |
    | 50 % | **183** | **18** | 216.5 | **+16** |

    - The offset is proportional to scale (≈ 31 px × scale), as in rung 16 §L.12. Horizontally the
      title is centred.
    - **Chosen size: 50 %**, ≈85 % of the canvas width, ≈4.7 % of the height (one line).
    - **Target band:** centre **≈15 % down** (player y 66.5). That's below the platform header
      (≈ top 8–12 %) and over the hair and forehead, above the eyes (≈24 %), in both the wide seg 0
      and the punched seg 1.
    - **Delta:** 66.5 − 216.5 = **−150 player px = 752 canvas px up**.
    - Typed Position = 2 × canvas px, positive = up (typed Y scales with canvas height), so **X 0,
      Y +1504**, i.e. `transform.y` ≈ **0.7833**.
24. **Position Y applied:** click the title block (286,727), then Position Y box (1766,428):
    `ctrl+a`, type `1504`, Enter.
    - The draft saved on the first 0.5 s poll (snapshot `draft-24-title-y.json`).
    - **diff exactly 1 line: `.tracks[3].segments[0].clip.transform.y` 0.0 → 0.78333**; scale 0.5,
      start 0, duration 3 unchanged
    - **Measured** (empty click, ruler (314,628); timecode vs `56-tc-title-hold.png` 0 px > 15; and
      a second ruler click (296,628)):
      - yellow bbox **x 32–214, y 58–75 (183 × 18)**, centre **(123.0, 66.5)** in both frames
      - **exactly the predicted centre (123.5, 66.5)**
    - The anchor model and the typed-Y rule hold on a 9:16 canvas too.
    - **Frames** (`59-title-placed-2s.png` at 00:00:02:04, punched seg 1; `59-title-placed-1s7.png`
      at 00:00:01:23, wide seg 0):
      - «ليه لازم نتميز عن جيميناي؟» is **readable yellow bold on one line at ≈15 % down**, over
        the top of the head and the hair line, **above the eyes**
      - clear of the 70 % caption («لازم» visible at 2:04); correctly joined right-to-left Arabic
    - **Undo/redo gate:** Ctrl+Z → ty **0.0** (only Y reverted); Ctrl+Shift+Z → **0.78333**,
      byte-identical to `draft-24`. No modal.
    - ⚠ **Logo clash found:** the logo still has its 16:9 values (scale 0.12, tf 0.8385 / 0.8093).
      On the 9:16 canvas it renders **tiny at the top-right (≈9 % down), just above the title's
      right end**, which crowds the title for the first 3 s and is barely legible.
25. **Logo re-place plan:** move it to the **plain wall strip right of the head** (player crop
    x≈185–231 is wall at 15–50 % down in every frame checked) at ≈30 % down. That is clear of the
    title band (12.7–17.3 %) and the captions (70 %). Size it up for 9:16; the size comes from the
    image dimensions and is checked in a frame.

## Wait conditions

## Verification

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| `key right --repeat 63` advanced only 29 frames; the editor dimmed | a modal **"Couldn't output sound — Something went wrong on the sound output device. Connect to another device." [Go to settings] [Hide]** (`Qt622QWindowIcon` (760,421)–(1160,609)) opened mid-stepping (frame stepping scrubs audio) and swallowed the remaining keys; draft unchanged | click **Hide** (1094,573), never Go to settings; re-read the timecode and step the remainder in small checked batches; check `cc.py windows` for the (760,421) window after each batch |
| `]` then a clip click selected nothing; the tool icon stayed the plain arrow; the playhead moved 04:09:11 → 04:10:02 | `cc.py` warned "could not confirm CapCut is foreground" on the `]` press, so the key was lost and the click only re-activated the window (it also moved the playhead). No playback (tolerant timecode diff 0 px); draft unchanged | `cc.py focus` first, press `]`, **crop the tool icon (10,578)–(170,614) for the double-arrow glyph before clicking**; the playhead position doesn't matter for a rightward selection |

## Tree coverage notes

## Open questions for the user
- Which highlight range (candidates pending).
