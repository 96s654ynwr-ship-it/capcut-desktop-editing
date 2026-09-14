# CapCut Pro / AI Feature Catalog (desktop, Windows)

The user has a **CapCut Pro** subscription. Tiers, locations and names change often and vary by
region and account.

**Every row starts `unverified`.** The "Reported location" column comes from public
documentation and marketing pages. It is a lead to check, not a fact. Capability 0 (and later
rungs) replaces it with the route actually observed in this install. Columns:

- **Tier badge seen:** the badge CapCut shows (Pro, crown, credits icon, none).
- **Credits?:** whether running it spends AI credits. If it does, confirm with the user before
  every run.
- **Rung:** the ladder capability that will demonstrate the feature.

| Feature | Reported location (unverified lead) | Verified route (tree/landmark) | Tier badge seen | Credits? | Rung | Status |
|---|---|---|---|---|---|---|
| Auto captions | Captions/Text tab → Auto captions | Captions → Auto captions → Spoken language (Arabic) → **Generate** | "Pro" tag on Generate | none seen | 8 | **agent-verified 2026-09-14**: ≈80 s for 7:30 Arabic, 239 captions, no credit prompt |
| Speaker-identified captions | Auto captions options | **not found** in the 9.4.0.4015 Auto captions form or language list | | | 8 | observed absent 2026-09-14 (check caption inspector next) |
| Transcript-based editing ("edit via transcript") | Captions area or clip context | Timeline toolbar (clip selected) → **Transcript** icon | Pro diamond | ? | 3 | route observed 2026-09-14 (not run) |
| Split scenes | — | Timeline toolbar (clip selected) → **Split scenes** | "Free" badge | ? | 2 | route observed 2026-09-14 (not run) |
| AI extend | — | Timeline toolbar (clip selected) → **AI extend** | none seen | likely | — | route observed 2026-09-14 (not run) |
| AI edit | — | Timeline toolbar (clip selected) → **AI edit** | none seen | likely | — | route observed 2026-09-14 (not run) |
| Auto adjust | — | Timeline toolbar (clip selected) → **Auto adjust** | Pro diamond | ? | 14 | route observed 2026-09-14 (not run) |
| Enhance visuals | — | Timeline toolbar (clip selected) → **Enhance visuals** (HD icon) | none seen | ? | — | route observed 2026-09-14 (not run) |
| Extract audio | — | Timeline toolbar (clip selected) → **Extract audio** | none seen | no | 2 | route observed 2026-09-14 (not run) |
| Freeze frame | — | Timeline toolbar (clip selected) → **Freeze** | none seen | no | 2 | route observed 2026-09-14 (not run) |
| Remove filler words / pauses | Transcript editor | | | | 3 | unverified |
| Vocal isolation | Inspector → Audio | | | | 11 | unverified |
| Enhance voice | Inspector → Audio | | | | 11 | unverified |
| Reduce noise | Inspector → Audio | | | | 11 | unverified |
| AI voice effects / voice changer | Inspector → Audio / Voice changer | | | | 11 | unverified |
| Text to speech | Text inspector | | | | — | unverified |
| Auto ducking / loudness normalize | Inspector → Audio | | | | 11 | unverified |
| Beat detection (auto beat marks) | Audio clip → Beat / timeline toolbar | | | | 12 | unverified |
| Auto reframe | Inspector → Video / canvas ratio | | | | 12 | unverified |
| Remove background (auto) | Inspector → Video → Remove BG | | | | 13 | unverified |
| Chroma key | Inspector → Video → Remove BG | | | | 13 | unverified |
| Stabilization | Inspector → Video | | | | 13 | unverified |
| Camera tracking | Inspector → Video / tracking | | | | 13 | unverified |
| Motion tracking | Inspector → Video / tracking | | | | 13 | unverified |
| Relight / retouch | Inspector → Video | | | | — | unverified |
| Enhance quality / upscale | Inspector → Video | | | | — | unverified |
| Smooth slow-mo (frame interpolation) | Inspector → Speed | | | | — | unverified |
| Color match / auto color correction | Inspector → Adjust | | | | 14 | unverified |
| Masks | Inspector → Video → Mask | | | | 14 | unverified |
| Keyframes | Inspector property diamond icons | | | | 7 | unverified |
| Pro transitions / effects / filters / text templates | Asset toolbar tabs (Pro badge on items) | | | | 9, 14 | unverified |
| Long video to shorts | Home screen tools | | | | — | unverified |
| Export 4K / high fps / high bitrate | Export dialog | | | | 15 | unverified |
| Cloud storage / space sync | Home screen / project menu | | | | never (side effect) | unverified |

## Pro badges observed in the UI (2026-09-14, CapCut 9.4.0.4015)

A purple diamond next to a control or on a library card is the Pro marker. None of these were
run, so credits are unknown.

