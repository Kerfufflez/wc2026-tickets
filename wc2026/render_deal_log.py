"""Render deal_log.json into styled HTML changelog."""

from __future__ import annotations

import html
import json

from wc2026.config import REPORT_DEAL_LOG_HTML, REPORT_DEAL_LOG_JSON, TEMPLATE_DEAL_LOG
from wc2026.dates import format_est, now_est
from wc2026.tracker import load_deal_log_entries


def _esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def _signed(n: int) -> str:
    if n > 0:
        return f"+{n}"
    if n < 0:
        return str(n)
    return "±0"


def _delta_class(n: int) -> str:
    if n > 0:
        return "up"
    if n < 0:
        return "down"
    return "flat"


def _deal_row(deal: dict, accent: str = "") -> str:
    tags = []
    if deal.get("derived"):
        tags.append('<span class="deal-tag">4-pack split</span>')
    if deal.get("front"):
        tags.append('<span class="deal-tag deal-tag-front">front</span>')
    change = deal.get("change")
    change_html = (
        f'<span class="deal-change">{_esc(change)}</span>' if change else ""
    )
    tags_html = "".join(tags)
    return f"""<li class="deal-row {accent}">
  <div class="deal-main">
    <span class="deal-loc">Sec {_esc(deal['sec'])} · Row {_esc(deal['row'])}</span>
    <span class="deal-meta">{_esc(deal['seats'])} · {deal['gs']}t{(' · ' + tags_html) if tags_html else ''}</span>
  </div>
  <div class="deal-price">
    <span class="deal-avg">${deal['avg']:,}<span class="deal-per">/ea</span></span>
    {change_html}
  </div>
</li>"""


def _cat_signals(cat: dict, is_baseline: bool) -> list[tuple[str, str]]:
    if is_baseline:
        return []
    signals: list[tuple[str, str]] = []
    n_cheaper = len(cat.get("cheaper", []))
    if n_cheaper:
        signals.append((f"{n_cheaper} cheaper", "green"))
    n_top = len(cat.get("top10_new_g2", [])) + len(cat.get("top10_new_g4", []))
    if n_top:
        signals.append((f"{n_top} new in top 10", "blue"))
    g2d, g4d = cat.get("g2_delta", 0), cat.get("g4_delta", 0)
    if not n_cheaper and not n_top and not g2d and not g4d:
        signals.append(("no changes", "muted"))
    return signals


def render_cat_preview(cat_key: str, cat: dict, is_baseline: bool) -> str:
    g2d, g4d = cat.get("g2_delta", 0), cat.get("g4_delta", 0)
    signals = _cat_signals(cat, is_baseline)
    signals_html = "".join(
        f'<span class="signal signal-{kind}">{_esc(text)}</span>'
        for text, kind in signals
    )
    if is_baseline:
        delta_html = (
            f'<span class="inv-count">{cat["g2_count"]} G2</span>'
            f'<span class="inv-count">{cat["g4_count"]} G4</span>'
        )
    else:
        delta_html = (
            f'<span class="delta delta-{_delta_class(g2d)}">G2 {_signed(g2d)}</span>'
            f'<span class="delta delta-{_delta_class(g4d)}">G4 {_signed(g4d)}</span>'
        )
    return f"""<div class="cat-preview-row">
  <span class="cat-preview-label">{_esc(cat['label'])}</span>
  <div class="cat-preview-deltas">{delta_html}</div>
  <div class="cat-preview-signals">{signals_html}</div>
</div>"""


