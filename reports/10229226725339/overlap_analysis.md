## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 124 groups, price range $2,936 – $230,000 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 238 Row 2 Seats 5–6  avg $1,719/ea  total $3,438
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 151 groups, price range $1,996 – $18,998 total
G4 fetched: 133 groups → 399 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   390 |       97.7% | May exist in G2, not top-100   |
| NEW        |     9 |        2.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 8 Seats 10–11  avg $1,029/ea  total $2,058
Cheapest New: Sec 511 Row 7 Seats 11–12  avg $11,500/ea  total $23,000

Pairs eligible for merge (NEW below G2 min $1,996): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 26 groups, price range $2,047 – $11,500 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       93.8% | May exist in G2, not top-100   |
| NEW        |     3 |        6.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 507 Row 5 Seats 6–7  avg $1,121/ea  total $2,242
Cheapest New: Sec 527 Row 7 Seats 4–5  avg $1,018/ea  total $2,036

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            258 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            390 | DERIVE          |
| Cat 3    |       0.0% |         3 |             45 | INVESTIGATE     |

Overall recommendation: **DERIVE**

