## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 151 groups, price range $6,785 – $69,000 total
G4 fetched: 62 groups → 186 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |       98.4% | May exist in G2, not top-100   |
| NEW        |     3 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 111 Row 34 Seats 7–8  avg $3,450/ea  total $6,900
Cheapest New: Sec 114 Row 29 Seats 1–2  avg $3,324/ea  total $6,648

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 120 groups, price range $5,502 – $115,000 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       97.5% | May exist in G2, not top-100   |
| NEW        |     3 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row 24 Seats 9–10  avg $2,789/ea  total $5,578
Cheapest New: Sec C18 Row 10 Seats 9–10  avg $86,250/ea  total $172,500

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 50 groups, price range $4,600 – $27,140 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 29 Seats 17–18  avg $2,754/ea  total $5,508
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 7 groups, price range $6,210 – $11,040 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 29 Seats 9–10  avg $3,237/ea  total $6,474
Cheapest New: Sec 207 Row 25 Seats 19–20  avg $2,760/ea  total $5,520

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            183 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            117 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             27 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

