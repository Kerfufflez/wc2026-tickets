#!/usr/bin/env bash
# Full refresh: update match list, then refresh all games.
# Usage:
#   ./refresh.sh              — refresh all games
#   ./refresh.sh --game M102  — refresh one game by event code or pid
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" == "--game" ]]; then
  python3 -m wc2026 fetch-games
  python3 -m wc2026 refresh --game "$2"
  echo ""
  echo "Local dashboard: reports/${2}/dashboard.html"
  echo "Run ./serve.sh to preview at http://localhost:8080/"
else
  python3 -m wc2026 fetch-games
  python3 -m wc2026 refresh-all
  echo ""
  echo "Run ./serve.sh to preview at http://localhost:8080/"
fi
