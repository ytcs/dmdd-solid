#!/usr/bin/env python3
"""Generate tex/appB/B-1.tex (List of symbols) from NOTATION.md.

Usage: python3 figscripts/appB/gen_B1.py        (from anywhere; paths are resolved from this file)
Writes tex/appB/B-1.tex and figscripts/appB/gen_B1.log. Deterministic: a rerun on the same inputs gives the same files.

Steps
1. Read the symbol table of NOTATION.md (the rows before the clash list). Drop every row whose first use is a dash or is marked
   removed or unused; a symbol inside a row whose own first use is a dash ("ρ_crit: —; h: 1.1") is dropped from that row.
2. Strip flags, dates and every editorial parenthesis (sections, merges, clash entries, typography notes, sources) from the
   meaning; cut a long meaning of a one-symbol row at its first top-level semicolon.
3. Render symbols in LaTeX math with the book's macros (tex/macros.tex). Sub- and superscript typography (upright or italic,
   e.g. v_{\\mathrm{esc}} but \\mu_{\\chi e}) is read from the accepted tex itself: every math token of tex/ch*/ and tex/app*/ is
   tokenized (with the tokenizer of ledgers/check_notation.py) and the most frequent spelling of each (base, script) is used.
   Symbols that do not convert mechanically are in EXPLICIT. Anything left unconverted is logged.
4. First use: the first section number of the cell, turned into \\labelcref{sec:N.M} or \\labelcref{app:X.n} when that label
   exists in tex/**/*.tex (checked here); otherwise printed as plain text and logged.
Revised 2026-11-07 after the App. B accuracy review (ledgers/REVIEWS/appB/accuracy.md, editor rulings B1, B3): a section number
counts as editorial only as a pointer, never as a decimal value; a multi-symbol row keeps its clause count; equation labels leave
the clause, not the clause itself; "(14.5)" in a symbol cell is dropped; Σ is a sum in a meaning; the imaginary unit, \\operatorname
names, primes after an index list, and bold vector letters follow the tex (per first-use file); scope notes (SCOPE) mark the
accepted local reuse of a symbol.
Revised 2026-11-07 after the post-revision check (ledgers/REVIEWS/appCEB-postrev-check.md, items 9-14): e^pz and y_χν̃ in EXPLICIT;
a lone < or > is a script (E_<, E_>); ∗ between factors is \ast; a value list after "= 0," stays in the math; "stream a" is math.
5. Group by the chapter of first use (Chaps. 1-22, then Apps. A, C, D, E, F); within a group, sort by first-use section and then
   by the order of the rows in NOTATION.md, which is the order in which the symbols were introduced within a section.
"""
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE.parents[1]
TEX = BOOK / "tex"
NOTATION = BOOK / "NOTATION.md"
OUT = TEX / "appB" / "B-1.tex"
LOG = HERE / "gen_B1.log"

sys.path.insert(0, str(BOOK / "ledgers"))
sys.dont_write_bytecode = True
import check_notation as cn  # noqa: E402  (tokenizer of the accepted tex; read-only use)

log_unrendered = []   # (row, symbol or text, reason)
log_dropped = []      # (line, symbol, first use)
log_nolabel = []      # (line, symbol, section)

# ----------------------------------------------------------------------------------------------------------- characters
GREEK = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ϵ": r"\epsilon", "ζ": r"\zeta",
    "η": r"\eta", "θ": r"\theta", "ϑ": r"\vartheta", "ι": r"\iota", "κ": r"\kappa", "ϰ": r"\varkappa", "λ": r"\lambda",
    "μ": r"\mu", "ν": r"\nu", "ξ": r"\xi", "π": r"\pi", "ϖ": r"\varpi", "ρ": r"\rho", "ϱ": r"\varrho", "σ": r"\sigma",
    "ς": r"\varsigma", "τ": r"\tau", "υ": r"\upsilon", "φ": r"\phi", "ϕ": r"\varphi", "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega",
    "Γ": r"\varGamma", "Δ": r"\Delta", "Θ": r"\Theta", "Λ": r"\Lambda", "Ξ": r"\Xi", "Π": r"\Pi", "Σ": r"\Sigma",
    "Υ": r"\Upsilon", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega", "ℓ": r"\ell", "ħ": r"\hbar",
}
SYMB = {
    "·": r"\cdot ", "⟨": r"\langle ", "⟩": r"\rangle ", "∥": r"\parallel ", "⊥": r"\perp ", "±": r"\pm ", "∓": r"\mp ",
    "→": r"\to ", "×": r"\times ", "∞": r"\infty ", "∂": r"\partial ", "∇": r"\nabla ", "−": "-", "…": r"\dots ",
    "⊙": r"\odot ", "⊕": r"\oplus ", "≻": r"\succ ", "⌊": r"\lfloor ", "⌋": r"\rfloor ", "𝟙": r"\mathbb{1}",
    "∫": r"\int ", "≈": r"\approx ", "≃": r"\simeq ", "≤": r"\le ", "≥": r"\ge ", "≪": r"\ll ", "≫": r"\gg ", "∝": r"\propto ",
    "≡": r"\equiv ", "≠": r"\ne ", "∼": r"\sim ", "~": r"\sim ", "√": r"\surd ", "∑": r"\sum ", "∏": r"\prod ",
    "∈": r"\in ", "⊗": r"\otimes ", "∘": r"\circ ", "↑": r"\uparrow ", "↓": r"\downarrow ", "↔": r"\leftrightarrow ",
    "⇒": r"\Rightarrow ", "°": r"^\circ ", "‖": r"\Vert ", "\\|": "|", "⟂": r"\perp ", "†": r"^{\dagger}", "‡": r"^{\ddagger}",
    "∗": r"\ast ", "′": "'", "″": "''", "−": "-", "–": "-", "Å": r"\text{\AA}", "{": "{", "}": "}", "%": r"\%", "&": r"\&",
    "#": r"\#", "∮": r"\oint ", "⋯": r"\cdots ", "⋅": r"\cdot ", "∖": r"\setminus ", "∪": r"\cup ", "∩": r"\cap ",
    "ℏ": r"\hbar ", "⟦": "[", "⟧": "]", "∠": r"\angle ", "□": r"\square ", "◦": r"\circ ", "⁄": "/", "≲": r"\lesssim ",
    "≳": r"\gtrsim ", "∧": r"\wedge ", "∨": r"\vee ", "⊂": r"\subset ", "∅": r"\emptyset ", "ℕ": r"\mathbb{N}",
    "○": r"\circ ", "½": r"\tfrac{1}{2}", "⊃": r"\supset ", "µ": r"\mu ", "𝟏": r"\mathbf{1}", "ᵀ": r"^{\mathsf{T}}",
    "ℝ": r"\mathbb{R}", "ℤ": r"\mathbb{Z}", "ℂ": r"\mathbb{C}", "ℑ": r"\mathfrak{I}", "ℜ": r"\mathfrak{R}",
}
SUPMAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁽⁾ⁿⁱ", "0123456789-+()ni")
SUBMAP = str.maketrans("₀₁₂₃₄₅₆₇₈₉₋₊₍₎ₙₐₑₒₓₖₗₘₚₛₜᵢⱼ", "0123456789-+()naeoxklmpstij")
SUPCH = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁽⁾ⁿⁱ")
SUBCH = set("₀₁₂₃₄₅₆₇₈₉₋₊₍₎ₙₐₑₒₓₖₗₘₚₛₜᵢⱼ")
ACC = {"\u0304": r"\bar", "\u0303": r"\tilde", "\u0302": r"\hat", "\u0307": r"\dot", "\u0308": r"\ddot", "\u030c": r"\check",
       "\u20d7": r"\vec"}


def alphabet(ch):
    """Return the TeX of one letter-like character (math alphanumerics, Greek, Latin), or None."""
    o = ord(ch)
    special = {"𝓃": r"\nd", "𝓥": r"\Vol", "𝖦": r"\GF", "𝖠": r"\SpecA", "ℬ": r"\mathcal{B}", "ℰ": r"\mathcal{E}",
               "ℱ": r"\mathcal{F}", "ℋ": r"\mathcal{H}", "ℐ": r"\mathcal{I}", "ℒ": r"\mathcal{L}", "ℳ": r"\mathcal{M}",
               "ℛ": r"\mathcal{R}", "ℭ": r"\mathfrak{C}", "ℌ": r"\mathfrak{H}", "ℨ": r"\mathfrak{Z}", "ℯ": r"\mathscr{e}",
               "ℊ": r"\mathscr{g}", "ℴ": r"\mathscr{o}"}
    if ch in special:
        return special[ch]
    if ch in GREEK:
        return GREEK[ch]
    if ch.isascii() and ch.isalpha():
        return ch
    rng = [
        (0x1D400, "A", r"\vect{%s}"), (0x1D41A, "a", r"\vect{%s}"),            # bold
        (0x1D49C, "A", r"\mathcal{%s}"), (0x1D4B6, "a", r"\mathscr{%s}"),     # script
        (0x1D4D0, "A", r"\mathscr{%s}"), (0x1D4EA, "a", r"\mathscr{%s}"),     # bold script (book: \mathscr)
        (0x1D504, "A", r"\mathfrak{%s}"), (0x1D51E, "a", r"\mathfrak{%s}"),   # fraktur
        (0x1D5A0, "A", r"\mathsf{%s}"), (0x1D5BA, "a", r"\mathsf{%s}"),       # sans-serif
    ]
    for start, a, fmt in rng:
        if start <= o < start + 26:
            return fmt % chr(ord(a) + o - start)
    if 0x1D6C2 <= o < 0x1D6C2 + 25:  # bold small Greek
        g = "αβγδεζηθικλμνξοπρςστυφχψω"[o - 0x1D6C2]
        return r"\vect{%s}" % GREEK.get(g, g)
    if 0x1D6A8 <= o < 0x1D6A8 + 25:  # bold capital Greek
        g = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"[o - 0x1D6A8]
        return r"\vect{%s}" % GREEK.get(g, g)
    bold_greek_extra = {"𝛜": r"\vect{\epsilon}", "𝛝": r"\vect{\vartheta}", "𝛟": r"\vect{\phi}", "𝛡": r"\vect{\varpi}",
                        "𝛠": r"\vect{\varrho}", "𝛞": r"\vect{\varkappa}"}
    return bold_greek_extra.get(ch)


