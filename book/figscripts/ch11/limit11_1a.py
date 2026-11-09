"""Limit 11.1a: long-wavelength acoustic structure factor against the full one-phonon response of silicon.
Output: tex/figures/ch11/limit11_1a.pdf. Prints the numbers quoted in the box, the caption and Appendix F.

Full result (solid): the omega-integrated one-phonon nuclear response per unit mass at T = 0, all six branches,
   int dw S1/rho_T = (pi / 2 m_u^2) sum_nu |sum_kappa e^{i q.tau_kappa} q.e*_{kappa nu}(Q)|^2 e^{-2W(q)} / omega_{Q nu}
(eq:11.1-S1 with c_kappa = A_kappa, M_kappa = A_kappa m_u, two equal atoms per cell), averaged over the directions of q.
   Phonons: PBE force constants of Sect. 5.2 (DFPT, 6^3 grid, a = 5.431 A), Fourier-interpolated by figscripts/ch05/si_ifc.py
   (cell-phase convention: D(q + G) = D(q), so the unreduced q enters only through e^{i q.tau}; Umklapp is automatic).
   Debye-Waller exponent 2W = q^2 <u_x^2>, <u_x^2> = 2.45e-3 A^2 (T = 0, DFPT density of states; WE 5.7).
Long-wavelength formula (dashed, = 1): pi q / m_u^2 sum_nu (q.e_nu)^2 / c_nu (2205.02250 Eq. (30) with Eq. (27), for all
   three acoustic branches), with the PBE sound speeds and polarizations of the same force constants (c_nu from omega at
   |Q| = 0.004 x 2pi/a), so that the ratio tends to one as q -> 0 by construction.
Leading correction (dotted): the long-wavelength eigenvectors with the true acoustic dispersion, sum_nu (q.e_nu)^2 / omega_nu(q)
   in place of sum_nu (q.e_nu)^2/(c_nu q) (acoustic branches at the reduced wavevector; shown for q < q_BZ).
q_BZ = (6 pi^2/Omega)^(1/3) = 1.139 A^-1 = 2.248 keV, Omega = a^3/4.  Directions: Gauss-Legendre 24 x 48 grid (App. C.18).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
sys.path.insert(0, HERE)
import si_ifc  # noqa: E402
import phon11 as P  # noqa: E402

A_ANG = 5.431
TWO_PI_A = 2 * np.pi / A_ANG                      # A^-1 per unit of 2pi/a
UX2 = 2.45e-3                                     # A^2 (WE 5.7)
QBZ = (6 * np.pi**2 / (A_ANG**3 / 4))**(1 / 3)    # A^-1
TAU = si_ifc.TAU                                  # alat units

qh, wq = P.sphere_grid(24, 48)

# long-wavelength speeds and polarizations from the same force constants
eps = 0.004
w0, ev0 = si_ifc.phonons(eps * qh)                # meV, (n,6), (n,6,6)
c_lw = w0[:, :3] / (eps * TWO_PI_A)               # meV A
e_lw = np.zeros((len(qh), 3, 3))
for nu in range(3):
    v = ev0[:, :, nu]
    e = (v[:, 0:3] + v[:, 3:6])                   # acoustic: both atoms move together; e_kappa = ehat / sqrt 2
    e = np.real(e * np.exp(-1j * np.angle(e[np.arange(len(qh)), np.argmax(np.abs(e), 1)]))[:, None])
    e_lw[:, :, nu] = e / np.linalg.norm(e, axis=1)[:, None]
proj2_lw = np.einsum("ni,nik->nk", qh, e_lw)**2
coef_lw = np.sum(wq * (proj2_lw / c_lw).sum(1))   # <sum (q.e)^2 / c>, (meV A)^-1
MEVA_KMS = 1e-13 / 6.582119569e-16 / 1e3          # 1 meV A (per hbar) in km/s
print("PBE long-wave: <sum_nu (q.e)^2> = %.4f; 1/<sum (q.e)^2/c> = %.3f km/s; <c_LA> = %.3f km/s"
      % (np.sum(wq * proj2_lw.sum(1)), MEVA_KMS / coef_lw, MEVA_KMS * np.sum(wq * c_lw[:, 2])))


def full_ratio(qmag):
    """[full omega-integrated one-phonon response] / [long-wavelength formula], direction-averaged, at |q| = qmag (A^-1)."""
    qv = qmag * qh / TWO_PI_A                      # 2pi/a units
    w, ev = si_ifc.phonons(qv)
    w = np.maximum(w, 1e-3)
    ph = np.exp(2j * np.pi * (qv @ TAU.T))         # e^{i q.tau}, (n,2)
    amp = np.zeros((len(qh), 6), complex)
    for k in range(2):
        amp += ph[:, k:k + 1] * np.einsum("ni,nij->nj", qmag * qh, np.conj(ev[:, 3 * k:3 * k + 3, :]))
    full = np.sum(wq * (np.abs(amp)**2 / w).sum(1)) / 2 * np.exp(-qmag**2 * UX2)
    lw = qmag * coef_lw
    # dispersion-only correction: long-wave eigenvectors, acoustic omega at the reduced wavevector
    disp = np.sum(wq * (proj2_lw * qmag**2 / w[:, :3]).sum(1))
    return full / lw, disp / lw


x = np.concatenate([np.linspace(0.02, 0.2, 10), np.linspace(0.22, 1.5, 65)])
R = np.array([full_ratio(xi * QBZ) for xi in x])
for xi, (r, d) in zip(x, R):
    if np.isclose(xi, [0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5], atol=0.011).any():
        print("q/q_BZ = %.2f (q = %.3f keV): full/formula = %.3f, dispersion-only = %.3f" % (xi, xi * QBZ * 1.973269804, r, d))
# 10 % boundary
bad = np.where(np.abs(R[:, 0] - 1) > 0.10)[0]
x10 = x[bad[0]] if len(bad) else np.nan
print("full/formula leaves +-10%% first at q/q_BZ = %.2f (q = %.2f keV)" % (x10, x10 * QBZ * 1.973269804))
bad5 = np.where(np.abs(R[:, 0] - 1) > 0.05)[0]
print("leaves +-5%% at q/q_BZ = %.2f" % x[bad5[0]])
print("2W at q_BZ = %.4f" % (QBZ**2 * UX2))

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.axvspan(0, x10, color="0.88", lw=0)
ax.axhline(1.0, color="k", ls="--", lw=1.0, label="long-wavelength formula")
ax.plot(x, R[:, 0], color="C3", lw=1.5, label="full one-phonon response (PBE)")
m = x <= 1.0
ax.plot(x[m], R[m, 1], color="C0", ls=":", lw=1.4, label="formula with true acoustic dispersion")
ax.axvline(1.0, color="0.5", lw=0.6)
ax.set_xlim(0, 1.5)
ax.set_ylim(0.8, 2.3)
ax.set_xlabel(r"$q/q_{\mathrm{BZ}}$")
ax.set_ylabel(r"$\int\!\mathrm{d}\omega\,S^{(1)}\,/\,$formula")
sec = ax.secondary_xaxis("top", functions=(lambda t: t * QBZ * 1.973269804, lambda k: k / (QBZ * 1.973269804)))
sec.set_xlabel(r"$q$ [keV] (silicon)")
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_1a.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
