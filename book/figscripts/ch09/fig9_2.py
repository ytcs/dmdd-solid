"""Fig. 9.2 (fig:9-qomega) of Sect. 9.3: the excitations of silicon on the (q, omega) plane, by sector, on the axes of
Fig. 1.5 (log q from 1 eV to 2 MeV, log omega from 1e-6 to 1e3 eV), with the reach of elastic dark matter of 0.3, 1 and
10 MeV. Prints every number quoted in Sect. 9.3 and Worked Example 9.3 to fig9_2.log.

Cached inputs (no new first-principles run):
  figscripts/ch05/fig5_2_data.npz  PBE phonon dispersion (QE, DFPT, a = 5.431 A, natural Si 28.0855 u; Sect. 5.2) on the
                                   path Gamma-X along [001] (indices 0-60, q in units of 2pi/a, frequencies in cm^-1) and
                                   the phonon density of states (48^3 grid, 0.25 cm^-1 bins, 6 modes per cell).
  figscripts/ch05/si_ifc.py        the same force constants, for omega_TA at the phonon wavevector of the
                                   phonon-assisted onset (as fig13_6.py).
  figscripts/ch03/qe_si_pbe.npz    E_min(q) along [100], [110], [111] from the PBE bands of Fig. 3.6 (48^3 grid, no
                                   spin-orbit coupling); conduction bands shifted by 0.613 eV so that the indirect gap is
                                   the measured E_g(0) = 1.17 eV (as Figs. 3.6, 13.1, 13.6).
  figscripts/ch10/si_elf_binned.npz the random-phase loss function of silicon with local fields of Knapen, Kozaczuk and
                                   Lin (arXiv:2101.08275, DarkELF tables; scissor gap 1.11 eV), averaged over directions
                                   in 100 eV bins of |q| from 0.49 to 22.5 keV (Sect. 10.2).
Book values used (with their home sections):
  v_max = (544 + 250.5) km/s = 2.650e-3 (Sect. 1.2); a = 5.431 A; k_c = 0.85 (2pi/a) = 1.94 keV (Sect. 3.3);
  E_g(0) = 1.17 eV (Sect. 3.3); delta_w = 0.3 eV (Sect. 13.6); q_BZ = (6 pi^2/Omega)^(1/3) = 2.25 keV (Sect. 11.1);
  omega_p = 16.6 eV, k_F = 3.57 keV (valence gas, r_s = 2; Sects. 4.5, 10.3), quadratic plasmon dispersion
  omega_pl^2 = omega_p^2 + (3/5) q^2 v_F^2 up to its cutoff 2.24 keV (Sect. 10.3); measured loss peak 16.4 eV
  (Sect. 10.3); Si 2p binding 99.4 eV (Sect. 3.5); impulse onset x_R = 4 at 92.5 keV (Sect. 11.4); end of the
  one-phonon regime 10 keV (Sect. 8.5); exciton binding 14.7 meV (Sect. 10.5); Migdal moment estimate
  P_Mig ~ (E_R/<omega_e>) (dM/M) with dM/M = 2.7e-4 and <omega_e> ~ 6 eV (Sect. 12.1).
Modelling choices (stated in the caption):
  * lattice band: incoherent harmonic response at T = 0 (Sect. 11.3) from the PBE density of states,
    S(q, omega) = sum_n Poisson(n; 2W) p1^{*n}(omega), p1 ~ g(omega)/omega, 2W = q^2 <u_x^2>; drawn from q_BZ to the
    impulse onset as the band holding the central 90 % of the weight that creates phonons (5 % and 95 % quantiles);
    above the onset the impulse Gaussian (Sect. 11.4) with mean E_R and width sigma = (E_R <omega>)^(1/2), same quantiles.
    Inside the zone the coherent branches along [100] are drawn instead.
  * pair continuum lower edge: the minimum over the three directions of E_min(q) for |q| <= 6.46 keV (end of the [110]
    data; [100] and [111] continued periodically with |G_200| = 4.57 keV and |G_111| = 3.95 keV), and E_g beyond, where
    some direction of q lies near a valley image k_c + G (gap between image radii logged below).
  * loss function shown as a gray scale where L > 1e-3 (its own maximum is 3.7).
Run: python fig9_2.py (a few seconds). Output: tex/figures/ch09/fig9_2.pdf, fig9_2.log.
"""
import os
import sys
import itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc                                   # noqa: E402

