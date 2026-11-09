"""Coulomb kernels of Sect. 16.2: numbers quoted in the text.

  * finite thickness d of a sheet with a uniform profile across it (homogeneous medium):
      v(q) = v2D(q) F(qd),  F(x) = 2/x - 2(1 - e^{-x})/x^2 = 1 - x/3 + O(x^2);
    evaluated for d = 3.35 A, the interlayer distance of bilayer graphene used by Das, Jang, Min arXiv:2312.00866
    (text after their Eq. (11)), at the momenta of sub-MeV dark matter;
  * cylindrical shell: exact 2 alpha I0 K0 against the logarithmic form 2 alpha [ln(2/q r_t) - gamma_E];
  * the substrate factor 2/(eps_a + eps_b) for a sheet on a half space eps_b in vacuum.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L


def Fthick(x):
    return 2 / x - 2 * (1 - np.exp(-x)) / x ** 2


d = 0.335 / L.HBARC
for q in [100.0, 300.0, 1000.0]:
    print(f"sheet d = 3.35 A, q = {q:.0f} eV: q d = {q*d:.3f}, F(qd) = {Fthick(q*d):.3f} (1 - qd/3 = {1-q*d/3:.3f})")
x10 = brentq(lambda x: Fthick(x) - 0.9, 0.01, 2)
print(f"F(qd) = 0.9 at q d = {x10:.3f}: q = {x10/d:.0f} eV for d = 3.35 A")
for q in [1.0, 10.0, 100.0, 282.0]:
    print(f"shell r_t = 0.7 nm, q = {q} eV: q r_t = {q*L.R_T:.4f}, log/exact kernel = {L.v1D_log(q)/L.v1D(q):.4f}")
xr = brentq(lambda x: L.v1D_log(x / L.R_T) / L.v1D(x / L.R_T) - 0.9, 0.05, 1.0)
print(f"log form 10 % below the exact kernel at q r_t = {xr:.3f} (q = {xr/L.R_T:.0f} eV for r_t = 0.7 nm)")
print(f"N_ch v1D/(pi v_D) at q = 1, 10, 100 eV: " + ", ".join(f"{L.N_CH*L.v1D(q)/(np.pi*L.V_D):.1f}" for q in [1.0, 10.0, 100.0]))
print(f"single-channel g at the same kernel, q = 10 eV: {L.g_c(10.0, nch=1):.3f} (four channels {L.g_c(10.0):.3f})")
