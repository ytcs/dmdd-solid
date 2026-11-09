"""Shared donor model for Sect. 16.5 (dopants): anisotropic effective-mass donor of silicon, its dipole spectrum
(lines and continuum), its polarizability, and the effective-medium dielectric function of a doped crystal.
Run directly: prints every model number of Sect. 16.5 and writes donor16_5.npz (used by fig16_5.py, limit16_5a.py,
we16_5.py).  Natural units hbar = c = 1; inside the solver lengths are in a*_perp and energies in Ry*_perp.

Inputs and their sources
  Constants (CODATA, as App. D.23 and fig7_4.py): Ry = 13605.693 meV, a0 = 0.529177 A, hbar c = 1973.2698 eV A,
     alpha = 1/137.035999.
  Silicon valley masses m_perp = 0.191, m_par = 0.916 m_e (tab:3-materials); gamma_m = m_perp/m_par.
  Static dielectric constant at liquid-helium temperature eps_host = 11.4 (Sect. 7.4: the value fixed by the measured
     2p+- level and used for donor spectra by Faulkner 1969 and Smith et al., arXiv:1612.00569).
  Measured Si:P levels (binding energies, meV; Vinh et al., arXiv:0812.0148, Fig. 1; P ground state 45.59,
     Jagannath et al. 1981): 1s(A1) 45.59, 2p0 11.48, 2p+- 6.40, 3p0 5.47.  3p+- 3.12 meV is the effective-mass value
     used by Smith et al. (Sect. 7.4).

Method (named in the text and the captions)
  The envelope equation eq:7.4-EMT is solved as in fig7_4.py: z scaled by gamma_m^{1/2} makes the kinetic term
  isotropic; the Coulomb term -2/(r g(theta)) is expanded in Legendre polynomials (even L <= LMAX_POT); the envelope in
  spherical harmonics of fixed m and parity (l <= LMAX); second-order finite differences, step H, box RMAX.
  Ground state: lowest state of the (m = 0, even) block.  Two ground-state models:
     'EMT'  the effective-mass ground state (1s at 31.3 meV for eps 11.4);
     'CC'   the same block with a model central cell, -V_c exp(-r'^2/r_c^2) in the scaled coordinates, V_c tuned so
            that the 1s binding is the measured 45.59 meV (r_c = 0.10 and 0.20 a*_perp, 3.2 and 6.3 A).
  In both, the transition energies use the measured ground state, omega = E_f + 45.59 meV.
  Dipole operator: z = gamma_m^{1/2} z' (valley axis), x = x'.  Final states in the (m = 0, odd) block (p0 series) and the
  (m = 1, odd) block (p+- series; the m = -1 partners double the transverse strength).
  The dipole spectrum of each block: the KSTATES eigenpairs nearest the middle of [-0.7, ECUT] Ry* (shift-invert ARPACK),
  which cover every bound state and the box-discretized continuum below ECUT, with weights w_f = |<f|b>|^2, b = D psi0.
  The states above ECUT enter the real part of the polarizability through their exact static sum (sparse LU solve of
  (H - E) x = b minus the explicit states), added as a constant for omega well below ECUT.
  A1 ground state of six valleys: the cubic average of a dipole strength is (|Z|^2 + 2 |X|^2)/3 per polarization, with
  |X|^2 summed over m' = +-1.
  Polarizability (Heaviside-Lorentz): alpha_pol(omega) = e^2 sum_f |<f|e.r|i>|^2 [1/(w_f - omega - i0) + 1/(w_f + omega)],
  = 8 pi eps_host a*^3 A(omega) with A in a*^2/Ry* units.  Donor part of the dielectric function eps^D = n_D alpha_pol.
  Effective medium (Clausius-Mossotti / Maxwell Garnett form, as the dot medium of Sect. 16.3):
     eps_eff = eps_host (1 + 2y)/(1 - y),  y = eps^D/(3 eps_host);  static divergence at y(0) = 1.
Checks printed: hydrogen (gamma = 1): 2p dipole 0.5549 a0^2, static polarizability 9/2 a0^3 (Gaussian), TRK sum 1;
  Thomas-Reiche-Kuhn sums of the EMT donor, sum_f w_f |X_f|^2 = 1 and sum_f w_f |Z'_f|^2 = 1 (reduced units);
  level positions against fig7_4.py; convergence in LMAX, H, RMAX for the static polarizability and the 2p0 strength.
Runtime: about two minutes.
"""
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre
from scipy.optimize import brentq
from sympy.physics.wigner import wigner_3j

