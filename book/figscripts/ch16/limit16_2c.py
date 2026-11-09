"""Limit Check 16.2c (effective medium of a layered stack) of Sect. 16.2: comparison plot and caption numbers.

Output: tex/figures/ch16/limit16_2c.pdf.
Model stack (the toy of Lasenby and Prabhu arXiv:2110.01587, Sect. IV and Fig. 4): conducting layers of thickness
d_A = 1 nm with eps_A = 10 [1 - omega_p^2/(omega(omega + i gamma))], omega_p = 0.5 eV, gamma = 0.1 omega_p (their
analogy to NbN), alternating with vacuum layers d_B = 4 nm (eps_B = 1); period a_s = 5 nm, filling f = 0.2.
Literature form: the effective medium, Lasenby-Prabhu Eq. (16), = the uniaxial medium with eps_par (along the stacking
axis) = harmonic mean and eps_perp (in plane) = arithmetic mean (Sect. 16.2).
Fuller result: the exact head eps^-1_{00}(k, omega) of the periodic stack (lowd16_2.stack_general; in-plane closed
form lowd16_2.stack_inplane).  Plotted: frequency of the maximum of the loss function L = Im(-eps^-1_{00}) over the
effective-medium value, against k a_s, for k in the plane (theta = 90 deg from the axis) and at theta = 30 deg.
Leading correction (in-plane, Sect. 16.2): 1/eps = 1/eps_perp + (k a_s)^2 f^2 (1-f)^2 (eps_A - eps_B)^2/(12 eps_par eps_perp^2).
Shaded: both directions within 10 % of the effective medium.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L

WP, GAM, EINF = 0.5, 0.05, 10.0
DA, DB = 1.0, 4.0           # nm
A = DA + DB
F = DA / A
EB = 1.0


def epsA(w):
    return EINF * (1 - WP ** 2 / (w * (w + 1j * GAM)))


def peak(inv_fun):
    """Frequency of the maximum of Im(-inv_fun(omega)) between 0.05 and 0.6 eV."""
    w = np.linspace(0.05, 0.6, 2201)
    Lw = np.array([np.imag(-inv_fun(x)) for x in w])
    i = int(np.argmax(Lw))
    res = minimize_scalar(lambda x: -np.imag(inv_fun(x)), bounds=(w[max(i - 1, 0)], w[min(i + 1, len(w) - 1)]),
                          method="bounded", options={"xatol": 1e-8})
    return res.x


def corr_inv(w, ka):
    eA = epsA(w)
    epar = 1 / (F / eA + (1 - F) / EB)
    eperp = F * eA + (1 - F) * EB
    return 1 / eperp + ka ** 2 * F ** 2 * (1 - F) ** 2 * (eA - EB) ** 2 / (12 * epar * eperp ** 2)


CTH = {"in plane": 0.0, "30 deg": np.cos(np.radians(30))}
w_emt = {lab: peak(lambda w, c=c: L.emt_inv(epsA(w), EB, F, c)) for lab, c in CTH.items()}
print(f"model: d_A = {DA} nm, d_B = {DB} nm, a_s = {A} nm, f = {F}, omega_p = {WP} eV, gamma = {GAM} eV, eps_inf = {EINF}")
for lab, w0 in w_emt.items():
    print(f"  effective-medium loss peak, {lab}: {w0:.4f} eV")
# check: exact solution reproduces the effective medium at small k a_s and the in-plane closed form
w = 0.3
for c in CTH.values():
    ex = L.stack_general(epsA(w), EB, DA, DB, 1e-4 / A, max(c, 1e-9))
    em = L.emt_inv(epsA(w), EB, F, c)
    assert abs(ex - em) < 1e-6 * abs(em), (ex, em)
assert abs(L.stack_general(epsA(w), EB, DA, DB, 2.0 / A, 1e-9) - L.stack_inplane(epsA(w), EB, F, 2.0)) < 1e-10

kas = np.geomspace(0.05, 12, 70)
ratio = {}
for lab, c in CTH.items():
    rr = []
    for ka in kas:
        k = ka / A
        if c == 0.0:
            f = lambda x, ka=ka: L.stack_inplane(epsA(x), EB, F, ka)
        else:
            f = lambda x, k=k, c=c: L.stack_general(epsA(x), EB, DA, DB, k, c)
        rr.append(peak(f) / w_emt[lab])
    ratio[lab] = np.array(rr)
rc = np.array([peak(lambda x, ka=ka: corr_inv(x, ka)) for ka in kas]) / w_emt["in plane"]

for lab in CTH:
    for ka in [0.5, 1.0, 2.0, 5.0]:
        print(f"  {lab}: k a_s = {ka}: peak / effective medium = {np.interp(ka, kas, ratio[lab]):.4f}")
for ka in [0.5, 1.0, 2.0]:
    print(f"  in plane, leading correction at k a_s = {ka}: {np.interp(ka, kas, rc):.4f}")


def cross(lab):
    r = ratio[lab]
    j = np.argmax(np.abs(r - 1) > 0.1)
    return brentq(lambda ka: np.interp(np.log(ka), np.log(kas), np.abs(r - 1)) - 0.1, kas[j - 1], kas[j])


k10 = {lab: cross(lab) for lab in CTH}
for lab in CTH:
    print(f"  10% point, {lab}: k a_s = {k10[lab]:.3f}, k = {k10[lab]/A:.3f} nm^-1 = {k10[lab]/A*L.HBARC:.1f} eV")
lim = min(k10.values())
print(f"  large k a_s, in plane: peak at {ratio['in plane'][-1]*w_emt['in plane']:.4f} eV "
      f"(isolated-layer limit eps_A = -eps_B coth(k d_A/2) -> -1: {WP*np.sqrt(EINF/(EINF+1)):.4f} eV for gamma -> 0)")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(kas[0], lim, color="0.9", lw=0)
ax.semilogx(kas, np.ones_like(kas), color="k", lw=1.0, ls="--", label="effective medium (both directions)")
ax.semilogx(kas, ratio["in plane"], color="C3", lw=1.4, label=r"exact stack, $\mathbf{k}$ in the plane")
ax.semilogx(kas[kas < 3], rc[kas < 3], color="C3", lw=0.9, ls=":", label=r"leading correction $O(k^2a_s^2)$")
ax.semilogx(kas, ratio["30 deg"], color="C0", lw=1.4, label=r"exact stack, $30^\circ$ from the axis")
ax.set_xlabel(r"$k a_s$")
ax.set_ylabel("loss peak / effective medium")
ax.set_xlim(kas[0], kas[-1])
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tex/figures/ch16/limit16_2c.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
print(f"  30 deg at k a_s = {kas[-1]:.1f}: peak at {ratio['30 deg'][-1]*w_emt['30 deg']:.4f} eV")
print(f"  10% point at 30 deg: k = {k10['30 deg']/A*L.HBARC:.1f} eV = 2 m_chi v_max for m_chi = {k10['30 deg']/A*L.HBARC/(2*L.VMAX)/1e3:.1f} keV")
