# Capability 08: Auto captions + styling

## Status
- **Ladder status:** demonstrated, round 3 (awaiting user approval).
  - **Round 3 result (2026-09-14, `0914 (4)-copy`):**
    - Arabic-only Auto captions (1 track × 239)
    - the user-chosen "Classic: black box" word-by-word template, lower third (y −0.73)
    - «حاجة 1» → «حاجة واحدة» fixed
    - frames checked inside a short caption, the longest caption and the fixed caption
      (00:04:07:21 «حاجة واحدة بس هاشترك»; 00:04:08:21 «في كلود في الغالب»)
    - undo/redo gate passed, saved
    - original and user projects untouched
    - Evidence: `evidence/2026-09-14/cap8c/` (sheet: `arabic-template-sheet.png`).
  - **User feedback on round 2 (2026-09-14):** "We should have only one language Arabic, instead
    of bilingual Arabic + English".
  - **Round 3 plan** on `0914 (4)-copy`:
    1. Regenerate Auto captions Arabic with **Bilingual: None** and Delete current captions ✓.
    2. Re-apply the user-chosen black-box template.
    3. Position it in the lower third.
    4. Re-apply the «حاجة 1» → «حاجة واحدة» fix.
    5. Verify, then ask again.
  - **Round 3 pre-check (agent-verified 2026-09-14):**
    - The copy's draft mtime was **19:03:19**, after the agent's 17:12:46 save. It was presumably
      re-saved when the user opened the copy to review.
    - Read-only checks showed nothing else changed:
      - all 478 captions have identical text and timing
      - both text tracks keep their y positions
      - the 7 video segments match rung 7, and seg 4 still has 2 keyframes
    - Round-3 baseline: `evidence/2026-09-14/cap8c/round3-baseline*.json`.
  - **Round 3, step 1: back to one language (executed 2026-09-14):**
    1. Open `0914 (4)-copy` (first home card; the title bar confirmed it), then Captions ▸ Auto
       captions (≈57,131).
    2. The form **remembers the last choices**: Spoken language Arabic, Bilingual captions
       **English**.
    3. Open the Bilingual dropdown (≈383,255). English is ticked ✓ at the bottom of the visible
       list, and **None** is the first row (≈243,300).
    4. Choose None, then tick Delete current captions and Generate, as in round 2.
       - The first attempt failed (see Failure modes: a `focus` call closed the popup). On the
         retry, with the dropdown opened and None clicked in one command, the field read
         **None**.
       - The draft was unchanged by the form edits.
    5. **Generate (executed + draft-verified 2026-09-14 19:13:01):** Arabic · Bilingual None ·
       Delete current captions ✓. The draft saved **3 s** later and the loading window was gone by
       4 s (cached recognition). No dialogs.
       - **Result:**
         - **one text track, 239 captions, all `ar-SA` `sub_type` 0**, plain `texts` in the default
           style at y **−0.73**
         - the English track and **both templates removed**: `text_templates` and `effects` are no
           longer in the materials; `texts` 478 → 239; tracks 3 → 2
       - Video segments unchanged.
       - ⚠ `regen_check.py`'s comparison printed "False (0 before)". The pre-regeneration dump
         came from a script that doesn't resolve template materials, so every language was None.
         That's a tooling artefact, not a mismatch. Compare against a template-aware or
         pre-template dump.
       - **Correct comparison (agent-verified):** the regenerated 239 Arabic captions are
         **identical in start, duration and text** to round 2's bilingual Arabic track **and** to
         round 1's first generation (before its text fix). CapCut reuses the same cached
         recognition on every regeneration.
         - So a regeneration is **deterministic but destructive**: caption 129 reads «…حاجة **1**
           بس…» again, and every manual fix must be re-applied.
         - Style resets to the default: `font_size` 7, white, `border_width` 0.08, system font.
         - The video track still has 7 segments, and seg 4 keeps its 2 push-in keyframes.
       - **Timeline:** a single **TT** caption row at y≈763 above the video. Undo/redo arrows are
         active in the toolbar.
    6. **Re-apply the template:**
       1. Ruler click (240,628), then Ctrl+= ×4. The view shows 00:05 → 00:40, ≈44.6 px/s, with
          caption pills on the y≈763 row.
       2. Click the pill «بقالي فترة عايز اعمل» (≈300,763).
       3. Text ▸ Templates (1623,127), then the Classic chip (1653,271). Screenshot the grid
          **before** clicking a tile, because a tile click applies immediately.
       - Pre-template snapshot: `cap8c/styles-before-template.json` (1 track × 239 `texts`, y −0.73).
       - **Observed** (`templates-classic.png`):
         - The pill got a white border. The player shows the selected caption «بقالي فترة عايز اعمل
           براند او» with its bounding box.
         - The checkbox reads **Apply to all main captions ✓**. With one language, every caption
           is a main caption.
         - The Classic grid loaded; the black-box tile is row 1 left.
         - ⚠ The grid sat **≈8 px lower** than in round 2 (tile text y≈371, ☆ y≈392). Aim for
           the tile body left of the ☆, ≈(1480,363), from a fresh screenshot each time.
       4. **Applied (executed + draft-verified 2026-09-14 19:16:39):** click the black-box tile
          (1480,363). The draft saved **2 s** later.
          - `cc.py` printed "WARN: could not confirm CapCut is foreground". The click still landed
            (draft changed as intended), but always confirm by draft or screenshot after that
            warning.
          - **Result:**
            - 1 text track × **239 `text_templates` "边框弹出黑色"** (7331662668685774086)
            - materials `text_templates` 0 → 239, `effects` 0 → 239, `texts` 239
            - template-aware check: **all 239 captions have identical start, duration and text**
          - **Position stayed at y −0.73 (−788 px, lower third) for all 239.** In round 2 the same
            template moved bilingual tracks to −0.28 (Arabic) and −1.09…−1.20 (English). CapCut
            re-lays out only when two languages have to be stacked. Single-language captions keep
            their position.
       5. **On the player** (`cap8c/midframes/`, agent-verified 2026-09-14):
          - **Longest caption** (seg 122) at 00:03:50:06: «بشتغل بكلود بشكل كبير», with the black
            box on «بشتغل». At 00:03:51:16: «وشايف ان هو», box on «وشايف».
          - The text is bold white Arabic with correctly joined letters, in the **lower third**
            over the shirt/desk line, fully inside the frame, and paged into short chunks.
          - Frames `a`/`b` (00:00:02:12, 00:00:03:07) show **no caption, correctly**: the
            zoomed-view ruler click at x 300 landed at ≈1.6 s, inside the silence between caption 0
            (ends 1.567 s) and caption 1 (starts 3.800 s).
          - At Ctrl+= ×4 the ruler reads 00:05 at x≈455, so x = 455 + (t − 5) × 44.6. Use Home + ↓
            to land exactly on caption starts instead of ruler clicks.
          - **Short caption** (caption 1, via Home + ↓×3, then → ×25) at 00:00:04:19: «زهجت من
            التاجيل وخلاص», box on «التاجيل». Lower third, inside the frame, readable over the
            shirt and desk.
       6. **Locating caption 129** (246.133 → 249.067 s) for the text fix:
          1. Shift+Z (fit), then ruler click (945,628). The playhead snapped to the video join
             00:04:05:22 (245.733 s), the nearest cut.
          2. Ctrl+= ×4 gives ≈46 px/s (04:00 at x≈700, 04:10 at x≈1160).
          - The pill «فانا لو هاشترك في حاجة 1» spans **x≈958–1092 on the y≈763 row**, starting just
            right of the 04:05:22 video join.
          3. Ruler click (1030,628), then click the pill (1020,763), then Text ▸ **Basic**
             (≈1516,127).
          - **Observed** (`caption129-selected.png`, `caption129-basic.png`):
            - The pill has a white border. Playhead 00:04:07:21.
            - The player shows «حاجة **1** بس هاشترك», with the template's black box on «1». The
              digit is visibly highlighted as a word.
            - Sub-tabs are **Basic · Templates · Effects** (no Bubble with a template).
            - **Apply to all main captions ✓**. Font **Staatliches-Regular**, size **11**.
            - The **text box** is in the same place as round 1 (≈1510–1890 × 200–280), showing
              «فانا لو هاشترك في حاجة 1 بس هاشترك في كلود في الغالب».
          - Pre-fix dump (template-aware): `cap8c/texts-before-fix.json`.
       7. **Text fix on a templated caption (executed + draft-verified 2026-09-14 19:21:36):**
          1. Click in the text box (1700,240), then `key ctrl+a`.
          2. `type "فانا لو هاشترك في حاجة واحدة بس هاشترك في كلود في الغالب"`.
          - **Autosave ran repeatedly while typing:** polls read «فا» (0.1 s), «فانا لو هاشت»
            (2.2 s), «…واحدة بس هاش» (6.3 s), «…كلود ف» (8.3 s), then the full text at **10.4 s**.
            Keep polling until the text equals the full target.
          - **Template-aware before/after:** 239 → 239 captions, **exactly 1 changed**: #129 text
            `…حاجة 1 بس…` → `…حاجة واحدة بس…`. Start, duration, kind (template) and y (−0.73)
            unchanged, and no other caption touched.
          - The template stays on the edited caption. The fix doesn't drop it back to plain text.
          - **Player** (`caption129-fixed.png`): «حاجة **واحدة** بس هاشترك», with the word
            «واحدة» in place of the digit.
       8. **Undo / redo / save (agent-verified 2026-09-14):**
          - Click the ruler first so keys go to the timeline, not the text box.
          - **Ctrl+Z (once):** only the last typed letter was removed («…الغالب» → «…الغال»). Text
            undo is per character with a template too.
          - **Ctrl+Shift+Z:** the template-aware dump is **identical to the verified fix**, which
            was the gate for saving.
          - **Menu ▸ Back to home page:** saved (19:23:11); tree root `HomeWindow`.
          - **Final state on disk:**
            - **1 text track, 239 captions, all `text_templates` "边框弹出黑色", all `ar-SA`, all
              y −0.73**
            - identical to the verified fix
            - materials `texts` 239, `text_templates` 239, `effects` 239
            - video 7 segments, seg 4 keeps its 2 push-in keyframes
          - **Scope:**
            - the original `0914 (4)` is unchanged since before the duplicate (16:25:54.656)
            - the user's projects (0707, 0720, 0728, the Arabic-titled one) and `0914 (5)` are
              unchanged
       9. **Round-3 recipe (Arabic-only captions with a caption template):**
          1. Captions ▸ Auto captions: Spoken language **Arabic**, **Bilingual None**. The form
             remembers the last choice, so check it. Tick **Delete current captions ✓**, then
             Generate.
          2. Select any caption → Text ▸ **Templates** → chip → tile. It applies to all main
             captions and keeps y −0.73 for single-language captions.
          3. Re-apply known text fixes: select the caption → Text ▸ Basic text box → Ctrl+A → type
             the full text. Poll until it's fully saved.
          4. Check frames inside captions, then the undo/redo gate, then Back to home page, then the
             template-aware dump.
  - Round 1 (Arabic captions, outline preset, size 11, text fix) is below. User feedback on round 1
    (2026-09-14): **"Try bilingual captions, and restyle"**.
  - **Round 2, demonstrated 2026-09-14 on `0914 (4)-copy`:**
    - Bilingual Arabic + English captions (2 × 239)
    - the user-chosen **"Classic: black box"** caption template (`边框弹出黑色`, word-by-word
      highlight) on both tracks
    - English moved from off-frame (Y −1292) to Y −700
  - **Verified:**
    - all 478 captions keep text and timing
    - on-screen frames inside captions for both languages
    - undo/redo
    - saved
    - original `0914 (4)` and the user's projects untouched
  - See G.
  - **Choices:** restyle with a **caption Template** (Text ▸ Templates); bilingual second language
    **English**; work on a **CapCut duplicate of `0914 (4)`** so the verified state above stays
    intact.
  - **Evidence for this round:** `evidence/2026-09-14/cap8b/`.
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** 2026-09-14, Claude Code, on `0914 (4)`.
  - Arabic Auto captions: 239 captions in ≈80 s, no credit prompt.
  - Style applied to all: preset "white with black outline", font size 7 → 11, lower third.
  - One recognition error fixed natively: «حاجة 1» → «حاجة واحدة».
  - Timing spot-checked at 3 places, with caption boundaries frame-exact.
  - Undo/redo verified (text undo is per character).
  - Saved via Back to home page. Final checks: 1 style signature × 239; texts identical to the
    verified state; the structure diff against baseline is exactly the added caption track; rung-7
    keyframes intact.
