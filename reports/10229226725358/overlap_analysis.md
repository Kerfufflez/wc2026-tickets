## Category 1 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 122 groups, price range $8,970 – $89,865 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       92.9% | May exist in G2, not top-100   |
| NEW        |     6 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 33 Seats 17–18  avg $4,623/ea  total $9,246
Cheapest New: Sec 121 Row 12 Seats 6–7  avg $115,000/ea  total $230,000

Pairs eligible for merge (NEW below G2 min $8,970): 0

## Category 2 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 165 groups, price range $6,773 – $115,000 total
G4 fetched: 43 groups → 129 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   129 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 26 Seats 13–14  avg $3,565/ea  total $7,130
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 179 groups, price range $5,692 – $57,500 total
G4 fetched: 54 groups → 162 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   162 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 23 Seats 5–6  avg $3,094/ea  total $6,188
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 12 groups, price range $9,200 – $80,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 27 Seats 7–8  avg $6,601/ea  total $13,202
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             78 | DERIVE          |
| Cat 2    |       0.0% |         0 |            129 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            162 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

