# Running this skill from Codex (Windows)

## Discovery

Codex loads user-scope skills from `~/.agents/skills/`. This skill lives there as
`capcut-desktop-editing`. `agents/openai.yaml` sets its display name and allows implicit
invocation.

## Two ways to see and act

1. **Codex native computer use** (Codex app on **Windows 11**, recent builds). If your tool list
   includes native computer use:
   - use it for screenshots, clicks and typing
   - still use `cc.py tree/find` for control names and states, and `draft_inspect.py` for
     verification

   The native tool takes over the foreground, so the user must leave the desktop alone.
2. **Bundled scripts** (the only option on Windows 10, and always valid). Run `cc.py` from your
   PowerShell shell and view screenshots with your image viewing tool (e.g. `view_image` on the
   PNG path printed by `cc.py screenshot`).

The machine this skill was built on runs **Windows 10 Pro**, so use option 2 there.

## Sandbox and approvals (important)

Codex's Windows sandbox runs commands with restricted tokens. UI Automation queries and
`SendInput` into another desktop process may be **blocked or silently empty** inside the sandbox.

- **If `cc.py tree` returns 0 nodes while CapCut is visibly open,** or input commands report
  `SendInput blocked`, the sandbox is the cause.
- Ask the user to approve running these commands outside the sandbox, or to run the session with
  full access, for the CapCut work.
- Record in `accessibility-controls.md` → Method notes which mode worked.

## Running commands

```powershell
$S = "$env:USERPROFILE\.agents\skills\capcut-desktop-editing"
& "$S\scripts\.venv\Scripts\python.exe" "$S\scripts\cc.py" windows
```

Setup (once): `powershell -ExecutionPolicy Bypass -File "$S\scripts\setup.ps1"`. It needs network
access to install packages, which may require approval.

## Working rhythm in Codex

- **Warn the user before input batches.** If they're steering from the ChatGPT mobile app, say
  when you're done so they can use the PC again.
- **Keep batches small** and look again after each one (the same loop as SKILL.md).
- **Long AI jobs:** one `cc.py wait-for ... --timeout 600` call.

## Writing back

- Apply patches to the reference files in the skill folder.
- **Commit after approval only** (`git -C $S add -A; git -C $S commit -m "..."`).
- Claude Code reads the same folder through a junction, so both agents stay in sync.
