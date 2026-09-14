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
- **Transition:** "Subtle free (Recommended)": a free dissolve/mix-type card, default duration; skip
  Pro diamonds.
- **Colour:** "Pro Auto adjust": Inspector Adjust ▸ Auto adjust (Pro). Stop if a cost or credit
  prompt appears.

## Open questions for the user
- None yet.
