## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 73 groups, price range $1,150 – $27,060 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 30 Seats 5–6  avg $575/ea  total $1,150
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 122 groups, price range $736 – $3,703 total
G4 fetched: 60 groups → 180 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |       96.7% | May exist in G2, not top-100   |
| NEW        |     6 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 24 Seats 12–13  avg $448/ea  total $896
Cheapest New: Sec 127 Row 26 Seats 26–27  avg $2,300/ea  total $4,600

Pairs eligible for merge (NEW below G2 min $736): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 36 groups, price range $690 – $2,576 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row 4 Seats 1–2  avg $460/ea  total $920
Cheapest New: Sec 340 Row 17 Seats 16–17  avg $3,291/ea  total $6,582

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            150 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            174 | DERIVE          |
| Cat 3    |       0.0% |         3 |             57 | INVESTIGATE     |

Overall recommendation: **DERIVE**

