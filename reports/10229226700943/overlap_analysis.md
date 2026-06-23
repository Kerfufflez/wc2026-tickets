## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 20 groups, price range $1,610 – $2,990 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       92.3% | May exist in G2, not top-100   |
| NEW        |     3 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 111 Row 15 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: Sec 136 Row 16 Seats 11–12  avg $3,450/ea  total $6,900

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 29 groups, price range $1,167 – $4,600 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       71.4% | May exist in G2, not top-100   |
| NEW        |     6 |       28.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec M11 Row 18 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 124 Row 33 Seats 4–5  avg $2,645/ea  total $5,290

Pairs eligible for merge (NEW below G2 min $1,167): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 20 groups, price range $1,150 – $3,565 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       93.8% | May exist in G2, not top-100   |
| NEW        |     3 |        6.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 221 Row 16 Seats 23–24  avg $620/ea  total $1,240
Cheapest New: Sec 218 Row 11 Seats 1–2  avg $2,300/ea  total $4,600

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 2 groups, price range $1,610 – $1,725 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 28 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             15 | DERIVE          |
| Cat 3    |       0.0% |         3 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

