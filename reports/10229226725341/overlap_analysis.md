## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 96 groups, price range $6,900 – $67,850 total
G4 fetched: 84 groups → 252 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   252 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 17 Seats 17–18  avg $3,451/ea  total $6,902
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 10 groups, price range $6,440 – $19,895 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 14 Seats 2–3  avg $3,863/ea  total $7,726
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 14 groups, price range $6,900 – $17,250 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 28 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: Sec 331 Row 22 Seats 9–10  avg $3,444/ea  total $6,888

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            252 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              3 | SKIP            |
| Cat 3    |       0.0% |         3 |             27 | INVESTIGATE     |

Overall recommendation: **PARTIAL**

