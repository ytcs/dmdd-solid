"""Fig. 9.3 (fig:9-axes) and Table 9.3 (tab:9-limitchecks) of Sect. 9.4: the Limit Checks of Part II (Chaps. 10-17) and
the formulas of Appendix F without a Limit Check, placed on the truncation label of Sect. 8.5 by the axis of their
leading correction.

Inputs (read, never edited):
  tex/ch10..ch17/s*.tex   every \\begin{limitbox}[Title][lim:N.Mx]  (the boxes that exist)
  tex/appF/F-rows.tex     the rows of Appendix F (tab:F-rows), split at \\midrule
Classification (this script, CLASS below): for each Limit Check, the axis on which its comparison result lies one
step from the formula, i.e. the axis k of the step T -> T_k^+ of Sect. 8.8, read from the box caption (what the
"fuller result" adds) and the Leading-correction column of its F row. Where the comparison is not a step along one
of the eight components of T (eq:8.5-label), the leading correction is an expansion in a parameter that the label
records only as a qualifier in words (Sect. 8.5), sorted into four groups:
  LW  long wavelength (q against a lattice, Fermi or cutoff momentum)
  KH  kinematics of the halo and of the signal (mass against an edge, line widths, coherence time)
  DM  dark-matter side and coupling (relativistic kinematics, operator content, order in the coupling)
  TM  target model and method (material parameters, defects, spin-wave order, numerical convergence)
Rows of App. F marked "(no box)" are placed the same way from their Leading-correction column (hollow chips).

Checks (asserted): every Part II limitbox label is classified exactly once and no classified label is missing from
the tex; every Part II F row is either a box row or a no-box row in NOBOX; the quoted strings in QUOTES occur in
the F rows or in the box text (so that the numbers Sect. 9.4 prints are the ones the home sections print).
Outputs: tex/figures/ch09/fig9_3.pdf, tex/ch09/tab9-3.tex, figscripts/ch09/fig9_3.log (all counts printed in 9.4).
Runtime < 2 s.
"""
import glob
import os
import re
from collections import Counter, OrderedDict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
TEX = os.path.join(BOOK, "tex")
LOG = open(os.path.join(HERE, "fig9_3.log"), "w")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


