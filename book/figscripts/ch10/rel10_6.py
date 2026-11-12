"""Numbers of Sect. 10.6 on relativistic corrections: shell velocities, Foldy-Wouthuysen corrections to the density
vertex and the scalar density, the next order, and the mass-velocity and orbit-orbit shifts of the f-sum rule.
Natural units; energies in eV. Run time a few seconds once core10_6_orbitals.npz exists (else ~2 min).

Inputs
  [orbitals] core10_6.py (ld1.x all-electron atoms, PBE, scalar-relativistic; Fig. 3.10 files). <p^2> of a shell is
     int p^4 phi^2 dp with phi normalized to int p^2 phi^2 dp = 1; <v^2> = <p^2>/m_e^2.
  [binding] X-Ray Data Booklet Table 1-1 (Williams 2009): Ge 3d5/2 29.2, 3d3/2 29.8 eV (splitting 0.6 eV,
     centroid 29.44 eV).
  [vertex] eq:C.15-vertex: exp(iq.r) -> exp(iq.r)[1 - q^2/8m^2 + (i/4m^2) sigma.(q x p)].
  [scalar] eq:8.1-scalar and eq:C.15-bilinears: psibar psi = n_e - T_e/m_e, relative correction <v^2>/2.
  [mass-velocity f-sum] eq:4.3-mv: delta_mv = -(5/3) Kbar/m_e - q^2/4m_e^2, Kbar = kinetic energy per electron of
     the nonrelativistic all-electron PBE atom (ld1.x printout Ekin, ../ch03/ld1/si_r0.out, ge_r0.out); for Si this is
     checked against Sect. 4.3, which used the virial theorem with the Roothaan-Hartree-Fock energy -288.854 Ha of
     Bunge, Barrientos and Bunge (1993).  1 Ha = 27.211386 eV.
  [orbit-orbit f-sum] eq:10.6-oo (derived in the text): delta_oo(q -> pairs with q r_ij << 1) = -(4/3) E_ee/(N_e m_e),
     with E_ee = alpha <sum_{i<j} 1/r_ij> estimated as E_H + E_xc of the nonrelativistic all-electron PBE atoms,
     ../ch03/ld1/si_r0.out and ge_r0.out (ld1.x printout: Eh, Exc).
  [2509.14534] Ge, Sheng and Xing: xenon inner shells with Z_eff ~ 50, recoil energies 10-50 keV (Sect. 1, Sect. 5.2).
"""
import os
import re
import numpy as np
import core10_6 as c

ME, ALPHA = c.ME, c.ALPHA
HA = 27.211386
HERE = os.path.dirname(os.path.abspath(__file__))


def ld1_energy(name, key):
    txt = open(os.path.join(HERE, "..", "ch03", "ld1", name + ".out")).read()
    return float(re.search(rf"{key}\s*=\s*([-\d.]+)\s*Ry,\s*([-\d.]+)\s*Ha", txt).group(2))


print("--- shell velocities <v^2> = <p^2>/m^2 (direct from the momentum-space orbitals)")
v2 = {}
for mat in ("Si", "Ge"):
    for h, s in c.atom(mat).items():
        p = s.k
        mask = p > 0
        p2 = np.trapezoid(p[mask] ** 4 * s.phi2[mask], p[mask])
        v2[(mat, h)] = p2 / ME ** 2
        print(f"{mat} {h}: <p^2>^(1/2) = {np.sqrt(p2) / 1e3:.2f} keV, <v^2> = {p2 / ME ** 2:.2e}, "
              f"kinetic energy {p2 / (2 * ME):.0f} eV, <r> = {s.rmean:.3f} bohr")
for z, lab in ((14, "Si 1s"), (32, "Ge 1s")):
    print(f"{lab}: (Z alpha)^2 = {(z * ALPHA) ** 2:.4f}")

print("--- density vertex, eq:C.15-vertex")
for qk in (11.2, 15.0, 30.0, 46.0):
    q = qk * 1e3
    print(f"q = {qk} keV: scalar |rho|^2 change q^2/4m^2 = {q ** 2 / (4 * ME ** 2):.1e}; spin term amplitude "
          f"q p/4m^2 with Ge 3d p_rms: {q * np.sqrt(v2[('Ge', '3D')]) * ME / (4 * ME ** 2):.1e}, "
          f"squared {(q * np.sqrt(v2[('Ge', '3D')]) * ME / (4 * ME ** 2)) ** 2:.1e}")
print("--- scalar density: relative correction <v^2>/2")
for k in (("Ge", "3D"), ("Si", "2P"), ("Si", "2S"), ("Ge", "4P")):
    print(f"{k}: {v2[k] / 2:.1e}")
print("--- Ge 3d spin-orbit splitting / binding: 0.6 / 29.44 =", f"{0.6 / 29.44:.3f}")
print("--- next order: <v^2>^2 for Ge 3d =", f"{v2[('Ge', '3D')] ** 2:.1e}", "; Si 2p", f"{v2[('Si', '2P')] ** 2:.1e}")
print("--- Dirac s-wave cusp factor (q/Z alpha m)^((Z alpha)^2) at the openings of the s shells")
for lab, z, qk in (("Si 2s", 14, 57.0), ("Ge 3s", 32, 68.0), ("Ge 1s at 10 Z alpha m", 32, 10 * 32 * ALPHA * ME / 1e3)):
    za = z * ALPHA
    print(f"{lab}: q = {qk:.0f} keV, factor {(qk * 1e3 / (za * ME)) ** (za ** 2):.4f}")
print("--- 2509.14534 regime: xenon Z_eff = 50: (Z alpha)^2 =", f"{(50 * ALPHA) ** 2:.3f}",
      "; recoil 10-50 keV: T/m =", f"{10e3 / ME:.3f}-{50e3 / ME:.3f}",
      "; halo deposits <= 100 eV: T/m <=", f"{100 / ME:.1e}")

print("--- f-sum shifts")
EHF_SI = -288.854
NE = {"Si": 14, "Ge": 32}
res = {}
for mat in ("Si", "Ge"):
    eh, exc, ekin = (ld1_energy(f"{mat.lower()}_r0", k) for k in ("Eh", "Exc", "Ekin"))
    kbar = ekin * HA / NE[mat]
    dmv = 5 / 3 * kbar / ME
    eee = (eh + exc) * HA
    doo = 4 / 3 * eee / (NE[mat] * ME)
    res[mat] = (dmv, doo)
    chk = f" (Sect. 4.3, Hartree-Fock virial: {-EHF_SI * HA / 14:.1f} eV)" if mat == "Si" else ""
    print(f"{mat}: Kbar = {kbar:.1f} eV{chk}; total kinetic {ekin:.2f} Ha; delta_mv = -{dmv:.2e}; "
          f"E_ee = E_H + E_xc = {eh:.2f} + ({exc:.2f}) Ha = {eee:.0f} eV; delta_oo(pairs q r << 1) = -{doo:.2e}; "
          f"oo/mv = {doo / dmv:.2f}; total = -{100 * (dmv + doo):.2f} %")
for qk in (10.0, 30.0, 53.0):
    print(f"q^2/4m^2 at {qk} keV = {(qk * 1e3) ** 2 / (4 * ME ** 2):.1e}")
assert 0.25 < res["Ge"][1] / res["Ge"][0] < 0.40
