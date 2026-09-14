# Capability NN — <Title>

> Copy this template to `references/capabilities/NN-<slug>.md`. Replace every placeholder. Delete
> any section that truly doesn't apply, but never delete Failure modes. Write it so an agent with
> no memory of your session can repeat it exactly.

## Status
- **Ladder status:** not-started | in-progress | demonstrated | approved
- **CapCut version:** 9.4.0.4015 (from `cc.py version`)
- **Demonstrated:** YYYY-MM-DD by <agent: Claude Code / Codex>
- **Approved:** YYYY-MM-DD, "<user's words>"
- **Practice project:** `<copy name>` (duplicate of `<original>`)
- **Evidence:** `evidence/YYYY-MM-DD/HHMMSS-NN-.../`

## Goal
One or two sentences: the editorial intent and what the result looks like.

## Preconditions
- Rungs this depends on (must be `approved`).
- The required CapCut state: which screen, which panel open, what's selected, playhead position.
- The required media/footage characteristics.

## Native route (overview)
The route a CapCut editor would take, in one line. Example: *Timeline toolbar → Split (Ctrl+B)
with the playhead on the cut point.*

## Procedure
Each step has an action, how to identify the control, and what to observe afterwards.

1. **Action:** …
   **Control:** `cc.py act invoke --type Button --name "…"` *(tree)* | `key ctrl+b` *(shortcut)* |
   landmark "…" → `screenshot --grid` then `click` *(canvas)*
   **Expect:** … (tree node appears or changes state / visual change / timecode)
2. …

## Wait conditions
Async work (AI processing, transcription, export): what indicates progress, what indicates it's
done, typical duration seen, and the timeout you used.

## Verification
- **Visual:** which screenshot regions to check and what they must show.
- **Draft diff:** the exact expected changes (segments added/removed/retimed, materials added,
  keyframes) and "nothing else changed".
- **Playback or export spot-check** if relevant.

## Parameters
| Parameter | Value used | Universal or shot-specific | How to judge it |
|---|---|---|---|

## Undo / recovery
How to revert (Ctrl+Z count, panel reset buttons) and how you confirmed the revert.

## Failure modes seen
| Symptom | Cause | Recovery |
|---|---|---|

## Tree coverage notes
Controls in this procedure that were **not** exposed to UI Automation and needed screenshots.
Also note anything that became exposed only after hovering or focusing.

## Open questions for the user
