# Control Strategy: operating CapCut like a person

Computer use is slow and eats context, so get as much as possible from cheap, structured sources.
Use pixels only where nothing else works.

## The four layers

1. **UI Automation tree** (`cc.py tree / find / act`). This is the cheapest and most precise
   source: names, control types, enabled/selected/toggle state, values, and rectangles.
   - Prefer `act invoke|toggle|select|expand|set-value`, which go through UIA patterns. They don't
     move the mouse and don't care about overlap.
   - Fall back to `act click` (the element's rectangle centre) when an element has no pattern.
2. **Keyboard shortcuts and menus** (`cc.py key`). These are stable across layouts. Make sure the
   focus is right first (see `keyboard-shortcuts.md`).
3. **Screenshots with a grid** (`cc.py screenshot --grid`). Use these for things the tree can't
   see: timeline clips, waveforms, the playhead, the ruler, the player canvas, thumbnails, and
   unlabeled icon buttons.
   - Grid labels are **screen coordinates**, so read a label and pass the number straight to
     `click` or `drag`.
   - Crop with `--region l,t,r,b` for detail instead of shooting the whole screen at full
     resolution.
4. **Draft JSON, read-only** (`draft_inspect.py`). Use it to prove what an edit changed. It is
   never an edit path.

## Loop discipline

- **Look, act (2–5 steps), look again.** Indices from `tree`/`find` are valid only until the UI
  changes. `act --index N` re-locates the node live by type, name and id, but still re-read after
  every batch.
- **Resolve ambiguity deliberately.** When a query matches several elements, `act` refuses and
  lists them. Tighten the query (`--type`, `--id`, `--within "<ancestor name>"`) or pass `--nth`
  after checking which one you mean.
- **Run `cc.py focus` before input.** Keyboard input goes to the foreground window. Mouse clicks go
  to whatever window is under the pointer.
  - Windows' foreground lock sometimes refuses the refocus
    (`WARN: could not confirm CapCut is foreground`). This was observed on 2026-09-14 while the
    Claude app kept re-raising itself.
  - A click still lands on CapCut if CapCut is visible under the pointer, but **never send keys
    after that warning**. Re-run `cc.py focus`, then `cc.py screenshot`, and check
    `foreground_ok` first.
- **Popups change size with their state.** Dialog buttons move when a tab changes the dialog's
  height. In the Shortcuts dialog, Cancel moved from y≈908 to y≈374.
  - Prefer fixed anchors, like a dialog's ✕ in its top-right corner, or take a new screenshot
    before clicking footer buttons.
  - Named dialog windows in the tree (`HelpDialog`, `ExportWindow_Container`) give their current
    rect.
- **Screenshot before and after anything irreversible.**
- **Stop on the unexpected.** A modal, upsell, crash dialog, login prompt or update prompt ends
  the batch. Deal with it (close/cancel) or ask the user.

## Qt 6 / QML specifics (CapCut 9.x)

> **Observed 2026-09-14 on 9.4.0.4015:** the home window's UIA tree is a single root element
> (`Window "CapCut"`, id `HomeWindow`, FrameworkId `Qt`). No children were found via walkers,
> `FindAll`, `ElementFromPoint` or MSAA. Treat CapCut as **screenshot-first**, and re-probe each
> new window type before assuming the same. The general Qt notes below still describe what to look
> for when probing.

- **Qt switches accessibility on lazily** when a UIA client first queries. A first dump can be
  nearly empty. `cc.py tree` retries once automatically, and if it's still sparse, focus the
  window and try again.
- **QML items are exposed only if the developers gave them an accessible role and name.** Expect:
  - menus, dialogs, text fields, checkboxes and labelled buttons → exposed
  - custom-drawn surfaces (timeline tracks and clips, waveform, player canvas, effect thumbnails)
    → usually not exposed, or exposed as unnamed `Pane`/`Custom` nodes with rectangles only
- **Icon-only buttons** may have an empty Name but a `HelpText` (tooltip). Use `tree --patterns`
  to see HelpText. If there's nothing, hover it (`cc.py act hover --index N` or `cc.py hover x y`),
  wait about a second, and screenshot the tooltip.
- **Popups, dropdowns, context menus and dialogs are separate top-level windows.** `tree`/`find`
  walk all visible CapCut windows by default. `--root window` restricts to the main window.
- **CEF (embedded Chromium) panels** show up as a `Document`/`Pane` subtree with web-style
  accessibility. They may need focus before their contents appear.

## Coordinates, DPI and windows

- **The scripts are per-monitor DPI aware.** Every coordinate (tree rectangles, grid labels,
  click/drag) is in **physical screen pixels**, so they agree with each other at any scale factor.
- **Keep CapCut maximized** (`cc.py focus --maximize`) on one monitor for consistent layouts.
  After any window move or resize, take a new screenshot before clicking by coordinate.
- **Never store coordinates in references.** Store landmarks instead: "Split = scissors icon,
  timeline toolbar, 2nd from left, tooltip 'Split'".

## Timeline technique (to be refined by rungs 1–2)

- **Positioning the playhead.** Candidate routes, to verify in rung 1:
  - click the ruler at a grid x-coordinate, then fine-tune with Left/Right (1 frame) while
    reading the player timecode
  - Up/Down to jump between edit points
  - any timecode entry field CapCut exposes

  Always confirm the final position from the player timecode (tree text or zoomed screenshot).
- **Zoom** the timeline (Ctrl+=/Ctrl+- or Ctrl+scroll) until the target region is wide enough to
  click accurately. Record the zoom route in the procedure.
- **Select clips** by clicking the clip body at a grid coordinate. Confirm selection by the
  highlight in a zoomed screenshot, or by the inspector switching to that clip's properties
  (tree).
- **Drag trims** use `cc.py drag` with `--steps 15+`, so Qt receives intermediate mouse moves.

## Async operations

- **AI captions, vocal isolation, background removal, tracking and export** run in the
  background. After starting one:
  - poll with `cc.py wait-for --contains "<done indicator>" --timeout <s>`, or `--gone` on a
    progress label
  - or take screenshots every 5–15 s
- **Record the indicators and typical durations** in the procedure file.

## Token economy

- Use `tree --filter interactive` for orientation, and `--root` on a subtree (`find` first, then
  `tree --within`) for detail.
- Use `screenshot --scale 0.5` for overview and `--region` for precision. Don't view full-res,
  full-screen shots repeatedly.
- Use `--json` dumps saved to evidence for later comparison instead of re-printing large trees.