HERE = os.path.dirname(os.path.abspath(__file__))

RY, A0, HBARC, ALPHA = 13605.693, 0.529177, 1973.2698, 1 / 137.035999
MPERP, MPAR = 0.191, 0.916
GAM = MPERP / MPAR
EPS = 11.4
RYS = MPERP * RY / EPS**2            # meV
AS = EPS / MPERP * A0                 # Angstrom
E1S_MEAS = 45.59                      # meV
MEAS_BIND = {"2p0": 11.48, "2p+-": 6.40, "3p0": 5.47, "3p+-": 3.12}

LMAX, LMAX_POT, H, RMAX, ECUT, KSTATES = 12, 24, 0.02, 90.0, 3.0, 520


def gaunt(l1, L, l2, m1, M, m2):
    """int Y*_{l1 m1} Y_{L M} Y_{l2 m2} dOmega."""
    return float((-1) ** m1 * np.sqrt((2 * l1 + 1) * (2 * L + 1) * (2 * l2 + 1) / (4 * np.pi))
                 * wigner_3j(l1, L, l2, 0, 0, 0) * wigner_3j(l1, L, l2, -m1, M, m2))


class Model:
    def __init__(self, g_m=GAM, lmax=LMAX, Lmax=LMAX_POT, h=H, rmax=RMAX):
        self.g, self.lmax, self.Lmax, self.h = g_m, lmax, Lmax, h
        self.n = int(rmax / h)
        self.r = h * np.arange(1, self.n + 1)
        x, w = leggauss(200)
        gth = np.sqrt(1 - (1 - g_m) * x**2)
        self.Ls = list(range(0, Lmax + 1, 2))
        self.cL = [(2 * L + 1) / 2 * np.sum(w * eval_legendre(L, x) / gth) for L in self.Ls]

    def ls(self, m, parity):
        return [l for l in range(abs(m), self.lmax + 1) if l % 2 == parity]

    def hamiltonian(self, m, parity, Vc=0.0, rc=0.1):
        ls, n, r, h = self.ls(m, parity), self.n, self.r, self.h
        D2 = sp.diags([np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)], [-1, 0, 1]) / h**2
        blocks = [[None] * len(ls) for _ in ls]
        for i, l in enumerate(ls):
            for j, lp in enumerate(ls):
                coup = 0.0
                for iL, L in enumerate(self.Ls):
                    if abs(l - lp) <= L <= l + lp:
                        gnt = float((-1) ** m * np.sqrt((2 * l + 1) * (2 * lp + 1))
                                    * wigner_3j(l, L, lp, 0, 0, 0) * wigner_3j(l, L, lp, -m, 0, m))
                        coup += self.cL[iL] * gnt
                M = sp.diags(-2 * coup / r)
                if i == j:
                    M = M - D2 + sp.diags(l * (l + 1) / r**2 - Vc * np.exp(-(r / rc) ** 2))
                blocks[i][j] = M
        return sp.bmat(blocks).tocsc()

    def dipole(self, m_to, M):
        """Matrix of r Y-component from the (m=0, even) block to the (m_to, odd) block.
        M = 0: z' = r cos(theta) = sqrt(4pi/3) r Y10.  M = 1: the m'=+1 part of x' = sqrt(2pi/3) r (Y1,-1 - Y11)."""
        le, lo, n = self.ls(0, 0), self.ls(m_to, 1), self.n
        blocks = [[None] * len(le) for _ in lo]
        for i, l1 in enumerate(lo):
            for j, l2 in enumerate(le):
                if M == 0:
                    c = np.sqrt(4 * np.pi / 3) * gaunt(l1, 1, l2, 0, 0, 0)
                else:
                    c = -np.sqrt(2 * np.pi / 3) * gaunt(l1, 1, l2, 1, 1, 0)
                blocks[i][j] = sp.diags(c * self.r) if c != 0 else sp.csr_matrix((n, n))
        return sp.bmat(blocks).tocsr()


def ground(model, Vc=0.0, rc=0.1):
    He = model.hamiltonian(0, 0, Vc, rc)
    val, vec = sla.eigsh(He, k=1, sigma=-12.0, which="LM")
    return val[0], vec[:, 0]


