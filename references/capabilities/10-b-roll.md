# Capability 10: B-roll / overlay track (picture-in-picture)

## Status
- **Ladder status:** demonstrated
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14 (Claude Code). B-roll #6 as a muted upper-left PiP (40%, X −1557 /
  Y 528), 00:01:36:02–00:01:40:02, source in 2.000 s, on overlay track 3. Verified on the draft,
  frames, undo/redo and save.
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

### C. Open the copy and import the B-roll (executed 2026-09-14)
1. **Open the copy:**
   - Home, `scroll 1100 700 -5`, then a grid screenshot. The first card is **0914 (4)-copy**
     (≈383,703), newest after the rung-9 save.
   - Click it. The tree root is `MainWindow` on the first poll.
   - A screenshot taken ≈3 s later still showed a half-loaded top bar (only "Post") with a black
     media placeholder. The Details panel already read Name **0914 (4)-copy**. Wait ≈2 s more
     before keyboard input.
2. **Import:**
   - `focus`, then `key ctrl+i`. The native file dialog is found on the first poll (`find --type
     Edit --id 1148`).
   - `act set-value --type Edit --id 1148 --value "E:\videos\VID_20260501_233809.mp4"`, then
     `act invoke --type Button --id 1 --name Open`. The dialog is gone on the next poll.
3. **Observed** (`03-imported.png`):
   - The new media card **VID_20260501_233809.mp4** is at ≈(382,313), below the existing
     "Added" card, selected (cyan border).
   - The player switched to **"Previewing — video"**, showing the portrait clip, length 00:00:37:29.
   - Title bar: "Auto saved: 21:01:16".
4. **Agent-verified:**
   - `draft_content.json` shows **No differences** against the baseline. Importing does not touch
     the timeline or `materials.videos`, even though its mtime changed to 21:01:16.
   - The import is recorded in **`draft_meta_info.json` → `draft_materials`**:
     `E:/videos/VID_20260501_233809.mp4`, duration 37 958 000 µs.
   - The source file stays in place ("Imported media: Stay in original location").

### D. Playhead to 00:01:34:02 (executed 2026-09-14)
1. Click empty timeline space (≈1000,675). The header returns to "Player-Timeline 01".
2. Click the ruler at fit zoom at x = 229 + 2.7833 × t, here **x 491** for t≈94 s.
   - The playhead snapped to **00:01:31:29** (91.967 s), the start of caption «وهاعمل» at 91.97 s.
     As in rungs 5 and 8, ruler clicks snap to caption boundaries.
   - Read from a zoomed crop of the header and timecode (`05-hdr-tc.png`).
3. Press `key right` × **63** (30 fps: 2822 − 2759 frames) to reach 00:01:34:02.

### E. Drop the media card onto a new overlay track (executed 2026-09-14)
1. Run `drag 382 313 491 680 --steps 40 --hold 0.4`: from the media card to the empty area above
   the top TT row, at the playhead's x. The draft saved within 0.5 s.
2. **Agent-verified** (`overlay_check.py`):
   - A **new video track, index 3, `flag=2` (overlay)**, is appended after the two text tracks.
     Track order is `video, text, text, video`.
   - **1 segment**, file `E:/videos/VID_20260501_233809.mp4`. The material is **720×1280** (CapCut
     applied the −90° rotation).
   - **Start 94.067 s = 00:01:34:02**, exactly the playhead: the drop **snapped to the playhead**.
   - Duration **37.967 s** (the whole clip), source in 0.000 s, speed 1.0.
   - **Volume 1.0** (B-roll audio live, still to mute).
   - Clip scale 1.0, transform (0, 0), so it is full size and centred. Segment `render_index` 1,
     `track_render_index` 3.
   - `diff` vs baseline is **additive only**:
     - track_count 3→4, segment_count 247→248
     - materials videos / canvases / speeds / placeholder_infos / sound_channel_mappings /
       material_colors / vocal_separations +1 each
     - `+ track 3 [video] added with 1 segments`
     - Main track, captions and title are unchanged. The rung-7 keyframes are intact (2).
