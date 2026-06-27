## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 152 groups, price range $6,785 – $57,500 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |       96.2% | May exist in G2, not top-100   |
| NEW        |     9 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 106 Row 29 Seats 9–10  avg $3,641/ea  total $7,282
Cheapest New: Sec 129 Row 25 Seats 14–15  avg $3,162/ea  total $6,324

Pairs eligible for merge (NEW below G2 min $6,785): 6

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 169 groups, price range $5,290 – $230,000 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 19 Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 57 groups, price range $4,577 – $30,590 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |       96.6% | May exist in G2, not top-100   |
| NEW        |     3 |        3.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row 21 Seats 1–2  avg $2,875/ea  total $5,750
Cheapest New: Sec 327 Row 23 Seats 14–15  avg $286,919/ea  total $573,838

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

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
| Cat 1    |       0.0% |         9 |            225 | DERIVE          |
| Cat 2    |       0.0% |         0 |            231 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             84 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

