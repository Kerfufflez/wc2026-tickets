## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 40 groups, price range $1,589 – $14,675 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       88.9% | May exist in G2, not top-100   |
| NEW        |     3 |       11.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 219 Row TT Seats 5–6  avg $811/ea  total $1,622
Cheapest New: Sec 218 Row MM Seats 5–6  avg $730/ea  total $1,460

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 31 groups, price range $1,297 – $8,108 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row EE Seats 5–6  avg $795/ea  total $1,590
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             24 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

