## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 354 groups, price range $1,380 – $18,170 total
G4 fetched: 148 groups → 444 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   441 |       99.3% | May exist in G2, not top-100   |
| NEW        |     3 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 239 Row 11 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 231 Row 20 Seats 1–2  avg $23,000/ea  total $46,000

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 277 groups, price range $1,084 – $8,740 total
G4 fetched: 136 groups → 408 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   402 |       98.5% | May exist in G2, not top-100   |
| NEW        |     6 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 513 Row 9 Seats 10–11  avg $605/ea  total $1,210
Cheapest New: Sec 303 Row 2 Seats 1–2  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $1,084): 0

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 81 groups, price range $1,035 – $8,050 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 547 Row 20 Seats 1–2  avg $529/ea  total $1,058
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            441 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            402 | DERIVE          |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |

Overall recommendation: **DERIVE**

