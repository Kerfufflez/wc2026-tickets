## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 12 groups, price range $4,025 – $6,900 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       14.3% | May exist in G2, not top-100   |
| NEW        |    18 |       85.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 5 Seats 7–8  avg $2,415/ea  total $4,830
Cheapest New: Sec 104 Row 12 Seats 1–2  avg $1,978/ea  total $3,956

Pairs eligible for merge (NEW below G2 min $4,025): 3

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 22 groups, price range $2,811 – $23,000 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 15 Seats 22–23  avg $1,609/ea  total $3,218
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 5 groups, price range $3,450 – $5,449 total
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
Cheapest New: Sec 317 Row 25 Seats 21–22  avg $3,608/ea  total $7,216

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        18 |              3 | DERIVE          |
| Cat 2    |       0.0% |         0 |             27 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

