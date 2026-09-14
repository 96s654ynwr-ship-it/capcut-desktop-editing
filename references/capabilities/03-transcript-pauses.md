# Capability 03: Transcript editing (remove pauses and filler words)

## Status
- **Ladder status:** approved (user, 2026-09-14: "Approve, try Cap 4 on 152759")
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. Route mapped on `0914-copy`, where nothing was
  detected. Removal demonstrated on the raw take `VID_20260623_152043.mp4` in practice project
  `0914 (1)`, which is left in the cleaned state (pause removed, 112.9 s).
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
  not demonstrated yet. It needs footage with natural pauses.
- **User choice (2026-09-14):** retry on the raw take **`E:\videos\VID_20260623_152043.mp4`**
  (2:15, 1280×720, 228 MB). Import it into a **new blank agent-owned practice project** created
  with Create project. Evidence: `evidence/2026-09-14/cap3/take2/`.

### D. Setup on the raw take (executed + agent-verified 2026-09-14)
1. **Leave the previous project:** Menu ▸ Back to home page; wait for the `HomeWindow` root.
2. **New practice project:**
   - Scroll home to the top (`cc.py scroll 1000 500 10`), then click **Create project** (≈1075,145).
   - Wait for the `MainWindow` root, then `focus --maximize`.
   - CapCut auto-named the project **`0914 (1)`**, since `0914` already existed.
3. **Import:**
   - Press **Ctrl+I**; the native file dialog opens in about 2 s.
   - `act set-value --type Edit --id 1148 --value "E:\videos\VID_20260623_152043.mp4"`, then
     `act invoke --type Button --id 1 --name Open`.
   - After about 6 s the media card appears at ≈(335,217). The player surface id changes to
     `MainWindow.surface_single_resource_player` while it previews a media item.
4. **Place on the timeline:** `cc.py drag 335 217 700 840 --steps 40 --hold 0.4`.
   - Draft: 1 segment, 0 → **135.200 s** (00:02:15:06), src 0.
   - The canvas auto-set to **1920×1080**.
   - Saved about 5 s later.
5. **Run Transcript:**
   - Select the clip (click 700,830), then click the Transcript icon (≈592,598).
   - `RoughCutWindow` appeared after **12.6 s** (about 17 s total) for the 2:15 clip.
   - The draft was unchanged by the analysis.

### E. Detection result on the raw take (observed 2026-09-14)
- **Pauses tab:** **1 item, "Pauses 22.30s" at 00:00:54:23.** It is drawn as a struck-through pill
  and **ticked by default**, along with "Select all".
- **Repeats:** "No repeats identified". **Filler words:** "No filler words identified". The empty
  state text is specific per tab.
- **All tab:** transcript lines in time order, plus the pause row (ticked). This take is a gym
  clip with background music, so the transcript picked up **song lyrics**, e.g. "you're the
  reason I have to make it come true" at 01:17:03. Transcript rows are not pre-ticked, only
  detected pauses/repeats/fillers are.
- **Footer:** **Total duration** previews the result with ticked items removed. It changed from
  02:15:06 to **00:01:52:27** (135.2 − 22.3 ≈ 112.9 s). **Delete** became enabled (cyan, Pro
  diamond) once an item was ticked.
- ⚠ **Detected items come pre-ticked.** Review every tab and untick anything that shouldn't go
  before pressing Delete.

### F. Remove the pause (executed + agent-verified 2026-09-14)
1. **Action:** click **Delete** in the footer (≈1516,969 on this layout). The pause was the only
   ticked item.
2. **Result in the UI:** the `RoughCutWindow` closed by itself within 3 s, and the editor timeline
   shows two segments.
3. **Draft** (saved about 2 min after the previous marker; poll the mtime):
   - `duration 135.200 → 112.900 s`
   - `segment_count 1 → 2`
   - `[0] 0.000 → 54.767 s, src 0.000`
   - `[1] 54.767 → 112.900 s, **src 77.067**`

   The source range 54.767–77.067 s (**22.300 s**, exactly the detected pause) was removed and the
   gap closed. The new duration matches the dialog's "Total duration" preview. Helper materials
   went 1 → 2, the split shape.
4. **Undo / redo (agent-verified):**
   - **Ctrl+Z** saved about 4 s later. Diff against the pre-delete state (`after-add.json`): **No
     differences**, so the single 135.2 s segment is back.
   - **Ctrl+Shift+Z** saved about 4 s later. Diff against `after-pause-delete.json`: **No
     differences**, so the pause cut is re-applied exactly.
   - The whole Remove-filler-words operation is **one undo step**.
5. **Interpretation:** CapCut implements "remove pause" as **split at the pause start, then drop
   the pause range from the source**. The result is ordinary main-track segments (no compound clip,
   since "Create compound clip" was unticked).
- **Lesson:** a short, tightly spoken clip may have no detectable pauses. Pick footage with natural
  pauses (a raw take) for this rung, or run it on each segment of a longer take.

### G. Spot-check the cut (agent-verified 2026-09-14)
1. Click empty timeline space (1500,760) so the timeline has focus.
2. `cc.py key home` moved the timecode to **00:00:00:00**. The total now reads **00:01:52:27**.
3. `cc.py key down` (**Next cut point**) moved the playhead to **00:00:54:23**, exactly the cut
   (54.767 s).
4. `left` gave 00:00:54:22 and `right right` gave 00:00:54:24. The player frames on either side
   show **two different moments** (standing at the rack, then already on the bench with a spotter
   behind). That's a visible jump, consistent with 22.3 s removed.
5. Only **one** cut exists on this take (one pause detected), so the "3 cut points" check becomes
   this single cut.

## Wait conditions
- **Analysis:** "Analyzing… Identifying pauses…" dialog. Wait with
  `cc.py wait-for --cls RoughCutWindow --timeout 600`. It took 12.6 s for 2:15 and 7 s for a 13 s
  clip.
- **Delete:** the RoughCutWindow closes within about 3 s. The draft autosave may lag; poll the
  mtime (up to 90 s).

## Verification
- **Dialog:** pause row(s) listed with duration and start; Total duration preview = original −
  ticked items.
- **Draft diff:**
  - duration shrinks by exactly the pause length
  - a new segment starts at the pause start with `src_start` = pause end
  - no other changes besides doubled helper materials
- **Visual:** ↓ lands on the cut timecode, and the frames at cut−1 and cut+1 are different moments.
- **Undo** returns to the pre-delete draft (No differences); redo re-applies it identically.

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