# ----------------------------------------------------------------------------------------------------------- tex harvest
FILE_SUBS = defaultdict(lambda: defaultdict(Counter))
# per file: letter -> Counter{"bold": n, "plain": n} for the letters that the book prints bold when they are vectors
VECLETTERS = set("qkQGRrpK")
BOLDVEC = {}   # letter -> True for the row being converted (set in main from the first-use file)
PRIME_IN_SUB = {}   # one-letter subscript (NOTATION spelling) -> True if the tex writes x_{a'} more often than x_a' (filled below)
FILE_VEC = defaultdict(lambda: defaultdict(Counter))
FILE_SUPS = defaultdict(lambda: defaultdict(Counter))
CURRENT = {"file": None}


class Scoped(dict):
    """A (base, script) -> Counter table that answers from the first-use file of the current row when it can."""
    def __init__(self, base, per_file):
        super().__init__(base)
        self.per_file = per_file

    def __getitem__(self, k):
        f = CURRENT["file"]
        if f and k in self.per_file.get(f, {}):
            return self.per_file[f][k]
        return dict.__getitem__(self, k)


def harvest():
    """(base key, normalized script) -> Counter of TeX spellings of that script, from the math of the accepted tex."""
    subs, sups, bases = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    gsubs = defaultdict(Counter)
    files = sorted(TEX.glob("ch*/*.tex")) + sorted(TEX.glob("app[ACDEF]/*.tex"))
    for f in files:
        for seg in cn.math_segments(f.read_text(encoding="utf-8")):
            for k, raw in cn.tokens(seg):
                bkey = k.split("_")[0].split("^")[0]
                m = re.match(r"(\\[A-Za-z]+\s*(\{(?:[^{}]|\{[^{}]*\})*\})?|[A-Za-z])", raw)
                if not m:
                    continue
                braw = m.group(0)
                bases[k.split("^")[0]][braw.strip()] += 1
                if k.split("^")[0] in VECLETTERS:
                    FILE_VEC[f.relative_to(TEX).as_posix()][k.split("^")[0]][
                        "bold" if braw.strip().startswith("\\vect") else "plain"] += 1
                rest = raw[len(braw):]
                i = 0
                while i < len(rest):
                    while i < len(rest) and rest[i] == " ":
                        i += 1
                    if i < len(rest) and rest[i] in "_^":
                        w = rest[i]
                        g, j = cn.read_group(rest, i + 1)
                        i = j
                        nk = cn.norm_script(g)
                        if not nk:
                            continue

                        fk = f.relative_to(TEX).as_posix()
                        if w == "_":
                            subs[(bkey, nk)][g.strip()] += 1
                            gsubs[nk][g.strip()] += 1
                            FILE_SUBS[fk][(bkey, nk)][g.strip()] += 1
                        else:
                            sups[(bkey, nk)][g.strip()] += 1
                            FILE_SUPS[fk][(bkey, nk)][g.strip()] += 1
                    else:
                        i += 1
    return subs, sups, bases, gsubs


SUBS, SUPS, BASES, GSUBS = harvest()
for (_b, _nk), _cnt in list(SUBS.items()):
    if len(_nk) == 2 and _nk.endswith("′"):
        PRIME_IN_SUB[_nk[0]] = PRIME_IN_SUB.get(_nk[0], 0) + sum(_cnt.values())
SUBS = Scoped(SUBS, FILE_SUBS)
SUPS = Scoped(SUPS, FILE_SUPS)

BOLDPLAIN = dict(cn.BOLD)


def norm_key(s):
    """NOTATION spelling of a script -> the normalization of check_notation.norm_script (|B marks a bold letter)."""
    bold = any(0x1D400 <= ord(c) <= 0x1D433 or 0x1D6A8 <= ord(c) <= 0x1D6E1 for c in s)
    s = "".join(BOLDPLAIN.get(c, c) for c in s)
    s = s.translate(SUBMAP).translate(SUPMAP)
    s = s.replace("{", "").replace("}", "").replace(" ", "").replace("_", "").replace("'", "′")
    s = unicodedata.normalize("NFD", s)
    return "".join(cn.FOLD.get(c, c) for c in s)


def base_key(tex_base, uni_base):
    b = "".join(BOLDPLAIN.get(c, c) for c in uni_base)
    b = unicodedata.normalize("NFD", b)
    return "".join(cn.FOLD.get(c, c) for c in b)


OPERATORS = {"Re": r"\Real", "Im": r"\Imag", "Tr": r"\Tr", "ln": r"\ln", "log": r"\log", "exp": r"\exp", "sin": r"\sin",
             "cos": r"\cos", "tan": r"\tan", "tanh": r"\tanh", "cosh": r"\cosh", "sinh": r"\sinh", "max": r"\max",
             "min": r"\min", "det": r"\det", "arg": r"\arg", "sinc": r"\operatorname{sinc}", "sgn": r"\operatorname{sgn}",
             "erf": r"\operatorname{erf}", "erfc": r"\operatorname{erfc}", "Li": r"\operatorname{Li}", "diag": r"\operatorname{diag}",
             "Var": r"\operatorname{Var}", "Cov": r"\operatorname{Cov}", "tr": r"\operatorname{tr}", "sign": r"\operatorname{sign}",
             "Ei": r"\operatorname{Ei}", "csc": r"\csc", "coth": r"\coth", "cot": r"\cot", "sec": r"\sec", "lim": r"\lim",
             "sup": r"\sup", "inf": r"\inf", "PV": r"\operatorname{PV}", "fp": r"\operatorname{fp}",
             "ZPR": r"\mathrm{ZPR}"}
# operator names that are also ordinary words or element symbols: an operator only when an argument follows
OPERATORS_ARG = {"Si": r"\operatorname{Si}"}


def script_tex(content, bkey, kind, row):
    """TeX of a sub- or superscript written in NOTATION spelling."""
    nk = norm_key(content)
    table = SUBS if kind == "_" else SUPS
    if nk and (bkey, nk) in table:
        return table[(bkey, nk)].most_common(1)[0][0]
    if kind == "_" and nk in GSUBS and len(nk) > 1:
        return GSUBS[nk].most_common(1)[0][0]
    # mechanical: comma-separated parts; ASCII words of two or more letters upright, single letters italic
    parts = re.split(r"(,|;)", content)
    out = []
    for p in parts:
        if p in (",", ";"):
            out.append(p)
            continue
        if re.fullmatch(r"[A-Za-z]{2,}", p) and kind == "_":
            out.append(r"\mathrm{%s}" % p)
        elif re.fullmatch(r"[A-Za-z]{3,}", p) and kind == "^":
            out.append(r"\mathrm{%s}" % p)
        else:
            out.append(math(p, row, inner=True))
    return "".join(out)


def take_script(s, i):
    """Read a NOTATION script starting at s[i] (after _ or ^). Returns (content, next index, braced)."""
    if i < len(s) and s[i] == "{":
        d = 0
        for j in range(i, len(s)):
            d += s[j] == "{"
            d -= s[j] == "}"
            if d == 0:
                return s[i + 1:j], j + 1, True
        return s[i + 1:], len(s), True
    if i < len(s) and s[i] == "(":
        d = 0
        for j in range(i, len(s)):
            d += s[j] == "("
            d -= s[j] == ")"
            if d == 0:
                return s[i:j + 1], j + 1, True
        return s[i:], len(s), True
    if i < len(s) and s[i] in "+−±∓" and (i + 1 == len(s) or not s[i + 1].isalnum()):
        return s[i], i + 1, True
    if i < len(s) and s[i] in "<>":
        j = i
        while j < len(s) and s[j] in "<>":
            j += 1
        return s[i:j], j, True   # E_<, E_>, 𝒱_<> of 18.2 (post-revision check, item 10)
    if i < len(s) and s[i] == "⟨":
        k = s.find("⟩", i)
        if k > 0:
            return s[i:k + 1], k + 1, True
    j = i
    while j < len(s):
        c = s[j]
        if c == "′" and j > i and j + 1 < len(s) and (s[j + 1].isalnum() or s[j + 1] in GREEK):
            j += 1   # 𝒰_j′j: a prime inside an index list
            continue
        if c == "′" and j > i and (j - i >= 2 or PRIME_IN_SUB.get(s[i:j])):
            return s[i:j + 1], j + 1, False   # R_GG′, D_κκ′: the prime belongs to the last index
        if c in "_^ ()[]{}|/⟨⟩=+<>≈·∗" or c in SUPCH or c in SUBCH or c in "†′″*":
            if c == "*" and j == i:
                j += 1
            break
        if c in ",;" and (j + 1 >= len(s) or s[j + 1] == " " or s[j + 1] in ")]"):
            break
        if c == "−" and j > i:
            break
        j += 1
    return s[i:j], j, False


_CMDS = sorted({v.strip().lstrip("\\").split("{")[0] for v in list(GREEK.values()) + list(SYMB.values()) + list(OPERATORS.values())
                if v.strip().startswith("\\") and re.fullmatch(r"\\[A-Za-z]+", v.strip())}, key=len, reverse=True)
KNOWN_CMDS = set(_CMDS) | set("""mathrm vect nd Vol mathcal mathscr mathfrak mathsf mathbb mathbf text dd ee ii tfrac frac sqrt bar
tilde hat dot ddot check vec GF SpecA prime dagger ddagger operatorname AA Real Imag Tr langle rangle left right big Big
quad qquad cdot ldots dots cdots boldsymbol bm op Eg mchi vmin sigmae FDM""".split())


