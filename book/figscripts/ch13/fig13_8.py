"""Fig. 13.8 (fig:13-replicas), the replica-edge numbers of Sect. 13.8 and Worked example 13.8 (we:13-darkphoton-edge).
Log: fig13_8.log (every number quoted in Sect. 13.8 that this script produces).

Physics (Sect. 13.8). In the Wannier-Mott limit the phonon-assisted edge of one branch nu with excitonic final states is the
free-pair edge A_nu x^2 (eq:6.5-edge, x = w - E_g - w_nu at T -> 0) with the relative-motion weight at zero separation
replaced by the bracket of eq:10.5-lines and convolved with the centre-of-mass density of states. In units of A_nu:
    X(x) = 32 sum_n (E_b)^{3/2} n^-3 (x + E_b/n^2)^{1/2}            (s lines, n >= 1, each for x + E_b/n^2 > 0)
         + (8/pi) int_0^x dE E^{1/2} (x - E)^{1/2} F(E),            F(E) = 2 pi xi / (1 - exp(-2 pi xi)), xi = (E_b/E)^{1/2}
with the free limit (no lines, F = 1) equal to x^2. The pair masses cancel in this ratio because mu_x M_eh = m_e m_h for
isotropic parabolic bands (derived in the text); only E_b enters.
Model inputs (all as in fig13_5.py, Sect. 13.5, a labelled model, not a computation):
  E_g(T) = 1.1692 eV - a T^2/(T + b), a = 4.9e-4 eV/K, b = 655 K (Alex, Finkbeiner and Weber 1996; Sect. 6.3).
  w_TA = 18.27 meV, w_TO = 57.73 meV (Macfarlane et al. 1958; Sect. 6.5); C_TA : C_TO = 5.5 : 4.0 (Rajkanan et al. 1979 via
  Stanford et al. arXiv:2010.15844 after Eq. (4)).
  E_x^b = 14.7 meV (Shaklee and Nahory 1970; Sect. 4.9), the same for the heavy- and light-hole copies (simplification).
  One overall scale per model, fitted to the measured 300 K absorption (Franta et al. 2017, refractiveindex.info
  Franta-300K.yml) by the geometric mean of data/model on 1.18 <= w <= 1.30 eV, exactly as in fig13_5.py.
Comparison at T -> 0: the fit of Stanford et al. to their 0.5 K data (arXiv:2010.15844 Eqs. (4)-(7)): alpha =
  sum_i C_i c0 (w - E_g1 - w_i)^2 with c0 = 325 eV^-2 cm^-1, E_g1(0) = 1.134 eV, C_TA = 5.5, C_TO = 4.0 (second indirect gap
  2.5 eV and the direct term negligible below 1.4 eV); their lowest photon energy is 1.21 eV (1028 nm).
Dark photon (WE 13.8): R = (rho_chi/rho_T) zeta^2 L (eq:10.7-dp), L = eps2/|eps|^2, eps2 = n_r alpha c/w, |eps|^2 ~ eps1^2
  (eps2 ~ 1e-4), eps1 and n_r from Franta 300 K; rho_chi = 0.3 GeV/cm^3, rho_T = 2.33 g/cm^3 (as WE 10.7).
Run: python fig13_8.py   (numpy, scipy, matplotlib; seconds)
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch13")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "fig13_8.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


kB = 86.17e-6
W = {"TA": 212 * kB, "TO": 670 * kB}
C = {"TA": 5.5, "TO": 4.0}
EB = 14.7e-3
NMAX = 400


def Eg(T):
    return 1.1692 - 4.9e-4 * T**2 / (T + 655.0)


def nB(w, T):
    if T <= 0:
        return 0.0
    x = w / (kB * T)
    return 0.0 if x > 700 else 1.0 / np.expm1(x)


def fermi(E):
    xi = np.sqrt(EB / E)
    return 2 * np.pi * xi / (-np.expm1(-2 * np.pi * xi))


def cont(x):
    """(8/pi) int_0^x E^1/2 (x-E)^1/2 F(E) dE, in units where the free edge is x^2."""
    if x <= 0:
        return 0.0
    # substitution E = x sin^2 t removes both square-root end points
    f = lambda t: (np.sin(t) * np.cos(t)) ** 2 * 2 * x**2 * fermi(x * np.sin(t) ** 2)
    v, _ = quad(f, 1e-12, np.pi / 2, limit=200)
    return 8 / np.pi * v


def lines(x, nmax=NMAX):
    n = np.arange(1, nmax + 1)
    arg = x + EB / n**2
    return 32 * EB**1.5 * np.sum(np.where(arg > 0, np.sqrt(np.maximum(arg, 0)), 0) / n**3)


def line1s(x):
    return 32 * EB**1.5 * np.sqrt(max(x + EB, 0))


def X(x):
    return lines(x) + cont(x)


def Xfree(x):
    return max(x, 0.0) ** 2


Xv = np.vectorize(X)
Xfv = np.vectorize(Xfree)


def alpha(w, T, model, nus=("TA", "TO")):
    f = Xv if model == "x" else Xfv
    tot = 0.0
    for nu in nus:
        n = nB(W[nu], T)
        tot = tot + C[nu] * ((n + 1) * f(w - Eg(T) - W[nu]) + (n * f(w - Eg(T) + W[nu]) if n > 0 else 0.0))
    return tot


# ------------------------------------------------------------- checks of the replica edge
out("checks: free limit (F = 1, no lines) of the convolution = x^2:",
    "%.6f" % (8 / np.pi * quad(lambda E: np.sqrt(E * (0.05 - E)), 0, 0.05)[0] / 0.05**2))
out("relative-motion weight per unit energy at the edge (units of the edge formula): lines 32 E_b^1.5 n^-3 / (2 E_b n^-3)"
    " = %.4f, continuum (8/pi) 2 pi E_b^1/2 = %.4f eV^1/2 (they match)" % (16 * np.sqrt(EB), 8 / np.pi * 2 * np.pi * np.sqrt(EB)))
# near threshold the continuum rises as (32/3) E_b^1/2 x^3/2
for xm in (0.1e-3, 1e-3):
    out("  continuum at x = %.1f meV: %.4e, (32/3) E_b^1/2 x^3/2 = %.4e" % (xm * 1e3, cont(xm), 32 / 3 * np.sqrt(EB) * xm**1.5))
# 1s line against free continuum at equal distance from own threshold: 32 (E_b/x)^{3/2}
for xm in (14.7e-3, 50e-3):
    out("  1s line / free edge at equal distance x = %.1f meV from their own thresholds: %.2f (32 (E_b/x)^1.5 = %.2f)"
        % (xm * 1e3, line1s(xm - EB) / xm**2, 32 * (EB / xm) ** 1.5))

# ------------------------------------------------------------- T -> 0 edge, ratio excitonic / free
E0 = Eg(0) + W["TA"]
out("\nT -> 0: free TA threshold E_g(0) + w_TA = %.4f eV; 1s TA replica %.4f eV; 2s %.4f eV; TO free %.4f, 1s TO %.4f eV"
    % (E0, E0 - EB, E0 - EB / 4, Eg(0) + W["TO"], Eg(0) + W["TO"] - EB))
for xm in (0, 5, 10, 12.5, 15, 25, 50, 100, 200):
    w = E0 + xm * 1e-3
    xe, xf = alpha(w, 0.0, "x"), alpha(w, 0.0, "f")
    out("  x = %5.1f meV above E_g(0)+w_TA: excitonic/free (same A) = %s; 1s-line share of the excitonic TA edge %.3f"
        % (xm, ("%.3f" % (xe / xf)) if xf > 0 else "inf", line1s(xm * 1e-3) / X(xm * 1e-3)))
for xm in (-14.7, -10, -5, -3.675):
    out("  below the free edge, x = %.2f meV: excitonic alpha / A = %.4e eV^2" % (xm, alpha(E0 + xm * 1e-3, 0.0, "x")))

# ------------------------------------------------------------- data and fitted scales (as fig13_5.py)
rows = []
for line in open(os.path.join(BOOK, "figscripts", "data", "4.4", "si_franta_300K.yml")):
    p = line.split()
    if len(p) == 3:
        try:
            rows.append([float(x) for x in p])
        except ValueError:
            pass
lam, nr, kap = np.array(rows).T
wd = 1.239841984 / lam
ad = 4 * np.pi * kap / (lam * 1e-4)
o = np.argsort(wd)
wd, ad, nr, kap = wd[o], ad[o], nr[o], kap[o]
fit = (wd >= 1.18) & (wd <= 1.30)
Af = np.exp(np.mean(np.log(ad[fit] / alpha(wd[fit], 300.0, "f"))))
Ax = np.exp(np.mean(np.log(ad[fit] / alpha(wd[fit], 300.0, "x"))))
out("\nscales fitted to Franta 300 K on 1.18-1.30 eV: free A = %.1f, excitonic A = %.1f cm^-1 eV^-2 (ratio %.3f)"
    % (Af, Ax, Ax / Af))
EG300 = Eg(300.0)
for dm in (17, 36, 55, 100, 200):
    w = EG300 + dm * 1e-3
    i = np.argmin(abs(wd - w))
    out("  300 K, w = E_g(300) + %3d meV = %.4f eV (data point %.4f): data/free %.2f, data/excitonic %.2f"
        % (dm, w, wd[i], ad[i] / (Af * alpha(wd[i], 300.0, "f")), ad[i] / (Ax * alpha(wd[i], 300.0, "x"))))
sel = (wd >= 1.18) & (wd <= 1.60)
rf = ad[sel] / (Af * alpha(wd[sel], 300.0, "f"))
rx = ad[sel] / (Ax * alpha(wd[sel], 300.0, "x"))
out("  1.18-1.60 eV: data/free %.2f to %.2f; data/excitonic %.2f to %.2f" % (rf.min(), rf.max(), rx.min(), rx.max()))
sel2 = (wd >= 1.30) & (wd <= 1.60)
out("  1.30-1.60 eV: data/free %.2f to %.2f; data/excitonic %.2f to %.2f"
    % ((ad[sel2] / (Af * alpha(wd[sel2], 300.0, "f"))).min(), (ad[sel2] / (Af * alpha(wd[sel2], 300.0, "f"))).max(),
       (ad[sel2] / (Ax * alpha(wd[sel2], 300.0, "x"))).min(), (ad[sel2] / (Ax * alpha(wd[sel2], 300.0, "x"))).max()))


def stanford(w):
    tot = 0.0
    for nu in W:
        tot = tot + C[nu] * 325.0 * np.maximum(w - 1.134 - W[nu], 0) ** 2
    return tot


out("\nT -> 0 against the 0.5 K fit of Stanford et al. (effective gap 1.134 eV):")
for w in (1.20, 1.21, 1.28, 1.31):
    out("  w = %.2f eV: Stanford fit %.3g, free model %.3g, excitonic model %.3g cm^-1"
        % (w, stanford(w), Af * alpha(w, 0.0, "f"), Ax * alpha(w, 0.0, "x")))

# ------------------------------------------------------------- Worked example: 1.2 eV dark photon
out("\nWorked example: dark photon at m = 1.200 eV")
w = 1.200
i0 = np.argmin(abs(wd - w))
n_r = np.interp(w, wd, nr)
k_e = np.interp(w, wd, kap)
eps1 = n_r**2 - k_e**2
hc = 1.973269804e-5       # eV cm
out("  Franta 300 K at 1.200 eV: n_r = %.4f, kappa = %.3e, eps1 = %.3f, alpha_300K = %.3g cm^-1"
    % (n_r, k_e, eps1, np.interp(w, wd, ad)))
pref = 0.3 / 2.33 * 1.519267e24 * 1e3 * 3.15576e7   # (rho_chi/rho_T)/hbar per kg-yr, GeV/g -> 1/(kg yr)
out("  rho_chi/rho_T/hbar = %.4g per kg-yr (WE 10.7: 1.52e33/0.2467 = %.4g)" % (pref, 1.52e33 / 0.2467))
cases = [("300 K data, untransferred", np.interp(w, wd, ad)),
         ("free-pair model at 77 K", Af * alpha(w, 77.0, "f")),
         ("free-pair model, T -> 0", Af * alpha(w, 0.0, "f")),
         ("excitonic model, T -> 0", Ax * alpha(w, 0.0, "x")),
         ("Stanford et al. 0.5 K fit", stanford(w))]
for lab, a in cases:
    eps2 = n_r * a * hc / w
    L = eps2 / eps1**2
    R = pref * L
    z3 = np.sqrt(3.0 / R)
    out("  %-28s alpha = %.3g cm^-1, eps2 = %.3e, L = %.3e, R = %.3g zeta^2 /kg/yr, zeta(3/kg-yr) = %.2e"
        % (lab, a, eps2, L, R, z3))
x_TA = w - Eg(0) - W["TA"]
x_TO = w - Eg(0) - W["TO"]
out("  free-pair TA distance x_TA = %.2f meV above E_g(0)+w_TA; TO x = %.2f meV; 1s TA replica %.2f meV above its threshold"
    % (x_TA * 1e3, x_TO * 1e3, (x_TA + EB) * 1e3))
xe = X(x_TA)
out("  excitonic TA edge in units of A: lines %.4e (1s %.4e), continuum %.4e, total %.4e; free x^2 = %.4e; ratio %.2f"
    % (lines(x_TA), line1s(x_TA), cont(x_TA), xe, x_TA**2, xe / x_TA**2))
out("  TO excitonic %.4e vs free %.4e (in units of A)" % (X(x_TO), max(x_TO, 0) ** 2))
a_st = stanford(w)
out("  Stanford fit TA part %.3f, TO part %.3f cm^-1" % (5.5 * 325 * (w - 1.134 - W["TA"]) ** 2, 4.0 * 325 * (w - 1.134 - W["TO"]) ** 2))

# ------------------------------------------------------------- figure
wg = np.linspace(1.150, 1.320, 1200)
fx = Ax * alpha(wg, 0.0, "x")
ff = Af * alpha(wg, 0.0, "f")
f1s = np.array([Ax * sum(C[nu] * line1s(ww - Eg(0) - W[nu]) * (ww - Eg(0) - W[nu] + EB > 0) for nu in W) for ww in wg])
fst = stanford(wg)
fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.1), gridspec_kw={"width_ratios": [1.25, 1.0]})
ax = axs[0]
sq = lambda y: np.sqrt(np.maximum(y, 0.0))
ax.plot(wg, sq(fx), color="C3", lw=1.4, label="excitonic (Wannier–Mott)")
ax.plot(wg, sq(f1s), color="C3", lw=0.8, ls=":", label=r"$1s$ replicas alone")
ax.plot(wg, sq(ff), color="C0", lw=1.2, ls="--", label="free pairs")
m = wg >= 1.205
ax.plot(wg[m], sq(fst[m]), color="0.45", lw=1.0, ls="-.", label="fit to 0.5 K data")
for xv, lab, c in ((E0 - EB, r"$1s$+TA", "C3"), (E0, r"TA", "C0"), (Eg(0) + W["TO"] - EB, r"$1s$+TO", "C3"),
                   (Eg(0) + W["TO"], "TO", "C0")):
    ax.axvline(xv, color=c, lw=0.5, ls=":")
    ax.text(xv + 0.0012, 4.55, lab, fontsize=7, color=c, rotation=90, va="top")
ax.set_xlim(1.165, 1.32)
ax.set_ylim(0, 4.6)
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_ylabel(r"$\sqrt{\alpha_\mathrm{abs}}$ at $T\to0$ (cm$^{-1/2}$)")
ax.legend(fontsize=7, frameon=False, loc="lower right")
ax.text(0.97, 0.97, "(a)", transform=ax.transAxes, fontsize=8, va="top", ha="right")
ax = axs[1]
s3 = (wd > 1.09) & (wd < 1.45)
ax.plot(wd[s3], ad[s3] / (Af * alpha(wd[s3], 300.0, "f")), color="C0", lw=1.1, ls="--", label="data / free pairs")
ax.plot(wd[s3], ad[s3] / (Ax * alpha(wd[s3], 300.0, "x")), color="C3", lw=1.3, label="data / excitonic")
ax.axhline(1, color="0.6", lw=0.4, zorder=0)
ax.axvspan(1.18, 1.30, color="0.9", lw=0)
ax.axvline(EG300, color="0.6", lw=0.5, ls=":")
ax.text(EG300 - 0.002, 3.85, r"$E_\mathrm{g}$ (300 K)", fontsize=7, rotation=90, va="top", ha="right", color="0.35")
ax.set_xlim(1.09, 1.45)
ax.set_ylim(0, 4)
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_ylabel(r"measured / model at 300 K")
ax.legend(fontsize=7, frameon=False, loc="upper center", handlelength=2.6)
ax.text(0.97, 0.97, "(b)", transform=ax.transAxes, fontsize=8, va="top", ha="right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig13_8.pdf"))
out("wrote", os.path.join(FIG, "fig13_8.pdf"))
