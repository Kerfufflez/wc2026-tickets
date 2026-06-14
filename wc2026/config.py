"""Paths and API constants — single source of truth."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Seat groups API
API_BASE = "https://dlvtfsmonledyyjaqjcn.supabase.co/rest/v1/match_seat_groups"
APIKEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsdnRmc21vbmxlZHl5amFxamNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY0MDk3NDcsImV4cCI6MjA5MTk4NTc0N30.warYGD7rBH_x_qx9i56WfcJ3RKhCALBEarzHSUpkq5k"
)
API_HEADERS = {
    "apikey": APIKEY,
    "accept-profile": "api",
    "origin": "https://seatsidekick.com",
}
PAGE_SIZE = 100
MAX_SINGLE_LIMIT = 1000

# Matches list API
MATCHES_API = "https://seatsidekick.com/api/matches"
MATCHES_CACHE = ROOT / "data" / "matches.json"

# Template sources (shared across all games)
TEMPLATE = ROOT / "templates" / "dashboard.html"
TEMPLATE_DEAL_LOG = ROOT / "templates" / "deal_log.html"
STATIC = ROOT / "static"
REFRESH_JS = STATIC / "refresh.js"
DEAL_LOG_JS = STATIC / "deal_log.js"

# Docs root
DOCS = ROOT / "docs"


# --- Per-game path helpers ---

def game_raw_dir(pid: str) -> Path:
    return ROOT / "data" / "raw" / pid


def game_raw_path(pid: str, filename: str) -> Path:
    return game_raw_dir(pid) / filename


def game_fetch_meta(pid: str) -> Path:
    return game_raw_dir(pid) / "fetch_meta.json"


def game_report_dir(pid: str) -> Path:
    return ROOT / "reports" / pid


def game_report_html(pid: str) -> Path:
    return game_report_dir(pid) / "dashboard.html"


def game_overlap(pid: str) -> Path:
    return game_report_dir(pid) / "overlap_analysis.md"


def game_history(pid: str) -> Path:
    return game_report_dir(pid) / "history"


def game_snapshots(pid: str) -> Path:
    return game_history(pid) / "snapshots"


def game_deal_log_json(pid: str) -> Path:
    return game_history(pid) / "deal_log.json"


def game_deal_log_md(pid: str) -> Path:
    return game_history(pid) / "DEAL_LOG.md"


def game_deal_log_html(pid: str) -> Path:
    return game_history(pid) / "deal-log.html"


def game_docs_dir(pid: str) -> Path:
    return DOCS / "games" / pid


def game_docs_archive(pid: str) -> Path:
    return game_docs_dir(pid) / "archive"


def game_docs_history(pid: str) -> Path:
    return game_docs_dir(pid) / "history"


def game_docs_manifest(pid: str) -> Path:
    return game_docs_history(pid) / "manifest.json"


def game_docs_deal_log(pid: str) -> Path:
    return game_docs_history(pid) / "deal-log.html"
