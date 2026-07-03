## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 362 groups, price range $2,091 – $34,500 total
G4 fetched: 122 groups → 366 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   357 |       97.5% | May exist in G2, not top-100   |
| NEW        |     9 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 248 Row HH Seats 4–5  avg $1,216/ea  total $2,432
Cheapest New: Sec 203 Row RR Seats 6–7  avg $932/ea  total $1,864

Pairs eligible for merge (NEW below G2 min $2,091): 6

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 214 groups, price range $1,449 – $32,416 total
G4 fetched: 81 groups → 243 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   243 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 440 Row ZZ Seats 106–107  avg $891/ea  total $1,782
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 57 groups, price range $1,943 – $24,312 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 426 Row EE Seats 105–106  avg $1,216/ea  total $2,432
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 9 groups, price range $2,298 – $9,838 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 425 Row WW Seats 104–105  avg $1,297/ea  total $2,594
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            357 | DERIVE          |
| Cat 2    |       0.0% |         0 |            243 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             90 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

