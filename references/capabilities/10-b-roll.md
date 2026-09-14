# Capability 10: B-roll / overlay track (picture-in-picture)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0914 (4)-copy` (agent-owned duplicate of `0914 (4)`). It carries the
  approved rung 4–9 edits: cuts, punch-ins, the push-in, Arabic house captions, and the opening
  title. 7:30.533.
- **Evidence:** `evidence/2026-09-14/cap10/`

## Goal
Put B-roll from `E:\videos` on an **overlay video track** above the talking head, at a stated
time and duration, in two forms:
- **cutaway:** full-frame B-roll covering the speaker while his audio continues
- **picture-in-picture:** B-roll scaled down in a corner

Then verify placement, audio, layering with the captions and title, and undo/redo.

## Preconditions
- Rungs 0–9 approved. House style (`references/house-style.md`): captions stay Arabic-only in the
  lower third. The B-roll must not hide them. Check that the caption track renders above the overlay.
- Source media stays in place (project setting "Imported media: Stay in original location"). The
  agent never copies, moves or edits files in `E:\videos`.
- The B-roll clip is chosen by the user from a contact sheet, because content choice is a taste
  decision.

## Plan
1. **Pick B-roll:** extract a frame per candidate with CapCut's bundled ffmpeg (read-only). Show a
   contact sheet, and the user chooses the clip plus where in the talk it belongs.
2. **Import:** Media ▸ Import (Ctrl+I, the rung 3 route) the chosen file into `0914 (4)-copy`.
   Verify it is in the media panel and the draft `materials.videos` gains it.
3. **Place as overlay:** playhead at the stated time, then drag or add the clip onto a **new track
   above the main video** (not inserted into the main track). Record how CapCut creates the overlay
   track, and whether the main track shifts (ripple) or stays put.
4. **Trim** the overlay to the stated duration (e.g. 3–4 s) with the rung 2 trim route.
5. **Audio:** mute the B-roll (volume 0 / track mute) so the speaker's voice continues. Verify
   `volume` in the draft.
6. **Cutaway vs PiP:**
   - cutaway: full frame (scale 100%)
   - PiP: Transform Scale ≈35–40% plus Position toward a corner clear of the captions and the
     speaker's face
   - Check frames inside the overlay for both.
7. **Layering check:** captions and the title render above the overlay (render order / track
   order).
8. **Verify:** draft diff (new video track, segment start/duration, source in/out, clip transform,
   volume), frames before / inside / after, main track unchanged. Then the undo/redo gate, Back to
   home page save, and a scope check.

## Procedure

### A. Candidate B-roll (executed 2026-09-14, read-only)
- **Frames:** CapCut's bundled `D:\Bytedance\CapCut\Apps\9.4.0.4015\ffmpeg.exe`. For each clip, run
  `-ss 3 -i <src> -frames:v 1 -vf scale=384:-2` into `evidence/2026-09-14/cap10/candidates/`, then
  build a PIL contact sheet (`broll-candidates-sheet.png`).
- Durations and sizes come from `ffmpeg -i` (stderr). Every candidate reports **1280x720**, but
  many are **portrait** phone clips, where the 3 s frame is 9:16 (rotation metadata).

  | # | File | Duration | Frame shows |
  |---|---|---|---|
  | 1 | VID_20260416_203431 | 4:21.88 | landscape, office, three people at a desk |
  | 2 | VID_20260425_174820 | 8:04.32 | landscape, close-up of speaker in a grey tee (talking head) |
  | 3 | VID_20260428_064459 | 1:21.17 | landscape, speaker selfie, dim |
  | 4 | VID_20260501_111338 | 1:09.94 | landscape, empty chair and wall |
  | 5 | VID_20260501_233737 | 0:23.58 | **portrait**, purple-lit desk setup: laptop, monitor, light |
  | 6 | VID_20260501_233809 | 0:38.06 | **portrait**, speaker working at the purple-lit desk |
  | 7 | VID_20260530_182728 | 1:00.70 | portrait, Nile river view and a table |
  | 8 | VID_20260623_150351 | 0:34.73 | landscape, gym floor |
  | 9 | VID_20260626_202525 | 0:52.26 | portrait, office, two people at desks |
  | 10 | VID_20260628_173114 | 0:30.35 | portrait, gym bench press |
  | 11 | VID_20260721_110250 | 10:41.89 | landscape, the same room as the talking head, empty chair |

- **Framing implication:** a portrait clip as a full-frame cutaway on the 16:9 canvas leaves
  pillarbox bars unless scaled to fill (crop). PiP suits portrait clips naturally.

### A2. Moments in the talk that suit B-roll (read-only caption search)
- `cap10/caption_search.py "0914 (4)-copy" <keywords…>` lists house captions (template 边框弹出黑色)
  containing the keywords, with timeline start and duration. With no keywords it dumps all 239
  captions (`cap10/all-captions.txt`).
- Hits used to offer placements:

  | Start | Caption | Topic |
  |---|---|---|
  | 01:36.07 (+1.7 s) | «ابلكيشنز انا عايز اعملها» | apps he wants to build |
  | 01:54.90 (+1.4 s) | «هافتح الكاميرا واصور» | "I'll open the camera and film" |
  | 03:59.27 (+3.3 s) | «…ديزاين ماركتنج كودنج» | AI tools for design, marketing, coding |
  | 05:26.40 (+2.0 s) | «او بابلكيشنز خاصة بالاي اي» | AI apps. Inside the rung-7 push-in segment (262.5–359.467 s). |
  | 06:22.17 (+2.0 s) | «عايز التزم اني اعمل فيديو او اصور» | commit to making videos |

### B. Overlay route to reuse (from rung 2, Op 4, agent-verified)
- Drag a timeline segment from its **centre** straight up into the empty area above the main track.
  This creates a new video track, `flag=2` (overlay), at the **same time**. Starting near a clip
  edge grabs the trim handle instead.
- Track header icons on the overlay row: lock, eye, **speaker/mute** (mute = track `attribute` 1).

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
- **Clip:** #6 `E:\videos\VID_20260501_233809.mp4` (38.06 s, portrait, speaker working at the
  purple-lit desk). User's words: "6 working at desk (Recommended)".
- **Moment:** timeline **01:36** over «ابلكيشنز انا عايز اعملها» (caption starts 96.07 s), about
  4 s. User's words: "01:36 «ابلكيشنز انا عايز اعملها» (Recommended)".
- **Form:** **picture-in-picture**, scaled into a corner clear of the face and the lower-third
  captions, B-roll muted. User's words: "Picture-in-picture (Recommended)".

## Open questions for the user
- ~~Which B-roll clip / moment / form~~: answered above.
