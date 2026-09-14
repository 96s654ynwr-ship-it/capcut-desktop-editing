# House style (user-approved defaults)

These are the editing defaults this user has approved. Apply them unless the user asks for
something else in the current request. Each entry names the approval and the procedure that
produces it. Change an entry only when the user approves a change, and log it here.

## Captions (talking-head videos)

**Approved 2026-09-14** ("Approve, make it default", rung 8 round 3). Procedure:
`capabilities/08-auto-captions.md`, section G, the round-3 recipe.

| Setting | Default | Notes |
|---|---|---|
| Languages | **Arabic only** | The user rejected bilingual Arabic + English ("We should have only one language Arabic"). The bilingual route stays documented as an option, never the default. |
| Generation | Captions ▸ Auto captions → Spoken language **Arabic** → Bilingual **None** → Generate | Tick **Delete current captions** when replacing an existing set. Regeneration discards manual text fixes. |
| Look | Caption template **"Classic: black box"** (`边框弹出黑色`, resource 7331662668685774086) | Word-by-word: bold white Arabic, with the current word on a black box. Long captions are paged into short chunks. Pro diamond on the tile. |
| How to apply | Select any caption → inspector **Text ▸ Templates** → **Classic** chip → first tile | Applies to all main captions. The left Captions ▸ Templates panel only previews. |
| Position | Lower third, `clip.transform.y` **−0.73** (inspector Position Y −788; the real offset is ≈394 px below centre, since transform 1.0 = half the canvas, corrected 2026-09-14 in rung 10) | A single-language template keeps this position. Check frames inside captions. |
| Text fixes | Read captions for digits written instead of words (e.g. «1» → «واحدة»), English brand names and dialect words | Fix natively in Text ▸ Basic text box → Ctrl+A → type the full text, then poll until fully saved. |

**Verify every time:**
- one text track, all captions `text_templates` "边框弹出黑色", all `ar-SA`
- caption text and timing unchanged apart from intended fixes (template-aware dump)
- player frames inside a short and the longest caption
- undo/redo gate, then Back to home page

## Change log

| Date | Area | Change | User's words |
|---|---|---|---|
| 2026-09-14 | Captions | Default set: Arabic-only + Classic black-box template, lower third | "Approve, make it default" |
