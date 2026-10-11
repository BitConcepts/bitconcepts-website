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
