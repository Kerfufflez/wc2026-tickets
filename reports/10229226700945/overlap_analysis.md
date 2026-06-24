## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 48 groups, price range $2,990 – $11,500 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 215 Row 8 Seats 5–6  avg $1,915/ea  total $3,830
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 33 groups, price range $2,415 – $5,750 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       71.4% | May exist in G2, not top-100   |
| NEW        |     6 |       28.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 417 Row 19 Seats 9–10  avg $1,494/ea  total $2,988
Cheapest New: Sec 452 Row 5 Seats 5–6  avg $1,150/ea  total $2,300

Pairs eligible for merge (NEW below G2 min $2,415): 3

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 5 groups, price range $2,300 – $2,875,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row 11 Seats 6–7  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             42 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             15 | DERIVE          |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