# ---------------------------------------------------------------- classification of every Part II Limit Check
# label: (axis, value of the formula -> comparison, controlling parameter in words for Table 9.3)
# axis in {nB, ng, nA, X, nT, K, M, nD} or a qualifier group {LW, KH, DM, TM}.
CLASS = OrderedDict([
    ("10.1a", ("X", r"IP $\to$ RPA + LF", r"momentum transfer $q/q_0$ at fixed $\omega$")),
    ("10.2a", ("K", r"clamped $\to$ one-phonon", r"energy over the top of the phonon band")),
    ("10.2b", ("K", r"clamped $\to$ one-phonon", r"momentum transfer $q$")),
    ("10.3a", ("TM", "", r"energy over the gap, $\omega/\Eg$")),  # led by the gap: electron gas -> crystal bands
    ("10.3b", ("LW", "", r"momentum over the plasmon cutoff")),
    ("10.4a", ("DM", "", r"current-row rate over density-row rate")),
    ("10.5a", ("X", r"BSE, one time ordering $\to$ both", r"momentum transfer $|\vect{q}|$")),
    ("10.7a", ("X", r"no medium $\to$ measured $\varepsilon$", r"boson mass $m_\phi$")),
    ("10.7b", ("TM", "", r"upper cutoff of the spectral sum")),
    ("10.8a", ("KH", "", r"line width over the kinetic energy of the pair")),
    ("10.8b", ("DM", "", r"boson mass over electron mass")),
    ("10.9a", ("X", r"IP $\to$ RPA + LF", r"mass splitting $\Delta_\chi$")),
    ("10.9b", ("DM", "", r"dark-matter speed $v$")),
    ("10.9c", ("DM", "", r"dark-matter mass over the binding energy")),
    ("10.9d", ("X", r"no medium $\to$ measured $\varepsilon$", r"splitting over the valence plasma frequency")),
    ("11.1a", ("LW", "", r"$q/q_{\mathrm{BZ}}$")),
    ("11.1b", ("KH", "", r"dark-matter mass over the acoustic edge")),
    ("11.1c", ("TM", "", r"elastic anisotropy (Zener ratio)")),
    ("11.2a", ("LW", "", r"momentum transfer $q$ in three directions")),
    ("11.2b", ("KH", "", r"dark-matter mass $\mchi$")),
    ("11.2c", ("TM", "", r"share of one polar branch")),
    ("11.2d", ("TM", "", r"misfit of the inputs to the Lyddane--Sachs--Teller relation")),
    ("11.3a", ("K", r"incoherent $\to$ coherent multiphonon", r"$q/q_{\mathrm{BZ}}$")),
    ("11.3b", ("nT", r"classical $\to$ quantum occupations", r"distance from a reciprocal-lattice vector")),
    ("11.4a", ("K", r"impulse $\to$ multiphonon", r"recoil parameter $x_R$")),
    ("11.4b", ("K", r"impulse $\to$ multiphonon", r"dark-matter mass $\mchi$")),
    ("11.5a", ("nA", r"$0 \to 2$", r"momentum in units of the zero-point momentum")),
    ("11.5b", ("nA", r"$0 \to$ all even orders", r"Lindemann ratio")),
    ("11.5c", ("TM", "", r"threshold in standard deviations")),  # skewness 1/xi of the moment problem
    ("11.6a", ("TM", "", r"boson mass $m_\phi$")),
    ("11.6b", ("TM", "", r"phonon frequency, at three mass defects")),
    ("11.7a", ("KH", "", r"momentum transfer $q$")),
    ("11.8a", ("TM", "", r"boson mass $m_\phi$ near the polar phonon")),
    ("11.8b", ("KH", "", r"quality factor of the mode over that of the halo field")),
    ("11.8c", ("TM", "", r"frequency over the lowest mode of the body")),
    ("12.2a", ("nD", r"$2 \to$ all orders", r"multipole parameter $\xi_D$")),
    ("12.2b", ("nD", r"$2 \to$ all orders", r"multipole parameter $\xi_D$")),
    ("12.3a", ("X", r"RPA $\to$ RPA + LF (diagonal)", r"momentum given to the electrons, over $q_{\mathrm{BZ}}$")),
    ("12.3b", ("M", r"sudden $\to$ moving nucleus", r"dark-matter mass (largest recoil energy)")),
    ("12.3c", ("KH", "", r"dark-matter mass $\mchi$")),
    ("12.3d", ("TM", "", r"valence band width over the gap")),
    ("12.4a", ("M", r"sudden $\to$ exact denominators", r"Doppler shift over the electronic energy")),
    ("12.4b", ("nB", r"$2 \to 4$", r"electronic energy against the phonon band")),  # 2<w^2>/w_e^2: n_B step (8.5)
    ("12.6a", ("X", r"atomic $\to$ crystal loss function", r"boson mass $m_\phi$")),
    ("13.5a", ("X", r"IP $\to$ BSE", r"photon energy above the gap")),
    ("13.7a", ("TM", "", r"supercell size")),
    ("14.1a", ("TM", "", r"inverse spin, $1/2|\vect{S}|$")),
    ("14.3a", ("TM", "", r"applied over demagnetizing field; anisotropy over exchange")),
    ("14.4a", ("TM", "", r"orbital shift of the ion's $g$ factor")),
    ("14.5a", ("TM", "", r"dark-matter mass; level spacing over temperature")),
    ("14.5b", ("TM", "", r"temperature over the ordering temperature")),
    ("14.6a", ("KH", "", r"time over the coherence time of the field")),
    ("14.6b", ("KH", "", r"record length over the coherence time")),
    ("14.6c", ("KH", "", r"record length over the coherence time")),
    ("15.1a", ("X", r"bare BCS bubble $\to$ conserving", r"energy over the gap, on the kinematic edge")),
    ("15.2a", ("X", r"bare BCS bubble $\to$ conserving", r"energy over the gap, on the kinematic edge")),
    ("15.4a", ("TM", "", r"energy over the gap")),
    ("16.1a", ("X", r"Dirac bands $\to$ with remote bands", r"background dielectric constant")),
    ("16.2a", ("LW", "", r"momentum along the channel over $k_{\mathrm{F}}$")),
    ("16.2b", ("TM", "", r"plasmon speed over the Fermi speed of the light carriers")),
    ("16.2c", ("LW", "", r"wave number times layer period")),
    ("16.3a", ("TM", "", r"kinetic energy of the ejected electron")),
    ("16.3b", ("TM", "", r"energy above the dot gap, in confinement energies")),
    ("16.4a", ("TM", "", r"dark-matter mass $\mchi$")),
    ("16.5a", ("TM", "", r"donor density")),
    ("16.6a", ("K", r"impulse $\to$ bound atom", r"largest recoil energy over the threshold")),
    ("16.7a", ("TM", "", r"temperature")),
    ("16.7b", ("TM", "", r"boson mass $m_\phi$")),
    ("16.7c", ("DM", "", r"medium potential over the dark-matter energy")),
    ("16.7d", ("TM", "", r"boson mass against the Ioffe--Regel frequency")),
    ("16.8a", ("TM", "", r"splitting over temperature; coupling to the electrons")),
    ("16.8b", ("TM", "", r"dimensionless ohmic coupling")),
    ("16.8c", ("TM", "", r"temperature over the tunneling crossover")),
    ("16.8d", ("TM", "", r"time after cooling")),
    ("17.5a", ("TM", "", r"upper limit of the $f$-sum integral")),
])

