## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 30 groups, price range $2,415 – $6,440 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       81.8% | May exist in G2, not top-100   |
| NEW        |     6 |       18.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec NE-T-1 Row 3 Seats 33–34  avg $1,378/ea  total $2,756
Cheapest New: Sec 132 Row 32 Seats 15–16  avg $3,450/ea  total $6,900

Pairs eligible for merge (NEW below G2 min $2,415): 0

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 27 groups, price range $1,840 – $9,729 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 242 Row 14 Seats 19–20  avg $999/ea  total $1,998
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 14 groups, price range $1,999 – $6,900 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 214 Row 20 Seats 15–16  avg $1,150/ea  total $2,300
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             27 | DERIVE          |
| Cat 2    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

