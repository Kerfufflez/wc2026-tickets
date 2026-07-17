## Category 1 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 531 groups, price range $1,150 – $25,875 total
G4 fetched: 281 groups → 843 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   840 |       99.6% | May exist in G2, not top-100   |
| NEW        |     3 |        0.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 154 Row 15 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 121 Row 7 Seats 21–22  avg $25,875/ea  total $51,750

## Category 2 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 228 groups, price range $1,035 – $23,000 total
G4 fetched: 66 groups → 198 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 23 Seats 9–10  avg $592/ea  total $1,184
Cheapest New: Sec 319 Row 18 Seats 3–4  avg $432,069/ea  total $864,138

## Category 3 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 87 groups, price range $1,045 – $80,500 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 21 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 12 groups, price range $1,265 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 17–18  avg $920/ea  total $1,840
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            840 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            195 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

