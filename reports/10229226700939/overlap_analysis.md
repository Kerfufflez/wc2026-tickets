## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 10 groups, price range $1,610 – $2,645 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       50.0% | May exist in G2, not top-100   |
| NEW        |    12 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row DD Seats 1–2  avg $920/ea  total $1,840
Cheapest New: Sec 127 Row T Seats 3–4  avg $804/ea  total $1,608

Pairs eligible for merge (NEW below G2 min $1,610): 3

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 8 groups, price range $1,608 – $8,032 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row O Seats 11–12  avg $978/ea  total $1,956
Cheapest New: Sec 129 Row E Seats 9–10  avg $688/ea  total $1,376

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 11 groups, price range $1,276 – $8,395 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row AA Seats 13–14  avg $877/ea  total $1,754
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |             12 | DERIVE          |
| Cat 2    |       0.0% |         3 |              6 | SKIP            |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

