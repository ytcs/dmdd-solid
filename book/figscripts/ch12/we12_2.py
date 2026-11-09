"""Worked example 12.2 and the other numbers of Sect. 12.2 (every number quoted in the text is printed here).

Ge atom at E_R = 1 keV: probabilities from Ibe et al. (arXiv:1707.07258) Table II (excitation; FAC) and ancillary file
(ionization), and from Cox et al. (arXiv:2208.12222) dipole tables (ionization; Dirac-Hartree-Fock), rescaled by q_e^2.
First moment check: sum over final states of dE P = q_e^2 N_e/(2 m_e) = (N_e m_e/m_A) E_R at dipole order (eq:4.3-TRK,
eq:8.6-fsum-k with delta M = N_e m_e).
Time scales: nuclear radius / v_max for the kick (as in Sect. 6.1: Si 3.5 fm -> 4e-21 s); Ge Helm radius 4.77 fm (Sect. 2.2).
Lattice pull-back factor [1 - (omega/dE)^2]^-2 (Sect. 6.1) with the Ge zone-center optical phonon 37.6 meV (Table 5.1).
Helium lines: NIST ASD oscillator strengths (atom12_2.he_bound).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atom12_2 as A  # noqa: E402

HBAR = 6.582119569e-16     # eV s
C = 2.99792458e8           # m/s
VMAX = 2.650e-3


def mchi_for(el, ER):
    """Smallest dark-matter mass whose largest recoil energy 2 mu^2 v_max^2/m_A reaches E_R."""
    mu = np.sqrt(ER * A.MA[el] / 2) / VMAX
    return mu * A.MA[el] / (A.MA[el] - mu)


if __name__ == "__main__":
    ER = 1e3
    el = "Ge"
    v = A.v_recoil(el, ER)
    qe = A.q_e(el, ER)
    s = (qe / A.QE_REF)**2
    print(f"Ge: m_A = {A.MA[el] / 1e9:.4f} GeV; q = {A.MA[el] * v / 1e6:.3f} MeV; v = {v:.4e} = {v * C / 1e3:.1f} km/s; "
          f"q_e = {qe:.2f} eV; scale (q_e/511 eV)^2 = {s:.5f}")
    print(f"   q_e a0 = {qe / (A.ME * A.ALPHA):.4f}; with <r>_4p = 2.90 a0: {2.90 * qe / (A.ME * A.ALPHA):.3f}; "
          f"<r>_3d = 0.74 a0: {0.74 * qe / (A.ME * A.ALPHA):.4f}")
    print(f"   smallest m_chi for E_R = 1 keV: {mchi_for(el, ER) / 1e9:.3f} GeV")
    # ionization, Ibe
    ib = A.ibe_spectra("Ge")
    Pion = {}
    for (n, l), (E, p) in sorted(ib.items()):
        Pion[f"{n}{A.LNAME[l]}"] = np.trapezoid(p, E)
    tot_ion = sum(Pion.values())
    print("   ionization (FAC, q_ref): " + ", ".join(f"{k} {v:.3e}" for k, v in Pion.items()) + f"; total {tot_ion:.4e}")
    print("   ionization at 1 keV:     " + ", ".join(f"{k} {v * s:.3e}" for k, v in Pion.items()) + f"; total {tot_ion * s:.4e}")
    core = sum(v for k, v in Pion.items() if k not in ("4s", "4p"))
    print(f"   cores (n <= 3) at 1 keV: {core * s:.3e}; valence 4s+4p: {(Pion['4s'] + Pion['4p']) * s:.3e}")
    cox = {k: np.trapezoid(p, E) for k, (E, p) in A.cox_dipole("Ge").items()}
    print("   ionization (DHF) at 1 keV: " + ", ".join(f"{k} {v * s:.3e}" for k, v in cox.items())
          + f"; total {sum(cox.values()) * s:.4e}")
    # excitations, Ibe Table II
    exc = A.IBE_GE_EXC
    tot_exc = sum(exc.values())
    val_exc = sum(p for (i, f), p in exc.items() if i in ("4s", "4p"))
    print(f"   bound excitation (Table II, q_ref): total {tot_exc:.4e}, from 4s/4p {val_exc:.4e}, from 3d {exc[('3d', '4p')] + exc[('3d', '5p')]:.3e}")
    print(f"   bound excitation at 1 keV: total {tot_exc * s:.3e}; 4s->4p {exc[('4s', '4p')] * s:.3e}; 3d {(exc[('3d', '4p')] + exc[('3d', '5p')]) * s:.3e}")
    print(f"   all transitions at 1 keV: {(tot_exc + tot_ion) * s:.3e}; ratio exc/ion {tot_exc / tot_ion:.3f}")
    # first moment
    m1_exact = A.QE_REF**2 * A.NE[el] / (2 * A.ME)
    m1_ion = 0.0
    for (n, l), (E, p) in ib.items():
        m1_ion += np.trapezoid(p * (E + A.IBE_GE_E[f"{n}{A.LNAME[l]}"]), E)
    m1_exc = sum(p * (A.IBE_GE_E[i] - A.IBE_GE_E[f]) for (i, f), p in exc.items())
    print(f"   first moment at q_ref: exact {m1_exact:.3f} eV; ionization {m1_ion:.3f} + excitation {m1_exc:.3f} = "
          f"{m1_ion + m1_exc:.3f} eV ({(m1_ion + m1_exc) / m1_exact:.3f})")
    print(f"   mean electronic energy per recoil (N_e m_e/m_A) E_R = {A.NE[el] * A.ME / A.MA[el] * ER:.4f} eV; "
          f"N_e m_e/m_A = {A.NE[el] * A.ME / A.MA[el]:.3e}")
    print(f"   mean energy of an ionizing event: {m1_ion / tot_ion:.0f} eV; of a 3d ionization: "
          f"{np.trapezoid(ib[(3, 2)][1] * (ib[(3, 2)][0] + 35.0), ib[(3, 2)][0]) / Pion['3d']:.0f} eV")
    # time scales
    tau = 4.77e-15 / (VMAX * C)
    for name, dE in (("3d (29.4 eV)", 29.4), ("4p (7.9 eV)", 7.9)):
        print(f"   suddenness {name}: tau_acc = {tau:.2e} s, dE tau = {dE * tau / HBAR:.2e}, "
              f"pull-back factor = {1 / (1 - (0.0376 / dE)**2)**2 - 1:.2e} above one")
    print(f"   x_R = E_R/<omega> = {ER / 23.6e-3:.0f} (Ge <omega> = 23.6 meV, Sect. 11.4)")
    # other atoms at 1 keV
    for e2 in ("Si", "Xe"):
        s2 = (A.q_e(e2, ER) / A.QE_REF)**2
        if e2 == "Si":
            P2 = A.cox_dipole_total("Si")
        else:
            P2 = sum(np.trapezoid(p, E) for E, p in A.ibe_spectra("Xe").values())
        print(f"{e2}: q_e = {A.q_e(e2, ER):.2f} eV, scale {s2:.5f}, P_ion(q_ref) = {P2:.4e}, P_ion(1 keV) = {P2 * s2:.3e}, "
              f"(N_e m_e/m_A)E_R = {A.NE[e2] * A.ME / A.MA[e2] * ER:.4f} eV")
    sp = A.cox_dipole("Si")
    s2 = (A.q_e("Si", ER) / A.QE_REF)**2
    Psi = {k: np.trapezoid(p, E) * s2 for k, (E, p) in sp.items()}
    print("   Si shells at 1 keV: " + ", ".join(f"{k} {v:.3e}" for k, v in Psi.items())
          + f"; cores {Psi['1s'] + Psi['2s'] + Psi['2p']:.3e}")
    # hydrogen and m_A vs nucleus mass
    for e2 in ("Si", "Ge"):
        print(f"{e2}: 2 N_e m_e/m_A (relative change of P_Mig from m_A vs M) = {2 * A.NE[e2] * A.ME / A.MA[e2]:.2e}")
    # helium
    terms, tail, tail_f = A.he_bound()
    allb = sum(terms.values()) + tail
    n3 = terms[2] + terms[3]
    print(f"He: P_exc/(v/alpha)^2: 2P {terms[2]:.4f}, 3P {terms[3]:.4f}, n<=3 {n3:.4f}, all {allb:.4f} (tail {tail:.4f}); n<=3/all {n3 / allb:.3f}")
    for vN in (1e-4, 3e-4):
        print(f"   v = {vN:.0e}: (v/alpha)^2 = {(vN / A.ALPHA)**2:.3e}; P(2P) = {terms[2] * (vN / A.ALPHA)**2:.2e}; "
              f"all lines {allb * (vN / A.ALPHA)**2:.2e}")
    rows = A.he_lines()
    print("   He f values n=2..4:", [(n, f) for n, f, _ in rows[:3]], " bound f sum", sum(f for _, f, _ in rows) + tail_f)
    # He at E_R where 2P opens: kinematics not needed; m_e alpha^2
    print(f"m_e alpha^2 = {A.HARTREE:.4f} eV")
    # helium at E_R = 10 eV (below the 20.6 eV first excitation)
    vHe = A.v_recoil("He", 10.0)
    print(f"He at E_R = 10 eV: v_A = {vHe:.3e}, (v/alpha)^2 = {(vHe / A.ALPHA)**2:.3e}, P(2P) = {terms[2] * (vHe / A.ALPHA)**2:.2e}, "
          f"P(all) = {allb * (vHe / A.ALPHA)**2:.2e}, smallest m_chi {mchi_for('He', 10.0) / 1e6:.1f} MeV, "
          f"1/2 m v_max^2 there {0.5 * mchi_for('He', 10.0) * VMAX**2:.0f} eV")
    # core radii vs bond (Sect. 10.6 orbitals, <r> in bohr) and lattice pull-back for Si 2p
    for name, r in (("Si 2p", 0.538), ("Ge 3d", 0.737), ("Si 3p", 2.795), ("Ge 4p", 2.899)):
        print(f"   <r> {name} = {r * 0.529177:.2f} A")
    print(f"   Si 2p pull-back: {1 / (1 - (0.0641 / 99.55)**2)**2 - 1:.1e}; Si tau_acc dE(2p) = {99.55 * 3.5e-15 / (VMAX * C) / HBAR:.1e}")
    # helium: largest xi_D for m_chi = 1 GeV; hydrogen dipole error there (cached exact sums of limit12_2b.py)
    mu = 1e9 * A.MA["He"] / (1e9 + A.MA["He"])
    xiHe = 2 * mu * VMAX / A.MA["He"] / A.ALPHA
    d = np.load(os.path.join(HERE, "limit12_2b_exact.npz"))
    rH = np.interp(xiHe, d["xi"], d["ex"] / d["xi"]**2)
    print(f"He, m_chi = 1 GeV: largest xi_D = {xiHe:.3f}; hydrogen dipole/exact bound there - 1 = {0.71659 / rH - 1:.3f}")
