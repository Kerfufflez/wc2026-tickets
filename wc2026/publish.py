"""Publish dashboard to docs/ for GitHub Pages."""

from __future__ import annotations

import json
import re
import shutil
from datetime import date

from wc2026.config import (
    DEAL_LOG_JS,
    DOCS,
    DOCS_ARCHIVE,
    DOCS_DEAL_LOG,
    DOCS_HISTORY,
    DOCS_MANIFEST,
    REFRESH_JS,
    REPORT_DEAL_LOG_HTML,
    REPORT_HTML,
)
from wc2026.dates import format_est_short, now_est
from wc2026.tracker import snapshot_dates_manifest

CONTEXT_RE = re.compile(
    r'<meta name="snapshot-context" content="[^"]*">'
)
SELECT_RE = re.compile(
    r'(<select id="snapshot-picker"[^>]*>)(.*?)(</select>)',
    re.DOTALL,
)
LAST_UPDATED_RE = re.compile(
    r'(<p class="last-updated" id="last-updated"[^>]*>Last updated: <strong>)[^<]+(</strong></p>)'
)


def build_options(dates: list[dict], current: str | None, latest_label: str) -> str:
    latest_sel = " selected" if current is None else ""
    lines = [f'<option value=""{latest_sel}>{latest_label}</option>']
    for item in dates:
        d = item["date"]
        sel = " selected" if current == d else ""
        label = item.get("label", d)
        lines.append(f'<option value="{d}"{sel}>{label}</option>')
    return "\n          ".join(lines)


def set_snapshot_context(html: str, context: str) -> str:
    tag = f'<meta name="snapshot-context" content="{context}">'
    if CONTEXT_RE.search(html):
        return CONTEXT_RE.sub(tag, html, count=1)
    return html.replace("</head>", f"  {tag}\n</head>", 1)


def inject_dropdown(
    html: str, dates: list[dict], current: str | None, latest_label: str
) -> str:
    options = build_options(dates, current, latest_label)
    inner = f"\n          {options}\n        "
    if not SELECT_RE.search(html):
        raise RuntimeError("Snapshot dropdown <select> missing from HTML template")
    return SELECT_RE.sub(rf"\g<1>{inner}\g<3>", html, count=1)


def list_archive_dates() -> list[str]:
    if not DOCS_ARCHIVE.exists():
        return []
    return sorted(
        (p.stem for p in DOCS_ARCHIVE.glob("*.html")),
        reverse=True,
    )


def latest_option_label(html: str) -> str:
    m = LAST_UPDATED_RE.search(html)
    if m:
        inner = html[m.start() : m.end()]
        strong = re.search(r"<strong>([^<]+)</strong>", inner)
        if strong:
            return f"Latest · {strong.group(1)}"
    return f"Latest · {format_est_short(now_est())}"


def publish_docs() -> None:
    if not REPORT_HTML.exists():
        raise FileNotFoundError(f"Missing built report: {REPORT_HTML}")

    today = date.today().isoformat()
    DOCS_ARCHIVE.mkdir(parents=True, exist_ok=True)
    DOCS_HISTORY.mkdir(parents=True, exist_ok=True)

    base_html = REPORT_HTML.read_text(encoding="utf-8")
    archive_path = DOCS_ARCHIVE / f"{today}.html"
    archive_path.write_text(base_html, encoding="utf-8")

    manifest_dates = snapshot_dates_manifest()
    DOCS_MANIFEST.write_text(
        json.dumps({"dates": manifest_dates}, indent=2) + "\n",
        encoding="utf-8",
    )

    dates_for_dropdown = manifest_dates
    latest_label = latest_option_label(base_html)

    if REFRESH_JS.exists():
        shutil.copy2(REFRESH_JS, DOCS / "refresh.js")

    if REPORT_DEAL_LOG_HTML.exists():
        published_log = REPORT_DEAL_LOG_HTML.read_text(encoding="utf-8")
        published_log = published_log.replace(
            'href="../dashboard.html"', 'href="../index.html"'
        )
        DOCS_DEAL_LOG.write_text(published_log, encoding="utf-8")
        if DEAL_LOG_JS.exists():
            shutil.copy2(DEAL_LOG_JS, DOCS_HISTORY / "deal_log.js")

    index_html = inject_dropdown(
        set_snapshot_context(base_html, "index"),
        dates_for_dropdown,
        current=None,
        latest_label=latest_label,
    )
    index_html = index_html.replace(
        'href="history/DEAL_LOG.md"', 'href="history/deal-log.html"'
    )
    (DOCS / "index.html").write_text(index_html, encoding="utf-8")

    archive_dates = list_archive_dates()
    for d in archive_dates:
        path = DOCS_ARCHIVE / f"{d}.html"
        raw = base_html if d == today else path.read_text(encoding="utf-8")
        published = inject_dropdown(
            set_snapshot_context(raw, "archive"),
            dates_for_dropdown,
            current=d,
            latest_label=latest_label,
        )
        published = published.replace(
            'href="history/DEAL_LOG.md"', 'href="../history/deal-log.html"'
        )
        published = published.replace('src="refresh.js"', 'src="../refresh.js"')
        path.write_text(published, encoding="utf-8")

    print("Published docs/index.html")
    print(f"Published docs/archive/{today}.html")
    if REPORT_DEAL_LOG_HTML.exists():
        print("Published docs/history/deal-log.html")
    print(
        f"Archive dates: {', '.join(archive_dates) if archive_dates else '(none)'}"
    )


def main() -> int:
    publish_docs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
