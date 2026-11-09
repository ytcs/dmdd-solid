"""Fig. 4.2: dynamic structure factor of the non-interacting electron gas at T = 0 and its particle-hole continuum
(Sect. 4.2, Worked example 4.3), and every number quoted in Worked examples 4.3 and 4.4.
Output: tex/figures/ch04/fig4_2.pdf. Natural units hbar = c = k_B = 1.

Model (derived in Sect. 4.2, Worked example 4.3; no external data enter the curves):
  S0(q, w) = (2 pi / V) * 2 * sum_k Theta(k_F - k) Theta(|k + q| - k_F) delta(w - (k+q)^2/2m + k^2/2m)
           = (m / 2 pi q) (k_F^2 - k_min^2),  k_min = max(|m w/q - q/2|, sqrt(max(k_F^2 - 2 m w, 0))), if k_min < k_F; else 0,
  i.e. S0 = m^2 w / (pi q) for 0 < w < q v_F - q^2/2m (q < 2 k_F), and (m / 2 pi q)[k_F^2 - (m w/q - q/2)^2] up to the
  upper edge w_+ = q v_F + q^2/2m; lower edge w_- = q^2/2m - q v_F for q > 2 k_F.
  Plotted in reduced units: x = q/k_F, w/E_F, S0/(m_e k_F).
Inputs for the silicon-density numbers (all as quoted in Sect. 2.5 and App. A.1/A.2 of the book):
  valence density n_e = 2.00e23 cm^-3 (App. A.2); m_e = 510998.95 eV; hbar c = 197.3269804 eV nm;
  v_max = 2.65e-3 (Sect. 2.5: v_esc + v_E = 544 + ~250 km/s, as in Chap. 1).
Hydrogen numbers (Worked example 4.4) re-evaluated from the closed forms of Sect. 2.2:
  F_1s(q) = 16/(4 + q^2 a0^2)^2, |f_{1s->2p}|^2 = 72 (q a0)^2 / (9/4 + q^2 a0^2)^6.
Display choices: map range q/k_F in [0, 3], w/E_F in [0, 12]; cuts at q/k_F = 0.5, 1.5, 3; the dark-matter line
w = q v_max is drawn for the silicon density (v_max/v_F = 0.379).
"""
import os
import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def S0_red(x, nu):
    """S0 / (m k_F) at q = x k_F, w = nu E_F (E_F = k_F^2/2m). Units m = k_F = 1, so E_F = 1/2, w = nu/2."""
    w = 0.5 * nu
    q = x
    a = np.abs(w / q - q / 2)
    b = np.sqrt(np.clip(1.0 - 2 * w, 0, None))
    kmin = np.maximum(a, b)
    val = (1.0 / (2 * np.pi * q)) * (1.0 - kmin**2)
    return np.where((kmin < 1.0) & (w > 0), val, 0.0)


# ---- checks of the closed form ---------------------------------------------------------------------------------------
# density in these units: n_e = k_F^3 / 3 pi^2
n_e = 1.0 / (3 * np.pi**2)
def blocking(x):  # unblocked fraction of Sect. 2.5, eq:2.5-blocking
    return np.where(x < 2, 0.75 * x - x**3 / 16, 1.0)

for x in [0.1, 0.5, 1.0, 1.5, 1.99, 2.5, 3.0, 5.0]:
    wplus = x * 1.0 + x**2 / 2           # w_+ = q v_F + q^2/2m in units m = k_F = 1
    wminus = max(x**2 / 2 - x, 0.0)
    f = lambda w: S0_red(x, 2 * w)
    pts = [p for p in [x - x**2 / 2, x**2 / 2] if wminus < p < wplus]
    tot, _ = integrate.quad(f, wminus, wplus, points=pts or None, limit=400)
    mom, _ = integrate.quad(lambda w: w * f(w), wminus, wplus, points=pts or None, limit=400)
    # total weight = 2 pi n_e S^st(q), S^st = unblocked fraction
    assert np.isclose(tot, 2 * np.pi * n_e * blocking(x), rtol=1e-6), (x, tot)
    # f-sum: int w S dw = pi n_e q^2 / m (eq:A.7-fsum)
    assert np.isclose(mom, np.pi * n_e * x**2, rtol=1e-6), (x, mom)
