# Capability 07: Keyframed eased push-ins

## Status
- **Ladder status:** demonstrated (awaiting user approval)
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. Segment 4 of `0914 (4)` got an eased Scale push-in,
  100% at 00:04:22:15 → 108% at 00:05:59:13. Undo/redo verified. Saved via Menu ▸ Back to home
  page: the diff against the post-easing state showed No differences, and the diff against the
  rung-7 baseline showed exactly one change (segment 4 keyframes).
- **Scope check:** the user's projects (0707, 0720, 0728, the Arabic-titled one) have unchanged
  mtimes. `0914 (5)` (empty, created 14:26) wasn't made by this rung and wasn't touched.
- **Approved:** not yet
- **Practice project:** `0914 (4)`, the cleaned and punched talking-head take of
  `VID_20260720_190542.mp4` from rungs 4–6. 7:30.533, 1920×1080, 7 main-track segments; segments
  1, 3 and 5 carry the rung-6 static punch-in (110%, Y −10).
- **Evidence:** `evidence/2026-09-14/cap7/`

## Goal
A slow, eased push-in across one unpunched segment: Scale animates from 100% at the segment start
to about 108% near its end, with an ease so the move starts and stops gently. Record the native
keyframe route, how easing is applied, and how the keyframes appear in the draft.

## Preconditions
- Rungs 0–6 approved.
- Tools reused:
  - clip selection by body click and fit zoom (rungs 2, 6)
  - ↓ next cut point, ←/→ frames, measuring split for exact playhead placement (rungs 1, 5)
  - Inspector Transform Scale box, type + Enter (rung 6)
  - draft verification (`draft_inspect.py summary/diff`)

## Plan
1. **Pick the segment:** an unpunched one (0, 2, 4 or 6), so the push-in doesn't fight a static
   punch-in. Segment 4 (262.500 → 359.467 s, 97 s) is long enough to read at fit zoom.
2. **Map the keyframe controls:** the ◇ next to Scale, what happens when a value changes with a
   keyframe present, the keyframe panel (Alt+K), Add keyframe (Shift+Alt+K), and where easing
   lives (keyframe right-click, the panel, or the inspector).
3. **Apply:** keyframe Scale 100% at the segment start, move the playhead near the end, set 108%.
4. **Ease:** apply CapCut's ease option to the keyframes.
5. **Verify:**
   - Draft: keyframes on exactly that segment, with the stated times and values, plus the easing
     data.
   - Player frames at start, mid and end showing the scale growing.
   - Undo/redo, save.

## Procedure

### A. Open and select (agent-verified 2026-09-14)
- **Home grid moved:** after a relaunch, the Projects grid sat below the "AI-powered creative suite"
  row. Scroll the home page down (`scroll 1100 700 -5`) to reveal the card names, and read them
  before clicking. `0914 (4)` was the 2nd card at ≈(565,680), after a new `0914 (5)`.
- **Fit zoom this session:** Shift+Z put the clips on x 230 → 1528 (span 1298). Segment 4
  (262.500 → 359.467 s) spanned x ≈ 987 → 1265, so its body is at (1127, 830).
- **Clicking empty timeline space moves the playhead** to the click position. Place the playhead
  *after* that click, then re-select the clip. Clicking a clip body does not move the playhead.
- **Playhead to segment start:** click empty timeline space (1500,740), then Home, then
  `key down --repeat 4 --gap 0.3`. The player read 00:04:22:15 = 262.500 s, join 4.

### B. Scale keyframes (agent-verified 2026-09-14)
- **Inspector keyframe controls:** each Transform row ends in `‹ ◇ ›`, meaning previous keyframe /
  add or remove keyframe / next keyframe. Scale's ◇ is at ≈(1872,257) in the maximized layout
  (Position ≈(1872,352), Rotate ≈(1872,399)). The ◇ is **hollow** when the playhead isn't on a
  keyframe and **filled cyan** when it is.
