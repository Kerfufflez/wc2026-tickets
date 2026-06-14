"""Publish dashboard to docs/games/{pid}/ for GitHub Pages."""

from __future__ import annotations

import json
import re
import shutil
from datetime import date

from wc2026.config import (
    DEAL_LOG_JS,
    DOCS,
    REFRESH_JS,
    ROOT,
    game_deal_log_html,
    game_docs_archive,
    game_docs_dir,
    game_docs_history,
    game_docs_manifest,
    game_docs_deal_log,
    game_report_html,
)
from wc2026.dates import format_dropdown_label, label_from_last_updated, now_est
from wc2026.games import format_game_date, load_matches

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
    last_updated: str, dates: list[dict], current: str | None, latest_label: str, pid: str
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
    html: str, dates: list[dict], current: str | None, latest_label: str, pid: str = ""
) -> str:
    html = patch_header_styles(html)
    last_updated = _last_updated_text(html) or format_dropdown_label(now_est())
    block = render_header_row(last_updated, dates, current, latest_label, pid)
    if HEADER_ROW_RE.search(html):
        return HEADER_ROW_RE.sub(block, html, count=1)
    return inject_dropdown(html, dates, current, latest_label)


def list_archive_dates(pid: str) -> list[str]:
    archive = game_docs_archive(pid)
    if not archive.exists():
        return []
    return sorted(
        (p.stem for p in archive.glob("*.html")),
        reverse=True,
    )


def _last_updated_text(html: str) -> str | None:
    m = LAST_UPDATED_RE.search(html)
    if not m:
        return None
    block = html[m.start(): m.end()]
    strong = re.search(r"<strong>([^<]+)</strong>", block)
    return strong.group(1).strip() if strong else None


def archive_manifest(pid: str, exclude_date: str | None = None) -> list[dict]:
    archive = game_docs_archive(pid)
    if not archive.exists():
        return []
    items: list[dict] = []
    for path in sorted(archive.glob("*.html"), key=lambda p: p.stem, reverse=True):
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


def _refresh_js_depth(depth: int) -> str:
    """Relative path from docs/games/{pid}/[archive/] to docs/refresh.js."""
    return "../" * depth + "../../refresh.js"


def _deal_log_js_depth(depth: int) -> str:
    return "../" * depth + "../../games/{pid}/history/deal_log.js"


