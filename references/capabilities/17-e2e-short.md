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
- Which highlight range (candidates pending).
