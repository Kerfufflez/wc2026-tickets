## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 249 groups, price range $6,555 – $345,000 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   303 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 127 Row 10 Seats 12–13  avg $3,837/ea  total $7,674
Cheapest New: Sec 107 Row 24 Seats 17–18  avg $2,932/ea  total $5,864

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 186 groups, price range $5,060 – $80,500 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row 36 Seats 13–14  avg $2,760/ea  total $5,520
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 92 groups, price range $4,600 – $57,500 total
G4 fetched: 43 groups → 129 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |       95.3% | May exist in G2, not top-100   |
| NEW        |     6 |        4.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 337 Row 7 Seats 16–17  avg $2,818/ea  total $5,636
Cheapest New: Sec 317 Row 27 Seats 11–12  avg $40,865/ea  total $81,730

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            303 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            258 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            123 | DERIVE          |

Overall recommendation: **DERIVE**

