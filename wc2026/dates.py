"""Eastern Time formatting — single source of truth for display timestamps."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def now_est() -> datetime:
    return datetime.now(ET)


def to_est(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=ET)
    return dt.astimezone(ET)


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


def iso_est(dt: datetime | None = None) -> str:
    d = to_est(dt) if dt is not None else now_est()
    return d.isoformat(timespec="seconds")


def snapshot_id(dt: datetime | None = None) -> str:
    """2026-06-05T181932 — safe filename stem"""
    d = to_est(dt) if dt is not None else now_est()
    return d.strftime("%Y-%m-%dT%H%M%S")


def parse_captured_at(value: str) -> datetime:
    """Parse ISO captured_at from snapshot JSON."""
    return to_est(datetime.fromisoformat(value))
