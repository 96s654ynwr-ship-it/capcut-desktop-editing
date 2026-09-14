# Capability 13: Visual Pro AI (remove background, stabilization, camera tracking)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** to be chosen with the user. It must be agent-owned: a CapCut duplicate or a
  new project. The approved masters `0914 (4)-copy` (horizontal) and `0914 (4)-copy-copy` (vertical)
  stay intact.
- **Evidence:** `evidence/2026-09-14/cap13/`

## Goal
Run CapCut's visual AI tools natively on suitable footage, verifying each in the draft and in frames:
- **Remove background:** Auto removal, which is Pro. Custom removal and Chroma key are fallbacks.
  The speaker is cut out; optionally a new background goes behind.
- **Stabilization:** Video ▸ Basic ▸ Stabilize, which is Pro, on shaky handheld footage. Measure the
  shake before and after.
- **Camera tracking:** Video ▸ Basic ▸ Camera tracking, which is Pro, on a clip with a moving
  subject. Keep the subject framed or attach an element to it.

## Preconditions
- Rungs 0–12 approved.
- Credits: the user's standing answer is "run; stop if a cost appears". Stop at any cost or upsell
  dialog. Every Pro audio and reframe tool so far ran with no cost dialog.
- **Known routes** (rungs 0 and 12, not yet run):
  - Inspector **Video ▸ Remove BG** sub-tab: **Auto removal** (Pro), **Custom removal ▾**,
    **Chroma key ▾** (with keyframes).
  - Inspector **Video ▸ Basic**, scrolled list: Enhance quality, Reduce image noise, Optical flow,
    AI remove, AI expand (Free), AI remix, Lip sync, Relight, Auto reframe, Remove flickers,
    AI movement, **Camera tracking** (Pro ▾), Motion blur, Canvas.
  - **Stabilize** (Pro) was seen in Video ▸ Basic in rung 0. It was not in the rung-12 list read,
    so re-check (it may sit above "Enhance quality").
  - A **Tracking** tab exists on text layers (captions and titles), a possible route for attaching
    a text layer to a moving subject.
- **Lessons to apply:**
  - Lock caption and title tracks before clicking a clip, so only the clip is selected.
  - Keep the timeline tool on **Select (A)**.
  - Never close menus with a fixed coordinate.
  - Poll the draft for expected values.
  - Async AI work shows progress inside MainWindow ("Processing N%" / "Applying N features"). The
    draft may save before the work finishes.

## Plan
1. **Pick footage with the user.** Compute a read-only motion/shake metric per candidate with the
   bundled ffmpeg, show a contact sheet, and choose a clip per feature (or one clip for all).
2. **Practice project:** a new agent-owned project with the chosen clips imported natively (Ctrl+I),
   or a duplicate. Baseline it.
3. **Remove BG:** apply Auto removal. Watch for processing and cost dialogs. Verify the draft
   material (e.g. a `…matting…` / removal ref) and frames showing the background removed.
   Optionally add a solid/blurred background via Canvas.
4. **Stabilize:** apply to the shaky clip with a stated level. Verify the draft (`stable` fields on the
   video material, which were `stable_level` 0 in rung 12) and measure frame-difference shake before
   vs after on player frames.
5. **Camera tracking:** apply to the moving-subject clip. Record the options (subject pick, zoom,
   speed), verify the draft and frames across the clip.
6. **Gate, save, scope check;** write up; demonstrate.

## Procedure

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

## User choices (2026-09-14)

## Open questions for the user
- Which of the three features, and which footage for each.
