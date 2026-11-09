#!/usr/bin/env python3
"""Concept-order and pointer check for the whole spine (Parts I-III, Chaps. 1-22, Appendices A-F).

Extended 2026-11-01 (SPINE-II) from the Part I check: every rule below now applies to every chapter; the new checks are listed under
"Parts II-III checks" at the end of this docstring.

Scans EVERY field of every entry in book/SPINE.md (purpose, learning outcomes, prerequisites, introduces, key results,
computational connection, boundary, sources, figures and worked examples, threads, budget) for the match terms of every row of
book/ledgers/CONCEPTS.md, and reports a violation whenever a term is used in a section that precedes the term's defining section.

Rules
- A term is available from the earliest defining section among the CONCEPTS rows that list it (so an "(op.)" row makes a symbol
  usable before its "(precise)" row). Rows defined in "READER" or "App. X.n" are available everywhere.
- Terms match literally (case-sensitive); an ASCII letter or digit may not touch either end of an ASCII-alphanumeric term end
  (so "E_d" does not match "E_dir" and "LDA" does not match "ALDA"); a term ending in a letter also matches its plural.
- A use inside a clause (text between semicolons) that carries a forward marker -- "forward", "precise in", "treated in" -- is a
  forward mention, not a use; it is counted and listed with --verbose. The marker exempts every term of its clause, so forward
  clauses are kept short.

Other checks
- Every concept row defined in a Part I section has at least one of its terms in that section's entry.
- Every "Used in (Part I)" section of a row is later than its defining section (and, with --write-used, the column is rewritten from
  the scan).
- Prerequisites: every "-> N.M" pointer is to an earlier section; every item pointed to READER.md is a verbatim (case-insensitive)
  substring of READER.md's "Assumed" paragraph.
- Appendices: every A/B/C row's "Used by" list and every D/E row's "(-> ...)" list equals the set of Part I entries that name it;
  every named appendix row exists; the E header's "first pointer" list matches.
- Threads: the opens/advances/closes of Part I entries equal the Part I columns of ledgers/THREADS.md.
- CLAIMS: every "D.n" in a claim's "Derived in" column exists and points back to the claim's section.
- Sizes: 3,000-6,000 words per section, 4-10 sections per chapter, 2-5 learning outcomes per section; chapter headers, the
  appendix headers and the Budget lines agree with the sums.

Parts II-III checks (SPINE-II)
- LIMITS map: the set of row labels of ../../LIMITS.md (every table row outside the superseded R1 hypothesis table and the H6 register,
  which repeat labels) equals the set of rows of the Appendix F map in SPINE.md, each exactly once; the section of each row exists; a row
  with a box label has that label in its section's entry; rows with box "--" (no limitbox: not a literature formula) are listed.
- Exact gaps: every CLOSED-AS-EXACT-GAP row of ../../state/LOOSE-ENDS.md appears ("LE-n") in the "Open problems" field of some entry.
- Deferred computations: every DC-n of ../../state/DEFERRED-COMPUTE.md appears in exactly one Appendix E' row.
- Atlas: every home section named in the Chapter 9 atlas table exists, and each row of the table has exactly one home per cell.
- Size exemptions: SIZE_EXEMPT lists the sections the user directed below the 3,000-word floor.

SPINE-II-REV checks (2026-11-02)
- Defining locations may also be "Front matter" (ordered with READER and the appendices: available everywhere).
- CHAP_EXEMPT lists chapters allowed outside 4-10 sections (Chap. 22: three indexed sections, review item S25).
- Open-item labels: every LE-n and XG-n label occurs in the "Open problems" field of exactly one entry; XG labels run 1..n.
- E′ content tags: every E′ row tags its content items with the section that uses them ("[N.M]"); the tag set equals its "(→ …)" list.
- Limitbox plots: every box named in an entry's key results has an entry in the "Limitbox plots:" item of the same entry's figures field
  (and vice versa); boxes and panels are counted for the Budget.

Usage: python3 check_concepts.py [--verbose] [--write-used]
Exit status 0 when there are no violations.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent
SPINE = BOOK / "SPINE.md"
CONCEPTS = HERE / "CONCEPTS.md"
THREADS = HERE / "THREADS.md"
CLAIMS = HERE / "CLAIMS.md"
READER = BOOK / "READER.md"
CAMPAIGN = BOOK.parent
LIMITS = CAMPAIGN / "LIMITS.md"
LOOSE = CAMPAIGN / "state" / "LOOSE-ENDS.md"
DEFER = CAMPAIGN / "state" / "DEFERRED-COMPUTE.md"
SIZE_EXEMPT = {(1, 1): "user directive 2026-11-01 (succinct background): 2,000 words (rate factorization upfront, 2026-11-02)"}
# Chapters exempt from the 4-10 sections rule (SPINE-II-REV): Chap. 22 became three indexed sections when the outlook merged into 22.1
# (structural review S25; editor decision 8: Chap. 22 is an index, not a restatement).
CHAP_EXEMPT = {22: "S25 / editor decision 8: outlook merged into 22.1; three indexed sections"}

FORWARD = re.compile(r"\bforward\b|precise in|treated in", re.I)
SEC = re.compile(r"(?<![\d.])([1-9]\d?)\.(\d{1,2})(?![\d])")
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]

violations = []
notes = []


def v(msg):
    violations.append(msg)


def num(s):
    return int(s.replace(",", ""))


def order(tag):
    """Order key of a defining location: READER / appendix / front matter -> (0, 0); 'N.M' -> (N, M); 'Chap. N' -> (N, 0)."""
    tag = tag.strip()
    if tag.startswith("READER") or tag.startswith("App") or tag.startswith("Front matter"):
        return (0, 0)
    m = re.match(r"(\d+)\.(\d+)", tag)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    m = re.match(r"Chap\.\s*(\d+)", tag)
    if m:
        return (int(m.group(1)), 0)
    raise ValueError("cannot order defining location %r" % tag)


def fmt(o):
    return "READER/App" if o == (0, 0) else "%d.%d" % o


# ---------------------------------------------------------------- SPINE parsing
spine = SPINE.read_text(encoding="utf-8")
lines = spine.splitlines()

entries = {}  # (ch, sec) -> dict(title, text, fields)
chap_hdr = {}  # ch -> (nsec, words)
cur = None
for ln in lines:
    m = re.match(r"### Chapter (\d+)\. .*\[(?:PLANNED|BLOCKED\([^)]*\)); (\d+) sections, ([\d,]+) words\]", ln)
    if m:
        chap_hdr[int(m.group(1))] = (int(m.group(2)), num(m.group(3)))
        cur = None
        continue
    m = re.match(r"### (\d+)\.(\d+) (.*?)\s+\[status:", ln)
    if m:
        cur = (int(m.group(1)), int(m.group(2)))
        entries[cur] = {"title": m.group(3), "lines": []}
        continue
    if ln.startswith("### ") or ln.startswith("## ") or ln.startswith("---"):
        cur = None
        continue
    if cur is not None:
        entries[cur]["lines"].append(ln)

for key, e in entries.items():
    fields = {}
    name = None
    for ln in e["lines"]:
        m = re.match(r"- ([A-Z][^:]+?):\s?(.*)", ln)
        if m:
            name = m.group(1).strip()
            fields[name] = m.group(2)
        elif name and ln.startswith("  "):
            fields[name] += " " + ln.strip()
        elif ln.strip():
            v("PARSE %d.%d: unrecognized line in the entry: %s" % (key + (ln.strip()[:80],)))
    e["fields"] = fields
    e["text"] = " ".join(fields.values())

order_list = sorted(entries)
if not order_list:
    sys.exit("no entries found in SPINE.md")

# ---------------------------------------------------------------- CONCEPTS parsing
ctext = CONCEPTS.read_text(encoding="utf-8")
crows = []  # dict(concept, defined, used, later, terms, line_index)
clines = ctext.splitlines()
for i, ln in enumerate(clines):
    if not ln.startswith("|") or ln.startswith("|---") or ln.startswith("| Concept"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) != 5:
        v("CONCEPTS line %d: expected 5 columns, found %d" % (i + 1, len(cells)))
        continue
    terms = re.findall(r"`([^`]+)`", cells[4])
    if not terms:
        v("CONCEPTS row %r has no match terms" % cells[0])
    crows.append(dict(concept=cells[0], defined=cells[1], used=cells[2], later=cells[3], terms=terms, idx=i))

avail = {}  # term -> (order, concept)
for r in crows:
    try:
        o = order(r["defined"])
    except ValueError as exc:
        v("CONCEPTS row %r: %s" % (r["concept"], exc))
        continue
    r["order"] = o
    for t in r["terms"]:
        if t not in avail or o < avail[t][0]:
            avail[t] = (o, r["concept"])


def term_regex(t):
    pat = re.escape(t)
    if re.match(r"[A-Za-z0-9]", t[0]):
        pat = r"(?<![A-Za-z0-9])" + pat
    if re.match(r"[A-Za-z]", t[-1]):
        pat = pat + r"(?:e?s)?(?![A-Za-z0-9])"
    elif re.match(r"[0-9]", t[-1]):
        pat = pat + r"(?![A-Za-z0-9])"
    return re.compile(pat)


term_re = {t: term_regex(t) for t in avail}

# ---------------------------------------------------------------- 1. concept order over all fields
uses = {}  # concept -> set of sections where used (not defining)
forward = []
term_hits = {t: 0 for t in avail}
for key in order_list:
    e = entries[key]
    for fname, ftext in e["fields"].items():
        for clause in ftext.split(";"):
            fwd = bool(FORWARD.search(clause))
            for t, rx in term_re.items():
                if not rx.search(clause):
                    continue
                term_hits[t] += 1
                o, concept = avail[t]
                if o > key:
                    if fwd:
                        forward.append("%d.%d %s: '%s' (defined %s) in a forward clause" % (key + (fname, t, fmt(o))))
                    else:
                        v("ORDER %d.%d [%s]: '%s' used before its definition in %s (%s): ...%s..."
                          % (key[0], key[1], fname, t, fmt(o), concept, clause.strip()[:110]))
for r in crows:
    if "order" not in r:
        continue
    secs = set()
    for key in order_list:
        if key == r["order"]:
            continue
        for fname, ftext in entries[key]["fields"].items():
            for clause in ftext.split(";"):
                if FORWARD.search(clause) and key < r["order"]:
                    continue
                if any(term_re[t].search(clause) for t in r["terms"]):
                    secs.add(key)
    r["scan_used"] = sorted(s for s in secs if s > r["order"])

# ---------------------------------------------------------------- 2. definitions present, Used-in column ordered
for r in crows:
    o = r.get("order")
    if o is None or o == (0, 0):
        continue
    if o not in entries:
        v("CONCEPTS row %r: defining section %s is not a spine entry" % (r["concept"], fmt(o)))
        continue
    if not any(term_re[t].search(entries[o]["text"]) for t in r["terms"]):
        v("DEFINE %s: no match term of %r occurs in its defining entry" % (fmt(o), r["concept"]))
    for s in SEC.findall(r["used"]):
        so = (int(s[0]), int(s[1]))
        if so <= o:
            v("USED-IN %r: lists %s, not after its definition %s" % (r["concept"], fmt(so), fmt(o)))
        if so not in entries:
            v("USED-IN %r: %s is not a spine section" % (r["concept"], fmt(so)))

if "--write-used" in sys.argv:
    for r in crows:
        if "scan_used" not in r:
            continue
        col = ", ".join(fmt(s) for s in r["scan_used"]) or "—"
        cells = [r["concept"], r["defined"], col, r["later"], clines[r["idx"]].strip().strip("|").split("|")[4].strip()]
        clines[r["idx"]] = "| " + " | ".join(cells) + " |"
    CONCEPTS.write_text("\n".join(clines) + "\n", encoding="utf-8")
    notes.append("CONCEPTS 'Used in (Part I)' column rewritten from the scan")

# ---------------------------------------------------------------- 3. prerequisites and READER
rtext = READER.read_text(encoding="utf-8")
m = re.search(r"\*\*Assumed:\*\*(.*?)- \*\*Not assumed", rtext, re.S)
assumed = re.sub(r"\s+", " ", m.group(1)).lower() if m else ""
if not assumed:
    v("READER.md: no 'Assumed' paragraph found")
reader_items = 0
for key in order_list:
    pre = entries[key]["fields"].get("Prerequisites") or entries[key]["fields"].get("Prerequisites (concept → section)")
    if pre is None:
        v("PREREQ %d.%d: no Prerequisites field" % key)
        continue
    for item in pre.split(";"):
        if "→" not in item:
            continue
        what, target = item.rsplit("→", 1)
        if "READER" in target:
            for concept in what.split(","):
                c = re.sub(r"\(.*?\)", "", concept).strip().lower()
                reader_items += 1
                if c and c not in assumed:
                    v("READER %d.%d: '%s' is not on READER.md's assumed list" % (key[0], key[1], concept.strip()))
            continue
        if "App." in target:
            continue
        for s in SEC.findall(target):
            so = (int(s[0]), int(s[1]))
            if so >= key:
                v("PREREQ %d.%d: points forward to %s (%s)" % (key[0], key[1], fmt(so), what.strip()))
            elif so not in entries:
                v("PREREQ %d.%d: points to %s, which is not a spine section" % (key[0], key[1], fmt(so)))

# ---------------------------------------------------------------- 4. appendices
APPID = r"[A-F]′?"
app_rows = {}  # 'C.4', 'E.16' -> dict(text, used set or None for 'all', budget)
app_hdr = {}
in_app = False
cur_row = None
for ln in lines:
    if ln.startswith("## Appendices"):
        in_app = True
        continue
    if in_app and ln.startswith("## "):
        break
    if not in_app:
        continue
    m = re.match(r"### Appendix (" + APPID + r")\. .*?\[PLANNED; ([\d,]+) words", ln)
    if m:
        app_hdr[m.group(1)] = num(m.group(2))
        cur_row = None
        continue
    m = re.match(r"- (" + APPID + r")\.(\d+) (.*)", ln)
    if m:
        cur_row = "%s.%s" % (m.group(1), m.group(2))
        app_rows[cur_row] = {"text": m.group(3)}
        continue
    if cur_row and ln.startswith("  "):
        app_rows[cur_row]["text"] += " " + ln.strip()
    elif not ln.startswith("  "):
        if ln.startswith("**Part I needs"):
            app_hdr["E-first"] = ln
        cur_row = None

for rid, row in app_rows.items():
    t = row["text"]
    b = re.findall(r"(?<![\d.,])(\d{1,2},\d{3}|\d{3})(?=\.|\s\()", t)
    row["budget"] = num(b[-1]) if b else 0
    if rid[0] in "ABC":
        mm = re.search(r"Used by: (.*?)(?:\.\s|\.$|;)", t)
        if not mm:
            row["used"] = set()
            if rid[0] != "B" or rid == "B.1":
                v("APP %s: no 'Used by' list" % rid)
        elif mm.group(1).startswith("all"):
            row["used"] = None
        else:
            row["used"] = {(int(a), int(b_)) for a, b_ in SEC.findall(mm.group(1))}
            m2 = re.search(r"Parts II–III: (.*?)(?:\.\s|\.$)", t)
            if m2:
                row["used"] |= {(int(a), int(b_)) for a, b_ in SEC.findall(m2.group(1))}
    else:
        mm = re.search(r"\(→ ([^)]*)\)", t)
        row["used"] = {(int(a), int(b_)) for a, b_ in SEC.findall(mm.group(1))} if mm else set()
        if not mm:
            v("APP %s: no '(→ ...)' list" % rid)

named = {}  # 'C.4' -> set of sections naming it
for key in order_list:
    txt = entries[key]["text"]
    refs = set()
    for mm in re.finditer(r"App\. ((?:" + APPID + r"\.\d+(?:, | and )?)+)", txt):
        refs |= set(re.findall(APPID + r"\.\d+", mm.group(1)))
    refs |= set(re.findall(r"(?<![A-Za-z.])([DEF]′?\.\d+)(?!\d)", txt))
    refs |= set(re.findall(r"(?<![A-Za-z.])([ABC]\.\d+)(?!\d)", txt))
    for r_ in refs:
        named.setdefault(r_, set()).add(key)
for r_, secs in sorted(named.items()):
    if r_ not in app_rows:
        v("APP %s named in %s but has no appendix row" % (r_, ", ".join(fmt(s) for s in sorted(secs))))
for rid, row in sorted(app_rows.items()):
    if row["used"] is None:
        continue
    got = named.get(rid, set())
    if got != row["used"]:
        v("APP %s: row lists %s; entries naming it: %s"
          % (rid, sorted(fmt(s) for s in row["used"]), sorted(fmt(s) for s in got)))
if "E-first" in app_hdr:
    hdr = app_hdr["E-first"]
    for grp, sec in re.findall(r"((?:E\.\d+(?: and )?)+) \((\d+\.\d+)", hdr):
        for e_ in re.findall(r"E\.\d+", grp):
            secs = sorted(named.get(e_, set()))
            if not secs or fmt(secs[0]) != sec:
                v("APP header: %s first pointer given as %s, scan finds %s" % (e_, sec, fmt(secs[0]) if secs else "none"))

# ---------------------------------------------------------------- 5. threads
ttext = THREADS.read_text(encoding="utf-8")
ledger = {}
for ln in ttext.splitlines():
    mm = re.match(r"\| (T\d) [^|]*\| ([^|]*)\| ([^|]*)\| ([^|]*)\|", ln)
    if mm:
        def part1(s):
            return {(int(a), int(b_)) for a, b_ in SEC.findall(s)}
        ledger[mm.group(1)] = {"opens": part1(mm.group(2)), "advances": part1(mm.group(3)), "closes": part1(mm.group(4))}
spine_thr = {t: {"opens": set(), "advances": set(), "closes": set()} for t in ledger}
for key in order_list:
    th = entries[key]["fields"].get("Threads") or entries[key]["fields"].get("Threads (open/advance/close)") or ""
    for verb, slot in (("open", "opens"), ("advance", "advances"), ("close", "closes")):
        for mm in re.finditer(verb + r"s? ((?:T\d(?:, | and )?)+)", th):
            for t in re.findall(r"T\d", mm.group(1)):
                spine_thr.setdefault(t, {"opens": set(), "advances": set(), "closes": set()})[slot].add(key)
for t in sorted(spine_thr):
    for slot in ("opens", "advances", "closes"):
        a, b_ = spine_thr[t][slot], ledger.get(t, {}).get(slot, set())
        if a != b_:
            v("THREAD %s %s: SPINE %s, THREADS.md %s" % (t, slot, sorted(fmt(s) for s in a), sorted(fmt(s) for s in b_)))

# ---------------------------------------------------------------- 6. claims
for ln in CLAIMS.read_text(encoding="utf-8").splitlines():
    mm = re.match(r"\| (II?-\d+) \| [^|]*\| ([^|]*)\| ([^|]*)\|", ln)
    if not mm:
        continue
    secs = {(int(a), int(b_)) for a, b_ in SEC.findall(mm.group(2))}
    for s in secs:
        if s not in entries:
            v("CLAIM %s: section %s is not a spine entry" % (mm.group(1), fmt(s)))
    for d in re.findall(r"D\.\d+", mm.group(3)):
        if d not in app_rows:
            v("CLAIM %s: %s does not exist" % (mm.group(1), d))
        elif not (app_rows[d]["used"] & secs):
            v("CLAIM %s: %s does not point to %s" % (mm.group(1), d, sorted(fmt(s) for s in secs)))

# ---------------------------------------------------------------- 7. sizes and totals
budgets = {}
for key in order_list:
    b = entries[key]["fields"].get("Budget (words)", "")
    mm = re.search(r"([\d,]+)", b)
    if not mm:
        v("SIZE %d.%d: no budget" % key)
        continue
    budgets[key] = num(mm.group(1))
    if not 3000 <= budgets[key] <= 6000 and key not in SIZE_EXEMPT:
        v("SIZE %d.%d: budget %d outside 3,000-6,000" % (key + (budgets[key],)))
    lo = entries[key]["fields"].get("Learning outcomes", "")
    n_lo = len({x for x in re.findall(r"\(([ivx]+)\)", lo) if x in ROMAN})
    if not 2 <= n_lo <= 5:
        v("SIZE %d.%d: %d learning outcomes (2-5 required)" % (key + (n_lo,)))
chap_sum = {}
for (c, s_), b in budgets.items():
    chap_sum.setdefault(c, []).append(b)
for c in sorted(chap_sum):
    n, w = len(chap_sum[c]), sum(chap_sum[c])
    if not 4 <= n <= 10 and c not in CHAP_EXEMPT:
        v("SIZE Chap. %d: %d sections (4-10 required)" % (c, n))
    if chap_hdr.get(c) != (n, w):
        v("TOTAL Chap. %d header says %s, entries give (%d sections, %d words)" % (c, chap_hdr.get(c), n, w))
PARTS = [("Part I, Chaps. 1–7", range(1, 8)), ("Chap. 8", range(8, 9)), ("Part II, Chaps. 9–17", range(9, 18)),
         ("Part III, Chaps. 18–22", range(18, 23))]
part_tot = {}
for label, rng in PARTS:
    secs = [k for k in budgets if k[0] in rng]
    nsec_, words_ = len(secs), sum(budgets[k] for k in secs)
    bud = re.search(re.escape(label) + r"[^:\n]*: (\d+) sections?, ([\d,]+) words.*?\(([\d,]+)\): \*\*([\d,]+) words", spine)
    if not bud:
        if secs:
            v("TOTAL: Budget line for %s not found" % label)
        continue
    if (int(bud.group(1)), num(bud.group(2))) != (nsec_, words_):
        v("TOTAL Budget line %s says %s sections, %s words; entries give %d, %d" % (label, bud.group(1), bud.group(2), nsec_, words_))
    nch = len({k[0] for k in secs})
    if num(bud.group(3)) != 900 * nch:
        v("TOTAL Budget line %s: outlines and summaries %s != 900 x %d chapters" % (label, bud.group(3), nch))
    if num(bud.group(2)) + num(bud.group(3)) != num(bud.group(4)):
        v("TOTAL Budget line %s: %s + %s != %s" % (label, bud.group(2), bud.group(3), bud.group(4)))
    part_tot[label] = num(bud.group(4))
nsec = len(budgets)
allwords = sum(budgets.values())
app_sum = {}
for rid, row in app_rows.items():
    k_ = rid.split(".")[0]
    app_sum[k_] = app_sum.get(k_, 0) + row["budget"]
APPS = ["A", "B", "C", "D", "E", "F"]
for a in APPS:
    if app_hdr.get(a) != app_sum.get(a):
        v("TOTAL App. %s header says %s, rows give %s" % (a, app_hdr.get(a), app_sum.get(a)))
abud = re.search(r"Appendices A–F: A ([\d,]+) · B ([\d,]+) · C ([\d,]+) · D ([\d,]+) · E ([\d,]+) · F ([\d,]+) = ([\d,]+) words", spine)
app_total = None
if abud:
    vals = [num(x) for x in abud.groups()]
    if vals[:6] != [app_sum.get(a) for a in APPS] or sum(vals[:6]) != vals[6]:
        v("TOTAL Budget appendix line %s disagrees with rows %s" % (vals, [app_sum.get(a) for a in APPS]))
    app_total = vals[6]
else:
    v("TOTAL: Budget line for the appendices not found")
tot = re.search(r"Front matter: about ([\d,]+) words.*?\*\*Total: about ([\d,]+) words", spine, re.S)
if tot and app_total is not None:
    want = sum(part_tot.values()) + app_total + num(tot.group(1))
    if num(tot.group(2)) != want:
        v("TOTAL book: Budget says %s, parts + appendices + front matter give %d" % (tot.group(2), want))
else:
    v("TOTAL: front-matter or book total line not found")

# ---------------------------------------------------------------- 8. Parts II-III coverage checks
def section_exists(tag):
    m_ = re.match(r"(\d+)\.(\d+)$", tag.strip())
    return bool(m_) and (int(m_.group(1)), int(m_.group(2))) in entries

ID_RE = r"(L[0-9A-Za-z′\-]*|LB1-\d+|B2-L\d+|R1-L\d+|LU\d+′?|LT\d+|CW\d-L\d+|CW4-[a-g]|CMPMC-(?:AUD|DEV)-L\d+|L-[A-Za-z]+\d*′?)"
lim_ids = []
if LIMITS.exists():
    ltext = LIMITS.read_text(encoding="utf-8")
    body = ltext.split("## H6 exact-gap register")[0]
    for ln in body.splitlines():
        mm = re.match(r"\| " + ID_RE + r" \|", ln)
        if mm and not ln.startswith("| # "):
            lim_ids.append(mm.group(1))
    dup = sorted({x for x in lim_ids if lim_ids.count(x) > 1})
    if dup:
        notes.append("LIMITS labels occurring in two rows of LIMITS.md (mapped once): %s" % ", ".join(dup))
lim_set = set(lim_ids)
fmap = {}
in_f = False
for ln in lines:
    if ln.startswith("### Appendix F"):
        in_f = True
        continue
    if in_f and (ln.startswith("### ") or ln.startswith("## ")):
        break
    if in_f:
        mm = re.match(r"\| (\S+) \| (\d+\.\d+) \| ([^|]+?) \|", ln)
        if mm:
            if mm.group(1) in fmap:
                v("F-MAP %s mapped twice" % mm.group(1))
            fmap[mm.group(1)] = (mm.group(2), mm.group(3).strip())
no_box = []
for rid in sorted(lim_set):
    if rid not in fmap:
        v("F-MAP: LIMITS row %s is not mapped" % rid)
for rid, (sec, box) in sorted(fmap.items()):
    if rid not in lim_set:
        v("F-MAP: %s is not a LIMITS row" % rid)
    if not section_exists(sec):
        v("F-MAP %s: section %s does not exist" % (rid, sec))
        continue
    if box in ("—", "--"):
        no_box.append(rid)
    elif box not in entries[tuple(int(x) for x in sec.split("."))]["text"]:
        v("F-MAP %s: box '%s' not named in the entry of %s" % (rid, box, sec))
if fmap:
    notes.append("LIMITS map: %d rows, %d mapped, %d with a limitbox, %d with no limitbox (key result only): %s"
                 % (len(lim_set), len(set(fmap) & lim_set), len(set(fmap) & lim_set) - len(no_box), len(no_box), ", ".join(no_box)))

if LOOSE.exists():
    ceg = re.findall(r"^\| (LE-\d+) \[CLOSED-AS-EXACT-GAP", LOOSE.read_text(encoding="utf-8"), re.M)
    op = " ".join(e["fields"].get(f, "") for e in entries.values() for f in e["fields"] if f.startswith("Open problems"))
    have = set(re.findall(r"LE-\d+", op))
    miss = [x for x in ceg if x not in have]
    for x in miss:
        v("GAP %s (CLOSED-AS-EXACT-GAP) is in no 'Open problems' field" % x)
    notes.append("exact gaps: %d CLOSED-AS-EXACT-GAP rows, %d placed in open-problems fields" % (len(ceg), len(ceg) - len(miss)))
    # SPINE-II-REV (editor decision 8): every open-item label (LE-n, XG-n) has exactly one home, i.e. it occurs in the
    # "Open problems" field of exactly one entry; XG labels are numbered 1..n without holes.
    homes = {}
    for key in order_list:
        for f, txt in entries[key]["fields"].items():
            if f.startswith("Open problems"):
                for lab in set(re.findall(r"\b(?:LE|XG)-\d+", txt)):
                    homes.setdefault(lab, []).append(key)
    for lab, ks in sorted(homes.items()):
        if len(ks) != 1:
            v("GAP %s has %d homes (%s); exactly one is required" % (lab, len(ks), ", ".join(fmt(k) for k in ks)))
    xg = sorted(int(l.split("-")[1]) for l in homes if l.startswith("XG"))
    if xg and xg != list(range(1, len(xg) + 1)):
        v("GAP: XG labels are not numbered 1..%d without holes: %s" % (len(xg), xg))
    notes.append("open-item labels: %d LE and %d XG labels, each in exactly one open-problems field"
                 % (sum(1 for l in homes if l.startswith("LE")), len(xg)))
if DEFER.exists():
    dcs = re.findall(r"^\| (DC-\d+) \|", DEFER.read_text(encoding="utf-8"), re.M)
    epr = {rid: row for rid, row in app_rows.items() if rid.startswith("E.") and int(rid.split(".")[1]) >= 14}
    for d in dcs:
        n_ = [rid for rid, row in epr.items()
              if d.split("-")[1] in re.findall(r"\d+", " ".join(re.findall(r"DC-[\d, ]+", row["text"])))]
        if len(n_) != 1:
            v("E spec: %s appears in %d spec rows (E.14–E.27) (%s)" % (d, len(n_), ", ".join(n_)))
    notes.append("deferred computations: %d DC items checked against %d spec rows (E.14–E.27)" % (len(dcs), len(epr)))
    # SPINE-II-REV (S19): pointers by content. Every content item of an E′ row carries the section that uses it as "[N.M]" (several
    # allowed, "[N.M, N.M]"); the set of those sections must equal the row's "(→ …)" list, which the appendix check above already ties
    # to the entries that name the row.
    for rid, row in sorted(epr.items()):
        content = row["text"].split("(→")[0]
        tagged = {(int(a), int(b_)) for grp in re.findall(r"\[([\d., ]+)\]", content) for a, b_ in SEC.findall(grp)}
        if not tagged:
            v("E spec %s: no content item carries its section tag [N.M]" % rid)
        elif tagged != row["used"]:
            v("E spec %s: content tags %s differ from the (→ …) list %s"
              % (rid, sorted(fmt(s) for s in tagged), sorted(fmt(s) for s in row["used"])))
atlas = False
cells = 0
skip_cols = set()
for ln in lines:
    if ln.startswith("**Atlas"):
        atlas = True
        continue
    if atlas and not ln.startswith("|"):
        if cells:
            break
        continue
    if atlas and ln.startswith("| Excitation"):
        # Chapter 9 merge (2026-11-07): the printed Table 9.1 has a Sector column, which names sectors, not homes
        hdr = [c.strip() for c in ln.strip().strip("|").split("|")][1:]
        skip_cols = {i for i, h in enumerate(hdr) if h == "Sector"}
        continue
    if atlas and ln.startswith("|") and not ln.startswith("|---"):
        cs = [c.strip() for c in ln.strip().strip("|").split("|")][1:]
        for i, c in enumerate(cs):
            # "○" (editor ruling R1, Ch9): allowed at leading order, computed in no section; no home
            if i in skip_cols or c in ("—", "", "○"):
                continue
            homes = re.findall(r"\d+\.\d+", c)
            cells += 1
            if len(homes) != 1:
                v("ATLAS cell %r in row %r has %d homes" % (c, ln[:40], len(homes)))
            for h in homes:
                if not section_exists(h):
                    v("ATLAS home %s does not exist" % h)
if cells:
    notes.append("atlas: %d filled cells, one home each" % cells)

# SPINE-II-REV (S1, editor decision 1): every limitbox named in an entry's key results has its comparison plot listed in the same entry's
# "Limitbox plots:" item (Figures field), and vice versa; panels are counted for the Budget.
NUMW = {"one": 1, "two": 2, "three": 3}
tot_boxes = tot_panels = 0
for key in order_list:
    flds = entries[key]["fields"]
    kr = flds.get("Key results", "") or flds.get("Key results (derived / cited)", "")
    named_boxes = set(re.findall(r"Limit (\d+\.\d+[a-z])", kr))
    fig = next((t for f, t in flds.items() if f.startswith("Figures")), "")
    mm = re.search(r"Limitbox plots: (.*)", fig)
    if not mm:
        if named_boxes or key[0] >= 8:
            v("PLOTS %d.%d: no 'Limitbox plots:' item in the figures field" % key)
        continue
    pending, panels = [], {}
    for t in re.finditer(r"(\d+\.\d+[a-z])|\((one|two|three) panel", mm.group(1)):
        if t.group(1):
            pending.append(t.group(1))
        else:
            for b_ in pending:
                panels[b_] = NUMW[t.group(2)]
            pending = []
    for b_ in pending:
        v("PLOTS %d.%d: box %s has no panel count" % (key + (b_,)))
    if set(panels) != named_boxes:
        v("PLOTS %d.%d: key results name %s, plots list %s" % (key + (sorted(named_boxes), sorted(panels))))
    tot_boxes += len(panels)
    tot_panels += sum(panels.values())
notes.append("limitbox plots: %d boxes, %d comparison panels listed in the figures fields" % (tot_boxes, tot_panels))

# ---------------------------------------------------------------- report
print("check_concepts.py: %d entries, %d concept rows, %d match terms, %d READER items, %d appendix rows"
      % (len(entries), len(crows), len(avail), reader_items, len(app_rows)))
print("totals: %d sections, %d words; by chapter %s; appendices %s (sum %d)"
      % (nsec, allwords, {c: sum(x) for c, x in sorted(chap_sum.items())}, dict(sorted(app_sum.items())), sum(app_sum.values())))
dead = [t for t, n in term_hits.items() if n == 0]
print("terms with no hit in any entry: %d %s" % (len(dead), dead if "--verbose" in sys.argv else ""))
print("forward mentions (allowed): %d" % len(forward))
if "--verbose" in sys.argv:
    for f in forward:
        print("  fwd  " + f)
for n_ in notes:
    print("note: " + n_)
print("violations: %d" % len(violations))
for x in violations:
    print("  " + x)
sys.exit(1 if violations else 0)
