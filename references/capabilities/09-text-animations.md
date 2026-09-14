# Capability 09: Animated text (titles, text templates, word-by-word)

## Status
- **Ladder status:** in-progress
- **CapCut version:** 9.4.0.4015
- **Demonstrated:** not yet
- **Approved:** not yet
- **Practice project:** `0914 (4)-copy`. It is the agent-owned duplicate carrying the approved
  house captions (Arabic-only, "Classic: black box") plus the rung 4–7 edits, 7:30.533.
- **Evidence:** `evidence/2026-09-14/cap9/`

## Goal
Add animated on-screen text at a stated time, separate from the auto captions:
- a **title** near the start: an Arabic headline with an in/out animation, or a text template
- its style, position and duration stated and verified

It must be readable in screenshots and must not collide with the house captions in the lower
third. Record the native route (Text asset tab → Add text / Text template → inspector Text ▸
Animation), how animations are stored in the draft, and how to verify them frame by frame.

## Preconditions
- Rungs 0–8 approved. House style in `references/house-style.md`: captions stay Arabic-only in
  the lower third, so titles go in the upper area.
- Tools reused:
  - ruler + Home/↓ + arrows for exact playhead placement (rungs 1, 5)
  - Text ▸ Basic text box / font / size / Transform Position (rung 8)
  - Text ▸ Templates (rung 8)
  - template-aware draft dumps (rung 8)
  - undo/redo gate and Back to home page save

## Plan
1. **Map the Text asset tab:** Add text, Text templates (categories, Pro badges), Text effects, and
   how a text element lands on the timeline (new text track, default duration, playhead position).
2. **Add a title** at a stated time (e.g. 00:00:01:00, 4 s long). Type an Arabic title (text to be
   confirmed with the user), style it (size, bold, colour or template), and place it in the upper
   third (Transform Position Y positive).
3. **Animate it:** inspector **Animation** tab (In / Out / Loop), pick an in and out animation with
   stated durations. Or use a text template with built-in animation.
4. **Verify:**
   - draft: new text segment at the stated start/duration, its material, animation refs
     (`material_animations`), position
   - frames at the start of the in animation, mid-hold and during the out animation
   - no overlap with a house caption at the same time
5. **Undo/redo, save,** then the draft check.

## Procedure

### A. Open the practice copy (executed 2026-09-14)
1. Home, then `scroll 1100 700 -5`, then a grid screenshot. Read the card names: the **first card
   read "0914 (4)-copy"** (≈383,680), the newest draft.
2. Check the draft mtime is unchanged since the baseline (19:23:11.901). The user sometimes reviews
   in CapCut between turns.
3. Click the card, then `focus --maximize`, and confirm the title bar reads **0914 (4)-copy**.
4. Asset tab **Text** (≈164,73).
   - **Observed** (`text-tab.png`): the title bar reads **0914 (4)-copy** and the draft is
     unchanged.
   - Left sub-list:

     | Item | Position |
     |---|---|
     | **Add text** (selected by default) | ≈(57,131) |
     | Yours ▾ | ≈(85,171) |
     | Text effects ▾ | ≈(85,211) |
     | **Text template ▾** | ≈(85,251) |
     | Auto captions | ≈(75,291) |
     | Local captions | ≈(78,331) |

   - The Add text grid shows a single **"Default text"** card (≈231,165).
   - The right panel shows project Details, because nothing is selected. The timeline has the
     house caption row (TT, y≈763) above the video.

### B. Text ▸ Text template panel (observed 2026-09-14, `text-template-open.png`)
- **Open:** click **Text template ▾** (≈85,251). It expands inline into categories and loaded
  within ≈6 s. The draft was unchanged.
- **Categories:**

  | Category | Position |
  |---|---|
  | **Trending** (default, cyan) | ≈(57,291) |
  | Whimsical | ≈(64,331) |
  | KATSEYE 👠 | ≈(64,371) |
  | Pixel Bead 👾 | ≈(69,411) |
  | Classic | ≈(55,451) |
  | NEW | ≈(47,491) |

  More categories are below, and the list scrolls.