def fix_cmds(t):
    """\\alpham -> \\alpha m: split a control word that is a known command followed by letters."""
    def rep(m):
        name = m.group(1)
        if name in KNOWN_CMDS:
            return m.group(0)
        for k in range(len(name) - 1, 0, -1):
            if name[:k] in KNOWN_CMDS:
                return "\\" + name[:k] + " " + name[k:]
        return m.group(0)
    return re.sub(r"\\([A-Za-z]+)", rep, t)


def add_sup(out, tex):
    """Append a superscript, merging with a superscript that is already there (x^{a}' -> x^{a\\prime})."""
    if out and out[-1].startswith("^{") and out[-1].endswith("}"):
        out[-1] = out[-1][:-1] + tex + "}"
    elif len(out) > 1 and out[-1].startswith("_{") and out[-2].startswith("^{") and out[-2].endswith("}"):
        out[-2] = out[-2][:-1] + tex + "}"
    elif tex == r"\prime":
        out.append("'")
    elif tex == r"\prime\prime":
        out.append("''")
    else:
        out.append("^{" + tex + "}")


def math(s, row="", inner=False, symbol=False):
    """Convert a NOTATION math string to TeX math (without dollars).

    symbol: the string is a Symbol cell, where Σ is the self-energy; in a meaning Σ is a sum unless it carries a superscript,
    the subscripts ₁, ₂, or the self-energy subscripts x, c with an argument, or stands alone.
    """
    s = s.replace("\\|", "|")
    s = unicodedata.normalize("NFC", s)
    out = []
    i = 0
    last_base = ("", "")  # (tex, unicode) of the last letter, for script lookup
    n = len(s)
    while i < n:
        c = s[i]
        # multi-letter ASCII operator names
        m = re.match(r"[A-Za-z]{2,}", s[i:])
        if m and not (i > 0 and s[i - 1] in "_^"):
            w = m.group(0)
            if w in OPERATORS:
                out.append(OPERATORS[w] + " ")
                i += len(w)
                last_base = ("", "")
                if w == "ZPR" and i < n and s[i] == "^":
                    content, j, _ = take_script(s, i + 1)
                    out[-1] = OPERATORS[w]
                    out.append("^{" + (r"\mathrm{%s}" % content if content.isalpha() else math(content, row, True)) + "}")
                    i = j
                continue
            if w in OPERATORS_ARG and i + len(w) < n and s[i + len(w)] == "(":
                out.append(OPERATORS_ARG[w])
                i += len(w)
                last_base = ("", "")
                continue
        if c == "d" and (i == 0 or not s[i - 1].isalpha()) and i + 1 < n and (
                s[i + 1] in "³²" or (alphabet(s[i + 1]) and s[i + 1] != "d" and (i == 0 or s[i - 1] in "∫ /(" ) and
                                     (i + 2 >= n or not s[i + 2].isalpha() or s[i + 1] in GREEK or ord(s[i + 1]) > 0x2000))):
            if i > 0 and s[i - 1] in "∫/(" or (i == 0 and n > 1 and (s[1] in "³²" or s[1] in GREEK or ord(s[1]) > 0x2000)) or \
                    (i > 0 and s[i - 1] == " " and (i + 2 >= n or not s[i + 2].isalnum())):
                out.append(r"\dd ")
                i += 1
                continue
        if c == "√":
            mm = re.match(r"√(\d+|[A-Za-z]|\([^()]*\))", s[i:])
            if mm:
                arg = mm.group(1)
                arg = arg[1:-1] if arg.startswith("(") else arg
                out.append(r"\sqrt{" + math(arg, row, True) + "}")
                i += len(mm.group(0))
                continue
        if c == "e" and i + 1 < n and s[i + 1] == "^" and (i == 0 or not s[i - 1].isalpha() or
                                                          re.match(r"\^\{?[−+-]?i", s[i + 1:])):   # Ôe^{−iωt}
            out.append(r"\ee")
            last_base = ("", "")
            i += 1
            continue
        if c in "{}":
            out.append("\\" + c)   # a literal brace (anticommutator, set); script groups were consumed above
            i += 1
            continue
        if c == "Σ" and not symbol:
            rest = s[i + 1:]
            selfenergy = (rest == "" or rest[0] in "^₁₂,;)" or re.match(r"_[xc](?:\(|$|[ ,;)])", rest) is not None or
                          rest.startswith(" ("))
            if not selfenergy:
                out.append(r"\sum ")
                last_base = ("", "")
                i += 1
                continue
        if c == "i" and not inner and (i == 0 or s[i - 1] in " +−-(^{[±∓|" or s[i - 1].isdigit() or
                                       unicodedata.combining(s[i - 1])) and \
                (i + 1 < n and (alphabet(unicodedata.normalize("NFD", s[i + 1])[0]) is not None or s[i + 1] in "(∇∂0") and
                 s[i + 1] not in "_^" or
                 (i > 0 and s[i - 1].isdigit() and (i + 1 == n or s[i + 1] in " ,;)"))):
            out.append(r"\ii ")   # the imaginary unit: e^{iq·r}, ib_y, f₁ + if₂, iω, 2i
            last_base = ("", "")
            i += 1
            continue
        if c == "…" and ((i > 0 and s[i - 1] == ":") or (i + 1 < n and s[i + 1] == ":")):
            out.append(r"\cdots ")
            i += 1
            continue
        if c in VECLETTERS and not symbol and not inner and BOLDVEC.get(c) and \
                "".join(out).count("\\{") <= "".join(out).count("\\}") and \
                (i == 0 or not (s[i - 1].isalnum() or s[i - 1] in "_^\\/") or (out and out[-1] == r"\ii ")) and \
                (i + 1 == n or not (s[i + 1].isalnum() or s[i + 1] in "_^" or s[i + 1] in SUPCH or s[i + 1] in SUBCH or
                                   unicodedata.combining(s[i + 1]))):
            out.append(r"\vect{%s}" % c)   # a vector letter that the first-use section prints bold
            last_base = (r"\vect{%s}" % c, c)
            i += 1
            continue
        if c in SYMB and c not in "{}′″†‡":
            out.append(SYMB[c])
            i += 1
            continue
        if c in VECLETTERS and i + 1 < n and s[i + 1] == "_" and (i == 0 or not s[i - 1].isalnum()):
            # a subscripted vector letter (Q_CDW, q_r, G_U): bold when the tex prints that symbol bold more often than plain
            content_, _, _ = take_script(s, i + 2)
            cnt_ = BASES.get(c + "_" + norm_key(content_), {})
            nb = sum(v for k_, v in cnt_.items() if k_.startswith("\\vect"))
            if nb > sum(cnt_.values()) - nb:
                out.append(r"\vect{%s}" % c)
                last_base = (r"\vect{%s}" % c, c)
                i += 1
                continue
        nfd = unicodedata.normalize("NFD", c)
        letter = alphabet(nfd[0]) if nfd else None
        if letter is not None:
            accents = list(nfd[1:])
            j = i + 1
            while j < n and unicodedata.combining(s[j]):
                accents.append(s[j])
                j += 1
            tex = letter
            for a in accents:
                if a in ACC:
                    tex = ACC[a] + "{" + tex + "}"
                else:
                    log_unrendered.append((row, s, "accent U+%04X" % ord(a)))
            uni = c + "".join(s[i + 1:j])
            # uppercase Greek: the book's choice between upright and italic, read from the tex
            if nfd[0] in "Γ":
                bk = base_key(tex, uni)
                cnt = Counter()
                for k2, v in [(bk, BASES.get(bk, {}))]:
                    if True:
                        for raw, nn in v.items():
                            if raw.startswith("\\Gamma") or raw.startswith("\\varGamma"):
                                cnt[raw.split("_")[0].split("{")[0]] += nn
                if cnt and not uni.startswith("Γ_") and s.strip() == "Γ":
                    tex = cnt.most_common(1)[0][0]
            out.append(tex)
            last_base = (tex, unicodedata.normalize("NFD", uni))
            i = j
            continue
        if c in "_^":
            content, j, braced = take_script(s, i + 1)
            bk = base_key(*last_base) if last_base[1] else ""
            table = SUBS if c == "_" else SUPS
            if not braced and content and len(content) >= 2 and (bk, norm_key(content)) not in table and \
                    j < n and s[j] in "_^" and alphabet(content[-1]) and \
                    (c == "_" and norm_key(content) in GSUBS and len(norm_key(content)) > 1):
                j -= 1   # m_em_p: a subscript known elsewhere, but the last letter starts the next factor here
                content = content[:-1]
            if c == "_" and not braced and out and out[-1].startswith(r"\sum") and "δ" in content[1:]:
                k_ = content.index("δ", 1)
                j -= len(content) - k_
                content = content[:k_]
            if not braced and content and (bk, norm_key(content)) not in table and \
                    not (c == "_" and norm_key(content) in GSUBS and len(norm_key(content)) > 1):
                # a new factor starts at a capital Greek letter, a bold, script, fraktur or sans letter, or an accented
                # letter, unless a longer spelling of this script is in the tex
                cut = None
                for q in range(1, len(content)):
                    ch = content[q]
                    nfd = unicodedata.normalize("NFD", ch)
                    if unicodedata.combining(ch):
                        continue
                    if ch in "ΓΔΘΛΞΠΣΥΦΨΩ∇∂" or 0x1D400 <= ord(ch) <= 0x1D7FF or ch in "ℬℰℱℋℐℒℳℛ𝓃" or \
                            (len(nfd) > 1 and nfd[1] in ACC) or (q + 1 < len(content) and unicodedata.combining(content[q + 1])):
                        cut = q
                        break
                if cut is not None:
                    j -= len(content) - cut
                    content = content[:cut]
                nk2 = norm_key(content)
                if len(content) >= 2 and (bk, nk2) not in table and not (c == "_" and nk2 in GSUBS and len(nk2) > 1):
                    if j < n and s[j] in "_^" and not unicodedata.combining(content[-1]):
                        # ∂_αu_β: the last letter of the run is the base of the next factor
                        j -= 1
                        content = content[:-1]
                    elif (bk, norm_key(content[:-1])) in table and alphabet(content[-1]) and \
                            not unicodedata.combining(content[-1]):
                        # m_ev: the subscript the tex uses, then a new factor
                        j -= 1
                        content = content[:-1]
                # m_φv: a Greek index followed by one Latin factor; ε^μνρσF_ρσ: Greek indices followed by a capital
                mm = re.match(r"^([^\x00-\x7f]+)([A-Za-z])$", content)
                if mm and (bk, norm_key(mm.group(1))) in table:
                    content = mm.group(1)
                    j -= 1
                else:
                    mm = re.match(r"^([\u0370-\u03ff]+)([A-Z].*)$", content)
                    if mm:
                        content = mm.group(1)
                        j -= len(mm.group(2))
            if content.startswith("(") and content.endswith(")") and c == "^":
                tex = "(" + math(content[1:-1], row, True) + ")"
            elif braced and not content.startswith("("):
                nk = norm_key(content)
                if (bk, nk) in table:
                    tex = table[(bk, nk)].most_common(1)[0][0]
                else:
                    tex = math(content, row, not (c == "^" and out and out[-1] == r"\ee"))   # e^{iq·r}: q may be bold
            elif content.startswith("("):
                tex = math(content, row, True)
            else:
                tex = script_tex(content, bk, c, row)
            if c == "^":
                add_sup(out, tex)
            else:
                out.append("_{" + tex + "}")
            i = j
            continue
        if c in SUPCH and i + 1 < n:
            pass
        mu = re.match(r"(%s)(?![A-Za-z])" % UNIT_ALT, s[i:]) if i > 0 and (s[i - 1].isdigit() or s[i - 1] in SUPCH) else None
        if mu and len(mu.group(1)) >= 2:
            out.append(r"\,\mathrm{%s}" % mu.group(1))
            last_base = ("", "")
            i += len(mu.group(1))
            continue
        if c in SUPCH:
            j = i
            while j < n and s[j] in SUPCH:
                j += 1
            add_sup(out, s[i:j].translate(SUPMAP))
            i = j
            continue
        if c in SUBCH:
            j = i
            while j < n and s[j] in SUBCH:
                j += 1
            dg = s[i:j].translate(SUBMAP)
            if out and out[-1].startswith("_{") and out[-1].endswith("}"):
                out[-1] = out[-1][:-1] + "_{" + dg + "}}"   # m_χ₁ = m_{χ_1}
            else:
                out.append("_{" + dg + "}")
            i = j
            continue
        if c in "′″†‡" or (c == "*" and out and not out[-1].endswith(" ")):
            add_sup(out, {"′": r"\prime", "″": r"\prime\prime", "†": r"\dagger", "‡": r"\ddagger", "*": "*"}[c])
            i += 1
            continue
        if c in SYMB:
            out.append(SYMB[c])
            i += 1
            continue
        if c == " ":
            out.append(" ")
            i += 1
            continue
        if c.isascii():
            out.append(c)
            i += 1
            continue
        log_unrendered.append((row, s, "character %r U+%04X" % (c, ord(c))))
        out.append(r"\,?\,")
        i += 1
    t = ""
    for piece in out:  # \pi G, \alpha m: a control word followed by a letter needs a space
        if piece and (piece[0].isalnum()) and re.search(r"\\[A-Za-z]+$", t):
            t += " "
        t += piece
    t = fix_cmds(t)
    t = re.sub(r" +", " ", t).strip()
    # a dangling space before a script or closing brace breaks nothing, but keep it tidy
    t = re.sub(r" ([_^}),])", r"\1", t)
    return t


