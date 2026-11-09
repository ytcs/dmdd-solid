"""Fig. 6.4 (fig:6-gapT) and the numbers of Sect. 6.3 and Worked example 6.3 (we:6-zpr).

Measured gap: E_g(T) = E_g(0) - a T^2 / (T + b), E_g(0) = 1.1692 eV, a = (4.9 +- 0.2)e-4 eV/K, b = 655 +- 40 K: the fit of
  Alex, Finkbeiner and Weber, J. Appl. Phys. 79, 6943 (1996) to photoluminescence of crystalline Si up to 1000 K, in the form
  of Ramanathan and Kurinsky, PRD 102, 063026 (2020), arXiv:2004.10709, Eq. (11) (the book's adopted silicon gap, Sect. 1.3).
  The band is the envelope of the four corners (a +- 0.2e-4, b -+ 40 K).
Computed zero-point renormalization (ZPR) of the indirect gap of Si: -56.2 meV (non-adiabatic AHC, LDA) and -64.3 meV
  (adiabatic AHC): Ponce et al., J. Chem. Phys. 143, 102813 (2015), arXiv:1504.05992, Table VI (App. E.8, we:E-zpr).
  Measured ZPR -62 / -64 meV: same table (from Cardona, Solid State Commun. 133, 3 (2005)).
Einstein energy: omega_Ein = <omega^-1>^-1 over the per-atom PBE phonon density of states of Sect. 5.2
  (figscripts/ch05/fig5_2_data.npz, column 'dos', cm^-1), the choice that makes the zero-point <u^2> of the Einstein
  crystal equal to that of the computed spectrum (we:5-u2 quotes 30.4 meV).
Model (eq:6.3-einstein): E_g(T) = E_g(0) + ZPR [coth(omega_Ein / 2T) - 1], anchored at the measured E_g(0).
  Comparison curve: shift proportional to <u^2>(T) of the full computed spectrum, E_g(0) + ZPR [<u^2>(T)/<u^2>(0) - 1].
Lifetime estimate (Sect. 6.3, 'Phonon-limited lifetimes'): spontaneous emission (T = 0) of acoustic phonons by an electron
  in a spherical parabolic valley of mass m* = (m_l m_t^2)^(1/3), m_l = 0.916, m_t = 0.191 m_e (Hensel et al. 1965; Sect. 3.3),
  with the deformation-potential vertex |g|^2 = Xi_nu^2 Q / (2 M_cell c_nu) (eq:6.2-D), Xi_nu^2 the average over directions
  of (Xi_d + Xi_u cos^2 th)^2 (LA) and (Xi_u sin th cos th)^2 (TA, one branch), Xi_d = 1.01, Xi_u = 8.84 eV (Li et al. 2021,
  DFPT; Sect. 6.2), c_LA = 8.43, c_TA = 5.84 km/s (measured [100] speeds, Sect. 5.2). Closed form (eq:6.3-cherenkov)
  Gamma = Omega Xi^2 m* Q_max^3 / (12 pi M_cell c k), Q_max = 2(k - m* c), checked here by direct quadrature.
Run: python fig6_4.py   (numpy, scipy, matplotlib; a few seconds)
"""
import os
import numpy as np
from scipy.integrate import dblquad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_4.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

KB = 8.617333262e-5          # eV/K
ME = 0.51099895e6            # eV
U = 931.49410242e6           # eV/u
HBARC = 1973.269804          # eV A
HBAR = 6.582119569e-16       # eV s
CM = 1.23984198e-4           # eV per cm^-1
C_KMS = 299792.458

# ---------------- measured gap ----------------
EG0, A_V, B_V = 1.1692, 4.9e-4, 655.0


def eg_meas(T, a=A_V, b=B_V):
    return EG0 - a * T ** 2 / (T + b)


# ---------------- Einstein energy from the computed DOS ----------------
d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
w = d["dos"][:, 0] * CM
g = d["dos"][:, 1] / CM
g *= 6 / np.trapezoid(g, w)            # 6 modes per cell
ga = g / 2                             # per atom, normalized to 3
m = w > 0
wE = 3 / np.trapezoid(ga[m] / w[m], w[m])
M_SI = 28.0855 * U


def u2(T):
    f = np.ones_like(w[m]) if T == 0 else 1 / np.tanh(w[m] / (2 * KB * T))
    return np.trapezoid(ga[m] * f / (2 * M_SI * w[m]), w[m])


print("omega_Ein = <omega^-1>^-1 = %.2f meV = %.0f K" % (wE * 1e3, wE / KB))

ZPR_NA, ZPR_AD = -56.2e-3, -64.3e-3


def coth(x):
    return 1 / np.tanh(x)


def einstein(T, zpr, wE=wE):
    T = np.maximum(T, 1e-6)
    return EG0 + zpr * (coth(wE / (2 * KB * T)) - 1)


