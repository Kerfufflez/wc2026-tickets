"""Render deal_log.json into styled HTML changelog."""

from __future__ import annotations

import html
import json

from wc2026.config import REPORT_DEAL_LOG_HTML, REPORT_DEAL_LOG_JSON, TEMPLATE_DEAL_LOG
from wc2026.dates import format_est, now_est
from wc2026.tracker import load_deal_log_entries


def _esc(text: str) -> str:
    return html.escape(text, quote=True)


def render_entry_card(entry: dict) -> str:
    lines_preview = "".join(
        f'<p class="changelog-preview-line">{_esc(line)}</p>'
        for line in entry.get("preview_lines", [])
    )
    detail = "\n".join(entry.get("detail_lines", []))
    if not detail and entry.get("is_baseline"):
        detail = "Baseline inventory — no prior scan to compare."

    badge = ""
    if entry.get("is_baseline"):
        badge = '<span class="changelog-badge">Baseline</span>'

    return f"""<article class="changelog-card" data-id="{_esc(entry['id'])}">
  <button type="button" class="changelog-card-header" aria-expanded="false">
    <div class="changelog-card-top">
      <time class="changelog-time" datetime="{_esc(entry.get('captured_at', ''))}">{_esc(entry['captured_label'])}</time>
      {badge}
      <span class="changelog-toggle" aria-hidden="true">+</span>
    </div>
    <div class="changelog-preview">{lines_preview}</div>
  </button>
  <div class="changelog-body" hidden>
    <div class="changelog-body-inner">{_esc(detail)}</div>
  </div>
</article>"""


def render_deal_log() -> None:
    TEMPLATE_DEAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    template = TEMPLATE_DEAL_LOG.read_text(encoding="utf-8")

    entries = load_deal_log_entries()
    if entries:
        cards = "\n".join(render_entry_card(e) for e in entries)
    else:
        cards = '<p class="changelog-empty">No refresh entries yet. Run <code>python3 -m wc2026 build</code> after fetching data.</p>'

    generated = format_est(now_est())
    html_out = (
        template.replace("__ENTRIES__", cards)
        .replace("__GENERATED__", _esc(generated))
        .replace("__BACK_LINK__", "../dashboard.html")
    )

    REPORT_DEAL_LOG_HTML.parent.mkdir(parents=True, exist_ok=True)
    REPORT_DEAL_LOG_HTML.write_text(html_out, encoding="utf-8")
    print(f"Rendered {REPORT_DEAL_LOG_HTML} ({len(entries)} entries)")


def main() -> int:
    if not REPORT_DEAL_LOG_JSON.exists():
        print(f"No {REPORT_DEAL_LOG_JSON} — run tracker first")
        return 1
    render_deal_log()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