LOG = open(os.path.join(HERE, "fig9_2.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804            # eV A
ME = 510998.95                 # eV
U = 931.49410242e6             # eV
M = 28.0855 * U                # natural Si
VMAX = (544.0 + 250.5) / 299792.458
A = 5.431
G1 = 2 * np.pi * HBARC / A     # 2pi/a = 2283 eV
KC = 0.85 * G1
KC2 = 2 * G1 - KC
EG = 1.17
DW = 0.3
SCIS = 0.613
QBZ = (6 * np.pi ** 2 / (A ** 3 / 4)) ** (1 / 3) * HBARC
CM1 = 1.23984198e-4            # eV per cm^-1
OMP, KF = 16.6, 3570.0
VF = KF / ME
E2P = 99.4
QIMP = 92.5e3
Q1PH = 10.0e3
EXB = 0.0147
out(f"2pi/a = {G1:.1f} eV, k_c = {KC:.0f} eV, q_BZ = {QBZ:.0f} eV, v_max = {VMAX:.4e}, M = {M / 1e9:.3f} GeV")

# ---------------- phonons -----------------------------------------------------------------------------------------
ph = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
qpath = ph["q"][:61, 2] * G1                     # Gamma -> X along [001], eV
fpath = ph["f"][:61] * CM1                       # eV
out(f"phonons: optical at Gamma {fpath[0, 5] * 1e3:.1f} meV; TA, LA at X {fpath[60, 0] * 1e3:.1f}, "
    f"{fpath[60, 2] * 1e3:.1f} meV (PBE)")
dos = ph["dos"]
w_dos = dos[:, 0] * CM1
g = dos[:, 1] / np.trapezoid(dos[:, 1], w_dos)   # normalized to one per eV
pos = w_dos > 0
ux2 = np.trapezoid(g[pos] / w_dos[pos], w_dos[pos]) / (2 * M) * HBARC ** 2   # A^2, per Cartesian direction
wmean = np.trapezoid(g * w_dos, w_dos)
out(f"from the PBE DOS: <u_x^2> = {ux2:.3e} A^2 (Sect. 11.4: 2.45e-3), <omega> = {wmean * 1e3:.1f} meV (Sect. 8.5: 40.9)")


def twoW(q):
    return (q / HBARC) ** 2 * ux2


for qq in (5e3, 10e3, 40e3):
    out(f"2W at {qq / 1e3:g} keV = {twoW(qq):.4f}; E_R = {qq ** 2 / (2 * M) * 1e3:.3f} meV")

# incoherent multiphonon band by FFT of the compound Poisson law
dw_bin = 0.25 * CM1
NB = 2 ** 16
wgrid = np.arange(NB) * dw_bin
p1 = np.zeros(NB)
p1[: len(w_dos)] = np.where(pos, g / np.where(pos, w_dos, 1), 0.0)
p1 /= p1.sum()
p1hat = np.fft.rfft(p1)


def quantiles(q, lo=0.05, hi=0.95):
    t = twoW(q)
    spec = np.fft.irfft(np.exp(t * (p1hat - 1.0)), NB)
    spec[0] -= np.exp(-t)                        # remove the zero-phonon line
    spec = np.clip(spec, 0, None)
    c = np.cumsum(spec) / spec.sum()
    return np.interp(lo, c, wgrid), np.interp(hi, c, wgrid), 1 - np.exp(-t) - t * np.exp(-t)


qlat = np.geomspace(QBZ, QIMP, 120)
band = np.array([quantiles(qq)[:2] for qq in qlat])
for qq in (QBZ, 10e3, 46e3, QIMP):
    lo_, hi_, n2 = quantiles(qq)
    out(f"lattice band at {qq / 1e3:.2f} keV: 5-95 % of phonon-creating weight {lo_ * 1e3:.1f} - {hi_ * 1e3:.1f} meV; "
        f"probability of two or more phonons {n2:.3e}")
qimp = np.geomspace(QIMP, 2e6, 200)
ER = qimp ** 2 / (2 * M)
sig = np.sqrt(ER * wmean)
imp_lo, imp_hi = ER - 1.645 * sig, ER + 1.645 * sig
out(f"impulse Gaussian at 92.5 keV: {imp_lo[0] * 1e3:.1f} - {imp_hi[0] * 1e3:.1f} meV (E_R {ER[0] * 1e3:.1f} meV)")
qx = np.sqrt(2 * M * EG)
MU_X = qx / (2 * VMAX)                         # q_max = 2 mu v_max: reduced mass, then m_chi = mu M/(M - mu)
out(f"free recoil E_R reaches E_g = {EG} eV at q = {qx / 1e3:.1f} keV; needs mu >= q/(2 v_max) = "
    f"{MU_X / 1e6:.2f} MeV, i.e. m_chi >= mu M/(M - mu) = {MU_X * M / (M - MU_X) / 1e6:.2f} MeV")
q2 = np.sqrt(2 * M * (EG + 1.645 * np.sqrt(EG * wmean)))   # rough check of where the band's upper edge is
qlo = np.sqrt(2 * M) * (np.sqrt(EG + 0.25 * 1.645 ** 2 * wmean) - 0.5 * 1.645 * np.sqrt(wmean))
out(f"upper 95 % edge of the impulse band reaches E_g at q = {qlo / 1e3:.1f} keV")

# ---------------- pair continuum ----------------------------------------------------------------------------------
d = np.load(os.path.join(HERE, "..", "ch03", "qe_si_pbe.npz"))
G200, G111 = 2 * G1, np.sqrt(3) * G1


def Emin_dir(qq, key, period):
    qg, eg = d["q" + key], d["E" + key] + SCIS
    if period is None:
        return np.where(qq <= qg[-1], np.interp(qq, qg, eg), np.nan)
    return np.interp(np.mod(qq, period), qg, eg)


qe = np.linspace(0, 6457, 2000)
E100 = Emin_dir(qe, "[100]", G200)
E110 = Emin_dir(qe, "[110]", None)
E111 = Emin_dir(qe, "[111]", G111)
Eenv = np.nanmin(np.vstack([E100, E110, E111]), axis=0)
out(f"E_min(0) = {Eenv[0]:.3f} eV; lowest of three directions at q = 1.0 keV: {np.interp(1000, qe, Eenv):.3f} eV")
for qq in (5000.0,):
    out(f"WE: E_min at |q| = {qq / 1e3:g} keV: [100] {Emin_dir(qq, '[100]', G200):.3f} eV "
        f"(q - G_200 = {qq - G200:.0f} eV), [110] {Emin_dir(qq, '[110]', None):.3f} eV, [111] "
        f"{Emin_dir(qq, '[111]', G111):.3f} eV (q - G_111 = {qq - G111:.0f} eV)")
# radii of valley images |k_c + G| (six valleys, G up to |G| < 40 keV)
Gs = np.array([g_ for g_ in itertools.product(range(-12, 13), repeat=3)
               if (g_[0] % 2 == g_[1] % 2 == g_[2] % 2)], float) * G1      # fcc reciprocal lattice (bcc points)
valleys = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float) * KC
rad = np.unique(np.round(np.linalg.norm(Gs[:, None, :] + valleys[None, :, :], axis=2).ravel(), 1))
rad = rad[rad < 30e3]
gaps = np.diff(rad)
sel = rad[:-1] >= 6.4e3
out(f"valley-image radii |k_c + G| between 6.4 and 30 keV: largest gap {gaps[sel].max():.0f} eV; "
    f"nearest radius to 5 keV: {rad[np.argmin(np.abs(rad - 5000))]:.0f} eV")
MEH = (0.916 + 0.277) * ME
out(f"valley-image radii below 6.4 keV (eV): {rad[rad < 6.4e3].round(0)}")
sel2 = qe >= KC
out(f"lowest of the three computed edges for k_c <= |q| <= 6.46 keV: max {np.nanmax(Eenv[sel2]):.3f} eV")
selm = (qe >= 3247) & (qe <= 4961)
out(f"lowest of the three computed edges between the image radii 3.25 and 4.96 keV: max {np.nanmax(Eenv[selm]):.3f} eV "
    f"at q = {qe[selm][np.nanargmax(Eenv[selm])]:.0f} eV (an upper value for the minimum over all directions)")
out(f"parabolic pair energy above E_g at half the largest gap: {(0.5 * gaps[sel].max()) ** 2 / (2 * MEH) * 1e3:.1f} meV "
    f"(pair mass along the axis 1.193 m_e)")

# ---------------- window along [100] (as fig13_6.py) --------------------------------------------------------------
qw = np.linspace(0.0, G200, 4567)
Ew = Emin_dir(qw, "[100]", G200)


def nearest_valley(qq):
    imgs = np.array([KC, KC2, G200 + KC])
    return np.min(np.abs(qq[:, None] - imgs[None, :]), axis=1) / G1


QS = nearest_valley(qw)
wph, _ = si_ifc.phonons(np.column_stack([QS, 0 * QS, 0 * QS]))
EPA = EG + np.clip(wph[:, 0], 0, None) / 1e3
okw = EPA <= Ew - DW
edges = qw[np.where(np.diff(okw.astype(int)) != 0)[0]]
j1 = np.argmin(np.abs(qw - 1000))
out(f"window along [100]: open for |q| <= {edges[0]:.0f} eV and again from {edges[1]:.0f} eV "
    f"(to {edges[2] if len(edges) > 2 else G200:.0f} eV); at 1.0 keV from {EPA[j1]:.4f} to {Ew[j1] - DW:.4f} eV")
out(f"phonon-assisted onset at q -> 0: E_g + omega_TA(k_c) = {EPA[0]:.4f} eV; top of the window there "
    f"{Ew[0] - DW:.3f} eV")

# ---------------- loss function -----------------------------------------------------------------------------------
e = np.load(os.path.join(HERE, "..", "ch10", "si_elf_binned.npz"))
Lq, Lw, L = e["q"], e["omega"], e["lf"]
iq = np.argmin(np.abs(Lq - 5000))
out(f"WE: loss function (RPA+LF, tables) at q = {Lq[iq]:.0f} eV: L(2 eV) = {np.interp(2.0, Lw, L[:, iq]):.3e}, "
    f"maximum over omega {L[:, iq].max():.3f} at {Lw[np.argmax(L[:, iq])]:.1f} eV; first omega with L > 1e-3: "
    f"{Lw[np.argmax(L[:, iq] > 1e-3)]:.2f} eV")
for qq in (500, 1000, 2000):
    k = np.argmin(np.abs(Lq - qq))
    out(f"loss peak at q = {Lq[k]:.0f} eV: {Lw[np.argmax(L[:, k])]:.1f} eV")

# ---------------- reach and worked example ------------------------------------------------------------------------
for m in (0.3e6, 1e6, 10e6):
    wmax = 0.5 * m * VMAX ** 2
    qmax = 2 * m * VMAX
    disc = (m * VMAX) ** 2 - 2 * m * EG
    band_g = (m * VMAX - np.sqrt(disc), m * VMAX + np.sqrt(disc)) if disc > 0 else (np.nan, np.nan)
    out(f"m_chi = {m / 1e6:g} MeV: largest deposit {wmax:.3f} eV at q = {m * VMAX / 1e3:.3f} keV; q <= {qmax / 1e3:.2f} keV;"
        f" 2W at q_max {twoW(qmax):.3f}; reaches E_g = 1.17 eV for q in {band_g[0] / 1e3:.3f}-{band_g[1] / 1e3:.2f} keV")
QPL = 2240.0                                   # end of the quadratic plasmon dispersion (Sect. 10.3)
WPL = np.sqrt(OMP ** 2 + 0.6 * (QPL * VF) ** 2)
out(f"plasmon (quadratic dispersion) ends at {QPL / 1e3:.2f} keV at {WPL:.2f} eV: phase velocity {WPL / QPL:.3e} = "
    f"{WPL / QPL / VMAX:.2f} v_max; q v_max there = {QPL * VMAX:.2f} eV (exact Lindhard zero: q_c = 2.60 keV, "
    f"q_c v_max = {2600 * VMAX:.2f} eV)")
out(f"threshold mass at E_g = 1.17 eV: {2 * EG / VMAX ** 2 / 1e6:.4f} MeV")
q_we, w_we = 5000.0, 2.0
out(f"WE: q v_max = {q_we * VMAX:.3f} eV; m_chi >= q^2/[2(q v_max - omega)] = {q_we ** 2 / (2 * (q_we * VMAX - w_we)) / 1e6:.3f} MeV;"
    f" omega/q = {w_we / q_we:.2e} = {w_we / q_we * 299792.458:.0f} km/s")
for m in (10e6,):
    vm = w_we / q_we + q_we / (2 * m)
    out(f"WE: v_min at m_chi = {m / 1e6:g} MeV = {vm:.3e} = {vm * 299792.458:.0f} km/s")
t5 = twoW(q_we)
ER5 = q_we ** 2 / (2 * M)
out(f"WE: at 5 keV, 2W = {t5:.4f}, E_R = {ER5 * 1e3:.3f} meV; phonons needed for 2 eV: >= {w_we / fpath[0, 5]:.1f}")
WMAXPH = fpath[0, 5]
out(f"WE: phonon-assisted onset at any q lies below E_g + omega_max = {EG + WMAXPH:.3f} eV")
for key, per in (("[100]", G200), ("[110]", None), ("[111]", G111)):
    em = float(Emin_dir(q_we, key, per))
    zone = "zero-phonon open" if w_we >= em else ("edge band" if w_we > em - DW else "window")
    out(f"WE: along {key}: E_min - delta_w = {em - DW:.3f} eV, E_min = {em:.3f} eV -> omega = 2 eV in the {zone}")
rnear = rad[np.argmin(np.abs(rad - q_we))]
out(f"WE: nearest valley image radius {rnear:.0f} eV; parabolic pair energy above E_g at that |q|: "
    f"{(q_we - rnear) ** 2 / (2 * MEH) * 1e3:.1f} meV")
out(f"WE: Migdal moment estimate (E_R/6 eV)(2.7e-4) = {ER5 / 6.0 * 2.7e-4:.1e}")
out(f"WE: the plasmon line ends at 2.24 keV < 5 keV (quadratic dispersion, {WPL:.2f} eV there)")
out(f"WE: [111] margin of the window: E_min - delta_w - omega = {(float(Emin_dir(q_we, '[111]', G111)) - DW - w_we) * 1e3:.0f} meV")

# ---------------- figure ------------------------------------------------------------------------------------------
C_AD, C_0, C_P = "#2a8a3e", "#2166ac", "#d95f02"
fig, ax = plt.subplots(figsize=(6.3, 4.9))
# zero-phonon electronic: loss function and pair continuum
Lm = np.ma.masked_less(L, 1e-3)
qedges = np.concatenate([[Lq[0] - 50], 0.5 * (Lq[1:] + Lq[:-1]), [Lq[-1] + 50]])
wedges = np.concatenate([[1e-3], 0.5 * (Lw[1:] + Lw[:-1]), [Lw[-1] + 0.5]])
ax.pcolormesh(qedges, wedges, Lm, cmap="Greys", norm=LogNorm(1e-3, 4), shading="flat", alpha=0.55, rasterized=True)
qcont = np.geomspace(1, 2e6, 600)
Elow = np.where(qcont <= qe[-1], np.interp(qcont, qe, Eenv), EG)
ax.fill_between(qcont, Elow, 1e3, color=C_0, alpha=0.10, lw=0)
ax.plot(qcont, Elow, color=C_0, lw=1.3)
ax.text(1.5, 4.2, r"pairs: $\omega \geq E_{\mathrm{min}}(\boldsymbol{q})$", color=C_0, fontsize=7)
qpl = np.linspace(1, 2240, 300)
ax.plot(qpl, np.sqrt(OMP ** 2 + 0.6 * (qpl * VF) ** 2), color=C_0, lw=1.6, ls="--")
ax.text(1.5, 22, "plasmon", color=C_0, fontsize=7)
ax.axhline(E2P, color=C_0, lw=0.8, ls="-.")
ax.text(1.5, E2P * 1.15, r"Si $2p$ core", color=C_0, fontsize=7)
# phonon-dressed electronic: the window along [100], the edge band
qw_pl = np.where(qw > 0, qw, 1.0)
ax.fill_between(qw_pl, EPA, Ew - DW, where=okw, color=C_P, alpha=0.75, lw=0)
ax.fill_between(qw_pl, np.maximum(Ew - DW, EPA), Ew, where=Ew > EPA, color="white", alpha=0.9, lw=0)
ax.text(1.5, 0.66, "window: phonon-assisted pairs only", color=C_P, fontsize=7)
ax.axhline(EG, color=C_P, lw=0.7, ls=":")
ax.text(1.2e4, EG * 0.6, r"$E_{\mathrm{g}}$: phonon-assisted and Migdal onsets", color=C_P, fontsize=6.5, zorder=6,
        bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.8))
