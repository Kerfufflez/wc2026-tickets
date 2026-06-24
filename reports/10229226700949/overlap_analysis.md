## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 43 groups, price range $4,998 – $20,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       81.8% | May exist in G2, not top-100   |
| NEW        |     6 |       18.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 140 Row 35 Seats 13–14  avg $2,760/ea  total $5,520
Cheapest New: Sec CL10 Row 7 Seats 17–18  avg $11,500/ea  total $23,000

Pairs eligible for merge (NEW below G2 min $4,998): 0

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 27 groups, price range $3,450 – $17,250 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 3 Seats 13–14  avg $1,955/ea  total $3,910
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 7 groups, price range $3,450 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 20 Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 1 groups, price range $4,600 – $4,600 total
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
Cheapest New: Sec 318 Row 17 Seats 5–6  avg $2,070/ea  total $4,140

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             27 | DERIVE          |
| Cat 2    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

