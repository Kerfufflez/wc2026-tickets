## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 90 groups, price range $4,888 – $46,000 total
G4 fetched: 42 groups → 126 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   126 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 118 Row F Seats 1–2  avg $2,472/ea  total $4,944
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 83 groups, price range $3,680 – $25,300 total
G4 fetched: 44 groups → 132 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   126 |       95.5% | May exist in G2, not top-100   |
| NEW        |     6 |        4.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row LL Seats 9–10  avg $2,036/ea  total $4,072
Cheapest New: Sec 331 Row G Seats 1–2  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $3,680): 0

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 22 groups, price range $4,025 – $12,305 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |       90.0% | May exist in G2, not top-100   |
| NEW        |     6 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 320 Row P Seats 2–3  avg $2,057/ea  total $4,114
Cheapest New: Sec 301 Row R Seats 13–14  avg $1,804/ea  total $3,608

Pairs eligible for merge (NEW below G2 min $4,025): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            126 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            126 | DERIVE          |
| Cat 3    |       0.0% |         6 |             54 | DERIVE          |

Overall recommendation: **DERIVE**

