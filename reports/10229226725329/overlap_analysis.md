## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 100 groups, price range $3,243 – $1,426,000 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |       96.6% | May exist in G2, not top-100   |
| NEW        |     6 |        3.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row 21 Seats 9–10  avg $1,668/ea  total $3,336
Cheapest New: Sec 124 Row 16 Seats 13–14  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $3,243): 6

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 87 groups, price range $2,555 – $23,000 total
G4 fetched: 51 groups → 153 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   153 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 338 Row 5 Seats 1–2  avg $1,360/ea  total $2,720
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $2,760 – $8,050 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 18 Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            171 | DERIVE          |
| Cat 2    |       0.0% |         0 |            153 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

