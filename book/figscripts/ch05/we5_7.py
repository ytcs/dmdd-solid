"""Worked examples 5.7 and 5.8 (Sect. 5.6): the Debye-Waller exponent of silicon and the displaced oscillator.
Prints every number quoted in Sect. 5.6 and asserts the identities the section states.

Conventions (Sect. 5.6, App. D.15): 2W_kappa(q) = q.B_kappa.q; at a cubic site B_kappa = <u_x^2> 1, so 2W = q^2 <u_x^2>.
At T = 0 the n-phonon weight of the self (single-nucleus) response is Poisson, e^{-2W} (2W)^n / n!.
Inputs and sources:
  Si natural mass 28.0855 u (as the DFPT run and WE 5.4); omega_D = 55.6 meV from the measured elastic constants (WE 5.3, we5_3.py;
  C11, C12, C44 = 165.6, 63.9, 79.5 GPa, Martinez et al. 2019 Table I; a = 5.431 A), recomputed below with we5_4.debye_omega.
  DFPT density of states: fig5_2_data.npz (PBE, 6^3 Q grid, 48^3 tetrahedron DOS, cm^-1), as in we5_4.py.
  Reference <u_x^2> = 0.005941 A^2 at 293 K [Flensburg and Stewart, PRB 60, 284 (1999)] (as Sects. 5.1, 5.3).
  Bond coordinate of Sect. 5.1: zero-point length l_zp = 0.048 A (fig5_1.py; reduced mass M/2 of a 28Si pair, PBE optical 63.7 meV);
  measured optical phonon 64.1 meV (15.5 THz; Nilsson and Nelin 1972) used for the oscillator of WE 5.8.
Run: python we5_7.py   (numpy, scipy)
"""
import os
import sys
from math import factorial
import numpy as np
from scipy.special import iv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from we5_4 import debye_omega, debye_u2, dos_u2, HBARC, KB, U_EV, CM, A2  # noqa: E402  (we5_4 prints its own numbers on import)

print('\n' + '=' * 30 + ' Sect. 5.6 ' + '=' * 30)
M = 28.0855 * U_EV
T0, T293 = 0.0, 293 * KB
A2_EV = 1 / HBARC ** 2                     # 1 A^2 in eV^-2

# ---------------- DFPT density of states (per atom, normalized to 3) ----------------
d = np.load(os.path.join(HERE, 'fig5_2_data.npz'))
w = d['dos'][:, 0] * CM
g = d['dos'][:, 1] / CM
g *= 6 / np.trapezoid(g, w)
ga = g / 2
m = w > 0
w, ga = w[m], ga[m]

ux2 = {}
ux2['DFPT', 0] = A2(dos_u2(w, ga, M, T0)) / 3
ux2['DFPT', 293] = A2(dos_u2(w, ga, M, T293)) / 3
wD = debye_omega(165.6, 63.9, 79.5, 5.431, 28.0855)[0]
ux2['Debye', 0] = A2(debye_u2(M, wD, T0)[0]) / 3
ux2['Debye', 293] = A2(debye_u2(M, wD, T293)[0]) / 3
ux2['ref', 293] = 0.005941
print('omega_D = %.2f meV' % (wD * 1e3))
for k, v in ux2.items():
    print('<u_x^2> %-5s %3d K = %.4e A^2' % (k[0], k[1], v))

# ---------------- WE 5.7: 2W at q = 10 and 50 keV ----------------
print('\nWE 5.7')
for q in (10e3, 50e3):
    ER = q ** 2 / (2 * M)
    print('q = %2.0f keV: q^2 = %.3e eV^2, E_R = q^2/2M = %.3f meV' % (q / 1e3, q ** 2, ER * 1e3))
    for k, v in ux2.items():
        W2 = q ** 2 * v * A2_EV
        print('   2W (%-5s %3d K) = %.4f   e^{-2W} = %.4f' % (k[0], k[1], W2, np.exp(-W2)))
    W2 = q ** 2 * ux2['DFPT', 0] * A2_EV
    P = [np.exp(-W2) * W2 ** n / factorial(n) for n in range(6)]
    print('   T = 0 Poisson weights n = 0..4:', ' '.join('%.4f' % p for p in P[:5]),
          ' n >= 2: %.4f, n >= 3: %.4f' % (1 - P[0] - P[1], 1 - P[0] - P[1] - P[2]))
    print('   Debye/DFPT 2W ratio: 0 K %.3f, 293 K %.3f' % (ux2['Debye', 0] / ux2['DFPT', 0], ux2['Debye', 293] / ux2['DFPT', 293]))
