"""Fig. 1.9 (prints as the second figure of Sect. 1.5): schematic exclusion curve in (m_chi, sigma_e) for a heavy and a
light mediator. Output: tex/figures/ch01/fig1_9.pdf. The curve is schematic: the target response is a toy, and each
curve has an arbitrary normalization. Every number is sourced below.
  [B]   D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1: v0 = 238, v_esc = 544,
        |v_sun| = 250.5 km/s adopted (250.55 exact; Sect. 1.2); v_max = v_esc + v_E^ref = 794.5 km/s.
  [D.1] eta(v_min) closed form, Appendix D.1 (same code as fig1_6.py, checked there against quadrature).
  [KL]  T. Lin and Y. Kahn, Rep. Prog. Phys. 85, 066901 (2022), arXiv:2108.03239, Eq. (11): isotropic rate
        R = (1/rho_T)(rho_chi/m_chi) int q dq/(2 pi)^2 int d omega eta(v_min) (pi sigma_e F_DM^2/mu^2) S(q, omega).
  [E16] R. Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598, Eq. (5.2) (toy rate);
  [R20] K. Ramanathan and N. Kurinsky, Phys. Rev. D 102, 063026 (2020), Eq. (11): low-temperature silicon gap
        1.1692 eV, rounded to 1.17 eV (threshold E_th = E_g).
  [EMV] R. Essig, J. Mardon, T. Volansky, Phys. Rev. D 85, 076007 (2012), arXiv:1108.5383, Eq. (15): F_DM = 1, (q0/q)^2.
  [CODATA] alpha = 1/137.035999084, m_e = 510998.95 eV, c = 299792.458 km/s.
Toy target response (an assumption of this figure only, not a material property):
  S_toy(q, omega) = Theta(omega - E_g) Theta(omega_up - omega) exp(-q^2 / (2 q_s^2)), omega_up = 30 eV, q_s = 2 q0:
  a flat spectrum above the gap, cut at the momenta of valence electrons (a few q0).
Limit: sigma_lim(m_chi) = N_90 / (exposure * R(m_chi)/sigma_e); only the shape is plotted.
"""
import os
import numpy as np
from scipy.special import erf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V0, VESC, VE = 238.0, 544.0, 250.5            # km/s [B]
CKM = 299792.458                              # km/s [CODATA]
ALPHA, ME = 1 / 137.035999084, 510998.95      # [CODATA]; eV
Q0 = ALPHA * ME                               # 3.73 keV
EG = 1.17                                     # eV [R20], low-temperature gap
OMEGA_UP, QS = 30.0, 2 * Q0                   # toy response: Gaussian cutoff exp(-q^2/(2 QS^2)), QS = 2 q0 (see docstring)
VMAX = (VESC + VE) / CKM                      # 2.650e-3
Z = VESC / V0
N_ESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))


def eta(u):
    """Appendix D.1, all branches, at v_E^ref; returns (km/s)^-1."""
    k = np.pi * V0**2 / (VE * N_ESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


def rate_per_sigma(m, light):
    """[KL Eq. (11)] with S_toy, up to constant factors; m in eV."""
    mu = m * ME / (m + ME)
    om = np.linspace(EG, OMEGA_UP, 300)
    q = np.logspace(np.log10(EG / VMAX) - 0.01, np.log10(2 * m * VMAX) + 0.01, 600)
    O, Q = np.meshgrid(om, q, indexing="ij")
    vmin = (O / Q + Q / (2 * m)) * CKM                       # km/s, Delta_chi = 0 (Sect. 1.3)
    fdm2 = (Q0 / Q)**4 if light else 1.0                      # [EMV]
    integrand = Q * eta(vmin) * fdm2 * np.exp(-Q**2 / (2 * QS**2))
    inner = np.trapezoid(integrand, q, axis=1)
    return np.trapezoid(inner, om) / (m * mu**2)


mmin = 2 * EG / VMAX**2                                       # threshold mass, Eq. (1.3-mmin): 0.33 MeV
m = np.logspace(np.log10(mmin * 1.0005), np.log10(1e9), 260)  # eV
lim_h = np.array([1 / rate_per_sigma(x, False) for x in m])
lim_l = np.array([1 / rate_per_sigma(x, True) for x in m])
lim_h /= lim_h.min()
lim_l /= lim_l.min() / 30.0                                    # offset for legibility (arbitrary normalization)
mev = m / 1e6

fig, ax = plt.subplots(figsize=(5.0, 3.6))
ax.loglog(mev, lim_h, color="k", lw=1.4, label=r"heavy mediator, $F_{\mathrm{DM}} = 1$")
ax.loglog(mev, lim_l, color="C3", lw=1.4, ls="--", label=r"light mediator, $F_{\mathrm{DM}} = (q_0/q)^2$")
ax.fill_between(mev, lim_h, 1e9, color="0.9", lw=0)
ax.axvline(mmin / 1e6, color="0.5", lw=0.7, ls=":")
ax.text(mmin / 1e6 * 1.08, 0.5, r"$m_{\mathrm{min}}$", fontsize=8, color="0.3")
# guide: sigma_lim proportional to m_chi at large mass
mg = np.array([60.0, 600.0])
ax.loglog(mg, 2.0 * (mg / 60.0), color="0.4", lw=0.8)
ax.text(170, 2.0 * 170 / 60 * 0.45, r"$\propto m_\chi$", fontsize=8, color="0.3")
ax.text(2.0, 2e4, "excluded (heavy mediator)", fontsize=7, color="0.35")
ax.set_xlim(0.2, 1000)
ax.set_ylim(0.3, 1e6)
ax.set_xlabel(r"$m_\chi$ [MeV]")
ax.set_ylabel(r"$\bar\sigma_e$ limit (arbitrary normalization)")
ax.legend(fontsize=7, frameon=False, loc="upper right")
fig.tight_layout()

out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_9.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
i = np.argmin(lim_h); j = np.argmin(lim_l)
print("heavy minimum at %.2f MeV, light minimum at %.2f MeV" % (mev[i], mev[j]))
k1 = np.argmin(abs(mev - 1.0))
print("ratio to minimum at 1 MeV: heavy %.1f, light %.2f" % (lim_h[k1] / lim_h[i], lim_l[k1] / lim_l[j]))  # text: 46 and 1.4
for x in [0.4, 1, 10, 100, 1000]:
    k = np.argmin(abs(mev - x)); print(x, lim_h[k], lim_l[k] / 30)
