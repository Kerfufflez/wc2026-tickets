## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 54 groups, price range $5,635 – $16,100 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 126 Row 25 Seats 22–23  avg $3,042/ea  total $6,084
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 28 groups, price range $5,416 – $43,068 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 20 Seats 9–10  avg $2,875/ea  total $5,750
Cheapest New: Sec 321 Row 18 Seats 1–2  avg $2,645/ea  total $5,290

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 6 groups, price range $5,750 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 334 Row 25 Seats 21–22  avg $3,207/ea  total $6,414
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             57 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

