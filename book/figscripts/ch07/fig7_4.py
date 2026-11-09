"""Fig. 7.4 (hydrogenic donor levels in silicon) and every number of Sect. 7.4 on shallow donors, including
worked example "The binding of phosphorus in silicon".  Natural units hbar = c = 1; energies in meV, lengths in A.

Output: tex/figures/ch07/fig7_4.pdf

Inputs and their sources
  Constants (CODATA, as App. D.23): Ry = 13605.693 meV, a0 = 0.529177 A, hbar c = 1973.2698 eV A.
  Silicon valley masses m_perp = 0.191, m_par = 0.916 m_e (Table 3.1, tab:3-materials).
  Dielectric constant eps0 = 11.7 (Sect. 3.3, 4.4, App. D.23; room-temperature value, n = 3.42).
  Low-temperature value eps0 = 11.4, the value used for liquid-helium donor spectra by Faulkner, Phys. Rev. 184, 713
     (1969) and Smith et al., Sci. Rep. 7, 6010 (2017) (arXiv:1612.00569, text after their Eq. (2)).
  Measured donor levels (binding energies, meV; Vinh et al., PNAS 105, 10649 (2008), arXiv:0812.0148, Fig. 1;
     P ground-state triplet as Jagannath, Grabowski and Ramdas, Phys. Rev. B 23, 2082 (1981), quoted also by
     Gamble et al., arXiv:1408.3159):
       Si:P   1s(A1) 45.59, 1s(T2) 33.89, 1s(E) 32.58, 2p0 11.48, 2p+- 6.40, 3p0 5.47
       Si:As  1s(A1) 53.76, 1s(T2) 32.67, 1s(E) 31.26, 2p0 11.50, 2s 9.11, 2p+- 6.40, 3p0 5.49
       Si:Sb  1s(A1) 42.71 (experimental column of Claes et al., arXiv:2508.14738, Table 3)
  Faulkner's effective-mass 1s binding 31.27 meV (quoted by Smith et al., arXiv:1612.00569, p. 1).
  Supercell PBE binding of P, 19.2 meV (Claes et al., arXiv:2508.14738, Table 3 and Fig. 7).
  Kinematics (Sect. 1.3, 3.3): v_max = 2.650e-3, v_max^2 = 7.023e-6.
  Silicon lattice constant a = 5.431 A (Sect. 3.1); atomic density 8/a^3.

Method (named in the caption and the text)
  The anisotropic envelope equation, eq:D.23-EMT, in units a*_perp = eps/(m_perp alpha), Ry*_perp = m_perp alpha^2/2eps^2:
     [ -(d_x^2 + d_y^2) - gamma_m d_z^2 - 2/r ] F = E F,    gamma_m = m_perp/m_par.
  Scaling z = gamma_m^{1/2} z' makes the kinetic term isotropic; the potential becomes -2/(r' g(theta')),
  g = [1 - (1 - gamma_m) cos^2 theta']^{1/2}.  1/g is expanded in Legendre polynomials P_L (even L <= 28), the envelope in
  spherical harmonics Y_lm (fixed m and parity, l <= 14), and the coupled radial equations for u_l = r R_l are solved by
  second-order finite differences (step 0.02 a*_perp, box 90 a*_perp) with sparse shift-invert diagonalization.
  Checks: gamma_m = 1 returns hydrogen (-1, -1/4, -1/9); l <= 20 and a 150 a*_perp box change no level by more than 1e-5.
  States are labelled by the lowest eigenvalues of each symmetry: m = 0 even -> 1s, 2s; m = 0 odd -> 2p0, 3p0;
  |m| = 1 odd -> 2p+-.  Runtime about 30 s.
"""
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre
from scipy.optimize import minimize
from sympy.physics.wigner import wigner_3j
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch07")
os.makedirs(OUT, exist_ok=True)

