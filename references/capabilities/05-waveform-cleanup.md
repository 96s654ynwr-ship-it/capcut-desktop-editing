# Capability 05: Waveform / manual cleanup pass

## Status
- **Ladder status:** approved (user, 2026-09-14: "Approve + reusable script")
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. Five longest silences tightened in practice project
  `0914 (4)` (473.433 → 450.533 s).
- **Approved:** 2026-09-14
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

### C. Result of the scripted pass (agent-verified 2026-09-14, 13:35:28 → 13:37:59, ≈2.5 min)
- **Captions:** undone first. The timeline was confirmed back at baseline (2 segments, 473.433 s)
  before any cut.
- **Exact placement:**
  - The first measuring split landed 1–57 frames off target: ruler clicks at fit zoom land about
    ±2 s off.
  - After one arrow correction, the second measuring split was **exact every time**. No attempt
    needed a third pass.
- **Each W checkpoint passed** (duration delta and resume source both within 1 frame):

  | Gap (timeline) | Removed | Duration after | Join resumes src |
  |---|---|---|---|
  | 446.967 → 449.767 | 2.800 s | 470.633 | 499.800 |
  | 375.200 → 379.567 | 4.367 s | 466.267 | 429.600 |
  | 274.300 → 278.233 | 3.933 s | 462.333 | 328.267 |
  | 254.500 → 263.667 | 9.167 s | 453.167 | 313.700 |
  | 122.200 → 124.833 | 2.633 s | 450.533 | 171.767 |

- **Final:** **7 segments, 450.533 s** (−22.900 s, matching the prediction exactly).
- **W + main track magnet = ripple trim:** W removed the selected clip's part right of the playhead
  (up to the split at the gap end), and the following clips slid left. There's no separate delete
  of a small piece, so tiny pieces never need clicking.
- **Final segments:**

  | Timeline range | Source start |
  |---|---|
  | 0 → 122.200 | 46.933 |
  | 122.200 → 245.733 | 171.767 |
  | 245.733 → 251.867 | 298.400 |
  | 251.867 → 262.500 | 313.700 |
  | 262.500 → 359.467 | 328.267 |
  | 359.467 → 426.867 | 429.600 |
  | 426.867 → 450.533 | 499.800 |

  The 245.733 join is rung 4's cut, shifted by −2.633.
- **Undo / redo of the last W (agent-verified):**
  - **Ctrl+Z:** duration 450.533 → 453.167, and only the 02:02 gap came back. Segment 0 extended to
    124.833 and every later segment shifted +2.633 s. Its empty `material_animations` ref was
    removed too.
  - **Ctrl+Shift+Z:** diff against final: **No differences**. Each W trim is one undo step.
- **Saved:** Menu ▸ Back to home page, then diff against final: **No differences** on disk.
- **Scope:** the user's projects (0707, 0720, 0728, the Arabic-titled one) have unchanged
  mtimes.

### Reusable procedure: `scripts/tighten_gaps.py` (added after approval, 2026-09-14)
The one-off `evidence/…/cap5/cut_gaps.py` that demonstrated this rung is now a parameterised skill
script. It runs the same verified steps.

1. **Precondition:** the project is open in the editor, maximized and in the Default layout, and it
   has **Auto captions**. Generating them is a Pro feature that may use credits, so do it only with
   the user's consent. The captions must be the **last action**.
2. **Plan first:** `tighten_gaps.py --project "<name>" --min 0.6 --keep 0.125 --count 5 --dry-run`.
   This reads the draft only and prints each cut, the words either side and the expected final
   duration. Show the plan to the user when the scope isn't agreed yet.
3. **Run:** add `--undo-captions` (and `--all` instead of `--count N` for every qualifying gap). The
   script:
   - undoes the captions with one Ctrl+Z and checks that the text track is gone and the video
     segments are unchanged
   - confirms **this** project's draft saved, so the named project is really the one open
   - removes gaps latest-first, using the measuring-split placement plus W, with a
     duration/resume-source check after each cut
   - aborts on anything unexpected
4. **Log:** `evidence/<date>/tighten_gaps/<project>-HHMMSS.json`.
5. **Other layouts:** override `--fit-x0 --fit-span --ruler-y --clip-y --empty` after measuring a
   grid screenshot. The measuring loop corrects small errors, but clip-body clicks need to land
   inside the right clip.
6. **After it finishes:** use ↓ to spot-check the joins, then Menu ▸ Back to home page to force a
   save, then `draft_inspect.py summary`.

### D. Spot-check (agent-verified 2026-09-14)
- Click empty timeline space → **Home** → 00:00:00:00.
- **↓** → **00:02:02:06** (122.200, gap join) → **00:04:05:22** (245.733, rung-4 join) →
  **00:04:11:26** (251.867, join of the 9.167 s gap). All three match the draft boundaries to the
  frame.
- At the 9.167 s join: ← → 00:04:11:25 and →→ → 00:04:11:27. The frames either side are the same
  framing with a small head/hand shift, a normal talking-head jump cut. There's no black frame and
  no visible gap.
- The yellow CapCut tip bubble ("…cut long videos…") still overlaps the right part of the timecode
  readout. The playhead time on the left stays readable.

## Wait conditions (rung 5)
- **Auto captions:** ≈106 s for 7:53. Poll the draft for a non-empty `text` track.
- **Each measuring split / undo / W:** the draft saved within about 1–4 s during the scripted pass.
  `wait_save` polls the mtime with a 120 s timeout.
- **Whole 5-gap pass:** ≈2.5 min (13:35:28 → 13:37:59).

## Parameters (rung 5)
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Minimum gap considered | 0.60 s | editorial default | shorter gaps usually read as natural rhythm |
| Silence kept each side | 0.125 s (→ 0.25 s total) | editorial default | tighter feels rushed; looser leaves dead air |
| Gaps tightened | 5 longest (22.9 s) | demonstration scope | 79 candidates existed (90.6 s); ask the user how aggressive to go |
| Edit-join gaps | skipped | universal | spans a previous cut, so it isn't real silence |

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
