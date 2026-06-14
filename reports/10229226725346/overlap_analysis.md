## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 239 groups, price range $2,404 – $27,600 total
G4 fetched: 177 groups → 531 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   525 |       98.9% | May exist in G2, not top-100   |
| NEW        |     6 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 348 Row G Seats 5–6  avg $1,357/ea  total $2,714
Cheapest New: Sec 121 Row EE Seats 19–20  avg $21,321/ea  total $42,642

Pairs eligible for merge (NEW below G2 min $2,404): 0

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 77 groups, price range $1,979 – $17,250 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 637 Row Q Seats 9–10  avg $1,041/ea  total $2,082
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 26 groups, price range $2,185 – $23,000 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       69.2% | May exist in G2, not top-100   |
| NEW        |    12 |       30.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 625 Row L Seats 10–11  avg $1,144/ea  total $2,288
Cheapest New: Sec 622 Row L Seats 13–14  avg $1,035/ea  total $2,070

Pairs eligible for merge (NEW below G2 min $2,185): 9

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 5 groups, price range $2,760 – $28,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 750 Row P Seats 14–15  avg $1,495/ea  total $2,990
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            525 | DERIVE          |
| Cat 2    |       0.0% |         0 |            117 | INVESTIGATE     |
| Cat 3    |       0.0% |        12 |             27 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

