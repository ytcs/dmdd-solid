#!/usr/bin/env python3
"""Prose, style and standalone lint for LaTeX/Markdown book sources.

usage: lint.py FILE [FILE ...] [--banned BANNED-TERMS.txt] [--max-dash 1.0] [--json]

Checks: banned internal terms (regex per line), AI-prose phrases, em-dash density per paragraph,
empty signposting, stacked hedges, vague quantifiers, "it can be shown" style rugs, overlong
sentences, sentence-length monotony, equations not followed by punctuation (LaTeX display math).
Exit code 1 if any blocking hit (banned term or rug phrase).
"""
import argparse, json, re, statistics, sys

AI_PHRASES = [r"\bdelve\w*", r"\bcrucial\w*", r"\bpivotal\b", r"\bintricat\w+", r"\brealm\b", r"\blandscape\b",
    r"\btapestry\b", r"\bseamless\w*", r"\bleverag\w+", r"\bunderscor\w+", r"\bshowcas\w+", r"\bnotably\b",
    r"\bplays? an? (key|vital|crucial|pivotal|important) role\b", r"\ba wide (range|array|variety) of\b",
    r"\bcutting[- ]edge\b", r"\bpowerful\b", r"\belegant\w*", r"\bunlock\w*", r"\bempower\w*",
    r"\bin the realm of\b", r"\bgame[- ]chang\w+", r"\bholistic\b", r"\bparadigm\b", r"\bnuanced\b"]
SIGNPOST = [r"\bin this (section|chapter) we will\b", r"\blet us now turn\b", r"\bit is worth noting\b",
    r"\bit is important to note\b", r"\bit should be noted\b", r"\bneedless to say\b", r"\bas we will see\b",
    r"\bit goes without saying\b", r"\binterestingly,", r"\bimportantly,"]
HEDGES = [r"\bmay potentially\b", r"\bcould possibly\b", r"\bmight possibly\b", r"\bpotentially could\b",
    r"\bit (might|could) be argued\b"]
VAGUE = [r"\bsignificantly\b", r"\bsubstantially\b", r"\ba large number of\b", r"\bvery\b", r"\bquite\b"]
RUGS = [r"\bit can (easily )?be shown\b", r"\bstraightforward algebra\b", r"\bstandard manipulations?\b",
    r"\bone can show\b", r"\bit is easy to (see|show|verify)\b", r"\btrivially\b", r"\bobviously\b",
    r"\bclearly,"]
WORDY = [r"\beach and every\b", r"\bfirst and foremost\b", r"\bin order to\b", r"\bdue to the fact that\b",
    r"\bat this point in time\b", r"\bthe fact that\b", r"\bin terms of\b", r"\bit is (clear|evident) that\b"]
# pattern 25: periphrasis and negation-stacked withholding (warn tier, non-blocking)
PERIPHRASIS = [r"\bnever\b.{0,40}\b(anything|anyone)\b.{0,20}\b(except|but)\b", r"\bnothing\b.{0,30}\bexcept\b",
               r"\bdoes little more than\b", r"\bhas yet to\b", r"\b(that|this|the) silence\b",
               r"\b(data|results?|silence|crystal|lattice|nature)\b (tells?|speaks?|whispers?|hides?)\b",
               r"\b(fingerprint|signature) of\b(?! the (phonon|band))"]
NEGFRAME = [r"\bnot (just|merely|only) [^.]{1,60}, (but|it is)\b", r"\brather than merely\b"]

