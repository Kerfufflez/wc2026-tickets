#!/usr/bin/env bash
# Local preview server — serves reports/ at http://localhost:8080/
# After running, open: http://localhost:8080/<pid>/dashboard.html
# Example: http://localhost:8080/10229226725358/dashboard.html
set -euo pipefail
cd "$(dirname "$0")"
echo "Serving reports/ at http://localhost:8080/"
echo "Press Ctrl+C to stop."
python3 -m http.server 8080 -d reports/
