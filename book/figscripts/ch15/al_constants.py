"""One set of aluminum constants for the book (Ch. 15, and the aluminum numbers of Sects. 6.4, 7.2 and App. E.20).

Free-electron gas with the bare electron mass (m* = m_e): fcc, a = 4.05 A (state/DATA-ADDENDA.csv, Al a_exp,
arXiv:2109.13551 Table 2), three valence electrons per atom, four atoms per cubic cell, so
    n_e = 12/a^3,  k_F = (3 pi^2 n_e)^(1/3),  v_F = k_F/m_e,  E_F = k_F^2/2m_e,
    omega_p^2 = e^2 n_e/m_e,  k_TF^2 = 4 alpha m_e k_F/pi = 2 e^2 N_F  (N_F = m_e k_F/2pi^2 per spin),
in Heaviside-Lorentz natural units (e^2 = 4 pi alpha).  Then k_TF^2 v_F^2/3 = omega_p^2 exactly.
Sound speeds from the 0 K elastic constants of Kamm and Alers (1964), as quoted by Malica and Dal Corso,
arXiv:2109.13551 Table 2 row 'Expt.' (C11 = 114.3, C12 = 61.9, C44 = 31.6 GPa; state/DATA-ADDENDA.csv, which supersedes
the room-temperature Kittel set C11 = 106.8, C44 = 28.2 GPa per state/CORRECTIONS.md Sect. 19.13(g)), with
the near-0 K density 2.73 g cm^-3 (rho_T = 2.70 g cm^-3 at room temperature is used for rates):
c_LA = (C11/rho)^(1/2), c_TA = (C44/rho)^(1/2) along [100].
Gap: Delta_BCS = 0.18 meV (measured; Savrasov and Savrasov 1996, Table III).  v_max = 2.650e-3 (Sect. 1.2).
Run: python al_constants.py  (writes al_constants.log).  Imported by the other Ch. 15 scripts.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

ALPHA = 1 / 137.035999084
E2 = 4 * np.pi * ALPHA
ME = 510998.95                 # eV
HBARC = 1973.269804            # eV A
C_MS = 2.99792458e8            # m/s
HBAR_EVS = 6.582119569e-16     # eV s
VMAX = 2.650e-3

A_AL = 4.05                                   # A
NE = 12 / (A_AL / HBARC) ** 3                 # eV^3
KF = (3 * np.pi**2 * NE) ** (1 / 3)           # eV
VF = KF / ME
EF = KF**2 / (2 * ME)
WP = np.sqrt(E2 * NE / ME)                    # free-electron plasma frequency, eV
NF = ME * KF / (2 * np.pi**2)                 # per spin, eV^2
KTF = np.sqrt(2 * E2 * NF)                    # eV
RHO_T = 2700.0                                # kg/m^3, room temperature (rates)
RHO_0K = 2730.0                               # kg/m^3 near 0 K (a = 4.032 A at 4 K), for the 0 K sound speeds
C11, C12, C44 = 114.3e9, 61.9e9, 31.6e9       # Pa, 0 K (Kamm-Alers via 2109.13551)
C_LA = np.sqrt(C11 / RHO_0K) / C_MS
C_TA = np.sqrt(C44 / RHO_0K) / C_MS
DELTA = 0.18e-3                               # eV
WP_INTRA = 12.29                              # eV, computed intraband value (Savrasov and Savrasov 1996, Table IV)


def _report():
    um = HBARC * 1e-4      # 1 eV^-1 = 1973 A = 0.1973 um
    lines = [
        f"a = {A_AL} A, n_e = {NE / HBARC**3 * 1e24:.4e} cm^-3 (12 electrons per cube)",
        f"k_F = {KF:.1f} eV = {KF / HBARC:.4f} A^-1",
        f"v_F = k_F/m_e = {VF:.5e} = {VF * C_MS:.4e} m/s",
        f"E_F = {EF:.3f} eV",
        f"omega_p (free electrons) = {WP:.3f} eV",
        f"k_TF = {KTF:.1f} eV ; check k_TF^2 v_F^2/3 / omega_p^2 = {KTF**2 * VF**2 / 3 / WP**2:.6f}",
        f"N_F (per spin) = {NF:.4e} eV^2",
        f"v_max/v_F = {VMAX / VF:.4f} ; v_F/v_max = {VF / VMAX:.3f} ; v_max/(2 v_F) = {VMAX / (2 * VF):.4f}",
        f"c_LA = {C_LA * C_MS:.1f} m/s = {C_LA:.4e} ; c_TA = {C_TA * C_MS:.1f} m/s = {C_TA:.4e}",
        f"(c_LA/v_max)^2 = {(C_LA / VMAX)**2:.2e}",
        f"mass below which 2 m v_max c_LA < 2 Delta: {2 * DELTA / (2 * C_LA * VMAX) / 1e3:.2f} keV",
        f"coherence length v_F/(pi Delta) = {VF / (np.pi * DELTA) * um:.3f} um ; v_F/Delta = {VF / DELTA * um:.2f} um",
        f"Delta/E_F = {DELTA / EF:.2e}",
        f"Sect. 7.2 numbers (bulk gap): v_F/v_max = {VF / VMAX:.2f}; at m_min, q = 2(2 Delta)/v_max = "
        f"{4 * DELTA / VMAX:.4f} eV, 1/q = {VMAX / (4 * DELTA) * um:.3f} um, v_F q/Delta = {VF * 4 * DELTA / VMAX / DELTA:.2f}, "
        f"Delta/(v_F q) = {VMAX / (4 * VF):.3f}; coherence length / (1/q) = {VF / (np.pi * DELTA) / (VMAX / (4 * DELTA)):.2f}",
    ]
    return lines


if __name__ == "__main__":
    out = _report()
    print("\n".join(out))
    with open(os.path.join(HERE, "al_constants.log"), "w") as f:
        f.write("\n".join(out) + "\n")