Ry, a0, hbarc = 13605.693, 0.529177, 1973.2698   # meV, A, eV A
mperp, mpar = 0.191, 0.916
gam = mperp / mpar
vmax, vmax2 = 2.650e-3, 7.023e-6
a_si = 5.431


def close(x, ref, rtol=5e-3, name=""):
    assert abs(x - ref) <= rtol * abs(ref), f"{name}: {x} vs {ref}"
    print(f"  {name:60s} {x:.6g}   (quoted {ref})")


def levels(g_m, m, parity, lmax=14, Lmax=28, h=0.02, rmax=90.0, k=3, sigma=-2.0):
    x, w = leggauss(200)
    gth = np.sqrt(1 - (1 - g_m) * x**2)
    Ls = list(range(0, Lmax + 1, 2))
    cL = [(2 * L + 1) / 2 * np.sum(w * eval_legendre(L, x) / gth) for L in Ls]
    ls = [l for l in range(abs(m), lmax + 1) if l % 2 == parity]
    n = int(rmax / h)
    r = h * np.arange(1, n + 1)
    D2 = sp.diags([np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)], [-1, 0, 1]) / h**2
    blocks = [[None] * len(ls) for _ in ls]
    for i, l in enumerate(ls):
        for j, lp in enumerate(ls):
            coup = 0.0
            for iL, L in enumerate(Ls):
                if abs(l - lp) <= L <= l + lp:
                    gnt = float((-1) ** m * np.sqrt((2 * l + 1) * (2 * lp + 1))
                                * wigner_3j(l, L, lp, 0, 0, 0) * wigner_3j(l, L, lp, -m, 0, m))
                    coup += cL[iL] * gnt
            M = sp.diags(-2 * coup / r)
            if i == j:
                M = M - D2 + sp.diags(l * (l + 1) / r**2)
            blocks[i][j] = M
    H = sp.bmat(blocks).tocsc()
    return np.sort(sla.eigsh(H, k=k, sigma=sigma, which="LM", return_eigenvectors=False))


print("Hydrogen check (gamma_m = 1):", levels(1.0, 0, 0, lmax=4, Lmax=4))
e_even = levels(gam, 0, 0)
e_odd0 = levels(gam, 0, 1, sigma=-0.6)
e_odd1 = levels(gam, 1, 1, sigma=-0.4)
emt = {"1s": -e_even[0], "2p0": -e_odd0[0], "2s": -e_even[1], "2p+-": -e_odd1[0], "3p0": -e_odd0[1]}
print("EMT binding in units of Ry*_perp:", {k: round(v, 4) for k, v in emt.items()})


def Rystar(eps):
    return mperp * Ry / eps**2


def astar(eps):
    return eps / mperp * a0


print("\nEffective units")
close(gam, 0.209, 0.005, "gamma_m = m_perp/m_par")
close(Rystar(11.7), 18.98, 1e-3, "Ry*_perp (eps 11.7) [meV]")
close(astar(11.7), 32.4, 2e-3, "a*_perp (eps 11.7) [A]")
close(mperp * Ry / 11.7**2, 19.0, 0.01, "isotropic hydrogenic, m_perp [meV]")
close(mpar * Ry / 11.7**2, 91.0, 0.01, "isotropic hydrogenic, m_par [meV]")
close(11.7 / mperp * a0, 32.4, 0.01, "a* (m_perp) [A]")
close(11.7 / mpar * a0, 6.76, 0.01, "a* (m_par) [A]")


# Kohn-Luttinger variational energy, eq:D.23-variational
def Evar(p):
    a, b = p
    e = np.sqrt(1 - b**2 / a**2)
    return 2 / (3 * a**2) + gam / (3 * b**2) - 2 * np.arcsin(e) / (a * e)


res = minimize(Evar, [0.8, 0.45], bounds=[(0.2, 3), (0.1, 0.99)])
print("\nVariational (D.23):", res.fun, res.x * astar(11.7))
close(-res.fun * Rystar(11.7), 29.7, 3e-3, "variational binding [meV]")

