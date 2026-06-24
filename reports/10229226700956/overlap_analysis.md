## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 30 groups, price range $2,852 – $11,500 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       84.6% | May exist in G2, not top-100   |
| NEW        |     6 |       15.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 108 Row 23 Seats 1–2  avg $1,438/ea  total $2,876
Cheapest New: Sec 107 Row 27 Seats 21–22  avg $690/ea  total $1,380

Pairs eligible for merge (NEW below G2 min $2,852): 6

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 32 groups, price range $1,840 – $10,350 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 18 Seats 13–14  avg $1,265/ea  total $2,530
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 10 groups, price range $1,955 – $4,255 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 213 Row 6 Seats 11–12  avg $1,552/ea  total $3,104
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             33 | DERIVE          |
| Cat 2    |       0.0% |         0 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