# Rows of App. F marked "(no box)" in Chaps. 10-17, keyed by a fragment of their first column:
# (section, axis, step)
NOBOX = OrderedDict([
    ("Phonon-assisted electron-recoil rate", ("13.3", "ng", r"$2 \to 4$")),
    ("Inverse temperature transfer", ("13.5", "TM", "")),
    ("Nonadiabatic correction to the zero-point", ("13.7", "TM", "")),
    ("Longitudinal and transverse spin weights", ("14.1", "TM", "")),
    ("First BCS correction to the screening", ("15.1", "X", r"first order $\to$ resummed")),
    ("Drude and Mermin loss functions", ("15.3", "TM", "")),
    ("Impurity-assisted (Mattis--Bardeen)", ("15.4", "TM", "")),
    ("Spin-current absorption", ("15.4", "TM", "")),
    ("Interband response of a semiconducting nanotube", ("16.3", "X", r"RPA $\to$ BSE")),
    ("depolarization factor", ("16.3", "TM", "")),
])

# Strings Sect. 9.4 quotes from the home sections, with the file that must contain them.
QUOTES = [
    ("appF/F-rows.tex", r"0.05 of the unscreened value at the kinematic edge ($0.55\,q_0$), 0.22 at $q_0$"),
    ("appF/F-rows.tex", r"$q$-integrated 0.47 at \SI{5}{eV}"),
    ("ch10/s10-2.tex", r"carries more than $10^4$ times the electronic rate"),
    ("appF/F-rows.tex", r"within \SI{10}{\percent} for $x_R \ge 2.3$ ($q \ge \SI{70}{keV}$)"),
    ("ch01/s1-3.tex", r"Gray: $E_R \ge 9\omega_0 = \SI{0.54}{eV}$"),
    ("appF/F-rows.tex", r"$2\langle\omega_{\mathrm{ph}}^2\rangle/\omega_e^2 = 2.9\times10^{-3}$ at the Si gap"),
]

