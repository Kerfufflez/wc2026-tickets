## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 29 groups, price range $5,175 – $15,755 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 101 Row 5 Seats 14–15  avg $3,162/ea  total $6,324
Cheapest New: Sec 251 Row 14 Seats 5–6  avg $9,085/ea  total $18,170

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 28 groups, price range $5,060 – $43,068 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 320 Row 22 Seats 4–5  avg $4,474/ea  total $8,948
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

