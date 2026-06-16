## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 52 groups, price range $5,175 – $16,100 total
G4 fetched: 49 groups → 147 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |       98.0% | May exist in G2, not top-100   |
| NEW        |     3 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 250 Row 10 Seats 7–8  avg $2,721/ea  total $5,442
Cheapest New: Sec 126 Row 13 Seats 9–10  avg $17,250/ea  total $34,500

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 35 groups, price range $4,483 – $43,068 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 28 Seats 17–18  avg $2,299/ea  total $4,598
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 8 groups, price range $4,577 – $6,900 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 27 Seats 9–10  avg $2,556/ea  total $5,112
Cheapest New: Sec 302 Row 25 Seats 9–10  avg $4,715/ea  total $9,430

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            144 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             42 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