| Feature | Verified route | Badge |
|---|---|---|
| Normalize loudness | Inspector → Audio → Basic | Pro diamond |
| Enhance voice | Inspector → Audio → Basic (▾ options) | Pro diamond |
| Video translator | Inspector → Audio → Basic; also Asset → AI avatar | Pro diamond |
| Voice changer | Inspector → Audio → **Voice changer** sub-tab | (to check) |
| Velocity effects | Inspector → Speed → sub-tab | Pro diamond |
| Curve speed | Inspector → Speed → **Curve** sub-tab | none seen |
| Smooth slow-mo | Inspector → Speed → Standard (disabled for normal-speed clips) | Pro diamond |
| Auto adjust | Inspector → Adjust → Basic; also timeline toolbar | Pro diamond |
| Color match | Inspector → Adjust → Basic | Pro diamond |
| Color correction | Inspector → Adjust → Basic | Pro diamond |
| LUT / HSL / Curves / Color wheel / Mask | Inspector → Adjust | none seen |
| Stabilize | Inspector → Video → Basic | Pro diamond |
| Remove BG / Mask / Retouch | Inspector → Video sub-tabs | (to check inside) |
| Auto captions → Generate | Asset → Captions → Auto captions → **Generate** | "Pro" tag on button. **Agent-verified 2026-09-14:** no credit prompt. Loading window `id="Generating captions... N%"`. About 122 s for 8:43 of Arabic. Produces a text track whose materials carry per-word `words.start_time/end_time`, readable with `draft_inspect.py words` |
| Bilingual captions | Asset → Captions → Auto captions → Bilingual captions (list: None, Bengali, Burmese, Chinese, Dutch, English, …; the spoken language is excluded) | Pro diamond. **Agent-verified 2026-09-14 (Arabic → English):** no credit prompt. Regenerating with Delete current captions ✓ took ≈5 s (recognition reused). Produces 2 text tracks: translation = "sub captions" (`sub_type` 5, style size 5, placed below) and speech = "main captions". Manual text fixes are lost on regeneration |
| Caption templates | Selected caption → inspector Text ▸ **Templates** (chips Trending / Classic / NEW …) | Most tiles carry a Pro diamond, including Classic "black box" `边框弹出黑色`. **Agent-verified 2026-09-14:** applies to all captions of the selected track only (main or sub). Segments become `text_templates` + `effects` (`text_effect`); word-by-word highlight; can move the caption (English went to Y −1292, off-frame). The left Captions ▸ Templates panel only previews, and its "Generate captions" applies a template at generation time |
| Identify filler words | Asset → Captions → Auto captions (toggle, on by default) | Pro diamond |
| Auto lyrics | Asset → Captions | (to check) |
| AI avatar tools (Avatar library, Photo to avatar, Fashion model, Video translator, AI dialogue scene) | Asset → AI avatar | Pro diamond on each |
| Pro stickers / effects / transitions | Asset tabs; purple diamond on the card corner | Pro diamond |
| Auto removal (background) | Inspector → Video → Remove BG | Pro diamond |
| Custom removal / Chroma key | Inspector → Video → Remove BG | none seen |
| Brush mask / Pen mask | Inspector → Video → Mask | Pro diamond |
| Retouch (Face/Body/Hair, Auto styles, Skin) | Inspector → Video → Retouch | (to check per item) |
| Voice filters / Voice characters / Speech to song | Inspector → Audio → Voice changer | (cards not loaded yet) |
| Isolate voice (Keep vocal / Remove vocal) | Clip right-click → **Isolate voice ›** | "Free" badge |
| Extract audio | Clip right-click (Ctrl+Shift+S) | Pro diamond in context menu (toolbar icon showed none) |
| Transcript | Clip right-click; timeline toolbar | Pro diamond |
| **Remove filler words** (pauses / repeats / filler words) | Select a clip → timeline toolbar **Transcript** icon → "Analyzing… Identifying pauses…" (no confirmation dialog) → `RoughCutWindow` "Remove filler words" with tabs All/Pauses/Repeats/Filler words → tick items → **Delete** | Pro diamond on Delete. **Agent-verified 2026-09-14**: pause detection and Delete both ran with **no credit prompt or confirmation**. A 22.30 s pause was removed as a split plus a source skip, and it undoes in one step. Credit use isn't visible in the UI. Three analyses were run under the user's consent (23 s clip ×2, 2:15 take ×1) |
| Create multi-camera clip | Clip right-click | "Free" badge |

## Rules

- **Before running anything that shows a credits icon or cost,** state the feature, clip and
  expected cost, and wait for a yes.
- **If a Pro item still shows a lock or upsell,** don't click through to purchase. Record it as
  `blocked: upsell shown` and tell the user. The subscription may not cover it, or the login may
  have lapsed.
- **Record processing time and waiting indicators** for AI tools. Async steps are the most common
  cause of a procedure going wrong.
