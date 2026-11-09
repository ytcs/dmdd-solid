"""Worked example 16.3 (we:16-depol): the depolarization factor 9|eps_in|^2/|eps_in + 2 eps_out|^2 of a PbS dot in fused silica.

Inputs (public data; files kept in book/sources/16.3/):
  PbS   n^2 - 1 = 15.9 lam^2/(lam^2 - 0.77^2) + 133.2 lam^2/(lam^2 - 141^2)  (lam in micrometres, 3.5-10 um, 300 K):
        Zemel, Jensen and Schoolar, Phys. Rev. 140, A330 (1965), with the second term from the Handbook of Optics,
        as tabulated in the refractiveindex.info database (rii_PbS_Zemel.yml).  Below the bulk gap (0.41 eV), eps real.
  SiO2  fused silica, Sellmeier fit of Malitson, J. Opt. Soc. Am. 55, 1205 (1965), 0.21-3.71 um (6.7 um per Tan 1998),
        as tabulated in the refractiveindex.info database (rii_SiO2_Malitson.yml).
  The ultraviolet value eps_in = 1 + i is illustrative (|eps_in| of order one above the main interband peaks), not PbS data.
Printed: eps_in, eps_out, the inside-field factor 3 eps_out/(eps_in + 2 eps_out), the depolarization factor, its range for
Re eps_in = 10-25, and the sign criterion |eps_in|^2 > (eps_out/2)(Re eps_in + eps_out).
"""
import numpy as np

HC = 1.239841984   # eV um


def n2_formula1(lam, coef):
    s = 1.0
    for B, C in zip(coef[0::2], coef[1::2]):
        s += B * lam**2 / (lam**2 - C**2)
    return s


PBS = [15.9, 0.77, 133.2, 141.0]
SIO2 = [0.6961663, 0.0684043, 0.4079426, 0.1162414, 0.8974794, 9.896161]


def factor(ei, eo):
    return 9 * abs(ei) ** 2 / abs(ei + 2 * eo) ** 2


def crit(ei, eo):
    return abs(ei) ** 2 > 0.5 * eo * (ei.real + eo)


lam = 3.5
ei = n2_formula1(lam, PBS)
eo = n2_formula1(lam, SIO2)
print(f"lambda = {lam} um ({HC/lam:.3f} eV): eps_in(PbS) = {ei:.2f}, eps_out(silica) = {eo:.3f}")
print(f"  inside field 3 eps_out/(eps_in + 2 eps_out) = {3*eo/(ei+2*eo):.3f}; inside field in bulk PbS 1/eps_in = {1/ei:.4f}")
print(f"  depolarization factor 9 eps_in^2/(eps_in + 2 eps_out)^2 = {factor(ei+0j, eo):.2f}; |eps_in| >> eps_out limit 9")
for e in (10.0, 25.0):
    print(f"  Re eps_in = {e:.0f}: factor {factor(e+0j, eo):.2f}")
for lam2 in (0.496, 0.248):
    eo2 = n2_formula1(lam2, SIO2)
    print(f"silica at {lam2} um ({HC/lam2:.2f} eV): n = {np.sqrt(eo2):.4f}, eps_out = {eo2:.3f}")
eo5 = n2_formula1(0.248, SIO2)
for ei2 in (1 + 1j, eo5 + 0j, 3 + 3j):
    print(f"  eps_in = {ei2}: factor {factor(ei2, eo5):.3f}, criterion (> 1) {crit(ei2, eo5)}")
print("  for real eps_in the factor exceeds 1 exactly when eps_in > eps_out")
# reduced wavelength of a 1 eV dark photon moving at v = 1e-3: 1/(m v), hbar c = 197.327 eV nm
print(f"1/(m_phi v) at m_phi = 1 eV, v = 1e-3: {197.327e-9/1e-3*1e3:.3f} mm (dot radius 1.65 nm: m v R = {1.65/197.327e3*1e-3*1e3:.2e})")