- **Start keyframe:** with segment 4 selected and the playhead on its first frame, click the Scale ◇.
  - The draft saved within about 1 s. Segment 4 got `common_keyframes`:
    `[{property_type: "KFTypeScaleX", keyframe_list: [{time_offset: 328266666, values: [1.0],
    curveType: "Line", left_control/right_control: (0,0)}]}]`.
  - **`time_offset` is on the segment's SOURCE clock** in µs: segment 4's source starts at 328.267 s.
    `draft_inspect.py keyframes` converts it to timeline time.
  - Only one `KFTypeScaleX` group appears even with Uniform scale ON. Y follows X.
  - A first-use yellow tip appeared: *"Right-click the keyframe to create variable speed
    animations"*, with an **OK** button at ≈(1077,753). Click OK to dismiss it.
- **End keyframe:**
  1. Click empty timeline space, then Home, then `down --repeat 5` (to join 5 at 359.467), then
     **←**. The player read 00:05:59:13, segment 4's last frame.
  2. Re-select the clip body (1127,830).
  3. Click the Scale value box (≈1792,257), then `ctrl+a`, then `type "108" --enter`.
  - **Changing a value while the property already has a keyframe auto-adds a keyframe** at the
    playhead. The ◇ turned filled.
  - The draft gained a second `KFTypeScaleX` keyframe: `time_offset 425199999` (= 328.267 +
    96.933 s), `values [1.08]`, `curveType "Line"`.
  - `clip.scale` also changed to 1.08. It mirrors the value at the last edited keyframe; the
    keyframes drive playback.
- **Timeline markers:** a selected clip shows small diamond markers on its thumbnail strip at each
  keyframe time (y≈827).
- **Draft check:** `draft_inspect.py keyframes "0914 (4)"` printed:
  ```
  Track 0 [video] seg 4  00:04:22:15 (262.500s) -> 00:05:59:14 (359.467s)
      +   0.000s  KFTypeScaleX @ 00:04:22:15 (262.500s) = [1.0] Line L(0,0) R(0,0)
      +  96.933s  KFTypeScaleX @ 00:05:59:13 (359.433s) = [1.08] Line L(0,0) R(0,0)
  ```
  The diff against baseline showed one difference, on segment 4 only (clip scale plus keyframes).

### C. Easing (agent-verified in draft 2026-09-14)
- **Route:** with the clip selected, **right-click the keyframe marker** on the clip strip. The start
  marker sat just inside the clip's left edge at ≈(990,828). A zoom capture
  (`screenshot --region` around the clip) makes the diamonds easy to find.
- **Keyframe menu:** Ease in, Ease out, Easing, ✓ Linear, Show all presets, Show variable speed
  animation (Alt+K), Copy (Ctrl+C), Delete (Backspace).
- **Click "Easing"** (≈1055,827 with the menu opened from that marker). The draft saved within about
  1 s, and **both keyframes of the pair changed**, not only the one right-clicked:

  ```
  +   0.000s  KFTypeScaleX @ 00:04:22:15 (262.500s) = [1.0]  FreeCurveInOut L(0,0) R(4.07e+07,0)
  +  96.933s  KFTypeScaleX @ 00:05:59:13 (359.433s) = [1.08] FreeCurveInOut L(-4.07e+07,0) R(0,0)
  ```

  - `curveType` changed from `Line` to **`FreeCurveInOut`**.
  - The Bezier handles are in µs along the time axis: the start keyframe's right handle is
    +40.7 s and the end keyframe's left handle is −40.7 s, with y 0.
  - Over the 96.933 s span that is **0.42 / 0.58**, the classic ease-in-out curve
    `cubic-bezier(0.42, 0, 0.58, 1)`.
