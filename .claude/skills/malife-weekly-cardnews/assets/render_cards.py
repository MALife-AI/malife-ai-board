"""
malife-weekly-cardnews — Card Renderer

각 카드 HTML 파일을 1080x1350 PNG로 렌더한다.
Chrome headless 사용. macOS 기본 경로 가정.

Usage:
    python3 render_cards.py <html_dir> <png_dir>
"""
import sys
import subprocess
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render_png(html_path: Path, out_png: Path, width: int = 1080, height: int = 1350):
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--default-background-color=00000000",
        f"--window-size={width},{height}",
        f"--screenshot={out_png}",
        "--virtual-time-budget=4000",
        f"file://{html_path}",
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 render_cards.py <html_dir> <png_dir>")
        sys.exit(1)

    html_dir = Path(sys.argv[1]).resolve()
    png_dir = Path(sys.argv[2]).resolve()
    png_dir.mkdir(parents=True, exist_ok=True)

    html_files = sorted(html_dir.glob("*.html"))
    if not html_files:
        print(f"No HTML files in {html_dir}")
        sys.exit(1)

    for f in html_files:
        out = png_dir / f"{f.stem}.png"
        render_png(f, out)
        print(f"  ✓ {out.name}")


if __name__ == "__main__":
    main()
