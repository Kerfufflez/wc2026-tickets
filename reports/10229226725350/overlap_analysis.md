## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 62 groups, price range $6,291 – $26,795 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |       95.8% | May exist in G2, not top-100   |
| NEW        |     3 |        4.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row M Seats 5–6  avg $3,738/ea  total $7,476
Cheapest New: Sec 241 Row L Seats 5–6  avg $39,494/ea  total $78,988

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 65 groups, price range $5,750 – $29,572 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |       90.3% | May exist in G2, not top-100   |
| NEW        |     9 |        9.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row F Seats 9–10  avg $3,409/ea  total $6,818
Cheapest New: Sec 339 Row M Seats 17–18  avg $2,670/ea  total $5,340

Pairs eligible for merge (NEW below G2 min $5,750): 3

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 17 groups, price range $5,750 – $17,250 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row K Seats 3–4  avg $2,875/ea  total $5,750
Cheapest New: Sec 319 Row T Seats 10–11  avg $14,375/ea  total $28,750

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             69 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |             84 | DERIVE          |
| Cat 3    |       0.0% |         3 |             33 | INVESTIGATE     |

Overall recommendation: **DERIVE**

