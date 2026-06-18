## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 37 groups, price range $6,449 – $23,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec C313 Row 5 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 4 groups, price range $5,186 – $9,083 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 436 Row 5 Seats 17–18  avg $2,978/ea  total $5,956
Cheapest New: Sec 445 Row 17 Seats 21–22  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $5,186): 0

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 6 groups, price range $4,569 – $103,500 total
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
| Cat 1    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             12 | DERIVE          |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

