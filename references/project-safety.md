# Project Safety

## Where projects live

- **Default draft root:** `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\`. The user
  can change this in CapCut settings. `draft_inspect.py list` reads `root_meta_info.json`, which
  records the actual paths.
- **Each project is a folder** containing:
  - `draft_content.json`: timeline, tracks, segments, materials, keyframes; times in microseconds
  - `draft_meta_info.json`
  - `draft_cover.jpg`
  - imported/processed media and cache folders
- **In CapCut 9.4 the draft JSON is plaintext.** If a future build encrypts it,
  `draft_inspect.py` will say so. Then verification falls back to screenshots and the UI only.
  Record that in the ladder.

## Rules

1. **Never write project files.** No JSON edits, no copying files into or over a project folder,
   no deleting project folders. All changes go through CapCut's UI.
2. **Project-card menu hazards (home screen).** Right-clicking a project card shows Upload /
   Rename / **Duplicate** / **Delete**:
   - Delete is the next row below Duplicate, and **Backspace deletes a selected card**.
   - Click the vertical centre of the Duplicate row, from a fresh screenshot.
   - Never press Backspace/Delete while the home screen has focus.
   - Never choose Upload (cloud).
3. **Duplicate before editing.** Use CapCut's own duplicate/copy command on the home screen
   project card. The exact route is found and recorded by Capability 1 (candidate: the "…" menu or
   right-click on the card → Duplicate/Copy).
   - Name the copy `<original> - agent practice YYYY-MM-DD`.
   - Confirm with `draft_inspect.py list` that a new folder exists.
   - Confirm the original's `update_time` doesn't change during the session.
3. **Take a read-only snapshot for reference.** `cc.py evidence <label> --project "<copy>"` saves
   the draft summary and a copy of the JSON into `evidence/`. This is for diffs and for showing
   the user what changed. It is **not** a restore mechanism.
4. **Recovering from a bad edit:**
   - Use CapCut undo (Ctrl+Z), confirm the revert by screenshot and diff, then continue.
   - If undo can't fix it, stop and tell the user. Offer to delete the practice copy through
     CapCut's UI (needs their yes) and start a fresh duplicate.
   - Never repair the JSON.
5. **Browsing is not zero-write** (observed 2026-09-14). While mapping, I opened the inspector's
   Adjust ▸ HSL sub-tab on project `0914`. When the project was later saved (Back to home page),
   the draft gained an empty `hsl` material referenced by the clip (`materials.hsl: 0 → 1`).
   Earlier diffs had shown "No differences" only because the draft on disk hadn't been re-saved
   yet. Therefore:
   - Treat any project you open and click around in as modified.
   - Browse and map only in agent-owned practice projects.
   - **Before diffing, force a save**: Menu ▸ Back to home page. Then check that
     `draft_content.json`'s modification time moved.
6. **Draft freshness.** CapCut autosaves on a timer and on leaving the editor. Before a diff,
   check that `draft_content.json`'s modification time is newer than your last action. If it
   isn't, wait or return to the home screen to force a save.
6. **Never trigger sync or cloud actions.** Space/cloud upload, sharing links, publishing to
   TikTok/YouTube and team spaces all require explicit user approval.
7. **Export only to a folder the user named.** Never overwrite existing files without asking. The
   Export dialog pre-fills **Export to** with the last-used folder, so change it deliberately.
8. **Auto sync is ON on the user's machine.** Menu ▸ Settings ▸ Draft shows the Auto sync toggle on,
   with Synced items: Exported videos ☑ and Projects ☐. Don't change it; it's the user's setting.
   Instead, handle sync per export as below. Never click Settings ▸ Save, and never the Cache
   trash button.
9. **Uncheck "Sync exported videos to space" in the Export dialog before every export.** In
   9.4.0.4015 it is checked by default and uploads the video to CapCut cloud. Take a screenshot of
   the dialog showing it unchecked before pressing Export.
