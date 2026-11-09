"""Worked example 16.6 (we:16-fyield): the yield of F centers per keV of fluorine recoil in LiF.

Steps (inputs in cc16_6.py):
  1. Lindhard partition of a 1 keV fluorine recoil (Z = 9, A = 19, single-element form; arXiv:1803.02903 Eq. (3)):
     electronic share y_L E_R, damage energy T_d = (1 - y_L) E_R.
  2. Kinchin-Pease count n_v = T_d / (2 E_d) with E_d = 27 eV (as quoted by Cogswell et al. 2021, p. 2 and Table I);
     also with T_d = E_R (no electronic loss), the largest count the formula allows.
  3. Anion share: at most all displacements (upper value); one half if the two sublattices share them equally (stated
     as an assumption, not computed).
  4. Electrons: the electronic share divided by the band gap 14.2 eV bounds the number of electron-hole pairs from above
     (each pair costs at least the gap).
  5. Sub-GeV endpoints: E_R^max of a fluorine recoil for m_chi = 0.2, 0.3, 0.5 GeV (eq. 1.3-ERmax) and their counts.
Run: python we16_6.py > we16_6.log
"""
import numpy as np
import cc16_6 as C

E1 = 1000.0
y, Td, k, eps, g = C.lindhard(np.array([E1]), 9, 19)
y, Td = float(y[0]), float(Td[0])
n_lind = Td / (2 * C.E_D_LIF)
n_max = E1 / (2 * C.E_D_LIF)
print("1 keV fluorine recoil: k = %.4f, eps = %.4f, g = %.3f, y_L = %.4f" % (k, eps[0], g[0], y))
print("  electronic share %.1f eV, damage energy %.1f eV" % (y * E1, Td))
print("  Kinchin-Pease: %.2f displacements (Lindhard T_d), %.2f (T_d = E_R)" % (n_lind, n_max))
print("  F vacancies: <= %.1f (all on the anion sublattice), %.1f (equal share)" % (n_lind, n_lind / 2))
print("  e-h pairs <= %.1f (electronic share / gap %.1f eV)" % (y * E1 / C.GAP_LIF, C.GAP_LIF))
for m in (0.2e9, 0.3e9, 0.5e9):
    em = C.er_max(m, C.M_F)
    ym, Tm, *_ = C.lindhard(np.array([em]), 9, 19)
    print("m = %.1f GeV: E_R^max = %.1f eV, T_d = %.1f eV, count %.2f (Lindhard), %.2f (T_d = E_R), e-h pairs <= %.1f"
          % (m / 1e9, em, Tm[0], float(C.kinchin_pease(Tm, C.E_D_LIF)[0]), float(C.kinchin_pease(em, C.E_D_LIF)), ym[0] * em / C.GAP_LIF))
print("one displacement window E_d <= T_d < 2E_d in recoil energy: 31.3 to 63.7 eV (Lindhard; see fig16_6.log)")
