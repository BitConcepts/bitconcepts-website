# Spec 001 — tasks

- [x] T001 Recon: domain, DNS, GitHub org, tenant, branding (2026-10-11)
- [x] T002 Wireframes WF-01/WF-02/WF-03 drafted
- [x] T003 Owner approval of structure + wireframe direction
      ("Interstitial homepage + tracker at /research/", 2026-10-11)
- [x] T004 Build interstitial + research holding page on `staging`
- [x] T005 Create GitHub repo BitConcepts/bitconcepts-website, push `main` + `staging` — done 2026-10-11, repo public, main a62e6ae
- [x] T006 Local visual verification (Playwright, desktop + mobile)
- [ ] T007 Owner gate: Cloudflare dashboard sign-in — identify the
      account holding the bitconcepts.tech zone, record account/zone IDs
- [ ] T008 Mint "BitConcepts Ops" API token (owner session), store
      mode-600 outside git
- [ ] T009 Owner gate: Connect GitHub handshake for the BitConcepts
      org in Cloudflare Pages
- [ ] T010 Create Pages projects (prod = main, staging = staging),
      attach staging.bitconcepts.tech
- [ ] T011 Verify staging visually (Playwright vs wireframes)
- [ ] T012 Owner review of staging
- [ ] T013 Promote: attach apex + www to production, add FR-003
      redirect rule, verify production visually + curl path test,
      diff mail DNS unchanged

# Spec 002 (SSO) — placeholder tasks

- [ ] T101 Inventory Cloudflare members + IdPs on the BitConcepts account
- [ ] T102 Member present as tpierson@bitconcepts.tech with correct role
- [ ] T103 Zero Trust org (team domain bitconcepts.cloudflareaccess.com)
- [ ] T104 Entra app registration in the BitConcepts tenant (owner
      admin session); secret goes only into Cloudflare's IdP config
- [ ] T105 Entra OIDC IdP in Zero Trust; groups claim
- [ ] T106 Dashboard SSO domain bitconcepts.tech verified + enabled,
      Microsoft Entra as the only IdP
- [ ] T107 Clean-session SSO sign-in test passes (owner)
- [ ] T108 Only after T107: enforce SSO-only for the domain
