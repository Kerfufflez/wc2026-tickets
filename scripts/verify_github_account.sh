#!/usr/bin/env bash
# Run before creating the repo — confirms which GitHub account is active.
set -euo pipefail
if ! command -v gh >/dev/null 2>&1; then
  echo "Install GitHub CLI: brew install gh && gh auth login"
  exit 1
fi
echo "Active GitHub accounts:"
gh auth status
echo ""
echo "API identity (this is who will own the repo):"
gh api user --jq '"login: " + .login + "\nname: " + (.name // "n/a") + "\nemail: " + (.email // "n/a")'
echo ""
echo "If this is your WORK account, run: gh auth switch"
