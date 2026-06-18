## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 35 groups, price range $6,900 – $23,000 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec C313 Row 5 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 8 groups, price range $5,750 – $9,083 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       75.0% | May exist in G2, not top-100   |
| NEW        |     6 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 436 Row 5 Seats 17–18  avg $2,978/ea  total $5,956
Cheapest New: Sec 411 Row 30 Seats 23–24  avg $2,415/ea  total $4,830

Pairs eligible for merge (NEW below G2 min $5,750): 3

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 4 groups, price range $5,412 – $103,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 422 Row 16 Seats 10–11  avg $1,062,600/ea  total $2,125,200

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             30 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             18 | DERIVE          |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

