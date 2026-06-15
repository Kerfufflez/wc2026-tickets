## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 42 groups, price range $4,285 – $27,600 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 464 Row 6 Seats 6–7  avg $2,644/ea  total $5,288
Cheapest New: Sec 116 Row 22 Seats 7–8  avg $17,250/ea  total $34,500

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 17 groups, price range $5,035 – $16,330 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 565 Row 7 Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: Sec 534 Row 7 Seats 14–15  avg $2,300/ea  total $4,600

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 14 groups, price range $4,301 – $13,225 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       77.8% | May exist in G2, not top-100   |
| NEW        |     6 |       22.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 637 Row 9 Seats 1–2  avg $2,300/ea  total $4,600
Cheapest New: Sec 665 Row 9 Seats 17–18  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $4,301): 0

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 3 groups, price range $5,750 – $15,556 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 601 Row 8 Seats 14–15  avg $2,956/ea  total $5,912
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             12 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             21 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