AXES = ["nB", "ng", "nA", "X", "nT", "K", "M", "nD"]
GROUPS = ["LW", "KH", "DM", "TM"]
AXIS_TEX = {"nB": r"$n_B$", "ng": r"$n_g$", "nA": r"$n_A$", "X": r"$\mathcal{X}$", "nT": r"$n_T$",
            "K": r"$\mathcal{K}$", "M": r"$\mathfrak{M}$", "nD": r"$n_D$"}
AXIS_PARAM = {"nB": r"$\kappa_{\mathrm{BO}}$", "ng": r"$\theta_{\mathrm{ep}}$", "nA": r"$\eta_{\mathrm{anh}}$",
              "X": "none", "nT": r"$T/\omega_{\mathbf{Q}\nu}$", "K": r"$x_R,\,2W$", "M": r"$\Delta E\,\tau_{\mathrm{acc}}$",
              "nD": r"$\xi_D$"}
GROUP_NAME = {"LW": "long\nwave-\nlength", "KH": "kine-\nmatics,\nhalo", "DM": "dark-\nmatter\nside",
              "TM": "target model and method"}
GROUP_TEX = {"LW": "long wavelength", "KH": "kinematics and halo", "DM": "dark-matter side and coupling",
             "TM": "target model and method"}


def natkey(s):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]


# ---------------------------------------------------------------- read the boxes that exist
boxes = OrderedDict()
NUM = {}  # printed number of each box: chapter.(order of appearance in the chapter), as the limitbox counter prints it
for ch in range(10, 18):
    chap = open(os.path.join(TEX, f"ch{ch}", f"ch{ch}.tex")).read()
    i = 0
    for inp in re.findall(r"^\\input\{([^}]*)\}", chap, re.M):
        t = open(os.path.join(TEX, inp + ".tex")).read()
        for m in re.finditer(r"\\begin\{limitbox\}\[(.*?)\]\[lim:([^\]]*)\]", t):
            i += 1
            boxes[m.group(2)] = m.group(1)
            NUM[m.group(2)] = f"{ch}.{i}"
AUX = "/tmp/claude-0/build-ch09rev/main.aux"  # optional cross-check against a build of the book
if os.path.exists(AUX):
    aux = open(AUX).read()
    for k, n in NUM.items():
        m = re.search(r"\\newlabel\{lim:" + re.escape(k) + r"\}\{\{([^}]*)\}", aux)
        assert m and m.group(1) == n, (k, n, m and m.group(1))
    log("Printed box numbers checked against", AUX)
unlabelled = []
for f in glob.glob(os.path.join(TEX, "ch1[0-7]", "s*.tex")):
    for line in open(f):
        if r"\begin{limitbox}" in line and "][lim:" not in line:
            unlabelled.append((f, line.strip()))
assert not unlabelled, unlabelled
missing = [k for k in boxes if k not in CLASS]
extra = [k for k in CLASS if k not in boxes]
assert not missing and not extra, (missing, extra)
log("Part II Limit Checks (Chaps. 10-17) found in the tex:", len(boxes))
per_ch = Counter(k.split(".")[0] for k in boxes)
log("  per chapter:", ", ".join(f"Ch{c}: {per_ch[c]}" for c in sorted(per_ch, key=int)))

# ---------------------------------------------------------------- read App. F
ft = open(os.path.join(TEX, "appF", "F-rows.tex")).read()
body = ft.split("\\endfoot", 1)[1].split("\\end{longtable}")[0]
rows = [r.strip() for r in body.split("\\midrule") if r.strip()]


def section_of(row):
    m = re.findall(r"\\cref\{sec:(\d+)\.(\d+)\}\s*\\\\\s*$", row.strip())
    return (int(m[-1][0]), int(m[-1][1])) if m else None