# ---------------- Worked example numbers ----------------
print("\nWE 4.14 ratio Re Sigma(300 K)/Re Sigma(0) = %.4f ; 2n_B+1 at 60 meV, 300 K = %.4f"
      % (11.09 / 9.14, 2 / (np.exp(0.060 / (300 * KB)) - 1) + 1))
T300 = 300.0
x = wE / (2 * KB * T300)
print("300 K: omega_Ein/2T = %.4f, coth = %.4f, 2 n_B = %.4f" % (x, coth(x), coth(x) - 1))
for zpr in (ZPR_NA, ZPR_AD):
    print("  ZPR %.1f meV: model E_g(300)-E_g(0) = %.1f meV" % (zpr * 1e3, zpr * (coth(x) - 1) * 1e3))
print("measured E_g(300) = %.4f eV, shift %.1f meV" % (eg_meas(300), (eg_meas(300) - EG0) * 1e3))
r = u2(300) / u2(0)
print("<u^2>(300)/<u^2>(0) = %.3f (sqrt-ratio %.4f/%.4f A); <u^2>-scaled shift = %.1f meV"
      % (r, np.sqrt(u2(300) * HBARC ** 2 / 3), np.sqrt(u2(0) * HBARC ** 2 / 3), ZPR_NA * (r - 1) * 1e3))
slope = 2 * abs(ZPR_NA) / wE * KB
print("high-T slope 2|ZPR|/omega_Ein = %.3f meV/K (adiabatic ZPR: %.3f)" % (slope * 1e3, 2 * abs(ZPR_AD) / wE * KB * 1e3))
print("measured local slope dE/dT at 300, 500 K: %.3f, %.3f meV/K"
      % ((eg_meas(300.5) - eg_meas(299.5)) * 1e3, (eg_meas(500.5) - eg_meas(499.5)) * 1e3))
for TT in (100, 200, 300, 400, 500, 600):
    print("  T = %d K: model - measured = %.1f meV" % (TT, (einstein(TT, ZPR_NA) - eg_meas(TT)) * 1e3))
print("inverse: ZPR from 300 K shift = %.1f meV; from slope at 500 K = %.1f meV"
      % ((eg_meas(300) - EG0) / (coth(x) - 1) * 1e3, -(wE / KB / 2) * abs(eg_meas(500.5) - eg_meas(499.5)) * 1e3))
print("clamped gap E_g(0) - ZPR = %.4f eV (non-adiabatic), %.4f (adiabatic)" % (EG0 - ZPR_NA, EG0 - ZPR_AD))
# asymptote of the model: E_cl + 2 ZPR T / omega_Ein, through the clamped gap at T = 0; residual at 300 K
Ecl = EG0 - ZPR_NA
print("model vs its linear asymptote at 300 K: %.2f meV" % ((einstein(300, ZPR_NA) - (Ecl + 2 * ZPR_NA * KB * 300 / wE)) * 1e3))
print("  coth expansion check: ZPR*omega_Ein/(6T) = %.2f meV" % (ZPR_NA * wE / (6 * KB * 300) * 1e3))
# isotope: ZPR ~ M^-1/2
M28, M30 = 28.0855, 29.97377
print("isotope 30Si vs natural: Delta E_g = %.2f meV; -2M dE/dM check = %.1f meV"
      % (ZPR_NA * ((M28 / M30) ** 0.5 - 1) * 1e3, ZPR_NA * 1e3))
# detector temperatures
for T in (0.01, 1.0, 10.0):
    print("T = %5.2f K: Einstein thermal factor 2 n_B(omega_Ein) = %.2e" % (T, 2 / np.expm1(wE / (KB * T)) if wE / (KB * T) < 700 else 0.0))
print("T = 1 K: omega_Ein/T = %.0f" % (wE / KB / 1.0))

# ---------------- Froehlich (GaAs, numbers of Sect. 6.2) ----------------
print("\nGaAs: alpha_F omega_L = %.2f meV" % (0.072 * 36.35))

# ---------------- Cherenkov emission estimate (Si electrons) ----------------
A_SI = 5.431
OMEGA = A_SI ** 3 / 4 / HBARC ** 3       # eV^-3
M_CELL = 2 * M_SI
mstar = (0.916 * 0.191 ** 2) ** (1 / 3)
MS = mstar * ME
XD, XU = 1.01, 8.84
xi2_LA = XD ** 2 + 2 * XD * XU / 3 + XU ** 2 / 5
xi2_TA = XU ** 2 * (1 / 3 - 1 / 5)
cLA, cTA = 8.43 / C_KMS, 5.84 / C_KMS
print("\nm* = %.4f m_e; Xi_LA,rms = %.3f eV; Xi_TA,rms = %.3f eV" % (mstar, np.sqrt(xi2_LA), np.sqrt(xi2_TA)))
for c, lab in ((cLA, "LA"), (cTA, "TA")):
    print("  threshold %s: m* c^2/2 = %.4f meV, k_th = m* c = %.3e eV" % (lab, 0.5 * MS * c ** 2 * 1e3, MS * c))


