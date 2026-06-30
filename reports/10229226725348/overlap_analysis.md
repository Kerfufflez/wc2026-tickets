## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 45 groups, price range $9,143 – $44,850 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       88.9% | May exist in G2, not top-100   |
| NEW        |     3 |       11.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row C Seats 20–21  avg $4,600/ea  total $9,200
Cheapest New: Sec 467 Row 1 Seats 1–2  avg $35,649/ea  total $71,298

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 11 groups, price range $9,200 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 504 Row 9 Seats 10–11  avg $5,520/ea  total $11,040
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 11 groups, price range $7,360 – $16,100 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     6 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 668 Row 10 Seats 25–26  avg $3,450/ea  total $6,900

Pairs eligible for merge (NEW below G2 min $7,360): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             24 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              6 | SKIP            |
| Cat 3    |       0.0% |         6 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

