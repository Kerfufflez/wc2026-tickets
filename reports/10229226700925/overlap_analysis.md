## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 152 groups, price range $1,024 – $2,300,000 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   336 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 8 Seats 1–2  avg $575/ea  total $1,150
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 79 groups, price range $978 – $1,124,700 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |       97.4% | May exist in G2, not top-100   |
| NEW        |     3 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 256 Row 8 Seats 13–14  avg $518/ea  total $1,036
Cheapest New: Sec 202 Row 6 Seats 13–14  avg $470/ea  total $940

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 42 groups, price range $920 – $6,670 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 27 Seats 2–3  avg $489/ea  total $978
Cheapest New: Sec 314 Row 20 Seats 9–10  avg $430/ea  total $860

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 4 groups, price range $1,208 – $1,725 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 30 Seats 1–2  avg $667/ea  total $1,334
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            336 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            114 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