def spectrum(model, Vc=0.0, rc=0.1, ecut=ECUT, kstates=KSTATES):
    """Explicit eigenpairs of the odd blocks below ecut (shift-invert ARPACK), their dipole weights, and the exact
    totals from sparse solves: static sum 2 b.(H - E)^-1 b and the TRK sum b.(H - E0) b."""
    E0, psi0 = ground(model, Vc, rc)
    out = {"E0": E0, "psi0": psi0}
    for name, m_to, M, fac in (("z", 0, 0, model.g), ("x", 1, 1, 2.0)):
        Ho = model.hamiltonian(m_to, 1)
        b = model.dipole(m_to, M) @ psi0
        sig = (ecut - 0.7) / 2
        val, vec = sla.eigsh(Ho, k=kstates, sigma=sig, which="LM")
        o = np.argsort(val)
        val, vec = val[o], vec[:, o]
        lowest = sla.eigsh(Ho, k=1, sigma=-12.0, which="LM", return_eigenvectors=False)[0]
        assert abs(val[0] - lowest) < 1e-8 and val[-1] > ecut, (val[0], lowest, val[-1])
        keep = val < ecut
        w = (vec[:, keep].T @ b) ** 2
        lu = sla.splu((Ho - E0 * sp.identity(Ho.shape[0])).tocsc())
        tot_static = 2 * b @ lu.solve(b)
        trk = b @ (Ho @ b) - E0 * (b @ b)
        out[name] = (val[keep], fac * w)          # fac: z = gamma^{1/2} z'; m' = -1 partner doubles x
        out[name + "_static"] = fac * tot_static  # exact static 2 sum w/(E_f - E0)
        out[name + "_trk"] = fac * trk
        out[name + "_Ho"], out[name + "_b"] = Ho, b
    return out


def remainder(sp_, k, E_i):
    """Static contribution of the states above ecut, 2 sum_rest w/(E_f - E_i), from an exact solve at E_i."""
    Ho, b = sp_[k + "_Ho"], sp_[k + "_b"]
    fac = GAM if k == "z" else 2.0
    lu = sla.splu((Ho - E_i * sp.identity(Ho.shape[0])).tocsc())
    tot = fac * 2 * b @ lu.solve(b)
    th, w = sp_[k]
    return tot - 2 * np.sum(w / (th - E_i))


def static_A(sp_):
    """Reduced static polarizability per axis (exact solve with the model's own ground-state energy)."""
    return {k: sp_[k + "_static"] for k in ("z", "x")}


def bound_lines(sp_, nlines=3):
    """Lowest Ritz values below zero (bound lines) with weights, per block."""
    res = {}
    for k in ("z", "x"):
        th, w = sp_[k]
        sel = (th < 0) & (w > 1e-12)
        res[k] = (th[sel][:nlines], w[sel][:nlines])
    return res


def alpha_red(sp_, E_i, omega, eta, rem):
    """Cubic average per polarization, A = (A_z + 2 A_x)/3, with |X|^2 summed over m' = +-1 in w_x; complex, with
    Lorentzian half-width eta (resonant term) in Ry*.  rem[k]: static remainder of the states above ecut, added as a
    constant (their energies exceed omega by more than ecut - omega)."""
    tot = 0.0
    for k, wt in (("z", 1 / 3), ("x", 2 / 3)):
        th, w = sp_[k]
        d = th[None, :] - E_i
        tot = tot + wt * (np.sum(w[None, :] * (1 / (d - omega[:, None] - 1j * eta) + 1 / (d + omega[:, None])), axis=1)
                          + rem[k])
    return tot


def eps_D(Ared, nD_cm3):
    """Donor part of the dielectric function, n_D alpha_pol = 8 pi eps n_D a*^3 A."""
    nA3 = nD_cm3 * 1e-24 * AS**3
    return 8 * np.pi * EPS * nA3 * Ared


def eps_eff(epsD):
    y = epsD / (3 * EPS)
    return EPS * (1 + 2 * y) / (1 - y)


def tune_cc(model, rc):
    target = -E1S_MEAS / RYS
    f = lambda V: ground(model, V, rc)[0] - target
    lo, hi = 0.0, 2.0
    while f(hi) > 0:
        lo, hi = hi, 2 * hi
    return brentq(f, lo, hi, xtol=1e-6)