def gamma_closed(E, xi2, c):
    k = np.sqrt(2 * MS * E)
    if k <= MS * c:
        return 0.0
    qmax = 2 * (k - MS * c)
    return OMEGA * xi2 * MS * qmax ** 3 / (12 * np.pi * M_CELL * c * k)


def gamma_quad(E, xi2, c):
    """(2 pi) Omega int d^3Q/(2pi)^3 |g|^2 delta(eps_k - eps_{k+Q} - cQ), delta in cos(theta) done analytically
    only through a narrow Lorentzian of width eta, integrated numerically in (Q, cos theta)."""
    k = np.sqrt(2 * MS * E)
    eta = 1e-3 * E

    def f(ct, Q):
        arg = -(2 * k * Q * ct + Q ** 2) / (2 * MS) - c * Q
        lor = eta / np.pi / (arg ** 2 + eta ** 2)
        return 2 * np.pi * OMEGA / (2 * np.pi) ** 3 * 2 * np.pi * Q ** 2 * xi2 * Q / (2 * M_CELL * c) * lor
    val, _ = dblquad(f, 0, 2.2 * k, -1, 1, epsabs=0, epsrel=1e-6)
    return val


E = 0.010
gl, gt = gamma_closed(E, xi2_LA, cLA), gamma_closed(E, xi2_TA, cTA)
print("E = 10 meV: Gamma_LA = %.2f ueV, Gamma_TA = %.2f ueV, total %.2f ueV, tau = %.0f ps"
      % (gl * 1e6, gt * 1e6, (gl + gt) * 1e6, HBAR / (gl + gt) * 1e12))
gq = gamma_quad(E, xi2_LA, cLA)
print("  quadrature check LA: %.3f ueV (closed %.3f), rel %.1e" % (gq * 1e6, gl * 1e6, gq / gl - 1))
assert abs(gq / gl - 1) < 5e-3
for E in (0.001, 0.003, 0.010, 0.030):
    gg = gamma_closed(E, xi2_LA, cLA) + gamma_closed(E, xi2_TA, cTA)
    print("  E = %4.1f meV: Gamma = %.2f ueV, tau = %.0f ps" % (E * 1e3, gg * 1e6, HBAR / gg * 1e12))
# large-k form 4 Omega Xi^2 m*^2 E / (3 pi M_cell c)
print("  large-k form at 10 meV, LA: %.2f ueV" % (4 * OMEGA * xi2_LA * MS ** 2 * 0.010 / (3 * np.pi * M_CELL * cLA) * 1e6))

# ---------------- figure ----------------
T = np.linspace(0, 600, 601)
corners = [eg_meas(T, a, b) for a in (A_V - 0.2e-4, A_V + 0.2e-4) for b in (B_V - 40, B_V + 40)]
lo, hi = np.min(corners, axis=0), np.max(corners, axis=0)
fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.fill_between(T, lo, hi, color="0.8", lw=0, label="measured, $\\pm1\\sigma$")
ax.plot(T, eg_meas(T), color="k", lw=1.6, label="measured (photoluminescence fit)")
ax.plot(T, einstein(T, ZPR_NA), color="C0", lw=1.4, label="Einstein model, ZPR $-56.2$ meV")
ax.plot(T, einstein(T, ZPR_AD), color="C0", lw=1.0, ls="--", label="Einstein model, ZPR $-64.3$ meV")
u2r = np.array([u2(t) for t in T]) / u2(0)
ax.plot(T, EG0 + ZPR_NA * (u2r - 1), color="C3", lw=1.2, ls="-.", label="shift $\\propto\\langle u^2\\rangle$, ZPR $-56.2$ meV")
ax.plot(T, Ecl + 2 * ZPR_NA * KB * T / wE, color="C0", lw=0.8, ls=":")
ax.plot([0], [Ecl], "o", color="C0", ms=4)
ax.annotate("", xy=(8, EG0), xytext=(8, Ecl), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(14, 0.5 * (EG0 + Ecl), "ZPR", va="center", fontsize=8)
ax.text(20, Ecl + 0.002, "clamped lattice (model)", fontsize=8, color="C0")
ax.set_xlim(0, 600)
ax.set_ylim(1.02, 1.235)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Indirect gap of silicon (eV)")
ax.legend(fontsize=7, loc="lower left", frameon=False)
fig.tight_layout()
fig.savefig(OUT)
print("\nwrote", OUT)
