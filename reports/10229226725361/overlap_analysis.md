## Category 1 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 492 groups, price range $3,237 – $403,650 total
G4 fetched: 280 groups → 840 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   834 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 5 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $258,750/ea  total $517,500

Pairs eligible for merge (NEW below G2 min $3,237): 0

## Category 2 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 198 groups, price range $2,999 – $229,999 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 23 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 77 groups, price range $2,760 – $80,500 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row 20 Seats 5–6  avg $1,618/ea  total $3,236
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 8 groups, price range $3,795 – $13,570 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,832/ea  total $5,664
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            834 | DERIVE          |
| Cat 2    |       0.0% |         0 |            204 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             93 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

