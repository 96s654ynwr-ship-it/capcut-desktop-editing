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
- The title text (Arabic) and whether it should come from a text template or plain text with
  animations.
