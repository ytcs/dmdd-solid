#!/usr/bin/env python3
"""Symbol coverage check: every symbol printed in the tex of the book has a row in book/NOTATION.md.

Usage (from book/ or anywhere; paths are resolved from this file):
    python3 tools/check_notation.py [--bare] [--files GLOB ...] [--min N]
GLOB patterns are relative to tex/; the default is ch01/*.tex ch02/*.tex appA/*.tex. For the whole book:
    python3 tools/check_notation.py --files 'ch*/*.tex' 'app*/*.tex'
--bare also lists the bare Latin letters that have no row; --min N reports only gaps with at least N uses.
Exit status 1 when gaps are found, 0 otherwise. figscripts/appB/gen_B1.py imports the tokenizer of this file.

What it does
- Builds the set of NOTATION symbols from the Symbol column of book/NOTATION.md (every comma- or semicolon-separated item, arguments
  such as (q, ω) or [𝓃] dropped), normalized to a key  base[_sub][^sup]  (Unicode Greek, accents as combining marks, bold Latin
  dropped, bold Greek read as the plain letter, script/calligraphic/sans-serif/fraktur kept). A slash or semicolon inside braces
  belongs to the name (p_{1/2}).
- Extracts the math of the tex files ($...$, \\(...\\), \\[...\\], equation/align/gather/multline environments, starred or not), drops
  \\text{...}, \\label{...}, \\cref{...}, units (\\mathrm{...} that is not a sub- or superscript), and tokenizes it into symbols: a Latin
  letter, a Greek command, a typography macro of tex/macros.tex, or an accented/alphabet-wrapped letter (\\bar, \\tilde, \\hat, \\op,
  \\vect, \\bm, \\mathcal, \\mathscr, \\nd, \\mathsf, \\mathfrak), with its sub- and superscripts.
- A token matches when its key, or its key without a superscript (powers, daggers and primes are not part of a name), is a NOTATION
  key; a token whose subscript is only state/band/species/spin indices (i, f, n, m, k, s, σ, η, γ, κ, ...; offsets δ, Δ, ±; an
  ellipsis) matches a NOTATION row with the same base and an index subscript.
- Also accepted without a row: operators and constants in IGNORE (π, ∂, ∇, ħ); Kronecker deltas (δ with two or more index characters);
  any subscript on the bases of ANY_SUB (𝒮_O, 𝒟_{f_T}); Cartesian components on COMPONENT_BASES (k_x) and TENSOR_BASES (C_xxxx,
  σ_zz, S_xx); row labels in the subscripts of the response matrices on RESPONSE_BASES (S_{n_Mn_M}, R̃_{aZ}); a hat on a letter that
  has a row (its unit vector or operator), with index or component subscripts; a dot (time derivative); \\overline{...} is read as an
  average of its contents; ⟨σv⟩ is one symbol (its σ is not a bare σ).
- LOCAL lists symbols local to one passage that need no NOTATION row; LITERATURE lists notation that the text quotes from a cited
  paper (for App. B.2). Both are keyed by symbol (everywhere) or by (file, symbol) (one tex file only), and are reported apart.
- Bare (undecorated) Latin letters are generic (coordinates, dummies, indices) unless NOTATION has a row for them; they are reported
  only with --bare.

Macro-level extraction is feasible for decorated symbols and Greek letters; bare one-letter Latin symbols cannot be told apart from
dummy variables by a script, and are checked by grep (see --bare).
"""
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent
TEX = BOOK / "tex"
NOTATION = BOOK / "NOTATION.md"

GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ϵ", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
    "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π",
    "varpi": "ϖ", "rho": "ρ", "varrho": "ϱ", "sigma": "σ", "tau": "τ", "upsilon": "υ", "phi": "ϕ", "varphi": "φ", "chi": "χ",
    "psi": "ψ", "omega": "ω", "varGamma": "Γ", "varDelta": "Δ", "varTheta": "Θ", "varLambda": "Λ", "varXi": "Ξ",
    "varPi": "Π", "varSigma": "Σ", "varPhi": "Φ", "varPsi": "Ψ", "varOmega": "Ω", "varkappa": "κ", "varsigma": "σ", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ",
    "Upsilon": "Υ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω", "ell": "ℓ", "hbar": "ħ", "partial": "∂", "nabla": "∇",
}
# NOTATION writes φ for the field and ε for the dielectric function; LaTeX \phi and \epsilon are read as the same letters.
FOLD = {"ϕ": "φ", "ϵ": "ε"}
SYMS = {"to": "→", "rightarrow": "→", "prime": "′", "dagger": "†", "ast": "*", "star": "*", "infty": "∞", "odot": "⊙",
        "oplus": "⊕", "parallel": "∥", "perp": "⊥", "uparrow": "↑", "downarrow": "↓", "pm": "±", "mp": "∓", "cdot": "·",
        "ldots": "…", "dots": "…", "cdots": "…", "lt": "<", "gt": ">"}
