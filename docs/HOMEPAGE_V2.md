# STORK Homepage V2 — ecosystem-first layout

Issue #3. The visitor experience now leads with STORK as the ecosystem/community identity and a high-contrast **SCOUT Intelligence Division** feature in the first major content section. The primary SCOUT link and Radar, Brief and Data Health shortcuts appear **before** token history, routing concepts or dated earnings material.

## Editorial boundaries
- SCOUT is free to explore, read-only, and independent of STORK ownership, wallet connection or payment.
- STORK token information and published onchain references remain available in the Post Office section; no software revenue distribution or token appreciation is promised.
- Existing paper/postal design, images and historical material retained; archived September market desk remains labeled as historical.
- A newly added navigation provides jump links to SCOUT, Post Office and token records.

## Human QA / release gate
This GitHub-only edit has **not** been tested in a real browser or on production. Execute `python3 -m unittest discover -s tests`, then preview the site at 320, 390, and 1280px widths. Verify no horizontal overflow, visible focus, all images, link navigation and Back. At 390px Safari, test whether the SCOUT feature and CTA are clearly visible without searching or extensive scrolling; account for device/browser viewport variation. The large prior mast image has moved below the first-screen hero.

## Deployment and rollback
Review and approve the PR, then verify the actual static-site host/domain manually. The repository has its own deployment system, separate from SCOUT/Vercel; merging alone does not prove Netlify deployed. Revert the V2 commits via reviewed PR to restore the old hierarchy. Do not modify DNS, wallets, treasury, token issuance, or SCOUT application code.