if __name__ == "__main__":
    print(f"Units (eps = {EPS}): Ry*_perp = {RYS:.3f} meV, a*_perp = {AS:.3f} A, gamma_m = {GAM:.4f}")

    # ---------------- hydrogen checks (gamma = 1)
    hyd = Model(g_m=1.0, lmax=4, Lmax=4)
    sh = spectrum(hyd, kstates=120)
    lh = bound_lines(sh, 1)
    print("\nHydrogen check (gamma = 1, units a0, Ry):")
    print(f"  E(1s) = {sh['E0']:.6f} (exact -1)")
    print(f"  |<2p0|z|1s>|^2 = {lh['z'][1][0]:.5f} (exact 2^15/3^10 = {2**15/3**10:.5f}); "
          f"|<2p+-|x|1s>|^2 summed = {lh['x'][1][0]:.5f}")
    Ah = static_A(sh)
    print(f"  static polarizability 2 sum|z|^2/dE = {Ah['z']:.5f} Ry^-1 a0^2 -> Gaussian alpha = {2*Ah['z']:.5f} a0^3 (exact 4.5)")
    print(f"  TRK sum_f dE |z|^2 = <b|H - E0|b> = {sh['z_trk']:.5f}, x: {sh['x_trk']/2:.5f} per m' (exact 1, 1/2)")

    # ---------------- silicon EMT donor
    mod = Model()
    print(f"\nSilicon donor, l <= {LMAX}, L <= {LMAX_POT}, h = {H}, box {RMAX} a*_perp, states below {ECUT} Ry* explicit")
    sp_emt = spectrum(mod)
    E0 = sp_emt["E0"]
    print(f"  EMT 1s: {-E0:.4f} Ry* = {-E0*RYS:.2f} meV (fig7_4.py: 1.566 Ry*, 31.3 meV)")
    lb = bound_lines(sp_emt, 3)
    names = {"z": ["2p0", "3p0", "4p0"], "x": ["2p+-", "3p+-", "4p+-"]}
    for k in ("z", "x"):
        for nm, th in zip(names[k], lb[k][0]):
            print(f"  EMT {nm:5s} binding {-th*RYS:6.3f} meV")
    trk_emt = {k: sp_emt[k + "_trk"] for k in ("z", "x")}
    print(f"  TRK (reduced; exact 1 for x, gamma_m = {GAM:.4f} for z with z = gamma^1/2 z'): x {trk_emt['x']:.4f}, "
          f"z {trk_emt['z']:.4f} -> z/gamma {trk_emt['z']/GAM:.4f}")

    # ---------------- central-cell models
    models = {"EMT": (0.0, 0.1)}
    for rc in (0.10, 0.20):
        Vc = tune_cc(mod, rc)
        models[f"CC{rc:.2f}"] = (Vc, rc)
        print(f"  central cell r_c = {rc:.2f} a*_perp ({rc*AS:.1f} A): V_c = {Vc:.3f} Ry* = {Vc*RYS/1e3:.3f} eV "
              f"-> 1s binding {E1S_MEAS} meV")
    spectra = {"EMT": sp_emt}
    for k, (Vc, rc) in models.items():
        if k != "EMT":
            spectra[k] = spectrum(mod, Vc, rc)

    Ei = -E1S_MEAS / RYS          # measured ground state, used for all transition energies
    print("\nLines of the A1 ground state, transition energies with the measured 1s(A1) = 45.59 meV")
    print("  per-polarization cubic average |r|^2 = |Z|^2/3 (p0) or 2|X|^2/3 (p+-) [A^2]; f = 2 m_e omega |r|^2")
    lines_out = {}
    for key, s in spectra.items():
        lbk = bound_lines(s, 3)
        row = []
        for k in ("z", "x"):
            for nm, th, w in zip(names[k], lbk[k][0], lbk[k][1]):
                bind = MEAS_BIND.get(nm, -th * RYS)
                om = E1S_MEAS - bind                         # meV
                r2 = (1 if k == "z" else 2) * w / 3 * AS**2  # A^2, cubic average per polarization
                f = 2 * 0.51099895e6 * om * 1e-3 * r2 / HBARC**2  # 2 m_e omega r^2, dimensionless
                row.append((nm, om, r2, f))
        lines_out[key] = row
        print(f"  [{key}]")
        for nm, om, r2, f in row:
            print(f"    1s(A1) -> {nm:5s} at {om:6.2f} meV: |r|^2 = {r2:8.2f} A^2, f = {f:.4f}")
    # continuum share of the dipole strength
    for key, s in spectra.items():
        wt = {"z": 1 / 3, "x": 2 / 3}
        tot = sum(wt[k] * (s[k + "_trk"] + (s["E0"] - Ei) * np.sum(s[k][1]) * 0 ) for k in ("z", "x"))
        bnd = sum(wt[k] * np.sum(((s[k][0] - s["E0"]) * s[k][1])[s[k][0] < 0]) for k in ("z", "x"))
        print(f"  [{key}] TRK (own E0) total {tot:.4f} (reduced; 1 for x, gamma for z, cubic avg (gamma+2)/3 = "
              f"{(GAM+2)/3:.4f}); bound lines carry {bnd/tot:.3f}, continuum {1-bnd/tot:.3f}")

    # ---------------- static polarizability and Clausius-Mossotti density
    print("\nStatic polarizability (cubic average) and the Clausius-Mossotti divergence")
    pol = {}
    for key, s in spectra.items():
        A = static_A(s)               # static response with the model's own ground-state energy
        Abar = (A["z"] + 2 * A["x"]) / 3
        alpha = 8 * np.pi * EPS * Abar * AS**3          # A^3 (HL)
        nc = 3 / (8 * np.pi * Abar * AS**3) * 1e24     # cm^-3
        pol[key] = (Abar, alpha, nc)
        print(f"  [{key}] A_z = {A['z']:.4f}, A_x = {A['x']:.4f}, Abar = (A_z + 2A_x)/3 = {Abar:.4f} a*^2/Ry*; "
              f"alpha_pol/eps_host = {alpha/EPS:.4g} A^3 = {alpha/EPS/(4*np.pi)*1e-24:.3e} cm^3 (x 4pi, HL); "
              f"Clausius-Mossotti density n = {nc:.3e} cm^-3")
    for key, (Abar, alpha, nc) in pol.items():
        for nD in (1e15, 1e17, 1e18, 1.8e18):
            y = nD * 1e-24 * alpha / (3 * EPS)
            print(f"  [{key}] n_D = {nD:.1e}: y = n alpha/(3 eps) = {y:.3f}, static eps_eff/eps_host = "
                  f"{(1+2*y)/(1-y) if y < 1 else float('inf'):.3f}, linear 1 + 3y = {1+3*y:.3f}")
    # isotropic hydrogenic estimate with the radius of the measured binding
    aH = HBARC * ALPHA / (2 * EPS * E1S_MEAS * 1e-3)
    print(f"  hydrogenic radius alpha/(2 eps E_b) = {aH:.2f} A: Clausius-Mossotti n^(1/3) a = (6 pi)^(-1/3) = "
          f"{(6*np.pi)**(-1/3):.3f} -> n = {((6*np.pi)**(-1/3)/aH)**3*1e24:.2e} cm^-3")
    rp, rz = 24.3, 14.0
    ag = (rp * rp * rz) ** (1 / 3)
    print(f"  geometric-mean variational radius (24.3^2 14.0)^(1/3) = {ag:.2f} A")

    # ---------------- convergence of the EMT numbers
    print("\nConvergence (EMT ground state): static Abar and 2p0 |Z|^2")
    def quick(**kw):
        mm = Model(**kw)
        s = spectrum(mm)
        A = static_A(s)
        return (A["z"] + 2 * A["x"]) / 3, bound_lines(s, 1)["z"][1][0], s["E0"]
    ref = quick()
    for kw in ({"lmax": 14}, {"h": 0.015}, {"rmax": 120.0}):
        v = quick(**kw)
        print(f"  {kw}: Abar {v[0]:.5f} (ref {ref[0]:.5f}), 2p0 {v[1]:.5f} (ref {ref[1]:.5f}), E0 {v[2]:.5f} (ref {ref[2]:.5f})")

    rems = {k: {ax: remainder(spectra[k], ax, Ei) for ax in ("z", "x")} for k in spectra}
    for k in spectra:
        print(f"  [{k}] static remainder above {ECUT} Ry* at E_i: z {rems[k]['z']:.4f}, x {rems[k]['x']:.4f} "
              f"(of total z {static_A(spectra[k])['z']:.3f}, x {static_A(spectra[k])['x']:.3f})")
    np.savez(os.path.join(HERE, "donor16_5.npz"),
             **{f"{k}_{ax}_rem": rems[k][ax] for k in spectra for ax in ("z", "x")},
             **{f"{k}_{ax}_th": spectra[k][ax][0] for k in spectra for ax in ("z", "x")},
             **{f"{k}_{ax}_w": spectra[k][ax][1] for k in spectra for ax in ("z", "x")},
             **{f"{k}_E0": spectra[k]["E0"] for k in spectra},
             RYS=RYS, AS=AS, EPS=EPS)
    print("\nwrote donor16_5.npz")
