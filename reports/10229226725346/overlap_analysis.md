## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 284 groups, price range $3,680 – $27,600 total
G4 fetched: 138 groups → 414 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   402 |       97.1% | May exist in G2, not top-100   |
| NEW        |    12 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 133 Row HH Seats 12–13  avg $2,163/ea  total $4,326
Cheapest New: Sec 131 Row P Seats 7–8  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $3,680): 0

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 85 groups, price range $3,382 – $69,000 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 529 Row L Seats 12–13  avg $1,955/ea  total $3,910
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 31 groups, price range $3,795 – $27,600 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       85.7% | May exist in G2, not top-100   |
| NEW        |     6 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 641 Row K Seats 22–23  avg $2,299/ea  total $4,598
Cheapest New: Sec 627 Row D Seats 2–3  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $3,795): 3

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 4 groups, price range $3,678 – $28,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 750 Row P Seats 14–15  avg $1,955/ea  total $3,910
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            402 | DERIVE          |
| Cat 2    |       0.0% |         0 |            120 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             36 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

