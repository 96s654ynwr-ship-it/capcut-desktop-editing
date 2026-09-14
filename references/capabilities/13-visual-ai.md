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
   - **Observed** (`02-talk-dropped.png`):
     - The clip is auto-selected (white border, x≈229–781); Video ▸ Basic inspector.
     - Player "00:00:00:00 / 00:08:43:14". Its first frame shows the speaker's shoulder close to the
       lens, as he sits down.
     - Ruler at this auto zoom: 00:00 at x≈229, 05:00 at x≈545, so **≈1.053 px/s**.
       10:00 at x≈861 confirms it.
2. **Frame-exact playhead strategy:** `cc.py key --repeat N` loops `press_combo` with a default
   `--gap 0.06` s, and N has no cap. Stepping 2 850 frames from Home would take ≈3+ min. So: ruler
   click near the target (≈1 px/s at this zoom, no captions to snap to), read the zoomed timecode,
   then correct with `left`/`right` (1 frame each at 30 fps).
3. **Trim the talk clip to source 80–95 s** (clip still selected):
   - Ruler click at x = 229 + 95 × 1.053 ≈ **329** lands on **00:01:35:02** (`03-hdr-tc.png`), off by
     2 frames. The playhead handle sits at x≈329 over the selected clip (`03-timeline.png`); the draft
     is unchanged.
   - `key left --repeat 2` → **00:01:35:00**, confirmed by crop (`04-tc-before-W.png`), then **W**
     (delete right).
     - **Agent-verified (first poll):** duration 523.467 → **95.000 s**; one segment target 0 → 95,
       source start 0.
     - The clip stays selected; the timeline total reads 00:01:35:00.
   - Ruler click at x≈313 (80 s) lands on **00:01:19:27** (`06-hdr-tc.png`), 3 frames short. The
     clip is still selected (`06-timeline.png`).
   - `key right --repeat 3` → 00:01:20:00, then **Q** (delete left).
     - **Agent-verified (first poll):** duration **15.000 s**; segment target 0 → 15.000 s, **source
       start 80.000 s**. The magnet rippled the start to 0.
4. **Append the desk clip:** `drag 382 313 900 829 --steps 30 --hold 0.35` from the desk media card
   to the main track, right of the talk clip.
   - **Agent-verified (first poll):** 2 main-track segments.
     - talk: 0 → 15.000 s, source 80 s
     - **desk `VID_20260501_233809`: 15.000 → 52.967 s (37.967 s), source 0**. The magnet snapped
       it flush.
   - Canvas stays **original 1920×1080** (set by the first clip); duration 52.967 s.
   - **Observed** (`09-desk-dropped.png`):
     - The dropped desk clip is **auto-selected**. The timeline stays at the old zoom (≈1.053 px/s),
       so both clips fit in x≈229–285.
     - The playhead jumped back to **00:00:00:00**; player "00:00:00:00 / 00:00:52:29".
     - Pre-Q crop confirmed the cut was at 00:01:20:00 (`07-tc-before-Q.png`).
5. **Zoom in for frame-exact placement:** `key "ctrl+="` × 4 (`10-zoomed*.png`). The draft is
   unchanged.
   - Ruler labels: 00:00 at x≈228, 00:05 at ≈555, 00:10 at ≈882, 00:15 at ≈1210, 00:20 at ≈1537.
     That is **≈65.4 px/s** (≈2.2 px per frame).
   - The playhead stays at 00:00:00:00 and the desk clip stays selected (border from x≈1210).
   - Desk trim targets: timeline **17.000 s** (desk source 2 s) → ruler x ≈ 228 + 17 × 65.4 ≈
     **1340**, then **Q**. After the ripple the desk clip starts at 15 s with source 2 s. Then
     timeline **30.000 s** → **W**.
6. **Desk clip trim:**
   - Ruler click at x≈1340 lands on **00:00:16:29** (`11-hdr-tc.png`), 1 frame short. The desk clip
     stays selected, and the playhead handle is at x≈1340 inside it (`11-timeline.png`).
   - `key right` → 00:00:17:00, then **Q**.
     - **Agent-verified (first poll):** duration **50.967 s**; desk segment 15.000 → 50.967 s,
       **source start 2.000 s** (the magnet rippled it flush).
   - **Failed attempt (don't repeat):** 30 s is off-screen at this zoom (x≈2190), so I stepped
     instead with `key right --repeat 390 --gap 0.04` (13 s at 30 fps), then **W**.
     - The crop taken before W read **00:00:28:00** (`14-tc-before-W.png`). **60 of 390 key presses
       were dropped.**
     - The draft went to 28.000 s (desk 13.0 s).
     - One **Ctrl+Z** brought back exactly 50.967 s / desk 15.000 → 50.967, source 2.
   - **Working route:**
     - Click the timeline **zoom-out** button (≈1709,596) once. That gives ≈32.7 px/s, with
       00:30 at x≈1212, and the desk clip stays selected (`18-zoomed-out.png`).
     - Ruler click at x≈1212 → **00:00:30:01** (`19-tc-ruler30.png`).
     - `key left` → **00:00:30:00** (`20-tc-before-W.png`), then **W**.
     - **Agent-verified (first poll):** duration **30.000 s**; talk 0 → 15.000 s (source 80); **desk
       15.000 → 30.000 s (source 2.000)**. Timeline total 00:00:30:00 (`21-desk-trimmed.png`).
   - Rule: **never trust long key-repeat stepping.** Zoom so the target is on screen, click the
     ruler, correct by a few frames, and crop the timecode before every Q/W.

### E. "Before" player frames of the desk section (executed + agent-verified 2026-09-15)
- Ruler click at x≈721 (00:15 at 32.7 px/s) snapped to **00:00:15:00**, the desk clip start
  (`22-tc-desk-start.png`).
- **`player_frames.py <out> 300`** takes these crops:
  - preview crop (922,105)–(1125,475): the portrait video box inset 6 px, to avoid the selection
    handles
  - timecode crop (615,528)–(712,555)

  For each frame it presses Right, waits until the **timecode crop changes** (re-sending once after
  1 s), waits until the preview changes (≤0.35 s), and saves a 96 px-wide grayscale frame.
  - Result: 300 frames in **20 s**, **0 re-sends, 0 unchanged previews**.
  - **Agent-verified:** the saved timecode crops read 00:00:19:29 at frame 150 and **00:00:24:29 at
    frame 300**, so no frame was skipped. That contrasts with `key --repeat` in D.6.
- **`shake_metric.py shake-player-before --frames player-before`:** 299 pairs.
  - mean |dx| **0.288**, |dy| **0.177** px/frame; 35.5 % of pairs moved
  - **jitter 0.067**; path x −38…+3, y +1…+28; residual 3.19
  - Consistent with the source reference in C (0.24 / 0.14 / 0.062 over source 2–17 s), so player
    frames are a valid measurement surface.

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
