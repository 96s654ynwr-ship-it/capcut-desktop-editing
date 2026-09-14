# Capability 02: Timeline basics

## Status
- **Ladder status:** approved (user, 2026-09-14: "Approve, start Cap 3 (credits OK)")
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code. All six operations were verified, then undone. The
  final draft equals `baseline.json`.
- **Approved:** not yet
- **Practice project:** `0914-copy`. It starts with 2 segments of `VID_20260501_223643.mp4`:
  0–10.000 s (src 0) and 10.000–23.467 s (src 10.000).
- **Evidence:** `evidence/2026-09-14/cap2/`
- **Baseline draft summary:** `evidence/2026-09-14/cap2/baseline.json`

## Goal
Operate the timeline's basic editing controls natively, and know exactly what each one does to
the project:
- select and delete, with and without ripple (the main track magnet)
- trim to the playhead (Delete left Q / Delete right W)
- move a clip (onto an overlay track)
- add media to the timeline
- lock and mute a track

Each operation is demonstrated once, verified by screenshot and draft diff, then undone. The
next operation starts from the same baseline.

## Preconditions
- Rungs 0 and 1 approved.
- `0914-copy` is open in the editor, maximized, with the Default layout.
- Tools used from approved rungs:
  - playhead placement: ruler click + arrow keys + zoomed timecode (rung 1)
  - selecting a clip by clicking its body away from the playhead (rung 1)
  - Ctrl+Z (rung 1)

## Plan of operations (each: baseline → action → screenshot → wait for save → diff → Ctrl+Z → diff = baseline)
1. **Magnet state:** read the right-hand timeline toggles and record which one is the main track
   magnet (shortcut P) and whether it is on.
2. **Delete with ripple:** select segment 0 (0–10 s), then Backspace/Delete. Expected with magnet
   ON: segment 1 slides to 0 (duration 13.467 s). Expected with magnet OFF: a 10 s gap stays.
3. **Trim with Q / W:** playhead at 00:00:15:00 inside segment 1, segment selected, press **W**
   (Delete right). Expected: segment 1 ends at 15.000 s.
4. **Move to an overlay track:** drag segment 1 upward above the main track. Expected: a new
   video track, and the segment keeps its time.
5. **Add media:** drag the Media panel clip onto the timeline after the last segment. Expected:
   a new segment starting at 23.467 s.
6. **Track lock / mute:** click the track header's lock and speaker icons. Expected: track
   `attribute`/`flag` bits change in the draft, and clips can't be selected while locked. Undo or
   click again to restore.

## Procedure

### Common setup
- Open the practice project (home card → wait for `MainWindow` → `focus --maximize`).
- Re-measure the ruler scale from its tick labels (2026-09-14: 00:00 = x 228, 00:05 = 495, 00:10 = 762, 00:15 = 1030, 00:20 = 1297 → ≈53.4 px/s). Clip bodies sit on the main track at y ≈ 800–860 (centre ≈ 830).
- **Safety gate before any Backspace/Delete:** `cc.py tree --depth 0` root must be `MainWindow` (never `HomeWindow` — Backspace there deletes a project card) and `cc.py focus` must report `"foreground": true`.

### Op 2 — Delete a segment (ripple) — agent-verified 2026-09-14
1. **Select:** left-click the segment body away from the playhead (segment 0 at x=500, y=830).
2. **Delete:** `cc.py key backspace` (listed shortcut "Delete ← Backspace").
3. **Result (magnet ON — the default found in this project):** the gap closed — segment 1 slid from 10.000 s to **0.000 s** keeping its source offset (src@10.000). Draft diff vs baseline: `duration 23.467 → 13.467`, `segment_count 2 → 1`, removed segment 0–10.000, remaining segment `start 10.000 → 0.000`, helper materials 2 → 1. Autosave wrote the change within seconds (draft mtime 11:33:06).
4. **Undo:** `cc.py key ctrl+z` → saved 4 s later; diff vs baseline **No differences**.
5. **Takeaway:** with the main track magnet on, deleting on the main track **ripples** (closes the gap). To leave a gap you must turn the magnet off first (shortcut **P**) — see Op 2b.

### Op 2b: Identify and toggle the main track magnet (agent-verified 2026-09-14)
1. Zoom into the right-hand toggles with `cc.py screenshot --grid --step 50 --region 1340,560,1920,620`.
2. `cc.py key p` (timeline focused) toggles the **first cyan toggle (≈x 1422)**, which turns
   **grey = off**. Pressing P again turns it back to **cyan = on**.
3. No toast appears. The magnet state is read from the icon colour alone.
4. Pressing P twice left the draft identical to the baseline, but the draft wasn't re-saved in
   between. It's still unknown whether the magnet state is stored per project. Always read the
   icon at session start and never assume.
