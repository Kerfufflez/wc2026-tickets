## Category 1 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 119 groups, price range $9,994 – $89,916 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       92.6% | May exist in G2, not top-100   |
| NEW        |     6 |        7.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 33 Seats 17–18  avg $6,118/ea  total $12,236
Cheapest New: Sec 121 Row 12 Seats 6–7  avg $115,000/ea  total $230,000

Pairs eligible for merge (NEW below G2 min $9,994): 0

## Category 2 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 159 groups, price range $6,670 – $115,000 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   135 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 26 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 184 groups, price range $5,865 – $57,500 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   147 |       98.0% | May exist in G2, not top-100   |
| NEW        |     3 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row 21 Seats 17–18  avg $3,256/ea  total $6,512
Cheapest New: Sec 349 Row 23 Seats 1–2  avg $2,875/ea  total $5,750

## Category 4 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 16 groups, price range $5,750 – $80,500 total
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
| Cat 1    |       0.0% |         6 |             75 | DERIVE          |
| Cat 2    |       0.0% |         0 |            135 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            147 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

