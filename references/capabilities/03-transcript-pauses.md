# Capability 03: Transcript editing (remove pauses and filler words)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** (in progress 2026-09-14, Claude Code)
- **Approved:** not yet
- **Credits consent:** the user said "Approve, start Cap 3 (credits OK)" on 2026-09-14. Still show
  any credit/confirmation dialog and record its text before accepting.
- **Practice project:** `0914-copy`. It has 2 segments of the 23.467 s talking-head clip
  `VID_20260501_223643.mp4`: 0–10.000 s and 10.000–23.467 s (src 10.000).
- **Evidence:** `evidence/2026-09-14/cap3/`

## Goal
Use CapCut's native **Transcript** (text-based editing) to find silences/pauses and filler words
in spoken footage, remove them natively, and prove the result with a draft diff. Record the
settings used, the before/after duration and the segment count.

## Preconditions
- Rungs 0–2 approved.
- `0914-copy` open, maximized, Default layout. Main track magnet: note its state (it was on in
  rung 2).
- The user has consented to credit use for this rung.

## Known entry points (from rung 0 mapping)
- Timeline toolbar with a clip selected → **Transcript** icon (document with sound waves, Pro
  diamond).
- Clip right-click menu → **Transcript** (Pro).
- Related: Captions tab → Auto captions has an **Identify filler words** toggle (Pro), and
  shortcut rows list "Transcript" (unassigned).

## Plan
1. Baseline draft summary.
2. Select a clip and open Transcript. **Stop at any dialog** and screenshot it: scope (clip vs
   timeline), language, credit notice.
3. Start the transcription only after reading the dialog (consent given). Wait for completion;
   record indicators and duration.
4. In the Transcript panel, find the pauses/silence and filler-word tools. Record their
   options/thresholds.
5. Apply removal. Screenshot the timeline, wait for autosave, then diff (expect more segments with
   gaps closed and a shorter duration).
6. Spot-check 3 cut points by screenshot or playback.
7. Undo and diff to baseline. Decide with the user whether to keep a cleaned version.

## Procedure

### A. Start the transcript (executed 2026-09-14)
1. **Select** a clip on the main track (clicked segment 0 body at 500,830).
2. **Click the Transcript icon** in the timeline toolbar. On the maximized layout it's the
   document-with-waves icon at ≈(592, 598), with a Pro diamond.
3. **Observed:** **no confirmation or credit dialog appeared.** Processing started immediately,
   and a named UIA window **`RollingLoading.qml`** (cls `RollingLoading_QMLTYPE_*`, about 240×258,
   centred over the player) showed up.
   ⚠ **Clicking this icon starts transcription (and any credit use) at once.** Never click it
   without the user's consent for the rung.
4. **Loading dialog:** centred over the player, with the CapCut logo, **"Analyzing…"**,
   "Identifying pauses…" and a **Cancel** button. Cancel is the only way to abort before any
   result.
5. **Completion:** the loading window closes and a large named window opens:
   **`RoughCutWindow`** (cls `RoughCutWindow_QMLTYPE_*`, rect ≈ 243,37 → 1675,992). It contains
   its own player surface (`surface_main`). On a 23 s clip it took **under about 50 s** (clicked
   ≈11:46:4x, done before 11:47:30).
   **Better wait condition:** `cc.py wait-for --cls RoughCutWindow --timeout 600 --interval 2 --depth 2`.
   The loading window may already be gone by the time you check.

### B. The "Remove filler words" window (observed 2026-09-14)
The RoughCutWindow is titled **"Remove filler words"** (title centred at the top). **Scope: only
the selected clip.** Its player and "Total duration" showed 00:00:10:00, the length of segment 0.
Running the analysis alone did **not** change the draft (diff against the cap3 baseline: No
differences).

Layout on the maximized editor at 125% (approximate screen coordinates; re-screenshot before
clicking):
- **Left:** preview player with timecode `00:00:00:00 / 00:00:10:00` and a play button.
- **Right panel, tabs:** **All** (≈1230,103), **Pauses** (≈1297,103), **Repeats** (≈1383,103),
  **Filler words** (≈1485,103). The active tab is cyan.
- **Right panel, list:**
  - a **Select all** checkbox
  - one row per detected item, each with a checkbox, the transcript text (here Arabic, the
    footage's language) and a start timecode
  - "All" listed items at 00:00:00:00, 00:00:01:08, 00:00:05:03 and 00:00:06:05
- **Bottom:**
  - a mini timeline with its own undo/redo and zoom −/slider/+
  - **Total duration: 00:00:10:00**
  - a **Create compound clip** checkbox
  - **Delete** button with a Pro diamond, disabled until items are ticked
  - **Cancel**

⚠ **Delete removes the ticked items from the clip.** Cancel closes without changes.

### C. Detection result on segment 0 (0–10 s), 2026-09-14
- **Pauses / Repeats / Filler words** tabs each showed an empty state: a scissors-between-clips
  icon, **"No invalid clips identified"**, and "Change the material and try again". Nothing to
  remove.
- **All** tab: lists the clip's **transcript sentences**, one row per sentence, with a checkbox and
  start timecode (4 rows: 00:00:00:00, 00:00:01:08, 00:00:05:03, 00:00:06:05). Ticking sentence
  rows and pressing Delete would remove speech by text. That's text-based editing (rung 4
  territory), not pause removal.
- The mini timeline at the bottom stayed empty (ruler 00:00 · 2f · 4f), even with a clip in scope.
- **Close without changes:** **Cancel** (bottom-right, ≈1615,968 on this layout). The window
  closes and the draft is unchanged.
- **Second run on segment 1 (10.000–23.467 s, 13.5 s):**
  - Selected the segment, clicked Transcript.
  - `RoughCutWindow` appeared after **7 s** (11 s including the click and settle), faster than the
    first run. Analysis results may be cached per source media.
  - The draft was unchanged afterwards.
  - **Result:** Pauses, Repeats and Filler words were again all **"No invalid clips identified"**.
    All listed 3 sentences, at 00:00:00:00, 00:00:03:03 and 00:00:07:14. Those timecodes are
    **relative to the selected clip**, not the timeline.
  - Closed with Cancel; draft unchanged.
- **Status of rung 3 on this footage:** the pause/filler route is mapped end to end up to Delete,
  but **this 23 s take has nothing to remove**. The removal step itself (tick → Delete → diff) is
  not demonstrated yet. It needs footage with natural pauses. Waiting on the user to choose footage.
- **Lesson:** a short, tightly spoken clip may have no detectable pauses. Pick footage with natural
  pauses (a raw take) for this rung, or run it on each segment of a longer take.

## Wait conditions
*(transcription progress indicators and timing to record)*

## Verification
*(per step)*

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery
Ctrl+Z, verified by diff against the cap3 baseline.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes

## Open questions for the user
