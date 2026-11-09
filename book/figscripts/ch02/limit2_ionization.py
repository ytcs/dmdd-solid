"""Limit box 'Atomic ionization rate' (Sect. 2.2): plane-wave and Fermi-corrected plane-wave ionization spectra
of hydrogen 1s against the exact Coulomb-continuum result. Output: tex/figures/ch02/limit2_ionization.pdf.

Quantities (atomic units inside the functions: a0 = 1, momenta in 1/a0, energies in E_B = 13.6057 eV):
  Ionization form factor |f_ion(p_ej, q)|^2 as defined in [EMV Eq. (6)] (the box in Sect. 2.2), for the one
  electron of hydrogen 1s (one spin state).
  Plane wave: the text after the box, (2l+1) p^2/(4 pi^3 q) int k dk |chi_nl(k)|^2 [EMV text after Eq. (6)],
    divided by 2 for one electron, with |chi_10(k)|^2 = 256 pi^2 a0^3/(1 + k^2 a0^2)^4
    (normalized to int k^2 dk |chi|^2 = (2 pi)^3). Closed form: 16 p^2/(3 pi q) [(1+(p-q)^2)^-3 - (1+(p+q)^2)^-3].
  Fermi factor: F = 2 pi nu/(1 - exp(-2 pi nu)), nu = Z_eff alpha m_e/p_ej, Z_eff = 1 [EMV Eq. (1) and text].
  Exact: outgoing Coulomb waves of hydrogen, partial-wave sum with regular Coulomb functions F_l(eta, pr),
    eta = -1/(p a0) (attractive) [DLMF 33.2], radial normalization 4 pi F_l/(pr) for the box's
    <psi_p'|psi_p> = (2 pi)^3 delta(p'-p)/p^2. The script evaluates it by quadrature (mpmath.coulombf) and checks
    it against the closed-form hydrogen 1s continuum generalized oscillator strength [Bethe, Ann. Phys. 397, 325
    (1930); Inokuti, Rev. Mod. Phys. 43, 297 (1971)]; agreement to 1e-5 confirms the transcription, which it then uses on the grid.
  Checks printed: plane-wave partial-wave sum = closed form; closure at q a0 = 3 (continuum = 1 - F_1s^2 to 0.3%).
Rate spectrum: d<sigma v>/d ln E_ej = (sigma_e/8 mu^2) int q dq |f_ion|^2 F_DM^2 eta(v_min) [EMV Eq. (5)],
  heavy mediator F_DM = 1, v_min = (E_B + E_ej)/q + q/(2 m_chi) (Sect. 1.3).
  eta: standard halo model, v0 = 238 km/s, v_esc = 544 km/s, v_E = 250.5 km/s [Baxter et al., arXiv:2105.00599,
  Table 1], closed form of Appendix D.1 (same function as figscripts/ch01/fig1_6.py).
Constants: alpha = 1/137.035999084, m_e = 510998.95 eV (CODATA 2018), E_B = 13.605693 eV (Rydberg energy).
Shading: where the Fermi-corrected plane wave is within a factor of two of the exact spectrum (stated in caption).
"""
import os
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import erf, spherical_jn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ALPHA = 1 / 137.035999084
M_E = 510998.95                  # eV
Q0 = ALPHA * M_E                 # eV, = 1/a0
E_B = 13.605693                  # eV
C_KMS = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
ZE = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(ZE) - 2 / np.sqrt(np.pi) * ZE * np.exp(-ZE**2))


