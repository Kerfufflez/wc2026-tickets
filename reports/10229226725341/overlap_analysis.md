## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 99 groups, price range $7,393 – $67,850 total
G4 fetched: 83 groups → 249 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 18 Seats 11–12  avg $3,910/ea  total $7,820
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 28 groups, price range $7,130 – $34,500 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       81.2% | May exist in G2, not top-100   |
| NEW        |     9 |       18.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 14 Seats 2–3  avg $3,863/ea  total $7,726
Cheapest New: Sec 322 Row 30 Seats 5–6  avg $3,392/ea  total $6,784

Pairs eligible for merge (NEW below G2 min $7,130): 9

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 18 groups, price range $6,900 – $20,556 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 28 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: Sec 331 Row 22 Seats 9–10  avg $3,444/ea  total $6,888

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 4 groups, price range $6,647 – $9,888 total
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
Cheapest New: Sec 336 Row 30 Seats 13–14  avg $5,002/ea  total $10,004

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            249 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |             39 | DERIVE          |
| Cat 3    |       0.0% |         3 |             27 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

