## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 100 groups, price range $5,405 – $45,655 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 29 Seats 9–10  avg $2,864/ea  total $5,728
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 67 groups, price range $4,598 – $27,600 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       89.7% | May exist in G2, not top-100   |
| NEW        |     9 |       10.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 18 Seats 18–19  avg $2,415/ea  total $4,830
Cheapest New: Sec 342 Row 26 Seats 21–22  avg $2,168/ea  total $4,336

Pairs eligible for merge (NEW below G2 min $4,598): 6

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 53 groups, price range $4,255 – $23,000 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       96.4% | May exist in G2, not top-100   |
| NEW        |     3 |        3.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 19 Seats 1–2  avg $2,128/ea  total $4,256
Cheapest New: Sec 348 Row 23 Seats 17–18  avg $2,042/ea  total $4,084

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            141 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |             78 | DERIVE          |
| Cat 3    |       0.0% |         3 |             81 | INVESTIGATE     |

Overall recommendation: **DERIVE**

