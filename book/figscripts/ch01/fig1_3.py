"""Laboratory-frame speed distribution of the standard halo model on the days of largest and smallest
Earth speed. Output: tex/figures/ch01/fig1_3.pdf. Every plotted number is sourced below.
  [B]  D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1 and Eq. (11).
Speed distribution: F_chi(v) = v^2 * integral over directions of f_chi; closed form derived in the text
(Sect. 1.2) and Appendix D.1, checked here against direct quadrature.
"""
import os, datetime as dt
import numpy as np
from scipy.special import erf
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V0 = 238.0                                  # km/s, |LSR velocity| [B, Table 1]
VESC = 544.0                                # km/s [B, Table 1]
V_SUN = np.array([11.1, 238.0 + 12.2, 7.3]) # km/s, LSR (0,238,0) + peculiar (11.1,12.2,7.3) [B, Table 1]
V_ORB = 29.8                                # km/s, mean orbital speed [B, Table 1 and Eq. (13)]
OMEGA_YR = 0.0172                           # rad/day [B, below Eq. (11)]
T0 = dt.date(2018, 3, 22)                   # reference date of [B, Eq. (11)]

def v_orb(days):
    """Earth velocity relative to the Sun, galactic (U, V, W) components [B, Eq. (11)]."""
    w = OMEGA_YR * days
    return V_ORB * np.array([0.9941*np.cos(w) - 0.0504*np.sin(w),
                             0.1088*np.cos(w) + 0.4946*np.sin(w),
                             0.0042*np.cos(w) - 0.8677*np.sin(w)])

Z = VESC / V0
N_ESC = np.pi**1.5 * V0**3 * (erf(Z) - 2/np.sqrt(np.pi) * Z * np.exp(-Z**2))

def F(v, a):
    """Lab-frame speed distribution for Earth speed a (km/s); units (km/s)^-1."""
    pre = np.pi * v * V0**2 / (a * N_ESC)
    lo = np.exp(-(v - a)**2 / V0**2)
    hi = np.where(v < VESC - a, np.exp(-(v + a)**2 / V0**2), np.exp(-Z**2))
    return np.where(v < VESC + a, pre * (lo - hi), 0.0)

days = np.linspace(0, 365.25, 36526)
speeds = np.array([np.linalg.norm(V_SUN + v_orb(d)) for d in days])
i_max, i_min = speeds.argmax(), speeds.argmin()
a_jun, a_dec = speeds[i_max], speeds[i_min]       # 266.4 and 237.4 km/s
d_jun = T0 + dt.timedelta(days=float(days[i_max]))  # 2 June
d_dec = T0 + dt.timedelta(days=float(days[i_min]))  # 2 December
for a in (a_jun, a_dec):
    assert abs(quad(lambda v: F(v, a), 0, VESC + a, points=[VESC - a])[0] - 1) < 1e-8

v = np.linspace(0, 830, 1661)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.6, 4.8), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
c_jun, c_dec = "#eb6834", "#2a78d6"
ax1.plot(v, 1e3 * F(v, a_jun), color=c_jun, lw=1.6, label=rf"June (maximum), $|\mathbf{{v}}_E| = {a_jun:.1f}$ km/s")
ax1.plot(v, 1e3 * F(v, a_dec), color=c_dec, lw=1.6, ls="--", label=rf"December (minimum), $|\mathbf{{v}}_E| = {a_dec:.1f}$ km/s")
ax1.set_ylabel(r"$F_\chi(v)$  [$10^{-3}$ (km/s)$^{-1}$]")
ax1.set_ylim(0, 3.7)                              # headroom: the legend sits above the peak
ax1.legend(frameon=False, fontsize=8, loc="upper right")
ratio = F(v, a_jun) / np.where(F(v, a_dec) > 0, F(v, a_dec), np.nan)
ax2.plot(v, ratio, color="0.2", lw=1.4)
ax2.axhline(1, color="0.6", lw=0.6)
ax2.set_ylabel("June / December")
ax2.set_xlabel(r"laboratory speed $v$ [km/s]")
ax2.set_ylim(0, 4)
v_max = VESC + np.linalg.norm(V_SUN)              # 794.5 km/s
for ax in (ax1, ax2):
    ax.axvline(v_max, color="0.5", ls=":", lw=0.8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
ax1.text(v_max - 8, ax1.get_ylim()[1] * 0.5, r"$v_{\mathrm{max}}$", ha="right", fontsize=8, color="0.3")
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_3.pdf")
fig.savefig(out)
print(a_jun, d_jun, a_dec, d_dec, v_max)
