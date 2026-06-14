## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 103 groups, price range $598 – $10,350 total
G4 fetched: 156 groups → 468 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   462 |       98.7% | May exist in G2, not top-100   |
| NEW        |     6 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 110 Row 18 Seats 29–30  avg $330/ea  total $660
Cheapest New: Sec 110 Row 13 Seats 13–14  avg $288/ea  total $576

Pairs eligible for merge (NEW below G2 min $598): 3

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 163 groups, price range $540 – $8,050 total
G4 fetched: 120 groups → 360 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   360 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 23 Seats 4–5  avg $299/ea  total $598
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 85 groups, price range $448 – $3,565 total
G4 fetched: 42 groups → 126 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |       97.6% | May exist in G2, not top-100   |
| NEW        |     3 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 26 Seats 13–14  avg $229/ea  total $458
Cheapest New: Sec 237 Row 17 Seats 1–2  avg $224/ea  total $448

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 8 groups, price range $460 – $1,035 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 231 Row 22 Seats 1–2  avg $282/ea  total $564
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            462 | DERIVE          |
| Cat 2    |       0.0% |         0 |            360 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            123 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

