## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 136 groups, price range $742 – $2,474 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 222 Row OO Seats 3–4  avg $449/ea  total $898
Cheapest New: Sec 244 Row T Seats 6–7  avg $1,319/ea  total $2,638

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 182 groups, price range $635 – $8,247 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row E Seats 101–102  avg $383/ea  total $766
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 50 groups, price range $656 – $3,450 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 420 Row UU Seats 104–105  avg $402/ea  total $804
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 6 groups, price range $805 – $1,265 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 403 Row WW Seats 1–2  avg $529/ea  total $1,058
Cheapest New: Sec 428 Row XX Seats 2–3  avg $690/ea  total $1,380

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            225 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            219 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