part2 = [r for r in rows if section_of(r) and 10 <= section_of(r)[0] <= 17]
nobox_rows = [r for r in part2 if "(no box)" in r]
log("App. F rows, all chapters:", len(rows))
log("App. F rows with home in Chaps. 10-17:", len(part2))
log("  of which marked (no box):", len(nobox_rows))
log("  with an unsized leading correction (\\Fsize{unsized}):", sum("\\Fsize{unsized}" in r for r in part2))
log("  boxed rows (Part II rows minus no-box rows):", len(part2) - len(nobox_rows))
boxed_rows = [r for r in part2 if "(no box)" not in r]
unnamed = [r.split("&")[0][:60] for r in boxed_rows if "lim:" not in r.split("&")[0]]
assert not unnamed, unnamed       # every boxed Part II row names its Limit Check in column 1
named = set(re.findall(r"lim:(\d+\.\d+[a-z])", " ".join(r.split("&")[0] for r in boxed_rows)))
assert named == set(boxes), (named ^ set(boxes))
log("  boxed rows naming their Limit Check in column 1:", len(boxed_rows) - len(unnamed),
    "; distinct Limit Checks named:", len(named))
for r in nobox_rows:
    hits = [k for k in NOBOX if k in r]
    assert len(hits) == 1, (r[:80], hits)
assert len(NOBOX) == len(nobox_rows)
log("Limit Checks outside Part II (Chaps. 1-8, 18-21), for reference:",
    sum(len(re.findall(r"\\begin\{limitbox\}", open(f).read()))
        for f in glob.glob(os.path.join(TEX, "ch0[1-8]", "*.tex")) + glob.glob(os.path.join(TEX, "ch1[89]", "*.tex"))
        + glob.glob(os.path.join(TEX, "ch2[0-2]", "*.tex"))))
log("  of which in Part I (Chaps. 1-8):",
    sum(len(re.findall(r"\\begin\{limitbox\}", open(f).read())) for f in glob.glob(os.path.join(TEX, "ch0[1-8]", "*.tex"))))

for fn, s in QUOTES:
    assert s in open(os.path.join(TEX, fn)).read(), (fn, s)
log("Quoted strings found in their home files:", len(QUOTES))

# ---------------------------------------------------------------- counts by axis
cnt = Counter(v[0] for v in CLASS.values())
log("Limit Checks by the axis of the leading correction:")
for a in AXES:
    log(f"  {a:3s}: {cnt[a]:2d}  ", " ".join(k for k, v in CLASS.items() if v[0] == a))
log("  on a component of the label:", sum(cnt[a] for a in AXES))
for g in GROUPS:
    log(f"  {g:3s}: {cnt[g]:2d}  ", " ".join(k for k, v in CLASS.items() if v[0] == g))
log("  on a qualifier:", sum(cnt[g] for g in GROUPS))
for ch in range(10, 18):
    ks = [k for k in CLASS if k.startswith(f"{ch}.")]
    on = sum(CLASS[k][0] in AXES for k in ks)
    log(f"  Ch{ch}: {on} of {len(ks)} on a label component")
ncnt = Counter(v[1] for v in NOBOX.values())
log("No-box rows by axis:", dict(ncnt))

# ---------------------------------------------------------------- Table 9.3
with open(os.path.join(TEX, "ch09", "tab9-3.tex"), "w") as T:
    T.write("% Generated by figscripts/ch09/fig9_3.py; do not edit by hand.\n")
    T.write("{\\small\n\\setlength{\\tabcolsep}{4pt}\n")
    T.write("\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{0.11\\linewidth}"
            ">{\\raggedright\\arraybackslash}p{0.32\\linewidth}>{\\raggedright\\arraybackslash}p{0.27\\linewidth}"
            ">{\\raggedright\\arraybackslash}p{0.23\\linewidth}@{}}\n")
    cap = ("\\caption{The Limit Checks of \\crefrange{chap:10}{chap:17}, by chapter. Controlling parameter: the "
           "variable on the horizontal axis of the box. Leading correction: the component of the truncation label "
           "$\\mathfrak{T}$ of \\cref{eq:8.5-label} along which the comparison result lies one step from the "
           "formula, with the step; where the step is not along a component, the kind of qualifier it expands in. "
           "Formulas recovered as limits without a box are listed in \\cref{tab:F-rows}.}\\label{tab:9-limitchecks}\\\\\n")
    T.write(cap)
    head = ("\\toprule\nLimit Check & Formula & Controlling parameter & Leading correction \\\\\n\\midrule\n")
    T.write(head + "\\endfirsthead\n" + head + "\\endhead\n\\bottomrule\n\\endfoot\n")
    for ch in range(10, 18):
        T.write(f"\\multicolumn{{4}}{{@{{}}l}}{{\\emph{{\\Cref{{chap:{ch}}}}}}} \\\\\n")
        for k, (ax, step, par) in sorted(CLASS.items(), key=lambda kv: natkey(NUM[kv[0]])):
            if not k.startswith(f"{ch}."):
                continue
            title = boxes[k]
            lead = f"{AXIS_TEX[ax]}: {step}" if ax in AXES else GROUP_TEX[ax]
            T.write(f"\\ref{{lim:{k}}} & {title} & {par} & {lead} \\\\\n")
        if ch < 17:
            T.write("\\addlinespace\n")
    T.write("\\end{longtable}\n}\n")
