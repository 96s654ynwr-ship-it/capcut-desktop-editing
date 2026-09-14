# Capability 01 — Duplicate project, one split at an exact time, undo test, save

## Status
- **Ladder status:** demonstrated (awaiting user approval)
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code (Windows 10, 125% scale, CapCut maximized)
- **Approved:** —
- **Practice project:** `0914-copy`, a CapCut duplicate of `0914` (agent-created; one 23.467 s
  vertical clip `VID_20260501_223643.mp4`)
- **Evidence:** `evidence/2026-09-14/cap1/`

## Goal
Make one cut at an exact timecode on a copy of a project, prove the original project is untouched,
prove undo/redo work, and leave the copy saved with the split.

## Preconditions
- Rung 0 approved.
- CapCut is running on the home screen, maximized (`cc.py focus --maximize`).
- The source project is agent-owned. If the user names one of their own projects, duplicate it
  first. Never open the original.

## Native route (overview)
Home → right-click project card → **Duplicate** → open `<name>-copy` → click the timeline ruler at
the target time → fine-tune with ←/→ while reading the player timecode → **Ctrl+B** (Split) →
Ctrl+Z / Ctrl+Shift+Z → **Menu ▸ Back to home page** (forces save) → diff.

## Procedure

### A. Record the original's state
1. **Action:** `draft_inspect.py summary <source> --json evidence/.../source-before.json`, and note
   `draft_content.json` modification time.
   **Why:** proves later that the duplicate didn't touch the source.
   **Caution:** if the source was open and browsed earlier, save it first (Back to home page). The
   on-disk draft can lag the in-memory one. See project-safety rule 5.

### B. Duplicate via CapCut (executed + agent-verified 2026-09-14)
2. **Action:** on the home screen, scroll the main area down until the Projects row shows card
   names (`cc.py scroll 1000 700 -5`), then take a grid screenshot.
   **Control:** landmark. The project card thumbnail shows its name and "size | duration" below it.
   The newest project is first.
3. **Action:** right-click the card thumbnail centre (`cc.py click x y --right`).
   **Expect:** a menu opens *inside* the home window (no new tree window) with **Upload / Rename /
   Duplicate / Delete**.
4. **Action:** take a new screenshot of the menu, then left-click the **vertical centre of
   Duplicate**.
   ⚠ **Delete is the next row down, about 40 px away.** Never press Backspace on the home screen.
   **Expect:** within about 4 s a new card `<name>-copy` appears first in Projects, and
   `draft_inspect.py list` shows the `<name>-copy` folder with the same duration.
5. **Verify:** the source's `draft_content.json` mtime is unchanged.
   2026-09-14: `0914` stayed at 11:17:12, and the duplicate appeared at 11:19:39.

### C. Open the copy (executed 2026-09-14)
6. **Action:** left-click the `<name>-copy` card thumbnail.
   **Wait:** poll `cc.py tree --depth 0` until the root is `MainWindow` (about 3–5 s), then
   `focus --maximize`.
   **Expect:** the top-bar title and the Details inspector's **Name** both read `<name>-copy`.

### D. Place the playhead at the exact time (in progress)
7. **Action:** grid-screenshot the ruler strip (`screenshot --grid --step 50 --region
   0,540,1000,720`). Read the x of the `|00:00` and `|00:05`/`|00:10` tick marks and compute
   px/second. The scale depends on timeline zoom: on 2026-09-14, 00:00 = x 228, 00:05 = 495,
   00:10 = 762, so about 53.4 px/s (≈1.8 px/frame).
8. **Action:** click the ruler at `x = x₀ + t × px_per_s` on the ruler row (y≈632 at this layout).
   **Expect:** the playhead line jumps there, and the player timecode (≈ x 510–720, y 525–555)
   updates.
   **Observed 2026-09-14:** clicking x=762 for 10 s landed at **00:00:09:29**, one frame early.
   A click is accurate to about ±2 frames at this zoom. The playhead line sits on the `|00:10`
   tick. The clip was not selected, and the ruler click doesn't select it.
9. **Action:** fine-tune with `cc.py key left` / `right`. Each press is 1 frame (listed shortcut).
   Re-read the timecode after each small batch until it equals the target.
   **Read the timecode** by zooming into `--region 500,520,760,560`. The format is
   `HH:MM:SS:FF` (frames, 30 fps here), so `09:29` is the last frame before `10:00`.
   **Observed 2026-09-14:** one `cc.py key right` moved the playhead from 00:00:09:29 to
   **00:00:10:00**, confirmed by zoomed timecode. → is +1 frame (agent-verified). Keys reached the
   timeline after `cc.py focus` confirmed foreground, with focus left there by the ruler click.

