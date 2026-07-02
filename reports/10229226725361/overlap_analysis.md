## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 416 groups, price range $4,140 – $403,650 total
G4 fetched: 248 groups → 744 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   738 |       99.2% | May exist in G2, not top-100   |
| NEW        |     6 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 102 Row 10 Seats 21–22  avg $2,401/ea  total $4,802
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $258,750/ea  total $517,500

Pairs eligible for merge (NEW below G2 min $4,140): 0

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 120 groups, price range $3,795 – $46,000 total
G4 fetched: 36 groups → 108 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 27 Seats 12–13  avg $1,990/ea  total $3,980
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 60 groups, price range $3,220 – $80,500 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 356 Row 21 Seats 17–18  avg $1,696/ea  total $3,392
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 5 groups, price range $4,700 – $15,410 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,836/ea  total $5,672
Cheapest New: Sec 328 Row 30 Seats 2–3  avg $2,300/ea  total $4,600

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            738 | DERIVE          |
| Cat 2    |       0.0% |         0 |            108 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             84 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

