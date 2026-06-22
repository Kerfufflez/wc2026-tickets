## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 41 groups, price range $5,750 – $15,755 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       88.2% | May exist in G2, not top-100   |
| NEW        |     6 |       11.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 251 Row 12 Seats 8–9  avg $3,048/ea  total $6,096
Cheapest New: Sec 126 Row 15 Seats 11–12  avg $2,869/ea  total $5,738

Pairs eligible for merge (NEW below G2 min $5,750): 3

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 29 groups, price range $4,945 – $43,068 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 22 Seats 5–6  avg $2,846/ea  total $5,692
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 8 groups, price range $5,750 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 24 Seats 21–22  avg $3,680/ea  total $7,360
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             45 | DERIVE          |
| Cat 2    |       0.0% |         0 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