def render_cat_detail(cat: dict, is_baseline: bool) -> str:
    g2d, g4d = cat.get("g2_delta", 0), cat.get("g4_delta", 0)
    if is_baseline:
        counts = (
            f'<div class="cat-stat">'
            f'<span class="cat-stat-label">Inventory</span>'
            f'<span class="cat-stat-value">{cat["g2_count"]} G2 · {cat["g4_count"]} G4</span>'
            f"</div>"
        )
        body = counts + '<p class="cat-quiet">Baseline scan — nothing to compare yet.</p>'
    else:
        counts = (
            f'<div class="cat-stat-grid">'
            f'<div class="cat-stat"><span class="cat-stat-label">G2 listings</span>'
            f'<span class="cat-stat-value">{cat["g2_count"]} <span class="delta delta-{_delta_class(g2d)}">{_signed(g2d)}</span></span></div>'
            f'<div class="cat-stat"><span class="cat-stat-label">G4 listings</span>'
            f'<span class="cat-stat-value">{cat["g4_count"]} <span class="delta delta-{_delta_class(g4d)}">{_signed(g4d)}</span></span></div>'
            f"</div>"
        )
        sections: list[str] = [counts]

        cheaper = cat.get("cheaper", [])
        if cheaper:
            rows = "".join(_deal_row(d, "accent-drop") for d in cheaper)
            sections.append(
                f'<div class="cat-block"><h4 class="cat-block-title">Cheaper tickets</h4>'
                f'<ul class="deal-list">{rows}</ul></div>'
            )
        else:
            sections.append(
                '<div class="cat-block"><h4 class="cat-block-title">Cheaper tickets</h4>'
                '<p class="cat-quiet">None vs prior scan</p></div>'
            )

        for gs_label, key in (("G2", "top10_new_g2"), ("G4", "top10_new_g4")):
            items = cat.get(key, [])
            if items:
                rows = "".join(_deal_row(d, "accent-new") for d in items)
                sections.append(
                    f'<div class="cat-block"><h4 class="cat-block-title">New in top 10 · {gs_label}</h4>'
                    f'<ul class="deal-list">{rows}</ul></div>'
                )

        if not cheaper and not cat.get("top10_new_g2") and not cat.get("top10_new_g4"):
            if not g2d and not g4d:
                sections.append('<p class="cat-quiet">No listing movement this scan.</p>')

        body = "".join(sections)

    return f"""<section class="cat-panel">
  <h3 class="cat-panel-title">{_esc(cat['label'])}</h3>
  {body}
</section>"""


def render_entry_card(entry: dict) -> str:
    is_baseline = entry.get("is_baseline", False)
    categories = entry.get("categories", {})

    preview_rows = "".join(
        render_cat_preview(k, categories[k], is_baseline)
        for k in ("cat1", "cat2", "cat3")
        if k in categories
    )

    detail_sections = "".join(
        render_cat_detail(categories[k], is_baseline)
        for k in ("cat1", "cat2", "cat3")
        if k in categories
    )

    badge = ""
    if is_baseline:
        badge = '<span class="changelog-badge">Baseline</span>'

    prev_note = ""
    if entry.get("prev_label"):
        prev_note = (
            f'<p class="changelog-compare">vs {_esc(entry["prev_label"])}</p>'
        )

    return f"""<article class="changelog-card" data-id="{_esc(entry['id'])}">
  <button type="button" class="changelog-card-header" aria-expanded="false">
    <div class="changelog-card-top">
      <time class="changelog-time" datetime="{_esc(entry.get('captured_at', ''))}">{_esc(entry['captured_label'])}</time>
      {badge}
      <span class="changelog-toggle" aria-hidden="true">+</span>
    </div>
    {prev_note}
    <div class="changelog-preview">{preview_rows}</div>
  </button>
  <div class="changelog-body" hidden>
    <div class="changelog-body-inner">{detail_sections}</div>
  </div>
</article>"""


def render_deal_log() -> None:
    TEMPLATE_DEAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    template = TEMPLATE_DEAL_LOG.read_text(encoding="utf-8")

    entries = load_deal_log_entries()
    if entries:
        cards = "\n".join(render_entry_card(e) for e in entries)
    else:
        cards = (
            '<p class="changelog-empty">No refresh entries yet. Run '
            '<code>python3 -m wc2026 build</code> after fetching data.</p>'
        )

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
