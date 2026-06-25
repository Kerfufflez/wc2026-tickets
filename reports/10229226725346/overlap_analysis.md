## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 224 groups, price range $4,600 – $34,500 total
G4 fetched: 113 groups → 339 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   333 |       98.2% | May exist in G2, not top-100   |
| NEW        |     6 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row R Seats 1–2  avg $2,616/ea  total $5,232
Cheapest New: Sec 349 Row A Seats 1–2  avg $28,175/ea  total $56,350

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 65 groups, price range $4,600 – $69,000 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 631 Row M Seats 21–22  avg $2,707/ea  total $5,414
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 22 groups, price range $4,247 – $27,600 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       92.3% | May exist in G2, not top-100   |
| NEW        |     3 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 641 Row K Seats 22–23  avg $2,299/ea  total $4,598
Cheapest New: Sec 625 Row E Seats 7–8  avg $14,375/ea  total $28,750

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 3 groups, price range $5,260 – $28,750 total
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
| Cat 1    |       0.0% |         6 |            333 | DERIVE          |
| Cat 2    |       0.0% |         0 |             99 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