# ----------------------------------------------------------------------------------------------------------- explicit map
# Symbols that do not convert mechanically (NOTATION spelling -> TeX math).
EXPLICIT = {
    "Γ, X, L, K": r"\Gamma$, $\mathrm{X}$, $\mathrm{L}$, $\mathrm{K}",
    "dℛ/dω": r"\dd\mathcal{R}/\dd\omega",
    "⟨σv⟩": r"\langle\sigma v\rangle",
    "ħ": r"\hbar",
    "Ω_c h²": r"\Omega_{\mathrm{c}}h^2",
    "ħ, c, k_B": r"\hbar, c, k_{\mathrm{B}}",
    "dΩ_q": r"\dd\Omega_{\vect{q}}",
    "x*_max": r"x^{*}_{\mathrm{max}}",
    "𝔚^(2),th": r"\mathfrak{W}^{(2),\mathrm{th}}",
    "σ_ln ℛ": r"\sigma_{\ln\mathcal{R}}",
    # App. B post-revision check (2026-11-07, items 9, 11): the piezoelectric tensor e^{\mathrm{pz}} (an "e^" would be read as
    # the exponential) and the Yukawa coupling y_{\chi\tilde\nu} (the tilde would start a new factor), spelled as in 6.2, 10.9
    "e^pz_αβγ": r"e^{\mathrm{pz}}_{\alpha\beta\gamma}",
    "e^pz_zzz": r"e^{\mathrm{pz}}_{zzz}",
    "y_χν̃": r"y_{\chi\tilde{\nu}}",
    # the molecular labels 𝔬, 𝔵 of 16.4 inside a subscript (the converter starts a new factor at a fraktur letter)
    "A^λ_𝔬𝔵(Q)": r"A^{\lambda}_{\mathfrak{o}\mathfrak{x}}(Q)",
    "F_𝔬𝔵(q)": r"F_{\mathfrak{o}\mathfrak{x}}(q)",
    "f^(𝔬)_0𝔵(q)": r"f^{(\mathfrak{o})}_{0\mathfrak{x}}(q)",
    "φ_co′": r"\phi_{c\mathfrak{o}'}",
    "φ_co′′′": r"\phi_{c\mathfrak{o}'''}",
    "φ_vo′′": r"\phi_{v\mathfrak{o}''}",
    "ρ_0x′^o": r"\rho^{(\mathfrak{o}')}_{0\mathfrak{x}'}",
}

# ----------------------------------------------------------------------------------------------------------- text
TEXTCH = {"–": "--", "—": "---", "’": "'", "‘": "`", "“": "``", "”": "''", "…": r"\dots{}", "%": r"\%", "&": r"\&",
          "#": r"\#", "$": r"\$", "~": r"\textasciitilde{}", "°": r"\textdegree{}", "\u00a0": "~", "\u2009": r"\,",
          "\u202f": r"\,", "Å": r"\AA{}", "µ": r"$\mu$", "½": r"$\frac{1}{2}$", "×": r"$\times$", "∼": r"$\sim$", "≈": r"$\approx$", "→": r"$\to$"}
LATIN1_OK = set("éèêëáàâäíìîïóòôöúùûüçñÉÈÜÖÄßøØåÅ")

UNIT_WORDS = ("eV keV MeV GeV TeV meV μeV neV peV ueV cm m km mm nm pm fm μm um Å s ms μs ns ps fs K mK μK kg g mg yr d h min "
              "Hz kHz MHz GHz THz T mT μT G V mV kV A mA J W mW μW pW kpc pc Mpc rad sr mol bar Pa GPa e erg dyn barn b "
              "keVnr keVee eVee eVnr ee nr C F Ω S cm² kpc ppm ppb dru day days yrs Bq mBq μBq bohr Ry Ha").split()
UNIT_ALT = "|".join(sorted("eV keV MeV GeV TeV meV neV cm km nm kg yr mK Hz kHz MHz GHz THz kpc Mpc GPa".split(), key=len,
                           reverse=True))
UNIT_RE = re.compile(r"^(?:%s)(?:[⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?$" % "|".join(sorted(map(re.escape, UNIT_WORDS), key=len, reverse=True)))


def unit_tex(tok):
    m = re.match(r"^(.*?)([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?$", tok)
    base, exp = m.group(1), m.group(2)
    base_t = base.replace("μ", r"\mu").replace("Å", r"\text{\AA}").replace("Ω", r"\Omega")
    if base_t.startswith("\\mu"):
        t = r"\mu\mathrm{%s}" % base_t[3:]
    elif base_t.startswith("\\text") or base_t.startswith("\\Omega"):
        t = base_t
    else:
        t = r"\mathrm{%s}" % base_t
    if exp:
        t += "^{%s}" % exp.translate(SUPMAP)
    return t


MATHCH = set("_^=<>≈≃≤≥≪≫∝≡≠∼⟨⟩|∫∑∏∂∇√·±∓→∞⊙⊕≻⌊⌋𝟙′″†‡½⊃ᵀ−{}∈") | SUPCH | SUBCH
TEXT_OPERATORS = {"Re", "Im", "ln", "exp", "sin", "cos", "tan", "Tr", "det", "max", "min", "log", "sinh", "cosh", "tanh", "diag"}


def is_mathy(tok):
    core = tok.strip(".,;:")
    if not core:
        return False
    if any(c in MATHCH for c in core):
        return True
    for c in core:
        o = ord(c)
        if c in GREEK or (0x1D400 <= o <= 0x1D7FF) or c in "ℬℰℱℋℐℒℳℛℭℌℨ𝓃":
            return True
        if unicodedata.combining(c) or (unicodedata.normalize("NFD", c) != c and c not in LATIN1_OK):
            return True
    if re.fullmatch(r"\(?[b-zB-HJ-Z]\)?", core) or (len(core) == 1 and core in "ôêâ"):  # one letter (not a, I, A); ô
        return True
    if re.fullmatch(r"\(?\d+[a-z]\)?", core) and not re.fullmatch(r"\(?\d[spdf]\)?", core) or re.fullmatch(r"\(?[b-zB-HJ-Z]\([A-Za-z0-9,]+\)[*′]?\)?", core) or \
            re.fullmatch(r"\(?\d+\([A-Za-z]", core) or re.fullmatch(r"\(?[A-Za-z]{1,3}\*[A-Za-z]{0,3}\)?", core):
        return True   # 2y, p(y), 2(N, ka*, m*c
    if re.fullmatch(r"d[xyzqkrtuvsEωΩθφϕ]", core):
        return True   # the differential of ∫P_d dy
    if re.fullmatch(r"[\d.]*[/(][\d/().+]*", core) and any(ch.isdigit() for ch in core):
        return True   # 1/(1
    if re.fullmatch(r"[\[(|]*[\d.]*[A-Za-z]?[\])|]*/[\[(|]*[\d.]*[A-Za-z]?[\])|]*", core) and \
            re.search(r"[\[\]()|]", core) or re.fullmatch(r"[\[(]+\d[\d.]*", core):
        return True   # y)/(1, [(1
    if re.fullmatch(r"\(?[b-zB-HJ-Z]\)+", tok.strip(".,;:")):
        return True   # s)) closing a math group
    return False