- **Search:** "Search for text templates" (≈370,127), with a filter icon ≈(565,127).
- **Grid:** 3 columns, tiles ≈129 px apart horizontally and ≈123 px vertically, starting at tile
  centre ≈(231,240).
  - Each tile has a ⬇ download icon at its bottom-right.
  - **Most tiles carry a purple Pro diamond** (top-left).
  - Trending examples: "Chapter End" (Pro), "FINAL" flames (Pro), "The Story Begins" (Pro), "KEEP
    GOING" (Pro), "LOCATION" pin, "Breaking News" (Pro), "BAM!" comic (Pro), a Thai-script
    title (Pro), "CREATIVE" glow (Pro).
  - These are English/Latin previews. Arabic shaping must be verified on the player after typing
    the title.
- **Classic** (≈55,451): "CINEMATIC", "THE MOMENT BEGINS WITH ONE SCENE", "CREATIVE", "EXCLUSIVE",
  "SPECIAL OFFER" (all Pro). "TITLE HERE", "Simple Title" and "Simple Font" have no diamond.
- **NEW** (≈47,491): mostly Pro, except the "ABC" pair. Scrolling the category list (`scroll 80 450
  -3`) reveals Hits, Free Fire, Icons, **Title**, Retro, Advertisement, Social media, Tag, Vlog.
- **Search is the route to Arabic templates.** Click the search box (≈370,127), `type "عربي"`
  (clipboard paste), then Enter. After ≈5 s the grid fills with Arabic-script templates.
  - Most carry **no Pro diamond**. Examples: «الفرح في البساطة» (white brush), «يوم عادي، حياة
    عادية» (yellow bold), «الحياة تستمر» (glow calligraphy), «حياة صغيرة» (colour outline),
    «وتشرق الشمس» (green box), «يوم بسيط» (several), «استمتع بالوقت» (yellow frame), «قليلا الحياة»
    (red circle).
  - Some Latin and other scripts are mixed in: Vietnamese, Korean, French, German, Filipino.
  - While a search is active, the **category list is hidden**. The left column shows only the
    collapsed sub-list.
- **Scrolling the grid:** scroll at **(370,400)**, 3 ticks ≈ 1.3 rows. The panel ends at screen
  y≈565, and a scroll at y 600 lands on the timeline instead. Browsing, searching and scrolling
  never changed the draft (mtime unchanged).
- Candidate contact sheet: `evidence/2026-09-14/cap9/templates/title-candidates-sheet.png`, built
  with `cap9/contact_sheet.py`.

## Wait conditions

## Verification

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|
| Between turns the editor was closed (Home showing) and the copy's draft mtime moved 19:23:11 → 19:49:10. `diff` then listed 22 caption rows as `material changed` with identical text. | The user reviewed or closed the project, and CapCut re-serialized 22 caption text materials on close. `material_probe.py` showed only the summary `sig` hash differs. Text, template (239 × 边框弹出黑色), y −0.73 and the video track are unchanged. | Not an edit, so no action. Before trusting a baseline, re-run `track_styles.py` plus `diff`. Treat `material changed` with an identical name as re-serialization only after the template/position/text checks pass. The user also created `0914 (6)` at 20:05, which the agent does not touch. |

## Tree coverage notes

## User choices (2026-09-14)
- **Title text:** «زهقت من التأجيل» ("I'm done procrastinating"), the video's opening line and
  theme.
- **Build:** a **text template** from CapCut's Text ▸ Text templates, with built-in animation. Show
  the options before applying, because template choice is a taste decision.
- **Placement:** near the start, upper part of the frame, clear of the lower-third house captions.
- Baseline before any rung-9 change: `evidence/2026-09-14/cap9/baseline.json` (2 tracks, 246
  segments, draft 19:23:11).

## Open questions for the user
- Which text template (shown as a contact sheet before applying).
