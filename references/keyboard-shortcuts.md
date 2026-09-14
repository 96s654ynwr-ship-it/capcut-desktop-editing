# CapCut Desktop Keyboard Shortcuts (Windows)

Shortcuts are the most stable way to operate CapCut: they don't care about layout, DPI or tree
coverage. They do care about **focus**. Most editing shortcuts act on the timeline only when the
timeline (not a text field or the inspector) has focus. Click an empty timeline area, or check
that the focus doesn't sit in an Edit control (`cc.py tree --root focused`), before sending them.

**Status:** everything below is `unverified` (commonly reported defaults). Capability 0 must open
CapCut's own shortcut list and correct this table. CapCut also lets users remap shortcuts, and
custom mappings live in `%LOCALAPPDATA%\CapCut\User Data\Config\keymapSettings`.

| Action | Reported default | Verified | Notes |
|---|---|---|---|
| Play / pause | Space | | |
| Split at playhead | Ctrl+B | | acts on selected clip(s) or the clip under the playhead (verify) |
| Delete left of playhead (trim start) | Q | | ripple behaviour depends on main-track magnet |
| Delete right of playhead (trim end) | W | | |
| Delete selected | Delete / Backspace | | |
| Undo | Ctrl+Z | | |
| Redo | Ctrl+Shift+Z | | some builds: Ctrl+Y |
| Copy / cut / paste | Ctrl+C / Ctrl+X / Ctrl+V | | |
| Select all | Ctrl+A | | |
| Import media | Ctrl+I | | opens a Windows file dialog |
| Export | Ctrl+E | | opens the export dialog |
| Previous / next frame | Left / Right | | |
| Previous / next edit point | Up / Down | | |
| Zoom timeline in / out | Ctrl+= / Ctrl+- | | |
| Fit timeline to window | Shift+Z | | |
| Add marker | M | | |
| Group / ungroup | Ctrl+G / Ctrl+Shift+G | | |
| Create compound clip | Alt+G | | |
| Separate audio | Ctrl+Shift+S | | |
| Freeze frame | Shift+F | | |
| Toggle snapping | N | | |
| Mark in / out | I / O | | |
| Fullscreen player | Ctrl+Shift+F | | |

## How to verify a shortcut (during any rung)

1. Take a `cc.py evidence` snapshot, or at least a screenshot, before sending the shortcut.
2. Send `cc.py key <combo>` with the right focus.
3. Confirm the effect with a screenshot and, for edits, `draft_inspect.py diff`.
4. Mark the row `agent-verified` with the date and CapCut version.