for k in [('DFPT', 0), ('DFPT', 293), ('ref', 293), ('Debye', 0)]:
    print('q at which 2W = 1 (%s %d K): %.1f keV  (= %.2f A^-1)' % (k[0], k[1], HBARC / np.sqrt(ux2[k]) / 1e3, 1 / np.sqrt(ux2[k])))
# T = 0: E_R / 2W = 1 / (2 M <u_x^2>) = <omega^-1>^-1 (per-atom DOS normalized to 3)
inv_mean = 1 / (np.trapezoid(ga / w, w) / 3)
print('E_R/2W at T = 0 = 1/(2M<u_x^2>) = %.2f meV; <omega^-1>^-1 = %.2f meV'
      % (1 / (2 * M * ux2['DFPT', 0] * A2_EV) * 1e3, inv_mean * 1e3))
assert abs(1 / (2 * M * ux2['DFPT', 0] * A2_EV) / inv_mean - 1) < 1e-10
# G (shortest reciprocal vector of fcc Si) for orientation
a = 5.431
G111 = np.sqrt(3) * 2 * np.pi / a
print('|G_111| = %.3f A^-1 = %.2f keV; 2W(G111, 0 K, DFPT) = %.4f; e^{-2W} at 293 K (ref) = %.4f'
      % (G111, G111 * HBARC / 1e3, G111 ** 2 * ux2['DFPT', 0], np.exp(-G111 ** 2 * ux2['ref', 293])))

# ---------------- sum rules of the self response from the DOS (T = 0 and 293 K) ----------------
# one-phonon spectrum per unit 2W: q.C(t).q = (q^2/3) int dw g_a(w)/(2Mw) [(n+1) e^{-iwt} + n e^{iwt}]
for T in (T0, T293):
    n = np.zeros_like(w) if T == 0 else 1 / np.expm1(w / T)
    amp = ga / (2 * M * w) / 3                   # per unit q^2
    W2_per_q2 = np.trapezoid(amp * (2 * n + 1), w)
    first = np.trapezoid(amp * w * ((n + 1) - n), w)  # first moment of q.C(t).q per q^2: i d/dt at t = 0
    print('T = %3.0f K: first moment per q^2 = %.6e eV^-1 ; 1/(2M) = %.6e eV^-1' % (T / KB, first, 1 / (2 * M)))
    assert abs(first * 2 * M - 1) < 2e-3                # completeness: mean energy = E_R at any T (DOS norm 3 per atom)

# multiphonon spectrum at q = 50 keV, T = 0, by repeated convolution: total weight 1, mean energy E_R
q = 50e3
dw = 0.05e-3
grid = np.arange(0, 1.0, dw)
p1 = np.interp(grid, w, ga / w, left=0, right=0)
p1 /= np.trapezoid(p1, grid)                      # normalized one-phonon distribution p(omega) at T = 0
W2 = q ** 2 * ux2['DFPT', 0] * A2_EV
spec = np.zeros_like(grid)
pn = None
tot, mean = np.exp(-W2), 0.0
for nph in range(1, 25):
    pn = p1.copy() if pn is None else np.convolve(pn, p1)[:len(grid)] * dw
    wt = np.exp(-W2) * W2 ** nph / factorial(nph)
    tot += wt * np.trapezoid(pn, grid)
    mean += wt * np.trapezoid(pn * grid, grid)
print('q = 50 keV, T = 0: total weight %.5f, mean energy %.3f meV vs E_R %.3f meV' % (tot, mean * 1e3, q ** 2 / (2 * M) * 1e3))
assert abs(tot - 1) < 1e-3 and abs(mean / (q ** 2 / (2 * M)) - 1) < 5e-3

