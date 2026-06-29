## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 142 groups, price range $6,785 – $57,500 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 34 Seats 1–2  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 79 groups, price range $5,750 – $57,500 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       95.1% | May exist in G2, not top-100   |
| NEW        |     6 |        4.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 20 Seats 17–18  avg $2,990/ea  total $5,980
Cheapest New: Sec 313 Row 12 Seats 11–12  avg $2,702/ea  total $5,404

Pairs eligible for merge (NEW below G2 min $5,750): 6

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 80 groups, price range $4,370 – $24,610 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   111 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 9 Seats 9–10  avg $2,530/ea  total $5,060
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 8 groups, price range $6,900 – $20,700 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 33 Seats 6–7  avg $4,600/ea  total $9,200
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            201 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            117 | DERIVE          |
| Cat 3    |       0.0% |         0 |            111 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