OPS = {"=", "+", "−", "-", "≈", "<", ">", "≤", "≥", "×", "/", "~", "∼", "∝", "→", "±", "≪", "≫", "≡", "≠", "≃", "·", "≲", "≳",
       "∈", "⊥", "∥"}
NUM_RE = re.compile(r"^\(?[0-9][0-9.,]*\)?[,;.]?$")


def is_unit(tok):
    core = tok.strip(".,;:()")
    return bool(core) and bool(UNIT_RE.match(core))


HYPHEN_RE = re.compile(r"^(\(?)([^\s-]+)-(th|[a-z]{3,}[a-z-]*)([.,;:)]*)$")


# Meanings whose juxtaposed factors cannot be told apart mechanically (NOTATION spelling -> spelling with braces or spaces).
TEXT_FIX = {
    "u*_ck_j′u_ck_j": "u*_{ck_j′} u_{ck_j}",
    "w_κZ_κ": "w_κ Z_κ",
    "𝗑_abc†_ac_b": "𝗑_ab c†_a c_b",
    "O(m_ev⁴)": "O(m_e v⁴)",
    "∫₀^∞dω": "∫₀^∞ dω",
    # post-revision check of App. B (2026-11-07): juxtaposed factors that the converter split at the wrong letter
    "v_C + v_CRv_C": "v_C + v_C R v_C",
    "𝐮·J_z𝐩": "𝐮·J_z 𝐩",
    "exp(α_dd† − α_d*d)": "exp(α_d d† − α_d* d)",
    "ρ_χσ̄_eη/m_χ": "ρ_χ σ̄_e η/m_χ",
    "e^{iq·r_𝔬}f^(𝔬)_0𝔵": "e^{iq·r_𝔬}f^(𝔬)_{0𝔵}",
}


RAW_FIX = {
    "A ∈ {ad, 0, +}": r"$A \in \{\mathrm{ad}, 0, +\}$",
    "X ∈ {prim, Luke, gap}": r"$X \in \{\mathrm{prim}, \mathrm{Luke}, \mathrm{gap}\}$",
    "(km s⁻¹)²": r"$(\mathrm{km}\,\mathrm{s}^{-1})^{2}$",
    "(readout unit)² × time": r"(readout unit)$^{2}$ $\times$ time",   # 𝒮_sig, 𝒮_n of 14.6
    "of stream a of": r"of stream $a$ of",   # ξ_a of 21.2: the index a, not the article (post-revision check, item 14)
    # final residuals (2026-11-07): a precomposed accented letter used as a symbol printed as a text letter
    "diagonalizes ô)": r"diagonalizes $\hat{o}$)",
    "M^±_cvν(k, Q; ê)": r"$M^{\pm}_{cv\nu}(\vect{k}, \vect{Q}; \hat{e})$",
}


def text(s, row, unit_cell=False):
    """Convert a NOTATION meaning (prose with inline math) to TeX."""
    raw = {}
    for k_, (a, b) in enumerate(RAW_FIX.items()):
        if a in s:
            s = s.replace(a, "RAWFIX%d" % k_)
            raw["RAWFIX%d" % k_] = b
    t = text_(s, row, unit_cell)
    for ph, b in raw.items():
        t = t.replace(ph, b)
    return t


def text_(s, row, unit_cell=False):
    for a, b in TEXT_FIX.items():
        s = s.replace(a, b)
    s = unicodedata.normalize("NFC", s.replace("\\|", "|"))
    words = [t for t in re.split(r" +", s) if t]
    kinds = []
    for k, w in enumerate(words):
        prev = kinds[k - 1] if k else None
        if w in OPS:
            kinds.append("op")
        elif unit_cell and is_unit(w):
            kinds.append("unit")
        elif HYPHEN_RE.match(w) and is_mathy(HYPHEN_RE.match(w).group(2)):
            kinds.append("hy")
        elif re.fullmatch(r"\(?[A-Za-z]{3,}-[^\s-]+", w) and is_mathy(w.split("-", 1)[1].rstrip(".,;:)")) and \
                not is_unit(w.split("-", 1)[1]):
            kinds.append("hy2")
        elif (prev in ("num", "unit") or (k and is_unit(words[k - 1]) and any(ch in SUPCH for ch in w)) or
              (prev == "m" and (words[k - 1][-1].isdigit() or words[k - 1][-1] in SUPCH))) and is_unit(w) \
                and not words[k - 1].rstrip().endswith((",", ";")):
            kinds.append("unit")
        elif NUM_RE.match(w):
            kinds.append("num")
        elif is_mathy(w):
            kinds.append("m")
        elif re.match(r"\(?(?:%s)[(\[]" % "|".join(TEXT_OPERATORS), w):
            kinds.append("m")   # diag(1, −1)
        elif w.strip(".,;:()[") in TEXT_OPERATORS and k + 1 < len(words) and is_mathy(words[k + 1]):
            kinds.append("m")   # Re z, Im z, (sin x − x cos x)
        elif w.strip(".,;:()") in ("a", "A", "I"):
            kinds.append("amb")
        else:
            kinds.append("t")
    for k in range(len(words) - 2, -1, -1):  # "km" in "100h km s⁻¹"
        if kinds[k + 1] == "unit" and kinds[k] == "t" and is_unit(words[k]):
            kinds[k] = "unit"
    # operators, numbers and ambiguous letters next to math join the math
    changed = True
    while changed:
        changed = False
        for k in range(len(words)):
            left = kinds[k - 1] if k > 0 else None
            right = kinds[k + 1] if k + 1 < len(words) else None
            if kinds[k] == "op" and (left in ("m", "num", "op2", "amb") or right in ("m", "op2", "amb")):
                kinds[k] = "op2"
                changed = True
            elif kinds[k] in ("num", "amb") and (left == "op2" or right == "op2"):
                kinds[k] = "m"
                changed = True
            elif kinds[k] == "amb" and words[k].endswith(",") and right == "m" and \
                    re.fullmatch(r"\(?[A-Za-z][,;)]?", words[k + 1]):
                kinds[k] = "m"   # rows a, b; groups A, B
                changed = True
            elif kinds[k] == "num" and left == "m" and (right == "m" or words[k - 1].endswith(",") and
                                                         re.fullmatch(r"\d+\)[,;.]?", words[k])):
                kinds[k] = "m"   # (i = 1, 2)
                changed = True
            elif kinds[k] == "num" and left == "m" and re.search(r"= ?\d+,(?: \d+,)*$", " ".join(words[max(0, k - 6):k])) and (
                    re.fullmatch(r"\d+,", words[k]) and right == "num" or
                    re.fullmatch(r"\d+\)?[;.]?", words[k]) and right in (None, "t", "amb")):
                kinds[k] = "m"   # (n = 0, 1, 2), j = 1, 2: the rest of a value list after "= 0," (post-revision check, item 14)
                changed = True
            elif kinds[k] == "t" and words[k].strip(".,;:()") in TEXT_OPERATORS and (left == "m" or right == "m"):
                kinds[k] = "m"   # x cos x
                changed = True
    out = []
    k = 0
    while k < len(words):
        if kinds[k] in ("m", "op2"):
            j = k
            while j < len(words) and kinds[j] in ("m", "op2"):
                j += 1
                sofar = " ".join(words[k:j])
                if words[j - 1].endswith(";") and sofar.count("(") <= sofar.count(")") and \
                        sofar.count("[") <= sofar.count("]"):
                    break   # a semicolon ends the math: "at angle $\mu$; $\omega_\mu^2 ...$"
            span = " ".join(words[k:j])
            m = re.match(r"^(.*?)([,;:.]*)$", span)
            core, punct = m.group(1), m.group(2)
            lead = trail = ""
            while core.startswith("(") and core.count("(") > core.count(")"):
                lead, core = lead + "(", core[1:]
            while core.endswith(")") and core.count(")") > core.count("("):
                trail, core = ")" + trail, core[:-1]
            m2 = re.match(r"^(.*?)([,;:.]*)$", core)
            core, punct = m2.group(1), m2.group(2) + trail + punct
            out.append(lead + "$" + math(core, row) + "$" + punct)
            k = j
        elif kinds[k] == "unit":
            j = k
            while j < len(words) and kinds[j] == "unit":
                j += 1
            us = words[k:j]
            last = us[-1]
            m = re.match(r"^(.*?)([.,;:)]*)$", last)
            us[-1] = m.group(1)
            lead = ""
            out.append("$" + r"\,".join(unit_tex(u.strip("()")) for u in us) + "$" + m.group(2))
            k = j
        else:
            w = words[k]
            if kinds[k] == "op":
                w = {"−": "--", "×": r"$\times$", "→": r"$\to$", "≈": r"$\approx$", "±": r"$\pm$", "~": r"$\sim$",
                     "∼": r"$\sim$", "<": "$<$", ">": "$>$", "≤": r"$\le$", "≥": r"$\ge$", "∝": r"$\propto$",
                     "≪": r"$\ll$", "≫": r"$\gg$", "·": r"$\cdot$", "∈": r"$\in$", "⊥": r"$\perp$",
                     "∥": r"$\parallel$"}.get(w, w)
                out.append(w)
            elif kinds[k] == "hy2":
                a_, b_ = w.split("-", 1)
                mm = re.match(r"^(.*?)([.,;:)]*)$", b_)
                out.append(textchars(a_, row) + "-$" + math(mm.group(1), row) + "$" + mm.group(2))
            elif kinds[k] == "hy":
                mm = HYPHEN_RE.match(w)
                out.append(mm.group(1) + "$" + math(mm.group(2), row) + "$-" + mm.group(3) + mm.group(4))
            else:
                out.append(textchars(w, row))
            k += 1
    t = " ".join(out)
    t = re.sub(r"(\d) \$\\mathrm", r"\1~$\\mathrm", t)
    return t


