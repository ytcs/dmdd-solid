"""Fig. 13.7 (fig:13-window-T) and every number of Sect. 13.7 and its worked example (we:13-windowT).

(a) The indirect gap of silicon from 10 mK to 300 K: the fit E_g(T) = E_g(0) - a T^2/(T + b) to photoluminescence,
    E_g(0) = 1.1692 eV, a = 4.9e-4 eV/K, b = 655 K (Alex et al. 1996, as quoted by Ramanathan and Kurinsky,
    Phys. Rev. D 102, 063026 (2020), Eq. (11); Sect. 6.3), with the envelope of a +- 0.2e-4 eV/K and b +- 40 K (as in fig6_4.py).
    The book's low-temperature gap is the rounded 1.17 eV (Sect. 1.3, 3.3); all edges below use
    E_g(T) = 1.17 eV + Delta E_g(T), Delta E_g(T) = E_g^fit(T) - E_g^fit(0), a rigid shift.
(b) The window edges against temperature:
    * phonon-assisted onset (TA emission) m_min^PA(T) = min_q q^2 / {2 [q v_max - E_g(T) - omega_TA(k_c - q)]}, q along
      [100], with the book's PBE force constants of Sect. 5.2 (figscripts/ch05/si_ifc.py), exactly as fig13_1.py; the
      bound-pair replica with E_g - E_x^b (E_x^b = 14.7 meV, Sect. 4.9);
    * TA-absorption sideband: the same with E_g(T) - omega_TA, weighted by n_B(omega_TA(Q*)) (shown where n_B > 1e-3);
      optical-phonon absorption sideband printed (largest branch at Q*);
    * zero-phonon edge: the established 10 mK values 0.405-0.408 MeV (best 0.407, spin-orbit included) and the 1s line
      0.402-0.405 MeV (state of the art for the silicon window, Sect. 13.9), moved with the gap at the momentum transfer of
      the joint minimum, |q| = 1.33 keV (the off-axis optimum of the joint (q, k) minimization, re-minimized on plane-wave bands with spin-orbit coupling at the measured lattice constant; Sect. 13.9):
      m(Delta) = q^2 / {2 [q v_max - E_0 - Delta E_g]}, E_0 fixed by m(0); the re-minimization over q is second order.
Also printed: d m / d E_g at both edges; the non-adiabatic estimate of the intraband optical term,
    ZPR^na - ZPR^ad = Omega |g_O|^2 (2 m*)^{3/2} sqrt(omega_O) / (4 pi), checked by quadrature, with
    g_O = 0.25 eV (the hole optical vertex of Sect. 13.6), omega_O = 64.1 meV, Omega = a^3/4, a = 5.431 A, and the
    spherical hole masses m_e/(gamma1 -+ 2 gammabar), m_e/gamma1 (Luttinger parameters of Table 3.1: 4.285, 0.339, 1.446);
    the Ponce et al. (1504.05992) decomposition of their Table VI (indirect gap -64.3 adiabatic / -56.2 non-adiabatic meV;
    valence maximum +40.87 / +34.75 meV and conduction minimum -23.28 / -21.43 meV, Sect. VI A 2); the window shifts implied by 8 meV and by a 10 meV variation of
    the renormalization across the reached pair states.
Run: python fig13_7.py (about 15 s). Output: tex/figures/ch13/fig13_7.pdf; numbers in fig13_7.log.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc                                   # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch13")
LOG = open(os.path.join(HERE, "fig13_7.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804
ME = 510998.95
KB = 8.617333e-5
VMAX = 794.5 / 299792.458
V2 = VMAX ** 2
EG0 = 1.17
EXB = 0.0147
A = 5.431
G1 = 2 * np.pi * HBARC / A
KC = 0.85 * G1


def gapfit(T, a=4.9e-4, b=655.0):
    T = np.asarray(T, float)
    return 1.1692 - a * T ** 2 / (T + b)


def dEg(T, **kw):
    return gapfit(T, **kw) - gapfit(0.0, **kw)


def nB(w, T):
    x = w / (KB * T)
    return np.where(x > 700, 0.0, 1.0 / np.expm1(np.minimum(x, 700)))


q = np.linspace(600, 1300, 7001)
Qx = (KC - q) / G1
w, _ = si_ifc.phonons(np.column_stack([Qx, 0 * Qx, 0 * Qx]))
wTA = w[:, 0] / 1e3
wOPT = w[:, 5] / 1e3


def mreq(E):
    ok = q * VMAX > E
    return np.where(ok, q ** 2 / (2 * np.where(ok, q * VMAX - E, 1.0)), np.inf)


def edge(E):
    m = mreq(E)
    j = int(np.argmin(m))
    return m[j] / 1e6, q[j], j


# zero-phonon edge moved at the joint optimum
QZP = 1330.0   # |q| of the joint minimum as printed in Sect. 13.9 (plane-wave bands, spin-orbit, re-minimized at the measured a)


def zp_shift(m0, dE):
    E0 = QZP * VMAX - QZP ** 2 / (2 * m0 * 1e6)
    return QZP ** 2 / (2 * (QZP * VMAX - E0 - dE)) / 1e6


out(f"v_max^2 = {V2:.4e}; 2/v^2 = {2/V2/1e6:.4f} MeV/eV")
for T in (0.01, 1, 4, 10, 20, 50, 77, 100, 150, 200, 300):
    out(f"T = {T:7.2f} K: Delta E_g = {dEg(T)*1e3:9.4f} meV; n_B(14.8 meV) = {nB(0.0148, T):.3e}; n_B(30.4 meV) = {nB(0.0304, T):.3e}")
out(f"envelope at 300 K: Delta E_g from {dEg(300, a=5.1e-4, b=615)*1e3:.2f} to {dEg(300, a=4.7e-4, b=695)*1e3:.2f} meV")

rows = {}
for T in (0.01, 77.0, 300.0):
    Eg = EG0 + dEg(T)
    mPA, qs, j = edge(Eg + wTA)
    mX, _, _ = edge(Eg - EXB + wTA)
    mAbs, qa, ja = edge(Eg - wTA)
    mOpt, qo, jo = edge(Eg - wOPT)
    zp = [zp_shift(m, dEg(T)) for m in (0.405, 0.407, 0.408)]
    x1s = [zp_shift(m, dEg(T)) for m in (0.402, 0.405)]
    rows[T] = (mPA, mX, zp, x1s)
    out(f"T = {T} K: E_g = {Eg:.4f} eV; onset (TA emission) {mPA:.4f} MeV at q* = {qs:.0f} eV, omega_TA(Q*) = {wTA[j]*1e3:.2f} meV, "
        f"|Q*| = {(KC-qs)/G1:.3f} (2pi/a); replica {mX:.4f}; TA absorption sideband {mAbs:.4f} MeV (omega {wTA[ja]*1e3:.2f} meV, "
        f"n_B = {nB(wTA[ja], T):.3e}); optical absorption {mOpt:.4f} MeV (omega {wOPT[jo]*1e3:.2f} meV, n_B = {nB(wOPT[jo], T):.3e}); "
        f"zero-phonon edge {zp[0]:.4f}-{zp[2]:.4f} (best {zp[1]:.4f}); 1s line {x1s[0]:.4f}-{x1s[1]:.4f} MeV")

m0, mT = rows[0.01], rows[300.0]
out(f"WINDOW 10 mK: {m0[0]:.4f} -> {m0[2][1]:.4f} MeV (width {m0[2][1]-m0[0]:.4f}); 300 K: {mT[0]:.4f} -> {mT[2][1]:.4f} "
    f"(width {mT[2][1]-mT[0]:.4f}); onset shift {mT[0]-m0[0]:+.4f}, ZP shift {mT[2][1]-m0[2][1]:+.4f} MeV")
# derivatives
d = 1e-4
dPA = (edge(EG0 + d + wTA)[0] - edge(EG0 - d + wTA)[0]) / (2 * d)
dZP = (zp_shift(0.407, d) - zp_shift(0.407, -d)) / (2 * d)
out(f"dm/dE_g: onset {dPA:.4f} MeV/eV (2/v^2 = {2/V2/1e6:.4f}); zero-phonon edge {dZP:.4f} MeV/eV")
slope300 = -4.9e-4 * 300 * (300 + 2 * 655) / (300 + 655) ** 2
out(f"dE_g/dT at 300 K = {slope300*1e3:.4f} meV/K -> onset {dPA*slope300*1e6:.2f} keV/K = {dPA*slope300:.2e} MeV/K")
for T in (1, 4, 10, 20, 50):
    out(f"  onset shift at {T} K: {dPA*dEg(T):.2e} MeV")
out(f"1 % of omega_TA(Q*) moves the onset by {2*0.01*0.01479/V2/1e6:.1e} MeV")

# ---------------- non-adiabatic estimate ----------------
OM = A ** 3 / 4 / HBARC ** 3          # eV^-3
gO, wO = 0.25, 0.0641
g1, g2, g3 = 4.285, 0.339, 1.446
gbar = (2 * g2 + 3 * g3) / 5
masses = {"heavy": 1 / (g1 - 2 * gbar), "light": 1 / (g1 + 2 * gbar), "third (m_e/gamma1)": 1 / g1}
tot = 0.0
for name, mm in masses.items():
    m = mm * ME
    closed = OM * gO ** 2 * (2 * m) ** 1.5 * np.sqrt(wO) / (4 * np.pi)
    integ = quad(lambda Q: 4 * np.pi * Q ** 2 / (2 * np.pi) ** 3 * (2 * m / Q ** 2 - 1 / (Q ** 2 / (2 * m) + wO)), 0, np.inf,
                 limit=200)[0] * OM * gO ** 2
    tot += closed
    out(f"non-adiabatic intraband optical term, {name} hole m* = {mm:.3f} m_e: closed form {closed*1e3:.3f} meV, quadrature {integ*1e3:.3f} meV")
out(f"  sum over the three degenerate valence bands: {tot*1e3:.2f} meV")
vbm_ad, vbm_na = 40.87, 34.75       # Ponce et al. 1504.05992, Sect. VI A 2 (adiabatic / non-adiabatic, meV)
cbm_ad, cbm_na = -23.28, -21.43
gam_c = -42.1                        # conduction state at Gamma (Gamma_15), non-adiabatic, Table VI
out(f"Ponce Table VI: gap -64.3 / -56.2 meV (difference {64.3-56.2:.1f}); VBM +{vbm_ad} / +{vbm_na} (difference {vbm_ad-vbm_na:.2f}); "
    f"CBM {cbm_ad} / {cbm_na} (difference {cbm_na-cbm_ad:.2f}) meV; sum of the band shifts {(vbm_ad-vbm_na)+(cbm_na-cbm_ad):.2f} meV")
out(f"non-adiabatic renormalization of the conduction state at Gamma relative to the VBM: {gam_c} + {vbm_na} = {gam_c+vbm_na:.2f} meV;"
    f" against the CBM {cbm_na}: variation {gam_c+vbm_na-cbm_na:.1f} meV")
out(f"window: 8 meV on the gap moves the onset by {dPA*0.008:.4f} MeV and the ZP edge by {dZP*0.008:.4f} MeV; "
    f"10 meV variation across the reached states moves the ZP edge by {dZP*0.010:.4f} MeV")

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})
Ts = np.logspace(-2, np.log10(300), 160)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(4.8, 5.0), sharex=True, gridspec_kw={"height_ratios": [1, 1.5]})
lo = np.minimum(dEg(Ts, a=5.1e-4, b=615), dEg(Ts, a=4.7e-4, b=695))
hi = np.maximum(dEg(Ts, a=5.1e-4, b=615), dEg(Ts, a=4.7e-4, b=695))
a1.fill_between(Ts, EG0 + lo, EG0 + hi, color="0.85", lw=0)
a1.plot(Ts, EG0 + dEg(Ts), "k", lw=1.1, label=r"$E_{\mathrm{g}}(T)$")
a1.plot(Ts, EG0 + dEg(Ts) + wTA[edge(EG0 + wTA)[2]], color="tab:red", lw=0.9, ls="--",
        label=r"$E_{\mathrm{g}}(T) + \omega_{\mathrm{TA}}(\mathbf{Q}^*)$")
a1.set_ylabel("energy (eV)")
a1.legend(fontsize=7, frameon=False, loc="lower left")
a1.set_ylim(1.11, 1.195)
pa, xx, ab, zlo, zhi, zb, x1lo, x1hi = [], [], [], [], [], [], [], []
for T in Ts:
    Eg = EG0 + dEg(T)
    pa.append(edge(Eg + wTA)[0]); xx.append(edge(Eg - EXB + wTA)[0])
    mA, _, ja = edge(Eg - wTA)
    ab.append(mA if nB(wTA[ja], T) > 1e-3 else np.nan)
    zlo.append(zp_shift(0.405, dEg(T))); zhi.append(zp_shift(0.408, dEg(T))); zb.append(zp_shift(0.407, dEg(T)))
    x1lo.append(zp_shift(0.402, dEg(T))); x1hi.append(zp_shift(0.405, dEg(T)))
a2.fill_between(Ts, pa, zb, color="tab:red", alpha=0.10, lw=0)
a2.fill_between(Ts, zlo, zhi, color="tab:blue", alpha=0.35, lw=0, label="zero-phonon edge")
a2.plot(Ts, zb, color="tab:blue", lw=0.9)
a2.plot(Ts, x1lo, color="tab:blue", lw=0.6, ls=":", label="zero-phonon $1s$ line (lower end)")
a2.plot(Ts, pa, color="tab:red", lw=1.1, label="phonon-assisted onset (TA emission)")
a2.plot(Ts, xx, color="tab:red", lw=0.7, ls="--", label="bound-pair replica")
a2.plot(Ts, ab, color="tab:orange", lw=0.9, ls="-.", label=r"TA-absorption sideband ($n_{\mathrm{B}} > 10^{-3}$)")
a2.set_xscale("log")
a2.set_xlim(1e-2, 300)
a2.set_ylim(0.305, 0.42)
a2.set_xlabel("temperature $T$ (K)")
a2.set_ylabel(r"$m_\chi$ (MeV)")
a2.text(20, 0.352, "phonon-assisted\nonly", fontsize=7, color="tab:red", ha="center")
a2.legend(fontsize=6.5, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.85))
a1.text(0.012, 1.188, "(a)", fontsize=8); a2.text(0.012, 0.41, "(b)", fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig13_7.pdf"))
out("wrote fig13_7.pdf")
# one-phonon, zero-pair sector of the electron density (eq:13.7-fsum): first moment relative to n_e q^2/2m_e ~ Z_v m_e/M_cell
_ZV, _MCELL = 8, 2 * 28.0855 * 931.49410e6       # valence electrons and mass (eV) of the two-atom cell of Si
out(f"Z_v m_e / M_cell = {_ZV * 510998.95 / _MCELL:.1e}")
