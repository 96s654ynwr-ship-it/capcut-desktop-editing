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

### A. Candidate footage and a motion metric (executed 2026-09-14, read-only)
- **Metric:** with the bundled ffmpeg, per clip:
  `-ss 2 -t 12 -an -vf "scale=160:-2,format=gray,tblend=all_mode=difference,signalstats,metadata=mode=print:key=lavfi.signalstats.YAVG" -f null -`.
  Parse `YAVG=` from stderr. The mean absolute frame-to-frame luma difference is a proxy for
  camera shake plus subject motion. Output: `cap13/motion-metric.txt`.

  | Clip | Content | mean diff | p90 |
  |---|---|---|---|
  | VID_20260626_202525 | office, 2 people (portrait) | **6.07** | 12.43 |
  | VID_20260501_233737 | purple desk setup (portrait) | **5.33** | 9.16 |
  | VID_20260501_233809 | working at purple desk (portrait) | **5.12** | 8.99 |
  | VID_20260628_173114 | gym bench press (portrait) | **3.96** | 5.72 |
  | VID_20260425_174820 | close-up talking head, grey tee | 2.58 | 6.98 |
  | VID_20260501_111338 | empty chair + wall | 2.43 | 6.27 |
  | VID_20260416_203431 | office, 3 people | 1.66 | 3.68 |
  | VID_20260530_182728 | Nile view | 1.32 | 1.64 |
  | VID_20260428_064459 | selfie, dim | 1.30 | 2.01 |
  | VID_20260721_110250 | empty room (talk's room) | 0.62 | 1.90 |
  | VID_20260623_150351 | gym floor | 0.47 | 0.56 |

- **First read:**
  - **Stabilize:** the high-motion handheld clips (202525, 233737 / 233809).
  - **Remove BG:** a single person on a fairly plain background. Candidates are the talk's source
    `VID_20260720_190542` (speaker on a light wall) or 174820 (close-up).
  - **Camera tracking:** a clip where the subject moves, e.g. 173114 (gym) or 202525.
  - A frame-difference score can't separate camera shake from subject motion; the user's knowledge
    of the clips decides.
- Sheet: `cap13/visual-ai-candidates-sheet.png`, sorted by motion, reusing the rung-10 frames.

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
- **Features:** "Remove background (Recommended), Stabilization (Recommended)". **Camera tracking is
  not in scope** for this demonstration.
- **Stabilization clip:** "3 working at purple desk (Recommended)" = `E:\videos\VID_20260501_233809.mp4`
  (38 s, portrait via −90° rotation, handheld; motion 5.12).
- **Remove BG footage:** "Your talk footage (Recommended)" = `E:\videos\VID_20260720_190542.mp4`
  (the talking head, speaker on a light wall). Use a short section.
- **Project:** "New practice project (Recommended)". A fresh agent-owned project with just these
  clips, ≈10–20 s each. The approved projects stay untouched.
- Evidence from 2026-09-15 onward goes to `evidence/2026-09-15/cap13/` (date rollover). The
  candidate files stay in `evidence/2026-09-14/cap13/`.

## Open questions for the user
- Which of the three features, and which footage for each.
