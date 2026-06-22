## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 36 groups, price range $4,485 – $22,770 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 101 Row 32 Seats 9–10  avg $3,162/ea  total $6,324
Cheapest New: Sec CL10 Row 7 Seats 17–18  avg $11,500/ea  total $23,000

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 27 groups, price range $3,450 – $17,250 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 10 Seats 21–22  avg $2,874/ea  total $5,748
Cheapest New: Sec 335 Row 14 Seats 13–14  avg $12,322/ea  total $24,644

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 8 groups, price range $4,726 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 26 Seats 8–9  avg $2,875/ea  total $5,750
Cheapest New: Sec 304 Row 13 Seats 9–10  avg $2,932,500/ea  total $5,865,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

