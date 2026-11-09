"""Worked example 5.6 and the GaAs numbers of Sect. 5.5: Lyddane-Sachs-Teller relation, Born charge from the LO-TO
splitting, and the PBE dielectric constant and Born charges.
Natural units, Heaviside-Lorentz charge e^2 = 4 pi alpha (App. A.2).
Inputs and sources:
  omega_T = 8.13 THz, omega_L = 8.79 THz (neutron scattering) [Strauch and Dorner, JPCM 2, 1457 (1990), as tabulated in
      Dehghani et al., arXiv:2506.16977, Table I] (as Table 5.1).
  eps_0 = 12.9, eps_inf = 10.88 [Lockwood, Yu and Rowell, Solid State Commun. 136, 404 (2005), as quoted by Knapen et al.,
      arXiv:1712.06598, after Eq. (5)].
  a = 5.638 A [Csonka et al., PRB 79, 155107 (2009), Table II, as Table E.1]; Omega = a^3/4.
  masses Ga 69.723 u, As 74.9216 u (standard atomic weights).
  PBE values: gaas_cache/epsZ.json, extracted from ph.x outputs of tab5_1_gaas_qe.sh (8^3 k) and fig5_4_epsk.sh (12^3, 16^3 k)
      by gaas_cache_extract.py.
Run: python we5_6.py   (numpy)
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
THZ = 4.135667696e-3                 # eV per THz
U = 931.49410242e6                   # eV per u
HBARC = 1973.269804                  # eV A
ALPHA = 1 / 137.035999084
E2 = 4 * np.pi * ALPHA
wT, wL = 8.13 * THZ, 8.79 * THZ
eps0, epsi = 12.9, 10.88
a = 5.638
Om = a ** 3 / 4 / HBARC ** 3         # eV^-3
mu = 69.723 * 74.9216 / (69.723 + 74.9216) * U
print(f"omega_T = {wT*1e3:.2f} meV, omega_L = {wL*1e3:.2f} meV, splitting {1e3*(wL-wT):.2f} meV")
print(f"Omega = {a**3/4:.2f} A^3 = {Om:.4e} eV^-3; mu_red = {mu/U:.3f} u = {mu/1e9:.3f} GeV; e^2 = {E2:.5f}")
r_eps, r_w = eps0 / epsi, (wL / wT) ** 2
print(f"eps_0/eps_inf = {r_eps:.4f}; (omega_L/omega_T)^2 = {r_w:.4f}; difference {100*(r_eps/r_w-1):.2f} %")
wLp = wT * np.sqrt(r_eps)
print(f"LST prediction omega_L = omega_T sqrt(eps0/epsinf) = {wLp*1e3:.2f} meV ({100*(wLp/wL-1):+.2f} %);"
      f" predicted splitting {1e3*(wLp-wT):.2f} meV vs measured {1e3*(wL-wT):.2f} meV ({100*((wLp-wT)/(wL-wT)-1):+.0f} %)")
print(f"eps_0 predicted from eps_inf and the phonons: {epsi*r_w:.3f}")
print(f"estimate in text: e^2 Z^2/(Omega eps mu) with Z=2, Omega=45 A^3, eps=11, mu=36 u: "
      f"{E2*4/(45/HBARC**3*11*36*U):.2e} eV^2; omega_T^2 = {wT**2:.2e} eV^2")
Z_lo = np.sqrt(Om * epsi * mu * (wL ** 2 - wT ** 2) / E2)
Z_st = np.sqrt(Om * mu * wT ** 2 * (eps0 - epsi) / E2)
print(f"|Z*| from LO-TO and eps_inf (eq:5.5-LOTO): {Z_lo:.3f}; from eps_0 - eps_inf = e^2Z^2/(Omega mu wT^2): {Z_st:.3f}")
print(f"term e^2Z^2/(Omega eps_inf mu) = {E2*Z_lo**2/(Om*epsi*mu):.3e} eV^2")
f = os.path.join(HERE, "gaas_cache", "epsZ.json")
if os.path.exists(f):
    d = json.load(open(f))
    for k in sorted(d, key=lambda s: int(s)):
        v = d[k]
        s = v["Z_Ga"] + v["Z_As"]
        Zasr = (v["Z_Ga"] - v["Z_As"]) / 2
        line = (f"PBE k {k}^3: eps_inf = {v['eps']:.3f}, Z_Ga = {v['Z_Ga']:.4f}, Z_As = {v['Z_As']:.4f}, sum {s:+.4f}"
                f" ({100*abs(s)/Zasr:.1f} % of Z*), Z* with sum rule {Zasr:.4f}")
        if "gap" in v:
            line += f", direct gap at Gamma {v['gap']:.3f} eV"
        print(line)
        for wt_meV in (v.get("wT_meV"),):
            if wt_meV:
                wt = wt_meV * 1e-3
                for Zs, ep, lab in ((Zasr, v["eps"], "PBE Z*, PBE eps"), (Zasr, epsi, "PBE Z*, measured eps"),
                                    (Z_lo, epsi, "measured-splitting Z*, measured eps")):
                    dd = E2 * Zs ** 2 / (Om * ep * mu)
                    print(f"   splitting from eq:5.5-LOTO with omega_T = {wt_meV:.2f} meV ({lab}): "
                          f"{1e3*(np.sqrt(wt**2+dd)-wt):.2f} meV")
        print(f"   Z*(sum rule)/Z*(measured splitting) - 1 = {100*(Zasr/Z_lo-1):+.1f} %;"
              f" eps_inf PBE/measured = {v['eps']/epsi:.2f}")
