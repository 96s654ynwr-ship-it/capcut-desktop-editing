# Capability 15: Export (resolution, fps, bitrate, codec; verify the output file)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0915-copy` (the approved rung-14 promo, 30 s). Exporting only reads the
  project; the draft must stay unchanged.
- **Evidence:** `evidence/2026-09-15/cap15/`

## Goal
Export an approved edit natively through CapCut's Export dialog with stated settings, to a
user-approved folder. Then verify the file itself with the bundled ffmpeg/ffprobe: container,
codec, resolution, frame rate, duration, audio stream, loudness, and frames that match the
timeline.

## Preconditions
- Rungs 0–14 approved.
- **Side effects:** exporting writes a file, which the user approved for this run: 1080p 30fps
  H.264 to `E:\videos\exports`.
  - ⚠ **"Sync exported videos to space"** is **checked by default** in the dialog. It uploads to
    CapCut cloud, which the standing rules forbid, so **uncheck it before Export**.
  - Also stop on any Pro/credit/upsell prompt (e.g. for Pro features used in the edit).
- **Known route** (rung 0, observed, never run):
  - The cyan **Export** button (top-right) or **Ctrl+E** opens a named window
    `Export-<project>` (id `ExportWindow_Container`, no child controls in UIA).
  - Right-hand fields: Name, **Export to** path + folder icon, and a Video section with
    Resolution ▾ (1080P), Bit rate ▾ (Recommended), Codec ▾ (H.264), Format ▾ (mp4), Frame rate ▾
    (30fps), Color space.
  - Also: the Sync-to-space checkbox, an Audio section (unchecked, MP3), and a footer with
    Duration/Size, **Export** and **Cancel**. The settings list scrolls.
- **Bundled tools:** `D:\Bytedance\CapCut\Apps\9.4.0.4015\ffmpeg.exe` (read-only analysis).
  Check whether an `ffprobe.exe` sits beside it; otherwise use `ffmpeg -i`.

## User choices (2026-09-15)
- **Project:** "0915-copy promo (Recommended)".
- **Settings:** "1080p 30fps H.264 (Recommended)", bitrate left at CapCut's Recommended.
- **Folder:** "E:\videos\exports (Recommended)", a new subfolder created only through CapCut's own
  export dialog.

## Plan
1. Baseline: all project mtimes, the `0915-copy` draft copy, and the state of the exports folder.
2. Open `0915-copy`; open the Export dialog (Ctrl+E); screenshot every section (scroll the list).
3. Set Name, Export to `E:\videos\exports` (create the folder via the dialog's folder picker if
   needed), and Resolution 1080P / Bit rate Recommended / Codec H.264 / Format mp4 / Frame rate
   30fps. **Uncheck Sync to space.** Screenshot the final settings before clicking Export.
4. Export; record the progress UI and duration; wait for the completion screen. Do not click any
   share/upload/publish buttons on it.
5. Verify the file: size, `ffmpeg -i` stream info (h264, 1920×1080, 30 fps, AAC audio, 30.0 s),
   ebur128 loudness, and frames extracted at key times (logo, 14:23 blend, 16:14 canvas blur)
   compared with the player frames from rung 14.
6. Verify the draft is unchanged and the other projects' mtimes; confirm nothing was uploaded
   (sync unchecked).
7. Write up, contact sheet, ask for approval.

## Procedure

### A. Baseline (read-only, 2026-09-15)
- **Project mtimes:** 16 projects saved to `cap15/mtimes-before.txt`.
- **Draft copy:** `cap15/draft-before-export.json` (the `0915-copy` draft as saved at the end of
  rung 14, 02:59:12).