def strip_tex(t):
    t = re.sub(r"(?s)\\begin\{(equation|align|eqnarray|gather|multline)\*?\}.*?\\end\{\1\*?\}", " EQN ", t)
    t = re.sub(r"\$\$.*?\$\$", " EQN ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " M ", t)
    t = re.sub(r"%.*", "", t)
    t = re.sub(r"\\(cite|ref|eqref|label)\{[^}]*\}", " ", t)
    return t

def lint(path, banned, maxdash):
    raw = open(path, encoding="utf-8").read()
    hits = []
    def add(kind, pat, line, txt, blocking=False):
        hits.append({"file": path, "line": line, "kind": kind, "pattern": pat, "text": txt.strip()[:120], "blocking": blocking})
    lines = raw.splitlines()
    for i, ln in enumerate(lines, 1):
        low = ln.lower()
        for p in banned:
            if re.search(p, ln):
                add("BANNED", p, i, ln, True)
        for kind, pats, blk in (("AI-PHRASE", AI_PHRASES, False), ("SIGNPOST", SIGNPOST, False),
                                ("HEDGE", HEDGES, False), ("VAGUE", VAGUE, False), ("RUG", RUGS, True),
                                ("NEG-FRAME", NEGFRAME, False), ("WORDY", WORDY, False),
                                ("PERIPHRASIS", PERIPHRASIS, False)):
            for p in pats:
                if re.search(p, low):
                    add(kind, p, i, ln, blk)
    # titles: flag colons, questions, or long titles in sectioning commands; flag epigraphs
    for m in re.finditer(r"\\(part|chapter|section|subsection)\*?\{([^}]*)\}", raw):
        t = m.group(2); ln = raw[:m.start()].count("\n") + 1
        if ":" in t or "?" in t or len(t.split()) > 6:
            add("TITLE", "title not a short noun phrase", ln, t)
        if re.search(r"(?i)^(what|where|why|how|when)\b|\band (its|their) \w+$|^(putting|beyond|towards?|some|more on|a (closer )?look)\b|\b(subtleties|story|landscape|journey|big picture)\b", t.strip()):
            add("TITLE-GESTURE", "title gestures instead of naming content (pattern 21)", ln, t)
    if re.search(r"\\(epigraph|begin\{quote\})", raw):
        add("EPIGRAPH", "epigraph/quotation", 0, "")
    # display equations should end with punctuation inside the environment
    for m in re.finditer(r"(?s)\\begin\{(equation|align|gather|multline)\*?\}(.*?)\\end\{\1\*?\}", raw):
        body = re.sub(r"\\label\{[^}]*\}|\\nonumber|\\notag", "", m.group(2)).rstrip()
        if body and body[-1] not in ",.;:":
            add("EQ-PUNCT", "display equation not punctuated", raw[:m.start()].count("\n") + 1, body[-60:])
    text = strip_tex(raw)
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    for p in paras:
        words = len(p.split())
        dashes = p.count("—") + p.count("---")
        if words > 20 and dashes > maxdash:
            add("DASH", f">{maxdash} em dashes in paragraph", raw.find(p[:30]) and raw[:raw.find(p[:30])].count("\n") + 1, p[:80])
    sents = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if len(s.split()) > 2]
    lens = [len(s.split()) for s in sents]
    for s, n in zip(sents, lens):
        if n > 45:
            add("LONG-SENT", ">45 words", 0, s[:100])
    if len(lens) > 20:
        win = 8
        for k in range(len(lens) - win):
            seg = lens[k:k + win]
            if statistics.pstdev(seg) < 2.5:
                add("MONOTONY", "8 sentences of near-equal length", 0, sents[k][:80]); break
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--banned")
    ap.add_argument("--max-dash", type=float, default=1.0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    banned = []
    if a.banned:
        banned = [l.strip() for l in open(a.banned, encoding="utf-8") if l.strip() and not l.startswith("#")]
    allh = []
    for f in a.files:
        allh += lint(f, banned, a.max_dash)
    if a.json:
        print(json.dumps(allh, indent=1, ensure_ascii=False))
    else:
        for h in allh:
            print(f"{h['file']}:{h['line']}: [{h['kind']}{'!' if h['blocking'] else ''}] {h['pattern']} :: {h['text']}")
        print(f"-- {len(allh)} hits, {sum(h['blocking'] for h in allh)} blocking")
    sys.exit(1 if any(h["blocking"] for h in allh) else 0)

if __name__ == "__main__":
    main()