# continuity at the kink w = q v_F - q^2/2m and value m(2k_F - q)/2pi there
for x in [0.3, 0.5, 1.0, 1.7]:
    wk = x - x**2 / 2
    assert np.isclose(S0_red(x, 2 * wk * (1 - 1e-9)), (2 - x) / (2 * np.pi), rtol=1e-6)
    assert np.isclose(S0_red(x, 2 * wk * (1 + 1e-9)), (2 - x) / (2 * np.pi), rtol=1e-6)
# linear region: S0 = m^2 w / (pi q); on the line w = q v (v < v_F - q/2m) it is m^2 v / pi, independent of q
for x in [0.2, 0.8, 1.5]:
    v = 0.379
    if v < 1 - x / 2:
        assert np.isclose(S0_red(x, 2 * x * v), v / np.pi)
# large q: parabola centred on the free recoil w = q^2/2m with half-width q v_F
x = 4.0
assert S0_red(x, 2 * (x**2 / 2 + x * 0.999)) > 0 and S0_red(x, 2 * (x**2 / 2 + x * 1.001)) == 0
assert np.isclose(S0_red(x, 2 * x**2 / 2), 1 / (2 * np.pi * x))

# kink at q = k_F/2: w = 0.375 k_F^2/m = 0.75 E_F, S0 = 0.75 m k_F / pi = 0.239 m k_F
xk = 0.5
print(f"q = 0.5 k_F: kink at w/E_F = {2*(xk - xk**2/2):.3f}, S0 = {(2-xk)/(2*np.pi):.3f} m k_F")
assert np.isclose(2 * (xk - xk**2 / 2), 0.75)
assert np.isclose((2 - xk) / (2 * np.pi), 0.2387, atol=5e-5)

# ---- silicon-density numbers -----------------------------------------------------------------------------------------
hbarc_eVcm = 197.3269804e-7  # eV cm
me = 510998.95
ne_si = 2.00e23 * hbarc_eVcm**3  # eV^3
kF = (3 * np.pi**2 * ne_si) ** (1 / 3)
EF = kF**2 / (2 * me)
vF = kF / me
vmax = 2.65e-3
print(f"Si density: k_F = {kF/1e3:.2f} keV, E_F = {EF:.1f} eV, v_F = {vF:.2e}, v_max/v_F = {vmax/vF:.3f}")
assert abs(kF / 1e3 - 3.57) < 0.005 and abs(EF - 12.5) < 0.05 and abs(vF - 7.0e-3) < 0.05e-3
mekF = me * kF
print(f"m_e k_F = {mekF:.3e} eV^2")
S_line = me**2 * vmax / np.pi
print(f"S0 on w = q v_max (q < 2k_F(1 - v_max/v_F)): m_e^2 v_max / pi = {S_line:.2e} eV^2 = {S_line/mekF:.3f} m_e k_F")
assert np.isclose(S_line, 2.2e8, rtol=0.02)
qcut = 2 * kF * (1 - vmax / vF)
assert np.isclose(qcut / kF, 1.24, atol=0.005) and np.isclose(qcut / 1e3, 4.43, atol=0.005)
assert np.isclose(S_line / mekF, 0.121, atol=0.0005)
# caption, q = 3 k_F: omega_- = 3 E_F, omega_+ = 15 E_F (omega/E_F = x^2 -+ 2x)
assert np.isclose(3.0**2 - 2 * 3.0, 3.0) and np.isclose(3.0**2 + 2 * 3.0, 15.0)
assert S0_red(3.0, 2.99) == 0 and S0_red(3.0, 3.01) > 0 and S0_red(3.0, 14.99) > 0 and S0_red(3.0, 15.01) == 0
print(f"line inside the linear region for q < {qcut/kF:.2f} k_F = {qcut/1e3:.2f} keV")
# kink at q = k_F/2 in eV for silicon: 0.75 E_F
print(f"kink at q = k_F/2: {0.75*EF:.1f} eV")
assert np.isclose(np.exp(-1.12 / (8.617333e-5 * 300)), 1.53e-19, rtol=0.05)  # e^{-beta omega} across 1.12 eV at 300 K
# space and time scales of Sect. 4.2: 2pi/q0 and 1/omega for q0 = alpha m_e and omega = 10 eV
alpha = 1 / 137.035999
q0 = alpha * me
lam = 2 * np.pi * 197.3269804 / q0 * 10  # Angstrom (hbar c in eV nm -> x10 for Angstrom)
tau = 6.582119569e-16 / 10 * 1e15         # fs
print(f"2 pi / q0 = {lam:.2f} A; 1/omega at 10 eV = {tau:.3f} fs")
assert abs(lam - 3.32) < 0.01 and abs(tau - 0.066) < 0.001