- **`E:\videos\exports` does not exist yet.** `E:\videos` has one subfolder (the Arabic-titled
  project's export folder) and 48 top-level mp4 files. The new folder will be created only through
  CapCut's dialog.
- **No `ffprobe.exe`** beside the bundled ffmpeg, so file verification uses `ffmpeg -i` (stream
  info on stderr), `ebur128` and frame extraction.

### B. Open the project and the Export dialog (2026-09-15)
1. From Home (`scroll 1000 700 -3`, `00-home-projects.png`), click the **`0915-copy`** card
   ≈(383,793). `MainWindow` appears after 4 s; then `focus --maximize` (`01-editor-opened.png`).
2. **Ctrl+E.** `wait-for --id ExportWindow_Container --depth 3` matches in **0.2 s** (0.8 s wall).
   **Tree:**
   - `Window "Export-0915-copy"` id `ExportWindow_Container`, cls `ExportWindow_QMLTYPE_2223`,
     rect **(510,101)–(1410,929)**, a child of MainWindow
   - `cc.py windows` also lists it as a top-level `Qt622QWindowIcon` titled `Export-0915-copy`
   - as in rung 0, no child controls are exposed, so the dialog is **screenshot-only**
     (`02-export-dialog.png`)
3. **Dialog layout and defaults** (dialog rect (510,101)–(1410,929)):
   - **Left:** cover preview with **Edit cover**, showing the first frame with the logo.
   - Export timeline: Timeline 01.
   - **Name** ≈(1238,227): `0915-copy`.
   - **Export to** ≈(1220,273): `E:/videos/0915-copy.mp4`, the last-used folder. Folder icon
     ≈(1371,273).
   - **Video** ✓ (≈967,342):
     - Resolution ≈(1229,389): **1080P**
     - Bit rate ≈(1229,437): **Recommended**
     - Codec ≈(1229,484): **H.264**
     - Format ≈(1229,532): **mp4**
     - Frame rate ≈(1229,579): **30fps**
     - Color space: Rec. 709 SDR (read-only)

     **The defaults already match the user's 1080p / 30fps / H.264 choice.**
   - ⚠ **Sync exported videos to space ✓** ≈(967,696): checked by default.
   - **Audio** ☐ ≈(967,764), Format MP3 (greyed). This is a separate audio-only file option; the
     mp4 carries the soundtrack regardless.
   - **Footer:** "Duration: 30s | Size: about 30 MB" (the estimate implies ≈8 Mbps at
     Recommended), **Export** ≈(1244,895), **Cancel** ≈(1344,895).
4. **Draft unchanged by opening:** the mtime is still 02:59:12.029 and the diff vs
   `draft-before-export.json` shows no differences.

### C. Uncheck cloud sync and pick the export folder (2026-09-15)
1. **Uncheck "Sync exported videos to space":** click the checkbox ≈(967,696).
   - **Observed** (`03-sync-unchecked.png`, dialog crop): the box is **empty**. Everything else is
     unchanged: 1080P / Recommended / H.264 / mp4 / 30fps, Audio ☐, "about 30 MB".
2. **Folder icon** ≈(1371,273) opens a **native Windows folder picker**, and unlike the Export
   dialog it is **fully exposed to UIA**:
   - `cc.py windows`: `#32770` **"Select exporting path"** (518,101)–(1462,693), owned by
     CapCut.exe.
   - It opens in **E:\videos**, the last export folder. The address bar is
     `ToolBar "Address: E:\videos"`, with breadcrumb SplitButtons "This PC › New Volume (E:) ›
     videos".
   - Toolbar buttons: **Organize**, **`Button "New folder"`** ≈(688,202), Views, Help.
   - Left: `Tree "Tree View"` (Quick access, This PC, drives…). Right: `List "Items View"`, which
     here shows only the Arabic-titled project's folder.
   - **`Edit "Folder:"` id 1152** ≈(1080,622), **`Button "Select Folder"` id 1**
     ≈(1249,660), **`Button "Cancel"` id 2** ≈(1386,660).
   - Note: `tree --root focused` shows only the Folder: edit. Use the default roots with depth 16
     to see the whole dialog (`04-folder-picker.png`).

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
- None yet.
