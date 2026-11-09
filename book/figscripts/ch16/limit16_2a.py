"""Limit Check 16.2a (one-dimensional plasmons, linear-band RPA) of Sect. 16.2: comparison plot and caption numbers.

Output: tex/figures/ch16/limit16_2a.pdf.
Literature form (Zhang and Chen arXiv:2607.15338 Eqs. (3)-(4), N_ch = 1; book form with N_ch channels):
  S_wire = N_ch g_c |q| delta(omega - v q/g_c),  g_c = [1 + N_ch v1D(q)/(pi v)]^(-1/2),
the RPA of N_ch linear channels (exact for the linear-band model with density-density interaction).
Fuller result: the RPA of N_ch parabolic channels with the same velocity v at k_F (the band curvature that a real
band brings at q ~ k_F).  Per channel the 1D Lindhard function is
  R0_1 = (m/2 pi q) ln[(omega^2 - omega_-^2)/(omega^2 - omega_+^2)],  omega_pm = q v +- q^2/2m,
and the RPA zero 1 = v1D N_ch R0_1 has the closed form
  omega_pl^2 = (omega_+^2 e^y - omega_-^2)/(e^y - 1),  y = 2 pi q/(N_ch v1D m).
Pole share = first moment of the pole, omega_pl/(v1D d eps/d omega), over the f-sum N_ch v q^2/2 pi.
Leading correction (expansion in y, Sect. 16.2): omega_par/omega_lin = 1 + (q/k_F)^2 g_c^2 [1/4 + g_c^2/(3(1-g_c^2))]/2.
Model: kernel of a shell of radius r_t = 0.7 nm (eps_env = 1), N_ch = 4, v = v_D (graphene), k_F = 1/r_t: the
parabolic band is a stand-in for the curvature of the nanotube bands on the scale 1/r_t of the subband spacing.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L

KF = 1 / L.R_T
V = L.V_D
M = KF / V
N = L.N_CH


def parab(x):
    q = x * KF
    vq = L.v1D(q)
    y = 2 * np.pi * q / (N * vq * M)
    wp = q * V + q * q / (2 * M)
    wm = q * V - q * q / (2 * M)
    w = np.sqrt((wp ** 2 * np.exp(y) - wm ** 2) / np.expm1(y))
    dR = N * (M / (2 * np.pi * q)) * (2 * w / (w * w - wm * wm) - 2 * w / (w * w - wp * wp))
    share = (w / (vq * (-vq * dR))) / (N * V * q * q / (2 * np.pi))
    wlin = V * q / L.g_c(q)
    return w / wlin, share


def corr(x):
    g = L.g_c(x * KF)
    return 1 + 0.5 * x ** 2 * g ** 2 * (0.25 + g ** 2 / (3 * (1 - g ** 2)))


x = np.geomspace(0.01, 1.9, 300)
rat = np.array([parab(xx)[0] for xx in x])
sh = np.array([parab(xx)[1] for xx in x])
x10_w = brentq(lambda xx: parab(xx)[0] - 1.1, 0.5, 1.9)
x10_s = brentq(lambda xx: parab(xx)[1] - 0.9, 0.5, 1.9)
x10 = min(x10_w, x10_s)
print(f"k_F = 1/r_t = {KF:.1f} eV, v = v_D = {V:.4e}, m = k_F/v = {M/L.ME:.4f} m_e, N_ch = {N}")
for xx in [0.01, 0.1, 0.5, 1.0, 1.5, 1.9]:
    r, s = parab(xx)
    print(f"  q/k_F = {xx}: g_c = {L.g_c(xx*KF):.3f}, omega ratio {r:.4f} (leading correction {corr(xx):.4f}), pole share {s:.4f}")
print(f"  10% points: omega ratio 1.1 at q/k_F = {x10_w:.3f}; pole share 0.9 at q/k_F = {x10_s:.3f}")
print(f"  nanotube: k_F = 1/r_t corresponds to q = {KF:.0f} eV; subband threshold 2 v_D/r_t = {2*V*KF:.3f} eV")
assert abs(parab(0.1)[0] - corr(0.1)) < 1e-6

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(x[0], x10, color="0.9", lw=0)
ax.semilogx(x, np.ones_like(x), color="k", lw=1.0, ls="--", label="linear bands (frequency and pole share)")
ax.semilogx(x, rat, color="C3", lw=1.4, label=r"parabolic bands: $\omega_{\mathrm{pl}}$ ratio")
ax.semilogx(x, corr(x), color="C3", lw=0.9, ls=":", label=r"leading correction $O(q^2/k_{\mathrm{F}}^2)$")
ax.semilogx(x, sh, color="C0", lw=1.4, label="parabolic bands: pole share of the $f$-sum")
ax.set_xlabel(r"$q/k_{\mathrm{F}}$")
ax.set_ylabel("ratio to the linear-band result")
ax.set_xlim(x[0], x[-1])
ax.set_ylim(0.55, 1.4)
ax.legend(fontsize=7, frameon=False, loc="lower left")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tex/figures/ch16/limit16_2a.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out)
print("wrote", os.path.normpath(out))
