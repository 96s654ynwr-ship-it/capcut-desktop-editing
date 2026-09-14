# Capability 09: Animated text (titles, text templates, word-by-word)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0914 (4)-copy`. It is the agent-owned duplicate carrying the approved
  house captions (Arabic-only, "Classic: black box") plus the rung 4–7 edits, 7:30.533.
- **Evidence:** `evidence/2026-09-14/cap9/`

## Goal
Add animated on-screen text at a stated time, separate from the auto captions:
- a **title** near the start: an Arabic headline with an in/out animation, or a text template
- its style, position and duration stated and verified

It must be readable in screenshots and must not collide with the house captions in the lower
third. Record the native route (Text asset tab → Add text / Text template → inspector Text ▸
Animation), how animations are stored in the draft, and how to verify them frame by frame.

## Preconditions
- Rungs 0–8 approved. House style in `references/house-style.md`: captions stay Arabic-only in
  the lower third, so titles go in the upper area.
- Tools reused:
  - ruler + Home/↓ + arrows for exact playhead placement (rungs 1, 5)
  - Text ▸ Basic text box / font / size / Transform Position (rung 8)
  - Text ▸ Templates (rung 8)
  - template-aware draft dumps (rung 8)
  - undo/redo gate and Back to home page save

## Plan
1. **Map the Text asset tab:** Add text, Text templates (categories, Pro badges), Text effects, and
   how a text element lands on the timeline (new text track, default duration, playhead position).
2. **Add a title** at a stated time (e.g. 00:00:01:00, 4 s long). Type an Arabic title (text to be
   confirmed with the user), style it (size, bold, colour or template), and place it in the upper
   third (Transform Position Y positive).
3. **Animate it:** inspector **Animation** tab (In / Out / Loop), pick an in and out animation with
   stated durations. Or use a text template with built-in animation.
4. **Verify:**
   - draft: new text segment at the stated start/duration, its material, animation refs
     (`material_animations`), position
   - frames at the start of the in animation, mid-hold and during the out animation
   - no overlap with a house caption at the same time
5. **Undo/redo, save,** then the draft check.

## Procedure

### A. Open the practice copy (executed 2026-09-14)
1. Home, then `scroll 1100 700 -5`, then a grid screenshot. Read the card names: the **first card
   read "0914 (4)-copy"** (≈383,680), the newest draft.
2. Check the draft mtime is unchanged since the baseline (19:23:11.901). The user sometimes reviews
   in CapCut between turns.
3. Click the card, then `focus --maximize`, and confirm the title bar reads **0914 (4)-copy**.
4. Asset tab **Text** (≈164,73).
   - **Observed** (`text-tab.png`): the title bar reads **0914 (4)-copy** and the draft is
     unchanged.
   - Left sub-list:

     | Item | Position |
     |---|---|
     | **Add text** (selected by default) | ≈(57,131) |
     | Yours ▾ | ≈(85,171) |
     | Text effects ▾ | ≈(85,211) |
     | **Text template ▾** | ≈(85,251) |
     | Auto captions | ≈(75,291) |
     | Local captions | ≈(78,331) |

   - The Add text grid shows a single **"Default text"** card (≈231,165).
   - The right panel shows project Details, because nothing is selected. The timeline has the
     house caption row (TT, y≈763) above the video.

### B. Text ▸ Text template panel (observed 2026-09-14, `text-template-open.png`)
- **Open:** click **Text template ▾** (≈85,251). It expands inline into categories and loaded
  within ≈6 s. The draft was unchanged.
- **Categories:**

  | Category | Position |
  |---|---|
  | **Trending** (default, cyan) | ≈(57,291) |
  | Whimsical | ≈(64,331) |
  | KATSEYE 👠 | ≈(64,371) |
  | Pixel Bead 👾 | ≈(69,411) |
  | Classic | ≈(55,451) |
  | NEW | ≈(47,491) |

  More categories are below, and the list scrolls.
- **Search:** "Search for text templates" (≈370,127), with a filter icon ≈(565,127).
- **Grid:** 3 columns, tiles ≈129 px apart horizontally and ≈123 px vertically, starting at tile
  centre ≈(231,240).
  - Each tile has a ⬇ download icon at its bottom-right.
  - **Most tiles carry a purple Pro diamond** (top-left).
  - Trending examples: "Chapter End" (Pro), "FINAL" flames (Pro), "The Story Begins" (Pro), "KEEP
    GOING" (Pro), "LOCATION" pin, "Breaking News" (Pro), "BAM!" comic (Pro), a Thai-script
    title (Pro), "CREATIVE" glow (Pro).
  - These are English/Latin previews. Arabic shaping must be verified on the player after typing
    the title.