5. **Leave the magnet as found:** it's an editor preference the user relies on.

### Op 3: Trim to the playhead with W (Delete right), agent-verified 2026-09-14
1. **Place the playhead** at the trim point: click the ruler at `x₀ + t × px/s`. On
   2026-09-14, x=1030 landed exactly on **00:00:15:00**. Confirm by zooming into the timecode.
2. **Select** the segment under the playhead by clicking its body away from the playhead
   (segment 1 at x=1300, y=830). The selection click doesn't move the playhead.
3. **Trim:** `cc.py key w`.
4. **Result:**
   - segment 1 now ends at **15.000 s** (duration 13.467 → 5.000, src_duration likewise)
   - its start (10.000) and source start (10.000) are unchanged
   - project duration 23.467 → 15.000
   - the draft also gained an empty `material_animations` ref on the segment (CapCut adds empty
     helper materials on edits; benign)
   - autosaved about 2 s later
5. **Undo:** Ctrl+Z → the diff against baseline shows **No differences**.
7. *(see Op 4 below)*

### Op 4 — Move a segment onto an overlay track — agent-verified 2026-09-14
1. **Drag** the segment from its **centre** (far from both trim edges) straight up into the empty area above the main track: `cc.py drag 1120 830 1120 715 --steps 30 --hold 0.35`.
2. **Result:** a new **video track 1** (`flag=2` = overlay) is created holding the segment at the **same time** (10.000–23.467 s, src@10.000); the main track keeps only segment 0; project duration unchanged (23.467 s). Draft diff: `track_count 1 → 2`, `+ track 1 [video] added with 1 segments`, `- track 0 seg 10.000–23.467`. No ripple happened on the main track because the moved segment was the last one.
3. **Undo:** Ctrl+Z → **No differences** vs baseline.
4. **Note:** dragging near a clip edge grabs the trim handle instead of moving — always start the drag from the clip centre.

### Op 5 — Add media to the timeline — agent-verified 2026-09-14
1. **Precondition:** the clip is already in the project's Media panel (import route: rung 0 — Import → From device → native file dialog `set-value` id 1148 + invoke Open id 1).
2. **Locate** the media card: Media tab → card with filename + duration badge (2026-09-14 at ≈(337, 216); grid-screenshot `--region 0,40,520,600` first).
3. **Drag** the card onto the main track **past the last segment's end**: `cc.py drag 337 216 1650 830 --steps 40 --hold 0.4`.
4. **Result (magnet ON):** the clip is appended **flush** to the previous segment — new segment `23.467 → 46.933 s`, `src@0.000`; project duration 23.467 → 46.933; helper materials +1 each. (The drop x doesn't need to be exact: the main-track magnet snaps it to the end.)
5. **Undo:** Ctrl+Z → **No differences** vs baseline.
6. **Dropping onto empty timeline** (no clips yet) places the clip at 00:00 and sets the canvas to the clip's aspect (rung 0 observation).

### Op 6 — Lock and mute a track — agent-verified 2026-09-14
Track header icons (left of the main track, y ≈ 829 at this layout): track-type icon (≈x 29), **lock** (≈59), **eye/hide** (≈89), **speaker/mute** (≈119), "…" (≈149), then the **Cover** button (≈194). For an overlay track the same icons sit on that track's header row.
1. **Lock:** click the lock icon → the lock turns cyan and the whole track gets a **diagonal hatch overlay**. Draft: track `attribute 0 → 4` (autosaved ~1 s later). **Behaviour:** clicking a clip on the locked track does **not** select it (no white border, clip tools stay greyed).
2. **Unlock:** click the lock again → hatch gone, `attribute 4 → 0`.
3. **Mute:** click the speaker icon → a **"Track muted"** toast appears near the playhead, the speaker turns cyan with a slash. Draft: track `attribute 0 → 1`.
4. **Unmute:** click again → `attribute 1 → 0`.
5. **Verify:** after unlock + unmute, diff vs baseline = **No differences**.
6. **Attribute bits observed:** 1 = muted, 4 = locked (hide/eye presumably 2 — not yet exercised).

6. **Q (Delete left)** is the mirror operation. It removes the part left of the playhead, and with
   the magnet on it ripples the remainder to the left. It hasn't been demonstrated separately.

## Wait conditions
- Autosave after an edit takes 2–70 s. Poll `draft_content.json` mtime (see rung 1).

## Verification
*(per operation)*

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery
Ctrl+Z after each operation, verified by diff against `baseline.json` showing No differences.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes
All timeline surfaces are screenshot-driven. The only tree help is the `MainWindow` root.

## Open questions for the user
