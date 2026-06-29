## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 147 groups, price range $4,542 – $57,500 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row 25 Seats 7–8  avg $3,317/ea  total $6,634
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 83 groups, price range $5,635 – $57,500 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   126 |       93.3% | May exist in G2, not top-100   |
| NEW        |     9 |        6.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 6 Seats 3–4  avg $2,990/ea  total $5,980
Cheapest New: Sec 311 Row 1 Seats 10–11  avg $2,530/ea  total $5,060

Pairs eligible for merge (NEW below G2 min $5,635): 9

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 85 groups, price range $4,945 – $34,500 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |       97.3% | May exist in G2, not top-100   |
| NEW        |     3 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 9 Seats 9–10  avg $2,530/ea  total $5,060
Cheapest New: Sec 318 Row 24 Seats 1–2  avg $2,392/ea  total $4,784

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 8 groups, price range $6,900 – $20,700 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 33 Seats 6–7  avg $4,600/ea  total $9,200
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            204 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            126 | DERIVE          |
| Cat 3    |       0.0% |         3 |            108 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