- **Scope check:** the user's projects (0707, 0720, 0728, the Arabic-titled one) have unchanged
  mtimes. `0914 (1)` was opened and closed without edits (diff: No differences; its mtime changed
  from the save on exit). `0914 (5)` wasn't touched.
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

### C. Caption inspector (observed 2026-09-14, `caption-selected.png`)
- **Selecting a caption:**
  1. At fit zoom captions are slivers. Click the ruler near the target, then `key ctrl+= --repeat 4
     --gap 0.4`; the zoom centres on the playhead.
  2. Caption blocks become orange pills with text and an **A☰** icon on the TT row (y≈763).
  3. Click the ruler inside a pill so the player shows it, then click the pill (e.g. 573,763).
  - The pill gets a white border. The player shows the caption with a bounding box and
    rotate/delete handles.
- **Inspector tabs:** **Captions · Text · Animation · Tracking · Text to speech ›**. The Text tab
  opens by default.
- **Text sub-tabs:** **Basic · Templates · Bubble · Effects**.
- **Text ▸ Basic, top of panel:**

  | Control | Position | State / notes |
  |---|---|---|
  | **Apply to all main captions** checkbox | ≈(1470,167) | **ticked by default**; style edits go to every auto caption |
  | Text box | ≈(1510,190)–(1890,280) | shows the selected caption's text; edit it to fix a recognition error |
  | Font dropdown | ≈(1735,332) | "System" |
  | Font size | slider ≈(1470–1780,396); value box ≈(1840,396) | 7 |
  | Pattern | ≈(1607 / 1653 / 1699, 443) | **B** (bold) / **U** (underline) / **I** (italic) toggles |
  | Case | ≈(1610 / 1658 / 1700, 491) | **TT** / **tt** / **Tt** |
  | **Save as preset** | ≈(1840,545) | |

