## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 120 groups, price range $690 – $230,000 total
G4 fetched: 174 groups → 522 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   513 |       98.3% | May exist in G2, not top-100   |
| NEW        |     9 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row S Seats 1–2  avg $402/ea  total $804
Cheapest New: Sec 115 Row V Seats 13–14  avg $288/ea  total $576

Pairs eligible for merge (NEW below G2 min $690): 9

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 140 groups, price range $575 – $6,900 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 352 Row F Seats 13–14  avg $339/ea  total $678
Cheapest New: Sec 352 Row P Seats 9–10  avg $230/ea  total $460

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 39 groups, price range $391 – $4,922 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 616 Row N Seats 3–4  avg $218/ea  total $436
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 5 groups, price range $642 – $16,100 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 617 Row A Seats 1–2  avg $690/ea  total $1,380
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            513 | DERIVE          |
| Cat 2    |       0.0% |         3 |            234 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

