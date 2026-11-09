"""Worked example 16.5 (we:16-sip-line): the 1s(A1) -> 2p0 line of Si:P for a dark photon at its resonance.
Inputs: line strength |r|^2 per polarization from donor16_5.py (central-cell ground state, r_c = 3.2 A; and the
effective-mass envelope for comparison); line at 45.59 - 11.48 = 34.11 meV (Vinh et al., arXiv:0812.0148, Fig. 1);
narrowest measured full width 0.034 cm^-1 in 28Si and the 2p0 lifetime T1 = 205 ps, 1/T1 = 0.026 cm^-1 (Vinh et al., p. 5);
eps_host = 11.4 (Sect. 7.4); rho_chi = 0.3 GeV/cm^3 (Sect. 1.2), rho_T = 2.33 g/cm^3 (Sect. 3.1), v ~ 1e-3.
Rate (eq:10.7-dp with the loss function of eq:16.5-abs): R = zeta^2 (rho_chi/rho_T) L(m_phi).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import donorspec16_5 as S  # noqa: E402

HBAR_EVS = 6.582119569e-16
YR = 3.15576e7
CM1_MEV = 0.1239842
ND = 1e15
EPSH = S.EPS
W = 45.59 - 11.48

fac = 0.3e9 / 2.33 * 1e3 / HBAR_EVS * YR       # (rho_chi/rho_T) in 1/(kg yr) per unit L
print(f"rho_chi/rho_T = {0.3/2.33:.4f} GeV/g -> {fac:.3e} events per kg-yr per unit L and zeta^2")
for key in ("CC0.10", "EMT"):
    s = S.model(key)
    r2, w = S.line_strength(s, "z", 0)
    f = 2 * 0.51099895e6 * W * 1e-3 * r2 / S.HBARC**2
    I = 4 * np.pi**2 * S.ALPHA * ND * 1e-24 * r2 * S.HBARC          # eV, integral of eps_2^D over the line
    print(f"\n[{key}] 2p0 at {W:.2f} meV: |r|^2 = {r2:.2f} A^2, oscillator strength 2 m_e omega |r|^2 = {f:.3f}")
    print(f"   integral of eps_2^D over the line at n_D = 1e15: 4 pi^2 alpha n_D |r|^2 = {I:.3e} eV")
    for gam_cm in (0.034, 0.026):
        G = gam_cm * CM1_MEV * 1e-3                                    # eV
        e2 = 2 / (np.pi * G) * I
        Llin = e2 / EPSH**2
        A = S.A_of_omega(s, W, gam_cm * CM1_MEV, 1.5)[0]
        eD = S.epsD(A, ND)
        Lf = S.L_full(eD)
        R = fac * Lf
        print(f"   full width {gam_cm} cm^-1 = {G*1e6:.2f} ueV: peak eps_2^D = {e2:.3f} (model incl. background "
              f"{eD.imag:.3f}, Re {eD.real:.4f}); L_lin = {Llin:.3e}; effective medium L = {Lf:.3e} "
              f"({Lf/Llin:.4f} of linear)")
        print(f"      R = {R:.2e} zeta^2 per kg-yr; zeta for 3 events/kg-yr = {np.sqrt(3/R):.2e}")
    Lc = S.L_lin(S.epsD(S.A_of_omega(s, 50.0, 0.1, 1.5)[0], ND))
    print(f"   continuum at 50 meV: L = {Lc:.2e}, R = {fac*Lc:.2e} zeta^2, zeta(3/kg-yr) = {np.sqrt(3/(fac*Lc)):.2e}")
    A = S.A_of_omega(s, W, 0.034 * CM1_MEV, 1.5)[0]
    Lpk = S.L_full(S.epsD(A, ND))
    print(f"   line peak (0.034 cm^-1) over continuum at 50 meV: L ratio {Lpk/Lc:.0f}, zeta ratio {np.sqrt(Lpk/Lc):.1f}")
print(f"\n1/eps_host^2 = 1/{EPSH**2:.1f}")
print(f"Mass window: Gamma/m_phi = {0.034*CM1_MEV*1e-3/(W*1e-3):.2e}; dark-photon line width m v^2/2 at v = 1e-3: "
      f"{W*1e-3*0.5e-6*1e6:.3f} ueV")
print(f"lifetime floor 1/T1 = hbar/205 ps = {HBAR_EVS/205e-12*1e6:.2f} ueV (Vinh: 0.026 cm^-1 = {0.026*CM1_MEV*1e3:.2f} ueV)")