def textchars(w, row):
    o = []
    for c in w:
        if c in TEXTCH:
            o.append(TEXTCH[c])
        elif c.isascii() or c in LATIN1_OK:
            if not c.isascii() and len(w.strip("()[],;:.")) == 1:
                # a lone accented letter is a symbol (ô, ê), not a letter of a name
                log_unrendered.append((row, w, "accented letter used as a symbol %r U+%04X" % (c, ord(c))))
            o.append(c)
        elif c in GREEK:
            o.append("$" + GREEK[c] + "$")
        elif c in SYMB:
            o.append("$" + SYMB[c].strip() + "$")
        else:
            log_unrendered.append((row, w, "text character %r U+%04X" % (c, ord(c))))
    return "".join(o)


def units(u, row):
    u = u.strip()
    if u in ("—", "-", ""):
        return "---"
    parts = [p.strip() for p in u.split(";")]
    out = []
    for p in parts:
        if p in ("—", "-"):
            out.append("---")
            continue
        mm = re.fullmatch(r"\(([^()]+)\)([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)", p)
        if mm and units(mm.group(1), row).startswith("$"):
            inner = units(mm.group(1), row).strip("$")
            out.append("$(" + inner + ")^{" + mm.group(2).translate(SUPMAP) + "}$")
            continue
        mm = re.fullmatch(r"(\S+(?: \S+)*?) \(([^()]+)\)", p)
        if mm and units(mm.group(1), row).startswith("$") and units(mm.group(2), row).startswith("$"):
            out.append(units(mm.group(1), row) + " (" + units(mm.group(2), row) + ")")
            continue
        mm = re.fullmatch(r"(\S+(?: \S+)*?) (\([^()]*[A-Za-z]{3,}[^()]*\))", p)
        if mm and units(mm.group(1), row).startswith("$"):
            out.append(units(mm.group(1), row) + " " + text(mm.group(2), row, unit_cell=True))
            continue
        if p == "1":
            out.append("1")
            continue
        toks = [x for x in re.split(r"[ ·]+", p) if x]
        ts = []
        for t in toks:
            if UNIT_RE.match(t):
                ts.append(unit_tex(t))
            elif re.fullmatch(r"\((?:velocity|length|energy|momentum|time|mass|charge|frequency|area|volume|"
                              r"wavevector|density|temperature|field|angle|action|force)\)(?:[⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?", t):
                mm = re.match(r"\((\w+)\)(.*)", t)
                ts.append(r"(\text{%s})%s" % (mm.group(1), ("^{%s}" % mm.group(2).translate(SUPMAP)) if mm.group(2) else ""))
            elif re.fullmatch(r"eV\^\{[^}]*\}", t) or re.fullmatch(r"[A-Za-z]+\^\{?[-0-9/a-z]+\}?", t):
                b, e = t.split("^", 1)
                ts.append(r"\mathrm{%s}^{%s}" % (b, e.strip("{}")))
            elif re.fullmatch(r"(\S+?)\^\{([^}]*)\}", t) and UNIT_RE.match(t.split("^")[0]):
                b, e = t.split("^", 1)
                ts.append(unit_tex(b) + "^{%s}" % e.strip("{}").replace("\u2212", "-"))
            elif re.fullmatch(r"(?:velocity|length|energy|momentum|time|mass|area|volume)(?:[⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?", t):
                mm = re.match(r"([a-z]+)(.*)", t)
                ts.append(r"\text{%s}%s" % (mm.group(1), ("^{%s}" % mm.group(2).translate(SUPMAP)) if mm.group(2) else ""))
            elif re.fullmatch(r"[0-9.]+", t):
                ts.append(t)
            else:
                ts.append(None)
        if all(x is not None for x in ts):
            out.append("$" + r"\," .join(ts) + "$")
        else:
            out.append(text(p, row, unit_cell=True))
    return "; ".join(out)


# ----------------------------------------------------------------------------------------------------------- cleaning
EDITORIAL = re.compile(
    r"(\b\d{1,2}\.\d{1,2}[a-z]?\b|\b[A-F]\.\d{1,2}\b|\bApp\.|\bApps\.|\bChap|\bSect|\bEq\.|\bEqs\.|\beq:|\bentry\b|\bentries\b|"
    r"clash|merge|moved|removed|retired|SEAM|\bR\d+\b|\d{4}-\d{2}-\d{2}|mandatory|macro|\bnever\b|\bnot\b|\bonly\b|\bbare\b|"
    r"\blocal\b|et al|Table|\bRef|upright|italic|\bbold|calligraphic|fraktur|\bscript\b|sans|subscript|superscript|spelling|"
    r"\brow\b|\brows\b|draft|planned|research|literature|distinct from|renamed|formerly|\bcf\.|vartheta|varepsilon|\bhat\b|"
    r"\bprime\b|decoration|\bflag|⚑|\bWE\b|Worked example|Limit Check|\bnamed\b|\bdefined\b|derived|\bprecise\b|\bsee\b|"
    r"\bnot to be|\bdo not|\blabel\b|\bdrop|\bwritten\b|\bwrites\b|\bthe book\b|CODATA|NIST|arXiv|\bsource|\bvalue from|"
    r"\bquoted\b|\bin words\b|\bnotation\b|tilde|\bbar\b|\bdagger|\bindex\b|\bindices\b|\bargument\b|\bsymbol\b|"
    r"\bthis book\b|\bhere\b|Fig\.|\bRefs?\.|\bcampaign|\bledger|\breview|\bbrief|\beditor|\bwriter|\bvs\.|\bunit vector\b|"
    r"\bagainst\b|two symbols|\bvarphi\b)")
# a citation in parentheses: a name with a year, with "et al." or with a second name ("(Einstein)" is a meaning, not a citation)
CITE_PAREN = re.compile(r"^[A-Z][a-z]+(?:[–-][A-Z][a-z]+)?(?:(?:,? (?:and|&) [A-Z][a-z]+)+(?: et al\.?)?(?:,? \(?\d{4}\)?)?|"
                        r"(?:,? (?:and|&) [A-Z][a-z]+)*(?: et al\.?)(?:,? \(?\d{4}\)?)?|(?:,? (?:and|&) [A-Z][a-z]+)*,? \(?\d{4}\)?)$")
# A process clause: editorial text that is not part of the meaning. A section number counts only as a true pointer ("also 3.3",
# "see D.32", "(3.3)"), never as a decimal value ("2.67/t_coh", "1.27 eV"); pointers after "of", "in", "from" are removed
# from the clause instead (clean_meaning), and the clause is dropped only if nothing but qualifiers is left.
PROCESS_CLAUSE = re.compile(
    r"(^\s*(bare|never|not |only|(?:sub|super)script(?! \S+ (?:without|for|marks|denotes|labels)\b)|the planned|replaces|"
    r"formerly|renamed|distinct from|in (?:\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2})\b)|mandatory|clash|\bitalic\b|\bupright\b|"
    r"\bcaption\b|\bLimit \d|"
    r"\bentry \d|merge|SEAM|\bR\d+\b|\d{4}-\d{2}-\d{2}|\beq:|\bthe research\b|\bthe draft|\bplanned\b|retired|"
    r"\bChapter \d+ uses\b|\bwrites\b|\bApp\. B\b|\bthe literature\b|\bApp\.|\bChap\.|\bSect\.|cond-mat|arXiv|"
    r"\bFig\.|\bWE\b|\bTable\b|Limit Check|"
    r"(?:\b(?:see|also|cf\.)\s+|\()(?:\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2})[a-z]?(?![\d.]|\s*[/×·]|\s*(?:%|[kMGTmμunp]?eV|"
    r"km|cm|nm|Å|K|s|THz|GHz|MHz|fm|GPa|kpc)\b))")
# what is left of a clause that held only qualified pointers ("qualitative in 1.3, precise in 3.3" -> "qualitative, precise")
QUALIFIERS_ONLY = re.compile(r"(?:\s*(?:qualitative|precise|named|defined|used|introduced|derived|first|also|and|,))*\s*")


def strip_parens(s, depth_ok=None):
    """Remove top-level (...) groups whose content is editorial. Keeps math groups like (m_V² + q²)."""
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == "(":
            d, j = 0, i
            while j < n:
                d += s[j] == "("
                d -= s[j] == ")"
                if d == 0:
                    break
                j += 1
            grp = s[i:j + 1]
            inner = grp[1:-1]
            attached = i > 0 and not s[i - 1].isspace() and s[i - 1] not in "–—-"
            if not attached and (EDITORIAL.search(inner) or CITE_PAREN.match(inner.strip()) or "\\" in inner):
                # drop, with the preceding space
                while out and out[-1] == " ":
                    out.pop()
                i = j + 1
                continue
            out.append(grp)
            i = j + 1
            continue
        out.append(s[i])
        i += 1
    return "".join(out)


def split_top(s, sep=";"):
    out, d, cur = [], 0, ""
    for ch in s:
        if ch in "([{⟨":
            d += 1
        elif ch in ")]}⟩":
            d -= 1
        if ch == sep and d == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out]