print("\nEMT spectrum (full numerical solution)")
lev117 = {k: v * Rystar(11.7) for k, v in emt.items()}
lev114 = {k: v * Rystar(11.4) for k, v in emt.items()}
for k in emt:
    print(f"  {k:5s}  eps 11.7: {lev117[k]:6.2f} meV   eps 11.4: {lev114[k]:6.2f} meV")
close(lev117["1s"], 29.7, 3e-3, "EMT 1s, eps 11.7")
close(lev117["2p0"], 10.9, 5e-3, "EMT 2p0, eps 11.7")
close(lev117["2p+-"], 6.09, 3e-3, "EMT 2p+-, eps 11.7")
close(lev114["1s"], 31.3, 3e-3, "EMT 1s, eps 11.4")
close(lev114["2p0"], 11.51, 3e-3, "EMT 2p0, eps 11.4")
close(lev114["2p+-"], 6.42, 3e-3, "EMT 2p+-, eps 11.4")
close(lev114["3p0"], 5.49, 3e-3, "EMT 3p0, eps 11.4")
eps_fit = 11.7 * np.sqrt(lev117["2p+-"] / 6.40)
close(eps_fit, 11.41, 2e-3, "eps from measured 2p+- (6.40 meV)")
print(f"  variational - exact 1s, in units of Ry*: {(-res.fun) - emt['1s']:.4f}")
close(lev114["1s"], 31.27, 3e-3, "vs Faulkner 31.27 (quoted by Smith et al.)")
close(abs(lev114["2p0"] - 11.48) / 11.48, 0.0026, 0.2, "2p0 deviation from Si:P")

print("\nCentral-cell correction and valley-orbit parameters of Si:P (eq:D.23-vo)")
A1, T2, E = -45.59, -33.89, -32.58
E0 = -lev114["1s"]
close(45.59 - lev114["1s"], 14.3, 0.01, "central-cell correction of A1 vs EMT(11.4) [meV]")
close(45.59 - 29.7, 15.9, 0.01, "central-cell correction vs EMT(11.7) [meV]")
Df = (A1 - E) / 6
Dg = ((E - E0) + 2 * Df - (T2 - E0)) / 2
D0 = (T2 - E0) + Dg
print(f"  reference E0 = {E0:.2f} meV: Delta_0 = {D0:.2f}, Delta_g = {Dg:.2f}, Delta_f = {Df:.2f} meV")
assert Df < 0
close(D0 + Dg + 4 * Df, A1 - E0, 1e-9, "A1 reproduced")
close(D0 + Dg - 2 * Df, E - E0, 1e-9, "E reproduced")
close(D0 - Dg, T2 - E0, 1e-9, "T2 reproduced")
close(Df, -2.17, 0.01, "Delta_f")
close(D0, -4.09, 0.01, "Delta_0")
close(Dg, -1.51, 0.01, "Delta_g")
close(A1 - T2, -11.70, 1e-3, "1s(A1) - 1s(T2) [meV]")
close(A1 - E, -13.01, 1e-3, "1s(A1) - 1s(E) [meV]")
close(-3.12 + 45.59, 42.47, 1e-3, "1s(A1)->3p+- transition implied by 45.59 and EMT 3p+- 3.12")

