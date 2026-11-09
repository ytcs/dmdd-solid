"""Fig. 1.6: mean inverse speed above v_min, eta(v_min), in the standard halo model, at the reference Earth speed
and on the days of largest and smallest Earth speed. Output: tex/figures/ch01/fig1_6.pdf.
Every plotted number is sourced below.
  [B]   D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1 (v0 = 238 km/s, v_esc = 544 km/s,
        LSR (0, 238, 0) + peculiar (11.1, 12.2, 7.3) km/s, so |v_sun| = 250.5 km/s) and Eq. (11) (Earth orbit).
        Earth speeds 266.4 km/s (2 June) and 237.4 km/s (2 December) from Eq. (11), as computed in Sect. 1.2.
  [E16] R. Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598, Eqs. (67)-(68): the same branches as Appendix D.1.
Closed form: Appendix D.1, Eqs. (D.1-eta1), (D.1-eta2); checked here against quadrature of F_chi(v)/v.
Edge approximation: eta ~ pi v_esc exp(-v_esc^2/v0^2) delta^2 [1 + delta (2v_esc^2 - v0^2)/(3 v_esc v0^2)] / (v_E N_esc),
  delta = v_esc + v_E - v_min (Sect. 1.3, Eq. (1.3-edge)).
"""
import os
import numpy as np
from scipy.special import erf
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V0 = 238.0                      # km/s [B]
VESC = 544.0                    # km/s [B]
VE_REF = 250.5                  # km/s [B], |v_sun|
VE_JUN, VE_DEC = 266.4, 237.4   # km/s [B Eq. (11)], Sect. 1.2
Z = VESC / V0
N_ESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))


def eta(u, ve):
    """Appendix D.1, all branches; (km/s)^-1."""
    k = np.pi * V0**2 / (ve * N_ESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + ve) / V0) - erf((u - ve) / V0)) - 2 * ve * np.exp(-Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(Z) - erf((u - ve) / V0)) - (VESC + ve - u) * np.exp(-Z**2))
    return np.where(u < VESC - ve, b1, np.where(u < VESC + ve, b2, 0.0))


def f_speed(v, ve):
    """Laboratory speed distribution, Eq. (1.2-Fspeed); (km/s)^-1."""
    k = np.pi * V0**2 / (ve * N_ESC)
    if v >= VESC + ve:
        return 0.0
    hi = np.exp(-(v + ve)**2 / V0**2) if v < VESC - ve else np.exp(-Z**2)
    return k * v * (np.exp(-(v - ve)**2 / V0**2) - hi)


# check the closed form against quadrature
for u in [0.0, 300.0, 600.0, 780.0]:
    num = quad(lambda v: f_speed(v, VE_REF) / v, max(u, 1e-9), VESC + VE_REF, limit=200)[0]
    assert abs(num / eta(u, VE_REF) - 1) < 1e-6, (u, num, eta(u, VE_REF))

u = np.linspace(0, 820, 1641)
fig, ax = plt.subplots(figsize=(5.0, 3.6))
ax.semilogy(u, eta(u, VE_REF), color="k", lw=1.4, label=r"$v_{\mathrm{E}}^{\mathrm{ref}} = 250.5$ km/s")
ax.semilogy(u, eta(u, VE_JUN), color="C3", lw=1.0, ls="--", label="June maximum, 266.4 km/s")
ax.semilogy(u, eta(u, VE_DEC), color="C0", lw=1.0, ls="-.", label="December minimum, 237.4 km/s")
ue = np.linspace(700, VESC + VE_REF, 200)
dl = VESC + VE_REF - ue                                    # delta of Eq. (1.3-edge)
edge = np.pi * VESC * np.exp(-Z**2) * dl**2 / (VE_REF * N_ESC) * (1 + dl * (2 * VESC**2 - V0**2) / (3 * VESC * V0**2))
ax.semilogy(ue, edge, color="0.5", lw=1.0, ls=":", label="edge form")
ax.axvline(VESC - VE_REF, color="0.6", lw=0.6)
ax.text(VESC - VE_REF + 8, 2e-8, r"$v_{\mathrm{esc}} - v_{\mathrm{E}}^{\mathrm{ref}}$", fontsize=7, color="0.3")
ax.axvline(VESC + VE_REF, color="0.6", lw=0.6)
ax.text(VESC + VE_REF - 8, 1e-3, r"$v_{\mathrm{max}}$", fontsize=7, color="0.3", ha="right")
ax.set_xlim(0, 820)
ax.set_ylim(1e-8, 1e-2)
ax.set_xlabel(r"$v_{\mathrm{min}}$ [km/s]")
ax.set_ylabel(r"$\eta(v_{\mathrm{min}})$ [(km/s)$^{-1}$]")
ax.legend(fontsize=7, frameon=False, loc="lower left")
fig.tight_layout()

out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_6.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
