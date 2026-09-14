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
3. **Import** (rung-3 route):
   - `key ctrl+i`
   - `wait-for --type Edit --id 1148 --depth 30`: present after 2 s
   - `act set-value --type Edit --id 1148 --value <logo path>`
   - `act invoke --id 1 --name Open`

   **Agent-verified:**
   - The dialog closes and `draft_meta_info.json` lists `logo-ink-tight`.
   - A media card **"logo-ink-tight.png"** appears at ≈(382,411), selected. The player shows
     **"Previewing — Image"** 00:00:05:00, so a still image defaults to 5 s (`04-logo-imported.png`).
   - The transparent areas preview as black in the media preview only.
   - The logo file is re-hashed and **unchanged** (brand folder still 9 files).
4. **Put the logo on its own top overlay track:** `drag 382 411 236 662 --steps 40 --hold 0.4`,
   from the media card into the empty area above the existing overlay row (y≈745) at the 00:00 x.
   **Agent-verified (`layers.py 0915-copy`):**
   - a new **track 2** (`type` video, `flag` 2 = overlay, `attribute` 0), stacked above the
     cut-out overlay (track 1)
   - one segment **0.000 → 5.000 s**, source 0, on a new material (`-ink-tight.png`)
   - helper materials 3 → 4 (canvases, colors, placeholder_infos, sound_channel_mappings,
     speeds, videos, vocal_separations); duration stays 30.0 s
   - tracks 0 and 1 unchanged

   **Observed** (`05-logo-dropped.png`):
   - The logo clip is auto-selected on the **top row y≈745** (x≈230–438 = 0–5 s).
   - The rows shift down: cut-out overlay **y≈812**, main track **y≈895**.
   - The inspector shows Video ▸ Basic (Scale 100 %, Position 0/0) plus tabs Animation /
     Tracking / Adjust / AI stylize.
   - At 100 % the transparent PNG **fills the canvas width** (wordmark over the speaker); the
     transparency renders correctly.
5. **Extend the logo to the full 30 s:** `drag 436 745 1481 745 --steps 50 --hold 0.4`, from just
   inside the clip's right edge to the 00:30 x (the end of the desk clip).
   **Agent-verified (`logo_state.py 0915-copy --wait-dur 30`, first poll):**
   - logo segment 0 → **30.000 s**; `type` photo, 386×212; scale 1.0; transform 0/0
   - refs 6 → 7; project duration stays 30.0 s; tracks 0/1 unchanged
   - The edge snapped exactly to the timeline end (`06-logo-extended.png`).
6. **Plan for size and placement:**
   - **Scale ≈12 %:** the image is width-fit at 100 %, so ≈230 px wide on the 1920 canvas.
   - **Top-right corner with ≈40 px margins.** The real centre offset is ≈(+805, +437) px, so
     typed Position ≈ **X 1610, Y 874**. The typed unit is ½ canvas px, and positive Y = up
     (rung 10).
   - The top-right corner shows the window/wall in the talk section and a white wall in the
     desk section; the face stays clear.
7. **Set size and position** (logo clip selected, Video ▸ Basic). For each value box: click it,
   `key ctrl+a`, `type "<value>"`, `key enter`.
   - **Scale** box ≈(1792,257) → `12`.
   - **Position X** box ≈(1666,352) → `1610`.
   - **Position Y** box ≈(1788,352) → `874`.

   **Agent-verified (`logo_state.py`, first poll after each step):**
   - `clip.scale` 1.0 → **0.12**
   - `clip.transform` → **x 0.838542 (= 1610/1920), y 0.809259 (= 874/1080)**
   - duration 30.0 s; refs 7; other tracks unchanged (`draft-before-logo-place.json` is the
     baseline)
   - This confirms the typed-unit rule again: typed X = transform.x × canvas width, typed Y =
     transform.y × canvas height.

   **Observed** (`07-logo-placed.png`):
   - The dark wordmark with blue dots sits in the **top-right corner**, readable on the light wall.
   - The selection box spans ≈x 1268–1352, y 110–157 in the player (≈12 % of the canvas width),
     and the speaker's face is clear.
   - The inspector reads Scale 12 %, Position 1610 / 874.

### C. Transition at the 00:15 cut (2026-09-15)
1. **Asset tab Transitions** ≈(354,70) (`08-transitions-tab.png`):
   - Left list: Favorites, **Transitions ▾** (Trending, Classic, Whimsical, Pixel Bead (Pro),
     NEW, Hits, Overlay, Light, Camera, 3D…).
   - Search box ≈(380,127), placeholder "People are searching …".
   - Trending cards include Slight Jitter, Negati…ssolve (Pro), Dust Flurry, Shake & Flash (Pro),
     Blur Focus, B&W Ghost, and several more Pro cards.
