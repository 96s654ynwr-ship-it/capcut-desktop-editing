# Capability Ladder (the gate)

This file is the single source of truth for what the agent may do. Work only on the **lowest row
whose status is not `approved`**. Update this file at every status change.

Status values:
- `not-started`
- `in-progress`
- `demonstrated`: the agent verified it and is waiting for the user
- `approved`: the user said yes in chat
- `blocked`: record why in Notes

| # | Capability | Styles | Status | Procedure file | Demonstrated | Approved | Notes |
|---|---|---|---|---|---|---|---|
| 0 | Environment + accessibility/control map | all | approved | `accessibility-controls.md`, `keyboard-shortcuts.md`, `pro-features.md` | 2026-09-14 | 2026-09-14 | CapCut UI invisible to UIA/MSAA (root windows only; QT_ACCESSIBILITY=1 no effect) → screenshot-first. Named tree windows for dialogs (Shortcuts, Export) and the player surface; native file dialog fully exposed. DPI mapping verified at 125%. Practice project `0914`: clip imported + placed, verified by draft. Mapped: home, editor layout, asset tabs, inspector tabs, menu, full shortcut list (CapCut's own), export dialog (cancelled). **Gaps filled after approval (2026-09-14, view-only, draft unchanged):** Menu ▸ Layout; Settings (all 4 tabs, closed with Cancel); Video ▸ Remove BG/Mask/Retouch; Audio ▸ Voice changer; right-click menus on a clip and on empty timeline. **Deferred:** Transcript panel (Pro, may use credits) → rung 3 with the user's confirmation; basic-tool icons show no tooltips → identify in rungs 1–2 via shortcuts and behaviour. **Correction (2026-09-14):** the "draft unchanged" checks during mapping compared against an un-resaved draft. After Back to home page saved `0914`, it had an added empty `hsl` material from browsing Adjust ▸ HSL. Agent-owned project only; user projects untouched (mtimes unchanged). Lesson recorded in project-safety rule 5. |
| 1 | Duplicate project, open copy, one split at an exact time, undo test, save | all | in-progress | `capabilities/01-single-split.md` | | | 2026-09-14: source = practice project `0914` (1 segment, 23.467 s); split target 00:00:10:00. |
| 2 | Timeline basics: select, delete/ripple, trim, move, add media, track lock/mute | all | not-started | `capabilities/02-timeline-basics.md` | | | |
| 3 | Transcript editing: remove pauses/silences and filler words | YouTube | not-started | `capabilities/03-transcript-pauses.md` | | | |
| 4 | Bad-take removal via transcript | YouTube | not-started | `capabilities/04-bad-takes.md` | | | |
| 5 | Waveform/manual cleanup pass | YouTube | not-started | `capabilities/05-waveform-cleanup.md` | | | |
| 6 | Jump cuts with scale/position punch-in | YouTube | not-started | `capabilities/06-jump-cuts.md` | | | |
| 7 | Keyframed eased push-ins | YouTube, promo | not-started | `capabilities/07-push-ins.md` | | | |
| 8 | Auto captions + styling (incl. speaker-ID captions) | YouTube, shorts | not-started | `capabilities/08-auto-captions.md` | | | |
| 9 | Animated text: word-by-word, titles, text templates | shorts, promo | not-started | `capabilities/09-text-animations.md` | | | |
| 10 | B-roll / overlay track (picture-in-picture) | YouTube, promo | not-started | `capabilities/10-b-roll.md` | | | |
| 11 | Audio Pro: vocal isolation, enhance voice, noise reduction, music + ducking | Pro AI | not-started | `capabilities/11-audio-pro.md` | | | |
| 12 | Vertical: 9:16 canvas, auto reframe, beat-synced cuts | shorts | not-started | `capabilities/12-vertical.md` | | | |
| 13 | Visual Pro AI: remove background, stabilization, camera tracking | Pro AI | not-started | `capabilities/13-visual-ai.md` | | | |
| 14 | Promo polish: transitions, filters/adjust/color, logo/brand overlay, templates | promo | not-started | `capabilities/14-promo-polish.md` | | | |
| 15 | Export: resolution up to 4K, fps, bitrate, codec; verify the output file | all | not-started | `capabilities/15-export.md` | | | |
| 16 | End-to-end talking-head YouTube edit | YouTube | not-started | `capabilities/16-e2e-youtube.md` | | | |
| 17 | End-to-end vertical short | shorts | not-started | `capabilities/17-e2e-short.md` | | | |

## What "demonstrated" must show, per rung

- **0.**
  - `setup.ps1` works and `cc.py windows/tree/screenshot` work against the live CapCut.
  - DPI mapping is proven: clicking a tree element's rectangle centre hits it.
  - Every major area in `accessibility-controls.md` is filled in with its tree coverage level
    (full/partial/none), key named controls, and what needs screenshots.
  - Pro feature locations and tier badges are recorded in `pro-features.md`.
  - Shortcuts are checked against CapCut's own shortcut list.
  - Documents whether your agent's sandbox allows desktop input.
  - No project is modified.
- **1.**
  - The duplicate is created through CapCut's UI and the original is untouched (its draft
    `update_time` is unchanged).
  - The playhead is placed at a stated time and the player timecode confirms it.
  - One split: the draft diff shows one segment becoming two at that time.
  - Undo reverts it (diff) and redo re-applies it.
  - The project is saved/closed cleanly.
