## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 37 groups, price range $4,370 – $19,755 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 430 Row 6 Seats 14–15  avg $2,358/ea  total $4,716
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 7 groups, price range $5,049 – $10,281 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       44.4% | May exist in G2, not top-100   |
| NEW        |    15 |       55.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec PC02 Row 1 Seats 6–7  avg $2,588/ea  total $5,176
Cheapest New: Sec 518 Row 7 Seats 5–6  avg $2,012/ea  total $4,024

Pairs eligible for merge (NEW below G2 min $5,049): 9

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 12 groups, price range $3,306 – $9,731 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 644 Row 3 Seats 1–2  avg $2,530/ea  total $5,060
Cheapest New: Sec 641 Row 1 Seats 7–8  avg $23,184/ea  total $46,368

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 2 groups, price range $3,680 – $4,945 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 618 Row 5 Seats 13–14  avg $2,300/ea  total $4,600
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             42 | INVESTIGATE     |
| Cat 2    |       0.0% |        15 |             12 | DERIVE          |
| Cat 3    |       0.0% |         3 |              6 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