- **Scrolling the inspector:**
  - Scroll with the pointer **inside the inspector's label column**, e.g. `scroll 1480 440 -4`,
    over a label with no slider or number box beneath it.
  - The "Apply to all" checkbox, text box and **Save as preset** stay pinned while the middle
    scrolls.
  - Scrolling doesn't change the draft (verified by mtime).
- **Further down Text ▸ Basic** (`inspector-s1.png`, `inspector-s2.png`):
  - **Style preset tiles**, a grid of "Aa" swatches, 7 per row, with ▾ to expand:
    - ⊘ none (selected by default)
    - white with black outline
    - black with white outline
    - plain white
    - white on dark
    - yellow with black outline
    - red with white outline
    - a second row of gradient and colour tiles
  - **Transform ▴**: Scale 100% with ↺ and keyframe `‹ ◇ ›`; Position/Rotate further down.
  - Checkbox sections, each with ▾, ↺ and a keyframe diamond: **Background**, **Glow**, **Shadow**,
    **Curve**.

### D. Styling, applied to all captions (agent-verified 2026-09-14)
Style signatures are counted with the read-only `evidence/2026-09-14/cap8/caption_styles.py
"<project>"`, which lists distinct style signatures across every text material.

1. **Preset style "white with black outline"** (the 2nd tile, ≈1552,330, with the grid scrolled into
   view). Click it with **Apply to all main captions** ticked.
   - The draft saved within about 1 s. The tile shows a cyan selection ring. The player caption turned
     white with a black outline.
   - **All 239 materials still share one signature**, now:
     - `border_color` `#000000`
     - `content.styles[].strokes` = black, width 0.06
     - `background_color` `#000000` but `background_style` 0, so no box is drawn
     - `font_size` still 7, fill white
     - `preset_id` stays empty: the tile writes the fields directly rather than linking a preset
   - Text segment positions were unchanged (239 × y −0.73).
   - `draft_inspect.py diff` against the pre-style summary gave **exactly 239 "material changed"
     lines**, one per caption, with no timing or structure changes.
2. **Font size 7 → 11.**
   1. Scroll the inspector back to the top (`scroll 1480 440 10`).
   2. Click the Font size value box (≈1840,396), then `ctrl+a`, then `type "11" --enter`.
   - The draft saved within about 1 s. **All 239 materials moved to `font_size` 11.0**
     (`content.styles[].size` 11) and still share one signature. The outline stayed.
   - Enter commits, the same as the rung-6 Transform boxes.
3. **Readability at size 11** (`size11.png`, `longest-caption.png`, `error-caption-selected.png`):
   - A short caption «قال اللي انا عايز اعملها» is large and crisp, white with a black outline, in
     the lower third over the desk, about ⅓ of the frame width.
   - **The longest caption** (54 chars, seg 122 at 00:03:50:14, «كلود بالذات عشان انا بشتغل بكلود
     بشكل كبير وشايف ان هو») wraps to **two lines** and stays inside the frame. The first line is
     about 77% of the frame width; the 2nd line («هو») sits just above the bottom edge.
   - ⚠ **A wrap can split a word.** At 00:04:07:18 «…في كلود في الغالب» wrapped as «…في الغال» / «ب».
     CapCut breaks by width, not by word. That's acceptable for a demo; for delivery, reduce the size
     (10), shorten long captions (split them), or raise the position.

### E. Fixing a recognition error natively (agent-verified 2026-09-14)
- **Error:** seg 129 (246.133 → 249.067 s) read «فانا لو هاشترك في حاجة **1** بس هاشترك في كلود في
  الغالب». The speaker says «واحدة» ("one"); the recogniser wrote the digit.
