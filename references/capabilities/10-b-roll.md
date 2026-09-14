# Capability 10: B-roll / overlay track (picture-in-picture)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0914 (4)-copy` (agent-owned duplicate of `0914 (4)`). It carries the
  approved rung 4–9 edits: cuts, punch-ins, the push-in, Arabic house captions, and the opening
  title. 7:30.533.
- **Evidence:** `evidence/2026-09-14/cap10/`

## Goal
Put B-roll from `E:\videos` on an **overlay video track** above the talking head, at a stated
time and duration, in two forms:
- **cutaway:** full-frame B-roll covering the speaker while his audio continues
- **picture-in-picture:** B-roll scaled down in a corner

Then verify placement, audio, layering with the captions and title, and undo/redo.

## Preconditions
- Rungs 0–9 approved. House style (`references/house-style.md`): captions stay Arabic-only in the
  lower third. The B-roll must not hide them. Check that the caption track renders above the overlay.
- Source media stays in place (project setting "Imported media: Stay in original location"). The
  agent never copies, moves or edits files in `E:\videos`.
- The B-roll clip is chosen by the user from a contact sheet, because content choice is a taste
  decision.

## Plan
1. **Pick B-roll:** extract a frame per candidate with CapCut's bundled ffmpeg (read-only). Show a
   contact sheet, and the user chooses the clip plus where in the talk it belongs.
2. **Import:** Media ▸ Import (Ctrl+I, the rung 3 route) the chosen file into `0914 (4)-copy`.
   Verify it is in the media panel and the draft `materials.videos` gains it.
3. **Place as overlay:** playhead at the stated time, then drag or add the clip onto a **new track
   above the main video** (not inserted into the main track). Record how CapCut creates the overlay
   track, and whether the main track shifts (ripple) or stays put.
4. **Trim** the overlay to the stated duration (e.g. 3–4 s) with the rung 2 trim route.
5. **Audio:** mute the B-roll (volume 0 / track mute) so the speaker's voice continues. Verify
   `volume` in the draft.
6. **Cutaway vs PiP:**
   - cutaway: full frame (scale 100%)
   - PiP: Transform Scale ≈35–40% plus Position toward a corner clear of the captions and the
     speaker's face
   - Check frames inside the overlay for both.
7. **Layering check:** captions and the title render above the overlay (render order / track
   order).
8. **Verify:** draft diff (new video track, segment start/duration, source in/out, clip transform,
   volume), frames before / inside / after, main track unchanged. Then the undo/redo gate, Back to
   home page save, and a scope check.

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

## Open questions for the user
- Which B-roll clip, and at which moment of the talk (contact sheet first).
- Cutaway, PiP, or both.
