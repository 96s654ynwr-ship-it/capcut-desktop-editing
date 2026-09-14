# Running this skill from Claude Code (Windows)

Claude Code on Windows has no built-in desktop computer-use tool. The browser tools (Claude in
Chrome, the in-app Browser pane) cannot see native apps. Everything goes through this skill's
scripts.

## Paths

- **Skill folder:** `C:\Users\<you>\.agents\skills\capcut-desktop-editing` (canonical).
  `~/.claude/skills/capcut-desktop-editing` is a directory junction to it, so write-backs land in
  the same place Codex reads.
- **Python:** `<skill>\scripts\.venv\Scripts\python.exe`

## Running commands

Prefer the **PowerShell tool** (native Windows quoting, handles Unicode/Arabic names):

```powershell
$S = "$env:USERPROFILE\.agents\skills\capcut-desktop-editing"
& "$S\scripts\.venv\Scripts\python.exe" "$S\scripts\cc.py" tree --filter interactive
```

The PowerShell tool doesn't keep variables between calls, so repeat `$S = ...` on each call or use
full paths. From the **Bash tool** (Git Bash), use forward slashes:
`"$USERPROFILE/.agents/skills/capcut-desktop-editing/scripts/.venv/Scripts/python.exe" .../cc.py ...`

## Seeing the screen

- `cc.py screenshot ...` prints the PNG path. **Open it with the Read tool** to look at it.
- Use `--scale 0.5` for overviews and `--region` crops for detail. Every image costs context.

## Working rhythm in Claude Code

- **Before the first input batch,** tell the user: "I'm about to drive CapCut; please don't use
  the mouse or keyboard until I report back."
- **The Claude desktop app window is also on the desktop, and it can come back to the foreground
  on its own mid-batch.** This was observed on 2026-09-14: a hit-test sweep sampled the Claude
  window instead of CapCut. Because of this:
  - `cc.py` refocuses CapCut before every input command and screenshot.
  - Screenshot results report `foreground_ok`. If it's `false`, discard the image and retry.
  - For your own ad-hoc UIA scripts, check `GetForegroundWindow()` and the element's `ProcessId`
    before trusting a result.
  - Never send keys without CapCut confirmed in front.
- **Keep each tool call to one small batch.** You can chain several `cc.py` calls in one
  PowerShell command, separated by `;`, when you don't need to look in between. Look again before
  the next batch.
- **Long AI jobs:** use `cc.py wait-for ... --timeout 600` in one call rather than polling
  repeatedly.
- **Name PowerShell helper functions Verb-Noun** (for example `Show-DraftDiff` or
  `Wait-DraftSave`), never short words. On 2026-09-14 a helper called `Diff` silently ran the
  built-in `diff` alias (`Compare-Object`) instead, and the verification step failed. Aliases take
  precedence over functions.
- **Permission prompts:** if the user wants fewer prompts, suggest allowlisting the venv python
  command in their Claude Code settings. Don't change settings yourself.

## Writing back

- Edit the reference files with the Edit/Write tools.
- **Commit after approval only,** from the skill folder:
  `git -C "$env:USERPROFILE\.agents\skills\capcut-desktop-editing" add -A` then `commit`.
- Follow the session's commit attribution rules.
