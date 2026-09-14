# Capability 12: Vertical (9:16 canvas, auto reframe, beat-synced cuts)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** to be chosen with the user. It must be an agent-owned project: a CapCut
  duplicate or a new project. `0914 (4)-copy`, which holds rungs 4–11, stays intact as the
  horizontal master.
- **Evidence:** `evidence/2026-09-14/cap12/`

## Goal
Produce a vertical (9:16) version natively in CapCut:
- change the canvas ratio to 9:16
- keep the speaker framed, using CapCut's **auto reframe** where available, or manual Position/Scale
  per clip as a fallback
- optionally cut to a music beat using CapCut's beat marks

Verify every step in the draft (canvas config, per-clip transforms / reframe materials, cut times
against beat marks) and in frames.

## Preconditions
- Rungs 0–11 approved.
- House style (`references/house-style.md`): captions Arabic-only. In 9:16 their position and size
  must be re-checked, since the lower third moves.
- Known routes from rung 0, to re-verify:
  - player **Ratio** button (≈1371,541)
  - project **Details ▸ Modify** (aspect ratio / resolution)
  - timeline and toolbar items for reframe and beats, to locate
- Credits: follow the user's standing answer, "run; stop if a cost appears". Stop at any cost or
  upsell dialog.
- **Leads found before starting** (read-only, 2026-09-14):
  - Player bottom-right icons include **Ratio** (`accessibility-controls.md`, rung 0).
  - **Details** panel (nothing selected): Aspect ratio "Original", Resolution "Adapted", Frame
    rate, and a **Modify** button. A yellow onboarding bubble can cover Modify.
  - **The canvas follows the first clip** (rung 0): a vertical first clip set the project to
    1080×1920.
  - Keyboard shortcuts list **"Clear beats"** (unassigned), so beat marks exist in 9.4.
  - `pro-features.md` rows "Beat detection" and "Auto reframe" are still unverified.
  - `User Data\Cache\SmartCrop\` holds renders named `0728 9：16 With Text …` / `Without Text …`
    (2026-08-22) and `0914 (6) …` (20:04 today). The user's own projects have gone through
    CapCut's smart-crop / reframe pipeline, so the feature is present in this install. Those
    projects are **not** touched; this is a lead only.
  - Home screen: **"Long video to shorts"** tool (AI suite). It is a separate route and not the
    in-editor reframe.

## Plan
1. **Choose the source with the user:** a short section of the horizontal master vs a raw take.
   Also the length, and whether beat-synced cuts are wanted (they need a music track).
2. **Duplicate** the chosen project natively (rung 1 route), or create a new project, and baseline
   it.
3. **Canvas 9:16:** Ratio ▸ 9:16 (or Details ▸ Modify). Verify the draft canvas config and a frame.
4. **Reframe:** find Auto reframe (Pro?) and apply it to the clips. Otherwise use a per-clip Scale
   plus Position X (typed unit = ½ canvas px). Verify the face is centred in frames across clips.
5. **Captions and title** in 9:16: check their position and size in frames, and adjust natively if
   they go off-frame.
6. **Beat-synced cuts** (if chosen): add music, generate beat marks, then split and trim cuts onto
   beats. Verify cut times against beat times in the draft.
7. **Verify, gate, save, scope check.**

## Procedure

### A. Duplicate the master (executed 2026-09-14)
1. **Snapshot the master first:** `draft_inspect.py summary "0914 (4)-copy" --json cap12/master-before.json`.
   - `diff` vs `cap11/final.json` = No differences.
   - Master mtime 22:00:40.991.
   - All project mtimes are in `cap12/mtimes-before.txt`.
2. **Home:** `scroll 1100 700 -5`, then a grid screenshot (`00-home-grid.png`). The first card is
   **0914 (4)-copy**, "264.8M | 07:31", at ≈(383,703). Its size grew from 188.9M after rung 11's
   enhanced audio.
3. **Right-click the card** (`click 383 703 --right`), then a fresh grid screenshot
   (`01-card-menu.png`).
   - The menu opens next to the pointer: **Upload** ≈(423,726), **Rename** ≈(426,766), a separator,
     **Duplicate** ≈(430,812), then **Delete ⟵Backspace** ≈(421,852).
   - The menu is **not** in the UIA tree (only HomeWindow plus a tooltip), so the screenshot is the
     only source for row positions.
   - ⚠ Delete sits 40 px under Duplicate. Click the vertical centre of the Duplicate row.
4. **Click Duplicate** (≈430,812), then poll the drafts folder for a new directory.
   - **`0914 (4)-copy-copy`** appeared within ≈1 s. CapCut appends `-copy`, so a copy of a copy
     is `…-copy-copy`.
   - **Agent-verified:** the structure diff of `master-before.json` against the new copy's
     `copy-baseline.json` is **No differences**.
   - The copy carries the rung-11 audio materials (loudnesses, realtime_denoises, vocal_beautifys)
     and **28 files in `Resources/`** (the Enhance-voice results and loudness analyses). No
     reprocessing is needed.
   - Master mtime is still **22:00:40.991**, unchanged.
5. **Home after duplicating** (`02-after-duplicate.png`):
   - The new card **0914 (4)-copy-copy** "264.8M | 07:31" is **first** (≈383,703), and the master
     0914 (4)-copy moved to second (≈566,703).
   - The rest shift one slot right, so re-read card names before every click.

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
- **Source:** "Short clip from the master (Recommended)". Make a CapCut **duplicate of `0914
  (4)-copy`** and keep one ≈30 s section (the opening, with the title) in the duplicate. The master
  stays untouched.
- **Reframe:** "CapCut Auto reframe (Recommended)". Use CapCut's AI auto reframe, which follows the
  face. Stop at any cost or upsell dialog.
- **Beat sync:** "Skip beat sync for now (Recommended)". No music and no beat cuts in this rung;
  the ladder keeps beat sync for later.
- **Length:** "About 30 s (Recommended)". End on a sentence boundary from the caption timings.
- **Section picked by the agent** (from `cap10/all-captions.txt`, timeline times on the master):
  **00:00:00:00 → 00:00:35:16 (35.533 s)**.
  - It opens with «بسم الله الرحمن الرحيم» and «زهجت من التاجيل وخلاص» under the title, and runs
    through «…فقلت خليني اوثق / الرحلة مش هاحكي كتير / او مش هاحضر كتير», which ends at 35.27 s.
  - The next caption «هاوثق اللي انا هاعمله» starts at 35.80 s, so the cut sits in that 0.53 s gap.
  - Why not ≈30 s: 29.90–31.50 «كده فقلت خليني اوثق» continues into «الرحلة…» at 31.70, so a
    cut near 30 s would split the sentence. The shorter clean option, 0 → 25.2 s, drops the
    "document the journey" hook that matches the title.
  - The section lies entirely inside master clip 0 (0–122.2 s), which has no punch-in. The title
    (1–4 s) is included. The PiP (96 s) and every caption after 35.8 s fall outside it.

## Open questions for the user
- Source, length, beat-sync yes/no, music choice.
