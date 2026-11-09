"""Worked example 5.5 (Sect. 5.4): the zone-center optical frequency of silicon from frozen-phonon energy differences.
Data: fig5_1_data.npz (fig5_1_qe.sh / fig5_1_data.py: Quantum ESPRESSO 7.6, PBE, SG15 ONCV Si_ONCV_PBE-1.2.upf, ecutwfc 50 Ry,
Gamma-centered 8^3 k grid, a = 5.431 A, two-atom primitive cell). Displacement pattern: atom 1 by -(u/2) n, atom 2 by +(u/2) n,
n = (1,1,1)/sqrt(3), so u is the change of the [111] bond length; E(u) is the energy per cell, F_u the Hellmann-Feynman
generalized force on u. Energy per cell E = (1/2) Phi u^2 + (1/6) Phi3 u^3 + (1/24) Phi4 u^4 + ...
Estimators:  one-sided  2E(+-u)/u^2 = Phi +- Phi3 u/3 + ...      (error first order in u, from the cubic term)
             symmetric  [E(u) + E(-u) - 2E(0)]/u^2 = Phi + Phi4 u^2/12 + ...
             forces     [F_u(-u) - F_u(+u)]/(2u) = Phi + Phi4 u^2/6 + ...
Two-point extrapolation of the symmetric estimator: Phi = [4 S(u1) - S(u2)]/3 with u2 = 2 u1 (Richardson; removes u^2 term).
Frequency: the coordinate u carries the reduced mass M/2 (the two atoms move by u/2 in opposite directions, kinetic energy
(1/2)(M/2) udot^2), so omega = (2 Phi / M)^{1/2}. M = 28.0855 u (natural Si, as in the phonon runs).
Comparison values: DFPT at the same settings (Sect. 5.1, fig5_1.py) 63.7 meV; representative DFPT (60 Ry, 12^3 k; Sect. 5.2)
63.69 meV; measured 15.5 THz = 64.1 meV (Nilsson and Nelin, Phys. Rev. B 6, 3777 (1972)).
Run: python we5_5.py
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
d = np.load(os.path.join(HERE, "fig5_1_data.npz"))
u, E, F = d["u"], d["E"], d["Fu"]
AMU_EV = 931.49410242e6          # eV per atomic mass unit (CODATA 2018)
HBARC = 1973.269804              # eV Angstrom
M = 28.0855 * AMU_EV             # eV
E0 = E[np.argmin(np.abs(u))]


def at(x):
    return E[np.argmin(np.abs(u - x))], F[np.argmin(np.abs(u - x))]


def omega_meV(phi):              # phi in eV/A^2 -> hbar omega in meV
    return 1e3 * HBARC * np.sqrt(2 * phi / M)


S = {}
for h in (0.03, 0.06, 0.10):
    Ep, Fp = at(h); Em, Fm = at(-h)
    one_p, one_m = 2 * (Ep - E0) / h ** 2, 2 * (Em - E0) / h ** 2
    sym = (Ep + Em - 2 * E0) / h ** 2
    frc = (Fm - Fp) / (2 * h)
    S[h] = sym
    print(f"u = {h:.2f} A: E(+u) = {1e3*Ep:7.3f} meV, E(-u) = {1e3*Em:7.3f} meV")
    print(f"   one-sided Phi (+u) = {one_p:6.3f}, (-u) = {one_m:6.3f} eV/A^2  -> omega {omega_meV(one_p):5.2f}, {omega_meV(one_m):5.2f} meV")
    print(f"   symmetric Phi = {sym:6.3f} eV/A^2 -> omega = {omega_meV(sym):5.2f} meV;  forces Phi = {frc:6.3f} -> {omega_meV(frc):5.2f} meV")
    print(f"   one-sided spread (Phi(-u)-Phi(+u))/2 = {(one_m-one_p)/2:.3f} eV/A^2 = Phi3 u/3 -> Phi3 = {-3*(one_m-one_p)/2/h:6.1f} eV/A^3")
rich = (4 * S[0.03] - S[0.06]) / 3
print(f"Richardson (0.03, 0.06): Phi = {rich:.3f} eV/A^2 -> omega = {omega_meV(rich):.2f} meV")
print(f"Phi4 from symmetric estimators: {12*(S[0.06]-S[0.03])/(0.06**2-0.03**2):.0f} eV/A^4")
for ref, nm in ((63.7, "DFPT 50 Ry/8^3"), (63.69, "DFPT 60 Ry/12^3"), (64.1, "measured")):
    print(f"symmetric u=0.03 vs {nm} {ref} meV: {100*(omega_meV(S[0.03])-ref)/ref:+.2f} %")
