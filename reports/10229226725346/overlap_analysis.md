## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 212 groups, price range $5,152 – $34,500 total
G4 fetched: 99 groups → 297 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   291 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row R Seats 1–2  avg $2,616/ea  total $5,232
Cheapest New: Sec 349 Row A Seats 1–2  avg $28,175/ea  total $56,350

Pairs eligible for merge (NEW below G2 min $5,152): 0

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 54 groups, price range $4,920 – $69,000 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |       96.6% | May exist in G2, not top-100   |
| NEW        |     3 |        3.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 631 Row M Seats 21–22  avg $2,707/ea  total $5,414
Cheapest New: Sec 630 Row L Seats 12–13  avg $2,179/ea  total $4,358

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 22 groups, price range $4,247 – $23,000 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 641 Row K Seats 22–23  avg $2,299/ea  total $4,598
Cheapest New: Sec 625 Row E Seats 7–8  avg $14,375/ea  total $28,750

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 3 groups, price range $4,830 – $28,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 750 Row P Seats 14–15  avg $2,645/ea  total $5,290
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            291 | DERIVE          |
| Cat 2    |       0.0% |         3 |             84 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

