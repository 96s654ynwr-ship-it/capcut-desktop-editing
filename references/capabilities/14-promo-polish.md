# Capability 14: Promo polish (transitions, filters/adjust/color, logo/brand overlay, templates)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** to be chosen with the user. Must be agent-owned: a CapCut duplicate or a
  new project. The approved results `0914 (4)-copy`, `0914 (4)-copy-copy` and `0915` stay as
  they are unless the user says otherwise.
- **Evidence:** `evidence/2026-09-15/cap14/`

## Goal
Give a short edit a promo finish, natively, with each step verified in the saved project file and
by player frames:
- **one transition** at a cut
- **one colour step:** a filter, or Adjust
- **one logo / brand overlay** that stays in a corner for the chosen range

## Preconditions
- Rungs 0–13 approved.
- **Credits / Pro:** standing answer "run; stop if a cost appears". Stop at any cost, credit or
  upsell dialog. Pro diamonds are noted per card.
- **Known routes** (from rungs 0, 9, 10, 13; not yet run for this rung):
  - Asset tab **Transitions**: Favorites, Transitions ▾ (Trending, Classic, Overlay, Light,
    Camera, 3D…), named cards, some Pro.
  - Asset tab **Filters**: Favorites, Filters ▾ (Featured, NEW, Hits, CCD, Life, …), named cards,
    some Pro.
  - Asset tab **Adjustment**: Add adjustment (adds an adjustment layer), Yours ▾, LUT.
  - Inspector **Adjust ▸ Basic**: Auto adjust (Pro), Color match (Pro), Color correction (Pro),
    plus LUT / HSL / Curves / Color wheel.
  - **Library search:** a search box at the top of each asset panel ≈(380,127). Results can show
    "Loading…" for several seconds (rung 13).
  - **Dropping a library card onto a clip** attaches the item to that clip. Rung 13: the Effects
    "Blur" card went to the segment's `extra_material_refs` with no separate track.
  - **Overlay media:** Ctrl+I import (`act set-value --id 1148`, then invoke Open), then drag the
    media card above the tracks, which creates an overlay track (rung 10). Position units:
    typed = transform × canvas, and transform 1.0 = half the canvas.
  - **Text:** Text ▸ Add text / Text template (rung 9).
- **Lessons to apply:**
  - Screenshot before every click into a menu or panel.
  - Lock text tracks before clicking clips.
  - Frame-exact playhead: ruler click + arrows + timecode crop.
  - Ctrl+Shift+Z is redo (not Ctrl+Y).
  - Some steps take two undo steps; guard a field that must not change.

## Plan
1. Settle the scope with the user: project, logo source, transition style, colour approach.
2. Prepare the practice project (CapCut Duplicate if chosen) and baseline it (`layers.py`,
   draft copy, mtimes).
3. **Transition** at the chosen cut: card onto the cut point. Verify a draft `transitions` material
   and a segment ref, plus frames across the transition.
4. **Colour:** filter card onto the clip(s), or Adjust values. Verify the draft (`effects`/`filters`
   material, or adjust params) and before/after frames.
5. **Logo overlay:** import or build it, place it in a corner at a stated size and position, for the
   full duration or a stated range. Verify the overlay track, transform and frames.
6. Undo/redo gate per step, Back to home page, scope check, write-up, contact sheet, ask for
   approval.

## Procedure

### A. Duplicate `0915` (executed + agent-verified 2026-09-15)
1. **Baseline:** all project mtimes saved to `cap14/mtimes-before.txt` (15 projects).
2. **Home:** `scroll 1000 700 -3` brings the Projects row into view; the `0915` card is at ≈(383,793)
   with its name below (`00-home-projects.png`).
3. **Right-click the card** (`click 383 793 --right`). An **inline menu** opens, not a separate
   window (`01-card-context-menu.png`):
   - **Upload** ≈(423,816): cloud, never click.
   - **Rename** ≈(426,856).
   - **Duplicate** ≈(430,902).
   - **Delete ⌫** ≈(421,942), directly under Duplicate. ⚠ Click Duplicate exactly.
4. **Click Duplicate:** the new draft folder **`0915-copy`** appeared on the first 1 s poll
   (16 folders). `layers.py 0915-copy` shows the same state as `0915`: blurred-room main copy +
   muted cut-out overlay + stabilized desk, 30.0 s. The `0915` draft mtime is unchanged
   (01:55:20.315).
   - Filtered `draft_diff.py` of `0915` → `0915-copy`: **no differences** (`draft-baseline.json`).
   - ⚠ **The duplicate keeps the source's draft mtime** (both 01:55:20.315). For scope checks on the
     source, diff its content against a saved copy (`draft-0915-source.json`) instead of relying on
     mtime alone.
   - A "Copied" toast appears. The new card is **first** in Projects ≈(383,793) and `0915` moves
     to second ≈(566,793) (`02-after-duplicate.png`).

### B. Open the copy and import the logo (2026-09-15)
1. Click the `0915-copy` card. `MainWindow` appears after 4 s. The title bar and Details panel both
   read **0915-copy**; the state is identical (`03-copy-opened.png`).
2. **Logo file baseline:** `logo-before.txt` (mtime 2026-09-13 22:26:21.494, 22 638 B, sha256
   DE5C…0597), used to prove afterwards that CapCut didn't write to the client project.

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

## User choices (2026-09-15)
- **Project:** "Duplicate of 0915 (Recommended)". A CapCut Duplicate of the approved rung-13
  project, so `0915` itself stays untouched. The talk→desk cut at 00:15 is the transition point.
- **Logo:** "Check the Yousef AI logo in the downloads, or you can find the Yousef AI logos in
  yousef-omar-landing project in E:\client-projects\yousef-omar-landing\public\brand. If you didn't
  find them go with any text brand mark". Search those two places read-only; import the chosen file
  natively (Ctrl+I); fall back to a Text brand mark.
  - **Candidates found (read-only, `evidence/2026-09-15/cap14/logo-candidates.png`):**
    - Downloads: `lockup-yousef-ai-removebg-preview.png`, `lockup-yousef-ai-on-accent-removebg-preview.png`,
      `lockup-yousef-ai-cream-on-ink-removebg-preview.png` (661×377 RGBA, ≈96 % transparent)
    - `public/brand`:
      - `logo-cream-tight.png` / `logo-ink-tight.png` (386×211, ≈77 % transparent)
      - `logo-cream-on-ink.png` / `logo-ink-on-cream.png` (≈443×295, ≈86 % transparent)
      - `monogram-app-icon.png` (708², 4.7 % transparent)
      - `monogram-accent-square`, `monogram-ink-on-cream`, `monogram-knockout`,
        `monogram-yousef-ai-on-accent`: fully opaque, so they are not corner overlays
  - **Chosen: `E:\client-projects\yousef-omar-landing\public\brand\logo-ink-tight.png`** (#7).
    - It is the official brand file, transparent and tightly cropped: ink wordmark with the blue
      accent dots.
    - Both sections have light walls (a cream blurred room and a white/purple desk wall), where
      the cream variants would disappear.
    - The Downloads lockups are lower-quality "removebg-preview" exports.
    - Imported natively by path, read-only. The project's "Imported media: Stay in original
      location" setting means CapCut only references the file and never writes to the client
      project.
- **Transition:** "Subtle free (Recommended)": a free dissolve/mix-type card, default duration; skip
  Pro diamonds.
- **Colour:** "Pro Auto adjust": Inspector Adjust ▸ Auto adjust (Pro). Stop if a cost or credit
  prompt appears.

## Open questions for the user
- None yet.
