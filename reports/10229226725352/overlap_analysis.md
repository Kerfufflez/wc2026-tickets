## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 184 groups, price range $3,775 – $81,900 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       97.3% | May exist in G2, not top-100   |
| NEW        |     6 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 204 Row BB Seats 105–106  avg $1,998/ea  total $3,996
Cheapest New: Sec 224 Row FF Seats 5–6  avg $76,666/ea  total $153,332

Pairs eligible for merge (NEW below G2 min $3,775): 0

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 122 groups, price range $3,118 – $19,329 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   105 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 407 Row MM Seats 1–2  avg $1,805/ea  total $3,610
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 25 groups, price range $3,862 – $24,619 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |       87.5% | May exist in G2, not top-100   |
| NEW        |     6 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 426 Row NN Seats 3–4  avg $2,052/ea  total $4,104
Cheapest New: Sec 454 Row NN Seats 102–103  avg $1,801/ea  total $3,602

Pairs eligible for merge (NEW below G2 min $3,862): 6

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 2 groups, price range $4,842 – $10,010 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 428 Row ZZ Seats 1–2  avg $2,271/ea  total $4,542

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            219 | DERIVE          |
| Cat 2    |       0.0% |         0 |            105 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             42 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

