## Category 1 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 515 groups, price range $3,450 – $81,052 total
G4 fetched: 303 groups → 909 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   900 |       99.0% | May exist in G2, not top-100   |
| NEW        |     9 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 250 Row 15 Seats 16–17  avg $1,748/ea  total $3,496
Cheapest New: Sec 230 Row 3 Seats 19–20  avg $43,700/ea  total $87,400

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 2 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 202 groups, price range $2,875 – $229,999 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 21 Seats 5–6  avg $1,449/ea  total $2,898
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 93 groups, price range $2,939 – $80,500 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 14 Seats 17–18  avg $1,598/ea  total $3,196
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 9 groups, price range $3,450 – $13,570 total
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
| Cat 1    |       0.0% |         9 |            900 | DERIVE          |
| Cat 2    |       0.0% |         0 |            231 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

