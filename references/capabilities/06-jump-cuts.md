# Capability 06: Jump cuts with scale/position punch-in

## Status
- **Ladder status:** demonstrated (awaiting user approval)
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. Segments 1, 3 and 5 of `0914 (4)` punched in to 110%
  with Y −10.
- **Approved:** not yet
- **Practice project:** `0914 (4)`, the cleaned talking-head take of `VID_20260720_190542.mp4`.
  7:30.533, 1920×1080, 7 main-track segments. Joins at 122.200, 245.733, 251.867, 262.500, 359.467
  and 426.867 s.
- **Evidence:** `evidence/2026-09-14/cap6/`

## Goal
Make the cuts read as intentional jump cuts. Alternate segments get a static **punch-in** (scale up)
with a **position offset** that keeps the speaker's eye line at the same screen height across each
cut. Record the exact native route, the values used and how eye-line continuity was checked.

## Preconditions
- Rungs 0–5 approved.
- Tools reused:
  - clip selection by body click (rungs 1–2)
  - ↓ next cut point and ←/→ frames (rungs 1–3)
  - draft verification (`draft_inspect.py summary`: `clip.scale`, `clip.pos`)

## Plan
1. **Map the inspector Transform controls** in the maximized layout: Scale stepper/field, Uniform
   scale, Position X/Y fields. Find out how typed values are committed (Enter / click away) and
   what units Position uses. Verify each against the draft (`clip.scale`, `clip.transform`).
2. **Choose values from the footage:**
   - Read the eye height in a player frame.
   - Pick a punch-in (start at **110%**).
   - Compute the Y offset that keeps the eyes where they were. Scaling about the frame centre moves
     a point at height *y* to *cy + (y − cy) × s*, so the shift needed is −(y − cy)(s − 1) in
     canvas units.
3. **Apply to alternating segments** (2nd, 4th, 6th, …). Leave the others at 100%.
4. **Verify:**
   - Draft: scale/position on exactly the intended segments, nothing else changed.
   - Screenshots of the frames either side of each punched cut (↓ to the cut, ← / →) to check the
     eye line.
   - Undo/redo of one change, then save.

## Procedure

### A. Inspector Transform controls, maximized layout (observed 2026-09-14)
- **Open the project:** home card `0914 (4)` was first at ≈(383,683). Card names were read before
  clicking, and the title bar confirmed the project.
- **Select a clip:** Shift+Z (fit), then click the clip body. Segment 1 (122.2–245.7 s) at x≈762,
  y 830 got a white border, and the inspector showed **Video ▸ Basic ▸ Transform**.
- **Controls** (screen coords; not in the UIA tree, so drive them by click + keyboard):

  | Control | Position | Notes |
  |---|---|---|
  | Transform reset ↺ | ≈(1830,193) | |
  | Scale slider | y≈257 | value box **"100%"** at ≈(1792,257); ▲▼ stepper ≈(1837,257); keyframe ◇ ≈(1872,257) |
  | Uniform scale | ≈(1870,305) | toggle, ON |
  | Position X | ≈(1666,352) | value box, with stepper |
  | Position Y | ≈(1787,352) | value box, with stepper; keyframe ◇ ≈(1872,352) |
  | Rotate | ≈(1652,399) | "0.00°" |
  | Alignment buttons | y≈445, x≈1480–1800 | a row of them |
  | Blend | ≈(1470,515) | checkbox |

- **Player video surface** for frame captures: tree id `MainWindow.surface_main`, rect
  **536,107 → 1419,474**.
- **The player shows the frame under the playhead.** At the project end the speaker is out of
  frame, so move the playhead onto a join (Home, then ↓) before judging the eye line.

### B. Scale punch-in on one segment (agent-verified 2026-09-14)
1. **Frame the check:** click empty timeline space, then **Home**, then **↓**. The playhead lands on
   join 1 (00:02:02:06, first frame of segment 1). **←** gives 00:02:02:05, the last frame of
   segment 0. Capture the player surface `--region 536,107,1419,474` at full resolution for each.
2. **Re-select the segment:** click its body (x≈762, y 830). The playhead doesn't move.
3. **Set Scale:** click the Scale value box (≈1792,257), then `key ctrl+a`, then
   `type "110" --enter`.
   - **Enter commits:** the draft saved immediately and the box reads **110%**.
   - Draft diff: only segment 1's `clip.scale` changed, 1.0 → 1.1.
   - The diff also listed `src_duration` "changes" on two other segments with identical displayed
     values. That's float re-serialisation noise from CapCut, not a real change.
4. **Measurements** (screen px):
   - Displayed 1920×1080 frame ≈ x 636 → 1318 (682 px wide, ≈0.355 px per canvas px), centre
     ≈ (977, 299).
   - Eyes: segment 0 last frame ≈ y 273; segment 1 first frame at 100% ≈ y 270; at 110% ≈ **y 266**.
     The formula cy + (y − cy)·s = 299 + (270 − 299)·1.1 = 267.1 predicts that.
   - The speaker's eyes sit near frame centre, so a 110% punch-in only lifts the eye line about
     3–4 screen px (≈10 canvas px) and shifts it about 3 px left.

### C. Position units (agent-verified 2026-09-14)
- **Route:** click the Position Y value box (≈1787,352), then `ctrl+a`, then `type "-10" --enter`.
  Enter commits; the draft saved immediately.
- **Draft:** segment 1 `clip.pos.y` changed 0 → **−0.009259259 = −10 / 1080**. Nothing else changed.
- **Units:** the inspector's Position is in **canvas pixels**. The draft stores
  `pos.y = value / canvas_height` (1080 here). Presumably `pos.x = value / canvas_width`; verify
  before relying on it.
