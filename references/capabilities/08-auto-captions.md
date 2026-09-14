# Capability 08: Auto captions + styling

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Consent:** "Approve, start Cap 8". The option text said captions are Pro and may use credits,
  as in rungs 3–5.
- **Practice project:** `0914 (1)`, `VID_20260623_152043.mp4` with the rung-3 pause removed.
  112.9 s, 2 segments, Egyptian Arabic talking head. Short, so generation is quick.
- **Evidence:** `evidence/2026-09-14/cap8/`

## Goal
Generate CapCut's Auto captions for the talking-head take (language stated) and give them one
readable style: font/size, colour, stroke or background, and position in the lower third. Apply it
to every caption. Spot-check timing against the speech, fix at least one caption error natively,
and record the credit/Pro gating and what options exist for speaker-identified captions.

## Preconditions
- Rungs 0–7 approved.
- Tools reused:
  - Captions tab → Auto captions → Generate, and the `LVLoadingDialog` "Generating captions... N%"
    wait (rung 4)
  - `draft_inspect.py words` for per-word timings (rungs 4–5)
  - clip selection, ↓ cut points, ruler + arrows (rungs 1–2)

## Plan
1. **Generate:** open `0914 (1)` and go to Captions → Auto captions. Record every option (spoken
   language list, bilingual, filler words, anything about speakers), keep Auto detect or pick
   Arabic, then Generate. Wait on the loading window.
2. **Map styling:** select a caption and record the inspector tabs (Text / Basic / Presets /
   Bubble / Effects / Animation…) and whether edits apply to all captions or only one ("Apply to
   all", caption track selection).
3. **Style:** one preset or a manual style (e.g. white text, black stroke, bold, larger size, lower
   third). Verify in the draft (`materials.texts[].content` styles, `text_templates`, clip
   transform) and on the player.
4. **Timing spot-check:** 3 captions. Compare word timings with the transcript and the frames where
   speech starts.
5. **Fix one caption error natively:** edit the text of a misrecognised word, verify in the draft.
6. **Undo/redo, save.**

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
