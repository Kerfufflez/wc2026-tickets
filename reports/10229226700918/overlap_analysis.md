## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 26 groups, price range $2,528 – $9,218 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 137 Row 22 Seats 11–12  avg $1,368/ea  total $2,736
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 16 groups, price range $1,978 – $3,450 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       81.8% | May exist in G2, not top-100   |
| NEW        |     6 |       18.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 312 Row 19 Seats 15–16  avg $1,150/ea  total $2,300
Cheapest New: Sec 305 Row 13 Seats 17–18  avg $2,300/ea  total $4,600

Pairs eligible for merge (NEW below G2 min $1,978): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 2 groups, price range $2,024 – $2,300 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 337 Row 24 Seats 11–12  avg $1,150/ea  total $2,300
Cheapest New: Sec 301 Row 9 Seats 1–2  avg $992/ea  total $1,984

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             27 | DERIVE          |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

