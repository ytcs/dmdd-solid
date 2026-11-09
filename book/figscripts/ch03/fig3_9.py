"""Fig. 3.9: all-electron and pseudo valence orbitals of the silicon atom, in position and in momentum (Sect. 3.5).
Output: tex/figures/ch03/fig3_9.pdf. Prints the numbers quoted in Sect. 3.5 and in worked example we:3-Ecut.

Calculation (inputs and outputs in ld1/si_nc.*): ld1.x (Quantum ESPRESSO 7.6 atomic code), PBE, scalar-relativistic,
reference configuration [Ne]3s2 3p2. A single-projector norm-conserving pseudopotential is generated for this figure with
the Troullier-Martins construction at the core radii of the SG15 silicon potential of App. E.1/E.2 (s: 2.40, p: 3.56 bohr
requested; ld1.x places them on its grid at 2.425 and 3.529 bohr), local part from the smoothed all-electron potential
inside 2.40 bohr. Modelling choice: the SG15 file itself (Hamann's optimized form, two projectors per channel) cannot be
read by ld1.x ("mesh not supported"), so the pseudo-orbitals shown are those of this TM potential with the same radii,
not of SG15. The pseudo eigenvalues reproduce the all-electron ones (3s -0.79473 Ry, 3p -0.29996 vs -0.29997 Ry; si_nc.out).
File ld1/si_ncps.wfc columns: r, 3S (pseudo), 3P (pseudo), 3S (all-electron), 3P (all-electron), u = rR in bohr^-1/2.

Momentum amplitude: phi(p) = sqrt(2/pi) int dr r u(r) j_l(p r), normalized to int p^2 phi^2 dp = 1.
Numerical floor: the pseudo 3s tail (1.4e-8 per keV at 30 keV) is stable under dr halving and rmax 15-25 bohr; the
pseudo 3p tail below ~1e-8 per keV is not (it changes with rmax), so the text quotes only bounds (< 1e-7 of the weight above 30 keV).
Units: 1 bohr = 0.529177 Angstrom; 1 bohr^-1 = alpha m_e = 3.72894 keV. k_cut at 60 Ry = sqrt(60) bohr^-1 = 28.9 keV.
"""
import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_9.pdf")
AU_KEV = 3.72894
BOHR_A = 0.529177
RC = {"3S": 2.425, "3P": 3.529}   # bohr, as placed by ld1.x (si_nc.out)

d = np.loadtxt(os.path.join(HERE, "ld1", "si_ncps.wfc"))
r = d[:, 0]
ps = {"3S": d[:, 1], "3P": d[:, 2]}
ae = {"3S": d[:, 3], "3P": d[:, 4]}
# fix the overall sign of each orbital so that it is positive at large r
for dct in (ps, ae):
    for h in dct:
        i = np.argmin(np.abs(r - 5.0))
        dct[h] = dct[h] * np.sign(dct[h][i])


def momentum(u, l, p, rmax=25.0, dr=2e-4):
    sp = CubicSpline(r, u)
    x = np.arange(dr, rmax, dr)
    ux = np.where(x >= r[0], sp(x), u[0] * (x / r[0]) ** (l + 1))
    return np.array([np.sqrt(2 / np.pi) * np.trapezoid(x * ux * spherical_jn(l, pp * x), x) for pp in p])


p = np.logspace(np.log10(0.1 / AU_KEV), np.log10(120 / AU_KEV), 420)
mom = {}
for h, l in (("3S", 0), ("3P", 1)):
    for lab, src in (("AE", ae), ("PS", ps)):
        ph = momentum(src[h], l, p)
        dens = p ** 2 * ph ** 2
        mom[(h, lab)] = dens / AU_KEV   # per keV
        norm_r = np.trapezoid(src[h] ** 2, r)
        rc = RC[h]
        inside = np.trapezoid(src[h][r <= rc] ** 2, r[r <= rc])
        print(f"{h} {lab}: int u^2 = {norm_r:.5f}; charge inside r_c = {rc} bohr: {inside:.5f}; "
              f"momentum norm {np.trapezoid(dens, p):.5f}")
pk = p * AU_KEV
for h in ("3S", "3P"):
    for q in (5.0, 10.0, 20.0, 30.0, 40.0):
        m = pk >= q
        fa = np.trapezoid(mom[(h, "AE")][m], pk[m])
        fp = np.trapezoid(mom[(h, "PS")][m], pk[m])
        print(f"{h}: weight above {q:4.0f} keV: AE {fa:.2e}, PS {fp:.2e}, ratio AE/PS {fa / fp:.3g}")
    for q in (10.0, 30.0):
        i = np.argmin(np.abs(pk - q))
        print(f"{h}: density at {q} keV: AE {mom[(h, 'AE')][i]:.3e}, PS {mom[(h, 'PS')][i]:.3e} per keV, "
              f"ratio {mom[(h, 'AE')][i] / mom[(h, 'PS')][i]:.3g}")
    # momentum at which AE and PS densities first differ by 10 %
    rel = np.abs(mom[(h, "AE")] - mom[(h, "PS")]) / mom[(h, "AE")]
    j = np.where((rel > 0.1) & (pk > 1.0))[0][0]
    print(f"{h}: AE and PS momentum densities differ by >10 % from p = {pk[j]:.2f} keV")

plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.4, 2.9), gridspec_kw={"wspace": 0.32})
cols = {"3S": "C0", "3P": "C3"}
ra = r * BOHR_A
for h in ("3S", "3P"):
    ax.plot(ra, ae[h], color=cols[h], lw=1.1, label=f"{h[0]}{h[1].lower()} all-electron")
    ax.plot(ra, ps[h], color=cols[h], lw=1.1, ls="--", label=f"{h[0]}{h[1].lower()} pseudo")
    ax.axvline(RC[h] * BOHR_A, color=cols[h], lw=0.6, ls=":")
    ax.text(RC[h] * BOHR_A + 0.03, -0.62, rf"$r_c^{{{h[1].lower()}}}$", color=cols[h], fontsize=8)
ax.axhline(0, color="0.6", lw=0.5)
ax.set_xlim(0, 3.5)
ax.set_ylim(-0.7, 1.0)
ax.set_xlabel(r"$r$ ($\mathrm{\AA}$)")
ax.set_ylabel(r"$u(r) = rR(r)$ (bohr$^{-1/2}$)")
ax.set_title("(a)", fontsize=9, loc="left")
ax.legend(loc="upper right", fontsize=6.8, frameon=False, handlelength=1.8)

for h in ("3S", "3P"):
    bx.loglog(pk, mom[(h, "AE")], color=cols[h], lw=1.1)
    bx.loglog(pk, mom[(h, "PS")], color=cols[h], lw=1.1, ls="--")
bx.axvline(np.sqrt(60) * AU_KEV, color="0.5", lw=0.6, ls=":")
bx.text(np.sqrt(60) * AU_KEV * 1.06, 2e-1, r"$k_{\mathrm{cut}}$ at 60 Ry", color="0.4", fontsize=7, rotation=90, va="top")
bx.set_xlim(0.3, 120)
bx.set_ylim(1e-8, 1)   # pseudo 3p values below ~1e-8 depend on the integration range (rmax); not resolved
bx.set_xlabel(r"momentum $p$ (keV)")
bx.set_ylabel(r"$p^2|\phi(p)|^2$ (keV$^{-1}$)")
bx.set_title("(b)", fontsize=9, loc="left")
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
