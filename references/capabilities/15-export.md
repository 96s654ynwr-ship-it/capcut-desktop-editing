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
