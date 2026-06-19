## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 43 groups, price range $5,060 – $15,587 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |       94.1% | May exist in G2, not top-100   |
| NEW        |     3 |        5.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 245 Row 14 Seats 8–9  avg $2,760/ea  total $5,520
Cheapest New: Sec 146 Row 21 Seats 7–8  avg $9,200/ea  total $18,400

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 32 groups, price range $3,680 – $69,805 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row 5 Seats 11–12  avg $2,012/ea  total $4,024
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 6 groups, price range $4,025 – $7,475 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row 15 Seats 9–10  avg $2,371/ea  total $4,742
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             48 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

