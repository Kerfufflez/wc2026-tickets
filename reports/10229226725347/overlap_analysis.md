## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 179 groups, price range $5,750 – $57,500 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   303 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 16 Seats 1–2  avg $2,886/ea  total $5,772
Cheapest New: Sec 104 Row 43 Seats 17–18  avg $57,499/ea  total $114,998

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 189 groups, price range $4,554 – $230,000 total
G4 fetched: 95 groups → 285 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   282 |       98.9% | May exist in G2, not top-100   |
| NEW        |     3 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 19 Seats 17–18  avg $2,530/ea  total $5,060
Cheapest New: Sec 308 Row 19 Seats 13–14  avg $1,794/ea  total $3,588

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 76 groups, price range $3,990 – $69,000 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 23 Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 10 groups, price range $4,600 – $69,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            303 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            282 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             99 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

