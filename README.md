# bitconcepts-website

Source for https://bitconcepts.tech — hosted on Cloudflare Pages,
deployed from this repo (no build command; Pages serves the repo root).

- `main` → production (bitconcepts.tech + www.bitconcepts.tech)
- `staging` → staging (staging.bitconcepts.tech)

The homepage is a BitConcepts-branded interstitial that redirects
consulting visitors to https://axiovexsystems.com/. The research
tracker lives at `/research/` and is never redirected — its content
comes from the BitConcepts Indus decipherment program (Glossa-Lab)
and is built only from verified program values.

Changes follow the house flow: spec first (`specs/`), wireframes
before UI changes (`docs/wireframes/`), staging verification with
desktop + mobile screenshots before any production promotion.
Mail DNS for the BitConcepts Microsoft 365 tenant is never touched
by website work.
