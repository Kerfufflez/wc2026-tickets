"""Eastern Time formatting — single source of truth for display timestamps."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

_HAS_OFFSET = re.compile(r"(Z|[+-]\d{2}:\d{2})$")
_LEGACY_DAILY = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def now_est() -> datetime:
    return datetime.now(ET)


def to_est(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=ET)
    return dt.astimezone(ET)


def _has_offset(value: str) -> bool:
    return bool(_HAS_OFFSET.search(value.strip()))


def parse_captured_at(value: str, source: Path | None = None) -> datetime:
    """Parse snapshot captured_at; naive legacy UTC (CI) vs ET (local) handled."""
    raw = value.strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(raw)
    if dt.tzinfo is not None:
        return dt.astimezone(ET)
    if source and _LEGACY_DAILY.match(source.stem):
        # GitHub Actions wrote UTC without offset; local evening builds wrote ET.
        if dt.hour >= 17:
            return dt.replace(tzinfo=ET)
        return dt.replace(tzinfo=UTC).astimezone(ET)
    return dt.replace(tzinfo=ET)


def format_est(dt: datetime | None = None) -> str:
    """Jun 5, 2026 at 6:19 PM ET"""
    d = to_est(dt) if dt is not None else now_est()
    return f"{d.strftime('%b %-d, %Y at %-I:%M %p')} ET"


def format_est_short(dt: datetime | None = None) -> str:
    """6:19 PM ET"""
    d = to_est(dt) if dt is not None else now_est()
    return f"{d.strftime('%-I:%M %p')} ET"


def format_est_date(dt: datetime | None = None) -> str:
    """Jun 5, 2026"""
    d = to_est(dt) if dt is not None else now_est()
    return d.strftime("%b %-d, %Y")


def format_dropdown_label(dt: datetime | None = None) -> str:
    """Jun 5, 2026 · 6:19 PM ET"""
    d = to_est(dt) if dt is not None else now_est()
    return f"{format_est_date(d)} · {format_est_short(d)}"


def label_from_last_updated(text: str) -> str:
    """Convert 'Jun 6, 2026 at 12:01 PM ET' → dropdown label."""
    if " at " in text:
        date_part, time_part = text.split(" at ", 1)
        time_part = time_part.strip()
        if not time_part.endswith("ET"):
            time_part = f"{time_part} ET"
        return f"{date_part} · {time_part}"
    return text


def iso_est(dt: datetime | None = None) -> str:
    d = to_est(dt) if dt is not None else now_est()
    return d.isoformat(timespec="seconds")


def snapshot_id(dt: datetime | None = None) -> str:
    """2026-06-05T181932 — safe filename stem"""
    d = to_est(dt) if dt is not None else now_est()
    return d.strftime("%Y-%m-%dT%H%M%S")
