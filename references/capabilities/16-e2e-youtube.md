# Capability 16: End-to-end talking-head YouTube edit

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** a new agent-owned project for the chosen raw take (to be created). No
  existing project is touched.
- **Evidence:** `evidence/2026-09-15/cap16/`

## Goal
Take one raw, unused talking-head take all the way to a finished YouTube video, using **only
approved rungs** and their documented procedures, then export it. Every stage is verified in the
draft and in frames, and the final file is checked with ffmpeg.

## User choices (2026-09-15)
- **Footage:** "New talk take (Recommended)", an unused raw take. Show frames of candidates first.
- **Steps:** all of them:
  - "Cleanup (Recommended)": rungs 3–5, i.e. Transcript pauses/filler removal, bad takes, and a
    waveform tidy-up
  - "Jump cuts + push-ins (Recommended)": rungs 6–7
  - "Captions + title (Recommended)": rungs 8–9, using the house style (Arabic-only, Classic black
    box, lower third) and an animated Arabic title
  - "B-roll + audio + logo": rung 10 PiP B-roll, rung 11 Reduce noise + Enhance voice, rung 14
    Yousef AI logo top-right
- **Loudness:** "Skip normalize (Recommended)". Don't apply Normalize loudness (−23 LUFS); measure
  the exported file instead.
- **Export:** "1080p30 H.264 → exports (Recommended)", the rung-15 route: `E:\videos\exports`,
  cloud sync off, ffmpeg verification.
- **Standing rules still apply:**
  - credits OK for Transcript and Auto captions
  - Pro tools: "run; stop if a cost appears"
  - never touch the user's projects
  - native UI only, draft JSON read-only
  - confirm purchases, cloud, deletes and downloads

## Plan (stage gates, each verified before the next)
1. **Pick the take:** a read-only frame sheet of unused talk candidates; the user picks.
2. **New project + import** (rung 13 B route), then drop the take on the main track (baseline
   duration).
3. **Cleanup:**
   - rung 3: Transcript ▸ Remove filler words (pauses/repeats/fillers) ▸ Delete
   - rung 4: bad takes via the transcript / captions
   - rung 5: the waveform/gap pass with `scripts/tighten_gaps.py`
4. **Jump cuts / push-ins** (rungs 6–7): punch-in scale on alternate segments, plus a few eased
   push-ins.
5. **Captions + title** (rungs 8–9): Auto captions in Arabic, the Classic black box template in the
   lower third, text fixes; then an Arabic text-template title near the start.
6. **B-roll** (rung 10): a muted PiP at a stated moment, from the unused footage.
7. **Audio** (rung 11): Reduce noise + Enhance voice on all main clips (async; wait for results).
   **No Normalize.**
8. **Logo** (rung 14): `public/brand/logo-ink-tight.png` on the top overlay track, full length,
   12 % top-right. Check legibility over the footage.
9. **Save**, undo/redo spot gates, scope check.
10. **Export** (rung 15) and verify the file: streams, duration vs the draft, loudness, and frames
    at captions/title/B-roll/logo points.
11. Write up, contact sheet, ask for approval.

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

## Open questions for the user
- Which raw take (frame sheet pending).
