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
