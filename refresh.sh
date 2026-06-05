#!/usr/bin/env bash
# Daily dashboard refresh: fetch → validate/analysis → HTML + deal log
set -euo pipefail
cd "$(dirname "$0")"
python3 fetch_seatsidekick.py
python3 analyze_overlap.py
python3 build_html_data.py
echo ""
echo "Local dashboard: World Cup Semi-Final Tickets.html"
echo "Published site:  docs/index.html"
echo "Deal log:        history/DEAL_LOG.md"
