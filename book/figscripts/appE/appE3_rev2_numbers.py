"""Numbers recomputed in the second-pass revision of App. E.21-E.27 (part 2).

Each line prints the quantity, the inputs (with the chapter that supplies them)
and the value written in the tex. Run: python3 appE3_rev2_numbers.py > appE3_rev2_numbers.log
"""
import math

e = 1.602176634e-19      # C
eps_vac = 8.8541878128e-14  # F/cm
alpha_inv = 137.035999

print("E.24  DFT full-band 3.10 eV vs about 3.6 eV (s18-4): %.1f %% below" % (100*(1-3.10/3.6)))
dA = 0.25*5.703
print("E.24  z_qp = 0.8 raises A_AB = 5.703 eV^3 (eq:18.4-AAB) by 25 %%: dA = %.2f eV^3" % dA)
de = 0.076*dA
print("E.24  secant slope 0.076 eV^-2 (s18-4) x dA = %.3f eV = %.1f %% of 3.749 eV" % (de, 100*de/3.749))
print("E.24  Gaussian tail error 0.24/x (REF-DC-67 par. 8) at x = 20 E_g: %.3f" % (0.24/20))
print("E.24  h^{3/2} Richardson denominator 2^{3/2}-1 = %.3f (app:D.43)" % (2**1.5-1))
f = e/(11.4*eps_vac)
print("E.25  field per unit sheet charge, eps0 = 11.4 (s20-1): %.3e V/cm per cm^-2" % f)
n1 = 0.01/f
print("E.25  1 %% at 1 V/cm: n_sh = %.2e (face) to %.2e cm^-2 (midplane)" % (n1, 2*n1))
Ex = 14.7e-3/4.2e-7
print("E.25  exciton field ionization E_x^b/(e a_x) = 14.7 meV / 4.2 nm = %.2e V/cm" % Ex)
print("E.26  (Z alpha)^2 for Xe, Z = 54: %.3f" % ((54/alpha_inv)**2))
print("E.23  4096 x 31 meV = %.0f eV; over close Frenkel pair 6.8-7.5 eV: %.0f to %.0f" % (4096*0.031, 4096*0.031/7.5, 4096*0.031/6.8))
