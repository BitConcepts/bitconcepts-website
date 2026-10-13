# Spec 001 — BitConcepts redirect site + research home

Owner: Tristen Pierson. Decided 2026-10-11.

## Purpose

bitconcepts.tech today serves a 404. Give BitConcepts a live web
presence that (a) sends consulting visitors to ElectroHire with
BitConcepts branding intact, and (b) hosts the BitConcepts research
tracker at /research/, on the standing GitHub → Cloudflare Pages
pattern used by the Axiovex and Rockeagle sites.

## Requirements

- FR-001: Homepage `/` is a BitConcepts-branded interstitial per
  wireframe WF-01 (approved 2026-10-11): Continue button to
  https://electrohire.com/, 5-second auto-redirect (JS, with an
  8-second noscript meta-refresh fallback), cancellable via
  "Stay on this page".
  **Amendment (owner directive, 2026-10-11): the auto-redirect is
  REMOVED — no JS countdown, no meta-refresh. The homepage is a
  static landing page so visitors can reach /research/ at their own
  pace; the Continue button remains for consulting visitors.**
- FR-002: `/research/` is never redirected. It hosts the research
  tracker supplied by the Glossa-Lab program from its verified
  source pack; until integration it is an honest holding page.
  **Amendment (owner directive via Glossa-Lab chat, 2026-10-11):
  /research/ is now a Research home (programs index); the Indus
  script program tracker lives at /research/indus-script/. Future
  programs are added as cards on the index + their own subpages.**
- FR-003: Any other path on bitconcepts.tech (apex and www) 301s to
  https://electrohire.com/ via a Cloudflare redirect rule.
  **Amendment (owner directive, 2026-10-13): the consulting
  destination changed from Axiovex Systems to ElectroHire —
  ElectroHire is the suitable home for BitConcepts consulting;
  Axiovex does different consulting. Applies to the FR-003 rule,
  the FR-001 Continue button, and all consulting copy on the
  homepage and llms.txt. The research cross-links to the Axiovex
  research hub are NOT part of this change and stay.**
- FR-004: Hosting is Cloudflare Pages fed by this repo's branches:
  `staging` → staging.bitconcepts.tech, `main` → apex + www.
  No build command; Pages serves the repo root.
- FR-005: Mail is untouched: MX/SPF/DKIM/DMARC records for the
  BitConcepts Microsoft 365 tenant are preserved verbatim through
  every DNS/Pages change.
- FR-006: No claim appears on either page that is not in the
  verified record. The tracker never claims the Indus script is
  deciphered and names no other company or project.
- FR-007: Verification is visual: Playwright screenshots at desktop
  and mobile widths, compared against docs/wireframes/, on staging
  before production promotion and again after. Source checks alone
  never count as verification.
- FR-008: Cloudflare operations are API-first via a scoped
  "BitConcepts Ops" token (Pages/DNS/WAF/settings/cache, this
  account + zone only), minted in the dashboard by the owner
  session; the token value never enters chat, a repo, or memory.

## Out of scope (separate workstream in this project)

- Cloudflare dashboard SSO via the BitConcepts Microsoft tenant
  (Zero Trust + Entra OIDC, member tpierson@bitconcepts.tech,
  SSO tested before any enforcement). Tracked as Spec 002.
- The full tracker content build (owned by the Glossa-Lab chat;
  this spec only provides its hosting and integration point).

## Acceptance

Staging serves WF-01/WF-02 as screenshot-verified; after owner
review, production serves the same on apex + www; FR-003 rule
verified live with a curl path test; mail records diffed unchanged.
