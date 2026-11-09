"""Sect. 16.3, quantum-dot rate prefactor: the ratio of the printed rate of Blanco et al. (arXiv:2208.05967, Eq. (6), with
the form factor of its Eq. (10)) to the rate derived in the text (eq:16.3-qdrate), mu_chi_e/(4 omega), and the mass
dimensions of Eq. (6) with Eqs. (10) and (12).  Units: [eV]^n bookkeeping in natural units.
  printed:  dR/dlnE = N_t rho sigma/(8 m mu) int q dq eta F^2 |f|^2
  derived:  dR/dlnE = N_t omega rho sigma/(2 m mu^2) int q dq eta F^2 <|f|^2>   (|f|^2 of Eq. (10), dimension eV^-1)
"""
ME = 510998.95
for m in (1e6, 10e6, 100e6):
    mu = m * ME / (m + ME)
    for w in (3.0, 10.0):
        print(f"m_chi = {m/1e6:6.0f} MeV, omega = {w:4.1f} eV: mu = {mu/1e3:7.2f} keV, printed/derived = mu/(4 omega) = {mu/(4*w):.3e}")
# dimensions (powers of eV) of a rate per target: target eV^1
dim = {"N_t": 0, "rho": 4, "sigma": -2, "m": 1, "mu": 1, "qdq": 2, "eta": 0, "omega": 1}
eq6_10 = dim["rho"] + dim["sigma"] - dim["m"] - dim["mu"] + dim["qdq"] - 1      # |f|^2 of Eq. (10): eV^-1
eq6_12 = dim["rho"] + dim["sigma"] - dim["m"] - dim["mu"] + dim["qdq"] + 0      # |f|^2 of Eq. (12): dimensionless
der = dim["omega"] + dim["rho"] + dim["sigma"] - dim["m"] - 2 * dim["mu"] + dim["qdq"] - 1
print(f"mass dimension of a rate per target: 1; Eq. (6)+(10): {eq6_10}; Eq. (6)+(12): {eq6_12}; derived form: {der}")
