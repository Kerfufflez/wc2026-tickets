"""Paths and API constants — single source of truth."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# API
API_BASE = "https://dlvtfsmonledyyjaqjcn.supabase.co/rest/v1/match_seat_groups"
APIKEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsdnRmc21vbmxlZHl5amFxamNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY0MDk3NDcsImV4cCI6MjA5MTk4NTc0N30.warYGD7rBH_x_qx9i56WfcJ3RKhCALBEarzHSUpkq5k"
)
API_HEADERS = {
    "apikey": APIKEY,
    "accept-profile": "api",
    "origin": "https://seatsidekick.com",
}
PERFORMANCE_ID = "10229226725358"
PAGE_SIZE = 100
MAX_SINGLE_LIMIT = 1000

# Paths
TEMPLATE = ROOT / "templates" / "dashboard.html"
DATA_RAW = ROOT / "data" / "raw"
FETCH_META = ROOT / "data" / "fetch_meta.json"
REPORT_HTML = ROOT / "reports" / "dashboard.html"
REPORT_HISTORY = ROOT / "reports" / "history"
REPORT_SNAPSHOTS = REPORT_HISTORY / "snapshots"
REPORT_DEAL_LOG = REPORT_HISTORY / "DEAL_LOG.md"
REPORT_OVERLAP = ROOT / "reports" / "overlap_analysis.md"
DOCS = ROOT / "docs"
DOCS_ARCHIVE = DOCS / "archive"
DOCS_HISTORY = DOCS / "history"
DOCS_MANIFEST = DOCS_HISTORY / "manifest.json"
STATIC = ROOT / "static"
REFRESH_JS = STATIC / "refresh.js"

CATEGORIES = [
    ("cat1", "cat1_g2.json", "cat1_g4.json"),
    ("cat2", "cat2_g2.json", "cat2_g4.json"),
    ("cat3", "cat3_g2.json", "cat3_g4.json"),
]

FETCH_QUERIES = [
    ("cat1_g2.json", "Category 1", 2),
    ("cat1_g4.json", "Category 1", 4),
    ("cat2_g2.json", "Category 2", 2),
    ("cat2_g4.json", "Category 2", 4),
    ("cat3_g2.json", "Category 3", 2),
    ("cat3_g4.json", "Category 3", 4),
]


def raw_path(filename: str) -> Path:
    return DATA_RAW / filename