log("Wrote tex/ch09/tab9-3.tex with", len(CLASS), "rows")

# ---------------------------------------------------------------- Fig. 9.3
PAL = {10: "#0072B2", 11: "#E69F00", 12: "#009E73", 13: "#CC79A7", 14: "#56B4E9", 15: "#D55E00",
       16: "#8C6D31", 17: "#555555"}
plt.rcParams.update({"font.size": 7, "mathtext.fontset": "cm"})
cols = AXES + ["LW", "KH", "DM", "TM", "TM2"]
W_COL, H_ROW = 1.0, 0.36
fig, ax = plt.subplots(figsize=(6.3, 4.9))
NROW = 20
ax.set_xlim(-0.05, len(cols) * W_COL + 0.05)
ax.set_ylim(-1.1, NROW * H_ROW + 1.6)
ax.axis("off")


def chip(x, y, text, ch, hollow=False):
    c = PAL[ch]
    text = text if hollow else NUM[text]          # hollow chips carry the bare home-section number
    ax.add_patch(FancyBboxPatch((x + 0.08, y - 0.13), W_COL - 0.16, 0.27,
                                boxstyle="round,pad=0.0,rounding_size=0.06",
                                fc="white" if hollow else c, ec=c, lw=0.9))
    ax.text(x + W_COL / 2, y, text, ha="center", va="center", fontsize=6.3,
            color=c if hollow else "white", weight="bold")


top = NROW * H_ROW
# headers
for i, c in enumerate(cols):
    x = i * W_COL
    if c in AXES:
        ax.text(x + W_COL / 2, top + 0.95, AXIS_TEX[c], ha="center", va="center", fontsize=9)
        ax.text(x + W_COL / 2, top + 0.55, AXIS_PARAM[c], ha="center", va="center", fontsize=6.5, color="0.3")
    elif c in ("LW", "KH", "DM"):
        ax.text(x + W_COL / 2, top + 0.72, GROUP_NAME[c], ha="center", va="center", fontsize=5.8,
                linespacing=1.0)
    elif c == "TM":
        ax.text(x + W_COL, top + 0.72, "target model\nand method", ha="center", va="center", fontsize=5.8, linespacing=1.0)
ax.plot([0.05, len(AXES) * W_COL - 0.05], [top + 1.35] * 2, color="0.3", lw=0.6)
ax.text(len(AXES) * W_COL / 2, top + 1.47, r"components of the truncation label $\mathfrak{T}$",
        ha="center", va="bottom", fontsize=7)
ax.plot([len(AXES) * W_COL + 0.05, len(cols) * W_COL - 0.05], [top + 1.35] * 2, color="0.3", lw=0.6)
ax.text((len(AXES) + len(cols)) * W_COL / 2, top + 1.47, "qualifiers recorded in words",
        ha="center", va="bottom", fontsize=7)
ax.axvline(len(AXES) * W_COL, ymin=0.02, ymax=0.9, color="0.6", lw=0.6, ls=":")

