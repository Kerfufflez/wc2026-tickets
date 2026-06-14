## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 43 groups, price range $4,285 – $27,600 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 464 Row 6 Seats 6–7  avg $2,644/ea  total $5,288
Cheapest New: Sec 116 Row 22 Seats 7–8  avg $17,250/ea  total $34,500

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 18 groups, price range $4,428 – $16,330 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 534 Row 7 Seats 14–15  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 14 groups, price range $4,301 – $13,225 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 638 Row 7 Seats 21–22  avg $2,294/ea  total $4,588
Cheapest New: Sec 665 Row 9 Seats 17–18  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $4,301): 0

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 4 groups, price range $4,600 – $15,556 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 601 Row 8 Seats 14–15  avg $2,956/ea  total $5,912
Cheapest New: Sec 635 Row 5 Seats 16–17  avg $2,185/ea  total $4,370

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

