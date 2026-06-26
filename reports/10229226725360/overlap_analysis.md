## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 28 groups, price range $53,705 – $2,527,700 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 15 Seats 9–10  avg $27,140/ea  total $54,280
Cheapest New: Sec 103 Row 45 Seats 10–11  avg $25,300/ea  total $50,600

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 29 groups, price range $35,650 – $511,750 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 24 Seats 1–2  avg $18,975/ea  total $37,950
Cheapest New: Sec 319 Row 18 Seats 13–14  avg $15,984/ea  total $31,968

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 18 groups, price range $31,625 – $356,500 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 22 Seats 1–2  avg $17,250/ea  total $34,500
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 6 groups, price range $34,500 – $63,284 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 20 Seats 1–2  avg $17,250/ea  total $34,500
Cheapest New: Sec 331 Row 22 Seats 21–22  avg $33,350/ea  total $66,700

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             12 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             30 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

