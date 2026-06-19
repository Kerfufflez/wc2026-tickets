## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 14 groups, price range $1,831 – $2,840 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       62.5% | May exist in G2, not top-100   |
| NEW        |     9 |       37.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 109 Row T Seats 9–10  avg $954/ea  total $1,908
Cheapest New: Sec 108 Row BB Seats 1–2  avg $1,495/ea  total $2,990

Pairs eligible for merge (NEW below G2 min $1,831): 0

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 10 groups, price range $1,610 – $8,018 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 242 Row Y Seats 1–2  avg $862/ea  total $1,724
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 8 groups, price range $1,840 – $4,255 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 247 Row J Seats 5–6  avg $1,127/ea  total $2,254
Cheapest New: Sec 248 Row V Seats 9–10  avg $862/ea  total $1,724

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |             15 | DERIVE          |
| Cat 2    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

