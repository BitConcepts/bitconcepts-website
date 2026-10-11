# Wireframes — BitConcepts site (bitconcepts.tech)

Approved direction: Tristen, 2026-10-11 — "Interstitial homepage +
tracker at /research/" (chosen in the website chat over tracker-as-
homepage and pure-redirect-only).

## WF-01 — Homepage interstitial `/`

Single centered card on a charcoal field, no navigation, no other
pages linked except research and the destination:

```
+----------------------------------------------------------+
|                   [B logo, 148px]                        |
|                     BITCONCEPTS                          |
|                                                          |
|               Consulting has a new home.                 |
|                                                          |
|   BitConcepts' consulting and engineering services are   |
|   now delivered through Axiovex Systems. You're being    |
|   redirected there…                                      |
|                                                          |
|         [ Continue to Axiovex Systems → ]                |
|                                                          |
|   Redirecting in 5 seconds.  Stay on this page           |
|   ----------------------------------------------------   |
|   Here for the research? BitConcepts research            |
|   continues here: bitconcepts.tech/research/             |
|                                                          |
|   BitConcepts, LLC · tpierson@bitconcepts.tech           |
+----------------------------------------------------------+
```

- Branding: the BitConcepts mark (blue circuit "B", sampled blue
  #03a1d0) on charcoal — never Axiovex branding on this page.
- Behavior: JS countdown 5s → axiovexsystems.com (location.replace);
  noscript fallback meta-refresh at 8s; "Stay on this page" cancels
  the countdown; the research link is a normal navigation (never
  redirected).
- Mobile (≤480px): card padding tightens, logo 112px, button full width.

## WF-02 — Research tracker `/research/`

- BitConcepts-branded, same card/palette system, wider content layout
  when the full tracker lands.
- Content is supplied by the Glossa-Lab program (verified source pack,
  2026-10-11) and built in the Glossa-Lab chat; this repo hosts it.
  Until that content is integrated, the page is an honest holding
  page: it states the program's headline status (not deciphered —
  a well-audited, unproven hypothesis) and links to the program repo.
  No invented values, no placeholder numbers.
- Hard rules for the finished tracker: never claim decipherment;
  negative results at the same prominence as positive ones; no other
  company or project named; ownership line: "Indus decipherment
  research is a BitConcepts program."

## WF-03 — Everything else (any other path)

No page. A Cloudflare redirect rule sends any other path on
bitconcepts.tech (and www) to https://axiovexsystems.com/ with a
301. Mail DNS records are never touched by any rule.
