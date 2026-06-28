## Category 1 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 156 groups, price range $6,785 – $57,500 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |       97.4% | May exist in G2, not top-100   |
| NEW        |     6 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 27 Seats 9–10  avg $3,438/ea  total $6,876
Cheapest New: Sec 129 Row 25 Seats 14–15  avg $3,162/ea  total $6,324

Pairs eligible for merge (NEW below G2 min $6,785): 3

## Category 2 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 167 groups, price range $5,336 – $230,000 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   237 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 18 Seats 1–2  avg $2,794/ea  total $5,588
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 56 groups, price range $5,060 – $30,590 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       96.8% | May exist in G2, not top-100   |
| NEW        |     3 |        3.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 18 Seats 25–26  avg $2,706/ea  total $5,412
Cheapest New: Sec 327 Row 23 Seats 14–15  avg $286,919/ea  total $573,838

## Category 4 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 7 groups, price range $6,636 – $69,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 19 Seats 9–10  avg $4,025/ea  total $8,050
Cheapest New: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            225 | DERIVE          |
| Cat 2    |       0.0% |         0 |            237 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             90 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