3. **Observed UI** (`07-dropped.png`):
   - The new overlay row sits at the **top of the timeline stack** (header y≈744: video icon, lock,
     eye, speaker, …), **above** the title TT row (≈794) and the caption TT row (≈827). The main
     video row moved down to ≈891.
   - The clip block is **selected** (white border), x≈489–597 at fit zoom.
   - The inspector switched to the video tabs **Video · Audio · Speed · Animation · Tracking ›**,
     with Basic / Remove BG / Mask / Retouch. Transform: Scale 100% (box ≈1800,257), Position X
     ≈(1666,352) / Y ≈(1788,352), Rotate, an alignment row, and **Blend** ✓.
   - The toolbar gained clip tools, including crop, mirror, freeze and HD icons.
   - **Player at 00:01:34:02:** the portrait B-roll fills the frame height, centred (player
     x≈916–1131).
   - **The overlay renders on top of the house caption.** Only the caption's outer letters peek
     out either side of the B-roll. The top-of-stack overlay track draws above the text tracks.
   - Consequence: the PiP must sit **clear of the lower third**. Moving the overlay below the text
     layers is an open question.

### F. Trim the overlay to the window with Q / W (executed 2026-09-14)
The overlay clip is still selected after the drop, and the playhead is at 00:01:34:02.
1. Press `key right` × 60 to reach 00:01:36:02, then **`key q`** (Delete left).
   - **Agent-verified (first poll):** start **96.067 s (00:01:36:02)**, source in **2.000 s**,
     duration 35.967 s, end unchanged at 132.033 s.
   - On an overlay track, Q trims the head *and keeps the clip's remaining part in place*. There
     is no ripple and no gap-close.
2. Press `key right` × 120 to reach 00:01:40:02, then **`key w`** (Delete right).
   - **Agent-verified (first poll):** start 96.067 s, **duration 4.000 s, end 100.067 s
     (00:01:40:02)**, source in 2.000 s. Volume is still 1.0.
3. **Gate built into the chain:** W runs only if the post-Q draft shows start 00:01:36:02 and
   source 00:00:02:00.
4. **Observed after W** (`08-trimmed.png`):
   - The clip block stays **selected**: a narrow white-bordered block at x≈493–509 on the top row.
   - The playhead sits at 00:01:40:02, exactly the clip's end, and **the player shows no B-roll
     there**. The segment end is exclusive, so the last B-roll frame is 00:01:40:01.
   - The inspector is still Video ▸ Basic (Scale 100%, Position 0/0).
5. `diff` vs baseline is still additive only, with one more line: **`materials.material_animations`
   245 → 246**. The trim gave the overlay segment its (empty) animation material, which the title
   and captions already had. Main track, captions and title are unchanged.

### G. Picture-in-picture: scale and corner position (executed 2026-09-14)
With the overlay clip selected and the inspector on Video ▸ Basic, each box takes click, then
`key ctrl+a`, `type <value>`, `key enter`. Poll `overlay_check.py` after each.

| Box | Coordinates | Value | Draft after (first poll) |
|---|---|---|---|
| Scale | ≈1795,257 | `40` | `clip.scale` **(0.4, 0.4)**, uniform |
| Position X | ≈1666,352 | `-775` | `clip.transform.x` **−0.40365 = −775 / 1920** |
| Position Y | ≈1788,352 | `265` | `clip.transform.y` **0.24537 = 265 / 1080** |

- **Units (as first assumed; WRONG, see G2):** the draft stores `transform.x = X/1920` and
  `transform.y = Y/1080`, which is correct. But the typed value is **not** canvas px. One unit is
  ½ canvas px. Negative X means left, positive Y means up.
- **Geometry intent:**
  - At 40% the portrait clip (full height 1080 → 607.5 px wide) becomes ≈243 × 432 px.
  - Centre at (−775, +265) from canvas centre puts the box ≈60 px from the left and top edges,
    spanning canvas x≈63–307 and y≈59–491.
  - That is **upper-left**: clear of the speaker's face (canvas x≈730–990), the lower-third
    captions (y ≥ ≈788) and the right-hand window.
