# Capability 08: Auto captions + styling

## Status
- **Ladder status:** in-progress. The first demonstration is below. User feedback (2026-09-14):
  **"Try bilingual captions, and restyle"**, so demonstrate Bilingual captions (Pro) and a new
  caption style, then ask for approval again.
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
- **Style:** keep white + black outline at size 11 in the lower third? Or prefer a boxed background,
  a bolder or brand font, a highlight colour for key words, or a higher position?
- **Long captions:** at size 11 the longest wraps to 2 lines and one wrap split a word («الغال/ب»).
  Size 10, shorter caption splits, or accept it?
- **Speaker-identified captions** aren't offered in this version's Auto captions form. Should rung 8
  record that as unavailable, or should it look for another route (e.g. the Captions inspector tab)?
- **Bilingual captions** (Pro) weren't tried. Do you want Arabic + English captions?
