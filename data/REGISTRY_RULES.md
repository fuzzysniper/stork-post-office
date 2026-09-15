# Candidate Registry Rules v0.1

The Route Engine never joins or scores candidates by ticker alone.

## Canonical key
`token_mint + quote_mint + pool`

A candidate is `VERIFIED` only when all three identifiers resolve to the same token/reward market from source data.

## Join rules
1. Market-cap, volume, liquidity, age and price history must resolve to `token_mint`.
2. Reward history must resolve to the same `token_mint` and registered `quote_mint`.
3. Pool-level data must resolve to the registered `pool`.
4. A ticker/name mismatch is informational; an address mismatch is fatal.
5. Missing canonical identity fields => no numerical Route Score.
6. Conflicting identities => `QUARANTINED` until manually resolved.

## Validation clock
Research Snapshots #001 and #002 predate the canonical registry and do not count toward Route 002 activation.

The deployment-grade validation clock starts at Verified Snapshot V1. A route requires three consecutive identity-verified qualifying snapshots plus manual treasury review before declassification.

## Current registry status
- KNOTS: VERIFIED
- LOOP: VERIFIED
- LEVERCAT: VERIFIED
- STONKCAT: VERIFIED
- ZCAT: PENDING canonical token mint + pool despite strong research history
- LOOM: QUARANTINED due ticker/identity collision

No treasury deployment is authorized by registry inclusion alone.
