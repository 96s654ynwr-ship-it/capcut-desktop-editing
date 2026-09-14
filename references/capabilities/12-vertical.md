# Capability 12: Vertical (9:16 canvas, auto reframe, beat-synced cuts)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** to be chosen with the user. It must be an agent-owned project: a CapCut
  duplicate or a new project. `0914 (4)-copy`, which holds rungs 4–11, stays intact as the
  horizontal master.
- **Evidence:** `evidence/2026-09-14/cap12/`

## Goal
Produce a vertical (9:16) version natively in CapCut:
- change the canvas ratio to 9:16
- keep the speaker framed, using CapCut's **auto reframe** where available, or manual Position/Scale
  per clip as a fallback
- optionally cut to a music beat using CapCut's beat marks

Verify every step in the draft (canvas config, per-clip transforms / reframe materials, cut times
against beat marks) and in frames.

## Preconditions
- Rungs 0–11 approved.
- House style (`references/house-style.md`): captions Arabic-only. In 9:16 their position and size
  must be re-checked, since the lower third moves.
- Known routes from rung 0, to re-verify:
  - player **Ratio** button (≈1371,541)
  - project **Details ▸ Modify** (aspect ratio / resolution)
  - timeline and toolbar items for reframe and beats, to locate
- Credits: follow the user's standing answer, "run; stop if a cost appears". Stop at any cost or
  upsell dialog.
