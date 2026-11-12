"""Shared inputs of Sect. 12.2 (the atomic limit of the Migdal effect). Natural units, energies in eV.

Published tables used (no atomic structure is computed in this book):
  * Ibe, Nakano, Shoji and Suzuki, arXiv:1707.07258 (FAC, single-electron, dipole order):
      Table II (Ge, Xe): excitation probabilities p^d(nl -> n'l') and integrated ionization probabilities per (n, l)
      at q_e = m_e x 1e-3; ancillary files Ge.dat, Xe.dat: dp^c/dE_e in eV^-1 at q_e = 1 eV,
      "not divided by 2 pi" (note added); the probability per eV at q_e is (q_e/1 eV)^2 (dp^c/dE_e)/(2 pi).
  * Cox, Dolan, McCabe and Quiney, arXiv:2208.12222, data release (Zenodo 10.5281/zenodo.7659176): Dirac-Hartree-Fock, exclusive single ionization per orbital, dP/dE in keV^-1,
      E_e in keV; *_dipole.txt at v = 1e-3 (dipole order), *_DM.txt all multipoles L <= 10 on a velocity grid.
      Their v is the recoil velocity with q_e = m_e v.
  * Hydrogen: exact (closed forms of Sects. 2.2, 6.1 and numerical radial integrals below).
  * Helium 1s2 1S -> 1snp 1P oscillator strengths and energies: NIST ASD (Kramida et al.),
      He I resonance series (n = 2..10, accuracy AAA); n > 10 by the n^-3 tail.

Masses: atomic weights 28.0855 (Si), 72.630 (Ge), 131.293 (Xe) times u = 931.49410242 MeV (the book's Si value 26.162 GeV).
"""
import os
import numpy as np
from scipy.special import eval_genlaguerre, gammaln, spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "data", "12.2")
ME = 510998.95
ALPHA = 1 / 137.035999084
HARTREE = ME * ALPHA**2            # 27.2114 eV
U = 931.49410242e6
MA = {"Si": 28.0855 * U, "Ge": 72.630 * U, "Xe": 131.293 * U, "He": 4.002602 * U}
NE = {"Si": 14, "Ge": 32, "Xe": 54, "He": 2}
QE_REF = ME * 1e-3                 # q_e of the published tables (v = 1e-3)


def v_recoil(el, ER):
    """Recoil velocity of a free atom of mass m_A with kinetic energy E_R."""
    return np.sqrt(2 * ER / MA[el])


def q_e(el, ER):
    """Momentum given to each electron, m_e q/m_A = m_e v."""
    return ME * v_recoil(el, ER)


# ---------------------------------------------------------------- published tables
def _rows(path, ncol):
    out = []
    for line in open(path):
        p = line.split()
        try:
            r = [float(x) for x in p]
        except ValueError:
            continue
        if len(r) == ncol:
            out.append(r)
    return np.array(out)


def ibe_spectra(el):
    """{(n, l): (E_e [eV], dP/dE_e [eV^-1] at q_e = QE_REF)} from the ancillary files of 1707.07258."""
    lines = open(os.path.join(SRC, "ibe_anc", el + ".dat")).read().split("\n")
    out, cur, i = {}, None, 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("Principal"):
            n, l = map(int, lines[i + 1].split())
            cur = (n, l)
            out[cur] = []
            i += 3
            continue
        if s and cur is not None:
            out[cur].append([float(x) for x in s.split()])
        i += 1
    return {k: (np.array(v)[:, 0], np.array(v)[:, 1] * QE_REF**2 / (2 * np.pi)) for k, v in out.items()}


# Ibe et al., Table II, Ge at q_e = m_e x 1e-3: excitation probabilities (initial -> final) and level energies (eV)
IBE_GE_EXC = {("3d", "4p"): 2.3e-3, ("3d", "5p"): 2.3e-4, ("4s", "4p"): 4.0e-2, ("4s", "5p"): 3.9e-4,
              ("4p", "4d"): 2.7e-2, ("4p", "5s"): 1.6e-2, ("4p", "6s"): 1.5e-3,
              ("3p", "4d"): 6.0e-9, ("3p", "5s"): 2.8e-5, ("3p", "6s"): 8.3e-6, ("3s", "4p"): 3.7e-5, ("3s", "5p"): 5.6e-6,
              ("2s", "4p"): 1.8e-6, ("2s", "5p"): 2.8e-7, ("2p", "4d"): 3.3e-7, ("2p", "5s"): 1.1e-7, ("2p", "6s"): 3.4e-8,
              ("1s", "4p"): 5.0e-8, ("1s", "5p"): 7.9e-9}
IBE_GE_E = {"1s": 1.1e4, "2s": 1.4e3, "2p": 1.2e3, "3s": 1.7e2, "3p": 1.2e2, "3d": 35.0, "4s": 15.0, "4p": 6.5,
            "4d": 1.6, "5s": 3.0, "5p": 2.0, "6s": 1.4}
LNAME = "spdf"


def cox_dipole(el):
    """{orbital: (E_e [eV], dP/dE_e [eV^-1] at q_e = QE_REF)}, j-split orbitals merged (2p- + 2p -> 2p)."""
    d = os.path.join(SRC, "cox_migdal", el, "single-ionisation")
    out = {}
    for f in sorted(os.listdir(d)):
        if not f.endswith("_dipole.txt") or "single-ionisation" in f:
            continue
        orb = f.split("_")[1].rstrip("-")
        a = _rows(os.path.join(d, f), 3)
        E, p = a[:, 0] * 1e3, a[:, 2] / 1e3
        if orb in out:
            assert np.allclose(out[orb][0], E)
            out[orb] = (E, out[orb][1] + p)
        else:
            out[orb] = (E, p)
    return out


