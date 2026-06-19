## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 40 groups, price range $1,138 – $3,450 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       95.1% | May exist in G2, not top-100   |
| NEW        |     6 |        4.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 126 Row 8 Seats 1–2  avg $574/ea  total $1,148
Cheapest New: Sec 110 Row 12 Seats 29–30  avg $569/ea  total $1,138

Pairs eligible for merge (NEW below G2 min $1,138): 3

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 55 groups, price range $920 – $4,600 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       95.2% | May exist in G2, not top-100   |
| NEW        |     3 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row 28 Seats 4–5  avg $518/ea  total $1,036
Cheapest New: Sec 128 Row 33 Seats 19–20  avg $2,875/ea  total $5,750

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 26 groups, price range $824 – $3,565 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       92.3% | May exist in G2, not top-100   |
| NEW        |     3 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 222 Row 23 Seats 17–18  avg $518/ea  total $1,036
Cheapest New: Sec 218 Row 11 Seats 1–2  avg $2,300/ea  total $4,600

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 3 groups, price range $1,150 – $1,228 total
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
Cheapest New: Sec 207 Row 28 Seats 5–6  avg $805/ea  total $1,610

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            117 | DERIVE          |
| Cat 2    |       0.0% |         3 |             60 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

