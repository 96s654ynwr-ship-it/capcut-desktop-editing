# CapCut Desktop Editing (agent skill)

A skill that teaches an agent to edit video in the **real CapCut desktop app on Windows**. The
agent drives the application the way a person does instead of generating video from code. It's
modelled on [astra-premiere-editing](https://github.com/per-simmons/astra-premiere-editing),
rebuilt for CapCut, Windows, Claude Code and Codex.

## How it works

- **Control.** The agent reads the Windows UI Automation tree of CapCut (a Qt 6 app) for named
  controls. It uses keyboard shortcuts where they exist, and falls back to screenshots with a
  labelled coordinate grid for custom-drawn surfaces such as the timeline and the player.
- **Verification.** Every edit is checked visually and against a read-only diff of CapCut's
  project JSON. The skill never edits project files.
- **Capability ladder.** Each capability is worked out natively, executed on real footage,
  verified, and written back into `references/capabilities/`. Nothing advances until the user
  approves the current capability. Status lives in `references/capability-ladder.md`.

## Install

```powershell
# canonical location (Codex user scope)
git clone <this repo> "$env:USERPROFILE\.agents\skills\capcut-desktop-editing"
# Claude Code sees the same folder through a junction
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\capcut-desktop-editing" -Target "$env:USERPROFILE\.agents\skills\capcut-desktop-editing"
# private Python venv (needs uv)
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.agents\skills\capcut-desktop-editing\scripts\setup.ps1"
```

Then open CapCut and ask your agent to continue the CapCut capability ladder.

## Requirements

- Windows 10/11
- CapCut desktop (mapped against 9.4.0.4015)
- [uv](https://docs.astral.sh/uv/)
- Claude Code or Codex. For Codex, desktop input may need approval to run outside its sandbox.

## Adapting it

The procedures record one editor's taste. To adapt them, run the same loop that built them:
describe the edit you want, let the agent reproduce it in CapCut, approve it, and the agent writes
the procedure back.
