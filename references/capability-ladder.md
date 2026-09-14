# Capability Ladder (the gate)

This file is the single source of truth for what the agent may do. Work only on the **lowest row
whose status is not `approved`**. Update this file at every status change.

Status values:
- `not-started`
- `in-progress`
- `demonstrated`: the agent verified it and is waiting for the user
- `approved`: the user said yes in chat
- `blocked`: record why in Notes

| # | Capability | Styles | Status | Procedure file | Demonstrated | Approved | Notes |
|---|---|---|---|---|---|---|---|
| 0 | Environment + accessibility/control map | all | approved | `accessibility-controls.md`, `keyboard-shortcuts.md`, `pro-features.md` | 2026-09-14 | 2026-09-14 | CapCut UI invisible to UIA/MSAA (root windows only; QT_ACCESSIBILITY=1 no effect) → screenshot-first. Named tree windows for dialogs (Shortcuts, Export) and the player surface; native file dialog fully exposed. DPI mapping verified at 125%. Practice project `0914`: clip imported + placed, verified by draft. Mapped: home, editor layout, asset tabs, inspector tabs, menu, full shortcut list (CapCut's own), export dialog (cancelled). **Gaps filled after approval (2026-09-14, view-only, draft unchanged):** Menu ▸ Layout; Settings (all 4 tabs, closed with Cancel); Video ▸ Remove BG/Mask/Retouch; Audio ▸ Voice changer; right-click menus on a clip and on empty timeline. **Deferred:** Transcript panel (Pro, may use credits) → rung 3 with the user's confirmation; basic-tool icons show no tooltips → identify in rungs 1–2 via shortcuts and behaviour. **Correction (2026-09-14):** the "draft unchanged" checks during mapping compared against an un-resaved draft. After Back to home page saved `0914`, it had an added empty `hsl` material from browsing Adjust ▸ HSL. Agent-owned project only; user projects untouched (mtimes unchanged). Lesson recorded in project-safety rule 5. |
| 1 | Duplicate project, open copy, one split at an exact time, undo test, save | all | approved | `capabilities/01-single-split.md` | 2026-09-14 | 2026-09-14 | Source `0914` → CapCut Duplicate → `0914-copy`. Playhead: ruler click (09:29) + → = 00:00:10:00. Ctrl+B split verified by timeline + draft (0–10.000 / 10.000–23.467, src@10.000). Undo → No differences; redo → split restored; Back to home page saved. Source mtime unchanged. |
| 2 | Timeline basics: select, delete/ripple, trim, move, add media, track lock/mute | all | approved | `capabilities/02-timeline-basics.md` | 2026-09-14 | 2026-09-14 | On `0914-copy`, each op verified by timeline screenshot + draft diff, then undone to baseline (No differences): Backspace delete ripples (magnet ON); magnet = first right toggle, P toggles; W trims at playhead (15.000); drag-up → overlay track (flag 2) at same time; media card drag appends flush at end; lock = attr 4 (clips unselectable), mute = attr 1 ("Track muted" toast). |
| 3 | Transcript editing: remove pauses/silences and filler words | YouTube | approved | `capabilities/03-transcript-pauses.md` | 2026-09-14 | 2026-09-14 | Transcript icon → "Remove filler words" (RoughCutWindow). On `0914-copy` (23 s) nothing was detected. On the user-chosen raw take `VID_20260623_152043` (2:15) in new practice project `0914 (1)`: 1 pause (22.30 s @ 00:54:23, pre-ticked), 0 repeats, 0 filler words. Delete → draft 135.2 → 112.9 s, segments [0–54.767] + [54.767–112.9, src 77.067]. ↓ lands on the cut, frames jump. Undo/redo verified. |
| 4 | Bad-take removal via transcript | YouTube | approved | `capabilities/04-bad-takes.md` | 2026-09-14 | 2026-09-14 | Footage `VID_20260720_190542` (8:43) in practice project `0914 (4)`. CapCut's Repeats tab missed the spoken retakes, so they were found by reading the Transcript. Exact word boundaries came from Auto captions (`draft_inspect.py words`); captions were then undone. 3 splits (Ctrl+B, ruler + arrows, verified in draft) and 2 ripple deletes (later piece first). Result: 523.467 → 473.433 s, segments [0–248.367 src 46.933] + [248.367–473.433 src 298.400]. ↓ lands on the join; undo/redo verified; saved. |
| 5 | Waveform/manual cleanup pass | YouTube | approved | `capabilities/05-waveform-cleanup.md` | 2026-09-14 | 2026-09-14 | Waveform strip unreadable at the default track height, so gaps came from Auto-caption word timings (`draft_inspect.py gaps`): 79 real gaps ≥0.6 s. The 5 longest were tightened to 0.25 s by `cut_gaps.py` (measuring split → undo → arrow-correct → exact split at gap end → exact playhead at gap start → W ripple), each checkpoint verified in the draft. 473.433 → 450.533 s, 7 segments; ↓ lands on every join; undo/redo verified; saved. |
| 6 | Jump cuts with scale/position punch-in | YouTube | approved | `capabilities/06-jump-cuts.md` | 2026-09-14 | 2026-09-14 | On `0914 (4)`: Video ▸ Basic ▸ Transform Scale box then Position Y box (type + Enter). Position is in canvas px (draft pos.y = value/1080; negative = down). *Correction (rung 10): the storage mapping is right, but one typed unit = ½ canvas px, because `transform` 1.0 = half the canvas.* Segments 1, 3, 5 set to 110% / Y −10 (from the eye-height formula), each gated by the draft. Eye line within ≈±8 screen px at every punched join; no exposed borders; undo/redo verified; saved. |
| 7 | Keyframed eased push-ins | YouTube, promo | approved | `capabilities/07-push-ins.md` | 2026-09-14 | 2026-09-14 | On `0914 (4)` segment 4 (262.500–359.467 s, unpunched). Route: select the clip, playhead on the first frame, click the inspector Scale ◇; playhead on the last frame, type 108 + Enter (auto-adds a keyframe); right-click the keyframe marker ▸ **Easing**. Draft: 2× `KFTypeScaleX` (1.0 → 1.08), `FreeCurveInOut` with handles ±40.7 s (0.42/0.58 ease-in-out); `time_offset` is on the source clock. The inspector read 100/101/104/107/108% at start/¼/½/¾/end, which matches eased, not linear (102/106). One Ctrl+Z reverts the easing on both keyframes; redo gives No differences; saved via Back to home page, No differences. Applying a preset auto-played the player (paused with Space). New `draft_inspect.py keyframes` and a float-tolerant diff. User projects untouched. |
| 8 | Auto captions + styling (incl. speaker-ID captions) | YouTube, shorts | approved | `capabilities/08-auto-captions.md` | 2026-09-14 | 2026-09-14 | **Approved with round 3 as the house default** (`house-style.md`: Arabic-only Auto captions + "Classic: black box" template, lower third). **Round 3 demonstrated 2026-09-14**, after feedback "We should have only one language Arabic, instead of bilingual Arabic + English". On `0914 (4)-copy`: Auto captions Arabic + **Bilingual None** + Delete current captions ✓ → 1 track × 239 (≈3 s, identical to earlier recognitions). "Classic: black box" template re-applied via Text ▸ Templates (kept y −0.73, lower third). «حاجة 1» → «حاجة واحدة» fixed (1 of 239 changed). Frames checked inside short, long and fixed captions; undo/redo gate; saved via Back to home page; original `0914 (4)` and user projects untouched. **Round 2 demonstrated 2026-09-14** (after feedback "Try bilingual captions, and restyle"), on CapCut duplicate `0914 (4)-copy`. Steps: Auto captions Arabic + **Bilingual English** + Delete current captions ✓ → 2 tracks × 239 (English = "sub captions" `sub_type` 5; ≈5 s regeneration). **Caption template "Classic: black box"** (`边框弹出黑色`, word-by-word black-box highlight, Pro diamond) applied via the selected caption's inspector **Text ▸ Templates**, once per track; the left Captions ▸ Templates panel only previews. The template pushed English to Position Y −1292 (off-frame); fixed natively with Transform Position Y −700 (Apply to all sub captions, one undo step). Verified: all 478 captions keep text and timing; on-screen checks inside captions for both languages; undo/redo; saved; original `0914 (4)` and user projects untouched. **Earlier feedback:** "Try bilingual captions, and restyle". User choices: restyle with a caption **Template**, second language **English**, work on a **CapCut duplicate**: `0914 (4)-copy` created 16:28 (structure diff vs `0914 (4)` = No differences; source mtime unchanged). **First demonstration result:** Captions → Auto captions → Spoken language **Arabic** → Generate (Pro tag, no credit prompt): 239 captions in ≈80 s for 7:30. Selected a caption → Text ▸ Basic (Apply to all main captions ✓) → preset tile "white with black outline" + font size 7 → 11: one style signature × 239, position y −0.73. Fixed «حاجة 1» → «حاجة واحدة» in the caption text box: exactly 1 caption changed, `words` not updated, text undo per character. Timing: ↓ stops at caption boundaries; 3 spots frame-exact. Longest caption wraps to 2 lines inside the frame; one wrap split a word. **Speaker-ID captions: no control found** in the 9.4 Auto captions form. Saved; structure diff = the added caption track only. `cc.py --contains` now matches AutomationId. Practice project `0914 (4)` (7:30 Egyptian-Arabic talking head, with rung 6–7 edits). `0914 (1)` was opened first but rejected: it is gym footage whose transcript is song lyrics. Credits consent: "Approve, start Cap 8" (option text said captions may use credits). `0914 (5)`: leave alone (user). |
| 9 | Animated text: word-by-word, titles, text templates | shorts, promo | approved | `capabilities/09-text-animations.md` | 2026-09-14 | 2026-09-14 | **Demonstrated 2026-09-14** on `0914 (4)-copy` (carries the approved house captions).<br>**Template choice:** Text ▸ Text template ▸ search «عربي» (Arabic templates, most without Pro). A 12-tile contact sheet was shown, and the user picked "3 yellow bold (Recommended)", resource 7659823758919699730.<br>**Preview:** clicking a tile only previews ("Previewing — Text template", composited over the real timeline, draft unchanged). Hover shows +.<br>**Add:** playhead Home + 30 × → = 00:00:01:00, then +. Result: a new text track with 1 `text_templates` segment, 1.000 s + 3.000 s (template length), with a built-in **in** animation 0–1 s (type-on) and no out.<br>**Title:** «زهقت من التأجيل» via Text ▸ Basic "The 1 paragraph" box, Ctrl+A, paste. It replaced the two-line placeholder.<br>**Placement:** scale 100% clipped both frame edges; set Scale 55. Position Y 450 crossed the eyes and 700 grazed the head, so the final is **Y 800** (`transform.y` 0.74074, upper fifth).<br>**Frames:** type-on at 1:12, full title at 2:15 and 3:25 above the head and clear of the lower-third captions, gone at 4:05.<br>**Gate and save:** Ctrl+Z → Y 700, Ctrl+Shift+Z → Y 800. Saved via Back to home page. Final diff is the 6 additive lines only; 239 house captions and rung-7 keyframes intact; every other project untouched, including the user's new `0914 (6)`.<br>**New helpers:** `cap9/title_check.py` (retries half-written drafts), `material_probe.py`, `contact_sheet.py`. |
| 10 | B-roll / overlay track (picture-in-picture) | YouTube, promo | approved | `capabilities/10-b-roll.md` | 2026-09-14 | 2026-09-14 | **Demonstrated 2026-09-14** on `0914 (4)-copy`.<br>**Choice:** 11 `E:\videos` candidates were shown as a contact sheet (bundled ffmpeg, read-only). The user picked #6 `VID_20260501_233809.mp4` (38 s, portrait via −90° rotation), at 01:36 over «ابلكيشنز انا عايز اعملها», as PiP.<br>**Import:** Ctrl+I, set-value id 1148, Open. `draft_content` is unchanged; only `draft_meta_info` records the file. Import enters "Previewing — video". A ruler click doesn't leave preview; an empty-timeline click does.<br>**Place:** a ruler click snapped to 01:31:29, then 63 × → gave 00:01:34:02. Dragging the media card above the tracks at the playhead's x created **overlay track 3 (flag 2)**, snapped exactly to 94.067 s.<br>**Trim:** 60 × → then **Q** gave start 96.067 s with source in 2.000 s and no ripple. 120 × → then **W** gave 4.000 s, ending 100.067 s.<br>**PiP:** Video ▸ Basic Scale 40. Position X −775 / Y 265 landed at half the expected offset, which revealed that **`transform` 1.0 = half the canvas** (one typed unit = ½ px, confirmed by measuring the box). Final **X −1557 / Y 528** is the upper-left corner with ≈60 px margins, clear of the face and captions.<br>**Mute:** track speaker icon, `attribute` 1.<br>**Stacking:** the overlay track sits at the top of the stack and renders above text. Harmless here, since the PiP avoids the text.<br>**Frames:** none at 1:35:25; PiP at 1:36:02, 1:38:20 and 1:40:01; gone at 1:40:02.<br>**Gate and save:** Ctrl+Z → Y 265, Ctrl+Shift+Z → 528. Saved via Back to home page. Final diff is additive only: track +1, segment +1, per-clip materials +1. Captions, title and rung-7 keyframes intact; all other projects untouched.<br>**Corrections recorded:** Position-unit notes in rungs 6, 8 and 9, `accessibility-controls.md` and `house-style.md` (values unchanged). The empty-space click above an overlay row seeks but does not deselect. |
| 11 | Audio Pro: vocal isolation, enhance voice, noise reduction, music + ducking | Pro AI | demonstrated | `capabilities/11-audio-pro.md` | 2026-09-14 | | **Demonstrated 2026-09-14** on `0914 (4)-copy`, all 7 main clips (Ctrl+click multi-select → Inspector Audio ▸ Basic). User chose Enhance voice + Noise reduction + Normalize loudness, no music, "run; stop if a cost appears", whole talk.<br>**Reduce noise** (Pro checkbox, found in 9.4 below Video translator): instant, "Noise reduced" toast, draft `realtime_denoises` ×7 (denoise_v2, rate 0.85); a real-time filter, no file written.<br>**Enhance voice** (Pro, Intensity 75): **asynchronous ≈11 min**, shown as "Applying 7 features…" / "Enhancing voice… N%". Draft `vocal_beautifys` ×7 saved instantly. Results land in `Resources/audioAlg/` (upload WAV → vocal/background split → enhanced, non-WAV).<br>**Normalize loudness** (Pro): instant, draft `loudnesses` ×7, **target fixed at −23 LUFS**, analysed avg −11.3…−13.8 (after enhancement), UI "Normalized loudness to -23 LUFS".<br>No credit, cost or upsell dialog for any of them.<br>**Gate and save:** Ctrl+Z / Ctrl+Shift+Z on Normalize (0↔7, identical). Saved via Back to home page. Final diff = the three material types ×7 plus refs only; captions, title, PiP and keyframes intact; all other projects untouched.<br>**Not verifiable without an export:** the actual sound (the agent can't listen; caches are obfuscated). Source reference: clip 0 −14.2 LUFS / LRA 4.7 / TP −1.4.<br>**New helpers:** `cap11/audio_check.py`, `apply_watch.py`. |
| 12 | Vertical: 9:16 canvas, auto reframe, beat-synced cuts | shorts | not-started | `capabilities/12-vertical.md` | | | |
| 13 | Visual Pro AI: remove background, stabilization, camera tracking | Pro AI | not-started | `capabilities/13-visual-ai.md` | | | |
| 14 | Promo polish: transitions, filters/adjust/color, logo/brand overlay, templates | promo | not-started | `capabilities/14-promo-polish.md` | | | |
| 15 | Export: resolution up to 4K, fps, bitrate, codec; verify the output file | all | not-started | `capabilities/15-export.md` | | | |
| 16 | End-to-end talking-head YouTube edit | YouTube | not-started | `capabilities/16-e2e-youtube.md` | | | |
| 17 | End-to-end vertical short | shorts | not-started | `capabilities/17-e2e-short.md` | | | |

## What "demonstrated" must show, per rung

- **0.**
  - `setup.ps1` works and `cc.py windows/tree/screenshot` work against the live CapCut.
  - DPI mapping is proven: clicking a tree element's rectangle centre hits it.
  - Every major area in `accessibility-controls.md` is filled in with its tree coverage level
    (full/partial/none), key named controls, and what needs screenshots.
  - Pro feature locations and tier badges are recorded in `pro-features.md`.
  - Shortcuts are checked against CapCut's own shortcut list.
  - Documents whether your agent's sandbox allows desktop input.
  - No project is modified.
- **1.**
  - The duplicate is created through CapCut's UI and the original is untouched (its draft
    `update_time` is unchanged).
  - The playhead is placed at a stated time and the player timecode confirms it.
  - One split: the draft diff shows one segment becoming two at that time.
  - Undo reverts it (diff) and redo re-applies it.
  - The project is saved/closed cleanly.
- **2.**
  - Each basic operation is demonstrated once on the copy, with a diff per operation.
  - Ripple vs non-ripple behaviour and the magnet/main-track setting are documented.
- **3.**
  - CapCut's transcript/"remove pauses/filler words" route is run on real talking footage.
  - Settings used are documented. The before/after duration and segment count are shown.
  - The result is spot-checked at 3 cut points by screenshot or playback.
- **4.**
  - A repeated take is identified in the transcript and the bad version removed natively.
  - The kept take is named and the diff confirms the removed range.
- **5.**
  - Remaining breaths/gaps are found on the waveform (screenshots) and tightened.
  - The criteria used are documented (gap length, what gets kept).
- **6.**
  - Alternating punch-in at cuts with a stated scale/position.
  - Eye-line continuity is checked visually on adjacent frames.
  - Shot-specific values are flagged as such.
- **7.**
  - A keyframed scale move with easing over a stated range.
  - Keyframes are visible in the diff (`keyframes`/`common_keyframes`), and a playback screenshot
    is taken at start/mid/end.
- **8.**
  - Auto captions are generated (language stated) and a style is applied.
  - Timing is spot-checked and any caption errors fixed natively.
  - Credits/Pro gating is recorded.
- **9.**
  - Animated text is added at a stated time, with a word-by-word or template animation and style.
  - Readable in screenshots.
- **10.**
  - B-roll is placed on an overlay track at a stated range with a stated scale/fit.
  - Audio handling (muted/kept) is decided and verified.
- **11.**
  - Each audio tool is applied to a clip, with its settings documented.
  - For vocal isolation/enhance: credits are confirmed with the user before running, and the
    result is listened to or waveform-compared.
- **12.**
  - Canvas switched to 9:16 and auto reframe applied.
  - Beat marks created and cuts aligned to them.
  - Framing is checked by screenshot.
- **13.**
  - Each tool is applied to a clip. Processing waits are recorded, and results checked by
    screenshot.
  - Credits are confirmed first.
- **14.**
  - One of each (transition, filter/adjust, logo overlay) is applied and verified in the diff and
    by screenshot.
- **15.**
  - Export dialog settings are documented and the file is exported to a user-approved folder.
  - Bundled `ffmpeg -i` confirms resolution/fps/duration.
- **16/17.**
  - The full edit runs using only approved rungs, from raw takes to exported file.
  - The user reviews the final video.

## Approval log

| Date | Rung | User's words | Commit |
|---|---|---|---|
| 2026-09-14 | 0 | "Approve, fill gaps first" (approved; mapped the listed gaps without editing before starting rung 1) | see git log |
| 2026-09-14 | 1 | "Approve, start Capability 2" | see git log |
| 2026-09-14 | 2 | "Approve, start Cap 3 (credits OK)", which also consents to credit use for rung 3 | see git log |
| 2026-09-14 | 3 | "Approve, try Cap 4 on 152759" | see git log |
| 2026-09-14 | 4 | "Approve, start Cap 5" (the approved plan uses detected pauses + caption word timings as the gap finders) | see git log |
| 2026-09-14 | 5 | "Approve + reusable script": approve, then turn cut_gaps.py into a parameterised `scripts/tighten_gaps.py` before continuing | see git log |
| 2026-09-14 | 6 | "Approve, start Cap 7" | see git log |
| 2026-09-14 | 7 | "Approve, start Cap 8" (also: leave `0914 (5)` alone; the option text covered caption credits) | see git log |
| 2026-09-14 | 8 | "Approve, make it default", after round 1 feedback "Try bilingual captions, and restyle" and round 2 feedback "We should have only one language Arabic, instead of bilingual Arabic + English". Arabic-only + Classic black-box template is recorded as the default caption style in `house-style.md` | see git log |
| 2026-09-14 | 9 | "Approve, start Rung 10 (Recommended)". Accepted as demonstrated: Arabic text template #3 title, 1:00-4:00, scale 55%, Y 800, hard cut out (no out animation). Not a house default | see git log |
| 2026-09-14 | 10 | "Approve, start Rung 11 (Recommended)". Accepted as demonstrated: muted upper-left PiP (clip #6, 40%, X -1557 / Y 528) at 00:01:36:02-00:01:40:02, plus the Position-unit corrections (typed unit = 1/2 canvas px). Not a house default | see git log |