- **Route:**
  1. At Ctrl+= ×4 zoom (46.25 px/s), click the ruler inside the caption (x≈1780 for 247.6 s,
     87 px clear of the 245.733 video join, so it doesn't snap).
  2. Click the caption pill (1780,763) to select it. The inspector text box shows its text.
  3. Click in the text box (≈1700,240), then `key ctrl+a`, then
     `type "فانا لو هاشترك في حاجة واحدة بس هاشترك في كلود في الغالب"` (Unicode typing, no Enter;
     the box is multi-line).
- **Saves during typing:** the first autosave came **mid-typing** and stored «…واحدة بس هاش». Poll
  the draft until the text equals the full target before verifying. It was complete within about
  6 s of the first save.
- **Verification** (the read-only `evidence/…/cap8/caption_texts.py` dumps every caption's
  start/duration/text/words before and after):
  - **Exactly 1 of 239 captions changed**: seg 129 text `…حاجة 1 بس…` → `…حاجة واحدة بس…`.
    Start and duration were unchanged.
  - **"Apply to all main captions" does not propagate text edits.** It applies only to style.
  - The material's `words` list was **not** updated. The per-word tokens still hold the original
    recognition, so `draft_inspect.py words` shows «1». Re-run captions or edit timing if word-level
    data matters (e.g. word-by-word animation, rung 9).
  - The player immediately showed the corrected caption, now wrapping on a whole word («…كلود في» /
    «الغالب»).
- **Keyboard focus stays in the text box after typing.** Click the ruler before using Home, arrows,
  Ctrl+Z or other shortcuts, or those keys edit the caption text instead.
- **Undo is per character** (agent-verified): with focus on the timeline, one **Ctrl+Z** removed only
  the last typed letter («…الغالب» → «…الغال»). **Ctrl+Shift+Z** restored it, and every caption
  matched the post-fix dump exactly. To revert a whole text fix, retype the original text rather
  than pressing Ctrl+Z once per character.

### F. Timing spot-checks (agent-verified 2026-09-14, `evidence/…/cap8/timing/`)
- **↓ (next cut point) also stops at caption start and end boundaries**, not only at video joins.
  That lands the playhead exactly on a caption's first frame.
- **Check 1, first caption:**
  - Click the ruler to take focus, then **Home**, then **↓**. The playhead landed on **00:00:00:18 =
    0.600 s**, exactly seg 0's start, and the player showed «بسم الله الرحمن الرحيم».
  - **←** gives 00:00:00:17: **no caption**. The caption appears on its draft start frame.
  - The speaker is mid-breath with the mouth opening, consistent with speech starting.
- **Checks 2 and 3** (contact sheets `timing/c2-sheet.png`, `timing/c3-sheet.png`):
  1. Shift+Z (fit).
  2. Ruler click just before the target.
  3. Capture the player and timecode, then press **↓** five times, capturing after each.
- **Check 2**, around the corrected caption. Every stop matched a draft boundary to the frame:

  | Timecode | Boundary | Player |
  |---|---|---|
  | 04:03:15 = 243.500 | seg 128 start | «شامل وبشكل كويس خالص» |
  | 04:05:04 = 245.133 | seg 128 end | no caption |
  | 04:05:22 = 245.733 | video join | no caption, framing change |
  | 04:06:04 = 246.133 | seg 129 start | the **corrected** «…حاجة واحدة بس…» |
  | 04:09:02 = 249.067 | seg 129 end | no caption |
  | 04:09:04 = 249.133 | seg 130 | «يعني» |

- **Check 3**, near 5:53–5:57:

  | Timecode | Player |
  |---|---|
  | 05:52:29 | none |
  | 05:53:05 | «عنده نفس المشكلة» |
  | 05:54:00 | none |
  | 05:54:04 | «او كده وكلها الحاجات مجانية يعني مش» |
  | 05:56:22 | none |
  | 05:57:00 = 357.000 | seg 196 «مش عايز فلوس من الموضوع اصلا ولا هاخلي» |

- **Across all three checks:** captions appear exactly on their draft start frames and disappear on
  their end frames. In the no-caption frames the speaker's mouth is closed or pausing; in caption
  frames he is mid-speech or gesturing. The timing is consistent with the audio, though the agent
  can't hear it.

### G. Round 2: bilingual captions + caption template (in progress, 2026-09-14)
- **Why:** user feedback on the first demonstration: "Try bilingual captions, and restyle".
  - Restyle choice: a **caption Template** (Text ▸ Templates).
  - Second language: **English**.
  - Where: a **CapCut duplicate of `0914 (4)`**, so the verified round-1 state stays intact.
- **Before duplicating:**
  - The user had browsed `0914 (4)` in CapCut while answering. The agent left via Back to home page
    and re-verified: structure diff against round-1 final "No differences", 1 style signature × 239,
    caption texts identical.
  - Source draft mtime recorded as 16:25:54.656 (`cap8b/source-mtime-before.txt`).
- **Plan:**
  1. Home → right-click the `0914 (4)` card → **Duplicate**, clicked at the row centre from a fresh
     screenshot; Delete is the next row. Verify the new folder and that the source mtime is
     unchanged.
  2. Open the copy → Captions → Auto captions:
     - Spoken language **Arabic**
     - **Bilingual captions → English** (Pro)
     - tick **Delete current captions**, so the copy doesn't end up with two caption sets
     - Generate
  3. Inspect the draft: how the translation is stored (second text line, a separate track, or
     `translate_original_text`), caption count, timings.
  4. Select a caption → Text ▸ **Templates**: record the categories, Pro badges and whether it
     applies to all. Apply one template and verify in the draft (`caption_template_info`,
     `text_templates`) and the player, on a short and a long caption, for both languages.
  5. Undo/redo one step; save; diff; report.
- **Duplicate (agent-verified 2026-09-14):**
  - Right-click the `0914 (4)` thumbnail (first card, ≈383,680) to open the card menu: Upload
    (y≈703), Rename (≈744), **Duplicate (≈430,790)**, Delete ←Backspace (≈830).
  - Click Duplicate. Within 5 s a new folder **`0914 (4)-copy`** appeared (450.533 s), and the
    source `draft_content.json` mtime was unchanged (16:25:54.656).
  - The copy is the new **first** card, and the original moves to 2nd. Open it by the first card and
    confirm the title bar reads **0914 (4)-copy** before any edit. The Details panel also shows the
    name.
  - Structure diff of copy vs `0914 (4)`: **No differences** (239 captions, 1 style signature).
- **Bilingual captions dropdown** (≈383,255; purple Pro diamond on the label): a popup list with
  **✓ None, Bengali, Burmese, Chinese, Dutch, English**, … (alphabetical, scrolls). Rows are
  ≈40 px apart starting ≈(243,300). The spoken language (Arabic) isn't offered as a target.
  English is at ≈(243,500).
- **Bilingual generation (executed + agent-verified 2026-09-14):**
  - **Form:** Spoken language Arabic · Bilingual captions **English** · **Delete current captions
    ✓** (≈185,544). Then Generate (≈539,544). No credit or confirm dialog.
  - **Speed:** "Generating captions... 36%" was already showing 1.5 s after the click. The draft
    saved **≈5 s** after Generate, versus ≈80 s for the first generation, so CapCut apparently
    reused the cached speech recognition.
  - **Structure:** Delete current captions **removed the old caption track** and added **two new
    text tracks with identical timings**, 239 captions each:

    | Track | Language | `sub_type` | Position (`clip.transform.y`) |
    |---|---|---|---|
    | 1 | **English** (`en-US`) | **5** (translation) | **−0.7905**, bottom line |
    | 2 | **Arabic** (`ar-SA`) | 0 | **−0.5702**, above the English |

    Draft diff against the copy baseline: `track_count` 2 → 3, `materials.texts` 239 → 478, the old
    track removed and two added. Video segments unchanged. On the timeline the two **TT** rows sit
    at y≈727 and ≈763.
  - **Regeneration discards manual fixes:** the new Arabic is a fresh recognition, so caption 129
    reads «…حاجة **1** بس…» again. The English follows it: "If I want to subscribe, I need 1, but I
    will subscribe to Claude mostly". Re-apply text fixes **after** generating.
  - **Translation quality varies:**
    - «بسم الله الرحمن الرحيم» → "In the name of Allah, the Most Gracious, the Most Merciful" (good)
    - «زهجت من التاجيل وخلاص» → "I got bored of postponement **and salvation**" (wrong: «وخلاص»
      means "and that's it")
    - Read the English track for mistranslations of dialect words.
  - **Style resets on regeneration.** Both new tracks use CapCut's default caption style (system
    font, white, `border_width` 0.08, no stroke colour, no background, no template). The round-1
    preset and size 11 were **not** carried over.
    - Arabic: `font_size` 7, `content.styles.size` 7
    - English: `font_size` 7 but **`content.styles.size` 5**, so the translation line renders
      smaller
    - Each track has 1 style signature.
  - **Positions vary per caption:**
    - English: y −0.7905 for 225 captions, −0.843 for 13, −0.798 for 1
    - Arabic: −0.5702 for 207, −0.5806 for 32
    - CapCut apparently shifts a pair when a line wraps, so the two languages don't overlap. Don't
      "normalise" positions by hand without checking wrapped captions.
  - **On screen at the default style** (`bilingual-player-3800.png`, 00:00:03:24):
    - Arabic «زهجت من التاجيل وخلاص» sits on top.
    - English "I got bored of postponement and salvation" is directly below it.
    - The **English renders visually larger than the Arabic**: Latin glyphs at size 5 look bigger
      than Arabic at 7 in the system font.
    - Neither line has an outline, so the thin Arabic is hard to read over the shirt and desk. That
      makes restyling part of the job, not decoration.
