## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 102 groups, price range $677 – $10,350 total
G4 fetched: 149 groups → 447 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   441 |       98.7% | May exist in G2, not top-100   |
| NEW        |     6 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 111 Row 15 Seats 25–26  avg $343/ea  total $686
Cheapest New: Sec 110 Row 18 Seats 29–30  avg $330/ea  total $660

Pairs eligible for merge (NEW below G2 min $677): 3

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 153 groups, price range $575 – $4,600 total
G4 fetched: 115 groups → 345 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   339 |       98.3% | May exist in G2, not top-100   |
| NEW        |     6 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 23 Seats 4–5  avg $299/ea  total $598
Cheapest New: Sec C26 Row 1 Seats 17–18  avg $2,414/ea  total $4,828

Pairs eligible for merge (NEW below G2 min $575): 0

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 72 groups, price range $495 – $3,565 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       96.8% | May exist in G2, not top-100   |
| NEW        |     3 |        3.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 222 Row 30 Seats 18–19  avg $259/ea  total $518
Cheapest New: Sec 228 Row 24 Seats 17–18  avg $247/ea  total $494

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 9 groups, price range $601 – $1,228 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 239 Row 27 Seats 17–18  avg $401/ea  total $802
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            441 | DERIVE          |
| Cat 2    |       0.0% |         6 |            339 | DERIVE          |
| Cat 3    |       0.0% |         3 |             90 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

