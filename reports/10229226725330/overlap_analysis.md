## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 33 groups, price range $1,960 – $8,050 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row A Seats 1–2  avg $1,622/ea  total $3,244
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 15 groups, price range $2,070 – $12,478 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 203 Row NN Seats 5–6  avg $1,351/ea  total $2,702
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 6 groups, price range $1,886 – $4,370 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row C Seats 9–10  avg $1,242/ea  total $2,484
Cheapest New: Sec 228 Row E Seats 3–4  avg $920/ea  total $1,840

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              9 | SKIP            |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

