# Capability 08: Auto captions + styling

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Consent:** "Approve, start Cap 8". The option text said captions are Pro and may use credits,
  as in rungs 3–5.
- **Practice project:** `0914 (4)`, the cleaned, punched and pushed-in talking-head take of
  `VID_20260720_190542.mp4` from rungs 4–7. 7:30.533, 7 segments, dense Egyptian Arabic speech.
  - `0914 (1)` was opened first and rejected without edits: `VID_20260623_152043` is a gym clip
    whose transcript is background-music lyrics (rung 3 E), so captions wouldn't test talking-head
    captioning.
  - Generation on 7:30 takes about 2 min (rung 4: ≈122 s for 8:43).
- **Evidence:** `evidence/2026-09-14/cap8/`

## Goal
Generate CapCut's Auto captions for the talking-head take (language stated) and give them one
readable style: font/size, colour, stroke or background, and position in the lower third. Apply it
to every caption. Spot-check timing against the speech, fix at least one caption error natively,
and record the credit/Pro gating and what options exist for speaker-identified captions.

## Preconditions
- Rungs 0–7 approved.
- Tools reused:
  - Captions tab → Auto captions → Generate, and the `LVLoadingDialog` "Generating captions... N%"
    wait (rung 4)
  - `draft_inspect.py words` for per-word timings (rungs 4–5)
  - clip selection, ↓ cut points, ruler + arrows (rungs 1–2)

## Plan
1. **Generate:** open `0914 (1)` and go to Captions → Auto captions. Record every option (spoken
   language list, bilingual, filler words, anything about speakers), keep Auto detect or pick
   Arabic, then Generate. Wait on the loading window.
2. **Map styling:** select a caption and record the inspector tabs (Text / Basic / Presets /
   Bubble / Effects / Animation…) and whether edits apply to all captions or only one ("Apply to
   all", caption track selection).
3. **Style:** one preset or a manual style (e.g. white text, black stroke, bold, larger size, lower
   third). Verify in the draft (`materials.texts[].content` styles, `text_templates`, clip
   transform) and on the player.
4. **Timing spot-check:** 3 captions. Compare word timings with the transcript and the frames where
   speech starts.
5. **Fix one caption error natively:** edit the text of a misrecognised word, verify in the draft.
6. **Undo/redo, save.**

## Procedure

### 0. Where caption style lives in the draft (read-only look at the user's `0728`, 2026-09-14)
- **Caption segments:** a `text` track (flag 1) holds one segment per caption. The segment's
  `clip.transform.y` places it on screen; `0728` uses **−0.73** (lower third, same units as rung 6
  position: value / half canvas height).
- **Per-caption material:** `materials.texts[]`. Fields to diff when styling:
  - `font_size` (10.5), `text_size` (30), `font_name`/`font_path`/`font_id`
  - `text_color` (`#ffffffff`), `text_alpha`
  - `border_color`, `border_width`, `border_alpha` (stroke)
  - `background_style`, `background_color` (`#1D1D1DFF`), `background_alpha`,
    `background_round_radius`
  - `has_shadow` and `shadow_*`
  - `alignment`, `line_spacing`, `letter_spacing`, `bold_width`, `italic_degree`, `underline`
  - `preset_id` / `preset_name` / `style_name` / `caption_template_info` (presets and templates)
  - `words` (per-word timing), `recognize_*` / `language`
- **`content`** is a JSON string: `{"text": "...", "styles": [{"fill": {"content": {"solid":
  {"color": [r,g,b]}}}, "font": {"path", "id"}, "size": 10.5, "effectStyle": {...},
  "range": [0, 4]}]}`. Rich-text runs, so one caption can hold several styles.

### A. Auto captions form (observed 2026-09-14, `captions-panel.png`)
- **Open:** asset tab **Captions** (≈424,73), which lands on the left sub-list **Auto captions**
  (selected). The other sub-items are Templates ▾, Auto lyrics and Add captions. The editor title
  read **0914 (4)**.
- **Form**, top to bottom:

  | Control | Position | Default |
  |---|---|---|
  | Spoken language dropdown | ≈(383,160) | **Auto detect** |
  | Bilingual captions (purple Pro diamond) dropdown | ≈(383,255) | **None** |
  | Identify filler words (Pro diamond) toggle | ≈(565,313) | **ON** |
  | Delete current captions | ≈(185,544) | unticked |
  | Generate (cyan, "Pro" tag) | ≈(539,544) | |

- **No speaker-identification control** is present in this form on 9.4.0.4015, so speaker-ID
  captions aren't reachable here. Check the dropdown and the post-generation caption inspector
  before concluding it doesn't exist.
- **Tree:** only `MainWindow`, `editPanelLoader.editWin` and `MainWindow.surface_main` are named.
  The form is screenshot-only.
- **Spoken language dropdown** (executed 2026-09-14, `language-dropdown.png`):
  - Clicking the field opens a popup list (a new `Qt622QWindowIcon` in `cc.py windows`).
  - Visible list: **✓ Auto detect, Arabic, Bengali, Burmese, Chinese, Dutch**, then more
    alphabetically (it scrolls).
  - Rows are ≈40 px apart starting ≈(241,205).
  - No speaker option in the list.
- **Language chosen: Arabic** (≈241,245), so the language is stated rather than auto-detected.
  The footage is Egyptian Arabic.
- **Choosing Arabic hid the "Identify filler words" toggle** (`language-arabic.png`). The form then
  showed only Spoken language, Bilingual captions, Delete current captions and Generate. Filler-word
  identification seems to be offered only for some languages (or only under Auto detect).

### B. Generate (executed + agent-verified 2026-09-14)
- **Click Generate** (≈539,544). No credit, confirm or upsell dialog appeared. Right away a
  modal "Generating captions... N%" with a **Cancel** button appeared over the editor.
- **Tree:** `Window id="Generating captions... 0%" cls=LVLoadingDialog_QMLTYPE_*`
  @ (760,400)–(1160,630). **The progress text is in the AutomationId; the Name is "CapCut".**
  - `cc.py wait-for --contains "Generating captions"` timed out because `--contains` matched only
    Name/HelpText.
  - **Fixed:** `--contains` now also matches AutomationId.
  - The reliable completion signal remains the draft gaining a non-empty `text` track.
- **Duration:** clicked 15:48:39, draft saved with captions 15:49:59, so **≈80 s for 7:30** of
  Arabic speech. Rung 4 took ≈122 s for 8:43, so figure about 11 s per minute of footage.
- **Result:**
  - New text track (flag 1) with **239 caption segments**; `materials.texts` 0 → 239;
    `material_animations` 5 → 244 (one per caption).
  - The first caption «بسم الله الرحمن الرحيم» runs 0.600 → 1.567 s.
  - Draft diff against baseline: exactly the added track and those material counts. Video segments
    unchanged.
- **Timeline:** a new caption row labelled **TT** (with lock and eye) sits above the video track at
  y≈763 (fit zoom). At fit zoom the captions are thin orange blocks.
- **Default caption style** (all 239 share one style signature):

  | Field | Value |
  |---|---|
  | `type` | `subtitle` |
  | `language` | `ar-SA` |
  | Font | `…/Resources/Font/SystemFont/en.ttf` (system font) |
  | `font_size` | 7.0 |
  | `text_color` | `#FFFFFF` |
  | Border | `border_width` 0.08, empty `border_color` |
  | Background | `background_style` 0, no colour |
  | Shadow | `has_shadow` False |
  | `alignment` | 1 (centre) |
  | Preset | none (`preset_id` empty) |
  | Position | `clip.transform.y` **−0.73**, lower third |

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