# label columns: chips grouped under the value at which the formula sits (its step is in Table 9.3)
TIER = {"10.1a": "IP", "10.9a": "IP", "13.5a": "IP", "16.3": "RPA", "10.3a": "RPA", "12.3a": "RPA", "16.1a": "RPA",
        "15.1a": "BCS bubble", "15.2a": "BCS bubble", "15.1": "BCS bubble", "10.5a": "BSE",
        "10.7a": "no medium", "10.9d": "no medium", "12.6a": "no medium",
        "10.2a": "clamped", "10.2b": "clamped", "11.3a": "multiphonon", "11.4a": "impulse", "11.4b": "impulse",
        "16.6a": "impulse", "11.5a": "0", "11.5b": "0", "11.5c": "all orders", "11.3b": "2", "13.3": "2",
        "12.3b": "sudden", "12.4a": "sudden", "12.4b": "2", "12.2a": "2", "12.2b": "2"}
TIER_ORDER = ["0", "2", "all orders", "no medium", "IP", "RPA", "BCS bubble", "BSE", "clamped", "multiphonon",
              "impulse", "sudden"]
for i, a in enumerate(AXES):
    x = i * W_COL
    y = top
    entries = [(k, int(k.split(".")[0]), False) for k, v in CLASS.items() if v[0] == a]
    entries += [(v[0], int(v[0].split(".")[0]), True) for v in NOBOX.values() if v[1] == a]
    if not entries:
        ax.text(x + W_COL / 2, y - 0.1, "none", ha="center", va="top", fontsize=6, color="0.45", style="italic")
        continue
    tiers = sorted(set(TIER[e[0]] for e in entries), key=TIER_ORDER.index)
    for tr in tiers:
        es = sorted([e for e in entries if TIER[e[0]] == tr], key=lambda e: (e[2], natkey(NUM.get(e[0], e[0]))))
        ax.text(x + W_COL / 2, y - 0.02, tr, ha="center", va="top", fontsize=5.6, color="0.25", style="italic")
        y -= 0.3
        for k, ch, hol in es:
            chip(x, y - 0.08, k, ch, hol)
            y -= H_ROW
        y -= 0.04
    assert y > -0.2, (a, y)

# qualifier columns
for g in GROUPS:
    es = [(k, int(k.split(".")[0]), False) for k, v in CLASS.items() if v[0] == g]
    es += [(v[0], int(v[0].split(".")[0]), True) for v in NOBOX.values() if v[1] == g]
    es.sort(key=lambda e: (e[2], natkey(NUM.get(e[0], e[0]))))
    i0 = cols.index(g)
    for j, (k, ch, hol) in enumerate(es):
        i = i0 + (j // NROW if g == "TM" else 0)
        r = j % NROW if g == "TM" else j
        chip(i * W_COL, top - 0.15 - r * H_ROW, k, ch, hol)

# legend, two rows
for j, ch in enumerate(range(10, 18)):
    xx = 0.2 + (j % 5) * 2.0
    yy = -0.55 - 0.32 * (j // 5)
    ax.add_patch(FancyBboxPatch((xx, yy - 0.1), 0.28, 0.2, boxstyle="round,pad=0,rounding_size=0.05",
                                fc=PAL[ch], ec=PAL[ch]))
    ax.text(xx + 0.36, yy, f"Chap. {ch}", va="center", fontsize=6.3)
xx, yy = 0.2 + 3 * 2.0, -0.87
ax.add_patch(FancyBboxPatch((xx, yy - 0.1), 0.28, 0.2, boxstyle="round,pad=0,rounding_size=0.05",
                            fc="white", ec="0.3"))
ax.text(xx + 0.36, yy, "formula of Appendix F without a Limit Check (home section)", va="center", fontsize=6.3)
out = os.path.join(TEX, "figures", "ch09", "fig9_3.pdf")
fig.savefig(out, bbox_inches="tight")
log("Wrote", os.path.relpath(out, BOOK))
LOG.close()