- **Classic** (≈55,451): "CINEMATIC", "THE MOMENT BEGINS WITH ONE SCENE", "CREATIVE", "EXCLUSIVE",
  "SPECIAL OFFER" (all Pro). "TITLE HERE", "Simple Title" and "Simple Font" have no diamond.
- **NEW** (≈47,491): mostly Pro, except the "ABC" pair. Scrolling the category list (`scroll 80 450
  -3`) reveals Hits, Free Fire, Icons, **Title**, Retro, Advertisement, Social media, Tag, Vlog.
- **Search is the route to Arabic templates.** Click the search box (≈370,127), `type "عربي"`
  (clipboard paste), then Enter. After ≈5 s the grid fills with Arabic-script templates.
  - Most carry **no Pro diamond**. Examples: «الفرح في البساطة» (white brush), «يوم عادي، حياة
    عادية» (yellow bold), «الحياة تستمر» (glow calligraphy), «حياة صغيرة» (colour outline),
    «وتشرق الشمس» (green box), «يوم بسيط» (several), «استمتع بالوقت» (yellow frame), «قليلا الحياة»
    (red circle).
  - Some Latin and other scripts are mixed in: Vietnamese, Korean, French, German, Filipino.
  - While a search is active, the **category list is hidden**. The left column shows only the
    collapsed sub-list.
- **Scrolling the grid:** scroll at **(370,400)**, 3 ticks ≈ 1.3 rows. The panel ends at screen
  y≈565, and a scroll at y 600 lands on the timeline instead. Browsing, searching and scrolling
  never changed the draft (mtime unchanged).
- Candidate contact sheet: `evidence/2026-09-14/cap9/templates/title-candidates-sheet.png`, built
  with `cap9/contact_sheet.py`.

### C. Preview a text template (observed 2026-09-14)
- **Hover** a tile: a ☆ favourite icon appears left of the ⬇ download icon, at the tile's
  bottom-right. There is no + button, and no player change.
