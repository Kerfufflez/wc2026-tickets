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
from wc2026.dates import format_dropdown_label, label_from_last_updated, now_est

CONTEXT_RE = re.compile(
    r'<meta name="snapshot-context" content="[^"]*">'
)
SELECT_RE = re.compile(
    r'(<select id="snapshot-picker"[^>]*>)(.*?)(</select>)',
    re.DOTALL,
)
HEADER_ROW_RE = re.compile(
    r'<div class="header-row">.*?</div>\s*<hr class="divider">',
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
    inner = f"\n        {options}\n      "
    if not SELECT_RE.search(html):
        raise RuntimeError("Snapshot dropdown <select> missing from HTML template")
    return SELECT_RE.sub(rf"\g<1>{inner}\g<3>", html, count=1)


def render_header_row(
    last_updated: str, dates: list[dict], current: str | None, latest_label: str
) -> str:
    options = build_options(dates, current, latest_label)
    return f"""<div class="header-row">
    <p class="last-updated" id="last-updated" style="margin-bottom:0">Last updated: <strong>{last_updated}</strong></p>
    <div class="header-controls">
      <select id="snapshot-picker" class="snapshot-picker" onchange="goSnapshot(this.value)" aria-label="Snapshot date">
        {options}
      </select>
      <button type="button" id="refresh-btn" class="refresh-btn" aria-busy="false">
        <span id="refresh-btn-label">Refresh now</span>
      </button>
    </div>
  </div>
  <hr class="divider">"""


def patch_header_styles(html: str) -> str:
    """Keep snapshot dropdown compact on pages built from older templates."""
    html = re.sub(r"\.snapshot-label \{[^}]+\}\s*", "", html, flags=re.DOTALL)
    if ".header-controls {" not in html:
        html = html.replace(
            ".header-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 28px; }",
            ".header-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 28px; }\n"
            ".header-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; flex: 0 1 auto; min-width: 0; }",
        )
    else:
        html = html.replace(
            ".header-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; flex: 1 1 auto; min-width: 0; }",
            ".header-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; flex: 0 1 auto; min-width: 0; }",
        )
    html = re.sub(
        r"\.snapshot-picker \{[^}]+\}",
        (
            ".snapshot-picker {\n"
            "  font-size: 12px; font-weight: 500; font-family: inherit;\n"
            "  color: var(--text); background: var(--card);\n"
            "  border: 1px solid var(--border); border-radius: 6px;\n"
            "  padding: 6px 10px; cursor: pointer;\n"
            "  flex: 0 1 auto; max-width: 300px; min-width: 0;\n"
            "  box-sizing: border-box;\n"
            "}"
        ),
        html,
        count=1,
    )
    html = html.replace(
        "  .header-controls { width: 100%; flex-direction: column; align-items: stretch; }\n"
        "  .snapshot-label { width: 100%; flex: none; max-width: 100%; }\n"
        "  .snapshot-picker { width: 100%; max-width: 100%; }\n"
        "  .refresh-btn { width: 100%; }\n",
        "  .header-controls { width: 100%; flex-direction: row; align-items: center; }\n"
        "  .snapshot-picker { flex: 1 1 160px; max-width: none; }\n"
        "  .refresh-btn { flex: 0 0 auto; width: auto; }\n",
    )
    html = html.replace(
        "  .header-row .last-updated { flex: 1 1 auto; min-width: 0; }\n"
        "  .refresh-btn { flex: 1 1 auto; }\n",
        "  .header-row .last-updated { flex: 1 1 auto; min-width: 0; }\n"
        "  .header-controls { width: 100%; flex-direction: row; align-items: center; }\n"
        "  .snapshot-picker { flex: 1 1 160px; max-width: none; }\n"
        "  .refresh-btn { flex: 0 0 auto; width: auto; }\n",
    )
    return html


def standardize_header(
    html: str, dates: list[dict], current: str | None, latest_label: str
) -> str:
    """Normalize header row (compact dropdown + always-visible refresh)."""
    html = patch_header_styles(html)
    last_updated = _last_updated_text(html) or format_dropdown_label(now_est())
    block = render_header_row(last_updated, dates, current, latest_label)
    if HEADER_ROW_RE.search(html):
        return HEADER_ROW_RE.sub(block, html, count=1)
    return inject_dropdown(html, dates, current, latest_label)


def list_archive_dates() -> list[str]:
    if not DOCS_ARCHIVE.exists():
        return []
    return sorted(
        (p.stem for p in DOCS_ARCHIVE.glob("*.html")),
        reverse=True,
    )


def _last_updated_text(html: str) -> str | None:
    m = LAST_UPDATED_RE.search(html)
    if not m:
        return None
    block = html[m.start() : m.end()]
    strong = re.search(r"<strong>([^<]+)</strong>", block)
    return strong.group(1).strip() if strong else None


def archive_manifest(exclude_date: str | None = None) -> list[dict]:
    """Dropdown archive labels from each saved HTML (source of truth for display time)."""
    if not DOCS_ARCHIVE.exists():
        return []
    items: list[dict] = []
    for path in sorted(DOCS_ARCHIVE.glob("*.html"), key=lambda p: p.stem, reverse=True):
        day = path.stem
        if exclude_date and day == exclude_date:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            continue
        text = _last_updated_text(raw)
        if not text:
            continue
        items.append({"date": day, "label": label_from_last_updated(text)})
    return items


def latest_option_label(html: str) -> str:
    text = _last_updated_text(html)
    if text:
        return f"{label_from_last_updated(text)} · Latest"
    return f"{format_dropdown_label(now_est())} · Latest"


def publish_docs() -> None:
    if not REPORT_HTML.exists():
        raise FileNotFoundError(f"Missing built report: {REPORT_HTML}")

    today = date.today().isoformat()
    DOCS_ARCHIVE.mkdir(parents=True, exist_ok=True)
    DOCS_HISTORY.mkdir(parents=True, exist_ok=True)

    base_html = REPORT_HTML.read_text(encoding="utf-8")
    archive_path = DOCS_ARCHIVE / f"{today}.html"
    archive_path.write_text(base_html, encoding="utf-8")

    manifest_dates = archive_manifest(exclude_date=today)
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

    index_html = standardize_header(
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
        published = standardize_header(
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
