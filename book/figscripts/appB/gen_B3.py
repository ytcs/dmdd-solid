#!/usr/bin/env python3
"""Generate tex/appB/B-3.tex (Acronyms) from the book's tex.

Usage: python3 figscripts/appB/gen_B3.py
Writes tex/appB/B-3.tex and figscripts/appB/gen_B3.log. Deterministic.

1. Read the chapters and appendices in reading order (tex/vol1.tex, vol2.tex, vol3.tex -> chNN.tex / appX.tex -> \\input files; App. B itself is skipped).
2. Drop comments, math, verbatim-like arguments (\\cite, \\cref, \\label, \\ref, \\includegraphics, \\url, \\SI units) and
   collect every all-caps token of 2-6 characters (letters, digits allowed, at least two capitals) in the running text, captions and
   tables. Excluded: Roman numerals, chemical formulae (element symbols with digits), units and method names in EXCLUDE.
3. The expansion is taken from the text: the first place where the acronym is defined in the form "expansion (ACR)" or
   "ACR (expansion)", matched with the Schwartz-Hearst rule (the acronym's letters appear in order in the expansion, the first
   letter at the start of a word). The first-use column is the section of the first occurrence, as \\labelcref.
4. An acronym that is used but never expanded in the text is logged as a defect. Its table entry then comes from EXPANSION_FALLBACK
   (the hand-edited part of the table); an acronym with neither is logged and printed with a dash.
"""
import re
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE.parents[1]
TEX = BOOK / "tex"
OUT = TEX / "appB" / "B-3.tex"
LOG = HERE / "gen_B3.log"

