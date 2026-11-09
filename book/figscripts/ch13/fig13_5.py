"""Fig. 13.5 (fig:13-transfer), the temperature-transfer numbers of Sect. 13.5 and Worked example 13.5 (we:13-TA-transfer).
Log: fig13_5.log (every number quoted in Sect. 13.5 about the transfer).

Physics (Sect. 13.5, eq:13.5-forward and eq:13.5-inverse). Between the indirect and the direct gap the measured absorption of
silicon is the phonon-assisted eps_2 at q -> 0 (Sect. 13.3, 13.5). Branch by branch,
    sigma_nu(w; T) = (n_nu(T) + 1) s_nu(w - E_g(T) - w_nu) + n_nu(T) s_nu(w - E_g(T) + w_nu),
with s_nu the emission spectrum of branch nu as a function of the pair energy above the gap, taken independent of T (the
assumption the text sizes). Inverse (book's derivation): with r = exp(-w_nu/T) and dE = E_g(T) - E_g(0) < 0,
    sigma_nu(w; 0) = (1 - r) sum_{k>=0} (-r)^k sigma_nu(w + dE + 2 k w_nu; T).
Model of the edge used for the figure (a labelled model, not a computation): the Hall-Bardeen-Blatt form eq:6.5-edge,
free pairs, parabolic bands, constant matrix elements, two branches:
  E_g(T) = 1.1692 eV - a T^2/(T + b), a = 4.9e-4 eV/K, b = 655 K (Alex, Finkbeiner and Weber 1996, Eq. (11) as used in
           Sect. 6.3): E_g(77 K) = 1.1652 eV, E_g(300 K) = 1.1230 eV.
  w_TA = 18.27 meV, w_TO = 57.73 meV (Macfarlane et al. 1958, theta = 212 K and 670 K; Sect. 6.5).
  branch weights C_TA : C_TO = 5.5 : 4.0 (Rajkanan, Singh and Shewchun 1979, as quoted by Stanford et al.,
           arXiv:2010.15844, text after Eq. (4)).
  one overall scale A, fitted to the measured 300 K absorption (Franta et al. 2017, refractiveindex.info Franta-300K.yml,
           book/sources/4.4/si_franta_300K.yml) by the geometric mean of data/model on 1.18 eV <= w <= 1.30 eV.
Temperature dependence of the branch strength (sizing only): Stanford et al. (arXiv:2010.15844, Eqs. (6), (7)) fit
  A_1(T) = c0 exp(-c1 T), c1 = 1.7e-3 /K, to measurements at 0.5, 5, 77 and 295 K with an effective gap of 1.134 eV.
Excitonic thresholds (Sect. 6.5): E_x^b = 14.7 meV below the free-pair ones.
Run: python fig13_5.py   (numpy, matplotlib; seconds)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch13")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "fig13_5.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


kB = 86.17e-6                     # eV/K (Sect. 2.5)
W = {"TA": 212 * kB, "TO": 670 * kB}
C = {"TA": 5.5, "TO": 4.0}
EXB = 14.7e-3
T_MK = 0.010


def Eg(T):
    return 1.1692 - 4.9e-4 * T**2 / (T + 655.0)


def nB(w, T):
    x = w / (kB * T)
    return 0.0 if x > 700 else 1.0 / np.expm1(x)


def s_branch(eps, nu):
    """Emission spectrum of branch nu (free pairs, HBB): C_nu * eps^2 for eps > 0, in units of the scale A."""
    e = np.maximum(np.asarray(eps, float), 0.0)
    return C[nu] * e**2


def sigma(w, T, nus=("TA", "TO")):
    """Forward map (eq:13.5-forward), summed over the branches in nus, units of A [cm^-1 eV^-2 * eV^2]."""
    tot = 0.0
    for nu in nus:
        n = nB(W[nu], T)
        tot = tot + (n + 1) * s_branch(w - Eg(T) - W[nu], nu) + n * s_branch(w - Eg(T) + W[nu], nu)
    return tot


def inverse(f, w, T, nu, K=60):
    """Inverse transfer (eq:13.5-inverse) of a branch spectrum f(w') measured at T, to T -> 0."""
    r = np.exp(-W[nu] / (kB * T))
    dE = Eg(T) - Eg(0.0)
    tot = 0.0
    for k in range(K):
        tot = tot + (-r) ** k * f(w + dE + 2 * k * W[nu])
    return (1 - r) * tot


# ---------------------------------------------------------------- inputs
out("E_g(0) = %.4f, E_g(77 K) = %.4f, E_g(300 K) = %.4f eV; dE_g(77) = %.2f meV, dE_g(300) = %.2f meV"
    % (Eg(0), Eg(77), Eg(300), (Eg(77) - Eg(0)) * 1e3, (Eg(300) - Eg(0)) * 1e3))
for T in (77.0, 300.0):
    for nu in W:
        n = nB(W[nu], T)
        out("T = %g K, %s: w = %.2f meV, n = %.4g, (n+1)/n = exp(w/T) = %.4g, r = exp(-w/T) = %.4g"
            % (T, nu, W[nu] * 1e3, n, (n + 1) / n, n / (n + 1)))
E0TA = Eg(0) + W["TA"]
out("cold free-pair TA emission threshold E_g(0) + w_TA = %.4f eV; excitonic %.4f eV; TO emission %.4f eV"
    % (E0TA, E0TA - EXB, Eg(0) + W["TO"]))

# ---------------------------------------------------------------- inverse transfer: check against the forward model
ws = np.linspace(1.15, 1.6, 901)
for T in (77.0, 300.0):
    worst = 0.0
    for nu in W:
        exact = s_branch(ws - Eg(0) - W[nu], nu)
        rec = inverse(lambda x, nu=nu: sigma(x, T, (nu,)), ws, T, nu)
        scale = exact.max()
        worst = max(worst, np.max(np.abs(rec - exact)) / scale)
    out("inverse transfer from %g K reproduces the T = 0 model to %.1e (max abs error / max value, 1.15-1.6 eV, 60 terms)"
        % (T, worst))

# ---------------------------------------------------------------- the 77 K overestimate (untransferred data)
out("\nUntransferred 77 K data against the millikelvin spectrum, x = w - (E_g(0) + w_TA):")
for xm in (5, 10, 15, 20, 25, 50, 100):
    w = E0TA + xm * 1e-3
    ta = sigma(w, 77.0, ("TA",)) / sigma(w, 1e-3, ("TA",))
    two = sigma(w, 77.0) / sigma(w, 1e-3)
    out("  x = %3d meV: TA branch alone x%.3f, both branches x%.3f" % (xm, ta, two))
# where the factor crosses 2
xx = np.linspace(1e-3, 0.06, 6000)
fac = np.array([sigma(E0TA + x, 77.0) / sigma(E0TA + x, 1e-3) for x in xx])
out("  factor > 2 for x < %.1f meV" % (xx[np.argmin(np.abs(fac - 2))] * 1e3))
fs = np.exp(-1.7e-3 * 77.0)   # branch-strength factor at 77 K (Stanford et al. Eqs. (6), (7))
for xm in (15, 20, 25, 50, 100):
    w = E0TA + xm * 1e-3
    out("  with the 77 K strength factor %.3f: x = %d meV -> x%.2f" % (fs, xm, fs * sigma(w, 77.0) / sigma(w, 1e-3)))
out("  with the strength factor, > 2 for x < %.1f meV" % (xx[np.argmin(np.abs(fs * fac - 2))] * 1e3))
for xm in (25, 50, 100):     # 300 K for comparison
    w = E0TA + xm * 1e-3
    out("  300 K untransferred at x = %d meV: x%.2f" % (xm, sigma(w, 300.0) / sigma(w, 1e-3)))

# ---------------------------------------------------------------- Worked example: TA branch at x = 50 meV, 77 K
out("\nWorked example (TA branch, 77 K -> 10 mK, x = 50 meV):")
T = 77.0; nu = "TA"; w = E0TA + 0.050
n = nB(W[nu], T); dE = Eg(T) - Eg(0)
em = w - Eg(T) - W[nu]; ab = w - Eg(T) + W[nu]
out("  emission argument w - E_g(77) - w_TA = %.2f meV, absorption argument w - E_g(77) + w_TA = %.2f meV" % (em * 1e3, ab * 1e3))
g = (em / 0.050) ** 2
out("  gap shift (%.2f/50)^2 = %.4f; times n+1 = %.4f -> %.4f; absorption replica n (ab/50)^2 = %.4f; total %.4f"
    % (em * 1e3, g, n + 1, (n + 1) * g, n * (ab / 0.050) ** 2, (n + 1) * g + n * (ab / 0.050) ** 2))
r = n / (n + 1)
terms = [(1 - r) * (-r) ** k * sigma(w + dE + 2 * k * W[nu], T, (nu,)) / s_branch(0.050, nu) for k in range(5)]
for k, t in enumerate(terms):
    out("  series term k = %d: argument w + dE + 2k w_TA = %.4f eV, contribution %+.5f (in units of the 10 mK value)"
        % (k, w + dE + 2 * k * W[nu], t))
out("  partial sums: %s" % ", ".join("%.5f" % s for s in np.cumsum(terms)))

# ---------------------------------------------------------------- ill-posedness and branch-weight sensitivity
out("\nWithout branch resolution: a triangular solve upward divides by the occupation of the highest-argument term,")
out("  n_TO(77 K) = %.3g -> error growth exp(w_TO/T) = %.0f per step of 2 w_TO; at 300 K exp(w_TO/T) = %.2f, exp(w_TA/T) = %.2f"
    % (nB(W["TO"], 77), 1 / np.exp(-W["TO"] / (kB * 77)), 1 / np.exp(-W["TO"] / (kB * 300)), 1 / np.exp(-W["TA"] / (kB * 300))))


def transfer_total(T, wTA_frac_scale, w):
    """Transfer the total model spectrum at T with branch fractions computed from weights (C_TA*s, C_TO) instead of the
    true 5.5:4.0, then sum the transferred branches (what one does with unresolved data and assumed weights)."""
    cTA = C["TA"] * wTA_frac_scale

    def frac(x, nu):
        nTA, nTO = nB(W["TA"], T), nB(W["TO"], T)
        pTA = cTA / C["TA"] * ((nTA + 1) * s_branch(x - Eg(T) - W["TA"], "TA") + nTA * s_branch(x - Eg(T) + W["TA"], "TA"))
        pTO = (nTO + 1) * s_branch(x - Eg(T) - W["TO"], "TO") + nTO * s_branch(x - Eg(T) + W["TO"], "TO")
        tot = pTA + pTO
        p = pTA if nu == "TA" else pTO
        return np.where(tot > 0, p / np.where(tot > 0, tot, 1), 0.0)

    res = 0.0
    for nu in W:
        res = res + inverse(lambda x, nu=nu: frac(x, nu) * sigma(x, T), w, T, nu)
    return res


for T in (77.0, 300.0):
    for xm in (15, 50):
        w = E0TA + xm * 1e-3
        ref = sigma(w, 1e-3)
        lo, hi = transfer_total(T, 0.75, w) / ref, transfer_total(T, 1.25, w) / ref
        out("  T = %g K, x = %d meV: TA weight -25%% / +25%% gives the 10 mK value x%.3f / x%.3f" % (T, xm, lo, hi))

for T in (77.0, 295.0):
    out("T-dependent branch strength (Stanford et al. Eqs. (6), (7)): A_1(%g K)/A_1(0) = exp(-1.7e-3 T) = %.3f"
        % (T, np.exp(-1.7e-3 * T)))

# ---------------------------------------------------------------- measured 300 K data and the scale
rows = []
for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
    p = line.split()
    if len(p) == 3:
        try:
            rows.append([float(x) for x in p])
        except ValueError:
            pass
lam, nr, kap = np.array(rows).T
wd = 1.239841984 / lam
alpha_d = 4 * np.pi * kap / (lam * 1e-4)       # cm^-1
o = np.argsort(wd)
wd, alpha_d, nr = wd[o], alpha_d[o], nr[o]
fit = (wd >= 1.18) & (wd <= 1.30)
A = np.exp(np.mean(np.log(alpha_d[fit] / sigma(wd[fit], 300.0))))
out("\nscale A fitted to Franta 300 K on 1.18-1.30 eV: A = %.1f cm^-1 eV^-2 (A C_TA = %.0f, A C_TO = %.0f)" % (A, A * 5.5, A * 4.0))
for w0 in (1.15, 1.20, 1.25, 1.30):
    i = np.argmin(abs(wd - w0))
    out("  w = %.3f eV: data %.3g, model %.3g cm^-1" % (wd[i], alpha_d[i], A * sigma(wd[i], 300.0)))
i = np.argmin(abs(wd - E0TA - 0.050))
out("  at the WE energy w = %.4f eV: data 300 K %.3g cm^-1, model 300 K %.3g, model 77 K %.3g, model 10 mK %.3g; n_r = %.3f"
    % (wd[i], alpha_d[i], A * sigma(wd[i], 300.0), A * sigma(wd[i], 77.0), A * sigma(wd[i], T_MK), nr[i]))

# transfer of the measured 300 K data to 10 mK with the model's branch fractions


def data_interp(x):
    return np.interp(x, wd, alpha_d, left=0.0, right=np.nan)


def frac_model(x, nu, T=300.0):
    n = nB(W[nu], T)
    p = (n + 1) * s_branch(x - Eg(T) - W[nu], nu) + n * s_branch(x - Eg(T) + W[nu], nu)
    tot = sigma(x, T)
    return np.where(tot > 0, p / np.where(tot > 0, tot, 1), 0.0)


wplot = np.linspace(1.05, 1.42, 741)
trans = sum(inverse(lambda x, nu=nu: frac_model(x, nu) * data_interp(x), wplot, 300.0, nu) for nu in W)
for w0 in (1.18, 1.19, 1.20, 1.2375, 1.30, 1.40):
    i = np.argmin(abs(wplot - w0))
    out("  transferred 300 K data at %.4f eV: %.3g cm^-1 (model 10 mK %.3g)" % (wplot[i], trans[i], A * sigma(wplot[i], T_MK)))
hi_ = (wplot >= 1.25)
rr = trans[hi_] / (A * sigma(wplot[hi_], T_MK))
out("  transferred data / cold model on 1.25-1.42 eV: %.3f to %.3f" % (rr.min(), rr.max()))
neg = wplot[trans < -0.05]
out("  transferred data negative (< -0.05 cm^-1) at %s eV" % (("%.3f-%.3f" % (neg.min(), neg.max())) if len(neg) else "none"))
below = (wplot < E0TA)
out("  transferred data below the cold free-pair edge: max %.3g cm^-1, at %.4f eV"
    % (trans[below].max(), wplot[below][np.argmax(trans[below])]))

# ---------------------------------------------------------------- figure
fig, ax = plt.subplots(figsize=(6.4, 4.0))
sq = lambda y: np.sqrt(np.maximum(y, 0.0))
sel = (wd > 1.05) & (wd < 1.42)
ax.plot(wd[sel][::3], sq(alpha_d[sel][::3]), "o", ms=2.2, color="k", mfc="none", mew=0.6, label="measured, 300 K")
ax.plot(wplot, sq(A * sigma(wplot, 300.0)), color="k", lw=1.1, label="branch model, 300 K")
ax.plot(wplot, sq(A * sigma(wplot, 77.0)), color="0.45", lw=1.0, ls="--", label="branch model, 77 K")
ax.plot(wplot, sq(A * sigma(wplot, T_MK)), color="C0", lw=1.4, label="branch model, 10 mK")
ax.plot(wplot[::8], sq(trans[::8]), "s", ms=2.4, color="C0", mfc="none", mew=0.6, label="300 K data transferred to 10 mK")
for xv, lab in ((Eg(300) - W["TO"], r"$E_\mathrm{g}-\omega_\mathrm{TO}$"), (Eg(300) - W["TA"], r"$E_\mathrm{g}-\omega_\mathrm{TA}$")):
    ax.axvline(xv, ymax=0.88, color="0.6", lw=0.5, ls=":")    # stops below its label
    ax.text(xv, 23.2, lab + "\n(300 K)", fontsize=6.5, ha="center", va="top", color="0.35")
ax.axvline(E0TA, color="C0", lw=0.6, ls=":")
ax.text(E0TA - 0.002, 13.0, r"$E_\mathrm{g}+\omega_\mathrm{TA}$ (10 mK)", fontsize=6.5, color="C0", rotation=90, va="bottom", ha="right")
ax.axvline(Eg(0) + W["TO"], color="C0", lw=0.6, ls=":")
ax.text(Eg(0) + W["TO"] - 0.002, 13.0, r"$E_\mathrm{g}+\omega_\mathrm{TO}$ (10 mK)", fontsize=6.5, color="C0", rotation=90, va="bottom", ha="right")
ax.set_xlim(1.05, 1.42)
ax.set_ylim(0, 24)
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_ylabel(r"$\sqrt{\alpha_\mathrm{abs}}$ (cm$^{-1/2}$)")
ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.86))
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig13_5.pdf"))
out("wrote", os.path.join(FIG, "fig13_5.pdf"))
