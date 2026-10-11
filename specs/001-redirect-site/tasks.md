# Spec 001 — tasks

- [x] T001 Recon: domain, DNS, GitHub org, tenant, branding (2026-10-11)
- [x] T002 Wireframes WF-01/WF-02/WF-03 drafted
- [x] T003 Owner approval of structure + wireframe direction
      ("Interstitial homepage + tracker at /research/", 2026-10-11)
- [x] T004 Build interstitial + research holding page on `staging`
- [x] T005 Create GitHub repo BitConcepts/bitconcepts-website, push `main` + `staging` — done 2026-10-11, repo public, main a62e6ae
- [x] T006 Local visual verification (Playwright, desktop + mobile)
- [x] T006b Research tracker integrated at /research/ — Glossa-Lab final
      judged build verbatim (audit passed; sha256 04ccc13b…; local
      Playwright re-verified desktop+mobile, 0 console errors, 0px
      mobile overflow); staging synced with noindex guards re-asserted
- [x] T007 Owner gate: Cloudflare dashboard sign-in — account identified
      via owner-minted token: "Tpierson@bitconcepts.tech's Account"
      2df9ae83…; zone bitconcepts.tech 167534fd…
- [x] T008 "BitConcepts Ops" API token minted by owner; completed to
      full scope via API (token itself held Account API Tokens Write):
      account policies + zone policy (DNS, Zone Settings, Zone WAF,
      Dynamic URL Redirects, Cache Purge, Zone Read); live-verified
      incl. DNS write round-trip (2026-10-11)
- [x] T009 Connect GitHub handshake done: Cloudflare Workers and Pages
      app installed on the BitConcepts org (installation 170393152),
      repo access = bitconcepts-website only; owner linked the
      installation to the Cloudflare account in his browser
- [x] T010 Pages projects created via API (bitconcepts-website = main,
      bitconcepts-website-staging = staging; no build command, root
      "/"); staging.bitconcepts.tech attached + proxied CNAME
- [x] T011 Staging verified: served bytes match the staging branch
      (research byte-identical; home differs only by Cloudflare email
      obfuscation), noindex guards live, managed-browser screenshots
      desktop match wireframes; mobile verified on identical files
- [x] T012 Owner review of staging — approved ("Promote to
      production", 2026-10-11)
- [x] T013 Promoted 2026-10-11: apex + www attached to production,
      DNS repointed to Pages (mail DNS diffed vs baseline — all
      MX/TXT/SRV records identical), FR-003 catch-all 301 rule live,
      curl path matrix verified (site paths 200, all other paths
      301 → axiovexsystems.com, www→apex preserved)
- [x] T014 Homepage auto-redirect REMOVED (owner directive
      2026-10-11, "so folks can go to the research page"): countdown
      JS + noscript meta-refresh deleted, site.v1.js removed,
      FR-001 + WF-01 amended
- [ ] T015 SEO/AEO pass (owner directive 2026-10-11): self-canonical,
      Twitter cards, JSON-LD @graph (Organization/WebSite/WebPage/
      FAQPage matching the visible Quick answers), sitemap lastmod,
      robots AI-crawler allowances, expanded llms.txt; stylesheet
      bumped to styles.v3.css (FR-003 rule exception updated to
      match); AEO scan before/after

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