- **Expected values** (computed from those handles), used for the playback check:

  | Point in segment | Eased | Linear |
  |---|---|---|
  | 10% | 100.16% | 100.80% |
  | 25% | 101.03% | 102.00% |
  | 50% | 104.00% | 104.00% |
  | 75% | 106.97% | 106.00% |
  | 90% | 107.84% | 107.20% |
- **Applying a preset starts playback.** Right after "Easing" the player was playing from the
  keyframe: pause icon, moving timecode, live audio meter. It had run about 69 s by the time it was
  noticed. Most likely CapCut previews the preset (observed once, not re-tested).
  - **Always take a screenshot after applying a preset.** If the player shows ⏸, press **Space**
    once and confirm with two timecode captures a second apart.
  - Playback didn't change the draft (diff: No differences).

### D. Checkpoint frames (agent-verified 2026-09-14, `evidence/2026-09-14/cap7/checkpoints/`)
- **Per checkpoint:**
  1. Place the playhead: exact start/end via Home + ↓/←; ¼, ½ and ¾ via a ruler click at
     y 628, x = 230 + t × 1298 / 450.533.
  2. Re-select the clip body (1127,830).
  3. Capture `--region 536,90,1920,560 --full`, which covers the player, timecode and inspector.
- **The inspector Scale box shows the interpolated value under the playhead**, rounded to 1%. That
  makes it a cheap easing check at the ¼ and ¾ points, where eased and linear differ by about 1%.

  | Checkpoint | Timecode | Fraction | Inspector | Eased predicts | Linear predicts |
  |---|---|---|---|---|---|
  | start | 00:04:22:15 | 0 | **100%**, ◇ filled | 100 | 100 |
  | ¼ | 00:04:46:13 | 0.247 | **101%** | 101.0 | 102.0 |
  | ½ | 00:05:10:20 | 0.497 | **104%** | 104.0 | 104.0 |
  | ¾ | 00:05:34:27 | 0.747 | **107%** | 106.9 | 106.0 |
  | end | 00:05:59:13 | 1 | **108%**, ◇ filled | 108 | 108 |

- **Visual:**
  - The white selection box around the picture widens with the scale: ≈685 → 691 → 708 → 728 →
    735 screen px.
  - The window, mirror and chair visibly grow between the start and end frames.
  - At 108% the picture overflows the canvas, so no borders are exposed.
  - The speaker stays centred with Position 0,0. Face height shifts only a few px because the eyes
    sit near frame centre (see rung 6 D).

### E. Keyframe graph panel, Alt+K (observed 2026-09-14, `altk-panel.png`, `altk-zoom.png`)
- **Alt+K** with the keyframed clip selected opens an **inline panel on the timeline**, directly above
  that clip and exactly its width. It's not a separate window: `cc.py windows` showed no new
  top-level window. The same command is in the keyframe right-click menu as "Show variable speed
  animation".
- **Contents:**
  - a header "Transform ▴"
  - a row "Scale ▴", then four small curve-preset icons (≈x 1117–1192, y 702 at fit zoom), then
    `‹ ◆ ›`
  - a graph with a value axis from 0.00 to 2.00 and one line for the scale curve
  - At this axis range, a 100 → 108% move looks almost flat, so the ease isn't readable by eye
    here. Use the inspector readouts (D) and the draft handles (C) instead.
- **Hovering the preset icons** showed **no tooltip** (`altk-tooltips.png`). They're
  unidentified icons, probably the same curve presets as the right-click menu, and they weren't
  clicked.
- **While the panel is open the track moves down** by about 60 px: the clip strip went from y≈830 to
  y≈890. Close the panel (Alt+K again) before clicking clip bodies with the usual coordinates.
- Opening it didn't change the draft (diff: No differences).

### F. Undo / redo (agent-verified 2026-09-14)
- Close the Alt+K panel first (Alt+K again).
- **Ctrl+Z once:** the draft saved, and **both** keyframes went back to `Line` with (0,0) handles. The
  diff against the post-easing summary showed exactly that one change: the easing preset is a
  single undo step for the whole keyframe pair.