- **Click** the tile body (≈15 px up-left of centre, away from the icons):
  - The tile gets a cyan border.
  - The ⬇ icon turns into a cyan **+** (≈ tile centre + (37,39); for tile #3 ≈522,378).
  - The player header reads **"Previewing — Text template"**, with its time display showing the
    template's own length (#3: **00:00:03:00**).
  - **The draft is unchanged** (mtime identical). A click previews, and only the **+** adds.
- Downscaled full-window screenshots can make the Arabic tile thumbnails look mirrored or
  unjoined. A 2× crop (`10-hover-tiles-zoom.png`) shows they render correctly, so zoom in before
  judging Arabic shaping.
- **Play the preview:** click the player ▶ (≈1024,541), then grab player-region screenshots
  (`screenshot --region 612,90,1436,560` in a loop, one about every 0.5 s). Frames are in
  `cap9/preview/f01–f06.png`.
- **Template #3 animation, observed:**
  - Two centred lines of heavy yellow Arabic, very large (about two thirds of the frame width),
    over the paused-then-playing timeline video.
  - **In:** the text types on letter by letter. At 0:23 line 2 reads only «حياة ع». Fully shown by
    ≈1:13.
  - **Hold** until 3:00, with no visible out animation in the frames at 2:01 and 2:19.
  - At 3:00 the preview stops and resets to 0:00. It does not loop.
  - A «بسم الله الرحمن الرحيم» strip in the lower-middle at 0:23 and 1:13 is the **house caption**
    (0–≈2 s, current word on the black box). It also shows on the normal player at 00:00:01:00. The
    preview **composites the real timeline** (video + captions) under the template, which makes it
    a useful overlap check.
- **Leave the preview, then set the start:** click empty timeline space (≈1000,690). The header
  returns to "Player-Timeline 01", the tile loses its cyan border, and the draft is unchanged.
  Then `key home` plus 30 × `key right` (30 fps) puts the playhead at **00:00:01:00**, verified on
  the timecode.
  - As previewed, centred and large, it would cover the speaker's face. It needs Position Y moved
    up and probably a smaller scale.

### D. Add the template at the playhead (executed 2026-09-14)
1. With the playhead at 00:00:01:00, hover tile #3 (≈470,325). The hover icons show ☆ and a cyan
   **+** at ≈(523,379), because the tile is already downloaded from the preview. The zoom crop is
   `13-hover-tile3-icons.png`.
2. Click **+** (≈523,379), then poll the draft mtime until it changes. It saved within about 1 s
   (19:49:10 → 20:19:39).
3. **Agent-verified** with `title_check.py` and `draft_inspect.py diff`:
   - **New text track** (track 2, flag 0) with **1 segment**, above the caption track. The house
     caption track (239) is untouched.
   - `target_timerange`: start **1.000 s (00:00:01:00)**, duration **3.000 s**. The template's own
     length lands at the playhead.
   - Material `text_templates`: name **"Arabic An ordinary day, an ordinary life"**, resource
     **7659823758919699730**. One linked `texts` material holds the placeholder
     «يوم عادي،\nحياة عادية» (a two-line newline).
   - `extra_material_refs` → `material_animations` with one **in** animation, start 0, **duration
     1 000 000 µs (1 s)**, empty name (built into the template). There is no out animation, which
     matches the preview.
   - `clip`: scale 1.0, transform (0, 0), so it is centred.
   - Diff vs `after-close.json`: tracks 2→3, segments 246→247, texts / text_templates /
     material_animations +1 each. Nothing else changed.
4. **Observed UI after adding** (`14-added.png`):
   - Title bar: "Auto saved: 20:19:40".
   - The new segment is selected: a short red block at the start of a new TT row (y≈731) above
     the caption row (y≈763). Everything below shifted down one row.
   - The player at 00:00:01:00 shows no title yet (the in animation starts from nothing). Dashed
     vertical guides mark the title's box, x≈758–1289.
   - **Inspector for a selected text template:**
     - Top tabs: **Text · Tracking · Text to speech · AI avatars (Pro)**. There is **no Animation
       tab**, because the template's animation is built in.
     - Sub-tabs: Basic · Templates · Effects.
     - Basic shows **"The 1 paragraph"** with a text box ≈(1655,227) and a ▾ at ≈(1878,227).
       There is one box per template paragraph.
     - **Transform:** Scale 100% (box ≈1800,349), Uniform scale on, Position X ≈(1645,444) /
       Y ≈(1768,444), Plane rotation 0.00°, with keyframe ◇ at the right.
     - Bottom: "Save as preset".

### E. Replace the placeholder with the title (executed 2026-09-14)
1. Click the "The 1 paragraph" text box (≈1655,227), then `key ctrl+a` and `type "زهقت من التأجيل"`
   (clipboard paste). The template's two-line placeholder is fully replaced by one line.
2. Poll `title_check.py` until `texts == ["زهقت من التأجيل"]`. It matched on the 3rd poll (≈1.5 s).
   Title bar: "Auto saved: 20:20:44".
3. **Agent-verified:**
   - still 1 non-house segment
   - start 1.000 s, duration 3.000 s
   - template and in-animation refs unchanged
4. **Observed:**
   - The text box shows «زهقت من التأجيل» correctly joined right-to-left (zoom
     `15-typed-inspector.png`).
   - With one line the box shrinks, so the inspector rows move up ≈16 px: Transform ≈269, Scale box
     ≈(1800,333), Position X ≈(1645,428) / Y ≈(1768,428).
   - An alignment toolbar row appears under Plane rotation.
   - A horizontal dashed guide sits at player y≈247.
   - **Focus stays in the text box.** Arrow keys would move the caret, so click empty timeline space
     (≈1000,675) before stepping the playhead.
5. **Frame at 00:00:02:15 (hold), scale 100%, position (0,0)** (`16-hold-centred.png`):
   - The title renders as **one very large heavy yellow line**, correctly joined.
   - It is **wider than the frame**: «ز» is clipped at the right edge and the final letter at the
     left edge.
   - Its vertical centre sits **below** frame centre (player y≈375 of 99–482). The template's
     content box is anchored low, so transform (0,0) does not mean centred text.
   - It covers the speaker's chest and the lower-middle.
   - **Not acceptable as-is.** It needs a smaller scale and Position Y moved up (section F).

### F. Scale and place the title in the upper area (executed 2026-09-14)
1. Click the title block on its TT row (≈236,731). This **selects it without moving the playhead**,
   which stayed at 00:00:02:15. The inspector returns to Text ▸ Basic in the one-line layout (see
   section E), and the draft is unchanged.
2. **Scale:** click the Scale box (≈1785,333), then `key ctrl+a`, `type "55"`, `key enter`.
3. **Position Y:** click the Y box (≈1768,428), then `key ctrl+a`, `type "450"`, `key enter`.
4. **Agent-verified** (first poll): `clip.scale` = **(0.55, 0.55)** (uniform), `clip.transform` =
   **(0, 0.41667)**.
   - Y px / 1080, the same mapping as captions (positive = up).
   - Start 1.000 s, duration 3.000 s, text unchanged.
5. **Frame at 2:15 with scale 55%, Y 450** (`18-scaled-moved.png`, `18-player2x.png`):
   - The whole title is visible, correctly joined, with no clipping. It spans player x≈815–1235
     (≈62% of frame width).
   - The selection box (dashed, with a ⟳ rotate handle below) is taller than the glyphs: player
     y≈187–322.
   - **But the text band (y≈230–290) crosses the speaker's forehead and eyes** (head ≈225–320),
     so Y 450 is too low for this shot.
6. **Y 700:** repeat step 3 with `"700"`. The target text band is player y≈139–199, above the head.
   - Draft: `transform.y` **0.64815** (700/1080), first poll.
   - `diff` vs `after-close.json` is still only the 6 additive lines: track +1, segment +1,
     texts / text_templates / material_animations +1.
   - `track_styles.py`: track 1 is still 239 × 边框弹出黑色 at y −0.73. Track 2 is 1 × "Arabic An
     ordinary day, an ordinary life" at y 0.6481.
   - **Frame** (`19-player2x.png`): the title is fully in frame and clean, but the descenders of
     «من التأجيل» still graze the top of the speaker's head. Still slightly too low.
7. **Y 800:** repeat step 3 with `"800"` for about 36 px (2× crop) of clearance above the head, with
   ≈15% top margin. Then check frames across the title's life (section G).

### G. Frame check across the title's life (executed 2026-09-14, Y 800)
- Draft: `transform.y` **0.74074** (800/1080), scale 0.55, start 1.000 s, duration 3.000 s, text
  «زهقت من التأجيل», first poll.
- **Route:**
  1. Click empty timeline (≈1000,675) to deselect, so no selection box shows in the frames.
  2. `key home`, then Right × 42 / +33 / +40 / +10.
  3. After each, `screenshot --region 612,90,1436,560`.
  - Output: `cap9/frames/*.png`, contact sheet `frames/title-frames-sheet.png`.
- **Observed (agent-verified on frames plus timecode):**

  | Timecode | Phase | What the frame shows |
  |---|---|---|
  | 00:00:01:12 | in | **Type-on** reveal from the right: «زهقت م» visible, the rest not yet drawn. The house caption «بسم الله الرحمن الرحيم» is in the lower third, with no overlap. |
  | 00:00:02:15 | hold | Full title, one line, player y≈85–135 (upper fifth), x≈205–620. **Clear above the speaker's head.** No caption at this instant. |
  | 00:00:03:25 | hold, last frames | Full title, plus the caption «زهجت من التأجيل وخلاص». The speaker is saying the line, and the two layers are far apart vertically. |
  | 00:00:04:05 | after | Title **gone** (segment ends at 4.000 s), caption intact. |

  - There is **no out animation**: the title disappears on the cut at 4:00. This matches the
    single `in` entry in `material_animations`.
  - The caption spells the dialect «زهجت». The title uses «زهقت», as the user chose.

## Wait conditions
- **Text template panel / category / search results:** a screenshot after ≈5–6 s (thumbnails load
  lazily). No UIA signal is available.
- **Preview:** the player header changes to "Previewing — Text template" immediately on tile click.
- **Add / type / Scale / Position:** poll `title_check.py` for the *expected value*, not just an
  mtime change. Every change here landed within 0.5–1.5 s. CapCut can write the draft mid-typing, so
  the reader retries.
- **Frames:** after stepping the playhead, wait ≈0.9 s before the screenshot, and always read the
  timecode in the image.

## Verification
Evidence levels for rung 9 (2026-09-14, `0914 (4)-copy`):
- **Agent-verified (draft):**
  - one new text track (track 2) with 1 `text_templates` segment "Arabic An ordinary day, an
    ordinary life" (resource 7659823758919699730)
  - start **1.000 s**, duration **3.000 s**
  - text **«زهقت من التأجيل»** (placeholder fully replaced)
  - `material_animations`: one **in**, 0–1 s
  - clip scale **0.55**, transform **(0, 0.74074)** = Position Y 800
  - `diff` vs the pre-add state shows only the 6 additive lines. `track_styles.py` shows the 239
    house captions unchanged (边框弹出黑色, y −0.73).
- **Agent-verified (frames):** type-on at 1:12, full title above the head at 2:15 and 3:25, gone at
  4:05. No overlap with the lower-third captions. Arabic joined correctly at 2× zoom.
- **Undo/redo gate:** see below.
- **Save:** see section H.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Template | #3 "Arabic An ordinary day, an ordinary life" (search «عربي») | User taste choice | Shown as a contact sheet first. The user picked it. |
| Start | 00:00:01:00 (playhead: Home + 30 × →) | Shot-specific | Near the start, after the first caption word begins. |
| Duration | 3.000 s (the template default, not changed) | Template default | Check the title is gone after start + duration. |
| Text | «زهقت من التأجيل», one line | User choice | Draft `texts` equals the string, and the frame shows correct joining. |
| Scale | 55% | Shot-specific (depends on text length) | Whole line inside the frame with margin: ≈62% of width at 55% for 15 characters. At 100% it clipped both edges. |
| Position Y | 800 px (`transform.y` 0.74074) | Shot-specific (framing) | The text band sits above the speaker's head at hold frames. 450 crossed the eyes and 700 grazed the scalp. |
| Animation | Template built-in: in 1 s type-on, no out | Template default | `material_animations` has a single `in`, and the frame at 1:12 is partial. |

## Undo / recovery
- **Gate executed 2026-09-14:** with the title at Y 800 and timeline focus (after stepping the
  playhead):
  1. `key ctrl+z` → first poll: `transform.y` **0.64815** (Y 700). Scale, text and timing unchanged.
  2. `key ctrl+shift+z` → first poll: `transform.y` **0.74074** again. Start/duration/text are
     identical, and `diff` vs pre-add is the same 6 additive lines.
  - Frames `frames/gate-undo.png` and `gate-redo.png`.
- **Full removal, if needed:** select the title block on its TT row, then Delete (not Backspace
  inside a text field), then verify `title_check.py` shows 0 non-house segments and the text track
  count is back to 2.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| Clicking empty timeline space (≈1000,675) to deselect also **moved the playhead** to that x (≈00:04:34). The 45 × Right presses then landed at 00:04:36:03, not 2:15. | In the empty area above the tracks, a click both deselects and seeks. | Harmless: the draft was unchanged. After deselecting, press `home`, then step with Right (75 × for 00:00:02:15). Read the timecode before trusting a frame. |
| While polling right after typing the title, `title_check.py` failed with `JSONDecodeError: Invalid control character`. The next poll had no JSON output. | CapCut autosaves mid-typing, and the read caught `draft_content.json` half-written. | `title_check.py` now parses with `strict=False` and retries up to 10 × 0.4 s. Poll for the *expected text* instead of trusting the first read. The third poll matched «زهقت من التأجيل». |
| Between turns the editor was closed (Home showing) and the copy's draft mtime moved 19:23:11 → 19:49:10. `diff` then listed 22 caption rows as `material changed` with identical text. | The user reviewed or closed the project, and CapCut re-serialized 22 caption text materials on close. `material_probe.py` showed only the summary `sig` hash differs. Text, template (239 × 边框弹出黑色), y −0.73 and the video track are unchanged. | Not an edit, so no action. Before trusting a baseline, re-run `track_styles.py` plus `diff`. Treat `material changed` with an identical name as re-serialization only after the template/position/text checks pass. The user also created `0914 (6)` at 20:05, which the agent does not touch. |

## Tree coverage notes

## User choices (2026-09-14)
- **Title text:** «زهقت من التأجيل» ("I'm done procrastinating"), the video's opening line and
  theme.
- **Build:** a **text template** from CapCut's Text ▸ Text templates, with built-in animation. Show
  the options before applying, because template choice is a taste decision.
- **Placement:** near the start, upper part of the frame, clear of the lower-third house captions.
- **Template (chosen from the 12-tile sheet):** **#3 "yellow bold"**. It is the search «عربي» result
  whose preview reads «يوم عادي، حياة عادية» (row 1, column 3 of the unscrolled grid, ≈485,339
  on screen), with no Pro diamond. User's words: "3 yellow bold (Recommended)".
- Baseline before any rung-9 change: `evidence/2026-09-14/cap9/baseline.json` (2 tracks, 246
  segments, draft 19:23:11).

## Open questions for the user
- Which text template (shown as a contact sheet before applying).
