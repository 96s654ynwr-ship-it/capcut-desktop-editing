#!/usr/bin/env python3
"""tighten_gaps.py - tighten silences between spoken words in the CapCut project that is OPEN in the editor.

Native CapCut editing only (splits, W, undo), driven through cc.py; the draft JSON is only read to verify.

Prerequisite: the project has Auto captions (they carry per-word timings). Auto captions are a Pro feature
that may use credits - generate them only with the user's consent (Captions tab > Auto captions > Generate).

  tighten_gaps.py --project "0914 (4)" --dry-run
  tighten_gaps.py --project "0914 (4)" --count 5 --min 0.6 --keep 0.125 --undo-captions
  tighten_gaps.py --project "0914 (4)" --all --min 1.0 --keep 0.2 --undo-captions

Per gap (latest first, so earlier timecodes never shift):
  1. exact split at the gap end        (measuring split -> read draft -> undo -> arrow-correct -> repeat)
  2. exact playhead at the gap start   (same measuring loop, no split left behind)
  3. select that clip, press W         (delete right of playhead; ripples with the main-track magnet on)
  4. verify: duration dropped by exactly the gap, next segment resumes at the gap-end source frame
Anything unexpected aborts (Ctrl+Z undoes the last completed cut step by step).

Geometry defaults were measured with CapCut maximized at 1920x1030 physical px (125% scale), timeline
zoom-to-fit (Shift+Z). The measuring loop only needs ruler clicks inside the right clip, so small
geometry errors are corrected automatically; re-measure with a grid screenshot on other layouts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cc  # noqa: E402  (per-monitor DPI aware)
import draft_inspect as di  # noqa: E402

A = None          # parsed args
PROJ = None       # project folder
DRAFT = None      # draft_content.json
FRAME = 1 / 30.0
LOG: list[str] = []
LOG_PATH = None


def say(*parts):
    msg = " ".join(str(p) for p in parts)
    print(msg, flush=True)
    LOG.append(msg)


def finish(code, msg=None):
    if msg:
        say(("ABORT: " if code else "") + msg)
    if LOG_PATH:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOG_PATH.write_text(json.dumps(LOG, ensure_ascii=False, indent=1), encoding="utf-8")
    sys.exit(code)


def abort(msg):
    finish(2, msg)


# ----------------------------------------------------------------------------- CapCut I/O

def ensure_fg():
    for _ in range(4):
        if cc.user32.GetForegroundWindow() in {c["hwnd"] for c in cc.capcut_windows()}:
            return
        cc.focus_window(cc.main_window())
        time.sleep(0.4)
    abort("cannot bring CapCut to the foreground")


def is_editor():
    auto = cc.uia()
    ctrl = auto.ControlFromHandle(cc.main_window()["hwnd"])
    return (ctrl.AutomationId or "") == "MainWindow"


def key(combo, n=1):
    ensure_fg()
    for _ in range(n):
        cc.press_combo(combo)
        time.sleep(0.04)
    time.sleep(0.3)


def click(x, y):
    ensure_fg()
    cc.click_at(int(round(x)), int(round(y)))
    time.sleep(0.5)


def mtime():
    return DRAFT.stat().st_mtime


def wait_save(prev, timeout):
    end = time.time() + timeout
    while time.time() < end:
        time.sleep(0.7)
        if mtime() > prev:
            time.sleep(0.6)
            return True
    return False


def state():
    for _ in range(10):
        try:
            s = di.summarize(PROJ)
            vids = [t for t in s["tracks"] if t["type"] == "video"]
            if not vids:
                abort("project has no video track")
            return s, vids[0]["segments"]
        except (json.JSONDecodeError, UnicodeDecodeError):
            time.sleep(0.5)
    abort("could not read the draft")


def has_text_track(s):
    return any(t["type"] == "text" and t["segments"] for t in s["tracks"])


def bounds(sl):
    return sorted(g["start"] / 1e6 for g in sl)


def seg_key(sl):
    return [(g["start"], g["duration"], g["src_start"]) for g in sl]


# ----------------------------------------------------------------------------- timeline geometry

def fit():
    click(*A.empty)
    key("shift+z")
    time.sleep(1.0)


def x_of(t, dur):
    return A.fit_x0 + 2 + t * A.fit_span / dur


def segment_at(t, sl):
    for g in sl:
        s0, s1 = g["start"] / 1e6, (g["start"] + g["duration"]) / 1e6
        if s0 - 1e-6 <= t < s1 - 1e-6:
            return g, s0, s1
    abort(f"no segment contains {t:.3f}s")


def select_segment(t, sl, dur):
    _, s0, s1 = segment_at(t, sl)
    lo, hi = s0 + 1.5, s1 - 1.5
    cands = [c for c in ((s0 + s1) / 2, lo, hi) if lo <= c <= hi] or [(s0 + s1) / 2]
    click(x_of(max(cands, key=lambda c: abs(c - t)), dur), A.clip_y)


# ----------------------------------------------------------------------------- exact placement and cuts

def place_exact(t):
    """Leave the playhead exactly on time t with no split left behind."""
    s, sl = state()
    dur = s["duration"] / 1e6
    before = seg_key(sl)
    fit()
    near = [b for b in bounds(sl) if b > 0 and abs(b - t) < A.snap_avoid]
    tc = t
    if near:  # ruler clicks snap to nearby cuts - click well away and let the arrows walk back
        b = near[0]
        tc = b - A.snap_avoid if t < b else b + A.snap_avoid
        _, s0, s1 = segment_at(t, sl)
        tc = min(max(tc, s0 + 0.5), s1 - 0.5)
    click(x_of(tc, dur), A.ruler_y)
    for attempt in range(6):
        select_segment(t, sl, dur)
        prev = mtime()
        key("ctrl+b")
        if not wait_save(prev, A.save_timeout):
            abort(f"no draft save after a measuring split - is '{PROJ.name}' the project open in the editor?")
        _, sl2 = state()
        new = sorted(set(bounds(sl2)) - set(bounds(sl)))
        if len(new) != 1:
            abort(f"measuring split produced {len(new)} new boundaries")
        landed = new[0]
        delta = round((t - landed) / FRAME)
        say(f"    measure#{attempt}: target {t:.3f} landed {landed:.3f} -> delta {delta} frames")
        prev = mtime()
        key("ctrl+z")
        if not wait_save(prev, A.save_timeout):
            abort("no draft save after undoing a measuring split")
        _, sl3 = state()
        if seg_key(sl3) != before:
            abort("undo of the measuring split did not restore the segments")
        if delta == 0:
            return
        key("right" if delta > 0 else "left", abs(delta))
    abort(f"playhead did not converge on {t:.3f}s")


def split_exact(t):
    place_exact(t)
    s, sl = state()
    select_segment(t, sl, s["duration"] / 1e6)
    prev = mtime()
    key("ctrl+b")
    if not wait_save(prev, A.save_timeout):
        abort("no draft save after split")
    _, sl2 = state()
    if not any(abs(b - t) <= FRAME / 2 for b in bounds(sl2)):
        abort(f"split not at {t:.3f}s")
    say(f"  split verified at {t:.3f}")


def remove_range(a, b):
    say(f"== remove {a:.3f} -> {b:.3f} ({b - a:.3f}s)")
    split_exact(b)
    s, sl = state()
    dur_before = s["duration"] / 1e6
    src_at_b = next(g for g in sl if abs(g["start"] / 1e6 - b) <= FRAME / 2)["src_start"] / 1e6
    _, s0, s1 = segment_at(a, sl)
    if abs(s1 - b) > FRAME / 2:
        abort(f"clip containing {a:.3f}s ends at {s1:.3f}s, expected {b:.3f}s")
    place_exact(a)
    s, sl = state()
    select_segment(a, sl, s["duration"] / 1e6)
    prev = mtime()
    key("w")
    if not wait_save(prev, A.save_timeout):
        abort("no draft save after W")
    s2, sl2 = state()
    dur_after = s2["duration"] / 1e6
    nxt = [x for x in sl2 if abs(x["start"] / 1e6 - a) <= FRAME / 2]
    ok_dur = abs((dur_before - dur_after) - (b - a)) <= FRAME
    ok_join = bool(nxt) and abs(nxt[0]["src_start"] / 1e6 - src_at_b) <= FRAME / 2
    resumed = f"{nxt[0]['src_start'] / 1e6:.3f}" if nxt else "none"
    say(f"  W: duration {dur_before:.3f} -> {dur_after:.3f} (expected -{b - a:.3f}) ok={ok_dur}; "
        f"join resumes src {resumed} (expected {src_at_b:.3f}) ok={ok_join}")
    if not (ok_dur and ok_join):
        abort("W did not remove exactly the range with ripple")


# ----------------------------------------------------------------------------- main

def compute_gaps():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "gaps.json"
        r = subprocess.run([sys.executable, str(HERE / "draft_inspect.py"), "gaps", str(PROJ),
                            "--min", str(A.min), "--keep", str(A.keep), "--json", str(out)],
                           cwd=tmp, capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0 or not out.exists():
            abort(f"draft_inspect gaps failed: {r.stderr.strip()[-400:]}")
        return json.loads(out.read_text(encoding="utf-8"))


def parse_args():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", required=True, help="CapCut project name or folder (must be open in the editor)")
    ap.add_argument("--min", type=float, default=0.6, help="only gaps at least this long (s)")
    ap.add_argument("--keep", type=float, default=0.125, help="silence kept after/before each word (s)")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--count", type=int, default=5, help="tighten the N longest gaps (default 5)")
    g.add_argument("--all", action="store_true", help="tighten every qualifying gap")
    ap.add_argument("--undo-captions", action="store_true",
                    help="first undo the Auto captions with one Ctrl+Z (they must be the last action)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan; send no input to CapCut")
    ap.add_argument("--fit-x0", type=float, default=230)
    ap.add_argument("--fit-span", type=float, default=1297)
    ap.add_argument("--ruler-y", type=int, default=628)
    ap.add_argument("--clip-y", type=int, default=830)
    ap.add_argument("--empty", type=lambda v: tuple(int(p) for p in v.split(",")), default=(1500, 760),
                    help="x,y of empty timeline space used to focus the timeline")
    ap.add_argument("--snap-avoid", type=float, default=4.5)
    ap.add_argument("--save-timeout", type=float, default=120)
    ap.add_argument("--log", help="log JSON path (default evidence/<date>/tighten_gaps/<project>-HHMMSS.json)")
    return ap.parse_args()


def main():
    global A, PROJ, DRAFT, FRAME, LOG_PATH
    A = parse_args()
    PROJ = di.resolve_project(A.project)
    DRAFT = PROJ / "draft_content.json"
    now = dt.datetime.now()
    LOG_PATH = Path(A.log) if A.log else (cc.EVIDENCE_DIR / now.date().isoformat() / "tighten_gaps"
                                          / f"{PROJ.name}-{now.strftime('%H%M%S')}.json")
    s, sl = state()
    FRAME = 1.0 / float(s.get("fps") or 30.0)
    if not has_text_track(s):
        abort("no Auto captions in this project - generate them first (Pro, may use credits: ask the user)")
    gaps = [g for g in compute_gaps() if not g["crosses_join"]]
    chosen = gaps if A.all else sorted(gaps, key=lambda g: g["remove"], reverse=True)[:A.count]
    chosen.sort(key=lambda g: g["cut_start"], reverse=True)
    total = sum(g["remove"] for g in chosen)
    dur0 = s["duration"] / 1e6
    say(f"project {PROJ.name}: {len(sl)} video segments, {dur0:.3f}s; {len(gaps)} real gaps >= {A.min}s")
    for g in chosen:
        say(f"  plan: {g['cut_start']:.3f} -> {g['cut_end']:.3f}  (-{g['remove']:.3f}s)  «{g['after']}» | «{g['before']}»")
    say(f"expected result: {dur0:.3f}s -> {dur0 - total:.3f}s (-{total:.3f}s)")
    if A.dry_run:
        finish(0, "dry run - no input sent")

    if not is_editor():
        abort("the CapCut editor is not open")
    if not A.undo_captions:
        abort("captions are still on the timeline; re-run with --undo-captions (or remove them yourself first)")
    before = seg_key(sl)
    click(*A.empty)
    prev = mtime()
    key("ctrl+z")
    if not wait_save(prev, A.save_timeout):
        abort(f"no draft save after Ctrl+Z - is '{PROJ.name}' the project open in the editor?")
    s, sl = state()
    if has_text_track(s) or seg_key(sl) != before:
        abort("Ctrl+Z did not cleanly remove only the captions (captions were not the last action?)")
    say("captions undone; video segments unchanged")

    for g in chosen:
        remove_range(g["cut_start"], g["cut_end"])
    s, sl = state()
    say(f"FINAL: {len(sl)} segments, {s['duration'] / 1e6:.3f}s")
    finish(0, None)


if __name__ == "__main__":
    main()
