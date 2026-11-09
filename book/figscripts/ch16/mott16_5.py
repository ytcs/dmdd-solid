"""Sect. 16.5: donor spacing and orbit overlap in Si:P against density.
Inputs: Kohn-Luttinger radii r_perp = 24.3 A, r_par = 14.0 A (Sect. 7.4, eps 11.7); the measured metal-insulator density of
uncompensated Si:P, n_c ~ 3e18 cm^-3, as quoted by Du et al. (arXiv:2212.04504v1, Sect. II); 2.00e23 valence electrons
per cm^3 (Sect. 3.1).  Random (Poisson) donor positions: the nearest-neighbour distance d has P(d < x) = 1 - exp(-4 pi n x^3/3),
mean 0.554 n^{-1/3}.  'Overlap' is taken as a neighbour within the orbit diameter 2 r_perp (a stated convention).
"""
import numpy as np
from scipy.special import gamma

RP = 24.3
NC = 3e18
print(f"orbit diameter 2 r_perp = {2*RP/10:.2f} nm; mean NN distance = Gamma(4/3) (4 pi n/3)^(-1/3) = "
      f"{gamma(4/3)*(4*np.pi/3)**(-1/3):.3f} n^(-1/3)")
for n in (1e15, 1e16, 1e17, 1e18, 1.8e18, 3e18):
    nA = n * 1e-24
    sp = nA ** (-1 / 3) / 10
    nn = gamma(4 / 3) * (4 * np.pi / 3 * nA) ** (-1 / 3) / 10
    P = 1 - np.exp(-4 * np.pi / 3 * nA * (2 * RP) ** 3)
    print(f"n_D = {n:.1e} cm^-3 (n_D/n_c = {n/NC:.2f}): spacing n^-1/3 = {sp:6.1f} nm, mean NN distance {nn:6.1f} nm, "
          f"fraction with a neighbour within 2 r_perp = {P:.3g}; donors per valence electron {n/2.00e23:.1e}")
