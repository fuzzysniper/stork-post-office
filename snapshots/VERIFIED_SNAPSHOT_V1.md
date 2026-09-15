# STORK POST OFFICE — Verified Snapshot V1

Timestamp: 2026-09-14 late UTC / current web reads
Status: FIRST DEPLOYMENT-GRADE OBSERVATION
Treasury action: NONE

## Method
Only candidates with canonical registry identity (token mint + quote mint + pool) may receive a verified score. Missing fields are not guessed. Public data sources may refresh at different times; values below are treated as observations, not synchronized ticks.

## Verified board

### KNOTS / STONK
Identity: token mint `8RVBk8vxLiUHueLUW1f4izFVqN3nWippLhkohKg6EGkS`; pool `GeND…Emjo`; quote STONK `6GmAFS…MpUNgx`.
Observed: market cap ~$17.66M; 24h volume ~$1.20M; liquidity ~$920K; ~65.8% below peak; ~12.6K holders paid; ~7.83M STONK distributed / ~319.8K payouts in the current detail read. Reward ledger later showed ~8.02M STONK / ~329.8K payouts / ~12.8K holders, confirming continued activity.
Assessment: strong reward continuity, substantial distribution and usable liquidity; severe peak drawdown remains the dominant risk.
Verified V1 score: 80/100 — VALIDATION.

### STONKCAT / STONK
Identity: token mint `DkPQvrx7CDYrL4HfHijz6GqZLYm7Pd4rm1kTiumLFwhS`; pool `5SaA…pb7A`; quote STONK `6GmA…UNgx`.
Observed: market cap ~$1.59M; 24h volume ~$293.7K; ~68.1% below peak; ~1.14M STONK distributed; ~82K payouts; ~3.5K holders paid; holder count increased in recent HolderScan reads.
Assessment: clears basic size/activity gates but drawdown remains severe and reserve suitability is materially weaker than KNOTS.
Verified V1 score: 73/100 — OBSERVATION.

### LEVERCAT / xSOL
Identity verified in registry: token mint `AGi2s9zPRPHs3zEDPhPTroumTEXK5ufymYSfEFndCSSW`; quote xSOL; canonical pool registered.
Observed reward ledger: ~9.70M xSOL distributed; ~323.4K payouts; ~8.2K holders; recent payouts continuing.
Assessment: reward continuity and holder breadth are strong. Current synchronized market-cap/liquidity/drawdown fields were not sufficiently exposed in this read, so V1 cannot assign a deployment-grade numeric score without inventing inputs.
Verified V1 classification: DATA HOLD — numeric score withheld.

### LOOP / KNOTS
Identity verified in registry: token mint `HunmXDXMNQYVoDnUL6PNnSYEtFaTZA2WzGh1HJTW7aoV`; quote KNOTS; canonical pool registered.
Observed reward ledger: ~10.89M KNOTS distributed; ~194.8K payouts; ~5.5K holders; payouts remain active.
Assessment: meaningful reward activity, but youth/market-risk validation remains insufficient for treasury authorization.
Verified V1 classification: WATCH — numeric score withheld pending complete market fields and age validation.

## Priority research — ZCAT / ZEC
Reward ledger remains exceptional: token identity shown as `HcRLc9…DeJR`; ~5.7K ZEC distributed; ~$6.59M current-value equivalent; ~1.23M payouts; ~30K holders.
However, full canonical token mint + pool + quote identity has not yet been committed to the registry. Therefore ZCAT is NOT eligible for a Verified V1 score despite strong history.
Status: PRIORITY IDENTITY RESOLUTION.

## Macro environment
STONK itself was observed around ~$184M market cap with ~$2.36M 24h volume, ~$4.55M main-pool TVL, ~69.7K holders, and 15.34% supply burned in one current read. Reward ledger showed ~$41.2M of payouts valued at current prices across ~14.8K reward coins and ~15.7M payout events. Market conditions are risk-off enough that drawdown resilience remains important.

## V1 conclusion
1. KNOTS is the only registry candidate receiving a verified VALIDATION score in V1.
2. STONKCAT remains OBSERVATION.
3. LEVERCAT and LOOP remain data/validation holds rather than being force-scored.
4. ZCAT remains the highest-priority identity-resolution target.
5. Route 002 stays CLASSIFIED.
6. Reserve Principal remains untouched.

## Activation clock
KNOTS: 1 / 3 verified validation snapshots.
STONKCAT: 0 / 3.
LEVERCAT: 0 / 3 numeric validations.
LOOP: 0 / 3 numeric validations.
ZCAT: 0 / 3 until registry identity is complete.

No candidate is authorized for treasury deployment.