## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 101 groups, price range $821 – $3,910 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |       93.4% | May exist in G2, not top-100   |
| NEW        |    12 |        6.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 230 Row H Seats 9–10  avg $452/ea  total $904
Cheapest New: Sec 118 Row F Seats 5–6  avg $402/ea  total $804

Pairs eligible for merge (NEW below G2 min $821): 6

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 150 groups, price range $669 – $3,450 total
G4 fetched: 66 groups → 198 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   198 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row FF Seats 15–16  avg $345/ea  total $690
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 54 groups, price range $644 – $3,220 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       90.9% | May exist in G2, not top-100   |
| NEW        |     6 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 339 Row DD Seats 9–10  avg $390/ea  total $780
Cheapest New: Sec 324 Row DD Seats 9–10  avg $308/ea  total $616

Pairs eligible for merge (NEW below G2 min $644): 6

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 3 groups, price range $690 – $2,760 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row J Seats 16–17  avg $460/ea  total $920
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            171 | DERIVE          |
| Cat 2    |       0.0% |         0 |            198 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             60 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

