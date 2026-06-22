## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 414 groups, price range $3,680 – $403,650 total
G4 fetched: 270 groups → 810 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   804 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 1 Seats 17–18  avg $2,036/ea  total $4,072
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $3,680): 0

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 155 groups, price range $3,286 – $46,000 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 20 Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 49 groups, price range $3,910 – $271,400 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 30 Seats 17–18  avg $2,012/ea  total $4,024
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 4 groups, price range $3,910 – $16,100 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,875/ea  total $5,750
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            804 | DERIVE          |
| Cat 2    |       0.0% |         3 |            174 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             63 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

