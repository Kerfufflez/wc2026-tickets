## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 345 groups, price range $1,495 – $23,000 total
G4 fetched: 163 groups → 489 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   483 |       98.8% | May exist in G2, not top-100   |
| NEW        |     6 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 326 Row H Seats 5–6  avg $899/ea  total $1,798
Cheapest New: Sec 131 Row P Seats 7–8  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $1,495): 0

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 119 groups, price range $1,271 – $23,000 total
G4 fetched: 43 groups → 129 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   129 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 519 Row F Seats 8–9  avg $690/ea  total $1,380
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 66 groups, price range $1,265 – $6,658 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       95.2% | May exist in G2, not top-100   |
| NEW        |     3 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 622 Row J Seats 17–18  avg $678/ea  total $1,356
Cheapest New: Sec 628 Row P Seats 1–2  avg $4,082/ea  total $8,164

## Category 4 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 4 groups, price range $2,300 – $4,025 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 718 Row P Seats 1–2  avg $1,361/ea  total $2,722
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            483 | DERIVE          |
| Cat 2    |       0.0% |         0 |            129 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

