#!/usr/bin/env bash
# Daily dashboard refresh: fetch → overlap analysis → build + publish
set -euo pipefail
cd "$(dirname "$0")"
python3 -m wc2026 refresh
echo ""
echo "Local dashboard: reports/dashboard.html"
echo "Published site:  docs/index.html"
echo "Deal log:        reports/history/deal-log.html"
