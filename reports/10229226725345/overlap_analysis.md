## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 247 groups, price range $2,530 – $69,000 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   306 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 114 Row 9 Seats 1–2  avg $1,615/ea  total $3,230
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 193 groups, price range $1,840 – $34,500 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   180 |       95.2% | May exist in G2, not top-100   |
| NEW        |     9 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 16 Seats 15–16  avg $1,354/ea  total $2,708
Cheapest New: Sec 227 Row 25 Seats 17–18  avg $748/ea  total $1,496

Pairs eligible for merge (NEW below G2 min $1,840): 3

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 87 groups, price range $1,886 – $27,140 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 214 Row 19 Seats 13–14  avg $1,265/ea  total $2,530
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 10 groups, price range $1,955 – $11,040 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 29 Seats 9–10  avg $2,185/ea  total $4,370
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            306 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            180 | DERIVE          |
| Cat 3    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

