## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 420 groups, price range $3,450 – $81,650 total
G4 fetched: 278 groups → 834 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   825 |       98.9% | May exist in G2, not top-100   |
| NEW        |     9 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 251 Row 13 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 106 Row 29 Seats 10–11  avg $53,394/ea  total $106,788

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 150 groups, price range $3,286 – $46,000 total
G4 fetched: 66 groups → 198 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   192 |       97.0% | May exist in G2, not top-100   |
| NEW        |     6 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 20 Seats 17–18  avg $1,643/ea  total $3,286
Cheapest New: Sec 321 Row 24 Seats 9–10  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $3,286): 3

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 48 groups, price range $3,910 – $271,400 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 30 Seats 17–18  avg $2,012/ea  total $4,024
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 5 groups, price range $3,910 – $16,100 total
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
| Cat 1    |       0.0% |         9 |            825 | DERIVE          |
| Cat 2    |       0.0% |         6 |            192 | DERIVE          |
| Cat 3    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

