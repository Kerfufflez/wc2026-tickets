## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 49 groups, price range $2,990 – $16,100 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |       93.3% | May exist in G2, not top-100   |
| NEW        |     3 |        6.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 250 Row 5 Seats 1–2  avg $1,920/ea  total $3,840
Cheapest New: Sec 123 Row 22 Seats 17–18  avg $28,750/ea  total $57,500

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 31 groups, price range $2,298 – $11,500 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 409 Row 12 Seats 18–19  avg $1,322/ea  total $2,644
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 7 groups, price range $2,300 – $5,748 total
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
Cheapest New: Sec 405 Row 25 Seats 22–23  avg $1,437,500/ea  total $2,875,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             42 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