def eta(u):
    """Mean inverse speed above u (km/s), Appendix D.1; (km/s)^-1."""
    k = np.pi * V0**2 / (VE * NESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-ZE**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(ZE) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-ZE**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


def f_pw(p, q):
    return 16 * p**2 / (3 * np.pi * q) * ((1 + (p - q)**2)**-3 - (1 + (p + q)**2)**-3)


def fermi(p):
    nu = 1.0 / p
    return 2 * np.pi * nu / (1 - np.exp(-2 * np.pi * nu))


def f_exact(p, q):
    """Closed-form hydrogen 1s continuum (Bethe), converted to the |f_ion|^2 normalization (factor 2 p^2)."""
    th = np.arctan2(2 * p, q * q - p * p + 1)          # branch in [0, pi]
    gos = 2**8 * q * q * (q * q + (1 + p * p) / 3) * np.exp(-2 / p * th) / (
        ((q + p)**2 + 1)**3 * ((q - p)**2 + 1)**3 * (1 - np.exp(-2 * np.pi / p)))
    return 2 * p * p * gos


def f_partial(p, q, coulomb=True):
    """|f_ion|^2 = (4 p^3/pi) sum_L (2L+1) |int r^2 dr R_L(pr) j_L(qr) R_10(r)|^2, R_10 = 2 e^-r."""
    def integ(L):
        def g(r):
            if r == 0:
                return 0.0
            rad = float(mp.coulombf(L, -1.0 / p, p * r)) / (p * r) if coulomb else spherical_jn(L, p * r)
            return r * r * rad * spherical_jn(L, q * r) * 2 * np.exp(-r)
        return quad(g, 0, 60, limit=400)[0]
    return 4 * p**3 / np.pi * sum((2 * L + 1) * integ(L)**2 for L in range(int(8 + 3 * (p + q))))


for p, q in [(0.3, 1.0), (1.0, 1.0), (2.0, 3.0)]:
    a, b = f_partial(p, q), f_exact(p, q)
    c, d = f_partial(p, q, coulomb=False), f_pw(p, q)
    print(f"p={p}, q={q}: partial-wave exact {a:.6g} vs closed form {b:.6g}; plane wave {c:.6g} vs {d:.6g}")
    assert abs(a / b - 1) < 1e-5 and abs(c / d - 1) < 1e-5
cont = quad(lambda t: f_exact(np.exp(t / 2), 3.0) / 4, -12, 12, limit=500)[0]
print(f"closure at q a0 = 3: continuum {cont:.4f}, 1 - F_1s^2 = {1 - (16 / 13**2)**2:.4f}")

X = np.logspace(-2, 3, 6000)       # q a0


def spectrum(e_ej, mchi, f):
    """d<sigma v>/d ln E_ej up to the constant sigma_e/(8 mu^2 a0^2); e_ej in units of E_B, mchi in eV."""
    p = np.sqrt(e_ej)
    vmin = ((1 + e_ej) * E_B / (X * Q0) + X * Q0 / (2 * mchi)) * C_KMS
    return np.trapezoid(X * f(p, X) * eta(vmin), X)


E = np.logspace(-3, 2, 121)          # E_ej / E_B
masses = [(1e9, "1 GeV", "-"), (1e7, "10 MeV", "--")]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4.6, 4.6), sharex=True, gridspec_kw={"height_ratios": [1.2, 1]})
for mchi, lab, ls in masses:
    ex = np.array([spectrum(e, mchi, f_exact) for e in E])
    pw = np.array([spectrum(e, mchi, f_pw) for e in E])
    pf = np.array([spectrum(e, mchi, lambda p, q: f_pw(p, q) * fermi(p)) for e in E])
    ok = ex > 0
    if mchi == 1e9:
        norm = ex.max()
        ax1.loglog(E[ok], ex[ok] / norm, "k", lw=1.4, label="exact continuum")
        ax1.loglog(E[ok], pf[ok] / norm, "C3", lw=1.2, label=r"plane wave $\times$ Fermi factor")
        ax1.loglog(E[ok], pw[ok] / norm, "C0", lw=1.0, ls=":", label="plane wave")
        good = ok & (pf > ex / 2) & (pf < 2 * ex)
        edge = E[good].max() if good.any() else None
        tot = [np.trapezoid(s[ok], np.log(E[ok])) for s in (ex, pf, pw)]
        print(f"1 GeV: PWxF within factor 2 for E_ej/E_B <= {edge:.3g}; total rate ratios PWxF/exact = "
              f"{tot[1] / tot[0]:.3f}, PW/exact = {tot[2] / tot[0]:.3f}; peak of exact at E_ej/E_B = "
              f"{E[np.argmax(ex)]:.3g}; fraction of exact rate below edge = "
              f"{np.trapezoid(ex[ok & (E <= edge)], np.log(E[ok & (E <= edge)])) / tot[0]:.3f}")
    r = pf[ok] / ex[ok]
    ax2.semilogx(E[ok], r, "C3", lw=1.2, ls=ls, label=rf"$\times$ Fermi, $m_\chi = $ {lab}")
    ax2.semilogx(E[ok], pw[ok] / ex[ok], "C0", lw=1.0, ls=ls if ls != "-" else ":",
                 label=rf"plane wave, $m_\chi = $ {lab}")
    for e0 in (1e-3, 0.1, 1.0, 10.0):
        i = np.argmin(abs(E - e0))
        if ok[i]:
            print(f"  m_chi = {lab}, E_ej/E_B = {e0:g}: PWxF/exact = {pf[i] / ex[i]:.3f}, PW/exact = {pw[i] / ex[i]:.3f}")
for ax in (ax1, ax2):
    ax.axvspan(E[0], edge, color="0.88", lw=0)
ax2.axhline(1.0, color="0.6", lw=0.6)
ax1.set_ylim(1e-4, 3)
ax1.set_ylabel(r"$\mathrm{d}\langle\sigma v\rangle/\mathrm{d}\ln E_{\mathrm{ej}}$ (scaled)")
ax1.legend(fontsize=7, frameon=False, loc="lower left")
ax2.set_ylim(0, 1.45)
ax2.set_xlim(E[0], E[-1])
ax2.set_xlabel(r"$E_{\mathrm{ej}}/E_B$")
ax2.set_ylabel("ratio to exact")
ax2.legend(fontsize=6.5, frameon=False, loc="upper right", ncol=2)
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch02",
                   "limit2_ionization.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
