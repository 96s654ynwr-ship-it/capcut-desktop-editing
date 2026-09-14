#!/usr/bin/env python3
"""tooltip_sheet.py - hover a row of icon buttons and stitch their tooltips into one image.

CapCut's icon buttons are invisible to UI Automation, so tooltips are the way to name them.
Moves the mouse only (no clicks). Coordinates are physical screen pixels (read them off
`cc.py screenshot --grid`).

  tooltip_sheet.py --y 623 --xs 258 305 347 393 [--below 110] [--above 20] [--half-width 170] [--out sheet.png]
"""
import argparse
import datetime as dt
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cc  # noqa: E402  (sets DPI awareness on import)
from PIL import Image, ImageDraw, ImageFont  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--y", type=int, required=True, help="screen y of the icon row")
    ap.add_argument("--xs", type=int, nargs="+", required=True, help="screen x of each icon")
    ap.add_argument("--above", type=int, default=30, help="px captured above the row")
    ap.add_argument("--below", type=int, default=110, help="px captured below the row (tooltips usually appear below)")
    ap.add_argument("--half-width", type=int, default=170)
    ap.add_argument("--delay", type=float, default=1.3, help="seconds to wait for each tooltip")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--out")
    a = ap.parse_args()

    w = cc.main_window()
    cc.focus_window(w)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except Exception:
        font = ImageFont.load_default()
    tw, th = a.half_width * 2, a.above + a.below
    tiles = []
    for x in a.xs:
        if cc.user32.GetForegroundWindow() not in {c["hwnd"] for c in cc.capcut_windows()}:
            cc.focus_window(w)
        cc.move_to(x, a.y + a.below + 40)  # move away first so each tooltip re-triggers
        time.sleep(0.25)
        cc.move_to(x, a.y)
        time.sleep(a.delay)
        left = max(0, x - a.half_width)
        img, real = cc.grab([left, max(0, a.y - a.above), left + tw, a.y + a.below])
        tile = Image.new("RGB", (tw, th + 24), (20, 20, 20))
        tile.paste(img, (0, 24))
        d = ImageDraw.Draw(tile)
        d.text((4, 3), f"x={x} y={a.y}", fill=(255, 255, 0), font=font)
        d.line([(x - real[0], 24), (x - real[0], th + 24)], fill=(255, 0, 255), width=1)
        tiles.append(tile)
    cc.move_to(w["rect"][0] + 20, w["rect"][3] - 20)

    rows = (len(tiles) + a.cols - 1) // a.cols
    sheet = Image.new("RGB", (a.cols * (tw + 4), rows * (th + 28)), (0, 0, 0))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % a.cols) * (tw + 4), (i // a.cols) * (th + 28)))
    out = Path(a.out) if a.out else cc.EVIDENCE_DIR / "shots" / dt.date.today().isoformat() / (
        dt.datetime.now().strftime("%H%M%S") + ".tooltips.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    cc.out(dict(path=str(out), icons=len(a.xs), size=list(sheet.size)))


if __name__ == "__main__":
    main()