- **Ctrl+Shift+Z:** both returned to `FreeCurveInOut ±4.07e+07`. Diff against post-easing:
  **No differences**.
- The undo history per action: start keyframe (◇ click), end keyframe plus value (typed 108 +
  Enter), easing (menu). Ctrl+Z ×3 removes the whole push-in.

## Wait conditions
- **◇ click, value Enter, easing menu, undo, redo:** the draft saved within about 1–2 s each.
  Poll the mtime with a 90 s timeout.
- **After applying a preset:** check for auto-playback (C) before any further input.

## Verification
- `draft_inspect.py keyframes "<project>"` must list exactly two `KFTypeScaleX` keyframes on the
  intended segment, at its first and last frame, with values 1.0 / 1.08 and `FreeCurveInOut`
  handles.
- `draft_inspect.py diff <baseline> "<project>"` must show one difference, on that segment only.
- The inspector reads ≈101% at ¼ and ≈107% at ¾ (an eased curve). Linear would read 102% and 106%.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Start / end scale | 100% → 108% | style default (104–110% typical) | subtle enough not to feel like a zoom; more for short segments |
| Range | whole segment, first → last frame (96.9 s) | editorial choice | long segments give a near-imperceptible creep; for a 5–15 s segment the same 8% reads as a deliberate push |
| Easing | "Easing" (ease in-out, handles 0.42 / 0.58) | style default | starts and lands gently; Ease in / Ease out for moves that continue into or out of a cut |
| Position | 0, 0 | shot-specific | the speaker is centred; offset Y (rung 6 formula) if the eyes sit far from centre |
| Segment choice | unpunched segment 4 | style | avoid stacking on a rung-6 static punch-in unless the start value matches it (110%) |

## Undo / recovery
- Ctrl+Z steps back one action at a time: easing preset (both keyframes), then the end keyframe,
  then the start keyframe.
- To remove one keyframe, right-click its marker ▸ Delete (Backspace). Not exercised.
- Transform reset ↺ (≈1830,193) presumably clears the values too. Not exercised.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| `cc.py key down --repeat 4 --gap 250` hung past the 120 s tool timeout | `--gap` is **seconds**, not ms (250 s between presses) | kill the python process; use `--gap 0.25` |
| Only 1 of 4 ↓ presses landed (playhead on join 1) | the process above was killed mid-sequence | click empty timeline space, then Home, then ↓ again, and read the timecode before editing |
| Player was playing after choosing "Easing" | applying a curve preset starts a preview playback (observed once) | Space once; confirm two identical timecode captures |
| Diff listed `clip` changes on punched segments with identical values | CapCut float re-serialisation (1.0999999999999999 → 1.1) | fixed in `draft_inspect.py diff` (6-place rounding, 1 ms time tolerance) |
| Hovering the Alt+K panel's preset icons showed nothing | these icons have no tooltips | identify by right-click menu names instead; don't click unknown icons |
| Home card grid wasn't where it was last session | the home page scrolls; after relaunch the Projects row was lower | scroll the home page and read the card names before clicking |

## Tree coverage notes
- Nothing in this procedure was reachable through UI Automation: inspector keyframe ◇, value box,
  clip keyframe markers, keyframe right-click menu, Alt+K panel. It was all screenshot + coordinates
  + keyboard, verified through the draft.
- The keyframe right-click menu and the preview playback created no new named top-level window
  that is useful. The Alt+K panel is inline in the main window.

## Open questions for the user
- Is 100 → 108% over a whole ~97 s segment the feel you want, or should push-ins run over shorter
  stretches (e.g. the first 5–10 s after a cut, or across one sentence)?
- Which easing do you prefer by default: **Easing** (in-out, used here), **Ease in**, or **Ease out**?
- Should push-ins go on the rung-6 punched segments too (starting from 110%), or only on wide ones?
