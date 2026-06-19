## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 50 groups, price range $3,112 – $13,570 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 119 Row W Seats 14–15  avg $1,840/ea  total $3,680
Cheapest New: Sec 339 Row G Seats 1–2  avg $8,243/ea  total $16,486

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 5 groups, price range $3,036 – $6,900 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 630 Row Q Seats 9–10  avg $1,610/ea  total $3,220
Cheapest New: Sec 639 Row A Seats 10–11  avg $4,709/ea  total $9,418

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 3 groups, price range $2,875 – $4,025 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 629 Row K Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              6 | SKIP            |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