ROMAN = re.compile(r"^(?=[IVXLC]+$)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb
Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po
At Rn Fr Ra Ac Th Pa U Np Pu""".split())
# Not acronyms: units, method names built from symbols, labels of points and directions, and words set in capitals.
EXCLUDE = {"GW", "G0W0", "TW", "OK", "NO", "AND", "OR", "NOT", "SI", "MATH",
           "XXZ",                                 # a model label, not an abbreviation of words
           "ORCA", "TALYS", "TB2J", "SG15",       # program and library names that are not acronyms
           "BN", "BNQ-TTF", "PMN-PT"}             # material formulae and names
# Acronyms the text defines in words whose letters do not follow the definition (not defects).
DEFINED_IN_TEXT = {
    "SV": "transverse polarization in the plane of incidence (shear vertical)",
    "SH": "transverse polarization perpendicular to the plane of incidence (shear horizontal)",
    "X2C": "exact two-component (scalar-relativistic Hamiltonian)",
    "ZG": "Zacharias--Giustino (special displacement)",
    "CODATA": "Committee on Data of the International Science Council",
    "EXCEED-DM": "Extended Calculation of Electronic Excitations for Direct detection of Dark Matter (code)",
    "HSE06": "hybrid functional of Heyd, Scuseria and Ernzerhof, 2006 parametrization",
    "NR": "nonrelativistic",
    "PBE0": "hybrid functional built on the functional of Perdew, Burke and Ernzerhof",
    "SALMON": "Scalable Ab initio Light--Matter simulator for Optics and Nanoscience (code)",
    "XCOM": "photon cross-section database of the National Institute of Standards and Technology",
}
# Hand-edited expansions for acronyms the text uses without expanding (each is also logged as a defect).
EXPANSION_FALLBACK = {
    "ACE": "atomic cluster expansion", "ANO": "atomic natural orbital",
    "ANO-RCC": "atomic natural orbital, relativistic core-correlated (basis set)", "BCS": "Bardeen--Cooper--Schrieffer",
    "CASSCF": "complete-active-space self-consistent field", "CCD": "charge-coupled device",
    "CDMS": "Cryogenic Dark Matter Search", "CODATA": "Committee on Data of the International Science Council",
    "CPU": "central processing unit", "CVD": "chemical vapor deposition", "DAMIC": "Dark Matter in CCDs",
    "DFT": "density-functional theory", "DLMF": "Digital Library of Mathematical Functions", "DOS": "density of states",
    "EPW": "Electron--Phonon Wannier (code)",
    "EXCEED-DM": "Extended Calculation of Electronic Excitations for Direct detection of Dark Matter (code)",
    "FFT": "fast Fourier transform", "FIRE": "fast inertial relaxation engine", "FT": "fast transverse (phonon polarization)",
    "ST": "slow transverse (phonon polarization)", "G4CMP": "Geant4 Condensed Matter Physics (simulation toolkit)",
    "GIPAW": "gauge-including projector augmented wave", "GPAW": "grid-based projector-augmented wave (code)",
    "GPU": "graphics processing unit", "GRASP": "General-purpose Relativistic Atomic Structure Package",
    "HOMO": "highest occupied molecular orbital", "LUMO": "lowest unoccupied molecular orbital",
    "HSE06": "Heyd--Scuseria--Ernzerhof hybrid functional, 2006 parametrization",
    "JARVIS": "Joint Automated Repository for Various Integrated Simulations", "LF": "local fields (crystal local-field effects)",
    "MLIP": "machine-learned interatomic potential", "NR": "nonrelativistic", "NV": "nitrogen--vacancy",
    "PBE0": "hybrid functional of Perdew, Burke and Ernzerhof with one quarter exact exchange",
    "PT": "product of inversion (parity) and time reversal", "QED": "quantum electrodynamics", "RAVE": "Radial Velocity Experiment",
    "RPA": "random-phase approximation",
    "SALMON": "Scalable Ab initio Light--Matter simulator for Optics and Nanoscience",
    "SCAN": "strongly constrained and appropriately normed (functional)", "SOC": "spin--orbit coupling",
    "STE": "self-trapped exciton", "TRIM": "Transport of Ions in Matter", "WEST": "Without Empty States (code)",
    "XCOM": "photon cross-section database of NIST", "ZBL": "Ziegler--Biersack--Littmark",
    "CNT": "carbon nanotube", "TB09": "meta-GGA functional of Tran and Blaha (2009)",
}
# Expansions that replace the one found in the text, where the text names the authors rather than the thing named
# (App. B review, accuracy.md section 2; editor ruling B4).
EXPANSION_OVERRIDE = {
    "HSE": "hybrid functional of Heyd, Scuseria and Ernzerhof",
    "PBE": "generalized-gradient functional of Perdew, Burke and Ernzerhof",
}


def reading_order():
    """Files of the three volumes in reading order (Volume I, II, III); App. B and front matter are skipped and a file
    printed in several volumes (App. A) is read once."""
    sys.path.insert(0, str(TEX.parent / "tools"))
    import volumes as V  # noqa: E402
    files, seen = [], set()
    for vol in V.VOLS:
        for driver, fs in V.chapters(vol):
            if driver.parent.name == "appB":
                continue
            for f in fs:
                if f not in seen:
                    seen.add(f)
                    files.append(f)
    return files


def strip(text):
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray|displaymath)\*?\}.*?\\end\{\1\*?\}", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", " MATH ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " MATH ", text, flags=re.S)
    text = re.sub(r"\\(cite|Cite|cref|Cref|crefrange|Crefrange|labelcref|ref|eqref|label|includegraphics|url|href|input|"
                  r"printbibliography|nameref|pageref|addbibresource)\*?(\[[^\]]*\])*\{[^}]*\}", " ", text)
    text = re.sub(r"\\(SI|qty)\{[^}]*\}\{[^}]*\}|\\(si|unit)\{[^}]*\}", " ", text)
    text = re.sub(r"\\(mathrm|mathsf|operatorname|texttt)\{[^{}]*\}", " ", text)
    text = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])*(\{[^}]*\})?", " ", text)
    text = re.sub(r"\\[A-Za-z]+\*?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ").replace("--", "–")
    return text


TOKEN = re.compile(r"(?<![A-Za-z0-9\\_^])(?<![a-z]-)([A-Z][A-Z0-9]{1,5}(?:-[A-Z][A-Z0-9]{1,5})*)(?:s)?(?![A-Za-z0-9])")
STOP = {"of", "the", "and", "for", "a", "an", "in", "on", "to", "with", "plus", "by"}


def initials_match(acr, text):
    """Shortest window of trailing words whose part initials spell acr (stop words may be skipped)."""
    a = re.sub(r"[^a-z0-9]", "", acr.lower())
    words = text.split()
    for k in range(1, min(len(words), len(a) + 5) + 1):
        win = words[-k:]
        parts = []
        for w in win:
            for p in re.split(r"[-–/]", w.strip(",;:()")):
                if p:
                    parts.append(p)
        if not parts or parts[0].lower() in STOP:
            continue

        def match(i, j):
            if i == len(a):
                return j == len(parts) or all(x.lower() in STOP for x in parts[j:])
            if j == len(parts):
                return False
            p = parts[j].lower()
            if p[0] == a[i] and match(i + 1, j + 1):
                return True
            if len(p) > 1 and i + 1 < len(a) and p[:2] == a[i:i + 2] and match(i + 2, j + 1):
                return True
            if a[i].isdigit() and p.startswith(a[i]) and match(i + 1, j + 1):
                return True
            # digits of a year: "TB09" against "Tran and Blaha (2009)"
            d = re.match(r"\d+", a[i:])
            if d and p.isdigit() and p.endswith(d.group()) and match(i + len(d.group()), j + 1):
                return True
            # a letter with its digits inside one word: "G4" against "Geant4"
            d = re.match(r"\d+", a[i + 1:])
            if d and p[0] == a[i] and d.group() in p[1:] and match(i + 1 + len(d.group()), j + 1):
                return True
            if p in STOP and match(i, j + 1):
                return True
            return False
        if match(0, 0):
            return " ".join(win).strip(" ,;:(")
    return None


def expand_before(acr, text):
    e = initials_match(acr, text)
    if e:
        return e
    e = schwartz_hearst(acr, text)
    if e and 2 <= len(e.split()) <= len(acr) + 1 and e[0].lower() == acr[0].lower():
        inits = [p[0].lower() for w in e.split() for p in re.split(r"[-–/]", w) if p]
        hits = sum(1 for c in acr.lower() if c in inits)
        if 2 * hits > len(acr):
            return e
    return None


def is_acronym(tok):
    if tok in EXCLUDE or ROMAN.match(tok):
        return False
    if sum(c.isupper() for c in tok) < 2:
        return False
    if any(c.isdigit() for c in tok):
        # formula such as H2O or CO2: element symbols with counts
        if re.fullmatch(r"(?:[A-Z][a-z]?\d*)+", tok) and all(p in ELEMENTS for p in re.findall(r"[A-Z][a-z]?", tok)):
            return False
        if tok in ("MATH",):
            return False
    if tok == "MATH":
        return False
    return True


def schwartz_hearst(acr, text):
    """Shortest suffix of text (in words) that expands acr: its letters in order, the first at a word start."""
    words = text.split()
    words = words[-min(len(words), len(acr) + 6):]
    s = " ".join(words)
    a = acr.lower()
    si = len(s) - 1
    ai = len(a) - 1
    while ai >= 0:
        c = a[ai]
        if not c.isalnum():
            ai -= 1
            continue
        while si >= 0 and (s[si].lower() != c or (ai == 0 and si > 0 and s[si - 1].isalnum())):
            si -= 1
        if si < 0:
            return None
        si -= 1
        ai -= 1
    start = s.rfind(" ", 0, si + 1) + 1
    exp = s[start:].strip(" ,;:")
    return exp if exp else None


def main():
    files = reading_order()
    first = OrderedDict()       # acr -> (section label, file)
    count = defaultdict(int)
    expansion = {}
    for f in files:
        raw = f.read_text(encoding="utf-8")
        # section labels by position
        labs = [(m.start(), m.group(1)) for m in re.finditer(r"\\label\{((?:sec|app):[A-F]?[0-9]*\.?[0-9]+|app:[A-F])\}", raw)]
        chap = re.search(r"\\label\{(chap:\d+|app:[A-F])\}", raw)
        # work paragraph by paragraph so positions map to labels approximately
        pos = 0
        for para in re.split(r"(\n\s*\n)", raw):
            start = pos
            pos += len(para)
            lab = None
            for p, l in labs:
                if p <= start + len(para):
                    lab = l
            if lab is None and chap:
                lab = chap.group(1)
            if lab is None:
                mm = re.match(r"app([A-F])/", f.relative_to(TEX).as_posix())
                lab = "app:" + mm.group(1) if mm else None
            txt = strip(para)
            for m in TOKEN.finditer(txt):
                tok = m.group(1)
                if not is_acronym(tok):
                    continue
                count[tok] += 1
                if tok not in first:
                    first[tok] = (lab, f.relative_to(TEX).as_posix())
            # grouped: "longitudinal and transverse acoustic (LA, TA)"
            for m in re.finditer(r"(\w+) and (\w+) ([\w-]+) \(([A-Z]{2,6}), ([A-Z]{2,6})\)", txt):
                w1, w2, tail, a1, a2 = m.groups()
                for w, a in ((w1, a1), (w2, a2)):
                    if a not in expansion and initials_match(a, w + " " + tail):
                        expansion[a] = (w + " " + tail, f.relative_to(TEX).as_posix())
            # expansions "expansion (ACR)" and "expansion (ACR, ...)"
            for m in re.finditer(r"\(([A-Z][A-Z0-9]{1,5}(?:-[A-Z][A-Z0-9]{1,5})*)s?(?:\)|, )", txt):
                tok = m.group(1)
                if re.match(r"[A-Z]{2,6}\)", txt[m.end():]):
                    continue   # (LA, TA): handled as a group
                if tok in expansion or not is_acronym(tok):
                    continue
                exp = expand_before(tok, txt[:m.start()])
                if exp:
                    expansion[tok] = (exp, f.relative_to(TEX).as_posix())
            # "ACR (expansion)"
            for m in re.finditer(r"(?<![A-Za-z])([A-Z][A-Z0-9]{1,5})s? \(([^()]{4,80})\)", txt):
                tok, inner = m.group(1), m.group(2)
                if tok in expansion or not is_acronym(tok):
                    continue
                if initials_match(tok, inner) == inner.strip(" ,;:"):
                    expansion[tok] = (inner.strip(), f.relative_to(TEX).as_posix())
            # caption style "ACR, expansion;" and "the label ACR marks expansion"
            # (also the colon form of table captions, "SOC: spin--orbit coupling.")
            for m in re.finditer(r"(?:(?<=[;.:] )|^)\s*([A-Z][A-Z0-9]{1,5}(?:-[A-Z][A-Z0-9]{1,5})*)[,:] ([^;.]{3,90})(?=[;.])", txt, re.M):
                tok, inner = m.group(1), m.group(2).strip()
                if tok in expansion or not is_acronym(tok):
                    continue
                if expand_before(tok, inner) == inner.strip(" ,;:"):
                    expansion[tok] = (inner, f.relative_to(TEX).as_posix())
            # appositive "the ACR functional, the meta-GGA functional of Tran and Blaha (2009) ..."
            for m in re.finditer(r"(?<![A-Za-z])([A-Z][A-Z0-9]{1,5}) (?:functional|code|toolkit|package|method|model|potential), "
                                 r"(?:the |an? )?([^;.]{4,120})", txt):
                tok, words = m.group(1), m.group(2).split()
                if tok in expansion or not is_acronym(tok):
                    continue
                for k in range(1, len(words) + 1):
                    if initials_match(tok, " ".join(words[:k])):
                        expansion[tok] = (" ".join(words[:k]).strip(" ,;:"), f.relative_to(TEX).as_posix())
                        break
            for m in re.finditer(r"label ([A-Z][A-Z0-9]{1,5}) (?:marks|denotes|stands for) ([a-z][^.,;]{3,60})", txt):
                tok, inner = m.group(1), m.group(2).strip()
                if tok not in expansion:
                    expansion[tok] = (inner, f.relative_to(TEX).as_posix())

    for tok in list(first):
        if "-" in tok:
            parts = tok.split("-")
            if all(p in first or p in expansion or p in EXPANSION_FALLBACK for p in parts):
                for p in parts:
                    if p not in first:
                        first[p] = first[tok]
                    count[p] += count[tok]
                del first[tok]
    for tok, e in DEFINED_IN_TEXT.items():
        if tok in first and tok not in expansion:
            expansion[tok] = (e, "defined in words in " + first[tok][1])
    rows = []
    unexpanded = []
    for tok in sorted(first, key=lambda t: t.lower()):
        lab, fname = first[tok]
        if tok in EXPANSION_OVERRIDE:
            exp = EXPANSION_OVERRIDE[tok]
        elif tok in expansion:
            exp = expansion[tok][0]
            exp = re.sub(r"approximations$", "approximation", exp)
        elif tok in EXPANSION_FALLBACK:
            exp = EXPANSION_FALLBACK[tok]
            unexpanded.append((tok, fname, count[tok], "fallback expansion used"))
        else:
            exp = None
            unexpanded.append((tok, fname, count[tok], "no expansion anywhere"))
        rows.append((tok, exp, lab))

    out = [
        "% Acronyms. GENERATED by figscripts/appB/gen_B3.py from the tex; do not edit by hand, rerun the script.",
        r"\section{Acronyms}\label{app:B.3}",
        "",
        r"The last column gives the section or appendix in which the acronym first appears.",
        "",
        r"{\small",
        r"\begin{longtable}{@{}l>{\raggedright\arraybackslash}p{0.62\textwidth}l@{}}",
        r"\toprule",
        r"Acronym & Expansion & First use \\",
        r"\midrule",
        r"\endfirsthead",
        r"\toprule",
        r"Acronym & Expansion & First use \\",
        r"\midrule",
        r"\endhead",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    for tok, exp, lab in rows:
        e = exp if exp else "---"
        e = e.replace("&", r"\&").replace("%", r"\%").replace("–", "--")
        e = re.sub(r"\s+", " ", e)
        ref = r"\labelcref{%s}" % lab if lab and lab.startswith(("sec:", "app:")) and "." in lab else (
            r"\labelcref{%s}" % lab if lab else "")
        out.append("%s & %s & %s \\\\" % (tok, e, ref))
    out += [r"\end{longtable}", "}", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")

    with LOG.open("w", encoding="utf-8") as f:
        f.write("gen_B3.py log: tex -> tex/appB/B-3.tex\n\n")
        f.write("Acronyms found: %d (expanded in the text: %d)\n\n" % (len(rows), len(rows) - len(unexpanded)))
        f.write("Used but never expanded in the text (%d) -- defects to report:\n" % len(unexpanded))
        for tok, fname, n, why in unexpanded:
            f.write("  %-7s first in %-22s uses %4d  [%s]\n" % (tok, fname, n, why))
        order = {f.relative_to(TEX).as_posix(): i for i, f in enumerate(reading_order())}
        late = [(t, first[t][1], expansion[t][1]) for t in sorted(expansion, key=str.lower)
                if t in first and expansion[t][1] in order and order[expansion[t][1]] > order.get(first[t][1], 0)]
        f.write("\nExpanded only after the first use (%d) -- defects to report:\n" % len(late))
        for t, a, b in late:
            f.write("  %-7s first used in %-22s expanded in %s\n" % (t, a, b))
        f.write("\nExpansions and where they were found:\n")
        for tok in sorted(expansion, key=str.lower):
            f.write("  %-7s %-60s %s\n" % (tok, expansion[tok][0][:60], expansion[tok][1]))
    print("acronyms %d, unexpanded %d" % (len(rows), len(unexpanded)))


if __name__ == "__main__":
    main()
