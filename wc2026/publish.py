"""Publish dashboard to docs/ for GitHub Pages."""

from __future__ import annotations

import json
import re
import shutil
from datetime import date, datetime

from wc2026.config import (
    DOCS,
    DOCS_ARCHIVE,
    DOCS_HISTORY,
    DOCS_MANIFEST,
    REFRESH_JS,
    REPORT_DEAL_LOG,
    REPORT_HTML,
)

CONTEXT_RE = re.compile(
    r'<meta name="snapshot-context" content="[^"]*">'
)
SELECT_RE = re.compile(
    r'(<select id="snapshot-picker"[^>]*>)(.*?)(</select>)',
    re.DOTALL,
)


def format_date_label(iso_date: str) -> str:
    d = datetime.strptime(iso_date, "%Y-%m-%d")
    return d.strftime("%b %-d, %Y")


def build_options(dates: list[str], current: str | None) -> str:
    latest_sel = " selected" if current is None else ""
    lines = [f'<option value=""{latest_sel}>Latest</option>']
    for d in dates:
        sel = " selected" if current == d else ""
        lines.append(f'<option value="{d}"{sel}>{format_date_label(d)}</option>')
    return "\n          ".join(lines)


def set_snapshot_context(html: str, context: str) -> str:
    tag = f'<meta name="snapshot-context" content="{context}">'
    if CONTEXT_RE.search(html):
        return CONTEXT_RE.sub(tag, html, count=1)
    return html.replace("</head>", f"  {tag}\n</head>", 1)


def inject_dropdown(html: str, dates: list[str], current: str | None) -> str:
    options = build_options(dates, current)
    inner = f"\n          {options}\n        "
    if not SELECT_RE.search(html):
        raise RuntimeError("Snapshot dropdown <select> missing from HTML template")
    return SELECT_RE.sub(rf"\g<1>{inner}\g<3>", html, count=1)


def list_archive_dates() -> list[str]:
    if not DOCS_ARCHIVE.exists():
        return []
    dates = sorted(
        (p.stem for p in DOCS_ARCHIVE.glob("*.html")),
        reverse=True,
    )
    return dates


def publish_docs() -> None:
    if not REPORT_HTML.exists():
        raise FileNotFoundError(f"Missing built report: {REPORT_HTML}")

    today = date.today().isoformat()
    DOCS_ARCHIVE.mkdir(parents=True, exist_ok=True)
    DOCS_HISTORY.mkdir(parents=True, exist_ok=True)

    base_html = REPORT_HTML.read_text(encoding="utf-8")
    archive_path = DOCS_ARCHIVE / f"{today}.html"
    archive_path.write_text(base_html, encoding="utf-8")

    dates = list_archive_dates()
    DOCS_MANIFEST.write_text(json.dumps(dates, indent=2) + "\n", encoding="utf-8")

    if REPORT_DEAL_LOG.exists():
        shutil.copy2(REPORT_DEAL_LOG, DOCS_HISTORY / "DEAL_LOG.md")

    if REFRESH_JS.exists():
        shutil.copy2(REFRESH_JS, DOCS / "refresh.js")

    index_html = inject_dropdown(
        set_snapshot_context(base_html, "index"), dates, current=None
    )
    (DOCS / "index.html").write_text(index_html, encoding="utf-8")

    for d in dates:
        path = DOCS_ARCHIVE / f"{d}.html"
        raw = base_html if d == today else path.read_text(encoding="utf-8")
        published = inject_dropdown(
            set_snapshot_context(raw, "archive"), dates, current=d
        )
        published = published.replace(
            'href="history/DEAL_LOG.md"', 'href="../history/DEAL_LOG.md"'
        )
        published = published.replace('src="refresh.js"', 'src="../refresh.js"')
        path.write_text(published, encoding="utf-8")

    print("Published docs/index.html")
    print(f"Published docs/archive/{today}.html")
    print(f"Archive dates: {', '.join(dates) if dates else '(none)'}")


def main() -> int:
    publish_docs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
