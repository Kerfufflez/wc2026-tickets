## Category 1 — Pair Derivation Analysis
Date: July 14, 2026

G2 fetched: 152 groups, price range $3,646 – $62,100 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 242 Row 5 Seats 11–12  avg $2,082/ea  total $4,164
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 14, 2026

G2 fetched: 177 groups, price range $2,404 – $16,100 total
G4 fetched: 46 groups → 138 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   132 |       95.7% | May exist in G2, not top-100   |
| NEW        |     6 |        4.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 438 Row 24 Seats 9–10  avg $1,288/ea  total $2,576
Cheapest New: Sec 403 Row 3 Seats 17–18  avg $8,556/ea  total $17,112

Pairs eligible for merge (NEW below G2 min $2,404): 0

## Category 3 — Pair Derivation Analysis
Date: July 14, 2026

G2 fetched: 34 groups, price range $2,875 – $28,239 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 423 Row 22 Seats 9–10  avg $1,840/ea  total $3,680
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             93 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            132 | DERIVE          |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

