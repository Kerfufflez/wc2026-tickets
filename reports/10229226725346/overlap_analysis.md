## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 239 groups, price range $3,997 – $27,600 total
G4 fetched: 121 groups → 363 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   357 |       98.3% | May exist in G2, not top-100   |
| NEW        |     6 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 119 Row F Seats 9–10  avg $2,242/ea  total $4,484
Cheapest New: Sec 349 Row A Seats 1–2  avg $28,175/ea  total $56,350

Pairs eligible for merge (NEW below G2 min $3,997): 0

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 70 groups, price range $4,106 – $69,000 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |       97.1% | May exist in G2, not top-100   |
| NEW        |     3 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 631 Row M Seats 21–22  avg $2,707/ea  total $5,414
Cheapest New: Sec 551 Row F Seats 9–10  avg $1,495/ea  total $2,990

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 24 groups, price range $4,239 – $27,600 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       84.6% | May exist in G2, not top-100   |
| NEW        |     6 |       15.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 641 Row K Seats 22–23  avg $2,299/ea  total $4,598
Cheapest New: Sec 629 Row F Seats 13–14  avg $1,725/ea  total $3,450

Pairs eligible for merge (NEW below G2 min $4,239): 3

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
| Cat 1    |       0.0% |         6 |            357 | DERIVE          |
| Cat 2    |       0.0% |         3 |            102 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             33 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

