#!/usr/bin/env python3
"""Rank sentences of LaTeX prose by binding and parse-depth risk (prose-review pattern 27).

Usage: binding.py [--summary] [--min N] FILE.tex [FILE.tex ...]

Each flagged sentence is printed with the line of its paragraph, its flags and the sentence text.
Flags (a flag is a candidate for the reader to check, not a verdict; the tool misses many failures):
  PRON      pronoun with three or more number-compatible noun candidates in this and the previous sentence
  PROP      bare this/that/these/those/which standing for a proposition, or a sentence opening on one
  KIND      such X / all the same / both / either / the former / the latter / that of / those of / the rest
  REL       relational noun without its arguments (difference, mismatch, shift, missing, in between, ...)
  CHAIN     this sentence and the previous one both open on a pointer back
  GARDEN    reduced relative that a parser takes for a main verb, or a heavy subject with a participle
  HEAVY     subject of more than ten words, or containing a clause, before the main verb
  PPCHAIN   three or more stacked prepositional/genitive phrases
  APPOS     defining apposition of five or more words
  DEPTH     dependency depth above 9 or four or more subordinate/coordinate clauses
Requires spaCy with en_core_web_sm (or en_core_web_lg if installed).
"""
import re
import sys
from pathlib import Path

import spacy

try:
    NLP = spacy.load("en_core_web_lg", disable=["ner"])
except OSError:
    NLP = spacy.load("en_core_web_sm", disable=["ner"])

ABBR = {r"\bSects?\.": "Sect", r"\bEqs?\.": "Eq", r"\bRefs?\.": "Ref", r"\bFigs?\.": "Fig", r"\bChaps?\.": "Chap",
        r"\bApp\.": "App", r"\be\.g\.": "for example", r"\bi\.e\.": "that is", r"\bcf\.": "compare", r"\bet al\.": "et al",
        r"\bvs\.": "versus", r"\bapprox\.": "approximately", r"\bNo\.": "No"}
SKIP_ENV = r"equation|align|gather|multline|eqnarray|tabular|longtable|tikzpicture|verbatim|lstlisting|minted|displaymath|table"
POINTER_OPEN = re.compile(r"^(It|Its|This|These|That|Those|Such|They|Their|Both|The latter|The former|Here|There|Each|Either)\b")
KIND = re.compile(r"\bsuch (?!as\b|that\b|a\b)[a-z]+|\ball the same\b|\bthe (?:former|latter)\b|\b(?:that|those) of\b|\bthe rest\b"
                  r"|\bthe remainder\b|\bthe one\b|\bthe other\b(?! \w+ (?:hand|way))|\bin between\b")
REL = {"difference", "mismatch", "ratio", "shift", "excess", "deficit", "remainder", "correction", "denominator",
       "numerator", "offset", "discrepancy"}
REL_ADJ = {"missing", "remaining", "extra", "former", "latter"}
PRONS = {"it", "its", "itself", "they", "them", "their", "themselves"}
DEMS = {"this", "that", "these", "those"}


def strip(text):
    """LaTeX source -> list of (line, paragraph text). Math becomes a noun placeholder, references a proper noun."""
    t = re.sub(r"(?<!\\)%.*", "", text)
    lines = t.split("\n")
    paras, buf, start = [], [], 1
    for i, ln in enumerate(lines + [""], 1):
        if ln.strip() == "":
            if buf:
                paras.append((start, "\n".join(buf)))
            buf, start = [], i + 1
        else:
            buf.append(ln)
    out = []
    for line, p in paras:
        p = re.sub(r"(?s)\\begin\{(%s)\*?\}.*?\\end\{\1\*?\}" % SKIP_ENV, " Xeq ", p)
        p = re.sub(r"(?s)\\\[.*?\\\]", " Xeq ", p)
        p = re.sub(r"\$\$.*?\$\$", " Xeq ", p, flags=re.S)
        p = re.sub(r"\\\((.*?)\\\)", " Xm ", p)
        p = re.sub(r"\$[^$]*\$", " Xm ", p)
        p = re.sub(r"\\SI\{([^}]*)\}\{[^}]*\}", r" \1 units", p)
        p = re.sub(r"\\num\{([^}]*)\}", r" \1", p)
        p = re.sub(r"\\(?:c|C)ref(?:range)?\*?\{[^}]*\}(?:\{[^}]*\})?|\\(?:eq|page)?ref\{[^}]*\}", " Ref1 ", p)
        p = re.sub(r"~?\\cites?(?:\[[^\]]*\])*\{[^}]*\}", "", p)
        p = re.sub(r"\\label\{[^}]*\}|\\index\{[^}]*\}", "", p)
        p = re.sub(r"\\(?:caption|emph|textit|textbf|mathrm|text|keyterm|term|enquote)\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", p)
        p = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\{[^}]*\})*(?:\[[^\]]*\])?", " ", p)
        p = re.sub(r"\\(?:sub)*section\*?\{[^}]*\}|\\chapter\*?\{[^}]*\}|\\paragraph\*?\{[^}]*\}", " ", p)
        p = re.sub(r"\\[a-zA-Z]+\*?", " ", p)
        p = re.sub(r"[{}~]", " ", p).replace("``", '"').replace("''", '"').replace("--", "-")
        for k, v in ABBR.items():
            p = re.sub(k, v, p)
        p = re.sub(r"\s+", " ", p).strip()
        if len(p.split()) >= 6 and re.search(r"[a-z]{3,} [a-z]{3,}", p):
            out.append((line, p))
    return out


