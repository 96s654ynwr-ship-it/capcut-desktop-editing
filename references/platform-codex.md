# Running this skill from Codex (Windows)

## Discovery and invocation

The canonical repository is `%USERPROFILE%\.agents\skills\capcut-desktop-editing`.
Codex already discovers this user-scope skill. `agents/openai.yaml` enables implicit invocation;
the user can also request `$capcut-desktop-editing` explicitly. Claude Code's junction points to
this same repository. Do not install a second copy or replace that junction.

Use this skill for edits in the native CapCut desktop app. The CapCut cloud plugin and
code-rendered video workflows are separate backends and do not replace a desktop-edit request.

## Verified machine setup (2026-09-16)

- Windows 10 Pro, build 19045; CapCut 9.4.0.4015 at
  `D:\Bytedance\CapCut\Apps\9.4.0.4015\CapCut.exe`.
- Private Python 3.12 environment at `scripts\.venv\Scripts\python.exe`; imports of
  `uiautomation`, `comtypes`, `mss`, and `PIL` passed. `uv` is on PATH.
- Bundled `cc.py windows` and grid screenshot capture passed outside the sandbox; CapCut's
  home window was visually verified at 125% DPI. No project was opened or edited for this check.
- Native Codex Computer Use (`node_repl` + `@oai/sky`) listed and launched CapCut, but
  `get_window_state` failed twice, including after refreshing the main window:
  `SetIsBorderRequired failed: No such interface supported (0x80004002)`.
  Do not assume native capture works just because the package imports or the app is listed.

Use the bundled-script backend on this machine while that capture failure persists. If the OS
or Computer Use runtime changes, read the available `computer-use:computer-use` skill and its
guidance, then perform a read-only capability check. If native capture works, follow that
backend's current window-selection and observe/action/refresh rules. Native window-relative
coordinates and screenshot IDs are not interchangeable with `cc.py` physical screen coordinates.
Use one input backend for an editing session; keep `draft_inspect.py` for read-only verification.

## Bundled-script backend

Resolve the skill path from its loaded location. In PowerShell:

```powershell
$skillPath = "$env:USERPROFILE\.agents\skills\capcut-desktop-editing"
$capcutPython = Join-Path $skillPath 'scripts\.venv\Scripts\python.exe'
& $capcutPython -B "$skillPath\scripts\cc.py" version
& $capcutPython -B "$skillPath\scripts\cc.py" windows
& $capcutPython -B "$skillPath\scripts\cc.py" screenshot --grid --scale 0.6 --out '<workspace>\work\capcut.png'
```

Replace `<workspace>` with the current task's absolute workspace path. View the returned PNG
with `view_image`. Grid labels already express physical screen coordinates; use the returned
mapping when interpreting a scaled image. Focus and verify the intended CapCut window before
input; stop if focus cannot be confirmed.

Use `draft_inspect.py` to inspect projects and compare before/after summaries. It must never
write CapCut project files. Keep temporary screenshots and summaries in the task's `work/`
folder; preserve lasting capability evidence under the skill's ignored `evidence/` directory.

The existing environment is ready; rerun `scripts/setup.ps1` only if the environment is missing
or required imports fail. Setup requires write access to the skill folder and may need network.

## Sandbox and access

The Windows sandbox can run as a different identity. In this setup it returned an empty CapCut
installation and no windows, while the same read-only checks outside the sandbox found CapCut.
Do not treat empty registry/window/project results as proof that the app or projects are missing.
An empty UIA tree can also be CapCut's limited accessibility coverage; do not assume it always
means a sandbox failure.

Use the shell tool's `sandbox_permissions: "require_escalated"` with a narrowly scoped
justification when the task needs interactive desktop access, the user's CapCut project data,
or writes to this skill outside the workspace. Follow the tool's approval result; do not change
global access settings or repeatedly ask for authorization already supplied by the user.

Git may report dubious ownership under the sandbox identity. Prefer running the scoped git
command as the owning user. Do not add wildcard/global safe-directory exceptions or rewrite
unrelated Git configuration.

## Editing rhythm and write-back

- Read the ladder and house style. Reuse approved procedures for production edits; apply the
  learning/approval loop to new procedures. The recorded ladder has rungs 0-17 approved.
- Tell the user before input starts that the mouse and keyboard will be in use, and report when
  finished. Use small action batches, inspect the result, and stop on unexpected dialogs.
- Poll long processing jobs in bounded intervals of at most 60 seconds so progress updates and
  user steering remain possible. Refresh state before any subsequent input.
- Keep existing authorization and the skill's project-safety rules. Never infer authorization
  for a new credit-spending operation from historical practice-session approvals.
- Write reusable findings to the shared repository. Preserve unrelated edits; stage only files
  belonging to the approved capability, and commit capability changes after user approval.