# ---- hydrogen numbers (Worked example 4.4), from the closed forms of Sect. 2.2 ----------------------------------------
F1s = lambda y: 16 / (4 + y**2) ** 2
f2p = lambda y: 72 * y**2 / (9 / 4 + y**2) ** 6
print(f"H at q0: F_1s = {F1s(1):.2f}, F^2 = {F1s(1)**2:.2f}, 1 - F^2 = {1-F1s(1)**2:.2f}, |f_2p|^2 = {f2p(1):.3f}")
assert np.isclose(F1s(1), 0.64) and np.isclose(1 - F1s(1) ** 2, 0.59, atol=0.005) and np.isclose(f2p(1), 0.061, atol=5e-4)

# ---- figure ----------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.8), gridspec_kw={"width_ratios": [1.1, 1]})

xs = np.linspace(1e-3, 3.0, 600)
nus = np.linspace(0, 12, 600)
X, NU = np.meshgrid(xs, nus)
Z = S0_red(X, NU)
im = ax1.pcolormesh(X, NU, Z, cmap="Greys", shading="auto", vmin=0, vmax=0.35, rasterized=True)
cb = fig.colorbar(im, ax=ax1, pad=0.02)
cb.set_label(r"$S^0/(m_e k_{\mathrm{F}})$")
ax1.plot(xs, xs**2 + 2 * xs, "k-", lw=1.0)
ax1.plot(xs, np.clip(xs**2 - 2 * xs, 0, None), "k-", lw=1.0)
xk_line = xs[xs < 2]
ax1.plot(xk_line, 2 * xk_line - xk_line**2, "k:", lw=0.8)
ax1.plot(xs, xs**2, "k--", lw=0.8)
r = vmax / vF
ax1.plot(xs, 2 * r * xs, color="tab:red", lw=1.2)
ax1.fill_between(xs, 0, 2 * r * xs, color="tab:red", alpha=0.25, lw=0)
ax1.text(2.05, 10.4, r"$\omega_+$", fontsize=8)
ax1.text(2.45, 0.6, r"$\omega_-$", fontsize=8)
ax1.text(1.6, 1.6, r"$qv_{\max}$", color="tab:red", fontsize=8)
ax1.text(2.0, 5.0, r"$q^2/2m_e$", fontsize=8, rotation=0)
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 12)
ax1.set_xlabel(r"$q/k_{\mathrm{F}}$")
ax1.set_ylabel(r"$\omega/E_{\mathrm{F}}$")
ax1.text(0.04, 0.92, "(a)", transform=ax1.transAxes)

nu = np.linspace(0, 16, 4000)
for x, ls in [(0.5, "-"), (1.5, "--"), (3.0, "-.")]:
    ax2.plot(nu, S0_red(x, nu), "k", ls=ls, lw=1.0, label=rf"$q = {x:g}\,k_{{\mathrm{{F}}}}$")
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 0.3)
ax2.set_xlabel(r"$\omega/E_{\mathrm{F}}$")
ax2.set_ylabel(r"$S^0/(m_e k_{\mathrm{F}})$")
ax2.legend(frameon=False, fontsize=8)
ax2.text(0.04, 0.92, "(b)", transform=ax2.transAxes)

fig.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "..", "tex", "figures", "ch04", "fig4_2.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