- Start, duration and source in-point are unchanged (96.067 s / 4.000 s / 2.000 s).
- **Inspector confirmation** (`09-basic-after.png`): Scale **40%**, Uniform scale on, Position X
  **−775** / Y **265**, Rotate 0.00°, Blend ✓.

### G2. Frame check at X −775 / Y 265 exposed the Position units (2026-09-14, `frames/`)
- **Frames** (clip selected, so selection handles are visible):

  | Timecode | Result |
  |---|---|
  | 00:01:35:25 | No PiP. Caption «يعني في». |
  | 00:01:36:02 | PiP present, with caption «ابلكيشنز انا عايز اعملها». |
  | 00:01:38:00 | PiP present. |
  | 00:01:40:01 | PiP present, with caption «هتحللي مشاكلي الخاصة». |
  | 00:01:40:02 | PiP gone. |

  - The PiP never touches the face or the lower-third caption.
  - The overlay track mute shows as a cyan slashed speaker on the top row header
    (`11-muted-header.png`). Draft: track `attribute` **1**, segment volume stays 1.0.
- **But the PiP was not in the corner.**
  - Measured in the 1:36:02 frame (player frame x 71–753 = 682 px for 1920, so 0.3552):
    - box ≈ player x 232–318, y 77–228, which is **≈242 × 425 canvas px** (size correct)
    - centre at canvas **(574, 404)**, an offset of **(−386, +136)** from centre
  - Expected (−775, +265). The offset is **half** the typed values.
- **Correct units (agent-verified):**
  - `clip.transform` **1.0 = half the canvas**, so real offset = `transform.x × 960`,
    `transform.y × 540`.
  - The inspector Position box writes `transform.x = X/1920`, `transform.y = Y/1080`. **One
    Position unit = ½ canvas pixel.**
  - To offset a layer by *p* real px, type X = 2p (horizontal) or Y = 2p (vertical).
- **True upper-left for a 243 × 432 PiP with 60 px margins:**
  - centre offset (−778.5, +264) px
  - typed **X −1557, Y 528**, i.e. transform (−0.8109, +0.4889)

### G3. Corner placement at X −1557 / Y 528 (executed + agent-verified 2026-09-14, `frames2/`)
- Click the **Video** tab (≈1480,70), which returns to Basic. Then set Position X box `-1557` and Y
  box `528`.
  - Draft (first poll each): `transform` **(−0.8109375, 0.4888889)**.
  - Scale 0.4, start 96.067 s, duration 4.000 s, source in 2.000 s, and track attribute 1 (muted)
    are all unchanged.
- Refocus the timeline without seeking: click the overlay clip block (≈501,744). Then `right` ×7 /
  ×58 / ×61 / ×1.
- **Frames:**

  | Timecode | Result |
  |---|---|
  | 00:01:36:02 | PiP in the **upper-left corner**, caption «ابلكيشنز انا عايز اعملها» |
  | 00:01:38:00 | PiP present |
  | 00:01:40:01 | PiP present, caption «هتحللي مشاكلي الخاصة» |
  | 00:01:40:02 | PiP gone |

- **Measured box** at 1:36:02: player x≈92–178, y≈29–182, which is canvas **x≈59–301, y≈56–488**.
  Predicted by the half-canvas rule: 63–307 × 59–491. **Confirmed.**
  - The box sits on the plain wall, clear of the face (canvas x≈730–990) and the lower-third
    captions.
  - It never overlaps a text layer, so the overlay-above-text stacking doesn't show.

### H. Audio tab for a video clip (observed 2026-09-14, `10-audio-tab.png`)
- Inspector top tab **Audio** (≈1553,70) → sub-tabs **Basic · Voice changer**.
- Basic ✓ section:
  - **Volume** slider with a dB box at ≈(1790,257), default **0.0dB**, plus a keyframe ◇.
  - **Fade in** ≈(1790,311) and **Fade out** ≈(1790,365), both 0.0s.
  - **Normalize loudness** (Pro diamond, unchecked).
  - **Enhance voice** (Pro diamond, unchecked).
- The dB box has no obvious "0 volume" value. To silence B-roll, use the rung-2 **track mute**
  (speaker icon on the overlay row header), which is agent-verified as track `attribute` 1.

