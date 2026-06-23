## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 13 groups, price range $6,308 – $80,500 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row M Seats 17–18  avg $3,220/ea  total $6,440
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 3 groups, price range $5,750 – $6,944 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       20.0% | May exist in G2, not top-100   |
| NEW        |    12 |       80.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row L Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: Sec 242 Row BB Seats 10–11  avg $2,358/ea  total $4,716

Pairs eligible for merge (NEW below G2 min $5,750): 3

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 5 groups, price range $3,842 – $27,600 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 223 Row CC Seats 18–19  avg $5,175/ea  total $10,350
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             18 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |              3 | DERIVE          |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

