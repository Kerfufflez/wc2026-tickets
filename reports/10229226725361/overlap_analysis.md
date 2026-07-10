## Category 1 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 506 groups, price range $3,235 – $403,650 total
G4 fetched: 285 groups → 855 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   849 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 5 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $258,750/ea  total $517,500

Pairs eligible for merge (NEW below G2 min $3,235): 0

## Category 2 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 205 groups, price range $2,507 – $229,999 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   228 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row 28 Seats 18–19  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 83 groups, price range $2,645 – $80,500 total
G4 fetched: 34 groups → 102 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 18 Seats 17–18  avg $1,495/ea  total $2,990
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 6 groups, price range $3,907 – $13,570 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,831/ea  total $5,662
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            849 | DERIVE          |
| Cat 2    |       0.0% |         0 |            228 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            102 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

