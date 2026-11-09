"""Limit Check 14.5b (lim:14.5b, Sect. 14.5): the static magnetoelectric cross response of a multiferroic against T/T_CM.
Output tex/figures/ch14/limit14_5b.pdf, log limit14_5b.log.  Run: python limit14_5b.py  (seconds).

Literature formula: Roising et al., 2102.10171 Eq. (10): the magnetization driven by the axion is a single damped oscillator,
  |dM/theta_0| = |chi alpha M_0/(2 alpha_M) - c P_0/(2 m_P^2)| / sqrt((omega_a^2 - omega_M^2)^2 + eta_M^2 omega_a^2),
  whose static (adiabatic, omega_a << omega_M) limit is controlled by omega_M^-2 (their Sect. III D). Their omega_M comes from the
  Ginzburg-Landau free energy (their Eqs. (6)-(8)), whose quadratic coefficient is linear in T - T_CM; below T_CM the longitudinal
  stiffness is then 2 gamma_M (T_CM - T), and omega_M^-2 is proportional to the Landau longitudinal susceptibility
  chi_L = C/[2(T_CM - T)], C = |S|(|S|+1)/3 (units (g mu_B)^2 per spin, k_B = 1).
Fuller result (the same magnet beyond the Landau expansion): MODEL, a spin-|S| ferromagnet, |S| = 5/2 (Fe3+, the magnetic ion of
  the hexaferrite the source considers), treated
  (i) in Weiss mean field over the whole ordered range: <S_z> = |S| B_S(y), y = beta |S| (lambda <S_z> + h), lambda = 3 T_CM/[|S|(|S|+1)],
      chi_MF = beta |S|^2 B_S'(y) / [1 - lambda beta |S|^2 B_S'(y)]  (Landau is its expansion about T_CM);
  (ii) by linear spin waves for T << T_CM: nearest-neighbour simple-cubic ferromagnet, omega_k = Delta + 2 J|S| sum_i (1 - cos k_i),
      J|S| fixed by the mean-field T_CM = 2 J|S|(|S|+1) (z = 6), MODELLING CHOICE Delta = 0.02 T_CM (easy-axis gap);
      chi_SW = N^-1 sum_k beta n_k (n_k + 1) (thermal magnons; at T = 0 a collinear ferromagnet has chi = 0 because S^z_tot is
      conserved), 48^3 grid.
  Shaded: T/T_CM where the thermal spin-wave reduction of the moment, N^-1 sum_k n_k, is below 10 % of |S| (the regime T << T_CM in
  which linear spin-wave theory is the controlled calculation). Hatched: T > 0.9 T_CM, where critical fluctuations beyond mean field
  control the response and no controlled calculation exists (open).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
LOG = open(os.path.join(HERE, "limit14_5b.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


S = 2.5
C = S * (S + 1) / 3
lam = 3.0 / (S * (S + 1))          # T_CM = 1


def BS(y):
    if y < 1e-3:
        return (S + 1) / (3 * S) * y
    a, b = (2 * S + 1) / (2 * S), 1 / (2 * S)
    return a / np.tanh(a * y) - b / np.tanh(b * y)


def dBS(y):
    if y > 300:
        return 0.0
    a, b = (2 * S + 1) / (2 * S), 1 / (2 * S)
    return -a**2 / np.sinh(a * y)**2 + b**2 / np.sinh(b * y)**2


def chi_mf(t):
    f = lambda sig: sig - BS(S * lam * S * sig / t)
    sig = brentq(f, 1e-9, 1.0 + 1e-9) if t < 1 else 0.0
    y = S * lam * S * sig / t
    bp = dBS(y) if y > 1e-6 else (S + 1) / (3 * S)
    return S**2 * bp / t / (1 - lam * S**2 * bp / t), sig


JS = 1.0 / (2 * (S + 1))
DELTA = 0.02
n = 48
k = 2 * np.pi * (np.arange(n) + 0.5) / n
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
WK = DELTA + 2 * JS * ((1 - np.cos(KX)) + (1 - np.cos(KY)) + (1 - np.cos(KZ)))


def sw(t):
    nb = 1 / np.expm1(WK / t)
    return np.mean(nb * (nb + 1)) / t, np.mean(nb)


t = np.linspace(0.02, 0.995, 400)
cl = C / (2 * (1 - t))
cmf = np.array([chi_mf(x)[0] for x in t])
csw, dsw = np.array([sw(x) for x in t]).T
ratio = cl / cmf
okL = np.abs(ratio - 1) <= 0.1
out(f"|S| = {S}, C = {C:.4f}; spin-wave model J|S| = {JS:.4f} T_CM, bandwidth {12*JS:.3f} T_CM, gap {DELTA} T_CM")
out(f"Landau chi_L within 10 % of mean field for T/T_CM >= {t[okL].min():.3f}")
for x in (0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95):
    a, sig = chi_mf(x)
    b, d = sw(x)
    out(f"  T/T_CM = {x:4.2f}: Landau/MF = {C/(2*(1-x))/a:9.3g}, Landau/SW = {C/(2*(1-x))/b:9.3g}, MF <S_z>/|S| = {sig:.3f},"
        f" SW reduction/|S| = {d/S:.4f}")
tl = t[dsw / S <= 0.1].max()
out(f"thermal spin-wave reduction below 10 % of |S| for T/T_CM <= {tl:.3f}")

fig, ax = plt.subplots(figsize=(3.6, 3.0))
ax.axvspan(0, tl, color="0.88", lw=0, zorder=0)
ax.axvspan(0.9, 1.0, facecolor="none", edgecolor="0.6", hatch="////", lw=0, zorder=0)
ax.semilogy(t, cl / C, color="k", lw=1.0, label=r"Landau: $\omega_M^{-2}\propto(T_{\mathrm{CM}} - T)^{-1}$")
ax.semilogy(t, cmf / C, color="C3", lw=1.3, label="mean field")
m = t <= 0.6
ax.semilogy(t[m], csw[m] / C, color="C0", lw=1.3, ls="--", label=r"spin waves ($T \ll T_{\mathrm{CM}}$)")
ax.text(0.89, 2e-3, "critical:\nopen", fontsize=6.5, color="0.3", ha="right")
ax.set_xlim(0, 1)
ax.set_ylim(1e-3, 30)
ax.set_xlabel(r"$T/T_{\mathrm{CM}}$")
ax.set_ylabel(r"static longitudinal response $/\,C$")
ax.legend(fontsize=6.3, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_5b.pdf"))
out("wrote", os.path.join(FIG, "limit14_5b.pdf"))
LOG.close()