- **Leads found before starting** (read-only, 2026-09-14):
  - Player bottom-right icons include **Ratio** (`accessibility-controls.md`, rung 0).
  - **Details** panel (nothing selected): Aspect ratio "Original", Resolution "Adapted", Frame
    rate, and a **Modify** button. A yellow onboarding bubble can cover Modify.
  - **The canvas follows the first clip** (rung 0): a vertical first clip set the project to
    1080×1920.
  - Keyboard shortcuts list **"Clear beats"** (unassigned), so beat marks exist in 9.4.
  - `pro-features.md` rows "Beat detection" and "Auto reframe" are still unverified.
  - `User Data\Cache\SmartCrop\` holds renders named `0728 9：16 With Text …` / `Without Text …`
    (2026-08-22) and `0914 (6) …` (20:04 today). The user's own projects have gone through
    CapCut's smart-crop / reframe pipeline, so the feature is present in this install. Those
    projects are **not** touched; this is a lead only.
  - Home screen: **"Long video to shorts"** tool (AI suite). It is a separate route and not the
    in-editor reframe.

## Plan
1. **Choose the source with the user:** a short section of the horizontal master vs a raw take.
   Also the length, and whether beat-synced cuts are wanted (they need a music track).
2. **Duplicate** the chosen project natively (rung 1 route), or create a new project, and baseline
   it.
3. **Canvas 9:16:** Ratio ▸ 9:16 (or Details ▸ Modify). Verify the draft canvas config and a frame.
4. **Reframe:** find Auto reframe (Pro?) and apply it to the clips. Otherwise use a per-clip Scale
   plus Position X (typed unit = ½ canvas px). Verify the face is centred in frames across clips.
5. **Captions and title** in 9:16: check their position and size in frames, and adjust natively if
   they go off-frame.
6. **Beat-synced cuts** (if chosen): add music, generate beat marks, then split and trim cuts onto
   beats. Verify cut times against beat times in the draft.
7. **Verify, gate, save, scope check.**

## Procedure

### A. Duplicate the master (executed 2026-09-14)
1. **Snapshot the master first:** `draft_inspect.py summary "0914 (4)-copy" --json cap12/master-before.json`.
   - `diff` vs `cap11/final.json` = No differences.
   - Master mtime 22:00:40.991.
   - All project mtimes are in `cap12/mtimes-before.txt`.
2. **Home:** `scroll 1100 700 -5`, then a grid screenshot (`00-home-grid.png`). The first card is
   **0914 (4)-copy**, "264.8M | 07:31", at ≈(383,703). Its size grew from 188.9M after rung 11's
   enhanced audio.
3. **Right-click the card** (`click 383 703 --right`), then a fresh grid screenshot
   (`01-card-menu.png`).
   - The menu opens next to the pointer: **Upload** ≈(423,726), **Rename** ≈(426,766), a separator,
     **Duplicate** ≈(430,812), then **Delete ⟵Backspace** ≈(421,852).
   - The menu is **not** in the UIA tree (only HomeWindow plus a tooltip), so the screenshot is the
     only source for row positions.
   - ⚠ Delete sits 40 px under Duplicate. Click the vertical centre of the Duplicate row.
4. **Click Duplicate** (≈430,812), then poll the drafts folder for a new directory.
   - **`0914 (4)-copy-copy`** appeared within ≈1 s. CapCut appends `-copy`, so a copy of a copy
     is `…-copy-copy`.
   - **Agent-verified:** the structure diff of `master-before.json` against the new copy's
     `copy-baseline.json` is **No differences**.
   - The copy carries the rung-11 audio materials (loudnesses, realtime_denoises, vocal_beautifys)
     and **28 files in `Resources/`** (the Enhance-voice results and loudness analyses). No
     reprocessing is needed.
   - Master mtime is still **22:00:40.991**, unchanged.
5. **Home after duplicating** (`02-after-duplicate.png`):
   - The new card **0914 (4)-copy-copy** "264.8M | 07:31" is **first** (≈383,703), and the master
     0914 (4)-copy moved to second (≈566,703).
   - The rest shift one slot right, so re-read card names before every click.

### B. Open the copy and place the playhead at the section end (executed 2026-09-14)
1. Click the first card (≈383,703). `MainWindow` appears on the first poll. After ≈6 s,
   `focus --maximize`.
   - Title bar: **0914 (4)-copy-copy**. Details Name/Path are the copy's.
   - The timeline matches the master: PiP row, title TT, caption TT, 7 main clips.
   - The draft is unchanged by opening.
2. **Ruler click** at fit zoom: x = 229 + 2.7833 × 35.533 ≈ **328** (y 628).
   - The playhead landed on **00:00:37:10**, not ≈35.5 s. It snapped to the caption boundary
     «وانا هاعمل» at 37.33 s, as in rungs 5, 8 and 10.
3. `key left` × **54** (1120 → 1066 frames at 30 fps) → **00:00:35:16** (35.533 s), confirmed on
   a zoomed timecode crop (`05-tc.png`). The draft stays unchanged.

### C. Split all at the section end (executed + agent-verified 2026-09-14)
1. With the playhead at 00:00:35:16 and nothing selected, press **`key ctrl+shift+b`** (Split all).
   The draft saved on the first 0.5 s poll.
2. **`diff` vs `copy-baseline.json`:**
   - **Only the main track was split**, because it is the only track crossing 35.533 s. The caption
     track sits in a gap (35.27–35.80), the title ends at 4 s, and the PiP starts at 96 s. Split
     all leaves tracks that don't cross the playhead alone.
   - Main seg 0: duration 122.200 → **35.533 s** (src_duration likewise).
   - New seg: **35.533 → 122.200 s**, `VID_20260720_190542.mp4`.
   - segment_count 248 → 249, and every per-clip material +1 (videos, canvases, speeds,
     placeholder_infos, sound_channel_mappings, material_colors, vocal_separations,
     material_animations). The rung-11 **loudnesses / realtime_denoises / vocal_beautifys also +1**:
     the new piece gets its own copies.
   - Side effect: `+ref loudnesses; -ref loudnesses` on main segs at 122.2, 359.467 and 426.867 s.
     Their loudness materials were re-linked; values are checked in step 3.
3. **Audio refs after the split** (`audio_check.py` → `audio-after-split.json`, agent-verified):
   - Both halves of old clip 0, seg 0 (0–35.533) and the new seg 1 (35.533–122.2), keep denoise
     True, enhance `enable` True / 75, **the same `time_range` 46 933 333 + 122 200 000 µs** and
     the same loudness `file_id`, `avg` −11.67 and target −23.
   - The split did **not** re-run Enhance voice. Each piece plays the matching slice of the
     original enhanced result.
   - Segs 2–7 (former 1–6) keep identical values (−12.63, −12.62, −11.41, −11.34, −13.81, −13.71).
     The "re-linked" loudness refs are new material objects with unchanged values.
4. **After-split frame** (`06-after-split-all.png`):
   - A split line on main clip 0 at the playhead (x≈327). The left piece is labelled
     "VID_20260720_1…", the right one "VID_20260720_190542.mp4 00:01:26:2…".
   - The playhead stays at 00:00:35:16, nothing is selected, and the title bar reads "Auto saved:
     22:13:42".

### D. Selecting everything right of the playhead (in progress)
1. **Empty-timeline right-click** (`click 1000 680 --right`, `07-empty-timeline-menu.png`):
   - A `MenuWindow` appears in the tree. The right-click did **not** move the playhead (still
     00:00:35:16) or touch the draft.
   - Items: Close gap (disabled) ≈(1059,701), Close all gaps (disabled) ≈(1071,736), **Select**
     ≈(1047,777), Paste (disabled) ≈(1045,818), **Range ›** ≈(1048,854), **Render ›** ≈(1050,889).
   - "Select" has no ›, so it is an action or mode, not a submenu. Not clicked.
2. **Better route found in the shortcuts list:** **Select rightward = `]`** (and Select leftward =
   `[`), both "listed" and not yet verified. Plan: close the menu with a neutral click, refocus the
   timeline without seeking, then press `]`. The expected selection is every clip on every track
   starting at or after the playhead.
3. **Closing the menu:** a left-click on the empty Media panel area (≈380,480) closes the menu
   without seeking. `MenuWindow` is gone, the header reads "Player-Timeline 01", the playhead is
   still 00:00:35:16, and the draft is unchanged.
4. **Counts before deleting** (`section_check.py "0914 (4)-copy-copy" 35.533` →
   `section-before-delete.json`):

   | Track | Before cut | Straddling | After cut |
   |---|---|---|---|
   | 0 main video | 1 (ends 35.533) | 0 | 7 |
   | 1 captions | 18 (last ends 35.267) | 0 | 221 |
   | 2 title | 1 (ends 4.0) | 0 | 0 |
   | 3 overlay PiP | 0 | 0 | 1 |

   - Nothing straddles the cut, so deleting every "after" segment leaves exactly the 35.533 s
     section.
   - Canvas `ratio` "original", 1920×1080; duration 450.533 s.
5. **First `]` attempt:**
   - Refocused by clicking the right-hand piece of clip 0 (≈450,891). That selects it without
     seeking; the playhead stays at 35:16.
   - `cc.py key bracketright` failed with **"Unknown key 'bracketright'"**.
   - The selection didn't change: only the clicked piece is bordered (`10-after-bracket-tracks.png`).
6. **Second `]` attempt:** `cc.py key "]"` (VK_OEM_6 0xDD, a supported name) returned exit 0 and
   `{"keys": ["]"]}`.
   - The selection **still didn't change** (`11-after-bracket2-tracks.png`), and the playhead and
     draft are unchanged.
   - **Result:** the listed shortcut "Select rightward `]`" had no visible effect here. Either it
     isn't active in this context or layout, or it needs a state not yet found.
   - Don't rely on it. Its status in `keyboard-shortcuts.md` stays "listed" plus this note.
7. **Next route:** box-select (drag from empty timeline space) across all tracks right of the cut.
   Zoom in first, because at fit zoom (≈2.78 px/s) the last kept caption ends 1 px left of the cut
   and the first removed caption starts 1 px right of it.
8. **Zoom check** (`key "ctrl+="` × 4, `12-zoomed.png`):
   - Ruler labels 00:40 at x≈525 and 00:45 at x≈748 give **≈44.6 px/s**. The playhead stays at
     00:00:35:16 (x≈326), and the zoom keeps the playhead in view.
   - The last kept caption ends at x≈314 and the first removed caption («هاوثق…») starts at x≈338.
   - At this zoom, though, the PiP (96 s, x≈3020) and most later captions are **off-screen**, so a
     single box-select can't reach them.
   - The selected right piece of clip 0 is shown with a white border starting at the playhead.
9. **Revised plan:**
   1. Back to fit zoom (`key "ctrl+-"` × 4).
   2. **Ctrl+click** the right piece of clip 0, main clips 1–6 and the PiP block, then **Delete
      once** (one undo step).
   3. **Box-select the caption row only**, from empty space right of the last caption leftwards to
      just right of the cut, then Delete.
   4. Gate each delete with `section_check.py`. Expected final: main 1/0, captions 18/0, title 1/0,
      PiP 0. Otherwise Ctrl+Z.
10. **Back to fit zoom:** `key "ctrl+-"` × 4 restores the rung-11 layout (`13-fit-again.png`).
    - The playhead is still 00:00:35:16 (x≈327), and the right piece of clip 0 is still selected.
    - Main clips 1–6 are back at x≈740 / 921 / 945 / 1095 / 1323 / 1450 (y 891), the PiP block at
      ≈(501,744), and the caption row at y≈827 runs to x≈1450.
11. **Multi-select right of the cut:** with the right piece of clip 0 already selected, run
    `click <x> 891 --mod ctrl` for x = 740, 921, 945, 1095, 1323, 1450, then `click 501 744 --mod ctrl`
    (PiP).
    - **Observed** (`14-multiselect-right-tracks.png`): white borders on the right piece of clip 0,
      main clips 1–6 and the PiP block.
    - **Unexpectedly, every caption right of the cut is outlined too** (from x≈328 to the end of
      the caption row).
    - Captions left of the cut, the left piece of clip 0 and the title are **not** selected.
    - The selection was not captured after each Ctrl+click, so it's unknown which one pulled the
      captions in. It's likely the auto captions are linked to their source clips. With only the
      right piece of clip 0 selected (screens 09–11), no captions were outlined.
    - The playhead is still 00:00:35:16 and the draft is unchanged.
    - **So the planned separate caption box-select wasn't needed.** The next step deletes this
      selection once.

### E. Delete everything right of the cut (executed + agent-verified 2026-09-14)
1. With the selection from D.11, press **`key delete`**. The draft saved on the first 0.5 s poll.
2. **`section_check.py` → `section-after-delete.json`:**
   - track 0 main: **1 before / 0 after** (ends 35.533)
   - track 1 captions: **18 / 0** (last ends 35.267)
   - track 2 title: **1 / 0**
   - **the overlay track is gone** (3 tracks)
   - **duration 35.533 s**; canvas still `original` 1920×1080
3. **`diff` vs `copy-baseline.json`:**
   - duration 450.533 → **35.533 s**, track_count 4 → 3, segment_count 248 → 20
   - `- track 3 [video] removed`; the caption segments from 35.800 s onward are removed
   - materials shrink to match: videos / canvases / speeds / … 8 → 1, loudnesses / realtime_denoises
     / vocal_beautifys 7 → 1, texts / text_templates 240 → 19, effects 239 → 18,
     material_animations 246 → 20
4. `title_check`: 1 title, text tracks (1: 18), (2: 1).
   - `keyframes`: **none**. The rung-7 push-in lived on master seg 4 (262.5 s+), outside the
     section. Expected.
5. Master `0914 (4)-copy` mtime is still **22:00:40.991**.
6. **UI after delete** (`15-after-delete.png`):
   - The timeline shows only ≈35 s: the title TT, caption TT and one main clip, with **no overlay
     row**.
   - Player "00:00:35:16 / 00:00:35:16", "Auto saved: 22:23:52".
   - Aspect ratio still "Original".
7. **Undo/redo gate** (no MenuWindow or dialog open first):
   - `ctrl+z` → first poll: **duration 450.533 s**, t0 1/7, t1 18/221, t2 1/0, t3 0/1. That is
     exactly the pre-delete state, and one undo step removed all 229 segments.
   - `ctrl+shift+z` → first poll: **35.533 s**, t0 1/0, t1 18/0, t2 1/0.
   - Trimmed state saved as `trim-final.json`.

### F. Canvas 9:16 (executed 2026-09-14)
1. **Player Ratio button** (≈1371,541). A click opens a `MenuWindow` dropdown under the player
   (`17-ratio-menu.png`); the draft is unchanged by opening it.

   | Row | Position | Icon |
   |---|---|---|
   | **Original** ✓ (current) | ≈(1438,563) | — |
   | Custom | ≈(1438,598) | — |
   | 16:9 | ≈(1427,634) | landscape |
   | 4:3 | ≈(1424,669) | landscape |
   | 2.35:1 | ≈(1433,704) | landscape |
   | 2:1 | ≈(1423,739) | landscape |
   | 1.85:1 | ≈(1431,774) | landscape |
   | **9:16** | ≈(1427,810) | portrait |
   | 3:4 | ≈(1424,845) | portrait |
   | 5.8-inch | ≈(1440,880) | portrait |
   | 1:1 | ≈(1422,915) | square |

   A separator sits after Custom, after 1.85:1, and before 1:1.
2. **Click 9:16** (≈1427,810). The menu closes, and the draft saved on the first 0.5 s poll. No
   dialog.
3. **Agent-verified draft:**
   - `canvas_config` `{ratio: "original", 1920×1080}` → **`{ratio: "9:16", width: 1080, height:
     1920}`**. `diff` vs `trim-final.json` shows that single difference.
   - Main clip `clip` unchanged: scale 1.0, transform (0, 0). The ratio change does **not**
     auto-scale or reframe the video.
   - Captions keep `transform.y` −0.73 and the title keeps scale 0.55 / y 0.7407. These are
     normalised, so they move with the new canvas; frames still to check.
   - Duration 35.533 s and the counts (1 / 18 / 1) are unchanged.
4. **Observed after 9:16** (`18-after-916.png`, nothing selected, playhead 00:00:35:16):
   - The player shows a **portrait canvas** (x≈916–1131, y≈99–482). The 16:9 video sits
     **letterboxed in the middle** (y≈231–351) with **black bars above and below**. As the draft
     says, nothing reframes automatically.
   - The Ratio button now reads **"9:16"** (≈1373,541), and Details shows **Aspect ratio: 9:16**.
   - A **new player icon** appeared at ≈(1227,541), left of "Medium", with a **cyan dot**. Not yet
     identified: possibly a phone-preview or safe-zone toggle. Hover it before assuming.
   - "Auto saved: 22:26:22".

### G. Looking for Auto reframe (in progress)
1. **A clip click in 9:16** (≈277,840) selected the main clip **and a group of captions**: a white
   border on the main clip plus a white-bordered block on the caption row at x≈275–327
   (`19-clip-selected-916.png`).
   - The inspector became the **mixed "Properties" panel**: Transform only (Scale 100%, Uniform,
     Position X 0 / Y "-" mixed, Rotate, alignment row). There are **no Video/Audio tabs**, so no
     reframe control.
   - Scrolling the inspector (`20–22`) shows nothing more; that is all of Properties.
   - The toolbar shrinks to basic tools (`23-toolbar.png`), with no reframe icon.
   - Player: the letterboxed 16:9 video gets selection handles (✕, corners, ⟳) inside the 9:16
     canvas.
   - Draft unchanged.
2. **Hypothesis:** auto captions are linked to their source clip, so a clip click also selects
   captions under it. This matches D.11. Rung 11 clicks at (400,891) on the 7-clip horizontal
   timeline selected only the clip, which needs explaining. Next: right-click the clip (context
   menu), and hover the new player icon.
3. **New player icon** (≈1227,541): a **TikTok logo** with a cyan "new" dot
   (`24-player-icon-tooltip.png`). It appears once the canvas is 9:16. Hovering 1.8 s showed no
   tooltip; the only tooltip window was stale, over the timeline. Probably a TikTok safe-zone
   or preview overlay. Not clicked.
4. **Right-click on the clip in this mixed selection** (`click 277 845 --right`,
   `25-clip-context-menu.png`) opens a `MenuWindow` from ≈(305,457) downward:
   - Copy (Ctrl C), Cut (Ctrl X), Copy attributes (disabled), Paste attributes (disabled), Delete
     (Backspace)
   - Isolate voice (Free) ›, Sync video and audio (disabled)
   - Create compound clip (subproject) (Alt G), Create multi-camera clip (Free, disabled), Save
     preset
   - Group (Ctrl G), Ungroup (disabled), Deactivate clip (V), Link to media (disabled), Show
     variable speed animation (disabled)
   - Range ›, then the menu runs off-screen at the bottom
   - **No "Auto reframe" and no "Edit ›" item.** Compared with the single-clip menu from rung 0,
     Split scenes, Transcript, Extract audio, Export selected clips, Trim clip, Replace clip and
     Open file location are missing, consistent with a multi-selection.
   - Ungroup is disabled, so the clip and captions are not a Group. The co-selection has another
     cause.
5. **Accidental Cut and restore** (see Failure modes):
   - The "close menu" click at (380,480) landed inside the clip context menu. Draft at 22:30:00:
     **0 tracks, duration 0**.
   - Verified with no `MenuWindow` or dialog open, then a **single `ctrl+z`**. First poll: duration
     **35.533 s, ratio 9:16, 3 tracks**.
   - `diff` vs `trim-final.json` = **only the canvas change** (original 1920×1080 → 9:16
     1080×1920). Every clip, caption and title is back exactly.
   - The undo loop stops at the first state matching "35.533 / 9:16 / 3 tracks", and would redo
     once if the ratio reverted, so it can't over-undo past the canvas change.
   - **UI after the restore** (`28-after-restore.png`):
     - **All 20 segments are selected** (main clip, 18 captions, title, all white-bordered); the undo
       restores the cut selection.
     - The playhead is at 00:00:00:00, and the timeline **re-zoomed** to ≈16.7 px/s (00:10 at x≈395,
       00:20 at x≈562). The main clip spans x≈229–820 at y≈805–870, captions at y≈764, title at
       y≈731.
     - Inspector: mixed "Properties" (Scale "-", Position Y "-"). "Auto saved: 22:31:38".
6. **Clip-only selection by locking the text tracks:**
   - With no `MenuWindow` open, click the player panel's dark area (≈1300,300) to deselect
     (`29-deselect-*`).
   - Click the **lock** icons on the caption row (≈59,764) and the title row (≈59,731).
   - **Agent-verified draft:** caption track `attribute` 0 → **4**, title track 0 → **4**. Main
     video stays 0, duration 35.533 s and ratio 9:16 are unchanged.
   - Then click the main clip body (≈500,845), screenshot `30-clip-only-*`.
   - Unlock both tracks again before saving, so the text stays editable. Verify `attribute` back to
     0.
   - **Result (`30-clip-only-*`):**
     - The player-area click cleared the selection (no borders in `29-deselect-tracks.png`).
     - After locking, both text rows show the **diagonal lock hatch** with cyan lock icons.
     - The clip click selects **only the main clip**, and the inspector shows the full single-clip
       tabs **Video · Audio · Speed · Animation · Adjust · A…›** with sub-tabs Basic / Remove BG /
       Mask / Retouch.
     - Transform: Scale 100%, Position 0/0, Blend ✓. No reframe control is visible in the top of
       Video ▸ Basic.
   - **Lesson:** to get the single-clip Video inspector on a timeline with auto captions, lock the
     caption and title tracks first.
7. **Where Auto reframe lives** (single clip selected; `31–33`):
   - **Toolbar** (`31-toolbar-single-clip.png`): the clip tools after Delete are crop/transform
     icons, AI icons and HD. No labelled reframe button.
   - **Video ▸ Basic** scrolls to a long list below Transform/Blend (`scroll 1480 450 -4` × 3):

     | Control | Badge / extras |
     |---|---|
     | Enhance quality | Pro ▾ |
     | Reduce image noise | Pro ▾ |
     | Optical flow | Pro ▾, "Apply to all" |
     | AI remove | Pro ▾, reset |
     | AI expand | **Free** ▾, reset |
     | AI remix | **Try free** ▾, reset |
     | Lip sync | Pro ▾ |
     | Relight | Pro ▾, keyframe ◇ |
     | **Auto reframe** | **Pro ▾** |
     | Remove flickers | Pro ▾ |
     | AI movement | Pro ▾, reset |
     | Camera tracking | Pro ▾, reset |
     | Motion blur | ⓘ Pro ▾, reset |
     | Canvas | ✓ ▾, "Apply to all" (bottom of the list) |

   - **Auto reframe checkbox** ≈(1468,172), with **▾** ≈(1603,172), at the third scroll position
     (`32-video-basic-scroll3.png`).
   - The inspector tab row's **›** (≈1891,70) scrolls the tabs to reveal **AI stylize** after
     Adjust (`33-inspector-tabs-more.png`). The body stays on Video ▸ Basic.
   - Browsing only: the draft is unchanged.
8. **Auto reframe ▾ expanded** (click ≈1603,172; `34-auto-reframe-expanded.png`). The checkbox
   stays unticked, the draft is unchanged, and the panel opens inline:

   | Field | Default | Dropdown ≈ (screen, at this scroll) |
   |---|---|---|
   | Aspect ratio | **Original** | ≈(1751,221) |
   | Image stabilization | **Default** | ≈(1751,268) |
   | Camera moving speed | **Default** | ≈(1751,316) |
   | **Apply** button | greyed | ≈(1844,395) |

   - The labels and values render greyed while the box is unticked.
   - `scroll 1480 300 -2` scrolls the panel mostly out of view (`35-…`), and `+2` restores it.
9. **Tick the Auto reframe checkbox** (≈1468,172, after `scroll 1480 300 2`; before/after
   `36-before-tick.png`, `37-after-tick*.png`):
   - The checkbox turns cyan. Aspect ratio / Image stabilization / Camera moving speed become
     active (still Original / Default / Default), and **Apply** becomes enabled.
   - A **"Auto reframe applied"** toast appears over the timeline. "Auto saved: 22:37:23".
   - **No credit, cost or upsell dialog** (tree: MainWindow plus a tooltip).
   - The player is **still letterboxed**: with Aspect ratio "Original" nothing visibly changes.
     The selected clip gets a cyan outline.
   - **Draft** (`diff` vs `trim-final.json`): canvas 9:16, caption and title track `attribute` 0 → 4
     (the locks from step 6), and **main seg 0 `material changed`** (same file name). Clip scale and
     transform are unchanged (1.0 / 0,0); `crop` is the full frame, `crop_ratio` "free",
     `stable.stable_level` 0, `smart_motion` null. The deep diff vs the master's untouched material
     identifies the changed field (next step).
   - **Deep diff** of the copy's main video material vs the master's untouched one (read-only, both
     drafts): the **only** change is **`check_flag` 62978047 → 63043327** (+0xFF00). The segment
     itself (minus timeranges/refs) is identical.
   - So **ticking only sets a feature bit**. No reframe data exists yet; the real reframe happens
     with a target **Aspect ratio** plus **Apply**.

## Wait conditions

## Verification

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| **The whole timeline vanished** (draft 22:30:00: 3 tracks → 0, duration 0). The player went black with "Drag material here and start to create". | **Agent error.** To close the clip context menu, the agent clicked a fixed "neutral" point (≈380,480) in the Media panel, which had worked for the *empty-timeline* menu. The *clip* context menu opened at the pointer and spanned x≈280–655, y≈440–1030, over the Media panel. The click landed inside it, between **Copy (457)** and **Cut (492)**, and most likely ran **Cut**, removing the selected clip and captions and apparently the title too. | Undo (`ctrl+z`) until the draft matches `trim-final.json` plus the 9:16 canvas (see the restore record). **Rule:** never close a CapCut menu with a fixed coordinate. Take a screenshot, read the menu's rectangle, and click clearly outside it (e.g. the player's empty dark area) or use a spot verified for that menu. Re-check the tree for `MenuWindow` before any other input. Recorded in `project-safety.md` too. |

## Tree coverage notes

## User choices (2026-09-14)
- **Source:** "Short clip from the master (Recommended)". Make a CapCut **duplicate of `0914
  (4)-copy`** and keep one ≈30 s section (the opening, with the title) in the duplicate. The master
  stays untouched.
- **Reframe:** "CapCut Auto reframe (Recommended)". Use CapCut's AI auto reframe, which follows the
  face. Stop at any cost or upsell dialog.
- **Beat sync:** "Skip beat sync for now (Recommended)". No music and no beat cuts in this rung;
  the ladder keeps beat sync for later.
- **Length:** "About 30 s (Recommended)". End on a sentence boundary from the caption timings.
- **Section picked by the agent** (from `cap10/all-captions.txt`, timeline times on the master):
  **00:00:00:00 → 00:00:35:16 (35.533 s)**.
  - It opens with «بسم الله الرحمن الرحيم» and «زهجت من التاجيل وخلاص» under the title, and runs
    through «…فقلت خليني اوثق / الرحلة مش هاحكي كتير / او مش هاحضر كتير», which ends at 35.27 s.
  - The next caption «هاوثق اللي انا هاعمله» starts at 35.80 s, so the cut sits in that 0.53 s gap.
  - Why not ≈30 s: 29.90–31.50 «كده فقلت خليني اوثق» continues into «الرحلة…» at 31.70, so a
    cut near 30 s would split the sentence. The shorter clean option, 0 → 25.2 s, drops the
    "document the journey" hook that matches the title.
  - The section lies entirely inside master clip 0 (0–122.2 s), which has no punch-in. The title
    (1–4 s) is included. The PiP (96 s) and every caption after 35.8 s fall outside it.

## Open questions for the user
- Source, length, beat-sync yes/no, music choice.
