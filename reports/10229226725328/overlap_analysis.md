## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 184 groups, price range $2,174 – $52,900 total
G4 fetched: 101 groups → 303 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   303 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 18 Seats 5–6  avg $1,144/ea  total $2,288
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 217 groups, price range $1,725 – $16,100 total
G4 fetched: 153 groups → 459 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   447 |       97.4% | May exist in G2, not top-100   |
| NEW        |    12 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 519 Row 21 Seats 19–20  avg $903/ea  total $1,806
Cheapest New: Sec 543 Row 12 Seats 10–11  avg $8,625/ea  total $17,250

Pairs eligible for merge (NEW below G2 min $1,725): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 42 groups, price range $1,597 – $46,552 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 551 Row 11 Seats 1–2  avg $816/ea  total $1,632
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 2 groups, price range $2,300 – $2,760 total
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
Cheapest New: Sec 525 Row 12 Seats 3–4  avg $1,840/ea  total $3,680

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            303 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |            447 | DERIVE          |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

