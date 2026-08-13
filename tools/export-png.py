"""Re-export every logo SVG to PNG.

The SVGs are the source of truth; these exports exist for places that
cannot take vector art. Run after changing anything in logo/.

    python tools/export-png.py

Needs playwright with Chrome available:
    pip install playwright && playwright install chrome
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "logo/png"

# asset -> widths to emit
JOBS = {
    "mark": [1024, 512, 256, 128, 64, 32, 16],
    "mark-mono": [1024, 512, 256, 64],
    "wordmark": [1600, 800, 400],
    "lockup-horizontal": [2048, 1024, 512],
    "lockup-stacked": [1600, 800, 400],
}
# currentColor cannot travel in a PNG, so each asset ships in both inks
VARIANTS = {"": "#12141c", "-on-dark": "#f4f5f9"}


def main() -> int:
    from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for name, widths in JOBS.items():
            svg = (ROOT / f"logo/{name}.svg").read_text()
            box = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
            if not box:
                raise SystemExit(f"{name}.svg has no viewBox")
            vw, vh = float(box.group(1)), float(box.group(2))
            for suffix, ink in VARIANTS.items():
                for w in widths:
                    h = max(1, round(w * vh / vw))
                    page = browser.new_page(viewport={"width": w, "height": h})
                    sized = svg.replace("<svg", f"<svg width={w} height={h}", 1)
                    page.set_content(
                        f'<body style="margin:0;color:{ink}">'
                        f'<div style="width:{w}px;height:{h}px">{sized}</div></body>'
                    )
                    page.wait_for_timeout(60)
                    page.screenshot(path=str(OUT / f"{name}-{w}{suffix}.png"),
                                    omit_background=True)
                    page.close()
                    count += 1
        browser.close()
    print(f"{count} PNGs written to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
