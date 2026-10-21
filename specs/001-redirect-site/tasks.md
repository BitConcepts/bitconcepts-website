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
- [x] T015 SEO/AEO pass (owner directive 2026-10-11): self-canonical,
      Twitter cards, JSON-LD @graph (Organization/WebSite/WebPage/
      FAQPage matching the visible Quick answers), sitemap lastmod,
      robots AI-crawler allowances, expanded llms.txt; stylesheet
      bumped to styles.v3.css (FR-003 rule exception updated to
      match); AEO scan before/after

# Spec 002 (SSO) — placeholder tasks

- [x] T016 Research restructure (owner directive via Glossa chat
      2026-10-11): /research/ becomes the Research home (programs
      index, export sha256 a6725e76…); the Indus tracker moves to
      /research/indus-script/ (rebased export sha256 6d4bb756…,
      canonical/OG/JSON-LD rebased, breadcrumb added). Sitemap,
      llms.txt, homepage FAQ/JSON-LD links updated to the subpage.

- [x] T017 Consulting destination change (owner directive
      2026-10-13): Axiovex Systems → ElectroHire everywhere the
      redirect applies — FR-003 rule retargeted to
      https://electrohire.com/ (rule 1090d7c6…, entrypoint PUT;
      Ops token needed a zone policy with Zone Read + Dynamic URL
      Redirects Read/Write before the ruleset API would answer),
      homepage Continue button/copy/JSON-LD/FAQ, llms.txt
      consulting lines, WF-01 wireframe copy. Research cross-links
      to the Axiovex hub unchanged.

- [x] T018 Website currency update (owner standing rule 2026-10-13;
      Glossa-Lab handover, owner-approved prep): tracker status text
      updated to the verified Oct 13 position — claims at the
      explained stage, none accepted, outreach in progress;
      cross-compilation board entry resolved (compilations agree on
      shared objects; disagreement is composition — OSF ZD7UQ)
      superseding the "93.9% unexplained" framing; new board entry:
      flagship Dravidian readings NOT SUPPORTED vs no-language
      baseline (OSF EPHF7, bounded reading); PRED-2026-006 closed
      unscored + PRED-2026-010 registered (OSF WJEBQ); new Oct 13
      Latest research article; footer snapshot date updated.
      Related research section (Spec 003) preserved — surgical edit,
      NOT a wholesale export overwrite. Staging first; production
      on owner's site-side approval.

- [x] T019 Website currency update #2 (Glossa-Lab handover
      2026-10-20; program main 5e7f3cdb): record date Oct 20;
      Latest research gains the Oct 20 (Spec 035 / PRED-2026-010
      step-0 closure) and Oct 19 (Spec 033 Dravidian rerun)
      articles verbatim from a fresh artifact export; predictions
      note rewritten (010 closed unscored at opening checks —
      P000 unmappable, withheld data never opened; 011 registered,
      screened signs P217/P324; 003 candidate datasets flagged);
      releases point to Zenodo v5.0.0 (DOI 10.5281/zenodo.23351365,
      Oct 13) in Study papers, the releases array, homepage FAQ,
      and llms.txt (dated article texts untouched); CISI front
      updated (Vol 3.1 Basic data received Oct 14, intake done —
      2,123 records, no transcriptions, cannot score predictions);
      Spec 027 fronts updated (gazetteer built, period fields
      empty; Spec 030 NOT-YET-TESTABLE; Spec 031 Q7 closed at
      margins; route forward = period-assignment act). Related
      research preserved. Staging first, owner approval to promote.

- [x] T020 Correction + update (Glossa-Lab handover 2026-10-20,
      post-promotion): (1) CISI census corrected — Harappa 1,510 →
      1,604 (510 old excavations + 1,094 HARP seasons); the error
      was in the handover text, not the rendering. (2) Standing
      release pointers v5.0.0 → v5.1.0 (DOI 10.5281/zenodo.23503470,
      published 2026-10-20) in Study papers, releases array,
      homepage FAQ, llms.txt; dated texts untouched. (3) PRED-2026-003
      candidates: provenance assessed Oct 20 — both ICIT/Mahadevan
      lineage, NOT independent, candidacies close, 003 stays
      pending; both "not yet assessed" sentences replaced.

- [x] T021 PRED-2026-011 scored (Glossa-Lab handover 2026-10-20):
      predictions note updated — 011 CONFIRMED under Spec 036
      (Phase-400) on the withheld Harappa texts: P217 start rate
      0.8739 (104/119), P324 0.6111 (473/774), registered bar 0.40
      each, both required, independent recount in exact agreement.
      Limits stated with the claim: two signs only, P000 untested,
      cleanliness = training-pool exclusion not analyst blindness.
      Contract OSF GJEN4; registration T6WHQ unchanged. Dated
      article texts untouched.

- [x] T022 Release pointer update (Glossa-Lab handover 2026-10-20):
      v5.1.0 → v5.2.0 (DOI 10.5281/zenodo.23520218, published
      2026-10-20; carries the PRED-2026-011 CONFIRMED record) in
      Study papers, the releases array, homepage FAQ, and llms.txt.
      The research index names no versioned release (concept DOI
      only) — nothing to move there. Dated texts untouched;
      Related research preserved.

- [x] T101 Inventory done: members tpierson@ + anagaraja@ (both Super
      Admin, accepted); IdPs inventoried (built-in Cloudflare +
      Microsoft Entra ID after T105)
- [x] T102 Member tpierson@bitconcepts.tech present, Super Administrator
- [x] T103 Zero Trust org live; team domain renamed via API to
      bitconcepts.cloudflareaccess.com
- [x] T104 Entra app "Cloudflare Zero Trust" registered (client
      e8b2b402…, tenant 6d014029…, single-tenant, Web redirect =
      team-domain callback, security-groups claim on ID token);
      client secret "Cloudflare Zero Trust IdP" expires 2028-10-10,
      value only in Cloudflare's IdP config
- [x] T105 IdP "Microsoft Entra ID" (azureAD) created via API,
      support_groups on
- [x] T106 Dashboard SSO domain bitconcepts.tech — connector created
      via API (POST /accounts/{id}/sso_connectors), domain VERIFIED
      (TXT published via DNS API), connector ENABLED 2026-10-11 after
      the T107 test passed; built-in Cloudflare IdP deleted; both
      Access apps restricted to the Entra IdP only
- [x] T107 IdP sign-in test PASSED 2026-10-11: end-to-end sign-in
      through the App Launcher (enabled via API) as
      tpierson@bitconcepts.tech, identity provider AzureAD, SSO App
      listed — before enforcement
- [x] T108 Enforcement + post-checks 2026-10-11: connector enabled,
      built-in IdP deleted, apps restricted to Entra only; Ops token
      verified working after enable (API kill-switch). OWNER'S FIRST
      DASHBOARD SSO SIGN-IN verified in the Access logs:
      2026-10-12T01:14:56Z, app "SSO App", user
      tpierson@bitconcepts.tech, connection azureAD, allowed=true
      AEO result: 96/100 (check.aeojs.org, 2026-10-11) — AI Access,
      Content Structure, Schema, Citability all 20/20; sole flag
      'Description length' does not match any measured field (all
      six description fields on both pages count 91–198 chars,
      inside the 50–200 range; likely scores the www redirect host)
