## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 275 groups, price range $4,600 – $11,477,000 total
G4 fetched: 88 groups → 264 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   264 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 119 Row 32 Seats 13–14  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 255 groups, price range $3,680 – $59,570 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   303 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 24 Seats 3–4  avg $1,952/ea  total $3,904
Cheapest New: Sec 335 Row 13 Seats 6–7  avg $1,828/ea  total $3,656

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 13 groups, price range $3,622 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row 23 Seats 5–6  avg $4,600/ea  total $9,200
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            264 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            303 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

