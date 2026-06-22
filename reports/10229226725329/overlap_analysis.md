## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 122 groups, price range $3,946 – $1,426,000 total
G4 fetched: 52 groups → 156 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   156 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 137 Row 33 Seats 7–8  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 92 groups, price range $2,300 – $23,000 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 312 Row 12 Seats 17–18  avg $1,719/ea  total $3,438
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 4 groups, price range $4,140 – $5,750 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 13 Seats 5–6  avg $2,559/ea  total $5,118
Cheapest New: Sec 315 Row 18 Seats 5–6  avg $1,725/ea  total $3,450

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            156 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

