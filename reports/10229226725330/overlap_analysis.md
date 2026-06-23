## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 12 groups, price range $6,358 – $80,500 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row M Seats 17–18  avg $3,220/ea  total $6,440
Cheapest New: Sec 122 Row T Seats 21–22  avg $2,990/ea  total $5,980

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 4 groups, price range $4,830 – $7,360 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       25.0% | May exist in G2, not top-100   |
| NEW        |     9 |       75.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 242 Row BB Seats 10–11  avg $2,875/ea  total $5,750
Cheapest New: Sec 245 Row CC Seats 6–7  avg $3,795/ea  total $7,590

Pairs eligible for merge (NEW below G2 min $4,830): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 6 groups, price range $3,748 – $27,600 total
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
| Cat 1    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |              3 | DERIVE          |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