- **2.**
  - Each basic operation is demonstrated once on the copy, with a diff per operation.
  - Ripple vs non-ripple behaviour and the magnet/main-track setting are documented.
- **3.**
  - CapCut's transcript/"remove pauses/filler words" route is run on real talking footage.
  - Settings used are documented. The before/after duration and segment count are shown.
  - The result is spot-checked at 3 cut points by screenshot or playback.
- **4.**
  - A repeated take is identified in the transcript and the bad version removed natively.
  - The kept take is named and the diff confirms the removed range.
- **5.**
  - Remaining breaths/gaps are found on the waveform (screenshots) and tightened.
  - The criteria used are documented (gap length, what gets kept).
- **6.**
  - Alternating punch-in at cuts with a stated scale/position.
  - Eye-line continuity is checked visually on adjacent frames.
  - Shot-specific values are flagged as such.
- **7.**
  - A keyframed scale move with easing over a stated range.
  - Keyframes are visible in the diff (`keyframes`/`common_keyframes`), and a playback screenshot
    is taken at start/mid/end.
- **8.**
  - Auto captions are generated (language stated) and a style is applied.
  - Timing is spot-checked and any caption errors fixed natively.
  - Credits/Pro gating is recorded.
- **9.**
  - Animated text is added at a stated time, with a word-by-word or template animation and style.
  - Readable in screenshots.
- **10.**
  - B-roll is placed on an overlay track at a stated range with a stated scale/fit.
  - Audio handling (muted/kept) is decided and verified.
- **11.**
  - Each audio tool is applied to a clip, with its settings documented.
  - For vocal isolation/enhance: credits are confirmed with the user before running, and the
    result is listened to or waveform-compared.
- **12.**
  - Canvas switched to 9:16 and auto reframe applied.
  - Beat marks created and cuts aligned to them.
  - Framing is checked by screenshot.
- **13.**
  - Each tool is applied to a clip. Processing waits are recorded, and results checked by
    screenshot.
  - Credits are confirmed first.
- **14.**
  - One of each (transition, filter/adjust, logo overlay) is applied and verified in the diff and
    by screenshot.
- **15.**
  - Export dialog settings are documented and the file is exported to a user-approved folder.
  - Bundled `ffmpeg -i` confirms resolution/fps/duration.
- **16/17.**
  - The full edit runs using only approved rungs, from raw takes to exported file.
  - The user reviews the final video.

## Approval log

| Date | Rung | User's words | Commit |
|---|---|---|---|
| 2026-09-14 | 0 | "Approve, fill gaps first" (approved; mapped the listed gaps without editing before starting rung 1) | see git log |