print("\nSize of the donor, density and kinematics")
avar, bvar = res.x * astar(11.7)
close(avar, 24.3, 3e-3, "KL radius a [A]")
close(bvar, 14.0, 5e-3, "KL radius b [A]")
F0sq = 1 / (np.pi * avar**2 * bvar)      # |F(0)|^2 of the KL envelope, A^-3
Ncell_per_A3 = 8 / a_si**3
print("  |F(0)|^2 per atomic volume (probability on one site):", F0sq / Ncell_per_A3)
nD = 1e15 * 1e-24                        # cm^-3 -> A^-3
close(nD**(-1 / 3) / 10, 100.0, 1e-3, "mean spacing at 1e15 cm^-3 [nm]")
vol = 4 * np.pi / 3 * avar**2 * bvar
print("  density of one donor per KL spheroid [cm^-3]:", 1 / vol * 1e24)
mmin_P = 2 * 45.59e-3 / vmax2
close(mmin_P / 1e3, 13.0, 3e-3, "m_min to ionize Si:P [keV]")
q_thr = 2 * 45.59e-3 / vmax
close(q_thr, 34.4, 3e-3, "q at threshold, 2E/v_max [eV]")
close(hbarc / avar, 81.2, 3e-3, "1/a (KL transverse radius) [eV]")
close(hbarc / bvar, 141, 5e-3, "1/b [eV]")
close(q_thr * avar / hbarc, 0.42, 0.02, "q a")
close(2 * 1.17 / vmax2 / 1e6, 0.333, 3e-3, "silicon gap m_min [MeV]")

# --------------------------------------------------------------------------- figure
blue, orange, gray = "#2a78d6", "#eb6834", "0.45"
hy_perp, hy_par = mperp * Ry / 11.7**2, mpar * Ry / 11.7**2
# (column title, [(binding meV, label or None, label offset meV)], color)
cols = [
    ("hydrogenic\n$m^*_\\perp$", [(hy_perp, "1s", 0), (hy_perp / 4, "$n = 2$", 0)], gray),
    ("hydrogenic\n$m^*_\\parallel$", [(hy_par / 4, "$n = 2$", 0)], gray),
    ("effective mass\n$\\varepsilon_0 = 11.7$", [(lev117["1s"], "1s", 0), (lev117["2p0"], "2p$_0$", 0),
                                               (lev117["2s"], None, 0), (lev117["2p+-"], "2p$_\\pm$", 0.6),
                                               (lev117["3p0"], None, 0)], blue),
    ("effective mass\n$\\varepsilon_0 = 11.4$", [(lev114["1s"], "1s", 0), (lev114["2p0"], "2p$_0$", 0),
                                               (lev114["2s"], "2s", -0.3), (lev114["2p+-"], "2p$_\\pm$", 1.2),
                                               (lev114["3p0"], None, 0)], blue),
    ("Si:P\nmeasured", [(45.59, "1s(A$_1$)", 0), (33.89, "1s(T$_2$)", -1.2), (32.58, "1s(E)", 1.2),
                        (11.48, "2p$_0$", 0), (6.40, "2p$_\\pm$", 0.6), (5.47, None, 0)], orange),
    ("Si:As\nmeasured", [(53.76, "1s(A$_1$)", 0), (32.67, "1s(T$_2$)", -1.2), (31.26, "1s(E)", 1.2),
                         (11.50, "2p$_0$", 0), (9.11, "2s", -0.3), (6.40, "2p$_\\pm$", 1.2), (5.49, None, 0)], orange),
]
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for i, (lab, lv, c) in enumerate(cols):
    for e, name, off in lv:
        ax.hlines(-e, i - 0.30, i + 0.30, color=c, lw=1.6)
        if name:
            ax.text(i + 0.34, -e + off, name, fontsize=6.5, va="center")
    ax.text(i, 3.6, lab, ha="center", va="bottom", fontsize=7)
ax.annotate("", xy=(1, -58.5), xytext=(1, -52), arrowprops=dict(arrowstyle="->", color=gray, lw=0.8))
ax.text(1.08, -55, "1s at $-91.0$", fontsize=6.5, va="center")
ax.axhline(0, color="k", lw=0.8)
ax.text(-0.45, 0.4, "conduction-band minimum", fontsize=6.5, va="bottom")
ax.set_xlim(-0.5, 5.95)
ax.set_ylim(-59, 12)
ax.set_xticks([])
ax.set_yticks(range(-50, 1, 10))
ax.set_ylabel("level energy from the band edge (meV)")
for sname in ("top", "right", "bottom"):
    ax.spines[sname].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig7_4.pdf"))
print("wrote fig7_4.pdf")