2. **Search "dissolve":** click the search box, then `type "dissolve"`, Enter, and wait ≈9 s
   (`09-transitions-dissolve.png`). The first rows are:
   - **Dissolve** (Pro diamond)
   - Dissolve II, Light Fade
   - Negati…ssolve (Pro)
   - **Cross Fade** ≈(360,360), no diamond
   - Dissolve III
   - a third row with one more Pro card

   **Chosen: Cross Fade.** It is the plainest free dissolve, matching "Subtle free
   (Recommended)".
3. **Baseline:** `draft-before-transition.json`.
4. **Drop Cross Fade on the cut:** `drag 360 360 855 895 --steps 40 --hold 0.4`, from the card
   to the talk/desk boundary on the main track (00:15 = x≈855 at ≈41.7 px/s, main row y≈895).
   - No dialog; the window list is unchanged.
   - **Agent-verified** (`diff-transition.txt`, 23 filtered lines):
     - **+`materials.transitions[0]`**: `name` **Cross Fade**, `type` transition, `category_name`
       Transitions, **`duration` 2 000 000 µs (2.0 s default)**, **`is_overlap` true**,
       `resource_id`/`effect_id` 7655002527276076308, `platform` all
     - the **left (talk) segment**'s `extra_material_refs` gains the transition id (refs 8 → 9; it
       is inserted at index 3, so the later refs shift)
     - a +1 `material_animations` helper
     - duration stays **30.0 s**; both main segments keep their target and source ranges (the
       overlap does not shorten the timeline in the draft)
     - overlay tracks unchanged
   - **Observed** (`10-transition-dropped.png`):
     - A highlighted transition block with a ⋈ icon spans the cut on the main track (≈x 812–898 =
       14–16 s, centred on 00:15).
     - The inspector switches to **Transition ▸ Transition parameters**: Name Cross Fade, a
       **Duration** slider + box **2.0s**, a reset button, and an **"Apply to all"** button
       (bottom right; not clicked, it would add the transition to every cut).
     - The logo is visible top-right in the player.
5. **Frames around the cut** (ruler clicks x≈792/834/876/917 land on 13:14, 14:14, 15:14, 16:14;
   `11-xfade-*.png`):
   - 13:14 and 14:14 show the talk section: sharp cut-out over the blurred room, logo readable
     top-right. **No visible desk image mixed in at 14:14**, so the blend is checked at denser
     points next.
   - 15:14 and 16:14 show the desk section, pillarboxed.
   - ⚠ **Logo legibility:** in the desk section the top-right corner is the **black pillarbox**, so
     the dark ink wordmark is barely visible (only the blue dots stand out).
   - ⚠ **Overlay pop:** the cut-out overlay (track 1) ends hard at 15:00. The main-track Cross Fade
     cannot fade it, so the sharp speaker disappears abruptly at the cut.
   - **Denser frames** (x≈846/851/859/864 → 14:23, 15:00, 15:00, 15:06; `14-xfade-near-*.png`;
     the ruler snaps to the cut at 855):
     - **The blend renders in the paused preview:**
       - 14:23: the desk image is faintly mixed into the background, while the sharp cut-out
         speaker stays fully opaque in front.
       - 15:00: a strong mix. The cut-out overlay has already ended; the desk and the blurred
         room are ghosted together.
       - 15:06: desk-dominant with a faint ghost of the talk (shirt text).
       - At 14:14 and 15:14 no mix is visible, so the visible blend is concentrated within about
         ±0.5 s of the cut, even though `duration` is 2.0 s.
     - **Both artifacts confirmed.** The overlay pops (opaque speaker over a half-faded background,
       then gone at 15:00). The logo fades into the dark pillarbox from about 15:00.
6. **Undo/redo gate (agent-verified):**
   - The poll checks for `"Cross Fade"` in the draft text (PowerShell `Select-String`, no Python
     quoting).
   - Ctrl+Z → absent on the first poll; the logo guard is unchanged (scale 0.12, transform
     0.8385 / 0.8093).
   - Ctrl+Shift+Z → present on the first poll.
   - Diff vs `draft-after-transition.json`: **no differences** (`diff-xfade-gate.txt` is empty).
   - The transition is a single undo step.

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

- **Polish fixes found during verification:** "Fix both (Recommended)".
  1. Add a short **Fade out** Out-animation to the cut-out overlay clip (track 1, 0–15 s), so it
     dissolves with the Cross Fade instead of popping at 00:15.
  2. Fill the desk clip's black pillarbox with **Canvas ▸ Blur** (Video ▸ Basic ▸ Canvas), so the
     dark logo reads in the desk section.

## Open questions for the user
- None yet.
