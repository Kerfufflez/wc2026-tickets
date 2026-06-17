## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 126 groups, price range $7,820 – $115,000 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   180 |       98.4% | May exist in G2, not top-100   |
| NEW        |     3 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 134 Row 23 Seats 13–14  avg $3,939/ea  total $7,878
Cheapest New: Sec 131 Row 17 Seats 1–2  avg $3,852/ea  total $7,704

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 57 groups, price range $6,210 – $46,000 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    96 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 341 Row 23 Seats 10–11  avg $3,278/ea  total $6,556
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 20 groups, price range $5,938 – $26,294 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 30 Seats 9–10  avg $4,370/ea  total $8,740
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 11 groups, price range $6,084 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 24 Seats 13–14  avg $3,220/ea  total $6,440
Cheapest New: Sec 308 Row 27 Seats 9–10  avg $34,500/ea  total $69,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            180 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             96 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

