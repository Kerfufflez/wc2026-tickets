## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 454 groups, price range $3,048 – $92,000 total
G4 fetched: 286 groups → 858 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   852 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 24 Seats 13–14  avg $1,649/ea  total $3,298
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $3,048): 0

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 163 groups, price range $2,760 – $46,000 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 20 Seats 13–14  avg $1,409/ea  total $2,818
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 57 groups, price range $2,760 – $271,400 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 30 Seats 17–18  avg $1,484/ea  total $2,968
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 9 groups, price range $2,760 – $16,100 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,885/ea  total $5,770
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            852 | DERIVE          |
| Cat 2    |       0.0% |         3 |            204 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