# electron-following: phonon branches, lattice band, impulse band
qin = np.geomspace(1, QBZ, 300)
for col, lab in ((0, "TA"), (2, "LA")):
    c = fpath[6, col] / qpath[6]               # slope near Gamma from the data
    wcol = np.where(qin < qpath[6], c * qin, np.interp(qin, qpath, fpath[:, col]))
    ax.plot(qin, wcol, color=C_AD, lw=1.0)
ax.plot(qin, np.interp(qin, qpath, fpath[:, 5]), color=C_AD, lw=1.0)
ax.text(1.5, 0.075, "optical phonons", color=C_AD, fontsize=7)
ax.text(30, 2.4e-4, "acoustic phonons", color=C_AD, fontsize=7, rotation=31)
ax.fill_between(qlat, band[:, 0], band[:, 1], color=C_AD, alpha=0.35, lw=0)
ax.fill_between(qimp, np.clip(imp_lo, 1e-6, None), imp_hi, color=C_AD, alpha=0.35, lw=0)
ax.plot(qimp, ER, color=C_AD, lw=0.8, ls="--")
for qq, lab in ((Q1PH, "10 keV"), (QIMP, "92.5 keV")):
    ax.plot([qq, qq], [2e-3, 4e-3], color=C_AD, lw=0.8)
