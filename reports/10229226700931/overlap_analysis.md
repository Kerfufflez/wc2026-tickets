## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 52 groups, price range $3,968 – $27,600 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row 6 Seats 21–22  avg $2,530/ea  total $5,060
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 39 groups, price range $2,875 – $13,225 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |       93.3% | May exist in G2, not top-100   |
| NEW        |     3 |        6.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 434 Row 2 Seats 17–18  avg $1,725/ea  total $3,450
Cheapest New: Sec 406 Row 4 Seats 11–12  avg $8,247/ea  total $16,494

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 22 groups, price range $2,875 – $103,500 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 450 Row 22 Seats 20–21  avg $1,725/ea  total $3,450
Cheapest New: Sec 422 Row 16 Seats 10–11  avg $1,062,600/ea  total $2,125,200

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             51 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             42 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

