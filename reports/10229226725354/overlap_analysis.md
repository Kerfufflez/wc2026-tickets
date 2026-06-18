## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 127 groups, price range $6,647 – $633,487 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 24 Seats 13–14  avg $3,622/ea  total $7,244
Cheapest New: Sec 231 Row 18 Seats 9–10  avg $3,219/ea  total $6,438

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 164 groups, price range $5,164 – $57,500 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   336 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 10 Seats 17–18  avg $2,588/ea  total $5,176
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 35 groups, price range $5,173 – $23,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       81.8% | May exist in G2, not top-100   |
| NEW        |     6 |       18.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 526 Row 8 Seats 9–10  avg $2,645/ea  total $5,290
Cheapest New: Sec 547 Row 17 Seats 2–3  avg $12,362/ea  total $24,724

Pairs eligible for merge (NEW below G2 min $5,173): 0

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 1 groups, price range $6,900 – $6,900 total
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
Cheapest New: Sec 526 Row 12 Seats 1–2  avg $17,250/ea  total $34,500

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            174 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            336 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             27 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