def publish_docs(pid: str, match: dict) -> None:
    report_html = game_report_html(pid)
    if not report_html.exists():
        raise FileNotFoundError(f"Missing built report: {report_html}")

    today = date.today().isoformat()
    docs_dir = game_docs_dir(pid)
    archive_dir = game_docs_archive(pid)
    history_dir = game_docs_history(pid)
    archive_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    # Ensure shared refresh.js is at docs root
    docs_root = DOCS
    docs_root.mkdir(parents=True, exist_ok=True)
    if REFRESH_JS.exists():
        shutil.copy2(REFRESH_JS, docs_root / "refresh.js")

    base_html = report_html.read_text(encoding="utf-8")

    # Fix relative paths for docs/games/{pid}/ (2 levels deeper than docs root)
    base_html_docs = base_html.replace(
        'src="refresh.js"', 'src="../../refresh.js"'
    )

    # Save today's archive
    archive_path = archive_dir / f"{today}.html"
    archive_path.write_text(base_html_docs, encoding="utf-8")

    manifest_dates = archive_manifest(pid, exclude_date=today)
    game_docs_manifest(pid).write_text(
        json.dumps({"dates": manifest_dates}, indent=2) + "\n",
        encoding="utf-8",
    )

    latest_label = latest_option_label(base_html_docs)
    dates_for_dropdown = manifest_dates

    # Publish deal log
    deal_log_src = game_deal_log_html(pid)
    if deal_log_src.exists():
        published_log = deal_log_src.read_text(encoding="utf-8")
        published_log = published_log.replace(
            'href="../dashboard.html"', 'href="../index.html"'
        )
        game_docs_deal_log(pid).write_text(published_log, encoding="utf-8")
        deal_log_js_src = DEAL_LOG_JS
        if deal_log_js_src.exists():
            shutil.copy2(deal_log_js_src, history_dir / "deal_log.js")

    # Build docs/games/{pid}/index.html
    index_html = standardize_header(
        set_snapshot_context(base_html_docs, "index"),
        dates_for_dropdown,
        current=None,
        latest_label=latest_label,
        pid=pid,
    )
    index_html = index_html.replace(
        'href="history/DEAL_LOG.md"', 'href="history/deal-log.html"'
    )
    (docs_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Patch archive pages
    archive_dates = list_archive_dates(pid)
    for d in archive_dates:
        path = archive_dir / f"{d}.html"
        raw = base_html_docs if d == today else path.read_text(encoding="utf-8")
        published = standardize_header(
            set_snapshot_context(raw, "archive"),
            dates_for_dropdown,
            current=d,
            latest_label=latest_label,
            pid=pid,
        )
        published = published.replace(
            'href="history/DEAL_LOG.md"', 'href="../history/deal-log.html"'
        )
        published = published.replace('src="../../refresh.js"', 'src="../../../refresh.js"')
        path.write_text(published, encoding="utf-8")

    print(f"Published docs/games/{pid}/index.html")
    print(f"Published docs/games/{pid}/archive/{today}.html")
    if deal_log_src.exists():
        print(f"Published docs/games/{pid}/history/deal-log.html")
    print(
        f"Archive dates: {', '.join(archive_dates) if archive_dates else '(none)'}"
    )

    # Regenerate the top-level game-picker landing page
    _publish_index(pid)


def _game_picker_html(
    all_matches: list[dict],
    built_pids: set[str],
    link_prefix: str,
    link_suffix: str = "/",
) -> str:
    """Generate game-picker HTML. Built games are linked; others are plain text."""
    rows = ""
    for m in all_matches:
        pid = str(m["pid"])
        matchup = m.get("matchup", pid)
        venue = m.get("venue", "")
        stage = m.get("stage", "")
        game_date = format_game_date(m)
        if pid in built_pids:
            name_cell = f'<a href="{link_prefix}{pid}{link_suffix}">{matchup}</a>'
        else:
            name_cell = f'<span style="color:#999">{matchup}</span>'
        rows += (
            f'<tr>'
            f'<td>{name_cell}</td>'
            f'<td>{stage}</td>'
            f'<td>{game_date}</td>'
            f'<td>{venue}</td>'
            f'</tr>\n'
        )
    if not rows:
        rows = '<tr><td colspan="4">No games in data/matches.json.</td></tr>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WC2026 Ticket Tracker</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 860px; margin: 40px auto; padding: 0 16px; color: #1a1a1a; }}
    h1 {{ font-size: 1.5rem; margin-bottom: 4px; }}
    p.sub {{ color: #666; margin-top: 0; margin-bottom: 24px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid #e5e5e5; }}
    th {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #666; }}
    tr:hover td {{ background: #f9f9f9; }}
    a {{ color: #1d6bd4; text-decoration: none; font-weight: 500; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>WC2026 Ticket Tracker</h1>
  <p class="sub">Live SeatSidekick inventory dashboards, refreshed every 12 hours.</p>
  <table>
    <thead>
      <tr><th>Match</th><th>Stage</th><th>Date</th><th>Venue</th></tr>
    </thead>
    <tbody>
{rows}    </tbody>
  </table>
</body>
</html>
"""


def _publish_index(updated_pid: str | None = None) -> None:
    """Regenerate docs/index.html and reports/index.html listing all upcoming games."""
    try:
        matches = load_matches()
    except FileNotFoundError:
        return

    all_matches = sorted(matches, key=lambda m: m.get("date", ""))

    docs_built = {str(m["pid"]) for m in matches if (game_docs_dir(str(m["pid"])) / "index.html").exists()}
    docs_html = _game_picker_html(all_matches, docs_built, link_prefix="games/")
    (DOCS / "index.html").write_text(docs_html, encoding="utf-8")
    print(f"Published docs/index.html ({len(all_matches)} games, {len(docs_built)} with dashboards)")

    reports_built = {str(m["pid"]) for m in matches if (ROOT / "reports" / str(m["pid"]) / "dashboard.html").exists()}
    reports_html = _game_picker_html(all_matches, reports_built, link_prefix="", link_suffix="/dashboard.html")
    (ROOT / "reports" / "index.html").write_text(reports_html, encoding="utf-8")
    print(f"Published reports/index.html ({len(all_matches)} games, {len(reports_built)} with dashboards)")
