## Category 1 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 518 groups, price range $3,220 – $81,650 total
G4 fetched: 289 groups → 867 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   858 |       99.0% | May exist in G2, not top-100   |
| NEW        |     9 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 5 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 230 Row 3 Seats 19–20  avg $43,700/ea  total $87,400

Pairs eligible for merge (NEW below G2 min $3,220): 0

## Category 2 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 209 groups, price range $2,760 – $229,999 total
G4 fetched: 82 groups → 246 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   243 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row 28 Seats 18–19  avg $1,610/ea  total $3,220
Cheapest New: Sec 323 Row 20 Seats 8–9  avg $1,265/ea  total $2,530

## Category 3 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 85 groups, price range $2,588 – $80,500 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row 20 Seats 5–6  avg $1,305/ea  total $2,610
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 6 groups, price range $3,450 – $13,570 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 25–26  avg $1,955/ea  total $3,910
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            858 | DERIVE          |
| Cat 2    |       0.0% |         3 |            243 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             90 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

