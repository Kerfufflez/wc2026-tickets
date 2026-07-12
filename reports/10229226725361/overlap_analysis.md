## Category 1 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 517 groups, price range $3,218 – $81,650 total
G4 fetched: 283 groups → 849 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   840 |       98.9% | May exist in G2, not top-100   |
| NEW        |     9 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 5 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 230 Row 3 Seats 19–20  avg $43,700/ea  total $87,400

Pairs eligible for merge (NEW below G2 min $3,218): 0

## Category 2 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 209 groups, price range $2,875 – $229,999 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 21 Seats 5–6  avg $1,449/ea  total $2,898
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 85 groups, price range $2,875 – $80,500 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 18 Seats 17–18  avg $1,495/ea  total $2,990
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 8 groups, price range $3,450 – $13,570 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 25–26  avg $1,955/ea  total $3,910
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            840 | DERIVE          |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