# ---------------- WE 5.8: displaced oscillator ----------------
print('\nWE 5.8')
w0 = 64.1e-3
lzp = 0.048          # A, bond coordinate of Sect. 5.1
bond = np.sqrt(3) * a / 4
for S in (2.0,):
    Delta = 2 * lzp * np.sqrt(S)
    print('S = %.1f: Delta = 2 l0 sqrt(S) = %.3f A = %.1f %% of the bond %.3f A; relaxation energy S w0 = %.1f meV; '
          'Stokes shift 2 S w0 = %.1f meV' % (S, Delta, 100 * Delta / bond, bond, S * w0 * 1e3, 2 * S * w0 * 1e3))
    # coordinate overlap of two ground-state Gaussians displaced by Delta: exp(-Delta^2/(8 l0^2)) = exp(-S/2)
    x = np.linspace(-1, 1.5, 200001)
    psi = lambda x0: (2 * np.pi * lzp ** 2) ** -0.25 * np.exp(-(x - x0) ** 2 / (4 * lzp ** 2))
    ov = np.trapezoid(psi(0) * psi(Delta), x)
    print('   <0_e|0_g> numerical %.6f, e^{-S/2} = %.6f' % (ov, np.exp(-S / 2)))
    assert abs(ov - np.exp(-S / 2)) < 1e-8
    # <1_e|0_g>: psi_1(x) = (x/l0) psi_0(x) ; |<1_e|0_g>|^2 = S e^{-S}
    psi1 = lambda x0: (x - x0) / lzp * psi(x0)
    ov1 = np.trapezoid(psi1(Delta) * psi(0), x)
    print('   |<1_e|0_g>|^2 = %.6f, S e^{-S} = %.6f' % (ov1 ** 2, S * np.exp(-S)))
    assert abs(ov1 ** 2 - S * np.exp(-S)) < 1e-8
    P = [np.exp(-S) * S ** k / factorial(k) for k in range(8)]
    print('   T = 0 weights p = 0..5:', ' '.join('%.4f' % p for p in P[:6]))
    for TK in (300.0,):
        nb = 1 / np.expm1(w0 / (TK * KB))
        z = 2 * S * np.sqrt(nb * (nb + 1))
        Wp = {p: np.exp(-S * (2 * nb + 1)) * ((nb + 1) / nb) ** (p / 2) * iv(p, z) for p in range(-12, 40)}
        print('   T = %.0f K: n = %.4f, S(2n+1) = %.4f, e^{-S(2n+1)} = %.4f, ZPL weight %.4f (T = 0: %.4f), '
              'p = -1: %.4f, p = -2: %.5f, p = 1: %.4f, sum %.6f, mean %.4f'
              % (TK, nb, S * (2 * nb + 1), np.exp(-S * (2 * nb + 1)), Wp[0], P[0], Wp[-1], Wp[-2], Wp[1],
                 sum(Wp.values()), sum(p * v for p, v in Wp.items())))
        assert abs(sum(Wp.values()) - 1) < 1e-9 and abs(sum(p * v for p, v in Wp.items()) - S) < 1e-9
        # detailed balance between Stokes and anti-Stokes lines
        assert abs(Wp[-1] / Wp[1] - np.exp(-w0 / (TK * KB))) < 1e-12
    # ZPL weight at T where n = 0.5 (figure)
    nb = 0.5
    print('   n = 0.5 (T = %.3f w0 = %.0f K for w0 = 64.1 meV)' % (1 / np.log(3), w0 / np.log(3) / KB))
# Einstein-model check: kick with S = E_R / w_E reproduces 2W at T = 0 if w_E = <omega^-1>^-1
print('Einstein kick at q = 50 keV with w_E = %.1f meV: E_R/w_E = %.4f = 2W(T = 0)'
      % (inv_mean * 1e3, (50e3) ** 2 / (2 * M) / inv_mean))
for S in (0.5, 2, 5):
    print('S = %.1f: zero-phonon weight e^{-S} = %.4f; most probable p = %d' % (S, np.exp(-S), int(np.floor(S))))
