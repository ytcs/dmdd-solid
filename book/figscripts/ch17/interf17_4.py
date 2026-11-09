"""Fig. 17.4 (fig:17-interference) and every number of Sect. 17.4 and its worked example (we:17-gaas-interference).

Numbers (printed to interf17_4.log):
  * mass ratios m_e/M and Z m_e/M for Si and GaAs; the leading-order cross term 2 Z m_e / M of the electronic sectors for
    a dark photon (eq:8.3-boostward applied to every electronic final state, Sect. 17.4), and its square (the summed
    nuclear term relative to the electron term).
  * GaAs: Z/M of Ga and As, their mean and the spread of 2 m_e Z/M (the sublattice weights of the summed amplitude are
    not known; with both weights in [0, 1] the cross term lies between the two single-species values).
  * electron-following (Born-charge) cell for a dark photon at long wavelength: bare nuclear charge Z, following charge
    F = Z - Z* (Sect. 8.6, eq:12.5-cross: 14 for Si, 28.9 Ga, 35.1 As with |Z*| = 2.11 of Sect. 5.5), separate terms
    Z^2 + F^2, cross term -2 Z F, total Z*^2; cancelled fraction 2 Z F / (Z^2 + F^2).
  * window momenta as fractions of 2 pi / a (Si 0.9-1.3 keV, Sect. 13.3; GaAs q* = 1.15 keV, Sect. 13.1) and the
    smallest momentum transfer that deposits the gap, E_g / v_max.
  * radius q_BZ of the sphere with the volume of the Brillouin zone, (6 pi^2 / Omega)^(1/3) (Si 2.25 keV as in 11.1).

Figure: the (q, omega) plane of (a) silicon and (b) GaAs near the gap, for scattering.
  Si: E_g = 1.17 eV (Sect. 3.3), k_c = 0.85 (2 pi / a), a = 5.431 A; zero-phonon edge of the parabolic valleys along
      [100], E_g + (q - K)^2 / 2 M_eh with M_eh = m_l + m_hh[100] = 0.916 + 0.277 = 1.193 m_e (Table 3.1; the model of
      Sect. 13.1, which lies 0.13 eV above the computed bands at 1 keV) and K = k_c and its images under (2,0,0) 2pi/a
      (4 pi / a - k_c, k_c + 4 pi / a); phonon-assisted threshold E_g + omega_TA(k_c - q) along [100] (the book's PBE force
      constants, figscripts/ch05/si_ifc.py); off-shell window margin delta_w = 0.3 eV (Sect. 13.6).
  GaAs: E_g = 1.52 eV; Gamma pair with the [111] heavy hole, M_eh = 0.067 + 0.893 = 0.960 m_e (Table 3.1, Vurgaftman 2001
      as tabulated there); L valleys 1.815 eV at |Gamma L| = sqrt(3) pi / a, X valleys 1.981 eV at 2 pi / a (a = 5.653 A);
      phonon-assisted threshold E_g + omega_TA with omega_TA <= 10.5 meV (computed TA at X, Table 5.x, an upper value).
  Both: largest deposit q v_max - q^2 / 2 m_chi for the masses shown, and the envelope q v_max (m_chi -> infinity),
      v_max = 794.5 km/s (Sect. 1.2).
  These are kinematic and band-edge curves; no rate is drawn.
Run: python interf17_4.py  (numpy, matplotlib; a few seconds). Output: tex/figures/ch17/fig17_4.pdf and interf17_4.log.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc  # noqa: E402

LOG = open(os.path.join(HERE, "interf17_4.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804           # eV A
ME_MEV = 0.51099895           # MeV
U_MEV = 931.49410242          # MeV (atomic mass unit)
ME_U = ME_MEV / U_MEV         # electron mass in u
VMAX = 794.5 / 299792.458

# ------------------------------------------------------------------ mass ratios and cross terms
out("m_e = %.6e u" % ME_U)
M_SI, Z_SI = 28.0855, 14
r_si = ME_U / M_SI
out("Si: M = %.4f u, m_e/M = %.4e, (m_e/M)^2 = %.3e" % (M_SI, r_si, r_si ** 2))
out("Si: Z m_e/M = %.4e; dark photon cross term 2 Z m_e/M = %.4e; summed nuclear term (Z m_e/M)^2 = %.3e"
    % (Z_SI * r_si, 2 * Z_SI * r_si, (Z_SI * r_si) ** 2))
out("Si: rate factor (1 + Z m_e/M)^2 - 1 = %.4e" % ((1 + Z_SI * r_si) ** 2 - 1))
out("Si: M/m_e = %.0f; m_u/m_e = %.1f" % (1 / r_si, 1 / ME_U))

M_GA, Z_GA = 69.723, 31
M_AS, Z_AS = 74.9216, 33
zga, zas = Z_GA / M_GA, Z_AS / M_AS
zbar = 0.5 * (zga + zas)
out("GaAs: Z/M Ga = %.6f /u, As = %.6f /u, mean %.6f /u; relative difference %.4f"
    % (zga, zas, zbar, (zga - zas) / zbar))
out("GaAs: 2 m_e Z/M: Ga %.4e, As %.4e, mean %.4e" % (2 * ME_U * zga, 2 * ME_U * zas, 2 * ME_U * zbar))
out("GaAs: (m_e Z/M)^2 at the mean: %.3e" % ((ME_U * zbar) ** 2))
out("GaAs: deviation of Z/M from the mean, (Z/M - zbar)/zbar = +-%.4f" % ((zga - zbar) / zbar))

# ------------------------------------------------------------------ electron-following (Born-charge) cell
ZSTAR = 2.11
out("Electron-following cell, dark photon, long wavelength (charge seen = Z - F, F = Z - Z*):")
for name, Z, zs in (("Si", 14, 0.0), ("Ga", 31, ZSTAR), ("As", 33, -ZSTAR)):
    F = Z - zs
    sep = Z ** 2 + F ** 2
    cross = -2 * Z * F
    out("  %s: Z = %d, Z* = %+.2f, F = %.2f; Z^2 = %.1f, F^2 = %.2f, cross = %.2f, total = %.3f (Z*^2 = %.3f); "
        "cancelled fraction of Z^2 + F^2 = %.5f; total/Z^2 = %.3e"
        % (name, Z, zs, F, Z ** 2, F ** 2, cross, sep + cross, zs ** 2, -cross / sep, (sep + cross) / Z ** 2))
    if zs != 0:
        out("     bare-nucleus term over total, Z^2/Z*^2 = %.1f" % (Z ** 2 / zs ** 2))

# ------------------------------------------------------------------ momentum scales
for name, a, eg, qwin in (("Si", 5.431, 1.17, (900.0, 1300.0)), ("GaAs", 5.653, 1.52, (1150.0, 1150.0))):
    g1 = 2 * np.pi * HBARC / a
    omega_cell = a ** 3 / 4
    qbz = (6 * np.pi ** 2 / omega_cell) ** (1 / 3) * HBARC
    out("%s: 2pi/a = %.0f eV; q_BZ = %.0f eV; E_g/v_max = %.0f eV = %.3f (2pi/a); window q = %.0f-%.0f eV = %.2f-%.2f (2pi/a)"
        % (name, g1, qbz, eg / VMAX, eg / VMAX / g1, qwin[0], qwin[1], qwin[0] / g1, qwin[1] / g1))

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.size": 8.5, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.0))

# silicon
A_SI = 5.431
G1 = 2 * np.pi * HBARC / A_SI
KC = 0.85 * G1
EG = 1.17
MEH = 1.193 * ME_MEV * 1e6
DW = 0.3
q = np.linspace(50.0, 4000.0, 2000)
Ks = np.array([KC, 2 * G1 - KC, KC + 2 * G1])
emin = EG + np.min((q[:, None] - Ks[None, :]) ** 2, axis=1) / (2 * MEH)
Qx = np.abs(KC - q) / G1
Qx = np.minimum(Qx, 1.0)
wTA = si_ifc.phonons(np.column_stack([Qx, 0 * Qx, 0 * Qx]))[0][:, 0] / 1e3
eth = EG + wTA
out("Si figure: TA(k_c - q) at q = 900 eV: %.2f meV; E_min(900 eV) parabolic = %.3f eV; images K = %s eV"
    % (np.interp(900, q, wTA) * 1e3, np.interp(900, q, emin), np.array2string(Ks, precision=0)))

ax = axs[0]
top = 2.6
kin = q * VMAX
ax.fill_between(q, eth, np.minimum(emin - DW, top), where=(emin - DW > eth), color="C1", alpha=0.35, lw=0)
ax.fill_between(q, np.maximum(emin, eth), top, color="C0", alpha=0.12, lw=0)
ax.fill_between(q, np.minimum(kin, top), top, where=kin < top, color="0.85", lw=0)
ax.plot(q, emin, "C0", lw=1.2)
ax.plot(q, emin - DW, "C0--", lw=0.8)
ax.plot(q, eth, "C1", lw=1.0)
ax.plot(q, kin, "k:", lw=0.9)
for m in (0.34, 0.40, 0.50):
    mm = m * 1e6
    ax.plot(q, q * VMAX - q ** 2 / (2 * mm), color="0.35", lw=0.6)
    j = np.argmax(q * VMAX - q ** 2 / (2 * mm))
    ax.text(q[j], (q * VMAX - q ** 2 / (2 * mm))[j] + 0.03, "%.2f" % m, fontsize=6.5, ha="center", color="0.3")
qbz_si = (6 * np.pi ** 2 / (A_SI ** 3 / 4)) ** (1 / 3) * HBARC
ax.axvline(qbz_si, color="0.5", lw=0.6, ls="-.")
ax.set_xlim(0, 4000)
ax.set_ylim(1.0, top)
ax.set_xlabel(r"$|\boldsymbol{q}|$ (eV)")
ax.set_ylabel(r"$\omega$ (eV)")
ax.set_title("(a) Si", fontsize=8.5, loc="left")
ax.text(3330, 1.33, "window", fontsize=7, color="C1")
ax.text(2500, 2.3, "zero-phonon\nand sideband", fontsize=7, color="C0", ha="center")
ax.text(50, 2.35, "no\nscattering", fontsize=7, color="0.4")
ax.text(qbz_si + 40, 1.05, r"$q_{\mathrm{BZ}}$", fontsize=7, color="0.4")
sec = ax.secondary_xaxis("top", functions=(lambda x: x / G1, lambda y: y * G1))
sec.set_xlabel(r"$|\boldsymbol{q}|/(2\pi/a)$", fontsize=7.5)

# GaAs
A_GA = 5.653
G1g = 2 * np.pi * HBARC / A_GA
EGg = 1.52
MEHg = 0.960 * ME_MEV * 1e6
q2 = np.linspace(50.0, 4000.0, 2000)
emin_g = EGg + q2 ** 2 / (2 * MEHg)
eth_g = EGg + 0.0105
qL, EL = np.sqrt(3) * np.pi * HBARC / A_GA, 1.815
qX, EX = G1g, 1.981
out("GaAs figure: |Gamma L| = %.0f eV (E_L = %.3f eV), |Gamma X| = %.0f eV (E_X = %.3f eV); Gamma-pair edge at q* = 1150 eV: "
    "%.3f eV above the gap" % (qL, EL, qX, EX, 1150.0 ** 2 / (2 * MEHg)))
ax = axs[1]
top2 = 3.0
kin2 = q2 * VMAX
upper = np.minimum(np.minimum(emin_g, top2), EL + 0 * q2)
ax.fill_between(q2, eth_g, upper, where=upper > eth_g, color="C1", alpha=0.35, lw=0)
ax.fill_between(q2, np.minimum(emin_g, EL), top2, color="C0", alpha=0.12, lw=0)
ax.fill_between(q2, np.minimum(kin2, top2), top2, where=kin2 < top2, color="0.85", lw=0)
ax.plot(q2, emin_g, "C0", lw=1.2)
ax.axhline(eth_g, color="C1", lw=1.0)
ax.axhline(EL, color="C0", lw=0.6, ls="--")
ax.plot([qL], [EL], "o", color="C0", ms=3)
ax.plot([qX], [EX], "s", color="C0", ms=3)
ax.text(qL + 60, EL + 0.04, "L", fontsize=7, color="C0")
ax.text(qX + 60, EX + 0.04, "X", fontsize=7, color="C0")
ax.plot(q2, kin2, "k:", lw=0.9)
for m in (0.45, 0.52, 0.70):
    mm = m * 1e6
    y = q2 * VMAX - q2 ** 2 / (2 * mm)
    ax.plot(q2, y, color="0.35", lw=0.6)
    j = np.argmax(y)
    dx = 130.0 if abs(q2[j] - 1150.0) < 150.0 else 0.0   # keep the 0.45 label clear of the q* line
    ax.text(q2[j] + dx, y[j] + 0.03, "%.2f" % m, fontsize=6.5, ha="center", color="0.3")
ax.axvline(1150.0, color="C3", lw=0.6, ls=":")
ax.text(1210, 2.62, r"$q^*$", fontsize=7, color="C3")
qbz_g = (6 * np.pi ** 2 / (A_GA ** 3 / 4)) ** (1 / 3) * HBARC
ax.axvline(qbz_g, color="0.5", lw=0.6, ls="-.")
ax.text(qbz_g + 40, 1.45, r"$q_{\mathrm{BZ}}$", fontsize=7, color="0.4")
ax.set_xlim(0, 4000)
ax.set_ylim(1.4, top2)
ax.set_xlabel(r"$|\boldsymbol{q}|$ (eV)")
ax.set_title("(b) GaAs", fontsize=8.5, loc="left")
ax.text(2400, 1.60, "phonon-assisted only", fontsize=7, color="C1", ha="center",
        bbox=dict(fc="#ffd2ab", ec="none", pad=0.4))   # band colour: keeps the q_BZ line out of the text
ax.text(50, 2.75, "no\nscattering", fontsize=7, color="0.4")
sec2 = ax.secondary_xaxis("top", functions=(lambda x: x / G1g, lambda y: y * G1g))
sec2.set_xlabel(r"$|\boldsymbol{q}|/(2\pi/a)$", fontsize=7.5)

fig.tight_layout()
outpdf = os.path.join(HERE, "..", "..", "tex", "figures", "ch17", "fig17_4.pdf")
fig.savefig(outpdf)
out("wrote", os.path.relpath(outpdf, HERE))
LOG.close()
