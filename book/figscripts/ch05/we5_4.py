"""Worked example 5.4 and Table 5.1 (Sect. 5.3): zero-point and thermal mean-square displacements.
Prints every number quoted in Sect. 5.3 (zero-point lengths, occupations, Debye and full-DOS <u^2>, the table rows).

Conventions (Sect. 5.3): <u^2> = tr B_kappa (all three Cartesian components); <u_x^2> = <u^2>/3 for a site of cubic
symmetry. Per-atom density of states g_ph/n_at, normalized to three modes per atom.
  <u^2> = int dw (g_ph(w)/n_at) coth(w/2T) / (2 M w)                  (equivalent atoms of one species)
  Debye: <u^2> = 9/(4 M w_D) [1 + 4 (T/w_D)^2 int_0^{w_D/T} x dx/(e^x - 1)]   (eq:5.3-debye; App. D.15)
Inputs and sources:
  Si: natural-abundance mass 28.0855 u (as the DFPT run of fig5_2_qe.sh); omega_D from the measured elastic constants
      C11, C12, C44 = 165.6, 63.9, 79.5 GPa [Martinez et al. 2019, Table I] and a = 5.431 A (WE 5.3, we5_3.py: 55.6 meV).
      DFPT density of states: fig5_2_data.npz (PBE, 6^3 Q grid, 48^3 tetrahedron DOS, cm^-1, normalized to 6 per cell).
      Measured <u_x^2> at 293 K: 0.005941 A^2 [Flensburg and Stewart, PRB 60, 284 (1999)] (as Sect. 5.1).
      Measured phonons: Gamma 15.5 THz (64.1 meV), X_TA 4.49 THz [Dolling 1963; Nilsson and Nelin 1972] (as Sect. 5.2).
  Ge: natural mass 72.630 u (IUPAC standard atomic weight); a = 5.658 A (room temperature; Rideau et al.
      2006, Sect. II A, tab:3-materials); C11, C12, C44 = 131, 49, 68 GPa [McSkimin and Andreatch 1963, as
      tabulated in Haxhijaj et al., Table III, "Expt."]; phonons Gamma 9.1, X_TA 2.4, X_LA 7.2, L_TA 1.9 THz
      [Haxhijaj et al., Table IV, "Expt.", from the neutron data of Nilsson and Nelin 1971].
  GaAs: Gamma TO 8.13, LO 8.79 THz [Strauch and Dorner 1990, as tabulated in arXiv:2506.16977, Table I];
      DFPT row from tab5_1_gaas_qe.sh (work directory /root/work/5.3, or its small outputs in gaas_cache/), parsed below.
Run: python we5_4.py   (numpy only)
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
U_EV = 931.49410242e6          # atomic mass unit in eV (CODATA 2018)
HBARC = 1973.269804            # eV Angstrom
KB = 8.617333262e-5            # eV/K
THZ = 4.135667696e-3           # eV per THz (h x 1 THz)
CM = 1.239841984e-4            # eV per cm^-1


def debye_omega(C11, C12, C44, a, M_u, nat_cubic=8):
    """omega_D (eV) from cubic elastic constants (GPa), lattice constant a (Angstrom), mass (u); method of we5_3.py."""
    GPA, AMU = 1e9, 1.66053906660e-27
    a_m = a * 1e-10
    rho = nat_cubic * M_u * AMU / a_m ** 3
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if i == j == k == l:
                        C[i, j, k, l] = C11 * GPA
                    elif i == j and k == l:
                        C[i, j, k, l] = C12 * GPA
                    elif (i == k and j == l) or (i == l and j == k):
                        C[i, j, k, l] = C44 * GPA
    x, w = np.polynomial.legendre.leggauss(200)
    phis = np.linspace(0, 2 * np.pi, 400, endpoint=False)
    inv3 = np.zeros(3)
    for ct, wt in zip(x, w):
        st = np.sqrt(1 - ct ** 2)
        for p in phis:
            qh = np.array([st * np.cos(p), st * np.sin(p), ct])
            ev = np.sort(np.linalg.eigvalsh(np.einsum('ijkl,j,l->ik', C, qh, qh)))[::-1]
            inv3 += wt * (2 * np.pi / len(phis)) * (ev / rho) ** -1.5
    inv3 /= 4 * np.pi
    cbar = (3 / inv3.sum()) ** (1 / 3)
    QD = (6 * np.pi ** 2 * nat_cubic / a_m ** 3) ** (1 / 3)
    hbar_SI, ev_SI = 1.054571817e-34, 1.602176634e-19
    return hbar_SI * cbar * QD / ev_SI, cbar, rho


def debye_u2(M_eV, wD, T):
    """<u^2> (eV^-2) in the Debye model, per atom, three components."""
    if T == 0:
        br = 1.0
    else:
        y = wD / T
        xs = np.linspace(1e-9, y, 200001)
        br = 1 + 4 * (T / wD) ** 2 * np.trapezoid(xs / np.expm1(xs), xs)
    return 9 / (4 * M_eV * wD) * br, br


def dos_u2(w, g_atom, M_eV, T):
    """<u^2> (eV^-2) from a per-atom DOS g_atom(w) (per eV, normalized to 3), w in eV."""
    m = w > 0
    w, g = w[m], g_atom[m]
    f = np.ones_like(w) if T == 0 else 1 / np.tanh(w / (2 * T))
    return np.trapezoid(g * f / (2 * M_eV * w), w)


def A2(x):          # eV^-2 -> Angstrom^2
    return x * HBARC ** 2


T300, T293 = 300 * KB, 293 * KB

# ---------------- zero-point lengths and occupations (silicon) ----------------
M_si = 28.0855 * U_EV
Mcell = 2 * M_si
print('M_Si = %.3f GeV, M_cell = %.3f GeV' % (M_si / 1e9, Mcell / 1e9))
w_opt = 15.5 * THZ
print('optical phonon 15.5 THz = %.1f meV' % (w_opt * 1e3))
for name, wq in [('Gamma optical 64.1 meV', 0.0641), ('X TA 4.49 THz', 4.49 * THZ), ('5 meV acoustic', 0.005)]:
    ell = HBARC / np.sqrt(2 * Mcell * wq)
    print('ell_Qnu (%s) = %.4f A ; n_B(300 K) = %.3f ; n_B(293 K) = %.3f ; n_B(10 mK) = %.1e'
          % (name, ell, 1 / np.expm1(wq / T300), 1 / np.expm1(wq / T293), 1 / np.expm1(min(wq / (0.01 * KB), 700))))
print('X TA = %.1f meV' % (4.49 * THZ * 1e3))
# bond coordinate of Sect. 5.1: ell_zp = (M omega)^-1/2 with M the natural mass used there (26.16 GeV in 5.1)
print('5.1 bond-coordinate length (M omega_opt)^-1/2 with M = 26.16 GeV, 63.7 meV: %.4f A'
      % (HBARC / np.sqrt(M_si * 0.0637)))
print('half of it (each atom moves u/2): %.4f A; ell_Gamma,opt with PBE 63.7 meV and natural mass: %.4f A'
      % (HBARC / np.sqrt(M_si * 0.0637) / 2, HBARC / np.sqrt(2 * Mcell * 0.0637)))

# ---------------- Debye model, silicon ----------------
wD_si, cb_si, rho_si = debye_omega(165.6, 63.9, 79.5, 5.431, 28.0855)
print('\nSi Debye: cbar = %.3f km/s, omega_D = %.2f meV, Theta_D = %.1f K, rho = %.3f g/cm3'
      % (cb_si / 1e3, wD_si * 1e3, wD_si / KB, rho_si / 1e3))
for T in [0, T293, T300]:
    u2, br = debye_u2(M_si, wD_si, T)
    if T > 0:
        print('  omega_D/T = %.4f, T/omega_D = %.4f, integral int_0^y x/(e^x-1) = %.4f'
              % (wD_si / T, T / wD_si, (br - 1) / (4 * (T / wD_si) ** 2)))
    print('  T = %5.1f K: bracket %.4f, <u^2> = %.5f A^2, <u_x^2> = %.6f A^2, sqrt<u_x^2> = %.4f A, sqrt<u^2> = %.4f A'
          % (T / KB, br, A2(u2), A2(u2) / 3, np.sqrt(A2(u2) / 3), np.sqrt(A2(u2))))
u2c = 9 * T300 / (M_si * wD_si ** 2)
print('  9/(4 M omega_D) = %.4e eV^-2 = %.5f A^2; M omega_D = %.4e eV^2' % (9 / (4 * M_si * wD_si), A2(9 / (4 * M_si * wD_si)), M_si * wD_si))
print('  1/sqrt<u^2>(300 K) as a momentum: %.1f keV; estimate 1/(2 M 30 meV) = %.5f A^2 (rms %.4f A)'
      % (HBARC / np.sqrt(A2(debye_u2(M_si, wD_si, T300)[0])) / 1e3, A2(1 / (2 * M_si * 0.030)), np.sqrt(A2(1 / (2 * M_si * 0.030)))))
print('  classical (equipartition) Debye value at 300 K: <u_x^2> = %.6f A^2' % (A2(u2c) / 3))
u20 = debye_u2(M_si, wD_si, 0)[0]
u2300 = debye_u2(M_si, wD_si, T300)[0]
print('  thermal part at 300 K: %.6f A^2 in <u_x^2>, ratio total/zero-point %.3f' % (A2(u2300 - u20) / 3, u2300 / u20))
print('  T at which the thermal part equals the zero-point part: ', end='')
for TK in np.arange(50, 400, 0.5):
    if debye_u2(M_si, wD_si, TK * KB)[1] >= 2:
        print('%.1f K' % TK)
        break
meas = 0.005941
print('  measured 293 K <u_x^2> = %.6f A^2 (sqrt %.4f A); Debye 293 K / measured = %.3f'
      % (meas, np.sqrt(meas), A2(debye_u2(M_si, wD_si, T293)[0]) / 3 / meas))
print('  Debye-Waller B = 8 pi^2 <u_x^2> (measured) = %.4f A^2' % (8 * np.pi ** 2 * meas))

# ---------------- DFPT density of states, silicon ----------------
d = np.load(os.path.join(HERE, 'fig5_2_data.npz'))
wcm, gcm = d['dos'][:, 0], d['dos'][:, 1]
w = wcm * CM
g = gcm / CM                                   # per eV per cell
g *= 6 / np.trapezoid(g, w)                        # renormalize to 3 n_at = 6 modes per cell
g_atom = g / 2
print('\nSi DFPT DOS: norm per atom = %.4f' % np.trapezoid(g_atom, w))
for T in [0, T293, T300]:
    u2 = dos_u2(w, g_atom, M_si, T)
    print('  T = %5.1f K: <u^2> = %.5f A^2, <u_x^2> = %.6f A^2, sqrt<u_x^2> = %.4f A'
          % (T / KB, A2(u2), A2(u2) / 3, np.sqrt(A2(u2) / 3)))
u2d0 = dos_u2(w, g_atom, M_si, 0)
u2d293 = dos_u2(w, g_atom, M_si, T293)
print('  DFPT 293 K / measured = %.3f ; Debye/DFPT at 0 K = %.3f ; at 300 K = %.3f'
      % (A2(u2d293) / 3 / meas, u20 / u2d0, u2300 / dos_u2(w, g_atom, M_si, T300)))
m = w > 0
inv1 = np.trapezoid(g_atom[m] / w[m], w[m]) / 3
inv2 = np.trapezoid(g_atom[m] / w[m] ** 2, w[m]) / 3
print('  per-atom moments: <1/w>^-1 = %.2f meV, <1/w^2>^-1/2 = %.2f meV (Debye: %.2f, %.2f meV)'
      % (1e3 / inv1, 1e3 / np.sqrt(inv2), 1e3 * 2 * wD_si / 3, 1e3 * wD_si / np.sqrt(3)))
# share of the zero-point <u^2> from modes below 20 meV
mm = (w > 0) & (w < 0.020)
print('  zero-point energy per cell (1/2) int g w dw = %.1f meV; mean phonon energy %.2f meV'
      % (0.5 * np.trapezoid(g * w, w) * 1e3, np.trapezoid(g * w, w) / 6 * 1e3))
print('  Debye per cell (9/8) n_at omega_D = %.1f meV' % (9 / 8 * 2 * wD_si * 1e3))
print('  Debye share of zero-point <u^2> below 20 meV: %.3f; Debye share of modes below 20 meV: %.3f'
      % ((0.020 / wD_si) ** 2, (0.020 / wD_si) ** 3))
print('  share of zero-point <u^2> from modes below 20 meV: %.3f (share of modes %.3f)'
      % (np.trapezoid(g_atom[mm] / w[mm], w[mm]) / np.trapezoid(g_atom[m] / w[m], w[m]), np.trapezoid(g_atom[mm], w[mm]) / 3))

# ---------------- germanium ----------------
M_ge = 72.630 * U_EV
wD_ge, cb_ge, rho_ge = debye_omega(131, 49, 68, 5.658, 72.630)
print('\nGe Debye: cbar = %.3f km/s, omega_D = %.2f meV, Theta_D = %.1f K, rho = %.3f g/cm3'
      % (cb_ge / 1e3, wD_ge * 1e3, wD_ge / KB, rho_ge / 1e3))
for T in [0, T300]:
    u2, br = debye_u2(M_ge, wD_ge, T)
    print('  T = %5.1f K: bracket %.4f, <u_x^2> = %.6f A^2, sqrt<u_x^2> = %.4f A' % (T / KB, br, A2(u2) / 3, np.sqrt(A2(u2) / 3)))
for nm, f in [('Gamma', 9.1), ('X_TA', 2.4), ('X_LA', 7.2), ('L_TA', 1.9)]:
    print('  Ge %s %.1f THz = %.1f meV' % (nm, f, f * THZ * 1e3))
print('  Ge/Si Gamma ratio %.3f, sqrt(M_Si/M_Ge) = %.3f' % (9.1 / 15.5, np.sqrt(28.0855 / 72.630)))

# ---------------- GaAs ----------------
for nm, f in [('Gamma TO', 8.13), ('Gamma LO', 8.79)]:
    print('GaAs %s %.2f THz = %.1f meV' % (nm, f, f * THZ * 1e3))
W = os.path.join(HERE, 'gaas_cache')   # small outputs of the run (gaas_cache_extract.py), with eps_inf and Z* of the
if not os.path.exists(os.path.join(W, 'GaAs.dos')):   # 28^3 k grid in the dipole term (gaas_q2r_epsZ.py, Sect. 5.5)
    W = '/root/work/5.3'
if os.path.exists(os.path.join(W, 'GaAs.dos')):
    M_ga, M_as = 69.723 * U_EV, 74.9216 * U_EV
    D = np.loadtxt(os.path.join(W, 'GaAs.dos'))
    wg, gt = D[:, 0] * CM, D[:, 1] / CM
    nrm = 6 / np.trapezoid(gt, wg)
    gGa, gAs = D[:, 2] / CM * nrm, D[:, 3] / CM * nrm      # atom-projected, each normalized to 3
    print('GaAs DFPT: projected norms %.3f %.3f' % (np.trapezoid(gGa, wg), np.trapezoid(gAs, wg)))
    for T in [0, T300]:
        for nm, gp, Mx in [('Ga', gGa, M_ga), ('As', gAs, M_as)]:
            u2 = dos_u2(wg, gp, Mx, T)
            print('  T = %5.1f K %s: <u_x^2> = %.6f A^2, sqrt = %.4f A' % (T / KB, nm, A2(u2) / 3, np.sqrt(A2(u2) / 3)))
    fr = open(os.path.join(W, 'GaAs.freq')).read()
    vals = np.array(fr.split('/', 1)[1].split(), float)
    vals = vals.reshape(4, len(vals) // 4)                 # q (3 or 4 columns, version dependent), then 6 frequencies
    for lab, row in zip(['Gamma[100]', 'X', 'L', 'Gamma[001]'], vals):
        print('  %s: ' % lab + ' '.join('%.2f' % (c * CM / THZ) for c in row[-6:]) + ' THz  = '
              + ' '.join('%.1f' % (c * CM * 1e3) for c in row[-6:]) + ' meV')
    # low-frequency Debye fit: g = 9 w^2 / w_D^3 per atom (two atoms, three modes each): fit 1-4 meV
    tot = (gGa + gAs) / 2
    mfit = (wg > 0.001) & (wg < 0.004)
    coef = np.sum(tot[mfit] * wg[mfit] ** 2) / np.sum(wg[mfit] ** 4)
    wDf = (9 / coef) ** (1 / 3)
    print('  DFPT low-frequency Debye fit (1-4 meV): omega_D = %.2f meV, Theta_D = %.0f K' % (wDf * 1e3, wDf / KB))
else:
    print('GaAs DFPT output not found in', W)
