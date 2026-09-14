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
2. **Duplicate before editing.** Use CapCut's own duplicate/copy command on the home screen
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
5. **Draft freshness.** CapCut autosaves on a timer and on leaving the editor. Before a diff,
   check that `draft_content.json`'s modification time is newer than your last action. If it
   isn't, wait or return to the home screen to force a save.
6. **Never trigger sync or cloud actions.** Space/cloud upload, sharing links, publishing to
   TikTok/YouTube and team spaces all require explicit user approval.
7. **Export only to a folder the user named.** Never overwrite existing files without asking. The
   Export dialog pre-fills **Export to** with the last-used folder, so change it deliberately.
8. **Uncheck "Sync exported videos to space" in the Export dialog before every export.** In
   9.4.0.4015 it is checked by default and uploads the video to CapCut cloud. Take a screenshot of
   the dialog showing it unchecked before pressing Export.
