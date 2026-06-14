## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 140 groups, price range $2,139 – $50,600 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       96.5% | May exist in G2, not top-100   |
| NEW        |     9 |        3.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 122 Row 22 Seats 10–11  avg $1,092/ea  total $2,184
Cheapest New: Sec 122 Row 37 Seats 31–32  avg $966/ea  total $1,932

Pairs eligible for merge (NEW below G2 min $2,139): 9

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 124 groups, price range $1,495 – $13,800 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   222 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 26 Seats 15–16  avg $804/ea  total $1,608
Cheapest New: Sec 308 Row 13 Seats 9–10  avg $11,500/ea  total $23,000

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 59 groups, price range $1,495 – $10,810 total
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
Date: June 14, 2026

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
| Cat 1    |       0.0% |         9 |            246 | DERIVE          |
| Cat 2    |       0.0% |         3 |            222 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

