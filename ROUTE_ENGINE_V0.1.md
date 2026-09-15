# STORK POST OFFICE — Route Engine v0.1

Status: INTERNAL / OBSERVATION ONLY

## Objective
Rank candidate Stonk ecosystem reward routes for durability and treasury suitability. The engine is a research filter, not an execution bot. No score authorizes capital deployment by itself.

## Hard intake gates
A candidate is rejected before scoring if any required gate fails:

- Graduated / actively tradeable
- Age >= 72 hours
- Market cap >= $750,000
- 72h realized reward data available
- Eligible holders >= 250
- Sustained trading activity across the observation window
- No obvious liquidity, contract, concentration, or operational red flag

Thresholds are provisional and should be recalibrated from observed ecosystem distributions.

## Route Score — 100 points

### 1. Yield Quality — 30
Measures realized rewards, not advertised APR.
- 72h realized APR / reward rate: 12
- 24h vs 72h consistency: 8
- payout count / continuity: 5
- reward value actually distributed: 5

Extreme APR receives no automatic bonus and may trigger a volatility penalty.

### 2. Survival — 25
- age / persistence: 7
- drawdown control: 8
- market-cap persistence: 5
- survival through weak ecosystem sessions: 5

### 3. Liquidity & Activity — 20
- sustained volume: 7
- volume / market-cap quality: 5
- liquidity depth where available: 5
- buy/sell activity quality: 3

### 4. Distribution — 15
- eligible holder count: 5
- holder growth / retention: 5
- concentration / whale risk: 5

### 5. Reward Asset Quality — 10
Rates the asset delivered to holders / treasury routes.
- liquidity / convertibility: 3
- strategic reserve desirability: 3
- volatility / survivability: 2
- ecosystem relevance: 2

## Penalties / kill conditions
- suspected manipulation or circular volume: reject
- material contract / transfer-risk concern: reject
- catastrophic liquidity deterioration: reject
- severe concentration with credible exit risk: reject or -20
- 24h price collapse >50% without recovery: -15 and observation hold
- realized APR spike caused by collapsing denominator: cap Yield Quality at 10/30

## Classification
- 85–100: PRIORITY ROUTE CANDIDATE
- 75–84: WATCH / VALIDATION
- 65–74: OBSERVATION
- <65: REJECT

## Activation rule
Route 002 is not declassified from a single snapshot. A candidate must:

1. Pass every hard gate.
2. Score >=75 on at least 3 consecutive scheduled snapshots.
3. Remain >=70 during at least one adverse / red market interval when observable.
4. Receive manual treasury review.
5. Have deployment size and exit/liquidity constraints defined before any treasury transaction.

## Treasury principle
The Post Office optimizes for durable delivery, not maximum displayed APR. Treasury transactions are disclosed as treasury activity and must not be used to manufacture volume, holders, or market signals.

## Initial data fields
`timestamp, ticker, contract, reward_asset, age_hours, market_cap, liquidity, volume_24h, volume_mc, holders, holder_delta, realized_apr_24h, realized_apr_72h, payout_count_72h, rewards_usd_72h, price_change_24h, drawdown, concentration_proxy, yield_score, survival_score, liquidity_score, distribution_score, reward_asset_score, penalties, route_score, classification`
