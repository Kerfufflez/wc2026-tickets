# WC2026 Semi-Final Ticket Dashboard

Live SeatSidekick inventory for the Atlanta World Cup semi-final, with day-over-day deal tracking.

## Share URL (after GitHub Pages setup)

`https://<your-personal-username>.github.io/wc2026-tickets/`

## Local refresh

```bash
./refresh.sh
```

## One-time GitHub setup (personal account)

**1. Confirm you are on your personal GitHub account** (not work):

```bash
gh auth status
gh api user --jq .login
```

If wrong account: `gh auth switch`

**2. Create and push the repo** (replace `YOUR_PERSONAL_USERNAME`):

```bash
git init
git add .
git commit -m "Initial publish: WC2026 ticket dashboard"
gh repo create YOUR_PERSONAL_USERNAME/wc2026-tickets --public --source=. --remote=origin --push
```

Without `gh` CLI: create a public repo named `wc2026-tickets` on your **personal** GitHub account in the browser, then:

```bash
git remote add origin https://github.com/YOUR_PERSONAL_USERNAME/wc2026-tickets.git
git branch -M main
git push -u origin main
```

**3. Enable GitHub Pages**

Repo → **Settings** → **Pages** → Build from **main** branch, folder **/docs** → Save.

Pages URL will be live in ~1–2 minutes.

## Automation

GitHub Actions runs every 6 hours (UTC) and on manual **workflow_dispatch**, fetching fresh data and pushing updates to `docs/`.

## Snapshot dropdown

The published site includes a **Snapshot** picker: **Latest** plus one archived HTML page per calendar day (`docs/archive/YYYY-MM-DD.html`).
