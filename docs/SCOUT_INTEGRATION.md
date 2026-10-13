# STORK × SCOUT homepage integration

This changes only the static Post Office website and preserves the original postal presentation. STORK is the ecosystem/community identity; [SCOUT](https://scout.storkcoin.xyz) is its independently accessible read-only research product. No STORK ownership, payment or wallet connection is required to read SCOUT. No subscription revenue-sharing, investment returns or token price expectations are promised.

## Scope

- Featured canonical SCOUT entry from the homepage hero and research panel.
- Added links to Radar, Daily Brief, Data Health and research methodology.
- Labeled the September 15, 2026 earnings snapshot as a historical archive, not a current schedule.
- Corrected the nonfunctional wallet-tracking prototype's presentation.
- Kept published onchain mint, treasury and transaction proof references intact.
- No SCOUT repository, DNS, deployment, treasury, tokenomics or automation changes.

## Checks and human review

Run `python3 -m unittest discover -s tests` (Python standard library). Review the updated static HTML at 320px, 390px and desktop widths, keyboard focus, content overflow, image loading, and links. Also test on Safari iPhone.

Because the homepage deploys separately (Netlify/static hosting), a GitHub PR pass **does not** establish that https://storkcoin.xyz has updated. Confirm deployment target and domain routing after an authorized merge; verify the SCOUT deep links and browser Back.

## Rollback

Revert the homepage and tests in a reviewed PR, keeping live infrastructure, onchain assets and domains untouched.