ax.text(2.6e3, 1.3e-3, "one phonon", color=C_AD, fontsize=6.5)
ax.text(1.4e4, 2.5e-3, "multiphonon", color=C_AD, fontsize=6.5)
ax.text(1.6e5, 6e-3, "impulse", color=C_AD, fontsize=6.5)
# reach
for m, ls in ((0.3e6, ":"), (1e6, "--"), (10e6, "-")):
    qq = np.geomspace(1, 2 * m * VMAX, 600)
    ax.plot(qq, qq * VMAX - qq ** 2 / (2 * m), color="k", lw=0.9, ls=ls)
    ax.text(2 * m * VMAX * 0.86, 3e-6, f"{m / 1e6:g} MeV", fontsize=6.5, ha="right", va="bottom", rotation=90)
qq = np.geomspace(1, 2e6, 100)
ax.plot(qq, qq * VMAX, color="0.45", lw=0.6, ls=":")
ax.axvline(QBZ, color="0.5", lw=0.6, ls="-.")
ax.text(QBZ * 1.08, 2e-6, r"$q_{\mathrm{BZ}}$", fontsize=7, color="0.3", rotation=90, va="bottom")
# interference markers (Table of overlap regions)
for (x, y, s) in ((300, 0.012, "1"), (9e3, 7.0, "2"), (500, 1.75, "3"), (1650, 1.33, "4")):
    ax.text(x, y, s, fontsize=6.5, ha="center", va="center",
            bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="k", lw=0.6))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1, 2e6)
ax.set_ylim(1e-6, 1e3)
ax.set_xlabel(r"momentum transfer $q$ [eV]")
ax.set_ylabel(r"energy transfer $\omega$ [eV]")
fig.tight_layout()
outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch09", "fig9_2.pdf")
fig.savefig(outp, dpi=300)
out("wrote", os.path.normpath(outp))