- **Selecting a bilingual caption (executed 2026-09-14):**
  - At Ctrl+= ×4 (≈44.5 px/s; 00:05 at x≈295, 00:10 at 518) the two caption rows sit at **y≈731
    (Arabic, track 2)** and **y≈763 (English, track 1)**. Pills are stacked with identical spans.
    English pills start with the A☰ icon; Arabic pills end with it.
  - Clicking the Arabic pill at (280,731) selects it without moving the playhead. The inspector shows
    Captions · Text · Animation · Tracking · Text to speech, and Text ▸ Basic shows «زهجت من التاجيل
    وخلاص», size 7, **Apply to all main captions ✓**.
  - The player draws the selection box around the Arabic line only.
- **Text ▸ Templates sub-tab** (≈1623,127):
  - Shows **Apply to all main captions ✓**, a **"Search for text templates"** field, and a
    **Loading…** spinner. The template list is fetched online, so wait for it.
  - The bottom bar has **Save as preset** and a **Reset** button (Basic has only Save as preset).
  - Opening the tab didn't change the draft.
  - ⚠ **It stayed on "Loading…" for over 32 s** (16:39:30 → 16:41:28) and never listed templates.
    Use the Captions panel route below instead.
- **Captions ▸ Templates (left asset panel)** (observed 2026-09-14, `captions-left-templates.png`):
  - With the Captions asset tab open, click the left sub-item **Templates ▾** (≈85,170). It expands
    into categories: **Favorites, Trending** (default), **Classic, NEW, Hits, Word, Glow,
    Lyrics**. Rows are ≈40 px apart from Favorites ≈(63,211).
  - It loaded within ≈5 s, while the inspector tab was still spinning.
  - **Search field:** "People are searching Basic" (≈370,127), with a filter icon.
  - **Grid:** three columns of animated preview tiles. Examples in Trending: "QUICK", yellow
    "Rubah", "Hôm", a small "THE QUICK", "THE", a boxed "THE", a glowing yellow "CAPTION".
    - **Nearly every tile has a purple Pro diamond** (top-left).
    - Each tile has ☆ (favourite) and ⬇ (download) icons (bottom-right).
  - **Footer** (greyed with a caption selected): "Delete current captions" and **"Generate
    captions"** (Pro). The template may be applied at generation time from here; the route is still
    to be confirmed.
  - Browsing categories and the grid didn't change the draft.
  - **Tiles seen 2026-09-14** (`templates/templates-sheet.png`; row/column in a 3-wide grid; Pro =
    purple diamond):

    | Category | Tiles |
    |---|---|
    | **Trending** | (animated blank) Pro · (blank "H") Pro · "QUICK" bold white Pro · "Rubah" yellow/green Pro · "Hôm" blue · "THE QUICK" small · "THE" bold white Pro · **boxed "THE"** (white text, rounded outlined box) Pro · glowing yellow "CAPTION" |
    | **Classic** | **"THE QUICK BROWN FOX" on a black box, no Pro badge** · **"THE QUICK" white with a yellow word highlight** Pro · blanks · "quick" bold white · "THE" white outline Pro · "QUICK" yellow italic Pro · "QUICK" white italic Pro |
    | **Word** | **Arabic «الثعلب» tiles** (gold/red Pro, **blue outline** Pro, green Pro) · "THE" bold white Pro · red "EL" box · "RUBAH" white-on-red glow · "COKLAT" red italic · "Rubah" yellow Pro |

  - The Word category's Arabic-preview tiles are the ones built for Arabic shaping. Latin-only
    previews may not join Arabic letters correctly, so verify on the player.
  - The user picks the template (a taste decision). Don't apply one without asking.
  - **User choice (2026-09-14): "Classic: black box"**, the Classic row 1 left tile "THE QUICK
    BROWN FOX": white text on a black box.
    - **Correction:** the tile **does** carry a purple Pro diamond (top-left, `classic-grid.png`).
      The earlier table and the option text told the user "no Pro badge", which was a misread of
      the downscaled sheet. Zoom into a tile before stating its tier.
    - Unlike its neighbours it shows only ☆ with no ⬇, so it's likely already downloaded.
    - At the maximized layout the tile centre is ≈(230,190).
  - **Clicking a template tile only previews it** (executed 2026-09-14, `template-clicked.png`,
    `template-player.png`):
    - The tile gets a cyan border and a cyan **+** button at its bottom-right (≈200,201).
    - The player switches to **"Previewing — Templates"** (Pro diamond, ⓘ) and plays a 00:00:02:07
      sample: "THE QUICK BROWN FOX" / "JUMPS OVER THE LAZY DOG" in bold white on a black box, over
      the current frame.
    - The footer **Generate captions** (Pro, ≈390,409) becomes enabled, and **Delete current
      captions** stays unticked.
    - **Draft unchanged:** no save, both tracks still at 1 default signature.
    - ⚠ Don't press **Generate captions** here without deciding about "Delete current captions".
      With it unticked, a new caption set would be added on top of the existing bilingual tracks.
    - **The tile click deselected the caption:** the right panel went back to project **Details**.
      A following **+** therefore has no caption selection to apply to.
    - **No tooltips** on the tile's **+** or on **Generate captions** (hovered 1.6 s each; no
      `LVToolTipWindow` for them). Identify them by position and behaviour.
    - **Re-selecting the caption pill ends the preview** (`reselected-after-preview.png`):
      - The player title returns to "Player-Timeline 01" at the same timecode (00:00:03:24).
      - The inspector shows the caption's Text ▸ Basic again.
      - The tile loses its cyan border and **+**, showing only ☆.
      - The footer greys out again. The draft is unchanged.
    - **Hover does not reveal the +** (`tile-hover.png`): with the caption selected, hovering the
      tile showed only ☆. The **+** exists only while that tile is previewing. A click at the +
      position without a preview lands on the tile body, which starts the preview again and
      deselects the caption. The **+** is therefore always pressed with **no caption selected**.
    - **Pressing the + while previewing did not apply the template** (executed 2026-09-14 16:56,
      `plus-visible-before-click.png`, `plus2-clicked.png`):
      - No draft save (still 16:33:54). Structure diff: No differences. Both caption tracks were
        still 1 default signature each.
      - The timeline was unchanged, with no new text element.
      - The player stayed in "Previewing — Templates", now **paused** at 00:00:00:15. The click
        seems to have acted on the preview instead.
    - **Conclusion so far:** in the Captions ▸ Templates side panel a template is picked for the
      **next generation** (footer "Generate captions", Pro). The panel doesn't restyle existing
      captions. For existing captions try the selected caption's inspector **Text ▸ Templates**
      with Apply to all main captions ✓.
