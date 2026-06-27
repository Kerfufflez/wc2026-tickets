## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 147 groups, price range $6,785 – $69,000 total
G4 fetched: 62 groups → 186 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |       98.4% | May exist in G2, not top-100   |
| NEW        |     3 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 128 Row 21 Seats 16–17  avg $3,450/ea  total $6,900
Cheapest New: Sec 114 Row 29 Seats 1–2  avg $3,324/ea  total $6,648

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 113 groups, price range $5,748 – $115,000 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |       95.0% | May exist in G2, not top-100   |
| NEW        |     6 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 242 Row 9 Seats 21–22  avg $2,973/ea  total $5,946
Cheapest New: Sec 205 Row 24 Seats 9–10  avg $2,789/ea  total $5,578

Pairs eligible for merge (NEW below G2 min $5,748): 3

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 49 groups, price range $5,508 – $27,140 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 237 Row 26 Seats 17–18  avg $3,278/ea  total $6,556
Cheapest New: Sec 206 Row 29 Seats 17–18  avg $2,754/ea  total $5,508

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 6 groups, price range $6,210 – $9,198 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 29 Seats 9–10  avg $3,245/ea  total $6,490
Cheapest New: Sec 207 Row 25 Seats 19–20  avg $2,760/ea  total $5,520

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            183 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            114 | DERIVE          |
| Cat 3    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