def remove_pointers(m):
    """Internal pointers in the running meaning: "of 3.3", "of WE 4.7", "in Table 8.1 and D.24", "from 13.4 on"."""
    sec = r"(?:\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2})[a-z]?(?![\d.]|\s*(?:%|[kMGTmμunp]?eV|km|cm|nm|Å|K|s|fm|GPa)\b)"
    pre = r"(?:WE\s+|Table\s+|Limit Check\s+|App\.\s+|Apps\.\s+|Sect\.\s+|Sects\.\s+|the\s+)?"
    m = re.sub(r",?\s+(?:of|in|from|as in|by)\s+%s%s(?:\s*(?:,|and)\s*%s%s)*(?:\s+on)?(?=[\s,;.:)]|$)" % (pre, sec, pre, sec), "", m)
    m = re.sub(r"\s+in Chaps?\.\s*[\d–-]+(?:\s+and)?", "", m)
    m = re.sub(r"\s+(?:of|in)\s+WE\s+[\w.:-]+", "", m)
    return m


def clean_meaning(m, nsym):
    m = m.replace("⚑", "").replace("\\|", "|").strip()
    m = strip_parens(m)
    m = strip_parens(m)
    m = re.sub(r"\s+", " ", m).strip()
    # equation labels in the running text go, not the clause that holds them: "angle averages of eq:20.3-avg for ...",
    # "case-I coherence integral ... of eq:7.2-pairspec, closed form eq:15.1-gI", "order symbol in eq:16.7-dp"
    eqlab = r"eq(?::|\.)\s?[A-Z]?[\w.:-]*[\w]"
    m = re.sub(r",?\s*closed form\s+" + eqlab, "", m)
    m = re.sub(r"\s+(?:of|in|from|as in|by|see)\s+" + eqlab, "", m)
    m = re.sub(r"\s+" + eqlab, "", m)
    # first sentence only
    m = re.split(r"(?<=[a-z0-9)$])\. (?=[A-Z])", m)[0]
    allc = [c for c in split_top(m, ";") if c]
    # 1. process clauses (never the first clause)
    keep = [c for k, c in enumerate(allc) if k == 0 or not PROCESS_CLAUSE.search(c)]
    # 2. pointers out of the running text; a clause left with qualifiers only goes. In a multi-symbol row a clause is dropped
    #    only if the clauses still match the symbols afterwards (or did not match them before): a dropped clause would shift
    #    every later meaning onto the wrong symbol.
    cleaned = [remove_pointers(c).strip(" ,") for c in keep]
    dropped = [c for k, c in enumerate(cleaned) if k == 0 or not QUALIFIERS_ONLY.fullmatch(c)]
    if nsym > 1 and len(cleaned) == nsym and len(dropped) != nsym:
        dropped = [c if c and not QUALIFIERS_ONLY.fullmatch(c) else "" for c in cleaned]
    clauses = [c for c in dropped if c]
    if nsym == 1 and len("; ".join(clauses)) > 150:
        clauses = clauses[:1]
    m = "; ".join(clauses)
    # comma-separated trailing remarks that are editorial
    m = re.sub(r",\s*(the )?(adopted|literature|reference) value [^;,]*$", "", m)
    m = re.sub(r",?\s*typeset \\\S+", "", m)
    m = re.sub(r"\s+([,;.])", r"\1", m).strip(" ,;")
    m = re.sub(r"\b(eq|sec|fig|lim|tab|app|chap|we):\S+", "", m)
    m = re.sub(r"\s+", " ", m).strip(" ,;:")
    return m


SECTOK = re.compile(r"(?<![\w.])(\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2})(?![\d])")


def first_use(cell):
    c = re.sub(r"\([^()]*(\([^()]*\)[^()]*)*\)", lambda mm: mm.group(0) if False else " ", cell)
    m = SECTOK.search(c)
    if not m:
        m = SECTOK.search(cell)
    return m.group(1) if m else None


def sec_sort(sec):
    a, b = sec.split(".")
    if a.isdigit():
        return (0, int(a), int(b))
    return (1, "ACDEF".index(a) if a in "ACDEF" else 9, int(b))


def group_of(sec):
    a = sec.split(".")[0]
    return ("ch", int(a)) if a.isdigit() else ("app", a)


def labels():
    labs = set()
    for f in TEX.rglob("*.tex"):
        if f.name == "B-1.tex":
            continue
        for m in re.finditer(r"\\label\{([^}]*)\}", f.read_text(encoding="utf-8", errors="replace")):
            labs.add(m.group(1))
    return labs


# ----------------------------------------------------------------------------------------------------------- symbol cell
NOTE_RE = re.compile(r"\s+\((?:[^()]*[A-Za-z]{3,}[^()]*)\)")
SECNOTE_RE = re.compile(r"\s*\((?:\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2})(?:,\s*(?:\d{1,2}\.\d{1,2}|[A-F]\.\d{1,2}))*\)")


def strip_notes(sym):
    return SECNOTE_RE.sub("", NOTE_RE.sub("", sym))


def split_items(sym):
    sym = strip_notes(sym)
    items = []
    for part in cn.split_top(sym, ",;"):
        items.append(part.strip())
    return [x for x in items if x]


def render_symbol(sym, row):
    s = SECNOTE_RE.sub("", sym.strip())
    if s in EXPLICIT:
        return "$" + EXPLICIT[s] + "$"
    seps = re.findall(r"([,;]) ", s)
    items = split_items(s)
    if not items:
        return ""
    texs = []
    for it in items:
        if it in EXPLICIT:
            texs.append(EXPLICIT[it])
        else:
            texs.append(math(it, row, symbol=True))
    # keep semicolons where the cell has them at top level
    out = "$" + texs[0] + "$"
    seplist = []
    d = 0
    s0 = strip_notes(s)
    for idx, ch in enumerate(s0):
        if ch in "([{⟨":
            d += 1
        elif ch in ")]}⟩":
            d -= 1
        elif ch in ",;" and d == 0 and idx + 1 < len(s0) and s0[idx + 1] == " ":
            seplist.append(ch)
    for k, t in enumerate(texs[1:]):
        sep = seplist[k] if k < len(seplist) else ","
        out += sep + " $" + t + "$"
    return out


def drop_dashed_symbols(sym, fu):
    """'ρ_crit: — (...); h: 1.1 (...)' -> remove ρ_crit from the symbol cell and return the remaining first-use text."""
    dead = re.findall(r"([^\s;:]+): —", fu)
    if not dead:
        return sym, fu, []
    items = cn.split_top(sym, ",;")
    keep = [x for x in items if x.strip() not in dead]
    fu2 = ";".join(p for p in split_top(fu, ";") if not re.search(r": —", p))
    return ", ".join(keep), fu2, dead


# ----------------------------------------------------------------------------------------------------------- scope notes
# Symbols with two meanings in different parts of the book that the editor accepted as local reuse (App. B review, editor ruling
# B3; NOTATION clash entry 96). B.1 lists both meanings; the local one carries a scope note. Key: the symbol as NOTATION spells
# it (None: the whole row) and the first-use section of its row; value: the labels of the sections where that meaning is used.
SCOPE = [
    ("E_p", "3.2", "sec:3.2"),                      # on-site p energy; E_p of 2.1 is the relativistic energy
    ("G_V", "10.8", "chap:10"), ("G_V", "11.1", "chap:11"),          # pair coupling; Voigt shear modulus
    ("s", "C.8", "app:C.8"),                        # elliptic modulus; s is the spin label of 2.3
    ("ω_p", "14.2", "sec:14.2"),                    # phonon energy at a crossing; ω_p is the plasma frequency
    ("v_T", "11.1", "chap:11"),                     # transverse sound speed; v_T is the transverse dark-matter velocity
    ("v₀", "D.7", "app:D.7,app:D.36"), ("v₀", "E.16", "app:E.16"),   # Coulomb head; contact kernel; v₀ is the halo speed
    (None, "22.3", "sec:22.3"),                     # the 22.3 rows: the fields p, n, e, χ, the CDW phase ϕ, ...
    ("ψ", "8.8", "sec:8.8"),                        # log-template; ψ is the Dirac field or a wavefunction
    ("ϵ", "3.5", "sec:3.5"), ("ϵ", "19.5", "sec:19.5"),               # E − m_e; collection efficiency
    ("Φ", "3.5", "sec:3.5"), ("Φ", "14.5", "sec:14.5"), ("Φ", "14.6", "sec:14.6"),
    ("L_e", "11.2", "chap:11"),                     # extraordinary-ray loss; L_e is the electron-channel loss
    ("c_L", "11.8", "sec:11.8"), ("c_L", "19.3", "sec:19.3"),         # plate speed; Lindhard constant
    ("ω_max", "19.2", "sec:19.2"),                  # ion-to-electron maximum; ω_max is the top of the phonon band
    ("Γ_abs", "20.5", "sec:20.5"),                  # per phonon in the film solve; per quantum of a bosonic field
    ("T_d", "14.4", "sec:14.4"), ("T_d", "16.6", "sec:16.6,sec:19.3,sec:19.4"),   # temperature; damage energy; point group
    ("U", "14.5", "sec:14.5"), ("U", "19.3", "sec:19.3"),             # molecular-magnet barrier; Sarkis binding energy
    ("N_X", "18.5", "sec:18.5"),                    # bound pairs at readout; N_X of 16.6 counts excitons per recoil
    ("Ξ", "C.12", "app:C.12,sec:21.2,app:D.46"),    # velocity measure; Ξ is the deformation constant
    ("ξ", "D.44", "app:D.44"),                      # one step ln(x_{j+1}/x_j); ξ is the energy mismatch
    ("ν", "4.5", "sec:4.5,app:D.8"),                # Lindhard reduced frequency; ν is the phonon branch
    ("α_M", "14.5", "sec:14.5"), ("α_M", "3.6", "app:E.10"),          # magnetoelectric coefficient; Madelung constant
    ("γ_n", "C.19", "app:C.19"),                    # neutron moment; γ_n is the width of mode n
    ("ω_k", "C.20", "app:C.20"), ("ω_k", "E.10", "app:E.10"),         # bath mode; vibronic mode
    ("j_L", "E.2", "app:E.2,app:E.7"),              # spherical Bessel function; j_L is the longitudinal current
    ("E_el", "19.2", "chap:19"),                    # electronic energy of a recoil; E_el of 5.4 is that of a configuration
    ("N_casc", "E.13", "app:E.13"),                 # simulated cascades; N_casc of 16.8 is the size of a release cascade
]
scope_used = set()