def cox_full(el):
    """(v grid, P_single(v)) all multipoles, exclusive single ionization summed over orbitals (the *_DM table)."""
    a = _rows(os.path.join(SRC, "cox_migdal", el, "single-ionisation", el + "_single-ionisation_DM.txt"), 3)
    vs = np.unique(a[:, 1])
    P = np.array([np.trapezoid(a[a[:, 1] == v, 2], a[a[:, 1] == v, 0]) for v in vs])
    return vs, P


def cox_dipole_total(el):
    a = _rows(os.path.join(SRC, "cox_migdal", el, "single-ionisation", el + "_single-ionisation_dipole.txt"), 3)
    return np.trapezoid(a[:, 2], a[:, 0])        # at v = 1e-3


def cox_constant(el, vfit=None):
    """Fit P_full(v) = c0 + a v^2 + b v^4 at small v. c0 is a velocity-independent part that a transition between
    orthogonal states cannot have (it comes from the incomplete orthogonality of initial and final orbitals in the
    source's calculation, its App. A 3); a is compared with the dipole coefficient."""
    vfit = vfit or {"Si": 6e-4, "Ge": 4e-4}[el]
    vs, P = cox_full(el)
    m = vs <= vfit
    A = np.vstack([np.ones(m.sum()), vs[m]**2, vs[m]**4]).T
    return np.linalg.lstsq(A, P[m], rcond=None)[0]


# ---------------------------------------------------------------- hydrogen (a0 = 1, xi = q_e a0)
R_GRID = np.linspace(1e-6, 60.0, 60001)


def R_nl(n, l, r):
    """Normalized hydrogen radial function (a0 = 1)."""
    rho = 2 * r / n
    lognorm = 0.5 * (3 * np.log(2.0 / n) + gammaln(n - l) - np.log(2 * n) - gammaln(n + l + 1))
    return np.exp(lognorm - rho / 2) * rho**l * eval_genlaguerre(n - l - 1, 2 * l + 1, rho)


R10 = 2 * np.exp(-R_GRID)


def p_bound_exact(xi, nmax=40, lmax=12):
    """Sum over bound n <= nmax, all l, of |<n l 0|e^{i xi z}|1s>|^2 = (2l+1)|int R_nl R_10 j_l(xi r) r^2 dr|^2,
    plus the tail sum_{n > nmax} ~ P_nmax nmax/2 (each l falls as n^-3)."""
    r = R_GRID
    tot, last = 0.0, 0.0
    for n in range(2, nmax + 1):
        pn = 0.0
        for l in range(0, min(n - 1, lmax) + 1):
            I = np.trapezoid(R_nl(n, l, r) * R10 * spherical_jn(l, xi * r) * r**2, r)
            pn += (2 * l + 1) * I**2
        tot += pn
        last = pn
    return tot + last * nmax / 2


def dipole_lines_H(nmax=60):
    """|<np|r|1s>|^2/3 = |<np|z|1s>|^2 per n (a0^2) and the oscillator strengths f_n = 2 dE |z|^2 (dE in hartree)."""
    r = R_GRID
    z2, f = [], []
    for n in range(2, nmax + 1):
        I = np.trapezoid(R_nl(n, 1, r) * R10 * r**3, r)
        z2.append(I**2 / 3)
        f.append(2 * 0.5 * (1 - 1 / n**2) * I**2 / 3)
    return np.arange(2, nmax + 1), np.array(z2), np.array(f)


def p_inel_H(xi):
    """1 - F_1s^2 with F_1s = 16/(4 + xi^2)^2 (eq:2.2-F1s, eq:6.1-P0)."""
    return 1 - (16 / (4 + xi**2)**2)**2


# ---------------------------------------------------------------- helium lines (NIST ASD)
def he_lines():
    rows = []
    for line in open(os.path.join(SRC, "nist_asd_HeI_resonance.tsv")).read().split("\n")[1:]:
        c = [x.strip('"') for x in line.split("\t")]
        if len(c) < 14 or c[13] != "1" or c[12] != "1P*" or not c[4]:
            continue
        n = int(c[11].split(".")[1][:-1])
        rows.append((n, float(c[4]), float(c[7].strip("[]"))))
    rows.sort()
    return rows        # (n, f, E [eV])


HE_IP = 24.587389       # eV, NIST ASD ionization energy of He I


def he_bound(nmax_list=10):
    """sum_f |<f|D_z|0>|^2 = sum f_n/(2 m_e dE_n) in units of a0^2 (atomic units: f/(2 dE)). Tail n > 10: f_n ~ C n^-3 at
    dE -> IP."""
    rows = he_lines()
    terms = {n: f / (2 * E / HARTREE) for n, f, E in rows}
    n_last, f_last, _ = rows[-1]
    C = f_last * n_last**3
    tail_f = sum(C / n**3 for n in range(n_last + 1, 2000))
    tail = tail_f / (2 * HE_IP / HARTREE)
    return terms, tail, tail_f


if __name__ == "__main__":
    for el in ("Si", "Ge"):
        c0, a, b = cox_constant(el)
        print(f"{el}: Cox dipole total at v=1e-3 {cox_dipole_total(el):.4e}; fit c0 = {c0:.3e}, a = {a:.4e} "
              f"(dipole {cox_dipole_total(el) / 1e-6:.4e}, ratio {a / (cox_dipole_total(el) / 1e-6):.4f})")
    n, z2, f = dipole_lines_H()
    print("H: |z|^2 2p,3p,4p", z2[:3], " bound sum", z2.sum() + z2[-1] * n[-1] / 2, " f bound", f.sum() + f[-1] * n[-1] / 2)
    terms, tail, tail_f = he_bound()
    print("He: terms", {k: round(v, 5) for k, v in terms.items()}, "tail", tail, "tail f", tail_f)
