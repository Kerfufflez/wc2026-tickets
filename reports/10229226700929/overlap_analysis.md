## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 110 groups, price range $1,838 – $41,216 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |       97.3% | May exist in G2, not top-100   |
| NEW        |     3 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 148 Row 36 Seats 24–25  avg $999/ea  total $1,998
Cheapest New: Sec 129 Row 25 Seats 26–27  avg $886/ea  total $1,772

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 64 groups, price range $1,564 – $6,900 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 1 Seats 11–12  avg $978/ea  total $1,956
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 27 groups, price range $1,208 – $6,900 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 12 Seats 23–24  avg $805/ea  total $1,610
Cheapest New: Sec 324 Row 24 Seats 18–19  avg $4,830/ea  total $9,660

Pairs eligible for merge (NEW below G2 min $1,208): 0

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 1 groups, price range $1,838 – $1,838 total
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
Cheapest New: Sec 346 Row 20 Seats 17–18  avg $805/ea  total $1,610

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            108 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             78 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