- **Inspector Text ▸ Templates, retry** (observed 2026-09-14 16:59, `retry-inspector-templates.png`):
  1. Click an Arabic caption pill (280,731). This also ends any side-panel preview.
  2. Click the **Templates** sub-tab (≈1623,127).
  - This time it **loaded within 12 s**. It had spun for over 32 s on the first visit, before the
    side panel had fetched the catalogue. If it spins, open Captions ▸ Templates in the left panel
    once, then come back.
  - **Layout:**
    - Apply to all main captions ✓
    - "Search for text templates"
    - a chip row: **★ · Trending · Classic · NEW · H…**, with a filter icon and ▾
    - a **Favorites** row ("No favorites yet")
    - a **Trending** row starting with a **⊘ none** tile (selected), then previews such as a Pro
      icon tile, "Rubah" and "The Quick Brown Fox"
    - footer **Save as preset · Reset**
  - Classic chip ≈(1653,271). Browsing didn't change the draft.
  - **Classic grid in the inspector** (`inspector-classic.png`): **4 tiles per row**, ≈97 px
    apart, rows ≈98 px apart, starting at tile centre ≈(1495,355). Each tile has ☆ and usually ⬇.
    - **Row 1:** **"THE QUICK BROWN FOX" black box (Pro diamond)** · two blank animated previews ·
      "THE QUICK" yellow highlight (Pro)
    - **Row 2:** "QUICK" white outline (Pro) · blank · "quick" white (Pro) · "QUICK" yellow italic
      (Pro)
    - Click a tile's body, not its ☆ or ⬇ icons at the bottom edge.
