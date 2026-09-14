# Capability 05: Waveform / manual cleanup pass

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** (in progress 2026-09-14, Claude Code)
- **Approved:** not yet
- **Consent:** "Approve, start Cap 5". The approved plan names **CapCut's detected pauses plus
  caption word timings** as the main gap-finding tools, because the waveform strip is too thin to
  read at the default track height.
- **Practice project:** `0914 (4)`, the cleaned 7:53.433 take of `VID_20260720_190542.mp4` from
  rung 4. Two segments: `[0–248.367 src 46.933]` + `[248.367–473.433 src 298.400]`.
- **Evidence:** `evidence/2026-09-14/cap5/`

## Goal
After the automatic passes, tighten the remaining breaths and dead air by hand. Decide gap by gap
what to cut, using explicit criteria (gap length, what gets kept), and verify every cut in the
draft.

## Preconditions
- Rungs 0–4 approved.
- Tools reused:
  - ruler click + arrows + Ctrl+B with draft verification (rung 1)
  - Backspace ripple (rung 2)
  - Shift+Z fit, Ctrl+= zoom (rung 4)
  - `draft_inspect.py words` on Auto captions (rung 4)

## Plan
1. **Explore whether the waveform can be made readable:** timeline toolbar display options,
   track-height controls, and a taller timeline panel. Record what exists.
2. **Find the gaps:**
   - Preferred: generate Auto captions, list every inter-word gap ≥ a threshold with word timings,
     then undo the captions.
   - Cross-check against the pauses CapCut lists in Transcript → Pauses.
3. **Set the criteria.** Default proposal: cut silences longer than **0.60 s** down to **0.25 s**,
   keeping 0.125 s after the previous word and 0.125 s before the next word. Never cut inside a
   word.
4. **Apply** to a handful of gaps (3–5), each split + delete, **latest first**, with every split
   verified in the draft.
5. **Verify:** duration shrinks by the sum of the removed pieces; ↓ spot-checks; undo/redo; save.

## Procedure

### A. Can the waveform be made readable? (explored 2026-09-14)
- **Opening the practice project:** with 10 projects the home grid wraps, 8 cards per row.
  `0914 (4)` was the first card at ≈(383,683). Card names were read before clicking; the title
  bar confirmed "0914 (4)".
- **Monitor-style icon** in the right timeline toolbar (≈1663,598): one click showed only a hover
  highlight. There was no popup, no new tree window, and the toolbar, timeline and track height
  were unchanged. It isn't a track-height or waveform control.
- **Conclusion so far:** no waveform-enlarging control found. Following the approved plan, gaps are
  found from **Auto captions word timings** (`draft_inspect.py words` / `gaps`) and cross-checked
  with Transcript → Pauses.

### B. Gap analysis from caption word timings (executed 2026-09-14)
- **Auto captions** on `0914 (4)` took ≈106 s for 7:53. They used the same route and named loading
  window as rung 4.
- **`draft_inspect.py gaps "0914 (4)" --min 0.6 --keep 0.125`** (JSON in `gaps-0.6.json`, all words
  in `words-all.json`):
  - **79 real silences ≥ 0.6 s**, totalling **90.567 s** removable while keeping 0.125 s on each
    side.
  - **+1 gap flagged `SPANS EDIT JOIN @ 248.367`** (rung 4's cut), correctly excluded.
- **Criteria for the demonstration:** tighten the **5 longest** real gaps to 0.25 s of silence (0.125
  s after the last word and 0.125 s before the next). Never cut inside a word. Process latest first.

  | Cut range | Removes | Between |
  |---|---|---|
  | 07:26:29 → 07:29:23 | 2.800 s | «واحاول» / «اوثق» |
  | 06:15:06 → 06:19:17 | 4.367 s | «هاخلي» / «ولا» |
  | 04:34:09 → 04:38:07 | 3.933 s | «وال» / «يبقى» |
  | 04:14:15 → 04:23:20 | 9.167 s | «تانية» / «يجب» |
  | 02:02:06 → 02:04:25 | 2.633 s | «و» / «بس» |

  Expected result: **473.433 → 450.533 s**.
- **Execution method:** `evidence/2026-09-14/cap5/cut_gaps.py` drives CapCut through `cc.py`
  functions. For each target time:
  1. Zoom to fit, then click the ruler (at least 4.5 s away from existing cuts, because snapping is
     on).
  2. Make a **measuring split**, read its exact time from the draft, **undo** it, and correct with
     ←/→ by the frame delta. Repeat until the measuring split lands on the target.
  3. Removal: exact split at the gap end, exact playhead at the gap start, select that clip, then
     **W**.
  4. Verify the duration dropped by exactly the gap, and that the next segment starts at the gap
     start with the source of the gap end. Otherwise abort.

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
