## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 26 groups, price range $2,275 – $19,550 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 134 Row H Seats 1–2  avg $1,535/ea  total $3,070
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 8 groups, price range $2,474 – $5,957 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     6 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 206 Row W Seats 13–14  avg $5,750/ea  total $11,500

Pairs eligible for merge (NEW below G2 min $2,474): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 10 groups, price range $1,852 – $5,559 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 202 Row Q Seats 12–13  avg $2,070/ea  total $4,140
Cheapest New: Sec 223 Row CC Seats 18–19  avg $3,392/ea  total $6,784

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |              0 | DERIVE          |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

