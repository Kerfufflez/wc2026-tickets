## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 135 groups, price range $1,955 – $50,600 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 29 Seats 5–6  avg $1,035/ea  total $2,070
Cheapest New: Sec 122 Row 37 Seats 31–32  avg $966/ea  total $1,932

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 120 groups, price range $1,150 – $13,800 total
G4 fetched: 74 groups → 222 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 26 Seats 15–16  avg $804/ea  total $1,608
Cheapest New: Sec 308 Row 13 Seats 9–10  avg $11,500/ea  total $23,000

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 54 groups, price range $1,495 – $10,810 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 24 Seats 9–10  avg $805/ea  total $1,610
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 4 groups, price range $1,552 – $2,300 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 312 Row 29 Seats 13–14  avg $2,242/ea  total $4,484

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            234 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            219 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

