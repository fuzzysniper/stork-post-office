# STORK POST OFFICE — Route Engine Snapshot 001

Timestamp: 2026-09-14 evening CT
Status: INTERNAL / OBSERVATION ONLY

This is the first baseline snapshot. Scores are intentionally provisional because concentration, exact 72h payout values, and current liquidity are incomplete for some candidates. No treasury deployment is authorized.

## Intake result

### Current leaders

| Rank | Candidate | Reward | MC / 24h volume | Age | Holders | Yield signal | Provisional score | Classification |
|---|---|---|---|---|---|---|---:|---|
| 1 | ZCAT | ZEC | ~$93–97M / ~$3.5–3.6M | 13d | ~29K | ~159–167% 72h APR | 86 | PRIORITY ROUTE CANDIDATE |
| 2 | KNOTS | STONK | ~$17.7M current / ~$1.2M current | 9d | 12.6K paid | historically ~500% 72h APR | 82 | WATCH / VALIDATION |
| 3 | LOOM | SOL | ~$1.75M recent / ~$385K recent | 33d | ~8K | ~558% 72h APR recent | 80 | WATCH / VALIDATION |
| 4 | STONKCAT | STONK | ~$1.59M current / ~$294K current | 21d | 3.5K paid | historically very high realized APR | 76 | WATCH / VALIDATION |
| 5 | LEVERCAT | xSOL | ~$4.2M recent / ~$597K recent | 5d | ~8K | ~608% 72h APR recent | 74 | OBSERVATION |

Scores are research estimates under v0.1, not investment ratings.

## Why the leaders rank this way

### ZCAT — 86
Best durability profile in the current sample: very large market cap, deep holder base, multi-day reward history, substantial lifetime distributions, and ZEC as a liquid reward asset. Yield is lower than smaller competitors, but Route Engine explicitly rewards durable delivery over maximum displayed APR.

### KNOTS — 82
Strong strategic fit because rewards are paid directly in STONK. Large reward history and holder base. Current weakness matters: market cap is materially below peak and the route needs consecutive snapshots to prove stabilization. High strategic value, but not cleared.

### LOOM — 80
Older than most of the new reward cohort, pays in SOL, and has meaningful historical payout activity. Strong reward-asset quality. Needs refreshed current price/liquidity and concentration data before moving higher.

### STONKCAT — 76
Native STONK reward route with meaningful distributions and holder growth. However, it remains far below peak market cap, so survival/drawdown prevents the very high realized APR from dominating the score.

### LEVERCAT — 74
High activity and yield, but xSOL adds reward-asset complexity and the token is much younger than the most durable candidates. Observation only.

## Gate failures / holds

- LOOP: HOLD — age below 72h in the baseline dataset and no full 72h APR window at initial scan. Re-evaluate next snapshot.
- TACZ: HOLD — too young / incomplete realized 72h data.
- HEV: REJECT FOR NOW — too young at baseline.
- SOLCAT: REJECT — market cap far below hard gate despite extreme displayed APR; severe price decline demonstrates denominator/yield distortion risk.
- ANALOS: REJECT — market cap far below hard gate.

## Snapshot 002 requirements

1. Refresh market cap, volume, price change, holders and payout recency for the top five.
2. Capture current liquidity for every candidate.
3. Add concentration / top-holder proxy.
4. Calculate 24h vs 72h realized-yield consistency rather than relying on one APR number.
5. Re-test LOOP after the 72h age/data gate.
6. No treasury transaction until a candidate has >=75 across three consecutive snapshots plus manual review.

## Current routing state

ROUTE 001: STONK — ACTIVE
ROUTE 002: CLASSIFIED — NO CANDIDATE CLEARED
ROUTES 003–005: CLASSIFIED