- **Confirmed at a larger value:** Position Y **−100** stored `pos.y = −0.0925926 = −100 / 1080`.
  The direction (whether negative moves the picture up or down) is read from the frame
  captured at −100, because a 10 px shift is too small to judge by eye.
- **Direction (agent-verified):** at 110% with Y 0 the eyes were at ≈y 266 screen px. At **Y −100**
  they moved to ≈**y 300**, about 34 screen px ≈ 96 canvas px **down**.
  - **Negative Position Y moves the picture down** (CapCut's Y axis points up).
  - To lower the eye line after a punch-in, use a negative Y.

### D. Choosing the eye-line correction
- **Formula:** a punch-in about the frame centre moves the eyes by (y_eye − cy)·(s − 1) canvas px.
  Here y_eye − cy ≈ (270 − 299) / 0.355 ≈ −82 canvas px, so at s = 1.1 the eyes rise ≈8 canvas px.
  Restoring them needs **Y ≈ −8 → −10**. The Y offset scales with how far the eyes sit from centre.
- The last frame of segment 0 had the eyes ≈3 screen px lower again (≈y 273). That's natural head
  movement between takes, not something to correct per cut.
- **Chosen values for this static tripod shot:** Scale **110%**, Position Y **−10**, X **0**. These
  are shot-specific: re-measure the eye height for other footage.

### E. Apply to alternating segments (agent-verified 2026-09-14)
- **Pattern:** punch segments **1, 3, 5** (the 2nd, 4th and 6th clips). Segments 0, 2, 4 and 6
  stay at 100%. Every join then cuts between a wide and a punched framing.
- **Per segment:**
  1. Shift+Z (fit), then click the clip body at its centre, at x = 232 + t_mid × (1297 / duration).
     With 450.533 s: segment 1 ≈ 762, segment 3 ≈ 972, segment 5 ≈ 1364.
     Segment 3 is only 10.6 s ≈ 30 px wide at fit zoom, so aim at its centre.
  2. **Gate:** read the segment's `clip.scale` from the draft before editing. It must be 1.0, which
     proves the click selected an unpunched clip and not a neighbour.
  3. Scale box (≈1792,257), then `ctrl+a`, then `type "110" --enter`. Wait for the draft save, then
     check this segment's scale is 1.1.
  4. Position Y box (≈1787,352), then `ctrl+a`, then `type "-10" --enter`. Wait for the save, then
     check `pos.y = −10/1080` and `pos.x = 0`.
- **Draft diff against baseline:** exactly three `clip` changes, on segments at 122.200, 251.867
  and 359.467 s (scale 1.0 → 1.1, pos.y 0 → −0.009259). The only other entries are
  float-noise `src_duration` lines with identical values.
- **Inspector values commit on Enter** in both boxes. No click-away was needed.

### F. Verification (agent-verified 2026-09-14)
- **Frames at every join.** For each join k (1–6): click empty timeline space, then Home, then
  `key down --repeat k`. Capture the first frame after the join, then ←, then the last frame
  before. Evidence is in `evidence/2026-09-14/cap6/joins/`. Timecodes confirmed the joins, e.g.
  join 1 = 00:02:02:06, join 3 = 00:04:11:26, join 5 = 00:05:59:14.
- **Eye line** (screen y of the eyes, player at ≈0.355 px per canvas px):

  | Join | Cut | Before | After |
  |---|---|---|---|
  | 1 | wide → punched | ≈273 | ≈270 |
  | 3 | wide → punched | ≈270 | ≈262 (head tilted down while reading) |
  | 5 | wide → punched | ≈262 | ≈265 |

  Every cut is within ≈±8 screen px (≈±22 canvas px). What difference remains comes from natural
  head movement, not the framing.
- **Framing change is visible on every punched join:** the window, mirror and chair are larger and
  shifted outward, so the cut reads as a deliberate jump cut rather than a glitch.
- **No exposed borders.** At 110% the picture overflows by 54 canvas px top and bottom, and the
  −10 px Y offset stays well inside that margin. No black edges showed in any capture.
- **Undo / redo (last change, segment 5 Y −10):**
  - **Ctrl+Z:** diff showed exactly one change, segment 5 `pos.y −0.009259 → 0` (scale stayed 1.1).
    Each field edit is its own undo step.
  - **Ctrl+Shift+Z:** diff against `after-punches.json`: **No differences**.
- **Saved:** Menu ▸ Back to home page, then diff: **No differences** on disk.
- **Scope:** the user's projects (0707, 0720, 0728, the Arabic-titled one) have unchanged mtimes.

## Parameters (rung 6)
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Punch-in scale | 110% | style default (105–115% typical) | tighter reads stronger, but costs resolution; 1080p source at 110% is still sharp |
| Position Y | −10 (canvas px) | **shot-specific** | −(y_eye − cy)·(s − 1); here eyes ≈82 px above centre |
| Position X | 0 | shot-specific | offset only if the speaker is off-centre |
| Which segments | alternate (1, 3, 5) | style default | every join alternates wide ↔ punched |

## Failure modes seen (rung 6)
| Symptom | Cause | Recovery |
|---|---|---|
| Player showed only the chair and no speaker | playhead parked at the end of the timeline | Home, then ↓ to a join before judging frames |
| Diff listed `src_duration` "changes" with identical values | CapCut float re-serialisation | ignore when the displayed values are identical |
| Ctrl+Z undid only the Y change, not the scale | each committed field edit is a separate undo step | press Ctrl+Z once per field to revert a whole punch-in |

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
