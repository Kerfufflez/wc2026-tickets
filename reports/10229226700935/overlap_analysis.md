## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 37 groups, price range $5,290 – $34,500 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |       95.5% | May exist in G2, not top-100   |
| NEW        |     3 |        4.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row F Seats 5–6  avg $2,645/ea  total $5,290
Cheapest New: Sec 116 Row J Seats 5–6  avg $2,530/ea  total $5,060

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 11 groups, price range $4,009 – $6,900 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 513 Row H Seats 3–4  avg $4,479/ea  total $8,958

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 5 groups, price range $4,600 – $18,054 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 625 Row F Seats 13–14  avg $2,588/ea  total $5,176
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             63 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              0 | SKIP            |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