### B. Overlay route to reuse (from rung 2, Op 4, agent-verified)
- Drag a timeline segment from its **centre** straight up into the empty area above the main track.
  This creates a new video track, `flag=2` (overlay), at the **same time**. Starting near a clip
  edge grabs the trim handle instead.
- Track header icons on the overlay row: lock, eye, **speaker/mute** (mute = track `attribute` 1).

### I. Undo/redo gate, clean frame, save (executed + agent-verified 2026-09-14)
1. **Gate:** with timeline focus, press `key ctrl+z`.
   - First poll: `transform.y` **0.24537** (Y 265). X, scale and the muted attribute are unchanged.
   - Then press `key ctrl+shift+z`. First poll: **0.48889** again, with start, duration and source
     in identical.
   - Each Position box edit is one undo step.
2. **Attempted clean frame:** click empty space above the tracks at x≈502, y 690, then screenshot
   the player (`frames2/clean-inside.png`).
   - The click **seeked** to **00:01:38:20**, inside the window, where the PiP and caption «هتحللي
     مشاكلي الخاصة» are present.
   - It did **not deselect** the overlay clip: the selection handles (✕, corner dots, ⟳) are still
     drawn.
   - Above the overlay row, empty space seeks but keeps the selection, unlike rung 9, where the
     click was above the text rows with no overlay track. A truly clean frame needs another
     deselect route. Untested, so don't claim one.
3. **Save:** Menu (≈140,22) → Back to home page (≈183,303).
   - `HomeWindow` on the first poll, polled with `$atHome`, not `$home`.
   - Copy mtime 21:17:16 → **21:17:23**.
4. **Final on disk:**
   - `overlay_check`:
     - file `E:/videos/VID_20260501_233809.mp4` on track 3 (flag 2), **track attribute 1 (muted)**
     - **start 96.067 s / duration 4.000 s / end 100.067 s**, source in **2.000 s**
     - scale **0.4**, transform **(−0.8109375, 0.4888889)**
     - segment volume 1.0
   - `diff` vs baseline, additive only:
     - track_count 3→4, segment_count 247→248, `+ track 3 [video] added with 1 segments`
     - materials videos / canvases / speeds / placeholder_infos / sound_channel_mappings /
       material_colors / vocal_separations / material_animations +1 each
   - `track_styles`: 239 × house captions (y −0.73) plus 1 × title (y 0.7407). `title_check`: 1
     title. `keyframes`: 2 on 1 segment (rung 7).
   - **Scope:** every other project's mtime is unchanged, including 0707, 0720, 0728, the
     Arabic-titled one, 0914 (5) and 0914 (6).

## Wait conditions
- **File dialog:** poll `find --type Edit --id 1148`. It was present on the first 0.5 s poll, and
  gone on the next poll after Open.
- **Media card** after import: about 6 s. Screenshot. The draft does not change, so only
  `draft_meta_info.json` can signal it.
- **Drop / Q / W / Scale / Position / mute:** poll `overlay_check.py` for the expected value.
  Every one landed on the first 0.5 s poll.
- **Frames:** wait ≈0.9 s after stepping, and read the timecode in the captured image.
- **Save:** tree root `HomeWindow`, plus the draft mtime.

## Verification
- **Draft:**
  - a new overlay video track (flag 2) with exactly one segment from the chosen file at the stated
    window and source in-point
  - scale and transform as typed, track attribute 1
  - `diff` vs baseline additive only
  - captions, title and keyframes unchanged
- **Frames:** nothing at start − 7 frames; PiP at the first frame, middle and last frame; nothing
  at the end frame (exclusive). Measure the PiP box against the prediction. It must not cover the
  face or the lower-third captions.
- **Audio:** track mute icon cyan/slashed plus `attribute` 1. There is no playback listening test,
  since the agent can't hear. The track mute is the verifiable signal.
