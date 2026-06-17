## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 42 groups, price range $1,495 – $16,100 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |       93.3% | May exist in G2, not top-100   |
| NEW        |     3 |        6.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 243 Row 4 Seats 8–9  avg $1,438/ea  total $2,876
Cheapest New: Sec 123 Row 22 Seats 17–18  avg $28,750/ea  total $57,500

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 32 groups, price range $1,608 – $11,500 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row 5 Seats 14–15  avg $1,035/ea  total $2,070
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 3 groups, price range $2,047 – $4,370 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 405 Row 20 Seats 1–2  avg $1,150/ea  total $2,300
Cheapest New: Sec 403 Row 16 Seats 5–6  avg $2,874/ea  total $5,748

Pairs eligible for merge (NEW below G2 min $2,047): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             42 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             51 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |              6 | DERIVE          |

Overall recommendation: **DERIVE**