def scope_note(labels):
    return r"(in \cref{%s})" % labels


def apply_scope(sym, sec, mean, nsym, row):
    """Mark the clause of each scoped symbol of the row with a placeholder; returns (meaning, {placeholder: TeX})."""
    items = split_items(sym)
    notes = {}
    clauses = split_top(mean, ";") if mean else []
    aligned = nsym > 1 and len(clauses) == nsym == len(items)
    tail = []
    for k, (it, sc, labs_) in enumerate(SCOPE):
        if sc != sec or (it is not None and it not in items):
            continue
        scope_used.add(k)
        ph = "SCOPENOTE%d" % k
        if it is None or nsym == 1:
            tail.append(ph)
            notes[ph] = scope_note(labs_)
        elif aligned:
            j = items.index(it)
            clauses[j] = clauses[j] + " " + ph
            notes[ph] = scope_note(labs_)
        else:
            tail.append(ph)
            notes[ph] = r"($%s$ in \cref{%s})" % (math(it, row, symbol=True), labs_)
    if aligned:
        mean = "; ".join(clauses)
    if tail:
        mean = mean + " " + " ".join(tail)
    return mean, notes


# ----------------------------------------------------------------------------------------------------------- main
def main():
    labs = labels()
    lines = NOTATION.read_text(encoding="utf-8").split("\n")
    end = next(i for i, l in enumerate(lines) if l.startswith("## Clashes"))
    rows = []
    for ln, l in enumerate(lines[:end], 1):
        if not l.startswith("| ") or l.startswith("| Symbol") or l.startswith("|---"):
            continue
        cells = [x.strip() for x in re.split(r"\s\|\s", " " + l.strip() + " ")[1:-1]]
        if len(cells) != 4:
            # a bar inside a cell without spaces is a bracket; anything else is malformed
            log_unrendered.append((ln, l[:80], "row does not have four cells"))
            continue
        sym, mean, unit, fu = cells
        fu_s = fu.strip()
        if fu_s.startswith("—") or re.search(r"\bunused\b|\bremoved\b", re.sub(r"\(.*", "", fu_s)) or \
                re.fullmatch(r"—.*", fu_s):
            log_dropped.append((ln, sym, fu_s))
            continue
        if re.search(r"unused\)?\s*$", fu_s) and not SECTOK.search(re.sub(r"\(.*?\)", "", fu_s)):
            log_dropped.append((ln, sym, fu_s))
            continue
        orig_items = cn.split_top(sym, ",;")
        sym, fu_s, dead = drop_dashed_symbols(sym, fu_s)
        if dead:
            cl = split_top(mean, ";")
            if len(cl) == len(orig_items):
                mean = "; ".join(c for c, it in zip(cl, orig_items) if it.strip() not in dead)
            ul = split_top(unit, ";")
            if len(ul) == len(orig_items):
                unit = "; ".join(c for c, it in zip(ul, orig_items) if it.strip() not in dead)
        for d_ in dead:
            log_dropped.append((ln, d_, "first use — (within the row of " + cells[0] + ")"))
        if re.match(r"\s*literature notation", mean, re.I):
            log_dropped.append((ln, sym, "literature notation (listed in the correspondence table instead)"))
            continue
        sec = first_use(fu_s)
        if sec is None:
            log_dropped.append((ln, sym, fu_s + "  [no section found]"))
            continue
        rows.append(dict(ln=ln, sym=sym, mean=mean, unit=unit, sec=sec, nsym=len(split_items(sym))))

    groups = defaultdict(list)
    for r in rows:
        groups[group_of(r["sec"])].append(r)
    order = [("ch", i) for i in range(1, 23)] + [("app", a) for a in "ACDEF"]
    for g in groups:
        if g not in order:
            order.append(g)

    body = []
    counts = []
    for g in order:
        rs = sorted(groups.get(g, []), key=lambda r: (sec_sort(r["sec"]), r["ln"]))
        if not rs:
            counts.append((g, 0))
            continue
        counts.append((g, len(rs)))
        if g[0] == "ch":
            head = r"Chapter~\ref{chap:%d}: \nameref{chap:%d}" % (g[1], g[1])
        else:
            head = r"Appendix~\ref{app:%s}: \nameref{app:%s}" % (g[1], g[1])
        body.append(r"\addlinespace[4pt]")
        body.append(r"\multicolumn{4}{@{}l}{\bfseries %s}\\*" % head)
        body.append(r"\addlinespace[2pt]")
        for r in rs:
            rowid = "line %d" % r["ln"]
            sec_ = r["sec"]
            CURRENT["file"] = ("ch%02d/s%s.tex" % (int(sec_.split(".")[0]), sec_.replace(".", "-"))) if sec_[0].isdigit() \
                else "app%s/%s.tex" % (sec_[0], sec_.replace(".", "-"))
            BOLDVEC.clear()
            for ch, cnt in FILE_VEC.get(CURRENT["file"], {}).items():
                # a letter the first-use section prints bold at least twice as often as plain is a vector there
                BOLDVEC[ch] = cnt["bold"] >= 3 and cnt["bold"] >= 2 * cnt["plain"]
            symt = render_symbol(r["sym"], rowid)
            cm, notes = apply_scope(r["sym"], r["sec"], clean_meaning(r["mean"], r["nsym"]), r["nsym"], rowid)
            meant = text(cm, rowid)
            for ph, note in notes.items():
                meant = meant.replace(ph, note)
            for lab_ in re.findall(r"\\cref\{([^}]*)\}", "".join(notes.values())):
                for l_ in lab_.split(","):
                    if l_ not in labs:
                        log_unrendered.append((rowid, l_, "scope-note label not in the tex"))
            if meant:
                meant = meant[0].upper() + meant[1:] if meant[0].isalpha() and meant[0].islower() else meant
            unitt = units(r["unit"], rowid)
            sec = r["sec"]
            lab = ("sec:" if sec[0].isdigit() else "app:") + sec
            if lab in labs:
                fut = r"\labelcref{%s}" % lab
            else:
                fut = sec
                log_nolabel.append((r["ln"], r["sym"], sec))
            cells_t = []
            for cell in (symt, meant, unitt):
                cell = re.sub(r"\$[^$]*\$", lambda mm: mm.group(0).replace("\u2212", "-"), cell)
                bad = [ch for ch in cell if not ch.isascii() and ch not in LATIN1_OK]
                for ch in bad:
                    log_unrendered.append((rowid, r["sym"], "left in output: %r U+%04X" % (ch, ord(ch))))
                cells_t.append("".join(ch for ch in cell if ch.isascii() or ch in LATIN1_OK))
            symt, meant, unitt = cells_t
            body.append("%s & %s & %s & %s \\\\" % (symt, meant, unitt, fut))

    head = [
        "% List of symbols. GENERATED by figscripts/appB/gen_B1.py; do not edit by hand, rerun the script.",
        r"\section{List of symbols}\label{app:B.1}",
        "",
        r"Each symbol is listed once, under the chapter or appendix of its first use; the last column gives the section of its first use.",
        r"The Units column gives the dimension in natural units ($\hbar = c = k_{\mathrm{B}} = 1$, \cref{app:A.1}) and, after a",
        r"semicolon, the conventional unit in which values are quoted. The entry 1 marks a dimensionless quantity, and a dash an",
        r"object without a dimension of its own, such as an operator, a state or a label.",
        "",
        r"{\footnotesize",
        r"\setlength{\tabcolsep}{4pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.22\textwidth}>{\raggedright\arraybackslash}p{0.50\textwidth}"
        r">{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.06\textwidth}@{}}",
        r"\toprule",
        r"Symbol & Meaning & Units & Sect. \\",
        r"\midrule",
        r"\endfirsthead",
        r"\toprule",
        r"Symbol & Meaning & Units & Sect. \\",
        r"\midrule",
        r"\endhead",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    tail = [r"\end{longtable}", r"}", ""]
    OUT.write_text("\n".join(head + body + tail), encoding="utf-8")

    with LOG.open("w", encoding="utf-8") as f:
        f.write("gen_B1.py log: NOTATION.md -> tex/appB/B-1.tex\n\n")
        f.write("Rows per group (%d rows in the table)\n" % len(rows))
        for g, c in counts:
            f.write("  %-8s %4d\n" % (("Chap. %d" % g[1]) if g[0] == "ch" else ("App. " + g[1]), c))
        f.write("\nDropped rows or symbols (%d): first use is a dash, removed or unused\n" % len(log_dropped))
        for ln, s, fu in log_dropped:
            f.write("  line %4d  %-28s %s\n" % (ln, s, fu))
        f.write("\nFirst-use sections with no label in the tex (%d): printed as plain text\n" % len(log_nolabel))
        for ln, s, sec in log_nolabel:
            f.write("  line %4d  %-28s %s\n" % (ln, s, sec))
        f.write("\nScope notes (editor ruling B3; NOTATION clash entry 96): %d of %d applied\n" % (len(scope_used), len(SCOPE)))
        for k, (it, sc, labs_) in enumerate(SCOPE):
            f.write("  %-8s %-6s in %-32s %s\n" % (it or "(row)", sc, labs_, "" if k in scope_used else "[NOT APPLIED]"))
        f.write("\nUnrendered symbols or characters (%d)\n" % len(log_unrendered))
        seen = set()
        for row, s, why in log_unrendered:
            if (row, s, why) in seen:
                continue
            seen.add((row, s, why))
            f.write("  %s  %s  [%s]\n" % (row, s, why))
    print("rows %d, dropped %d, no label %d, unrendered %d" % (len(rows), len(log_dropped), len(log_nolabel),
                                                               len(set(log_unrendered))))


if __name__ == "__main__":
    main()
