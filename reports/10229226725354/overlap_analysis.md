## Category 1 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 187 groups, price range $8,614 – $623,126 total
G4 fetched: 56 groups → 168 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   168 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 18 Seats 4–5  avg $4,775/ea  total $9,550
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 275 groups, price range $6,601 – $46,000 total
G4 fetched: 111 groups → 333 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   327 |       98.2% | May exist in G2, not top-100   |
| NEW        |     6 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row 5 Seats 6–7  avg $3,383/ea  total $6,766
Cheapest New: Sec 352 Row 4 Seats 13–14  avg $25,875/ea  total $51,750

Pairs eligible for merge (NEW below G2 min $6,601): 0

## Category 3 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 71 groups, price range $6,210 – $46,000 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 532 Row 21 Seats 17–18  avg $3,680/ea  total $7,360
Cheapest New: Sec 548 Row 21 Seats 13–14  avg $28,750/ea  total $57,500

## Category 4 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 4 groups, price range $7,015 – $18,400 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 526 Row 16 Seats 5–6  avg $6,900/ea  total $13,800
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            168 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            327 | DERIVE          |
| Cat 3    |       0.0% |         3 |             57 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

