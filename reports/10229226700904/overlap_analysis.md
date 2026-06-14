## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 101 groups, price range $1,886 – $82,465 total
G4 fetched: 36 groups → 108 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 148 Row 30 Seats 8–9  avg $1,129/ea  total $2,258
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 69 groups, price range $1,725 – $13,800 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 23 Seats 13–14  avg $920/ea  total $1,840
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 25 groups, price range $1,825 – $4,140 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 347 Row 25 Seats 1–2  avg $1,029/ea  total $2,058
Cheapest New: Sec 303 Row 6 Seats 7–8  avg $11,500/ea  total $23,000

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 3 groups, price range $2,254 – $2,760 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 19 Seats 25–26  avg $1,201/ea  total $2,402
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            108 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             87 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

