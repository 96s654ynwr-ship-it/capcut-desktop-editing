# Capability 04: Bad-take removal via transcript

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** — (in progress 2026-09-14, Claude Code)
- **Approved:** —
- **Consent:** the user said "Approve, try Cap 4 on 152759". Scan
  `E:\videos\VID_20260623_152759.mp4` (3:30, 1280×720) with Transcript. **If no repeated lines
  show up, stop and report.**
- **Practice project:** a new blank agent-owned project made with Create project (name recorded
  below).
- **Evidence:** `evidence/2026-09-14/cap4/`

## Goal
Find a line the speaker said more than once (a retake) in CapCut's transcript. Remove the bad
version natively and keep the good one. Name which take was kept, and confirm the removed range
with a draft diff.

## Preconditions
- Rungs 0–3 approved.
- Route from rung 3 reused as-is:
  1. Create project.
  2. Ctrl+I import.
  3. Drag the media card to the timeline.
  4. Select the clip.
  5. Click the Transcript toolbar icon.
  6. Wait for `RoughCutWindow` ("Remove filler words").

## Candidate native routes to test
1. **Repeats tab.** CapCut's own repeat detection. Items come pre-ticked; check what each item
   covers before pressing Delete.
2. **All tab, sentence rows.** Tick the transcript sentence(s) of the bad take and press Delete.
   This is text-based removal.
3. **Fallback without detection:** find the retake's timecodes in the All tab, then use the
   rung 1–2 tools on the timeline: split at start/end (Ctrl+B) and Backspace (ripple).

## Procedure

### A. Scan of `VID_20260623_152759.mp4` (executed 2026-09-14): no retakes, stopped as instructed
1. **Setup** reused the rung 3 route without changes:
   - Back to home page, then Create project. The new project is **`0914 (2)`**, found as the
     newest draft folder by creation time.
   - Ctrl+I → file dialog → set-value id 1148 → invoke Open.
   - Drag the media card (335,217) → (700,840). Draft: 1 segment, 0 → **209.533 s** (00:03:29:16),
     canvas 1920×1080.
2. **Transcript:** select the clip (700,830), click the Transcript icon (592,598).
   `RoughCutWindow` appeared after about **30 s** for a 3:30 clip. The draft was unchanged by the
   analysis.
3. **Result:**
   - **Repeats:** "No repeats identified".
   - **Filler words:** "No filler words identified".
   - **Pauses:** 1 item, **11.33 s at 00:00:25:00**, pre-ticked.
   - **All:** only **3 rows**, because the take is mostly gym footage with little speech:
     - an Arabic sentence at 00:00:11:20
     - the pause row
     - "Halo Makhluk Bumi" at 00:00:36:11, likely a misrecognised fragment
   - Nothing else across 5 scroll pages; the list doesn't scroll.
   - Footer Total duration preview: 00:03:18:06 (with the pause ticked).
4. **No repeated lines → stopped** per the user's instruction. Closed with **Cancel**; the
   pre-ticked pause was *not* removed. The draft was unchanged (diff against after-add: No
   differences).
5. **What rung 4 needs:** a talking-head take where the same line is said at least twice. CapCut's
   **Repeats** tab should list those. Otherwise use the All tab's sentence rows to find duplicate
   text and the timecodes to cut.

## Wait conditions
- Analysis: `cc.py wait-for --cls RoughCutWindow --timeout 900`. Expect roughly 15–40 s for 3:30.

## Verification
- **Draft diff:** the duration shrinks by the removed take's length, and the new segment's
  `src_start` equals the end of the removed range.
- **Visual:** ↓ lands on the cut, and the frames or lines on either side show the kept take
  continuing.
- **Undo** returns to the pre-delete draft.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery
Ctrl+Z, verified by a diff against the pre-delete summary.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes
Same as rung 3: `RoughCutWindow`, `RollingLoading.qml` and the native file dialog are named in
the tree. Everything else is screenshot-driven.

## Open questions for the user