def depth(tok):
    d = 0
    while tok.head.i != tok.i:
        tok, d = tok.head, d + 1
    return d


def nouns(span):
    return [t for t in span if t.pos_ in ("NOUN", "PROPN") and t.text not in ("Xm", "Xeq", "Ref1", "units")]


def number(t):
    n = t.morph.get("Number")
    return n[0] if n else ("Plur" if t.tag_ in ("NNS", "NNPS") else "Sing")


def flags(sent, prev):
    f = []
    words = [t for t in sent if not t.is_punct]
    first = sent.text.strip()
    if POINTER_OPEN.match(first) and prev is not None and POINTER_OPEN.match(prev.text.strip()):
        f.append("CHAIN")
    for t in sent:
        lw = t.lower_
        if lw in PRONS and t.pos_ == "PRON" or lw in ("its", "their"):
            if lw == "it" and t.dep_ in ("nsubj", "expl") and any(c.lower_ in ("to", "that") for c in t.head.subtree if c.i > t.head.i):
                continue  # pleonastic "it is ... to/that"
            want = "Plur" if lw in ("they", "them", "their", "themselves") else "Sing"
            cand = {c.lemma_ for c in (nouns(prev) if prev is not None else []) + nouns(sent[:t.i - sent.start])
                    if number(c) == want and c.dep_ not in ("compound", "npadvmod")}
            if len(cand) >= 3:
                f.append(f"PRON[{t.text}:{len(cand)}]")
        if lw in DEMS and t.pos_ == "PRON" and t.dep_ in ("nsubj", "nsubjpass", "dobj", "pobj"):
            f.append(f"PROP[{t.text}]")
        if t.lemma_ in REL and t.pos_ == "NOUN" and not any(c.dep_ == "prep" and c.lower_ in ("of", "between", "from", "in", "to", "on")
                                                            for c in t.children) and not any(c.dep_ in ("compound", "amod", "poss", "nmod") for c in t.children):
            f.append(f"REL[{t.text}]")
        if lw in REL_ADJ and t.dep_ == "amod":
            f.append(f"REL[{t.text}]")
        if lw == "both" and t.dep_ != "preconj" and t.dep_ != "det":
            f.append("KIND[both]")
        if t.tag_ == "VBN" and t.dep_ == "acl" and t.head.dep_ in ("nsubj", "nsubjpass") and t.i < t.head.head.i:
            f.append(f"GARDEN[{t.head.text} {t.text}]")
        if t.tag_ in ("VBN", "VBD") and any(c.dep_ == "nsubj" for c in t.children) and any(
                c.dep_ == "conj" and c.tag_ in ("VBZ", "VBP", "VBD") for c in t.children):
            f.append(f"GARDEN[{t.text}]")
        if t.dep_ in ("nsubj", "nsubjpass") and t.head.pos_ in ("VERB", "AUX"):
            sub = list(t.subtree)
            if len([w for w in sub if not w.is_punct]) > 10 or any(w.dep_ in ("relcl", "acl") for w in sub if w is not t):
                if len(sub) > 6:
                    f.append(f"HEAVY[{len(sub)}]")
        if t.dep_ == "appos" and len(list(t.subtree)) >= 5:
            f.append("APPOS")
        if t.dep_ == "pobj":
            n, u = 0, t
            while True:
                pp = [c for c in u.children if c.dep_ == "prep" and c.lower_ in ("of", "in", "at", "on", "for", "from", "with", "to")]
                pob = [g for c in pp for g in c.children if g.dep_ == "pobj"]
                if not pob:
                    break
                n, u = n + 1, pob[0]
            if n >= 2 and (t.head.head is None or t.head.head.dep_ != "pobj"):
                f.append(f"PPCHAIN[{n + 1}]")
    for m in KIND.finditer(sent.text):
        f.append(f"KIND[{m.group(0)}]")
    clauses = sum(1 for t in sent if t.dep_ in ("relcl", "acl", "advcl", "ccomp", "csubj") or (t.dep_ == "conj" and t.pos_ == "VERB"))
    dmax = max(depth(t) for t in sent)
    if dmax > 9 or clauses >= 4:
        f.append(f"DEPTH[d{dmax},c{clauses}]")
    seen, uniq = set(), []
    for x in f:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq, len(words)


def scan(path):
    res, nw = [], 0
    for line, p in strip(Path(path).read_text()):
        doc = NLP(p)
        prev = None
        for s in doc.sents:
            fl, n = flags(s, prev)
            nw += n
            if fl:
                res.append((line, fl, s.text.strip()))
            prev = s
    return res, nw


def main(argv):
    summary = "--summary" in argv
    mn = 1
    if "--min" in argv:
        mn = int(argv[argv.index("--min") + 1])
    files = [a for a in argv if a.endswith(".tex")]
    if not files:
        print(__doc__)
        return 0
    tot_s, tot_w = 0, 0
    for fn in files:
        res, nw = scan(fn)
        res = [r for r in res if len(r[1]) >= mn]
        tot_s += len(res)
        tot_w += nw
        if summary:
            print(f"{fn}: {nw} words, {len(res)} flagged sentences ({1000 * len(res) / max(nw, 1):.1f} per 1000 words)")
        else:
            for line, fl, s in res:
                print(f"{fn}:{line}: {' '.join(fl)}\n    {s}")
    print(f"TOTAL: {tot_w} words, {tot_s} flagged sentences ({1000 * tot_s / max(tot_w, 1):.1f} per 1000 words)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
