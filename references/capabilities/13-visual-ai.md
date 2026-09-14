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

### B. New practice project and import (executed + agent-verified 2026-09-15)
1. **Pre-checks:**
   - `HomeWindow` present, no menu or dialog.
   - All project mtimes saved to `evidence/2026-09-15/cap13/mtimes-before.txt`.
   - numpy is **not** in the skill venv. Installing it would download a package, so the shake metric
     uses PIL instead (`shake_metric.py`).
2. **Create project:** `scroll 1000 500 10` (home top), then click **Create project** (≈1102,144).
   - `MainWindow` on the first poll; `focus --maximize`.
   - The new draft folder **`0915`** appeared (CapCut names new projects by date).
3. **Import**, once per file (rung-3 route):
   - `key ctrl+i`, then poll `find --type Edit --id 1148`.
   - `act set-value --id 1148 --value <path>`, then `act invoke --id 1 --name Open`, and wait ≈5 s.
   - Files: `E:\videos\VID_20260720_190542.mp4` (talk), then `E:\videos\VID_20260501_233809.mp4` (desk).
   - **Agent-verified:** `draft_meta_info.json` lists both (523 454 000 µs and 37 958 000 µs).
     The timeline is still empty.
4. **Editor after import** (`01-new-project-imported.png`):
   - Title **0915**. Media cards: talk ≈(382,216), desk ≈(382,313).
   - The desk card is selected and the player shows **"Previewing — video"** (portrait, 00:00:37:29).
   - Empty timeline drop row "Drag material here and start to create" at y≈829.
   - Details: Aspect ratio Original, 30.00 fps.
   - A yellow "Layers can be reordered in…" onboarding bubble sits near **Modify**.

### C. Section choices and shake reference (read-only, 2026-09-15)
- **Remove-BG section:** talk footage source **80 → 95 s** (15 s).
  - Frames at 50/80/…/330 s (`talk-sections/talk-source-sheet.png`) show a tripod shot. The speaker
    is seated centre, and the background is **busy**: window, frame, chair, desk, shelves.
  - That makes a realistic Auto removal test. Any 15 s section looks alike.
- **Stabilize section:** desk clip source **2 → 17 s** (15 s), skipping the unsteady first 2 s seen
  in rung 10.
- **Source shake reference** (`shake_metric.py <clip> 2 15 shake-before`: 96 px wide, 30 fps,
  ±6 px search, 450 pairs, 12 s runtime):
  - mean |dx| **0.24** px/frame, mean |dy| **0.14** px/frame; 32 % of pairs moved
  - cumulative path x −32…+6 px, y +1…+25 px: a slow **pan / drift** of about ⅓ of the frame width
  - second-difference **jitter 0.062**; residual diff 3.49
  - At 96 px, sub-pixel shake is invisible. The before/after comparison must use the **same capture
    method** for both: player frames stepped through CapCut before and after Stabilize, analysed
    with `shake_metric.py --frames`.

### D. Build the practice timeline (in progress)
1. **Drop the talk clip:** `drag 382 216 700 829 --steps 30 --hold 0.35` from the media card to the
   empty drop row. The draft saved on the first poll.
   - **Agent-verified:** canvas `original` **1920×1080**, set by this first clip (source 1280×720).
     Main track, 1 segment, `VID_20260720_190542.mp4`, target 0 → **523.467 s**, source 0 → 523.467 s.
     The whole clip.

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
