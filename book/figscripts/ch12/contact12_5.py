"""Sect. 12.5: contact densities and the relativistic finite-nucleus factor (Table 12.1, third moment).
Run: python contact12_5.py (about 3 min; PySCF ROHF of the free Ge atom).

(1) Nonrelativistic point-nucleus contact density of the free Ge atom (3P ground state, [Ar]3d10 4s2 4p2), all-electron
    ROHF with PySCF, uncontracted cc-pVQZ basis of Ge (no core-valence set for Ge in PySCF) plus tight even-tempered s functions (ratio 3), as Sect. 8.3
    did for Si (figscripts/ch08/we8_4.py: n_e^(k) = 1765 a0^-3).  Convergence of the contact density printed against the number of tight functions.
(2) Relativistic finite-nucleus factor R_rel = <n_e>_nuc / n_e^NR(0), estimated from the Dirac 1s orbital of a point
    charge Z (Bethe and Salpeter, Sect. 14; C.15: g ~ r^(gamma_D - 1)), whose density relative to the
    Schroedinger 1s is  [2/Gamma(2 gamma_D + 1)] (2 Z r/a0)^(2 gamma_D - 2) exp(-2 Z r/a0) (normalized Dirac 1s, App. D.34),
    averaged over a uniformly charged nucleus of radius R_nuc (the average of r^(2g-2) over the sphere is
    3/(2g+1) R^(2g-2)), with exp(-2 Z r/a0) set to one inside the nucleus:
        R_rel = 6 / [(2 gamma_D + 1) Gamma(2 gamma_D + 1)] (2 Z R_nuc/a0)^(2 gamma_D - 2).
    Also printed: 2 Z R_nuc/a0, the factor with exp(-2 Z r/a0) kept in the sphere average (numerical quadrature), and
    the sensitivity to the radius, d ln R_rel = (2 gamma_D - 2) ln 1.1 for R_nuc -> 1.1 R_nuc.
    R_nuc from the Lewin-Smith parameters of Sect. 2.2 (Si 3.47 fm, Ge 4.77 fm).  Modelling choice: every s shell is
    given the 1s factor (all s densities share the r^(2g-2) behaviour inside the nucleus).
(3) Third Migdal moment per unit recoil energy, E3/E_R = [Z e^2 n_e^(k)/3 - Phi_on]/M (eq:12.5-third), Phi_on
    neglected (1e-6 relative, Sect. 12.5), NR and relativistic.
Units: hartree atomic units; e^2 = 4 pi alpha (Heaviside-Lorentz); 1/a0 = 3728.94 eV.
"""
import numpy as np
from scipy.special import gamma as Gf
from pyscf import gto, scf

ALPHA = 1 / 137.035999
INV_A0 = 3728.94          # eV
A0_FM = 52917.721
ME = 510998.95
M = {"Si": 26.162e9, "Ge": 67.654e9}    # atomic masses, eV (Si: Sect. 5.6; Ge: 72.630 u, Sect. 12.2)
Z = {"Si": 14, "Ge": 32, "Ga": 31, "As": 33}
AMASS = {"Si": 28.09, "Ge": 72.63, "Ga": 69.72, "As": 74.92}


def r_nuc(A):
    c = 1.23 * A**(1 / 3) - 0.60
    return np.sqrt(c**2 + 7 / 3 * np.pi**2 * 0.52**2 - 5 * 0.9**2)


def r_rel(el):
    z = Z[el]
    g = np.sqrt(1 - (z * ALPHA)**2)
    x = 2 * z * r_nuc(AMASS[el]) / A0_FM
    return 6 / ((2 * g + 1) * Gf(2 * g + 1)) * x**(2 * g - 2), g, r_nuc(AMASS[el])


def ge_contact(ntight):
    b = gto.uncontract(gto.load("cc-pvqz", "Ge"))
    smax = max(e[1][0] for e in b if e[0] == 0)
    extra = [[0, [smax * 3.0**(k + 1), 1.0]] for k in range(ntight)]
    mol = gto.M(atom="Ge 0 0 0", basis={"Ge": b + extra}, spin=2, verbose=0)
    mf = scf.ROHF(mol)
    mf.conv_tol = 1e-9
    mf.max_cycle = 200
    E = mf.kernel()
    d = mf.make_rdm1()
    d = d[0] + d[1]
    ao = mol.eval_gto("GTOval", np.zeros((1, 3)))[0]
    C, occ = mf.mo_coeff, mf.mo_occ
    order = [i for i in np.argsort(mf.mo_energy) if occ[i] > 0]
    mo0 = ao @ C
    val = order[-3:]          # 4s (doubly), 4p (two singly occupied)
    rho_val = float((mo0[val]**2 * occ[val]).sum())
    return E, float(ao @ d @ ao), rho_val


if __name__ == "__main__":
    for el in ["Si", "Ge", "Ga", "As"]:
        R, g, rn = r_rel(el)
        za2 = (Z[el] * ALPHA)**2
        lead = za2 * np.log(A0_FM / (2 * Z[el] * rn))
        print(f"{el}: Z = {Z[el]}, gamma_D - 1 = {g-1:.4f}, R_nuc = {rn:.2f} fm, R_rel = {R:.4f} (+{(R-1)*100:.1f} %); "
              f"(Z alpha)^2 = {za2:.4f}, logarithmic term (Z alpha)^2 ln(a0/2ZR) = {lead:.4f}, remainder {R-1-lead:+.4f}")
        x = 2 * Z[el] * rn / A0_FM
        rr = np.linspace(0, rn, 20001)[1:]
        dens = 2 / Gf(2 * g + 1) * (2 * Z[el] * rr / A0_FM)**(2 * g - 2) * np.exp(-2 * Z[el] * rr / A0_FM)
        Rexp = 3 / rn**3 * np.trapezoid(rr**2 * dens, rr)
        print(f"    2ZR/a0 = {x:.2e}; with exp(-2 Z r/a0) kept: R_rel = {Rexp:.4f} (dropping it overstates by "
              f"{(R/Rexp-1)*100:.2f} %); R_nuc +10 %: R_rel changes by {((1.1)**(2*g-2)-1)*100:+.3f} %")
    res = {}
    for nt in (0, 3, 6):
        E, rho, rv = ge_contact(nt)
        res[nt] = (rho, rv)
        print(f"Ge ROHF, {nt} tight s: E = {E:.5f} hartree, contact density {rho:.1f} a0^-3, "
              f"valence 4s4p {rv:.2f}")
    rho_ge, rv_ge = res[6]
    rho = {"Si": 1765.0, "Ge": rho_ge}
    e2 = 4 * np.pi * ALPHA
    for el in ["Si", "Ge"]:
        n = rho[el] * INV_A0**3
        E3 = Z[el] * e2 * n / 3 / M[el]
        R = r_rel(el)[0]
        print(f"{el}: n_e^(k) = {rho[el]:.0f} a0^-3; E3/E_R = {E3:.0f} eV^2 (NR), {E3*R:.0f} eV^2 (relativistic finite "
              f"nucleus); sqrt = {np.sqrt(E3):.1f} eV, {np.sqrt(E3*R):.1f} eV")
    print(f"Ge valence share of the contact density: {rv_ge/rho_ge:.2e}")
