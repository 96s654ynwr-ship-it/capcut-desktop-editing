# CapCut Accessibility and Control Map (Windows)

- **CapCut version mapped:** 9.4.0.4015 (Capability 0 in progress)
- **OS / scale:** Windows 10 Pro, English UI. Display at 125% (DPI 120). CapCut maximized, window
  rect 0,0 → 1920,1030 physical px.
- **UI framework:** Qt 6.2.2 (window class `Qt622QWindowIcon`; Qt Quick/QML + Qt Widgets) with CEF
  web panels (from the DLLs in the install folder)
- **Mapped by / date:** Claude Code, 2026-09-14 (home screen only so far)

This is an audit of what the Windows UI Automation (UIA) tree exposes. It isn't an exhaustive
manual. Every row carries an evidence label (`observed` / `executed` / `agent-verified` /
`user-approved`). Don't record pixel coordinates. Record names, control types, AutomationIds,
routes and visual landmarks. Re-verify after CapCut updates.

## Headline finding (observed, 2026-09-14)

**The CapCut home window exposes only its root element to UI Automation.** With CapCut verified in
the foreground:

| Probe | Result |
|---|---|
| Root element | `Window "CapCut"`, AutomationId `HomeWindow`, ClassName `HomePageX_QMLTYPE_186`, FrameworkId `Qt`, Value pattern = "CapCut" |
| RawViewWalker / ControlViewWalker from root | 1 element (root only) |
| `FindAll(TreeScope_Descendants, TrueCondition)` | 0 |
| `ElementFromPoint` on a 60 px grid over the window (CapCut-owned elements only) | 1 distinct element: the root |
| MSAA `AccessibleObjectFromWindow(OBJID_CLIENT).accChildCount` | 0 |
| Focused element | the root window |

The Qt UIA bridge is loaded and answers, but CapCut's QML item tree isn't published through it:
the items have no accessible roles, or are marked ignored. Until a later probe finds otherwise, **the
home screen is screenshot-driven**: landmarks + grid coordinates + keyboard.

Still to probe (needs the user's go-ahead):
- the **editor** window (a different QML root, may differ)
- popups, menus and dialogs (separate top-level windows)
- CEF web panels
- relaunching CapCut with `QT_ACCESSIBILITY=1`

The probe script is kept at `evidence/2026-09-14/cap0/uia_probe.py` (gitignored).

## Coverage summary

| Area | How to reach it | Tree coverage | Named controls worth knowing | Needs screenshots for |
|---|---|---|---|---|
| Home / project list | App launch | **none** (observed) | root `Window` id `HomeWindow` only | everything |
| Editor top bar (menu, project name, Export, account/Pro) | Open a project | ? | | |
| Asset toolbar (Media, Audio, Text, Stickers, Effects, Transitions, Captions, Filters, Adjustment, Templates, AI…) | Top-left of editor | ? | | |
| Media panel (import, local/library items) | Media tab | ? | | |
| Player (play/pause, timecode, ratio, fullscreen, quality) | Centre | ? | | |
| Inspector (right panel: Video/Audio/Text/Speed/Animation/Adjust tabs, AI tools) | Select a clip | ? | | |
| Timeline toolbar (select/split/delete/freeze/reverse/mirror/crop, magnet, linkage, preview axis, zoom) | Above the tracks | ? | | |
| Timeline tracks (clips, waveforms, playhead, ruler) | Bottom | ? | | |
| Transcript / text-based editing panel | ? | ? | | |
| Context menus (right-click clip/track) | Right-click | ? | | |
| Export dialog | Export button / Ctrl+E | ? | | |
| Settings / Shortcut list | Menu | ? | | |
| Modals: upsells, login, update prompts | Spontaneous | ? | | |

Coverage levels:
- `full`: every control needed is named in the tree
- `partial`: some controls are named, others need screenshots
- `none`: the area is custom-drawn and needs screenshots

## Method notes

- **Tree size:** home = 1 node.
- **Qt lazy activation:** a retry after 1.2 s and again after 3 s changed nothing. It's not a
  timing issue on the home screen.
- **Icon-only buttons:** can't tell from the tree; nothing is exposed. Use hover tooltips plus
  screenshots.
- **Popups/menus as separate windows:** not yet checked.
- **CEF:** not yet checked.
- **DPI:** the process is per-monitor aware. The window rect from DWM (0,0,1920,1030) matched the
  screenshot layout exactly at 125% scale. A click-mapping test is still pending, because it needs
  a harmless clickable target.
- **Agent sandbox:** Claude Code (desktop app, Windows) ran UIA queries, `SetForegroundWindow` and
  screen capture without any escalation.
- **Foreground stealing:** the Claude desktop app re-raised itself during a probe, and a
  point-sweep sampled the Claude window instead. Always verify the foreground and the element's
  `ProcessId`. `cc.py` screenshots now refocus CapCut and report `foreground_ok`.

## Areas

For each area add a table:

| Control | ControlType | Name / AutomationId | Patterns / state | Context landmark | Evidence |
|---|---|---|---|---|---|

### Home / project list

**Tree:** root only (see Headline finding). **Visual landmarks** (observed from a screenshot at
125%, maximized; positions are descriptive, not coordinates):

| Control | Landmark | Evidence |
|---|---|---|
| Account card | Top of left sidebar: avatar, account name, **Pro** badge with "View details", renewal date, "Create with Teams" button | observed |
| Sidebar nav | Left sidebar below the account card: Home, Templates. "Create with AI" group: Video Studio, Design Studio. "More tools" (expandable): Create with AI, Marketing tools. "Management": Library. Invite friends | observed |
| **Create project** | Large full-width cyan banner button at the top of the main area, "+" icon | observed |
| AI tool cards | Row under Create project: AI video, AI image, Extend video, AI edit, Enhance quality, AI remove | observed |
| AI-powered creative suite | Carousel: Video Studio, Design Studio, AI ad maker, Long video to shorts, with a ">" arrow at its right | observed |
| Projects section | "Projects" heading with search icon, grid/list toggle, **Trash**, **Project sync** buttons on the right; project thumbnail cards below (scroll down for more) | observed |
| Title bar | Top-right icon row before the minimize/maximize/close controls (purpose to confirm by hover tooltips) | observed |

### Editor top bar

### Asset toolbar

### Media panel

### Player

### Inspector

### Timeline toolbar

### Timeline tracks

### Transcript editor

### Context menus

### Export dialog

### Settings / shortcuts

### Modals
