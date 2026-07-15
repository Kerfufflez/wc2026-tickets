## Category 1 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 41 groups, price range $32,200 – $184,000 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 43 Seats 3–4  avg $17,250/ea  total $34,500
Cheapest New: Sec 245C Row 14 Seats 3–4  avg $15,588/ea  total $31,176

Pairs eligible for merge (NEW below G2 min $32,200): 6

## Category 2 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 69 groups, price range $18,508 – $184,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 23 Seats 21–22  avg $12,362/ea  total $24,724
Cheapest New: Sec 319 Row 13 Seats 16–17  avg $93,438/ea  total $186,876

## Category 3 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 49 groups, price range $16,100 – $1,357,000 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 22 Seats 9–10  avg $10,925/ea  total $21,850
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 9 groups, price range $17,133 – $54,050 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 23 Seats 26–27  avg $13,225/ea  total $26,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             12 | DERIVE          |
| Cat 2    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             27 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

