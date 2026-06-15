## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 36 groups, price range $1,150 – $5,750 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |       91.9% | May exist in G2, not top-100   |
| NEW        |     9 |        8.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 25 Seats 9–10  avg $575/ea  total $1,150
Cheapest New: Sec 117 Row 16 Seats 7–8  avg $552/ea  total $1,104

Pairs eligible for merge (NEW below G2 min $1,150): 9

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 95 groups, price range $860 – $3,450 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |       94.0% | May exist in G2, not top-100   |
| NEW        |     9 |        6.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row 9 Seats 9–10  avg $506/ea  total $1,012
Cheapest New: Sec 122 Row 36 Seats 31–32  avg $1,854/ea  total $3,708

Pairs eligible for merge (NEW below G2 min $860): 0

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 81 groups, price range $805 – $9,200 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 12 Seats 14–15  avg $436/ea  total $872
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 5 groups, price range $920 – $2,300 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row 30 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            102 | DERIVE          |
| Cat 2    |       0.0% |         9 |            141 | DERIVE          |
| Cat 3    |       0.0% |         0 |             99 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

