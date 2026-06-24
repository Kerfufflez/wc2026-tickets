## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 44 groups, price range $3,852 – $25,300 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |       88.5% | May exist in G2, not top-100   |
| NEW        |     9 |       11.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 24 Seats 21–22  avg $1,955/ea  total $3,910
Cheapest New: Sec 128 Row 18 Seats 9–10  avg $1,689/ea  total $3,378

Pairs eligible for merge (NEW below G2 min $3,852): 9

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 55 groups, price range $2,525 – $19,550 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row 15 Seats 5–6  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 19 groups, price range $2,530 – $9,200 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 325 Row 10 Seats 3–4  avg $1,955/ea  total $3,910
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 6 groups, price range $3,680 – $5,173 total
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
Cheapest New: Sec 321 Row 19 Seats 5–6  avg $4,370/ea  total $8,740

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |             69 | DERIVE          |
| Cat 2    |       0.0% |         0 |             42 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