### E. Split (in progress)
10. **Action:** select the clip by left-clicking its body **away from the playhead** (e.g. 300+ px
    to the right of it). Then zoom into the timecode again to confirm the selection click didn't
    move the playhead.
    **Observed 2026-09-14:**
    - Clicking the clip body at x=1100 selected it (white border) and left the timecode at
      00:00:10:00.
    - Selecting by clicking does not move the playhead.
    - The timeline toolbar's undo arrow became active.
11. **Action:** `cc.py key ctrl+b` (Split).
    **Result (agent-verified 2026-09-14):**
    - **Timeline:** two clips side by side, labelled `…mp4 00:00:10:00` and `…mp4 00:00:13:14`,
      with the boundary exactly on the playhead line. The right-hand clip stayed selected.
    - **Autosave:** the top-bar "Auto saved" changed to 11:24:10, about 2 s after the keypress,
      and `draft_content.json` mtime matched.
    - **Draft diff** vs pre-split:
      - `segment_count 1 → 2`
      - segment 0 `duration 23.467s → 10.000s` (src_duration likewise)
      - a new segment `10.000s → 23.467s`
      - per-segment helper materials doubled (canvases, speeds, sound_channel_mappings,
        vocal_separations, placeholder_infos, material_colors, hsl, videos: 1 → 2)

      This is the expected shape of a split, not an unintended change.

### F. Undo / redo test (agent-verified 2026-09-14)
12. **Action:** `cc.py key ctrl+z`.
    **Expect:** the timeline shows one clip again.
    **Wait** for autosave: poll `draft_content.json` mtime until it changes (took about 70 s
    here, 11:24:10 → 11:25:20; the autosave cadence varies).
    **Verify:** `draft_inspect.py diff <pre-split.json> <after-undo.json>` shows **No
    differences**, so even the helper materials are removed.
13. **Action:** `cc.py key ctrl+shift+z` (redo; CapCut labels it "Reset" in the shortcut list).
    **Expect:** the two clips are back.
    **Wait** for autosave (3 s here).
    **Verify:** the diff is identical to step 11's.

### G. Save and leave (agent-verified 2026-09-14)
14. **Action:** Menu (≈140,22) → **Back to home page** (≈183,303). Take a new screenshot of the
    open menu before clicking.
    **Expect:** within about 5 s the tree root is `HomeWindow`, and the draft mtime updates
    (11:25:28).
15. **Verify** the final state with `draft_inspect.py summary <copy>`:
    - `[0] 00:00:00:00 → 00:00:10:00, src@00:00:00:00`
    - `[1] 00:00:10:00 → 00:00:23:14, src@00:00:10:00`

    Then diff against pre-split (the split shape, nothing else), and confirm the source project's
    mtime is unchanged (`0914` still 11:17:12).

## Wait conditions
- **Duplicate:** new card appears in about 4 s.
- **Opening the editor:** `MainWindow` tree root in about 3–5 s.
- **Autosave after an edit:** anywhere from about 2 s to about 70 s. Poll the
  `draft_content.json` mtime (timeout 40–90 s) rather than sleeping a fixed time. The top bar's
  "Auto saved: HH:MM:SS" label shows the same moment.
- **Back to home page:** always writes the draft. Use it when you can't wait for autosave.

## Verification
- **Visual:** zoomed timecode reads the exact target before the split. After the split there are
  two clip labels whose durations sum to the original (10:00 + 13:14 = 23:14), with the boundary
  on the playhead.
- **Draft:**
  - after split / redo / final: `segment_count 1 → 2`, segment 0 ends at the target, the new
    segment starts at the target with `src_start` = target, and helper materials double
  - after undo: **No differences** vs pre-split
- **Source untouched:** the source's `draft_content.json` mtime is unchanged since before the
  duplicate.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Target time | 00:00:10:00 | per task | user-specified |
| Ruler scale | ≈53.4 px/s | depends on timeline zoom and window width | re-measure from ticks every session |

## Undo / recovery
- **Ctrl+Z** fully reverts the split. Verified by draft diff against pre-split: No differences,
  helper materials included. **Ctrl+Shift+Z** re-applies it identically.
- **Wrong split time?** Ctrl+Z, re-place the playhead (ruler click + arrows + zoomed timecode),
  then split again.
- **Project got into a bad state?** Leave through Menu ▸ Back to home page and tell the user.
  Offer to delete the practice copy with CapCut's card menu, which needs their yes, and duplicate
  the source again. Never repair the JSON.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| Original project changed after a "view-only" session | Browsing Adjust ▸ HSL added an empty `hsl` material, saved on Back to home page | Only browse in agent-owned projects; force-save before diffing |

## Tree coverage notes
None of this procedure is exposed to UIA except the window roots (`HomeWindow` / `MainWindow`).
Cards, menus, the ruler and the timecode are all screenshot-driven.

## Open questions for the user
