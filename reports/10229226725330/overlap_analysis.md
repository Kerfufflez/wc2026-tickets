## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 20 groups, price range $4,600 – $13,110 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 113 Row X Seats 5–6  avg $2,875/ea  total $5,750
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 7 groups, price range $4,600 – $8,057 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 240 Row AA Seats 8–9  avg $2,530/ea  total $5,060
Cheapest New: Sec 215 Row U Seats 1–2  avg $4,645/ea  total $9,290

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 7 groups, price range $5,140 – $27,600 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 230 Row J Seats 7–8  avg $2,731/ea  total $5,462
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |              6 | DERIVE          |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