- **Gate:** one Ctrl+Z reverts the last Position edit; Ctrl+Shift+Z restores it.
- **Save:** Back to home page, then the final checks on disk.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Clip | #6 `VID_20260501_233809.mp4` | User taste choice | Contact sheet first |
| Window | 00:01:36:02 → 00:01:40:02 (4.000 s) | Shot-specific | Start at the caption where the topic is spoken; cover 1–3 captions |
| Source in-point | 2.000 s | Clip-specific | Skip the unsteady first ≈2 s (frame strip) |
| Scale | 40% (≈243 × 432 px for a portrait clip) | Semi-universal for PiP | Readable but secondary; ≤ ≈25% of frame width |
| Position | X −1557, Y 528 (upper-left, ≈60 px margins) | Shot-specific | Typed unit = ½ px. Offset p px means typing 2p. Keep clear of the face and captions. |
| Audio | Overlay track muted (attribute 1) | Universal for B-roll over speech | Speaker keeps talking |

## Undo / recovery
- Each box edit, Q, W, mute and drop is its own undo step. The gate above reverted and restored
  Position Y.
- **Remove the B-roll entirely:** select the overlay block, then Delete (not Backspace inside a
  text field). Check that `overlay_check.py` shows 0 overlay segments and the track count is back
  to 3. The imported media card can stay: it does not touch `draft_content`.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| After import, a timeline ruler click (491,628) left the header on "Previewing — video", and the timecode still showed the preview clip (00:00:00:00 / 00:00:37:29). | Import auto-selects the new media card and enters media preview. A ruler click does not leave media preview. | First click empty timeline space (≈1000,675), which is the rung-9 route out of preview and also seeks. Then click the ruler. Always crop the header and timecode after the click. |

## Tree coverage notes

## User choices (2026-09-14)
- **Clip:** #6 `E:\videos\VID_20260501_233809.mp4` (38.06 s, portrait, speaker working at the
  purple-lit desk). User's words: "6 working at desk (Recommended)".
- **Moment:** timeline **01:36** over «ابلكيشنز انا عايز اعملها» (caption starts 96.07 s), about
  4 s. User's words: "01:36 «ابلكيشنز انا عايز اعملها» (Recommended)".
- **Form:** **picture-in-picture**, scaled into a corner clear of the face and the lower-third
  captions, B-roll muted. User's words: "Picture-in-picture (Recommended)".
- **Clip 6 probe** (`ffmpeg -i`, read-only):
  - Duration 38.06 s. Stored as h264 1280x720 with **displaymatrix rotation −90°**, so it displays
    **portrait 720×1280**.
  - It has a **stereo AAC audio track** (48 kHz). The B-roll must be muted so only the speaker is
    heard.
  - Opening-frames strip at 0/1/2/4/8 s: `cap10/clip6/clip6-strip.png`.
- **In-point decision** (from the strip):
  - At 0 s the camera is still settling (tilted desk, no face). From ≈1 s the speaker is at the
    purple desk, and the shot is steady from ≈2 s. **Source in-point = 2.000 s.**
  - Keyboard-exact route: place the clip on the overlay track starting at **00:01:34:02**. Then,
    with the playhead at 00:01:36:02 and the clip selected, press **Q** (delete left). Then at
    00:01:40:02 press **W** (delete right).
  - Overlay tracks don't ripple, so the clip should keep start 96.067 s with source 2.000 s. Verify
    in the draft.
- **Planned overlay window:** **00:01:36:02 → 00:01:40:02** (96.067–100.067 s, 4 s). It covers
  captions «ابلكيشنز انا عايز اعملها» (96.07), «ليا انا» (98.07) and «هتحللي مشاكلي الخاصة»
  (98.67–100.07). The B-roll source in-point is its own 0 s unless the opening frames are
  unusable.
- **Baseline** before any rung-10 change: `evidence/2026-09-14/cap10/baseline.json`
  - 3 tracks, 247 segments, draft 20:31:27
  - `diff` vs rung-9 `final.json` = No differences
- **Summary pitfall:** don't pipe `draft_inspect.py summary --json` into `Select-Object -First N`.
  The truncated pipeline exits 255, although this time the JSON had already been written. Redirect
  stdout to `$null` instead.

## Open questions for the user
- ~~Which B-roll clip / moment / form~~: answered above.