- **Applying the template from the inspector (executed + draft-verified 2026-09-14 17:00:51):**
  - **Setup:** Arabic caption selected, Text ▸ Templates ▸ Classic, Apply to all main captions ✓.
  - **Click** the "THE QUICK BROWN FOX" tile (1495,355). The draft saved **3 s** later
    (17:00:54). No confirm, upsell or credit dialog.
  - **Only the selected caption track changed:**
    - **Track 2 (Arabic):** all 239 segments now point to **`text_templates`** materials (was
      `texts`), all one template: name **"边框弹出黑色"** ("border pop-out, black"),
      `resource_id` 7331662668685774086.
    - Materials: `text_templates` 0 → 239 and **`effects` 0 → 239**. `texts` stays 478, because
      template materials link to text materials through `text_info_resources`.
    - **Position changed:** y −0.2787 × 194, −0.3141 × 32, −0.1685 × 13 (was −0.5702 / −0.5806).
      The template box sits higher.
    - **Track 1 (English): unchanged.** Same default signature and positions. **"Apply to all main
      captions" means all captions of the selected track (language), not both bilingual tracks.**
      Style the English track separately.
  - **`draft_inspect.py diff` noise:** a material-type change shows as each caption segment
    "added" with its template name (`text_templates:'… [template: 边框弹出黑色]'`). Structure
    (count, timing) must be checked with a template-aware text dump.
  - **Template-aware verification (agent-verified):**
    - Each template segment's text is resolved through `text_templates[].text_info_resources[0]
      .text_material_id` → `texts[].content.text`.
    - **All 478 captions have identical track, start, duration and text** before and after
      (0 mismatches). The template changes presentation only.
    - Template segments carry 2 `extra_material_refs`. The added `effects` are `type:
      "text_effect"` (resource 7317207872985633281).
  - **On screen** (`inspector-template-player.png`, 00:00:03:24):
    - «زهجت من التاجيل وخلاص» renders as **bold white Arabic on a solid black box** with correctly
      joined letters, centred at about the speaker's chest/shirt logo height.
    - The English line stays plain white in the lower third, with a clear gap between the two
      lines.
    - In the inspector the selected tile shows a cyan border. The side panel's black-box tile
      stays highlighted too.
  - **Timeline:** immediately after applying, the Arabic template pills drew as plain orange blocks
    with no label. **A few seconds later they showed their text and A☰ again**
    (`english-selected-classic.png`). It was a redraw lag, not a change. Find rows by y (Arabic
    ≈731, English ≈763) regardless.
- **Styling the English (translation) track** (observed 2026-09-14, `english-selected-classic.png`):
  - Click an English pill (440,763). The player draws the selection box around the English line.
  - The inspector checkbox reads **"Apply to all sub captions"** ✓, not "main captions". CapCut
    calls the translation track **sub captions**. That's why the Arabic ("main") template didn't
    reach it.
  - Text ▸ Templates (1623,127) ▸ Classic (1653,271) shows the same grid as before. Nothing is
    highlighted for this track yet.
  - **Apply** (executed + draft-verified 2026-09-14 17:03:43): click the black-box tile
    (1495,355). The draft saved **2 s** later.
    - **Track 1 (English):** 239 segments → `text_templates`, same template "边框弹出黑色"
      (7331662668685774086).
    - Materials: `text_templates` 239 → 478, `effects` 239 → 478. Track 2 unchanged.
    - **English positions moved down, past −1.0:** y −1.0859 × 190, −1.1961 × 48, −1.1213 × 1
      (was −0.79). Check on the player that the box isn't clipped at the frame bottom.
    - **Template-aware check:** all 478 captions keep identical track, start, duration and text
      compared with the pre-template dump.
    - `draft_inspect.py diff` reported 480 "differences", made up of the two material counts plus
      478 per-segment material swaps. That's expected for a template change, not a timing change.
    - ⚠ **On the player at 00:00:03:24** (`both-templated-player.png`):
      - The Arabic black box «زهجت من التاجيل وخلاص» is visible.
      - The **English line is not visible**: only its empty selection box is drawn, at about the
        bottom 10% of the frame.
      - The playhead is exactly on this caption's **first frame** (3.800 s), and the template name
        means "border **pop-out**", an entry animation. Possible causes: the English animation
        hasn't started, or the lowered position (y −1.09) clips it. Check mid-caption frames before
        concluding.
    - **The template is word-by-word, not a static box** (`both-templated-long.png` 00:03:48:26,
      `both-templated-5min.png` 00:05:37:09):
      - The Arabic line **builds up word by word**, and the **current word sits in the black box**
        with the earlier words plain white: «**كلود** بالذات عشان انا», «**هاعملهم** انا ال ا او».
      - So the tile's static preview ("THE QUICK BROWN FOX" on a black box) undersells it: it's a
        karaoke-style highlight that relies on the caption's per-word timings.
      - The English line was invisible in both frames too.
    - **Template data** (read-only, seg 1 of each track, 3.800 s +1.800):
      - Both tracks: `text_templates[].type` **`text_template_subtitle`**, `render_mode` 0,
        segment `visible` True, `clip.alpha` 1.
      - Both linked text materials were set to **`font_size` 10.5** (was 7; English style size
        was 5).
      - `text_info_resources[0].attach_info` carries its own start/duration (0 / 1 800 000 µs) and
        original size: English ≈738×149 px, Arabic ≈398×163 px.
      - `current_word_info` / `origin_word_info` are empty, so the word-by-word highlight is driven
        by the linked text's `words` (English 7 tokens, Arabic 4).
      - **English y = −1.196** for this caption (track range −1.196 … −1.086). Arabic y = −0.279
        (range −0.314 … −0.168).
    - **Mid-caption frames** (`midframes/`, agent-verified 2026-09-14):

      | Frame | Arabic box on | English |
      |---|---|---|
      | 00:00:04:19 (seg 1 + 25 f) | «التاجيل» | not visible |
      | 00:00:05:09 (seg 1 + 45 f) | «وخلاص» | not visible |
      | 00:05:37:29 | a highlight on a stray one-letter token («ال **ا** او») | not visible |
      | 00:05:38:24 | «ال…» | not visible |

      - The Arabic highlight advances word by word inside a caption, as intended.
      - ⚠ **The English is invisible on every frame, including well inside captions.** Only its
        empty selection box shows near the frame bottom. So it isn't the pop-out entry animation.
      - **Why:** English y is −1.086 … −1.196. In caption units ±1.0 is the frame edge (round 1's
        lower third was −0.73), and the English box is ≈149 / 1080 px tall ≈ 0.276 units. At
        −1.196 its top is ≈ −1.058, **entirely below the frame**.
      - **Fix needed:** move the sub captions (English) up natively. Check whether a Transform
        Position edit honours "Apply to all sub captions".
    - **English caption inspector after the template** (observed 2026-09-14,
      `english-basic-top.png`, `english-basic-s1.png`, `english-basic-s2.png`):
      - **Selecting:** at fit zoom, the English row (y≈763) starts at x≈232. A click there selected
        caption 0 ("In the name of Allah, the Most Gracious, the Most Merciful").
      - Clicking empty timeline space first had moved the playhead to 07:17:24, so the player
        showed a different caption.
      - Text sub-tabs are now **Basic · Templates · Effects**, with **no Bubble**, because a
        template is applied. Apply to all sub captions ✓.
      - **Font "Staatliches-Regular"**, size **11**. The template set its own font (the draft said
        10.5 before the view refreshed).
      - Scrolling down Basic: preset style tiles (⊘ selected), then **Transform ▴** (↺, keyframe;
        Scale 100%, Position below), then **Blend ✓** (Opacity **50%**), **Stroke ☐**,
        **Background ✓**.
      - One `scroll -4` step jumps about a whole section, so use smaller steps (±2) to stop on
        Transform ▸ Position.
      - **Transform section** (`english-basic-position.png`; after `scroll -4 -4 +2`):

        | Control | Position | Value |
        |---|---|---|
        | Scale slider + box | ≈(1790,271) | 100% |
        | Uniform scale toggle | ≈(1870,319) | ON |
        | **Position X** | ≈(1650,367) | **0** |
        | **Position Y** | ≈(1770,367) | **−1292** |
        | Plane rotation | ≈(1640,414) | 0.00° |
        | Alignment buttons | y≈462 | a row of them |

        Each row has keyframe `‹ ◇ ›`.
      - **Units:** Position is canvas px, and the draft stores `clip.transform.y = value / 1080`
        (−1292 / 1080 = −1.196), the same mapping as rung 6's video Position. Round 1's visible
        lower third was −0.73 = **−788 px**, and the Arabic template box sits at −301 px.
      - **Moving the English up (executed + draft-verified 2026-09-14 17:10:34):**
        1. With an English caption selected and **Apply to all sub captions ✓**, click the
           Position Y box (1770,367).
        2. `key ctrl+a`, then `type "-700" --enter`.
        - The draft saved **2 s** later.
        - **All 239 English captions now have y = −0.6481 (−700 px)**, one uniform value. The
          per-caption −1.086 / −1.121 / −1.196 variation is gone. **So Transform Position honours
          "Apply to all sub captions".**
        - Arabic track 2 is unchanged (−0.2787 × 194, −0.3141 × 32, −0.1685 × 13). The template
          stays on both tracks.
        - All 478 captions keep identical text, start and duration (template-aware check).
        - **On the player (agent-verified 2026-09-14):** the English is visible below the Arabic
          line, inside the frame, clear of the Arabic box.
          - **Caption 1** at 00:00:04:19 (`english-y-seg1-mid.png`): Arabic «زهجت من
            التاجيل وخلاص» with the box on «التاجيل»; English **"I GOT BORED OF"**.
          - **Longest caption** at 00:03:50:06 (`english-y-long-mid.png`): Arabic «بشتغل
            بكلود بشكل كبير» with the box on «بشتغل»; English **"I WORK WITH CLAUDE"**.
        - **Template look on the English:**
          - bold **uppercase** Staatliches
          - white text, with the current word in a black box
          - words revealed progressively
        - **Long captions are paged:** both languages show only a short chunk of a long caption at a
          time, so the round-1 two-line wrap problem goes away with this template.
- **Round-2 undo / redo / save (agent-verified 2026-09-14):**
  - Click the ruler first so the keys go to the timeline, not the Position box.
  - **Ctrl+Z (once):** the draft saved. English y went back to −1.0859 × 190 / −1.1961 × 48 /
    −1.1213 × 1, and the Arabic was unchanged. **The Apply-to-all position edit is one undo step
    for all 239 sub captions.**
  - **Ctrl+Shift+Z:** English y is −0.6481 × 239 again, the exact verified state. Save only after
    this gate passes.
  - **Menu ▸ Back to home page:** saved; tree root `HomeWindow`.
  - **Final checks on disk:**
    - Both text tracks: 239 × `text_templates` "边框弹出黑色", with English y −0.6481 × 239 and
      Arabic −0.2787 / −0.3141 / −0.1685.
    - All 478 captions have identical text, start and duration to the post-bilingual state.
    - The video track still has 7 segments, and seg 4 keeps its rung-7 keyframe group.
    - Structure against the copy baseline: `track_count` 2 → 3, `segment_count` 246 → 485,
      `texts` 239 → 478, `text_templates` 0 → 478, `effects` 0 → 478, `material_animations`
      244 → 483. No video change.
  - **Scope:**
    - The original `0914 (4)` mtime is unchanged since before the duplicate (16:25:54.656).
    - The user's projects (0707, 0720, 0728, the Arabic-titled one) are unchanged.
    - `0914 (5)` wasn't touched.
- **Round-2 recipe (bilingual + caption template), for reuse:**
  1. **Duplicate the project** if the current captions hold fixes worth keeping. Regeneration
     replaces them.
  2. **Generate:** Captions ▸ Auto captions → Spoken language → **Bilingual captions: <language>**
     → **Delete current captions ✓** → Generate. That gives 2 text tracks: translation = "sub
     captions" (`sub_type` 5), speech = "main captions".
  3. **Re-apply any text fixes.**
  4. **Main (speech) track:** select a main caption → Text ▸ **Templates** (the inspector tab,
     not the left side panel) → category chip → tile. It applies to all main captions.
  5. **Sub (translation) track:** select a sub caption and repeat step 4 ("Apply to all sub
     captions").
  6. **Check the player on frames inside captions.** If a line is missing, open Text ▸ Basic ▸
     Transform and type a Position Y inside the frame (here −700 px). It applies to all captions of
     that track.
  7. Undo/redo gate, then Back to home page, then the template-aware text/timing check.
      - Minor: one-letter recognition tokens (e.g. «ا») get their own tiny highlight box, a small
        visual glitch. Fixing the caption text removes it.
    - **Ruler clicks snap to caption boundaries.** With 478 caption boundaries at fit zoom, every
      ruler click landed on a caption's **first frame** (03:48:26 = 228.867 s, seg 122's start). To
      judge a caption, step **→** 15–45 frames into it after the click.

## Wait conditions
- **Generation:** ≈80 s for 7:30 of Arabic (≈11 s per minute of footage).
  - Poll the draft for a non-empty `text` track, the authoritative signal.
  - Or `cc.py wait-for --contains "Generating captions" --gone --timeout 900` (matches the loading
    window's AutomationId).
- **Preset tile, font size, ↓ navigation:** saved within about 1 s, or no save at all for
  navigation.
- **Text edit:** autosave can land **mid-typing**. Poll until the caption text equals the full
  target (≈6 s here).

## Verification
- **Structure:** `draft_inspect.py diff <baseline> "<project>"` shows exactly the added text track
  (N segments) and `materials.texts` 0 → N. Video segments and keyframes are unchanged.
- **Style reached every caption:** `evidence/…/cap8/caption_styles.py "<project>"` reports **1
  distinct style signature** across all N materials, with the chosen values (here: white,
  `border_color` #000000, stroke 0.06, `font_size` 11, y −0.73).
- **Text fix is local:** a `caption_texts.py` before/after dump shows exactly one changed caption,
  with timing unchanged.
- **Timing:** Home/ruler then ↓ lands on caption starts. ← one frame shows no caption. Check at
  least 3 places spread across the video.
- **Readability:** capture the player at a short and at the **longest** caption. Confirm it's inside
  the frame and check line wraps.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|
| Spoken language | Arabic (explicit) | per footage | state it; Auto detect also worked on this speaker in rung 4 |
| Preset style | tile 2, white with black outline | style default | readable over light and dark backgrounds without a box |
| Font size | 11 (default 7) | style default for 16:9 | 10–12; long captions wrap to 2 lines at 11 and can split a word |
| Position | default y −0.73 (lower third) | shot-specific | keep clear of the speaker's face and hands; here the text sits over the desk |
| Apply to all main captions | ticked (default) | universal | untick only to style one caption differently |
| Caption fixes | digit «1» → «واحدة» | per transcript | read captions for numerals, English brand names and dialect words |

## Undo / recovery
- **Generation** is one undo step. Rung 4 verified that one Ctrl+Z removes the whole caption track.
- **Preset and font size:** each click or Enter is a single step (not separately re-tested here;
  style changes are reversible with the tile ⊘ "none" and by typing 7 back).
- **Text edits undo per character.** Retype the original text to revert a fix.
- Always click the ruler first so Ctrl+Z goes to the timeline and not the text box.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| First practice project was unsuitable | `0914 (1)` is gym footage; its "speech" is song lyrics | check the rung-3 transcript notes before choosing footage for captions |
| `wait-for --contains "Generating captions"` timed out while generation was running | the progress text is in the loading window's AutomationId; `--contains` matched Name only | fixed in `cc.py` (`--contains` also matches AutomationId); poll the draft for a text track as the authoritative signal |
| Three inspector "scrolls" showed the same page | the pointer was at x 1120, over the **player**, not the inspector (which starts at x≈1447) | scroll inside the inspector label column (x≈1480). The player view and draft were unchanged |
| A scratchpad script "didn't exist" when run | the file wasn't where the shell looked | keep helper scripts under `evidence/<date>/capN/` |
| Clicking "None" in the Bilingual dropdown did nothing; the field still read English | the dropdown was opened in one command and the next command began with `cc.py focus`, which closed the popup, so the click hit empty panel | open a dropdown and click its row **in the same command**, with no `focus` call between; screenshot the field afterwards |
| Bilingual Generate: `wait-for --contains "Generating captions"` (30 s) reported "not present", yet the 1.5 s screenshot showed "Generating captions... 36%" | the second generation finished in ≈5 s (CapCut apparently reused the existing recognition), so the dialog was gone before polling started | treat the **draft save + changed caption dump** as the completion signal; screenshot immediately after Generate; only treat "never appeared" as a problem if the draft also didn't change |
| After asking the user a question, CapCut was back in the editor (a caption selected, presets expanded, different zoom), not the home screen the agent had left | the user used CapCut while answering (confirmed: "That was me, continue") | **after every question to the user, take a fresh screenshot + `tree` before any input**; check draft mtimes; leave via Back to home page and diff before continuing |
| Player showed no caption at the "longest caption" time | a fit-zoom ruler click at x 894 (meant as 230.5 s) landed on 00:03:48:09 = 228.3 s, before the caption starts (fit zoom is ±2 s, as in rung 5) | zoom first (Ctrl+= ×4 ≈ **46.25 px/s**; read two ruler labels), then click; confirm the timecode |

## Tree coverage notes
- **Named in the tree:** `LVLoadingDialog` during generation (progress in the AutomationId, e.g.
  `Generating captions... 0%`), and `HomeWindow` after Back to home page.
- **Screenshot-only:** the Auto captions form, the language popup, caption pills on the timeline,
  and the whole caption inspector (tabs, Apply to all, text box, font, size, pattern, preset tiles,
  Background/Glow/Shadow/Curve).
- The language dropdown opens as an extra `Qt622QWindowIcon` top-level window with no named
  children.

## Open questions for the user
- **Resolved by round 2:**
  - Style: the user chose the "Classic: black box" caption template.
  - Bilingual: Arabic + English demonstrated.
  - Long-caption wrapping: this template pages long captions into short chunks.
- **Template tier:** "Classic: black box" carries a **Pro diamond**. The option text before the
  choice wrongly said it had none. The user is on Pro, and no credit prompt appeared.
- **Placement:** keep Arabic at about chest height (−301 px) and English at −700 px? Or put both
  lower, e.g. Arabic −550 / English −800, clear of the shirt logo?
- **Translation quality:** a few English lines are wrong («وخلاص» → "and salvation"). Fix
  mistranslations caption by caption (text box), or accept machine translation?
- **Resolved by round 3:** captions are **Arabic only** (user, 2026-09-14). The bilingual route
  stays documented as an option, not the default.
- **Default for future edits:** make Arabic-only + "Classic: black box" in the lower third the default
  caption recipe for talking-head videos?
- **Speaker-identified captions** aren't offered in this version's Auto captions form. Record as
  unavailable on 9.4.0.4015?
