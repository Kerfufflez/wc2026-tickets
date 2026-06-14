## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 170 groups, price range $862 – $8,050 total
G4 fetched: 121 groups → 363 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   363 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 145 Row 21 Seats 15–16  avg $460/ea  total $920
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 173 groups, price range $805 – $5,750 total
G4 fetched: 135 groups → 405 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   393 |       97.0% | May exist in G2, not top-100   |
| NEW        |    12 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 10 Seats 5–6  avg $412/ea  total $824
Cheapest New: Sec 226 Row 21 Seats 9–10  avg $391/ea  total $782

Pairs eligible for merge (NEW below G2 min $805): 12

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 65 groups, price range $628 – $2,422 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 418 Row 17 Seats 21–22  avg $345/ea  total $690
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 2 groups, price range $920 – $1,840 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 22 Seats 18–19  avg $713/ea  total $1,426
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            363 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |            393 | DERIVE          |
| Cat 3    |       0.0% |         0 |            117 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

