"""Limit Check 14.4a (lim:14.4a, Sect. 14.4): the data-driven spin response.
Output tex/figures/ch14/limit14_4a.pdf, log limit14_4a.log.  Run: python limit14_4a.py (seconds).

Literature formula (Berlin, Millar, Trickle, Zhou, arXiv:2504.02927 Eqs. (8), (11), (26)): the neutron structure factor
  per formula unit fixes P_T:S of the spin density, sum_ab (P_T)_ab S_ab = 2 pi N_fu S^neu / ((gamma_n r_cl)^2 Omega),
  with the neutron coupling to the electron spin alone (their App. C: orbital moment quenched, g = 2).
  In the plot: ratio 1 (dark-matter spin response / response inferred from the neutron data).
Fuller result (book, Sect. 14.4): for a quenched ion with spectroscopic g (isotropic) the neutron couples to
  (g/2) F_M(q) S with the moment form factor F_M = <j0> + (1 - 2/g) <j2> (spin part <j0>, induced orbital part
  (g - 2) S with <j0> + <j2>, dipole approximation, App. C.19), while spin-coupled dark matter couples to
  lambda_S <j0> S.  The spin response is
      C(q, g) x [literature],   C = [lambda_S <j0> / ((g/2)(<j0> + (1 - 2/g) <j2>))]^2,
  with lambda_S = 1 (its correction is second order in the orbital admixture, Sect. 14.3).
  At q -> 0: C = 4/g^2 (0.826 at g = 2.2).
Controlling parameter: g - 2 (first order in the spin-orbit admixture).  Curves at q -> 0, q = |Q_AF| = 2.6 keV,
  q = 5.3 keV (largest momentum transfer of a 1 MeV particle, 2 m v_max) and q = 10 keV (dotted, outside the shading
  rule), with the radial integrals of Ni2+.
Shaded: g - 2 for which C stays within 10 % of 1 at all three q.
Markers: g = 2.2, the spectroscopic g of octahedral Ni2+ (Abragam and Bleaney 1970), and g = 2 + L/S = 2.34 with
  L/S = 0.34 from magnetic x-ray diffraction on NiO (Fernandez et al., PRB 57, 7870 (1998), as quoted by Kwon and Min,
  PRB 62, 73 (2000), cond-mat/0003371, p. 1; their LSDA+U with spin-orbit coupling gives 0.36).
Ni2+ radial integrals, Brown's fits (International Tables for Crystallography Vol. C, Sect. 4.4.5; the values
  distributed with the `periodictable` package, checked at run time), s = q/(4 pi) in A^-1:
  <j0> = A e^{-a s^2} + B e^{-b s^2} + C e^{-c s^2} + D, (0.0163, 35.8826, 0.3916, 13.2233, 0.6052, 4.3388, -0.0133);
  <j2> = s^2 [A e^{-a s^2} + B e^{-b s^2} + C e^{-c s^2} + D], (1.7080, 11.016, 1.2147, 4.1030, 0.3150, 1.5330, 0.0018).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_4a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


J0 = (0.0163, 35.8826, 0.3916, 13.2233, 0.6052, 4.3388, -0.0133)
J2 = (1.7080, 11.016, 1.2147, 4.1030, 0.3150, 1.5330, 0.0018)
HBARC_EV_A = 1973.269804      # eV A
VMAX = 794.5 / 299792.458


def fit(c, s2):
    A, a, B, b, C, cc, D = c
    return A * np.exp(-a * s2) + B * np.exp(-b * s2) + C * np.exp(-cc * s2) + D


def j0(q_kev):
    s2 = (q_kev * 1e3 / HBARC_EV_A / (4 * np.pi))**2
    return fit(J0, s2)


def j2(q_kev):
    s2 = (q_kev * 1e3 / HBARC_EV_A / (4 * np.pi))**2
    return s2 * fit(J2, s2)


def conv(q_kev, g, lam=1.0):
    F0, F2 = j0(q_kev), j2(q_kev)
    return (lam * F0 / ((g / 2) * (F0 + (1 - 2 / g) * F2)))**2


try:
    import periodictable as pt
    ff = pt.Ni.magnetic_ff[2]
    ok0 = np.allclose(ff.j0, J0, atol=1e-4)
    ok2 = np.allclose(ff.j2, J2, atol=1e-4)
    out(f"Brown coefficients match periodictable: j0 {ok0}, j2 {ok2}")
except Exception as e:
    out(f"periodictable check skipped: {e}")

qaf = np.sqrt(3) * np.pi / 4.17 * HBARC_EV_A / 1e3     # |Q_AF| = sqrt(3) pi/a in keV
q1 = 2 * 1e6 * VMAX / 1e3                              # 2 m v_max at 1 MeV, keV
out(f"|Q_AF| = {qaf:.2f} keV; 2 m v_max at 1 MeV = {q1:.2f} keV")
for q in (0.0, qaf, q1, 10.0, 15.0):
    out(f"q = {q:5.2f} keV: <j0> = {j0(q):.4f}, <j2> = {j2(q):.4f}, <j2>/<j0> = {j2(q)/j0(q):.4f}")
for g in (2.2, 2.34):
    out(f"g = {g}: C(0) = 4/g^2 = {4/g**2:.4f}; C(|Q_AF|) = {conv(qaf, g):.4f}; C(5.3 keV) = {conv(q1, g):.4f}; "
        f"C(10 keV) = {conv(10.0, g):.4f}")
out(f"g = 2.2 vs 2.34 at q -> 0: {4/2.2**2:.3f} vs {4/2.34**2:.3f}, ratio {(2.2/2.34)**2:.3f}")
out(f"lambda_S = g - 1 (wrong for a quenched ion) at g = 2.2 would give [1.2/1.1]^2 = {(1.2/1.1)**2:.3f} instead of {4/2.2**2:.3f}")

# validity: C within 10 % of 1 at all three q
gm2 = np.linspace(0, 0.45, 2000)
qs = (1e-6, qaf, q1)
Cs = np.array([[conv(q, 2 + d) for d in gm2] for q in qs])
okv = np.all(np.abs(Cs - 1) <= 0.1, axis=0)
gmax = gm2[okv].max()
out(f"C within 10 % of 1 at q -> 0, |Q_AF| and 5.3 keV for g - 2 <= {gmax:.3f}")
# where the constant 4/g^2 holds within 10 % of the full C for g = 2.2
qq = np.linspace(0.01, 20, 4000)
cq = conv(qq, 2.2)
dev = np.abs(cq / (4 / 2.2**2) - 1)
qbad = qq[dev > 0.1]
out(f"g = 2.2: constant 4/g^2 within 10 % of C(q) for q < {qbad.min() if qbad.size else np.inf:.2f} keV")
dev5 = np.abs(cq / (4 / 2.2**2) - 1)
for q in (2.6, 5.3, 8.0, 10.0):
    out(f"   C(q)/C(0) at {q} keV = {conv(q, 2.2)/(4/2.2**2):.4f}")
qz = qq[np.argmax(j0(qq) < 0)] if np.any(j0(qq) < 0) else None
out(f"first zero of <j0> (Ni2+ fit) at q = {qz:.2f} keV" if qz else "no zero of <j0> below 20 keV")

fig, ax = plt.subplots(figsize=(4.6, 3.2))
ax.axvspan(0, gmax, color="0.88", lw=0, zorder=0)
ax.axhline(1, color="k", lw=1.0, label="spin-only neutron coupling (formula)")
ax.plot(gm2, Cs[0], color="C3", lw=1.4, label=r"$q \to 0$: $4/g^2$")
ax.plot(gm2, Cs[1], color="C0", lw=1.2, ls="--", label=rf"$q = |\mathbf{{Q}}_\mathrm{{AF}}| = {qaf:.1f}$ keV")
ax.plot(gm2, Cs[2], color="C2", lw=1.2, ls="-.", label=rf"$q = {q1:.1f}$ keV")
ax.plot(gm2, [conv(10.0, 2 + d) for d in gm2], color="C1", lw=1.0, ls=":", label=r"$q = 10$ keV")
for gv, lab, dy in ((2.2, r"Ni$^{2+}$, $g_{\mathrm{ion}} = 2.2$", 0.03), (2.34, r"NiO, $L/S = 0.34$", 0.03)):
    ax.axvline(gv - 2, color="0.5", lw=0.6, ls=":")
    ax.plot([gv - 2], [4 / gv**2], "s", color="k", ms=4, mfc="w")
    ax.text(gv - 2 + 0.006, 4 / gv**2 + dy, lab, fontsize=6.5, color="0.2")
ax.set_xlim(0, 0.45)
ax.set_ylim(0.55, 1.05)
ax.set_xlabel(r"$g_{\mathrm{ion}} - 2$ (orbital admixture of a quenched ion)")
ax.set_ylabel(r"conversion factor $C_\mathrm{sn}$")
ax.legend(fontsize=6.3, frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_4a.pdf"))
out("wrote", os.path.join(FIG, "limit14_4a.pdf"))
LOG.close()
