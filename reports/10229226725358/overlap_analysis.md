## Category 1 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 132 groups, price range $8,740 – $90,057 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       96.7% | May exist in G2, not top-100   |
| NEW        |     3 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 33 Seats 17–18  avg $5,210/ea  total $10,420
Cheapest New: Sec 120 Row 36 Seats 4–5  avg $172,500/ea  total $345,000

## Category 2 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 168 groups, price range $5,980 – $115,000 total
G4 fetched: 46 groups → 138 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   138 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 22 Seats 17–18  avg $3,242/ea  total $6,484
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 185 groups, price range $5,520 – $57,500 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 20 Seats 13–14  avg $2,760/ea  total $5,520
Cheapest New: Sec 329 Row 16 Seats 14–15  avg $2,500/ea  total $5,000

## Category 4 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 15 groups, price range $6,900 – $80,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 27 Seats 7–8  avg $6,601/ea  total $13,202
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             87 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            138 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            174 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