SCRIPT = {c: s for c, s in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")}
SCRIPT_LOWER = {c: chr(0x1D4EA + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}  # bold script, as NOTATION writes 𝓃
SANS = {"G": "𝖦", "A": "𝖠", "F": "𝖥", "D": "𝖣", "L": "𝖫"}  # sans-serif functions of Chap. 4 and App. D (\GF, \SpecA)
# sans-serif Nambu objects of 7.2 and D.21 (dressed vertices 𝖵_η, 𝖵_j; phase coefficient 𝖼₂; matrices 𝗌₁, 𝗌₂, 𝗌_a)
SANS.update({"V": "𝖵", "c": "𝖼", "s": "𝗌"})
SANS.update({"Q": "𝖰"})  # 𝖰, 𝖰_obs of 14.6
SANS.update({"R": "𝖱", "f": "𝖿", "g": "𝗀", "t": "𝗍"})  # 𝖱_FC, 𝖿_u0, 𝗀_λ, 𝗍_ϑ of 21.2, 21.4, D.46, D.47
SANS.update({"M": "𝖬"})  # 𝖬_ik(Q̂) of C.18 and 𝖬_λλ′ of E.19
# \mathscr capitals are the bold-script letters NOTATION writes (𝓜¹), distinct from \mathcal (ℳ)
SCRIPT_BOLD = {c: chr(0x1D4D0 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
FRAK = {c: chr(0x1D504 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
FRAK.update({"C": "ℭ", "H": "ℌ", "I": "ℑ", "R": "ℜ", "Z": "ℨ"})
FRAK_LOWER = {c: chr(0x1D51E + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
ACCENT = {"bar": "\u0304", "tilde": "\u0303", "widetilde": "\u0303", "hat": "\u0302", "widehat": "\u0302",
          "op": "\u0302", "dot": "", "check": "\u030C"}  # a dot is a time derivative, not a new symbol
# typography macros of tex/macros.tex (and book-wide shorthands) -> NOTATION spelling
MACROS = {"Eg": "E_g", "mchi": "m_χ", "vmin": "v_min", "sigmae": "σ̄_e", "FDM": "F_DM", "GF": "𝖦", "SpecA": "𝖠", "hbar": "ħ",
          "Vol": "𝓥"}  # \Vol = \mathscr{V}, the normalization volume
# commands that are operators, spacing or structure, never symbols
SKIP = set("""frac dfrac tfrac sqrt left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr middle sum int iint iiint oint prod
lim max min sup inf sin cos tan cot sinh cosh tanh exp ln log arg det Re Im Tr Real Imag operatorname dd ee ii quad qquad
approx simeq sim propto equiv neq ne le leq ge geq ll gg lesssim gtrsim times div cdot cdots ldots dots vdots ddots in notin
subset cup cap wedge vee langle rangle lvert rvert lVert rVert vert Vert mid nonumber notag label tag eqref cref Cref ref cite
mathrm text textrm textit textbf mathit mathbf mathbb emph boldsymbol displaystyle textstyle scriptstyle limits nolimits
underbrace overbrace underset overset stackrel phantom hphantom vphantom mathstrut strut hline toprule midrule bottomrule
begin end qquad mathop mathrel mathbin mathord over choose binom pmod bmod gcd forall exists neg lnot land lor implies iff
leftarrow Leftarrow Rightarrow Leftrightarrow leftrightarrow mapsto longrightarrow uparrow downarrow updownarrow
circ bullet star dagger ddagger prime infty to rightarrow pm mp odot oplus otimes parallel perp hat bar tilde vect bm op
mathcal mathscr mathsf mathfrak nd widetilde widehat overline underline check dot ddot vec quad enspace thinspace negthinspace
SI si num unit qty ensuremath intertext shortintertext tfrac lbrace rbrace lfloor rfloor lceil rceil backslash setminus emptyset
varnothing aleph Box square triangle angle degree circledR checkmark ast colon dotsb dotsc dotsi dotsm dotso and
cases pmatrix bmatrix matrix aligned split gathered substack sb sp mkern mskip hspace vspace kern raisebox
lt gt le ge nexists sharp flat natural top bot imath jmath Im Re wp mho prec succ preceq succeq perp parallel""".split())
# Characters of a pure index subscript: state, band, spin, species, Lorentz, Cartesian and momentum labels.
INDEX_CHARS = set("ijfnmklsγκνμIJNPRTABabcvkqQGp′'αβ,+−-̃ _0123456789→↑↓[]()*")
# Offsets and signs inside index subscripts (H_{k₀+δk}, u_{n,k+Δk}, U_{±G₁}, ε_±), and ∥, ⊥.
INDEX_CHARS |= set("δΔ±∓∥⊥")
# An ellipsis inside an index list (Φ^{(n)}_{i₁…iₙ}, κκ′…κ′′).
INDEX_CHARS |= set("…")
# Spin labels σ (c_kσ, n_kσ, ψ_σ of 7.2, D.20, D.21) and the Nambu channel label η (R⁰_ηη, K_ηη, O_η of 7.2, D.21; the
# matrices 𝗌₁, 𝗌₂, 𝗌_a read as s1, s2, sa in a subscript).
INDEX_CHARS |= set("ση")
# Operators, constants and derivatives: never symbols of NOTATION.
IGNORE = {"π", "∂", "∇", "ħ"}
# Kronecker deltas: δ with two indices or momenta in the subscript.
KRONECKER = re.compile(r"^δ_.{2,}$")
# Bases whose subscript names an operator or state (𝒮_O, 𝒮_{n_e(q)}, 𝒟_{f_T}): any subscript is accepted when the base has a row.
ANY_SUB = {"𝒮", "𝒟", "ℱ"}  # ℱ_R of C.2 (lattice components, written ℱ_{R = ...})
# Cartesian components (k_x, p_z, k_∥, k_⊥) of the vectors that have a row: accepted on these bases only, so that
# named subscripts such as E_x (exchange energy) still need their own row.
COMPONENT_BASES = {"k", "p", "q", "r", "v", "u"}
COMPONENT_CHARS = set("xyzαβ∥⊥,")
# Cartesian components of tensors whose row has index subscripts (C_xxxx, C_xxyy of C_ijkl; σ_zz, σ_iz of σ_ij)
# of App. C.18. Only these bases, so that a named subscript such as E_x still needs its own row.
TENSOR_BASES = {"C", "σ"}
# S_ab, 𝔇_ab and the strain tensor X_αβ of 14.2: S_xx, S_yz, S^(2m)_zz, 𝔇_zz, X_xz
TENSOR_BASES |= {"S", "𝔇", "X"}
TENSOR_CHARS = set("xyz") | INDEX_CHARS
# Row labels in the subscripts of response matrices: S, R, R̃, 𝓜 and 𝔇 carry the
# names of the target rows they couple (S_{n_Mn_M}, S_{B𝐠}, S_{n𝒥}, R̃_{aZ}, R̃_{n_eZ}, R̃_{𝒯_eZ}, R̃_{j_TZ}, 𝓜³_{eκ}, 𝔇_{n_en_e}):
# the charge row Z (at 𝐪 + 𝐆), the nucleon row N, electrons e, the mass density n_M, the momentum density 𝐠, the spin current 𝒥,
# the kinetic-energy density 𝒯 and the transverse current j_T. Only these bases, so that a named subscript elsewhere needs a row.
RESPONSE_BASES = {"S", "R", "R\u0303", "𝓜", "𝔇"}
RESPONSE_CHARS = INDEX_CHARS | set("ZNeMgn𝒥𝒯T")
# The longitudinal current row j_L (S_{nj_L}, S_{j_Lj_L}, S_{j_Lj_Ti} of D.30).
RESPONSE_CHARS |= set("L")
# Literature notation quoted in the text (what a cited paper writes), which belongs in App. B.2, not in NOTATION.
# (α_D is also the key of the Dirac-matrix row 𝛂_D, β_D, γ_D; 1.4's quote of Essig et al.'s α_D then
# matches that row, and it stays literature notation by the NOTATION note.)
LITERATURE = {
    "α_D": "1.4 quotes Essig et al.'s dark fine-structure constant", "F_Yμν": "A.9 quotes the hypercharge field strength",
    "θ_W": "A.9 quotes the weak mixing angle", "M_0": "A.6 quotes Giustino's reference mass", "R_1": "2.2 quotes the literature's R₁",
    "n_χ": "A.8 quotes Catena et al.'s n_χ", "W": "A.7 quotes the literature's W for the loss function",
    ("appA/A-7.tex", "Π"): "A.7 quotes the literature's Π for the polarization",
    ("ch03/s3-2.tex", "f_[nk,mk′,GU]"): "3.2 quotes Essig et al.'s vertex f_[nk, mk′, G]",
    ("appC/C-18.tex", "μ"): "C.18 quotes the Lamé shear modulus μ = C_44 (and λ = C_12) of the elasticity literature",
    # Chap. 6 and App. D.16-D.18
    ("appD/D-17.tex", "W_e"): "D.17 quotes Giustino's W_e(ω) − W_e(0) of Ref. Eq. (140) (nonadiabatic subtraction)",
    # Chap. 8 and App. D.24-D.28
    ("ch08/s8-2.tex", "Π_φφ"): "8.2 quotes Mitridate et al.'s in-medium self-energy Π_φφ = Σ g*gR (Eqs. (20)-(22))",
    ("ch08/s8-4.tex", "Π_φA"): "8.4 quotes Mitridate et al.'s mixing self-energies Π_φA, Π_Aφ, Π_AA (Eqs. (20)-(22))",
    ("ch08/s8-4.tex", "Π_Aφ"): "8.4 quotes Mitridate et al.'s mixing self-energies Π_φA, Π_Aφ, Π_AA (Eqs. (20)-(22))",
    ("ch08/s8-4.tex", "Π_AA"): "8.4 quotes Mitridate et al.'s photon self-energy Π_AA (Eqs. (20)-(22))",
    ("appD/D-28.tex", "Π"): "D.28 quotes the orthogonal projector Π of Panati, Spohn and Teufel (Thm 2.1); the book writes 𝒫_ad",
    # Chap. 10 and App. D.29-D.30
    ("appD/D-30.tex", "W"): "D.30 relates the book's rows to Catena et al.'s crystal responses W̄₁-W̄₅ (2105.02233 Eqs. (10), (11), (D2))",
    ("ch10/s10-4.tex", "W"): "10.4 quotes Catena et al.'s crystal responses W̄₁-W̄₅ (2105.02233)",
    ("appD/D-29.tex", "V_cell"): "D.29 quotes Essig et al.'s cell volume V_cell in their Eq. (3.17) (the book writes Ω)",
    ("ch10/s10-9.tex", "T_χ"): "10.9 quotes Liang et al.'s boosted flux dΦ_χ/dT_χ with kinetic energies T_χ, T_e",
    ("ch10/s10-9.tex", "T_e"): "10.9 quotes Liang et al.'s boosted flux (kinetic energy T_e of the cosmic-ray electron)",
    ("ch10/s10-9.tex", "Φ_e"): "10.9 quotes Liang et al.'s cosmic-ray electron flux dΦ_e/dT_e",
    ("ch10/s10-9.tex", "Φ_χ"): "10.9 quotes Liang et al.'s boosted dark-matter flux dΦ_χ/dT_χ",
    ("ch10/s10-9.tex", "σ_χe"): "10.9 quotes Liang et al.'s dark-matter-electron cross-section in the boosted-flux formula",
    ("ch10/s10-9.tex", "σ_e"): "10.9 quotes Dror et al.'s name σ_e for the book's σ_F",
    ("ch10/s10-9.tex", "χ̄_2"): "10.9 quotes Baryakhtar et al.'s dipole operator χ̄₂σ^{μν}χ₁F_μν (Eqs. (2.1), (2.2))",
    # App. B: B.1 renders NOTATION rows; B.2 sets the literature's symbols in its first column
    ("appB/B-1.tex", "χ̄_2"): "B.1 row Λ_d quotes the dipole operator χ̄₂σ^{μν}χ₁F_μν of 10.9 (Baryakhtar et al.)",
    ("appB/B-2.tex", "λ_TF"): "B.2 literature column: the Thomas-Fermi length λ_TF for the book's 1/k_TF",
    ("appB/B-2.tex", "g_χ"): "B.2 literature column: mediator couplings g_χ, g_e for the book's y_χ, y_e",
    ("appB/B-2.tex", "Ω_D"): "B.2 literature column: the Wannier-spread split Ω_D + Ω_OD for the book's Ω̃_W",
    ("appB/B-2.tex", "Ω_OD"): "B.2 literature column: the Wannier-spread split Ω_D + Ω_OD for the book's Ω̃_W",
    ("appB/B-2.tex", "V_cell"): "B.2 literature column: the cell volume V_cell for the book's Ω",
    # App. F rows that quote a source's notation on purpose
    ("appF/F-rows.tex", "σ\u0304_n"): "F row 11.1b (Light-mediator single-phonon rate) quotes Griffin et al.'s σ̄_n at m_χv₀ in its Source column (the book writes σ_p)",
    ("appF/F-rows.tex", "V_cell"): "F row 11.2a quotes Knapen et al.'s C_F² ∝ 1/V_cell (the book writes Ω; as D.29, B.2)",
    ("appF/F-rows.tex", "f\u0304_d"): "F row 11.3a maps Campbell-Deem et al.'s f̄_d, m_d, D_d to the book's c_κ, M_κ, g_ph,κ/3",
    ("appF/F-rows.tex", "m_d"): "F row 11.3a maps Campbell-Deem et al.'s f̄_d, m_d, D_d to the book's c_κ, M_κ, g_ph,κ/3",
    ("appF/F-rows.tex", "D_d"): "F row 11.3a maps Campbell-Deem et al.'s f̄_d, m_d, D_d to the book's c_κ, M_κ, g_ph,κ/3",
    ("appF/F-rows.tex", "Δ_d"): "F row 11.4a identifies the book's σ_ω² with Campbell-Deem et al.'s Δ_d² at T = 0 (\"Δ_d² of the source\")",
    ("appF/F-rows.tex", "σ_NC"): "F row 11.4b quotes Dror et al.'s σ_NC in its Source column (\"their σ_NC\")",
    ("appF/F-rows.tex", "f\u0302_ℓm"): "F row 11.7a maps the sources' f̂_ℓm, T_ℓm (or W_ℓm), D^ij_d to the book's 2πℋ_ℓ, S_ℓm, D_κ",
    ("appF/F-rows.tex", "T_ℓm"): "F row 11.7a maps the sources' f̂_ℓm, T_ℓm (or W_ℓm), D^ij_d to the book's 2πℋ_ℓ, S_ℓm, D_κ",
    ("appF/F-rows.tex", "W_ℓm"): "F row 11.7a maps the sources' f̂_ℓm, T_ℓm (or W_ℓm), D^ij_d to the book's 2πℋ_ℓ, S_ℓm, D_κ",
    ("appF/F-rows.tex", "D_d^ij"): "F row 11.7a maps the sources' f̂_ℓm, T_ℓm (or W_ℓm), D^ij_d to the book's 2πℋ_ℓ, S_ℓm, D_κ",
    ("appF/F-rows.tex", "F_M"): "F row 12.4a quotes Berghaus et al.'s Eq. (4.8), F_{1,1} = F_M → A²",
    ("appF/F-rows.tex", "ε_S"): "F row 14.6a quotes Budker et al.'s level shift d_nε_SE* (the book writes Δε = d_nE*)",
    ("appF/F-rows.tex", "Z_r"): "F row 16.8c quotes the published form kZ_r = (κ/2πβ)Z‡e^{−βV_b} and k_inst of Lawrence et al.",
    ("appF/F-rows.tex", "k_inst"): "F row 16.8c quotes the published form kZ_r = (κ/2πβ)Z‡e^{−βV_b} and k_inst of Lawrence et al.",
    ("appF/F-rows.tex", "F_unc"): "F rows 18.2b, 18.2c quote Subashiev's published F_unc (the book writes F_ren)",
    ("appF/F-rows.tex", "Γ_md"): "F row 20.2b names Hernandez et al.'s Γ_md for the book's g_md (\"written with Γ_md ... in the source\")",
}

# Symbols local to one passage that need no NOTATION row, keyed as the script normalizes them.
LOCAL = {
    "ℐ": "1.2 local bracket ℐ(v_E)", "K_sp": "D.1 shorthand", "e_cut": "D.1 shorthand", "I_1": "D.1 shorthand",
    "I_2": "D.1 shorthand", "I_3": "D.1 shorthand", "y": "dummy (1.2, 1.3)", "s": "1.3 edge expansion / 2.3 spin / 1.1 entropy (rows)",
    "δ": "1.3 edge expansion (local)", "k": "1.5 background multiple (local)", "K": "1.5 binomial derivation (local)",
    "p": "1.5 binomial / 2.2 relative momentum", "c̃_f": "WE 2.1 rotating-frame amplitude (local)",
    "δE_g": "2.1 test-function scale (local)", "c̃_i": "2.1 rotating-frame amplitude (local)",
    "c_d": "D.12 orbital label d of v_ab,cd (local)", "ψ_d": "D.12 orbital label d of v_ab,cd (local)",
    "μ": "D.9 δμ, row 'φ_loc(t), δμ' (the tokenizer splits δ from μ)",
    "ϱ_k": "D.9 δϱ_k, row 'δϱ_k(t), δϱ^loc_k' (the tokenizer splits δ)",
    "ϱ_k^loc": "D.9 δϱ^loc_k, row 'δϱ_k(t), δϱ^loc_k' (the tokenizer splits δ)",
    "ϱ^loc": "D.9 δϱ^loc, row 'δϱ_k(t), δϱ^loc_k' (the tokenizer splits δ)",
    # Chap. 3, App. C.1-C.8, D.4-D.5: local to one file, keyed (file, symbol); checked before LITERATURE
    ("ch03/s3-1.tex", "r_Ne"): "3.1 electron positions r_1 ... r_{N_e} (index N_e)",
    ("ch03/s3-2.tex", "ε_G1/2"): "WE 3.3 band energy at k = G_1/2 (local)",
    ("ch03/s3-3.tex", "ε_hh,lh"): "3.3 heavy- and light-hole branches of eq:3.3-holes (band labels hh, lh)",
    ("ch03/s3-6.tex", "C"): "WE 3.10 eigenvector matrix C (local)", ("ch03/s3-6.tex", "D"): "3.6 phase matrix D(k) of the gauge argument (local)",
    ("ch03/s3-6.tex", "𝒮"): "3.6 spread functionals 𝒜[·], 𝒮[·] of eq:3.6-stationary (local)",
    ("ch03/s3-6.tex", "W"): "3.6 dW of eq:3.6-stationary (local)",
    ("appC/C-1.tex", "f_t"): "C.1 squeezed family f_t(x) = t f(tx) (local)", ("appC/C-2.tex", "g̃"): "C.2 Fourier transform of g (local)",
    ("appC/C-3.tex", "O_h"): "C.3 point-group label (Schoenflies)", ("appC/C-3.tex", "T_d"): "C.3 point-group label (Schoenflies)",
    ("appC/C-3.tex", "r_orb"): "C.3 orbital size in the multipole estimate (local)",
    ("appC/C-6.tex", "μ"): "C.6 Gaussian parameter μ of e^{−μx² + ηx} (bare, C.6 only; editor decision App. C; no keyed row)",
    ("appC/C-7.tex", "N\u0303"): "C.7 number operator of the transformed modes (local)", ("appC/C-7.tex", "P̃"): "C.7 pair operator of the transformed modes (local)",
    ("appC/C-7.tex", "Ψ̃"): "C.7 vector of transformed operators (local)", ("appC/C-7.tex", "W"): "C.7 bold generic matrix 𝐖 (row '𝐌, 𝐀, …')",
    # Chap. 5, App. D.13-D.15 and C.18
    ("ch05/s5-4.tex", "T_d"): "5.4 point-group label of the Si site (Schoenflies)",
    ("ch05/s5-6.tex", "μ"): "5.6 uses the Gaussian parameters μ, η of eq:C.6-gauss (bare, C.6 editor decision; no keyed row)",
    ("ch05/s5-7.tex", "X_d"): "5.7 Cartesian label d of X_a in the SCHA variation (row 'X_a, X̄_a'; labels a-d local)",
    ("ch05/s5-7.tex", "Φ_abcd"): "5.7 Φ^(4)_abcd with the Cartesian labels a-d of the SCHA variation (row Φ^(n))",
    ("ch05/s5-7.tex", "Φ_aux,cd"): "5.7 Φ^(2)_aux,cd, labels c, d of the SCHA variation (row Φ^(2)_aux)",
    ("ch05/s5-7.tex", "𝒞"): "5.7 'expanded in 𝒞', shorthand for 𝒞_κκ′(t) in one sentence",
    ("appD/D-13.tex", "k_e"): "D.13 solvable model: spring constant of the electron (k_e, K_N, ω_e, ω_BO, x, p, X, P local)",
    ("appD/D-13.tex", "ω_BO"): "D.13 solvable model: Born-Oppenheimer frequency (K_N/M)^{1/2} (local)",
    # Chap. 6 and App. D.16-D.18
    ("appD/D-17.tex", "Π"): "D.17 Π_ν with the labels dropped in one sentence (row Π_ν(Q, ω))",
    ("appD/D-17.tex", "ω̃"): "D.17 pole ω̃_Qν with the labels dropped (row 'ω̃_Qν, ω^ren_Qν')",
    # Chap. 7 and App. D.19-D.23
    ("ch07/s7-1.tex", "a_qr^†"): "7.1 a†_k at k = q_r, the first-zone part of q (rows a_kν and q_r)",
    ("ch07/s7-1.tex", "ω_qr^M"): "7.1 ω^M_k at k = q_r, the first-zone part of q (rows ω^M_k and q_r)",
    ("ch07/s7-1.tex", "s_e,x"): "7.1 Cartesian component of s_e(q) (row s_e(q))",
    ("ch07/s7-1.tex", "s_e,y"): "7.1 Cartesian component of s_e(q) (row s_e(q))",
    ("ch07/s7-3.tex", "E_q/2"): "7.3 E_k at k = q/2 (row 'ξ_k, E_k')",
    ("appD/D-23.tex", "U\u0303"): "D.23 Fourier transform Ũ(k − k′) of the donor potential U(r) (local)",
    ("ch07/s7-4.tex", "W"): "7.4 names e^{−2W} of eq:5.6-W, the Debye-Waller exponent (row W_κ(q), entry 11)",
    ("appD/D-22.tex", "W"): "D.22 unitary matrix W = M_1/m of the uniqueness argument (W, m local)",
    ("appD/D-23.tex", "μ"): "D.23 integration variable μ (a cosine) of ⟨1/r⟩ (local)",
    ("appD/D-23.tex", "k_zone"): "D.23 a momentum of the size of the zone, in the order estimate 1/(a*k_zone) (local)",
    # Chap. 8 and App. D.24-D.28
    ("appD/D-24.tex", "v_t"): "D.24 target velocity (𝐤 + 𝐤′)/2m in the reduction of v^⊥ (local)",
    ("appD/D-24.tex", "u\u0304"): "D.24 Dirac spinors u, ū of the bilinears (as the C.15 locals u(p, s))",
    ("appD/D-24.tex", "W"): "D.24 bold 𝐖 = Σ_j c^{(N_j)}𝐒_j, the nucleon-spin sum of the Wigner-Eckart step (W, w local)",
    ("appD/D-26.tex", "μ"): "D.26 reduced mass m_eM_κ/(m_e + M_κ) of the spring check (local; reduced masses are decorated elsewhere)",
    ("appD/D-28.tex", "μ"): "D.28 summation index over decay channels, as ν (local)",
    ("appD/D-24.tex", "Y^†"): "D.24 Y = Σ_b x_b Ṽ_b in the positivity proof of 𝔇 (local)",
    ("ch08/s8-2.tex", "k_F↑"): "WE 8.3 Fermi momentum of the polarized gas (k_F↑, v_F↑, E_F↑, S↑, S↓ local)",
    ("ch08/s8-2.tex", "v_F↑"): "WE 8.3 Fermi velocity of the polarized gas (local)",
    ("ch08/s8-2.tex", "E_F↑"): "WE 8.3 Fermi energy of the polarized gas (local)",
    ("ch08/s8-2.tex", "S_z"): "WE 8.3 spin projection S_z = +1/2 of every electron of the toy half-metal (local)",
    ("appD/D-25.tex", "Γ_Nφ→Nφ+1"): "D.25 emission rate between field occupations N_φ → N_φ + 1 (rows Γ_abs, N_φ)",
    ("appD/D-25.tex", "Γ_Nφ→Nφ-1"): "D.25 absorption rate between field occupations N_φ → N_φ − 1 (rows Γ_abs, N_φ)",
    ("appD/D-26.tex", "U_bg"): "D.26 potential of the uniform neutralizing background (local)",
    ("appD/D-26.tex", "Ω_y"): "D.26 solid angle of 𝐲 (local; Ω is the cell volume)",
    ("appD/D-26.tex", "ω_r"): "D.26 frequency of the relative mode of the spring check, ω_r² = K/μ (local)",
    ("appD/D-26.tex", "𝓃̃"): "D.26 Fourier transform of the spherical density in the j₂-kernel form (local)",
    ("appD/D-27.tex", "Z_g"): "D.27 atomic number of mass group g in the exactness proof (Z_g, 𝓃_g, c_e local)",
    ("appD/D-27.tex", "𝓃_g"): "D.27 total density of mass group g (local)",
    ("appD/D-27.tex", "c_e"): "D.27 c_s = c₁^{(s)} for s = e, the electron coefficient of the density coupling (row c_i^{(s)})",
    ("ch08/s8-4.tex", "e_κL^*"): "WE 8.6 polarization vector e_κν(Q) of the LO mode, ν = L (row e_κν)",
    ("ch08/s8-6.tex", "Ψ̃^nuc"): "8.6 widetilde over the product Ψ^nucΨ_j: the dressed (superadiabatic) state U_n(Ψ^nucΨ_j) (rows Ψ^nuc_i, U_n)",
    ("appD/D-28.tex", "Ψ̃^nuc"): "D.28 widetilde over the product Ψ^nucΨ_j: the dressed (superadiabatic) state (rows Ψ^nuc_i, U_n)",
    # Chap. 10 and App. D.29-D.30
    ("ch10/s10-7.tex", "D_3d"): "10.7 point-group label of sapphire (Schoenflies)",
    ("ch10/s10-9.tex", "u\u0304"): "10.9 Dirac spinors u, ū of the dark-matter current (as the C.15 locals u(p, s))",
    ("ch10/s10-8.tex", "μ"): "10.8 Lorentz index μ of ∂_μ, (p − p̄)^μ, γ^μ, ε^μ (an index, not the reduced mass)",
    ("ch10/s10-9.tex", "y_χν"): "10.9 y_χν̃ of row 'm_med, y_ee, y_χν̃' (the tokenizer drops the tilde inside a subscript)",
    ("ch10/s10-10.tex", "σ_ℛ"): "10.10 σ_{ln ℛ} of row 'σ_ln ℛ' (the tokenizer drops \\ln inside a subscript)",
    # Chap. 12 and App. D.33-D.34
    ("ch12/s12-1.tex", "W"): "12.1 names e^{−2W} of eq:5.6-W, the Debye-Waller exponent (row W_κ(q))",
    ("ch12/s12-4.tex", "W"): "12.4 names e^{−2W} of eq:5.6-W, the Debye-Waller exponent (row W_κ(q))",
    ("ch10/s10-8.tex", "ℳ\u0304"): "10.8 spin-averaged squared amplitude |ℳ̄|² of dark Compton scattering (row ℳ; bar = spin average)",
    # Chap. 14 and App. D.38
    ("appD/D-38.tex", "A_qr"): "D.38 A_k at k = q_r (rows A_k, q_r)",
    ("appD/D-38.tex", "B_qr"): "D.38 B_k at k = q_r (rows B_k, q_r)",
    ("appD/D-38.tex", "a_-qr1"): "D.38 magnon operator a_kν at k = −q_r, branch 1 (rows a_kν, q_r)",
    ("appD/D-38.tex", "a_-qr2"): "D.38 magnon operator at k = −q_r, branch 2 (rows a_kν, q_r)",
    ("appD/D-38.tex", "a_qr1"): "D.38 magnon operator at k = q_r, branch 1 (rows a_kν, q_r)",
    ("appD/D-38.tex", "a_qr2"): "D.38 magnon operator at k = q_r, branch 2 (rows a_kν, q_r)",
    ("appD/D-38.tex", "d_A,-qr"): "D.38 Holstein-Primakoff boson d_A at k = −q_r (rows d_A, d_B, q_r)",
    ("appD/D-38.tex", "d_Aqr"): "D.38 Holstein-Primakoff boson d_A at k = q_r (rows d_A, d_B, q_r)",
    ("appD/D-38.tex", "d_B,-qr"): "D.38 Holstein-Primakoff boson d_B at k = −q_r (rows d_A, d_B, q_r)",
    ("appD/D-38.tex", "d_Bqr"): "D.38 Holstein-Primakoff boson d_B at k = q_r (rows d_A, d_B, q_r)",
    ("appD/D-38.tex", "u_qr^M"): "D.38 u^M_k at k = q_r (rows u^M, q_r)",
    ("appD/D-38.tex", "v_qr^M"): "D.38 v^M_k at k = q_r (rows v^M, q_r)",
    ("appD/D-38.tex", "ω_qr^M"): "D.38 ω^M_k at k = q_r (rows ω^M_k, q_r)",
    ("appD/D-38.tex", "s_e,x"): "D.38 Cartesian component of s_e(q) (row s_e(q))",
    ("appD/D-38.tex", "s_e,y"): "D.38 Cartesian component of s_e(q) (row s_e(q))",
    ("ch14/s14-2.tex", "s_e,z"): "14.2 Cartesian component of s_e(q) (row s_e(q))",
    ("ch14/s14-3.tex", "s_e,x"): "14.3 Cartesian component of s_e(q) (row s_e(q))",
    ("ch14/s14-3.tex", "s_e,y"): "14.3 Cartesian component of s_e(q) (row s_e(q))",
    ("ch14/s14-5.tex", "s_e,x"): "14.5 Cartesian component of s_e(q) (row s_e(q))",
    ("ch14/s14-3.tex", "g_se,a^φ"): "14.3 g^φ_a for the rows a = s_e,a (row g^φ_a)",
    ("ch14/s14-5.tex", "σ_𝒥^P"): "14.5 σ^𝖯_a for the spin-current row a = 𝒥 (row σ^𝖳_a, σ^𝖯_a; the tokenizer drops the sans-serif)",
    ("ch14/s14-5.tex", "σ_𝒥^T"): "14.5 σ^𝖳_a for the spin-current row a = 𝒥 (row σ^𝖳_a, σ^𝖯_a; the tokenizer drops the sans-serif)",
    ("ch14/s14-5.tex", "E_Zee"): "14.5 ΔE_Zee, row '𝓃_mol, …, ΔE_Zee' (the tokenizer splits Δ)",
    ("ch14/s14-6.tex", "ω_eq"): "14.6 Δω_eq, row 'F_φ(ω), Δω_eq, Φ' (the tokenizer splits Δ)",
    ("ch14/s14-6.tex", "𝒦_tint"): "14.6 𝒦_t at t = t_int (rows 𝒦_t, t_int)",
    ("ch14/s14-4.tex", "W"): "14.4 names e^{−2W(k+G)}, the Debye-Waller exponent (row W_κ(q))",
    ("ch14/s14-5.tex", "μ^ph"): "14.5 𝛍^ph_𝐐ν with the labels dropped (row 𝛍^ph_𝐐ν)",
    # Chap. 17: material labels on existing symbols and the Δ split of Δω_eq
    ("ch17/s17-2.tex", "ω_eq"): "17.2 Δω_eq of 14.6 (the tokenizer splits Δ; row 'F_φ(ω), Δω_eq, Φ')",
    ("ch17/s17-summary.tex", "ω_eq"): "Ch17 Summary Δω_eq of 14.6 (the tokenizer splits Δ; row 'F_φ(ω), Δω_eq, Φ')",
    ("ch17/s17-2.tex", "L_Si"): "WE 17.2 loss function L of silicon (material label on row L)",
    ("ch17/s17-2.tex", "ρ_Si"): "WE 17.2 density of silicon (material label on row ρ_T)",
    ("ch17/s17-5.tex", "ℛ_C"): "WE 17.5 rate of diamond (material label on row ℛ; ℛ_A of eq:17.5-window)",
    ("ch17/s17-5.tex", "ℛ_Si"): "WE 17.5 rate of silicon (material label on row ℛ; ℛ_A of eq:17.5-window)",
    ("ch17/s17-5.tex", "W_C,Si"): "WE 17.5 window W_AB of diamond and silicon (row W_AB)",
    ("ch17/s17-1.tex", "W"): "17.1 names e^{−2W} of eq:5.6-W and 2W(q_max), the Debye-Waller exponent (row W_κ(q))",
    ("ch17/s17-3.tex", "W"): "17.3 names 2W, the Debye-Waller exponent (row W_κ(q))",
    # Chap. 18 and App. D.43-D.44: symbols local to D.43, D.44 and one passage,
    # type labels e, h on rows with a type subscript t, and the method name GW set in math
    ("ch18/s18-1.tex", "W"): "18.1 the method name GW set in math (row W^scr)",
    ("ch18/s18-4.tex", "W"): "18.4 the method name GW set in math (row W^scr)",
    ("ch18/s18-1.tex", "𝓚"): "18.1 the kernel 𝓚(nk → …) with the channel label dropped (row 𝓚_c)",
    ("ch18/s18-1.tex", "𝔊_3/2"): "WE 18.1 functional of the toy carrier at 3/2 (in units of E_g) (row 𝔊_x)",
    ("ch18/s18-1.tex", "𝔊_x′j"): "18.1 functional of a product state x′_j (row 𝔊_x)",
    ("appD/D-43.tex", "𝔊_x′j"): "D.43 functional of a product state x′_j (row 𝔊_x)",
    ("appD/D-43.tex", "m_x′j"): "D.43 mean vector of a product state x′_j (local, SEAM 18.1)",
    ("appD/D-43.tex", "M_x′j"): "D.43 second-moment matrix of a product state x′_j (local, SEAM 18.1)",
    ("appD/D-43.tex", "P_t"): "D.43 convolution weight ρ_t m_t (local, SEAM 18.1)",
    ("appD/D-43.tex", "P_t̄"): "D.43 convolution weight of the other type (local, SEAM 18.1)",
    ("appD/D-43.tex", "S_t"): "D.43 convolution weight ρ_t M_t (local, SEAM 18.1)",
    ("appD/D-43.tex", "S_t̄"): "D.43 convolution weight of the other type (local, SEAM 18.1)",
    ("appD/D-43.tex", "p_t"): "D.43 ionization probability of type t, p_ii of 18.3 per type (local, SEAM 18.1)",
    ("appD/D-43.tex", "d_ph"): "D.43 deposit of one phonon emission (local, SEAM 18.1)",
    ("appD/D-43.tex", "d_<"): "D.43 deposit of a terminal state (local, SEAM 18.1)",
    ("appD/D-44.tex", "K_xj"): "D.44 law K_x at x = x_j (row K_x)",
    ("appD/D-44.tex", "S_>"): "D.44 part of S(u) above the cut x_cut (local; row S(u))",
    ("appD/D-44.tex", "x_τ"): "D.44 energy of the line at the stopping time τ (local)",
    ("appD/D-44.tex", "𝔓_e"): "D.44 three-body density 𝔓_t of an electron (type label on row 𝔓_t)",
    ("ch18/s18-2.tex", "𝔓_e"): "18.2 three-body density 𝔓_t of an electron (type label on row 𝔓_t)",
    ("ch18/s18-3.tex", "v_e"): "18.3 subtree variance v_t of an electron (type label on row v_t)",
    ("ch18/s18-3.tex", "v_h"): "18.3 subtree variance v_t of a hole (type label on row v_t)",
    ("ch18/s18-3.tex", "P_no"): "WE 18.3 probability that a lone carrier escapes ionization (local)",
    # Chap. 19: Delta splits, a joint subscript, WE 19.6 locals.
    ("ch19/s19-5.tex", "E_zp"): "19.5 ΔE_zp (the tokenizer splits Δ; row 'E_phon(t), ΔE_zp(t), W_bias(t), N_ind')",
    ("ch19/s19-6.tex", "E_zp"): "19.6 ΔE_zp of 19.5 (the tokenizer splits Δ; row 'E_phon(t), ΔE_zp(t), …')",
    ("appD/D-45.tex", "E_zp"): "D.45 ΔE_zp of 19.5 (the tokenizer splits Δ; row 'E_phon(t), ΔE_zp(t), …')",
    ("ch19/s19-6.tex", "E_zp,ij"): "19.6 ΔE_zp,ij (the tokenizer splits Δ; row 'E^conf_i, ε^hop_ij, ΔE_zp,ij, …')",
    ("ch19/s19-2.tex", "F_LZ"): "19.2 ΔF_LZ (the tokenizer splits Δ; row 'h_LZ, ΔF_LZ, P_LZ, …')",
    ("ch19/s19-5.tex", "d_NR,ER"): "19.5 d_NR,ER, the joint subscript of d_NR and d_ER (row 't_win, E_miss, d_NR, d_ER')",
    ("ch19/s19-6.tex", "p_C"): "WE 19.6 occupation of the close pair C (local, entry 91(d); row p_i(t))",
    ("ch19/s19-6.tex", "Γ_C"): "WE 19.6 total decay rate of the close pair (local, entry 91(d))",
    ("ch19/s19-6.tex", "Γ_C0"): "WE 19.6 recombination rate of the close pair (local, entry 91(d))",
    ("ch19/s19-6.tex", "Γ_CB"): "WE 19.6 hop rate close pair → separated pair (local, entry 91(d))",
    ("ch19/s19-6.tex", "E_C^conf"): "WE 19.6 configurational energy of the close pair (local, entry 91(d); row E^conf_i)",
    # Chap. 22: the method name GW set in math
    ("ch22/s22-1.tex", "W"): "22.1 the method name GW set in math (row W^scr)",
    # App. B, C, E
    "σ_ℛ": "σ_{ln ℛ} of row 'σ_ln ℛ' (the tokenizer drops \\ln inside a subscript; 10.10, 11.9, 21.4, B.1)",
    ("appB/B-1.tex", "E_Zee"): "B.1 renders ΔE_Zee of row '𝓃_mol, …, ΔE_Zee' (the tokenizer splits Δ)",
    ("appB/B-1.tex", "E_zp"): "B.1 renders ΔE_zp of row 'E_phon(t), ΔE_zp(t), …' (the tokenizer splits Δ)",
    ("appB/B-1.tex", "E_zp,ij"): "B.1 renders ΔE_zp,ij of row 'E^conf_i, ε^hop_ij, ΔE_zp,ij, …' (the tokenizer splits Δ)",
    ("appB/B-1.tex", "F_LZ"): "B.1 renders ΔF_LZ of row 'h_LZ, ΔF_LZ, P_LZ, …' (the tokenizer splits Δ)",
    ("appB/B-1.tex", "ω_eq"): "B.1 renders Δω_eq of row 'F_φ(ω), Δω_eq, Φ' (the tokenizer splits Δ)",
    ("appB/B-1.tex", "F_ρσ"): "B.1 row 'A_μ, F_μν, Ã_μ; F̃^μν': the dual ½ε^μνρσF_ρσ (contracted indices of row F_μν)",
    ("appB/B-1.tex", "b_x"): "B.1 row 'b_𝐤±, b_𝐤x, b_𝐤y': (b_x ± ib_y)/√2 with 𝐤 dropped",
    ("appB/B-1.tex", "b_y"): "B.1 row 'b_𝐤±, b_𝐤x, b_𝐤y': (b_x ± ib_y)/√2 with 𝐤 dropped",
    ("appB/B-1.tex", "y_χν"): "B.1 renders y_χν̃ of row 'm_med, y_ee, y_χν̃' (the tokenizer drops the tilde inside a subscript)",
    ("appB/B-1.tex", "𝒦_tint"): "B.1 row 𝒦_t: 𝒦_t at t = t_int (rows 𝒦_t, t_int)",
    ("appC/C-11.tex", "𝔊_x′j"): "C.11 functional of a product state x′_j (row 𝔊_x)",
    ("appC/C-13.tex", "I_C"): "C.13 worked example: interval of material C (row 'I_a, ℓ_a, u_a'; labels A-D)",
    ("appC/C-13.tex", "I_D"): "C.13 worked example: interval of material D (row 'I_a, ℓ_a, u_a'; labels A-D)",
    ("appC/C-13.tex", "ℓ_C"): "C.13 worked example: lower end for material C (row 'I_a, ℓ_a, u_a'; labels A-D)",
    ("appC/C-13.tex", "ℓ_D"): "C.13 worked example: lower end for material D (row 'I_a, ℓ_a, u_a'; labels A-D)",
    ("appC/C-13.tex", "u_D"): "C.13 worked example: upper end for material D (row 'I_a, ℓ_a, u_a'; labels A-D)",
    ("appC/C-15.tex", "u\u0304"): "C.15 Dirac adjoint ū = u†γ⁰ of the local spinors u(p, s) (as the D.24 and 10.9 entries)",
    ("appC/C-17.tex", "σ_d"): "C.17 class of the six diagonal mirrors of 4̄3m (Schoenflies label)",
    ("appC/C-17.tex", "f_mxG"): "C.17 component f_𝐆 at the mirrored vector 𝗆_x𝐆 (row f_G)",
    ("appC/C-19.tex", "s_⊥,P\u0302"): "C.19 component of 𝐬_⊥ along the polarization P̂ (row 'f̂_mag, f̂_nuc, 𝐬_⊥')",
    ("appE/E-14.tex", "E\u0303"): "E.14 energy Ẽ_m of the zero-phonon final state with the label dropped (row 'Ẽ_m, z_qp(m)' of 8.6)",
    ("appE/E-19.tex", "𝒩_λ′^ch"): "E.19 𝒩^ch_λ at λ′ (row '… 𝒩^ch_λ')",
    ("appE/E-21.tex", "k_ι′"): "E.21 valley wavevector 𝐤_ι at ι′ (row 𝐤_ι)",
    # App. F labels and Δ splits on existing rows
    ("appF/F-rows.tex", "Y_ℓ0"): "F row 11.7a: Y_ℓm at m = 0 (row 'f̂_gal(s), Y_ℓm, …' of 11.7)",
    ("appF/F-rows.tex", "ω_eq"): "F row 14.6c: Δω_eq of 14.6 (the tokenizer splits Δ; row 'F_φ(ω), Δω_eq, Φ')",
    ("appF/F-rows.tex", "E_zp"): "F row 19.5a: ΔE_zp of 19.5 (the tokenizer splits Δ; row 'E_phon(t), ΔE_zp(t), …')",
}


def strip_braces(s):
    s = s.strip()
    while s.startswith("{") and s.endswith("}") and balanced(s[1:-1]):
        s = s[1:-1].strip()
    return s


def balanced(s):
    d = 0
    for ch in s:
        d += ch == "{"
        d -= ch == "}"
        if d < 0:
            return False
    return d == 0


def read_group(s, i):
    """Return (content, next index) for a TeX argument starting at s[i] (a {...} group, a command, or one char)."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        d, j = 0, i
        while j < len(s):
            d += s[j] == "{"
            d -= s[j] == "}"
            if d == 0:
                return s[i + 1:j], j + 1
            j += 1
        return s[i + 1:], len(s)
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1


def norm_script(t):
    """Normalize the TeX of a sub- or superscript to NOTATION's plain spelling."""
    t = re.sub(r"\\(mathrm|text|textrm|mathit|rm|mathsf|mathbf|operatorname|textup|bm|vect|boldsymbol)\s*", "", t)
    t = re.sub(r"\{\{([^{}]*)\}\}", r"{\1}", t)  # \bar{\mathrm{r}} -> \bar{r}
    t = re.sub(r"\\(mathcal|mathscr)\s*\{?([A-Za-z])\}?", lambda m: (SCRIPT if m.group(2).isupper() else SCRIPT_LOWER).get(m.group(2), m.group(2)), t)
    t = re.sub(r"\\op(?![A-Za-z])\s*\{?([A-Za-z])\}?", lambda m: m.group(1) + "\u0302", t)
    t = re.sub(r"\\(tilde|bar|hat)\s*\{?([A-Za-z])\}?", lambda m: m.group(2) + ACCENT[m.group(1)], t)

    def cmd(m):
        n = m.group(1)
        if n in GREEK:
            return GREEK[n]
        if n in SYMS:
            return SYMS[n]
        if n in MACROS:
            return MACROS[n]
        return ""
    t = re.sub(r"\\([A-Za-z]+)", cmd, t)
    t = re.sub(r"\\[,;:! ]", "", t)
    t = t.replace("{", "").replace("}", "").replace(" ", "").replace("~", "").replace("'", "′").replace("_", "")
    return "".join(FOLD.get(c, c) for c in t)


def key(base, sub="", sup=""):
    base = unicodedata.normalize("NFD", base)
    k = base
    if sub:
        k += "_" + sub
    if sup:
        k += "^" + sup
    return k


# ---------------------------------------------------------------- NOTATION keys
SUBDIG = str.maketrans("₀₁₂₃₄₅₆₇₈₉ₙ", "0123456789n")
SUPDIG = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
BOLD = {}
for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    BOLD[chr(0x1D400 + i)] = c
for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
    BOLD[chr(0x1D41A + i)] = c
BOLD["𝛔"] = "σ"
# bold Greek (𝛂_D, 𝛕_κ, 𝛜_kj, 𝛈): read as the plain letter, as the tex tokenizer drops \boldsymbol
for i, c in enumerate("αβγδεζηθικλμνξοπρςστυφχψω"):
    BOLD[chr(0x1D6C2 + i)] = c


def split_top(s, seps=",;"):
    """Split at top-level separators followed by a space ('H_Hub,0' and 'v_χ,max' stay whole)."""
    out, d, cur = [], 0, ""
    s = s + " "
    for i, ch in enumerate(s[:-1]):
        if ch in "([{⟨":
            d += 1
        elif ch in ")]}⟩":
            d -= 1
        if ch in seps and d == 0 and s[i + 1] == " ":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


def parse_unicode_symbol(s):
    """'v_E^ref' -> key; returns None for structures that are not symbols."""
    s = s.replace("\\|", "|").strip()
    if s.startswith("⟨") and not s.startswith("⟨p"):
        return None  # ⟨σv⟩, ⟨F_DM²⟩, ⟨⟨·⟩⟩: matched in the tex as whole expressions, never as their letters
    s = s.strip("|⟨⟩").strip()
    s = "".join(BOLD.get(c, c) for c in s)
    s = s.translate(SUBDIG)
    s = re.sub(r"\[[^\[\]]*\]$", "", s).strip()  # drop a functional argument (E_H[𝓃], K_s[𝓃])
    s = re.sub(r"\((?:[^()]|\([^()]*\))*\)$", "", s).strip()  # drop the argument
    s = re.sub(r"^d(?=[ΩℛΓσ])", "", s)  # dΩ_q, dℛ/dω
    s = re.split(r"/(?![^{]*\})", s)[0]  # a slash inside braces is part of the name (p_{1/2}, d_{5/2})
    s = s.split(" ")[0]
    if not s:
        return None
    s = unicodedata.normalize("NFD", s)
    m = re.match(r"([^\W\d_]|[ħℓ∂∇])([\u0300-\u036f]*)(\*?)(.*)$", s)
    if not m:
        return None
    base = m.group(1) + m.group(2)
    rest = m.group(4)
    sup = "*" if m.group(3) else ""
    sub = ""
    # digit subscripts written directly (q0 from q₀), ², ′
    mm = re.match(r"(\d)(.*)", rest)
    if mm and not rest.startswith("_"):
        sub, rest = mm.group(1), mm.group(2)
    while rest:
        if rest[0] == "_":
            g, rest = take(rest[1:])
            sub = (sub + "," + g) if sub else g
        elif rest[0] == "^":
            g, rest = take(rest[1:])
            sup = (sup + g) if sup else g
        elif rest[0] in "†′*":
            sup += rest[0]
            rest = rest[1:]
        elif rest[0] in "⁰²³⁻¹":  # powers and digit superscripts (R⁰_st), dropped as in the tex
            rest = rest[1:]
        else:
            break
    sub = "".join(FOLD.get(c, c) for c in sub.replace("{", "").replace("}", "").replace(" ", "").replace("_", "").translate(SUBDIG))
    sup = "".join(FOLD.get(c, c) for c in sup.replace("{", "").replace("}", "").replace(" ", "").translate(SUPDIG))
    base = "".join(FOLD.get(c, c) for c in base)
    return key(base, sub, name_sup(sup))


def take(s):
    if s.startswith("{"):
        d = 0
        for j, ch in enumerate(s):
            d += ch == "{"
            d -= ch == "}"
            if d == 0:
                return s[1:j], s[j + 1:]
        return s[1:], ""
    m = re.match(r"([^_^\s;()]*?)(?=[_^]|$|[\s;()])", s)
    g = m.group(1) if m else s
    return g, s[len(g):]


def split_semicolons(s):
    """Split at ';' outside braces only: S_{κ;GG′}^{ad} keeps its subscript whole."""
    out, d, cur = [], 0, ""
    for ch in s:
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
        if ch == ";" and d == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def notation_keys():
    keys = {}
    for ln in NOTATION.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("| ") or ln.startswith("| Symbol") or ln.startswith("|---"):
            continue
        cells = re.split(r"(?<!\\)\|", ln.strip().strip("|"))
        sym = cells[0].strip()
        sym = re.sub(r"\s*\((subscripts?|atomic|target states?)[^)]*\)", "", sym)
        for item in split_top(sym):
            for part in split_semicolons(item):
                k = parse_unicode_symbol(part)
                if k:
                    keys.setdefault(k, ln[:60])
    return keys


# ---------------------------------------------------------------- tex math extraction
ENV = r"(?:equation|align|gather|multline|eqnarray|displaymath|math)\*?"


def math_segments(text):
    text = re.sub(r"(?<!\\)%.*", "", text)
    segs = []
    for m in re.finditer(r"\\begin\{(" + ENV + r")\}(.*?)\\end\{\1\}", text, re.S):
        segs.append(m.group(2))
    text = re.sub(r"\\begin\{(" + ENV + r")\}(.*?)\\end\{\1\}", " ", text, flags=re.S)
    for m in re.finditer(r"\\\[(.*?)\\\]|\\\((.*?)\\\)|(?<!\\)\$\$(.*?)\$\$|(?<!\\)\$(.*?)(?<!\\)\$", text, re.S):
        segs.append(next(g for g in m.groups() if g is not None))
    return segs


def clean_math(s):
    s = re.sub(r"\\(label|cref|Cref|eqref|ref|cite|tag)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(text|textrm|textit|textbf|mbox|intertext|shortintertext)\s*\{(?:[^{}]|\{[^{}]*\})*\}", " ", s)
    s = re.sub(r"\\(SI|qty)\{[^}]*\}\{[^}]*\}|\\(si|unit|num)\{[^}]*\}", " ", s)
    s = re.sub(r"\\operatorname\*?\{[^}]*\}", " ", s)
    s = re.sub(r"\\langle\s*\\sigma\s*(?:\\,)?\s*v\s*\\rangle", " ", s)  # the row ⟨σv⟩
    s = re.sub(r"\\begin\{[a-z*]+\}(\{[^}]*\})?|\\end\{[a-z*]+\}", " ", s)
    return s


def tokens(s):
    """Yield (key, raw) for each symbol in a math string."""
    s = clean_math(s)
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        base = None
        start = i
        if ch == "\\":
            m = re.match(r"\\([A-Za-z]+)", s[i:])
            if not m:
                i += 2
                continue
            name = m.group(1)
            i += len(m.group(0))
            if name in GREEK:
                base = GREEK[name]
            elif name in MACROS:
                k = MACROS[name]
                base = k
            elif name == "nd":
                base = "𝓃"
            elif name in ("mathcal", "mathscr", "mathsf", "mathfrak", "mathbf", "bm", "vect", "boldsymbol", "mathit"):
                g, i = read_group(s, i)
                g = strip_braces(g)
                gk = list(tokens(g))
                if not gk:
                    continue
                b = gk[0][0]
                letter = b[0]
                if name == "mathscr" and letter.isupper():
                    b = SCRIPT_BOLD.get(letter, letter) + b[1:]
                elif name in ("mathcal", "mathscr"):
                    b = (SCRIPT if letter.isupper() else SCRIPT_LOWER).get(letter, letter) + b[1:]
                elif name == "mathsf":
                    b = SANS.get(letter, letter) + b[1:]
                elif name == "mathfrak":
                    b = (FRAK if letter.isupper() else FRAK_LOWER).get(letter, letter) + b[1:]
                base = b
            elif name == "overline":  # an average over a group, not an accent on one letter
                g, i = read_group(s, i)
                for t in tokens(strip_braces(g)):
                    yield t
                continue
            elif name in ACCENT or name in ("vec", "ddot", "underline"):
                g, i = read_group(s, i)
                gk = list(tokens(strip_braces(g)))
                if not gk:
                    continue
                b = gk[0][0]
                acc = ACCENT.get(name, "")
                # accent goes on the base letter, before any sub/superscript
                mm = re.match(r"([^_^]+)(.*)", b)
                base = unicodedata.normalize("NFD", mm.group(1)) + acc + mm.group(2)
            elif name == "mathrm":
                g, i = read_group(s, i)  # units, upright labels, e: not a symbol
                continue
            else:
                continue
        elif ch.isalpha() and ch.isascii():
            base = ch
            i += 1
        else:
            i += 1
            continue
        base = "".join(FOLD.get(c, c) for c in base)
        sub, sup = "", ""
        # gather sub/superscripts
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i < n and s[i] in "_^":
                which = s[i]
                g, i = read_group(s, i + 1)
                g = norm_script(g)
                if which == "_":
                    sub = (sub + "," + g) if sub else g
                else:
                    sup += g
            elif i < n and s[i] == "'":
                sup += "′"
                i += 1
            else:
                break
        if "_" in base and not sub:  # macro already carries a subscript
            base, sub = base.split("_", 1)
        elif "_" in base:
            b, s0 = base.split("_", 1)
            base, sub = b, s0 + "," + sub
        yield key(base, sub, name_sup(sup)), s[start:i]


def name_sup(sup):
    """Keep a superscript only when it is part of a name (letters, *, †); drop powers and primes."""
    t = re.sub(r"[0-9−\-+/().′]", "", sup)
    return t


def candidates(k):
    out = [k]
    b0 = k.split("_")[0].split("^")[0]
    if "^" in k and "_" not in k:
        sp = k.split("^", 1)[1]
        if sp and all(c in INDEX_CHARS for c in sp):
            out.append(b0 + "_" + sp)  # raised Lorentz indices: F^μν -> F_μν
    if "_" in k:
        # a named subscript followed by index subscripts (φ_ext,G′, K_full,cvk^x, 𝓃_e,G): the named row
        bs, rest = k.split("_", 1)
        sb, _, sp = rest.partition("^")
        parts = sb.split(",")
        if len(parts) > 1 and all(c in INDEX_CHARS for c in ",".join(parts[1:])):
            out.append(bs + "_" + parts[0] + ("^" + sp if sp else ""))
            out.append(bs + "_" + parts[0])
    if "^" in k:
        out.append(k.split("^")[0])
        # superscript that is a dagger or star on top of a named sup: v_E^ref† -> v_E^ref
        b, sp = k.split("^", 1)
        sp2 = sp.replace("†", "").replace("*", "")
        if sp2 != sp:
            out.append(b + ("^" + sp2 if sp2 else ""))
    # an isotope label in a subscript (b_{^{210}Pb}) is spelled with superscript digits in NOTATION (b_²¹⁰Pb);
    # a hat stacked on an accented letter (the best fit of σ̄_e, D.47) is the hat on a letter that has a row
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    iso = re.sub(r"_\^(\d+)", lambda m: "_" + m.group(1).translate(sup), k)
    if iso != k:
        out.append(iso)
    if "\u0302" in k:
        out.append(k.replace("\u0302", ""))
    # the sans-serif R, f, g, t keep their serif reading as a fallback (𝖱_𝔬 of 16.4 read as R_o)
    for a, g in (("R", "𝖱"), ("f", "𝖿"), ("g", "𝗀"), ("t", "𝗍")):
        if k.startswith(g):
            out.append(a + k[len(g):])
    return out


def is_index_sub(sub):
    return sub != "" and all(c in INDEX_CHARS for c in unicodedata.normalize("NFD", sub))


def main(argv):
    show_bare = "--bare" in argv
    minc = 1
    if "--min" in argv:
        minc = int(argv[argv.index("--min") + 1])
    globs = ["ch01/*.tex", "ch02/*.tex", "appA/*.tex"]
    if "--files" in argv:
        j = argv.index("--files") + 1
        globs = []
        while j < len(argv) and not argv[j].startswith("--"):
            globs.append(argv[j])
            j += 1
    nk = notation_keys()
    bases_indexed = {k.split("_")[0] for k in nk if "_" in k and is_index_sub(k.split("_", 1)[1].split("^")[0])}
    bare_rows = {k for k in nk if "_" not in k and "^" not in k}
    found = defaultdict(lambda: defaultdict(int))
    for g in globs:
        for f in sorted(TEX.glob(g)):
            for seg in math_segments(f.read_text(encoding="utf-8")):
                for k, raw in tokens(seg):
                    found[k][f.relative_to(TEX).as_posix()] += 1
    gaps, local, bare = [], [], []
    for k in sorted(found):
        cands = candidates(k)
        if any(c in nk for c in cands):
            continue
        b = k.split("_")[0].split("^")[0]
        sub = k.split("_", 1)[1].split("^")[0] if "_" in k else ""
        if b in IGNORE or KRONECKER.match(k.split("^")[0]):
            continue
        if sub and is_index_sub(sub) and (b in bases_indexed or b in bare_rows):
            continue
        if sub and b in ANY_SUB and any(x.startswith(b + "_") for x in nk):
            continue
        if sub and b in COMPONENT_BASES and b in bare_rows and set(sub) <= COMPONENT_CHARS:
            continue
        if sub and b in TENSOR_BASES and b in bases_indexed and len(sub) >= 2 and set(sub) <= TENSOR_CHARS:
            continue
        if sub and b in RESPONSE_BASES and (b in bases_indexed or b in bare_rows) and set(sub) <= RESPONSE_CHARS:
            continue
        if len(unicodedata.normalize("NFD", b)) == 2 and unicodedata.normalize("NFD", b)[1] == "\u0302":
            # a hat on a letter that has a row: its unit vector (bold) or its operator
            stem = unicodedata.normalize("NFD", b)[0] + k[len(b):]
            if any(c in nk for c in candidates(stem)):
                continue
            # a unit vector's index or Cartesian components (Q̂_i, Q̂_x of C.18): the rules for the stem
            b0 = unicodedata.normalize("NFD", b)[0]
            if sub and "^" not in k and (b0 in bases_indexed or b0 in bare_rows) and (
                    is_index_sub(sub) or set(sub) <= COMPONENT_CHARS):
                continue
        files = dict(found[k])
        # literature notation quoted in one file only: split those uses off
        for f in list(files):
            why = next((LITERATURE[(f, c)] for c in cands if (f, c) in LITERATURE), None)
            if why:
                local.append((k, files.pop(f), f, "literature notation, App. B.2: " + why))
                continue
            why = next((LOCAL[(f, c)] for c in cands if (f, c) in LOCAL), None)
            if why:
                local.append((k, files.pop(f), f, why))
        if not files:
            continue
        tot = sum(files.values())
        where = ", ".join("%s:%d" % (f, c) for f, c in sorted(files.items()))
        loc = next((LOCAL[c] for c in cands if c in LOCAL), None)
        lit = next((LITERATURE[c] for c in cands if c in LITERATURE), None)
        if lit:
            local.append((k, tot, where, "literature notation, App. B.2: " + lit))
        elif loc:
            local.append((k, tot, where, loc))
        elif "_" not in k and "^" not in k and len(b) == 1 and b.isascii():
            bare.append((k, tot, where))
        elif tot >= minc:
            gaps.append((k, tot, where))
    print("NOTATION keys: %d; distinct symbols in the tex: %d" % (len(nk), len(found)))
    print("\nGAPS (decorated or Greek symbols with no NOTATION row): %d" % len(gaps))
    for k, tot, where in gaps:
        print("  %-22s %4d  %s" % (k, tot, where))
    print("\nLOCAL (declared local in the SEAM files, or literature notation quoted for App. B.2; no row needed): %d" % len(local))
    for k, tot, where, why in local:
        print("  %-22s %4d  %s  [%s]" % (k, tot, where, why))
    print("\nBARE Latin letters without a row (generic coordinates, dummies; check by grep): %d" % len(bare))
    if show_bare:
        for k, tot, where in bare:
            print("  %-22s %4d  %s" % (k, tot, where))
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
