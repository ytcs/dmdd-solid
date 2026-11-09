"""Limit Check 13.5a (lim:13.5a, Sect. 13.5): phonon-assisted absorption, the q -> 0 limit of the phonon-assisted loss
function, in the Hall-Bardeen-Blatt form, against the measured absorption of silicon. Output: tex/figures/ch13/limit13_5a.pdf,
log limit13_5a.log.

Literature formula (eq:6.5-edge; Hall, Bardeen and Blatt 1954; the edge of eq:6.5-eps2PA, Noffsinger et al. 1202.3454 Eq. (1)):
    alpha_abs = sum_nu A_nu [ n_nu (w - E_g + w_nu)^2 + (n_nu + 1)(w - E_g - w_nu)^2 ]   (each term for positive argument)
free pairs, parabolic bands, matrix elements constant across the pockets, two branches:
    w_TA = 18.27 meV, w_TO = 57.73 meV (Macfarlane et al. 1958; Sect. 6.5), A_TA : A_TO = 5.5 : 4.0 (Rajkanan, Singh and
    Shewchun 1979, as quoted in Stanford et al. arXiv:2010.15844 after Eq. (4)),
    E_g(300 K) = 1.1230 eV (Alex et al. 1996 fit, Sect. 6.3), T = 300 K,
    one overall scale fitted to the data on 1.18-1.30 eV (geometric mean of data/formula), as in fig13_5.py.
Fuller result: the measured absorption of float-zone silicon at 300 K (Franta et al., Appl. Surf. Sci. 421, 405 (2017),
    refractiveindex.info Franta-300K.yml; book/sources/4.4/si_franta_300K.yml), which at q -> 0 is the full phonon-assisted
    eps_2 (plus, above E_dir, the direct one) at the temperature of the measurement.
Shaded: the energy range, around the fitted window, where the formula is within 15 % of the data.
Markers: second indirect threshold 2.5 eV at T = 0 (Stanford et al. Eq. (5), fixed value), i.e.
    2.454 eV at 300 K with their Varshni parameters (beta = 7.021e-4 eV/K, gamma = 1108 K); direct gap E_dir = 3.4 eV (Sect. 3.3).
Run: python limit13_5a.py  (seconds)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch13")
LOG = open(os.path.join(HERE, "limit13_5a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


kB = 86.17e-6
T = 300.0
W = {"TA": 212 * kB, "TO": 670 * kB}
C = {"TA": 5.5, "TO": 4.0}
EG = 1.1692 - 4.9e-4 * T**2 / (T + 655.0)
EG2 = 2.5 - 7.021e-4 * T**2 / (T + 1108.0)
EDIR = 3.4


def hbb(w):
    tot = 0.0
    for nu in W:
        n = 1.0 / np.expm1(W[nu] / (kB * T))
        tot = tot + C[nu] * (n * np.maximum(w - EG + W[nu], 0) ** 2 + (n + 1) * np.maximum(w - EG - W[nu], 0) ** 2)
    return tot


rows = []
for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
    p = line.split()
    if len(p) == 3:
        try:
            rows.append([float(x) for x in p])
        except ValueError:
            pass
lam, nr, kap = np.array(rows).T
w = 1.239841984 / lam
al = 4 * np.pi * kap / (lam * 1e-4)
o = np.argsort(w)
w, al = w[o], al[o]
fit = (w >= 1.18) & (w <= 1.30)
A = np.exp(np.mean(np.log(al[fit] / hbb(w[fit]))))
out("E_g(300 K) = %.4f eV; second indirect threshold at 300 K %.3f eV; scale A = %.1f cm^-1 eV^-2" % (EG, EG2, A))

sel = (w > 1.05) & (w < 3.45)
ws, ds = w[sel], al[sel]
ratio = ds / np.maximum(A * hbb(ws), 1e-30)
ok = np.abs(ratio - 1) <= 0.15
# contiguous run of ok containing the fit window centre
i0 = np.argmin(abs(ws - 1.24))
lo = i0
while lo > 0 and ok[lo - 1]:
    lo -= 1
hi = i0
while hi < len(ws) - 1 and ok[hi + 1]:
    hi += 1
out("formula within 15 %% of the data for %.3f <= w <= %.3f eV, i.e. %.0f to %.0f meV above E_g(300 K)"
    % (ws[lo], ws[hi], (ws[lo] - EG) * 1e3, (ws[hi] - EG) * 1e3))
for w0 in (1.10, 1.12, 1.14, 1.16, 1.18, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 2.0, 2.3, 2.5, 2.8, 3.0, 3.3):
    i = np.argmin(abs(ws - w0))
    out("  w = %.3f eV (w - E_g = %+.3f): data %.3g, formula %.3g cm^-1, data/formula %.3f"
        % (ws[i], ws[i] - EG, ds[i], A * hbb(ws[i]), ratio[i]))

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.axvspan(ws[lo], ws[hi], color="0.88", lw=0, zorder=0)
ax.semilogy(ws[::4], ds[::4], "o", ms=2.0, color="k", mfc="none", mew=0.5, label="measured absorption, 300 K")
wl = np.linspace(1.05, 3.45, 2000)
ax.semilogy(wl, A * hbb(wl), color="C3", lw=1.3, label="Hall–Bardeen–Blatt edge, two branches")
for xv, lab in ((EG2, "second indirect\nthreshold"), (EDIR, r"$E_\mathrm{dir}$")):
    ax.axvline(xv, color="0.55", lw=0.5, ls=":")
    ax.text(xv - 0.025, 2e-1, lab, fontsize=6.5, color="0.3", rotation=90, va="bottom", ha="right")
ax.set_xlim(1.05, 3.45)
ax.set_ylim(1e-1, 2e6)
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_ylabel(r"$\alpha_\mathrm{abs}$ (cm$^{-1}$)")
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit13_5a.pdf"))
out("wrote", os.path.join(FIG, "limit13_5a.pdf"))
