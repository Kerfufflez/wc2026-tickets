# WC2026 Semi-Final Ticket Dashboard

Live SeatSidekick inventory for the Atlanta World Cup semi-final, with day-over-day deal tracking.

## Project layout

```
wc2026/              Python package (fetch, build, tracker, publish)
data/raw/            API JSON snapshots + fetch_meta.json
templates/           Dashboard HTML source template
reports/             Built dashboard + overlap analysis + deal history
static/              Client-side refresh.js (live API pull in browser)
docs/                GitHub Pages output (auto-generated — don't edit)
scripts/             Helper scripts
```

## Share URL (after GitHub Pages setup)

`https://<your-personal-username>.github.io/wc2026-tickets/`

## Local refresh

```bash
./refresh.sh
# or: python3 -m wc2026 refresh
```

Individual steps:

```bash
python3 -m wc2026 fetch     # pull latest API data → data/raw/
python3 -m wc2026 overlap   # G4 pair overlap report → reports/overlap_analysis.md
python3 -m wc2026 build     # dashboard + deal log + docs/
```

Open `reports/dashboard.html` locally, or `docs/index.html` for the published copy.

The dashboard **Refresh now** button pulls live listings in the browser (60s cooldown) — works on GitHub Pages without waiting for CI.

## One-time GitHub setup (personal account)

Your global git email is already personal (`git config user.email`). This repo uses that identity locally — commits will not go through your work account unless you push to a work remote.

### Option A — Publish via Cursor (recommended, no `gh` needed)

Cursor’s GitHub connection handles auth for git push. Use it to create the repo on your **personal** account:

1. Open **Source Control** (sidebar or `Cmd+Shift+G`)
2. Click **Publish to GitHub** (cloud/upload icon on the `main` branch)
3. When prompted:
   - Choose your **personal** GitHub account (not work)
   - Repository name: `wc2026-tickets`
   - Visibility: **Public**
4. After push completes, on github.com open the new repo → **Settings** → **Pages**
5. Source: **Deploy from a branch** → **main** → folder **/docs** → **Save**

Share URL: `https://<your-personal-username>.github.io/wc2026-tickets/`

### Option B — GitHub CLI (`gh` is installed via Homebrew)

Log in once (pick personal account in the browser flow):

```bash
gh auth login
gh auth status
gh api user --jq .login   # confirm personal username
```

Then create and push:

```bash
gh repo create YOUR_PERSONAL_USERNAME/wc2026-tickets --public --source=. --remote=origin --push
```

Enable Pages: repo **Settings** → **Pages** → **main** / **/docs**

### Option C — Browser + git push

Create an empty public repo `wc2026-tickets` on your **personal** GitHub account, then:

```bash
git remote add origin https://github.com/YOUR_PERSONAL_USERNAME/wc2026-tickets.git
git push -u origin main
```

Cursor will prompt to sign in with GitHub if needed — use your personal account.

## Automation

GitHub Actions runs every 6 hours (UTC) and on manual **workflow_dispatch**, fetching fresh data and pushing updates to `docs/`.

## Snapshot dropdown

The published site includes a **Snapshot** picker: **Latest** plus one archived HTML page per calendar day (`docs/archive/YYYY-MM-DD.html`).
