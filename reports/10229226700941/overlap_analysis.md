## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 90 groups, price range $2,143 – $37,919 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |       96.6% | May exist in G2, not top-100   |
| NEW        |     3 |        3.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 202 Row RR Seats 9–10  avg $1,072/ea  total $2,144
Cheapest New: Sec 253 Row OO Seats 5–6  avg $1,041/ea  total $2,082

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 49 groups, price range $1,814 – $5,770 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       88.9% | May exist in G2, not top-100   |
| NEW        |     3 |       11.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 408 Row JJ Seats 2–3  avg $978/ea  total $1,956
Cheapest New: Sec 436 Row PP Seats 2–3  avg $103,040/ea  total $206,080

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 12 groups, price range $2,061 – $6,898 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 423 Row ZZ Seats 2–3  avg $1,236/ea  total $2,472
Cheapest New: Sec 425 Row CC Seats 101–102  avg $4,122/ea  total $8,244

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             84 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

