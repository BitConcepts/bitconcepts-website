#!/usr/bin/env python3
"""bitconcepts-website CI checks (stdlib only).

Content sanity for every branch: the three pages exist and close,
every JSON-LD block parses, every internal href/src resolves to a
file in the tree. Guard polarity by branch:
  main    — NO noindex anywhere: pages, robots.txt Disallow-all, and
            the _headers X-Robots-Tag line are all failures.
  staging — the guards MUST be present on all three.
"""
import json, posixpath, re, sys
from pathlib import Path

root = Path.cwd()
branch = sys.argv[1] if len(sys.argv) > 1 else ""
PAGES = ["index.html", "research/index.html", "research/indus-script/index.html"]
failures = []

def check(cond, msg):
    if not cond:
        failures.append(msg)

tree = {p.relative_to(root).as_posix() for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts}

for pg in PAGES:
    f = root / pg
    check(f.exists() and f.stat().st_size > 1000, f"{pg}: missing or trivial")
    if not f.exists():
        continue
    html = f.read_text(errors="replace")
    check("</html>" in html, f"{pg}: no closing </html>")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',
                         html, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            failures.append(f"{pg}: JSON-LD does not parse: {e}")
    base = posixpath.dirname(pg)
    for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
        u = m.group(1)
        if u.startswith(("http://", "https://", "mailto:", "#", "data:", "//")):
            continue
        u = u.split("#")[0].split("?")[0]
        if not u or u.startswith("/cdn-cgi/"):
            continue
        rel = (u.lstrip("/") if u.startswith("/")
               else posixpath.normpath(posixpath.join(base, u)))
        cands = [rel, rel + "/index.html"] if not rel.endswith(".html") else [rel]
        if rel.endswith("/"):
            cands = [rel + "index.html"]
        check(any(c in tree for c in cands),
              f"{pg}: internal link does not resolve: {u}")

robots = (root / "robots.txt").read_text() if (root / "robots.txt").exists() else ""
headers = (root / "_headers").read_text() if (root / "_headers").exists() else ""
disallow_all = re.search(r"(?m)^Disallow:\s*/\s*$", robots) is not None

if branch == "main":
    for pg in PAGES:
        if (root / pg).exists():
            check("noindex" not in (root / pg).read_text(),
                  f"GUARD: {pg} carries noindex on main")
    check(not disallow_all, "GUARD: robots.txt is Disallow-all on main")
    check("X-Robots-Tag" not in headers, "GUARD: _headers X-Robots-Tag on main")
elif branch == "staging":
    for pg in PAGES:
        if (root / pg).exists():
            check("noindex" in (root / pg).read_text(),
                  f"GUARD: {pg} is missing its noindex on staging")
    check(disallow_all, "GUARD: staging robots.txt is not Disallow-all")
    check("X-Robots-Tag" in headers, "GUARD: staging _headers lacks X-Robots-Tag")

if failures:
    print("SITE CHECKS FAILED:")
    for x in failures:
        print(" -", x)
    sys.exit(1)
print(f"site checks PASS on {branch or '(unknown branch)'}: "
      f"{len(PAGES)} pages, JSON-LD, internal links, guard polarity")
