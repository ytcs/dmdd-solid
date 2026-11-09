"""Reach factors read from input uncertainties for Table 16.1 and Sect. 16.9 (no new physics; arithmetic on book values).

Rule (eq:1.5-limscaling): a factor r on the rate of a scattering target moves sigma_e^lim by 1/r at every mass where
r is constant (normalization nuisance); for absorption R = zeta^2 (rho_chi/rho_T) L, so zeta^lim moves by r^(-1/2).
Sources of the inputs (book sections):
  graphene velocity: v_D = 3 t a_cc/2 = 3.02e-3 (t = 2.8 eV, Sects. 16.2, 16.3); the tube edges
                     q_perp r_t >= 2 n v_D/(3 v_max).
  vacuum ejection:   OPW/PW rate 1.44 (10 MeV), 1.84 (100 MeV), heavy; 1.14, 1.19 light (Sect. 16.3).
  quantum dots:      depolarization factor 6.00 (PbS in silica, 0.354 eV), 4.62-6.71 (Re eps_in = 10-25), 0.566 and 2.45
                     for the illustrative eps_in = 1 + i, 3 + 3i at 5 eV (WE 16.3).
  anthracene:        full/binned rate 1.063 (heavy, > 30 MeV), up to 1.27 (heavy, 1.2-7.5 MeV), 1.29-1.35 (light,
                     > 2 MeV) (Limit Check 16.4a; model).
  Si:P 2p0 line:     zeta^lim 2.3e-16 (central cell) and 1.3e-16 (effective-mass envelope) at 1e15 cm^-3 (WE 16.5);
                     line strengths 1/3.2-1/3.4 between the two ground states (Sect. 16.5).
  glass:             low-power loss tangent of a-SiO2, 3e-4 (thermal oxide) to 5e-3 (deposited oxide) (Sect. 16.7);
                     the dark-photon absorption rate on two-level systems is proportional to tan(delta_0) (Limit Check 16.7b).
Run: python inputs16_9.py > inputs16_9.log
"""
import numpy as np

for n in (1, 2):
    for vD in (3.02e-3,):
        x = 2 * n * vD / (3 * 2.650e-3)
        from scipy.special import j0
        print("  tube edge n = %d, v_D = %.2e: q_perp r_t >= %.3f, J0^2 = %.3f" % (n, vD, x, j0(x) ** 2))

for lab, r in [("OPW heavy 10 MeV", 1.44), ("OPW heavy 100 MeV", 1.84), ("OPW light 10 MeV", 1.14), ("OPW light 100 MeV", 1.19)]:
    print("ejection %-18s rate x%.2f -> sigma_lim x%.2f" % (lab, r, 1 / r))

for lab, r in [("eps_in = 1+i (5 eV)", 0.566), ("eps_in = 3+3i (5 eV)", 2.45), ("Re eps_in = 10", 4.62), ("PbS 0.354 eV", 6.00),
               ("Re eps_in = 25", 6.71)]:
    print("dot depolarization %-22s factor %.3f -> zeta_lim x%.3f" % (lab, r, r ** -0.5))
print("dot depolarization: range 0.566-6.71 spans %.1f in rate, %.2f in zeta_lim" % (6.71 / 0.566, np.sqrt(6.71 / 0.566)))

for lab, r in [("heavy > 30 MeV", 1.063), ("heavy max, 1.2-7.5 MeV", 1.27), ("light low", 1.29), ("light high", 1.35),
               ("heavy at 0.90 MeV (0.88-1.0 MeV window)", 1.383)]:
    print("anthracene full/binned %-40s %.3f -> sigma_lim x%.3f" % (lab, r, 1 / r))

print("Si:P 2p0 line zeta_lim ratio central cell/EMT = %.2f ; sqrt(3.2) = %.2f, sqrt(3.4) = %.2f"
      % (2.3e-16 / 1.3e-16, np.sqrt(3.2), np.sqrt(3.4)))

# two-level scattering (Sect. 16.7, tls16_7.log): host and core terms both scale with the tunneling strength used
print("a-SiO2 TLS scattering with C_l = 1.9e-4 instead of the polarization-averaged C = 2.6e-4: x%.3f" % (1.9 / 2.6))
r = 5e-3 / 3e-4
print("a-SiO2 tan(delta_0) 3e-4 to 5e-3: rate x%.1f, zeta_lim x%.2f" % (r, np.sqrt(r)))
