# Spec 003 — /research/ "Related research" cross-link to Axiovex Systems

Owner: Tristen Pierson. Directed 2026-10-11 (paired launch with the
Axiovex research hub; the two pages cross-link and go live together).

## Purpose

Axiovex Systems gains a research hub at
https://axiovexsystems.com/research/ presenting its own research
program, which runs the same evidence-first method as this program
on fundamental physics questions. The two programs' public pages
link to each other so a reader of either record can find the other.

## Requirements

- FR-001: `/research/` gains a closing "Related research" section
  per wireframe WF-04: one short paragraph and one link to
  https://axiovexsystems.com/research/. Plain framing only — no
  internal machinery (no claim ids, no scores, no spec numbers, no
  internal repo names beyond what the page already shows publicly).
- FR-002: Recorded tension, resolved as an exception. Spec 001
  FR-006 and WF-02 state the tracker names no other company or
  project. This section is a deliberate, owner-directed exception:
  a single end-of-page cross-link, after all tracker content, to
  the sister company the homepage already routes consulting to.
  It makes no research claims about the Axiovex program beyond the
  one framing sentence, and no Axiovex content enters the tracker
  body. The owner ratifies the exception at production promotion.
  **Ratified by the owner 2026-10-11 20:19 EDT** (see History).
- FR-003: The Axiovex hub links back to
  https://bitconcepts.tech/research/; both pages go live together.
  Until the Axiovex page is live, the link may return 404 — that is
  expected during staging and is not a defect of this change.
- FR-004: Verification follows Spec 001 FR-007: Playwright
  screenshots at desktop and mobile widths on staging, compared
  against docs/wireframes/, before any production promotion.
  Production promotion remains owner-gated.
- FR-005: llms.txt gains one line under Research naming the
  cross-link. No other pages change. Mail DNS is never touched.

## Acceptance

Staging serves the WF-04 section, screenshot-verified at desktop
and mobile widths; the link points at
https://axiovexsystems.com/research/ (reachability confirmed when
the Axiovex hub goes live); production promotion only after owner
review.

## History

- 2026-10-11: Section added in commit `059117f` to
  `research/index.html` (the tracker's then-location at `/research/`),
  merged to staging (`6a12729`), screenshot-verified. The llms.txt
  lines (FR-005) and the WF-04 wireframe also landed on staging.
- 2026-10-11 (T016 restructure): the tracker moved to
  `research/indus-script/index.html` and `/research/` became the
  program home. During that restructure's merge-conflict resolution
  (`7b04ab8`), the WF-04 section markup was dropped; the llms.txt
  lines and WF-04 survived on staging. A whole-branch
  staging→main promotion was ruled out: the branch diff carries
  staging guards (robots.txt Disallow, _headers X-Robots-Tag,
  noindex metas) that would deindex production.
- 2026-10-11 (remedy, Option A — surgical): the owner approved
  production promotion at 20:19 EDT, ratifying the FR-002
  exception to Spec 001 FR-006 / WF-02. The section was re-applied
  in its approved WF-04 form to
  `research/indus-script/index.html` — closing the tracker after
  its method section, before the footer, existing section
  furniture only, no new CSS — verified on staging, then promoted
  to main by cherry-picking only the four Spec 003 files
  (tracker page, llms.txt, WF-04 wireframe, this spec). No
  staging guard file (robots.txt, _headers, index.html, any
  noindex meta) moved to main.
