## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 108 groups, price range $3,908 – $57,500 total
G4 fetched: 101 groups → 303 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   300 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 31 Seats 25–26  avg $2,009/ea  total $4,018
Cheapest New: Sec 128 Row 37 Seats 8–9  avg $412,275/ea  total $824,550

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 161 groups, price range $2,760 – $23,000 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |       97.5% | May exist in G2, not top-100   |
| NEW        |     6 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 26 Seats 16–17  avg $1,409/ea  total $2,818
Cheapest New: Sec 333 Row 18 Seats 17–18  avg $978/ea  total $1,956

Pairs eligible for merge (NEW below G2 min $2,760): 6

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 43 groups, price range $2,872 – $20,442 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 9 Seats 9–10  avg $1,455/ea  total $2,910
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $2,932 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 21 Seats 11–12  avg $1,485/ea  total $2,970
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            300 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            231 | DERIVE          |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

