# STORK POST OFFICE — Route Engine Snapshot #002

Timestamp: 2026-09-14 late UTC
Status: OBSERVATION ONLY — NO TREASURY DEPLOYMENT

## Data-integrity upgrade
Snapshot #002 discovered an important ticker-collision risk: ticker/name alone is not a valid route identifier. A LOOM listing page showed a graduated reward token around $1.76M market cap / 8.2K holders / ~554% 72h APR, while a token-detail result for a different LOOM mint (`42E58ruTYuV5bTctHyN2roK9CDV3HNsUGERRwvxKGCZD`) showed an ungraduated ~$7K token with only 81 holders paid. Therefore:

**NEW HARD RULE: every candidate must be keyed by mint + quote mint + pool, never ticker alone.**

Snapshot #001's LOOM score is invalidated until the intended mint is positively resolved.

## Verified observations

### KNOTS / STONK — VERIFIED
Mint: `8RVBk8vxLiUHueLUW1f4izFVqN3nWippLhkohKg6EGkS`
- Market cap: ~$17.66M
- 24h volume: ~$1.20M
- Liquidity: ~$920K
- 24h price: -17.7%
- Peak: ~$51.61M; drawdown ~65.8%
- Age: 9d
- Rewards: ~7.83M STONK / ~$1.64M current value
- Payouts: ~319.8K
- Holders paid: ~12.6K
- HolderScan change: +1.6K 24h (latest available read)

Assessment: passes scale/activity/distribution gates; large drawdown remains the principal survival penalty. Remains VALIDATION, not cleared.

### STONKCAT / STONK — VERIFIED
Mint: `DkPQvrx7CDYrL4HfHijz6GqZLYm7Pd4rm1kTiumLFwhS`
- Market cap: ~$1.59M
- 24h volume: ~$293.7K
- Vol/MC: ~0.18x
- 24h price: +9.2% on captured detail snapshot
- Peak: ~$5.00M; drawdown ~68.1%
- Age: 21d
- Lifetime rewards ledger: ~1.15M STONK / ~$242K current value, ~82.7K payouts, ~3.5K holders

Assessment: passes minimum scale but severe peak drawdown keeps it below priority tier.

### ZCAT / ZEC — REWARD HISTORY VERIFIED; MARKET DETAIL PENDING MINT LOCK
- Lifetime reward rank: #1
- Distributed: ~5.7K ZEC
- Current-value equivalent: ~$6.59M
- Payouts: ~1.23M
- Holders: ~30.0K

Assessment: strongest proven reward-history candidate, but Snapshot #002 will not assign a new numerical score until mint/pool identity and same-time market/liquidity snapshot are locked. This is intentional data hygiene.

### LEVERCAT / xSOL — REWARD HISTORY VERIFIED; MARKET DETAIL PENDING MINT LOCK
- Lifetime reward rank: #8
- Distributed: ~9.70M xSOL
- Current-value equivalent: ~$633K
- Payouts: ~323.4K
- Holders: ~8.2K

Assessment: meaningful payout history; requires mint/pool and current market/liquidity verification before numerical rescore.

### LOOP / KNOTS — WATCH, NOT YET ELIGIBLE
- Lifetime rewards: ~10.89M KNOTS / ~$202K current value
- Payouts: ~194.8K
- Holders: ~5.5K

Assessment: ecosystem relevance is high, but age/72h validation and market-detail requirements remain. No route eligibility yet.

### LOOM / SOL — QUARANTINED
Snapshot #001 score removed pending mint identity resolution. Ticker collision demonstrated that a name-only scan can join metrics from different tokens.

## Snapshot #002 classification
1. ZCAT — PRIORITY RESEARCH / identity lock required before score #2
2. KNOTS — VALIDATION / verified
3. STONKCAT — OBSERVATION / verified
4. LEVERCAT — VALIDATION RESEARCH / identity lock required
5. LOOP — WATCH / insufficient validation window
6. LOOM — QUARANTINED / ticker collision

No candidate has satisfied Route 002 activation requirements.

## Engine changes effective immediately
1. Candidate primary key = `mint + quote_mint + pool`.
2. No metric may be joined by ticker/name alone.
3. A snapshot score requires a same-candidate identity lock across market, reward, and holder data.
4. Missing liquidity/concentration data lowers confidence; it may not be silently imputed.
5. Snapshot #001 LOOM result is formally invalidated.
6. Consecutive-validation counter starts only with identity-locked snapshots.

## Treasury decision
**HOLD RESERVE PRINCIPAL. ROUTE 002 REMAINS CLASSIFIED.**
