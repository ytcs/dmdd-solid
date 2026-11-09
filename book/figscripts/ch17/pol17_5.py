"""Sect. 17.5, polar channel: kinematic weights K_eta(omega, m) = int dq/q eta(v_min), v_min = omega/q + q/(2m) (eq:11.2-rate),
for the longitudinal energies of the book: GaAs 36.35 meV (Sect. 5.5/11.2), LiF 77.2 meV (1910.10716 Table I), sapphire band mean
109.9 meV (Sect. 11.2).  Halo from figscripts/ch11/phon11.py (standard halo of Sect. 1.2).  Log: pol17_5.log.
Run: python pol17_5.py > pol17_5.log
"""
import os, sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import phon11 as P  # noqa: E402
V = P.VMAX

def K(w, m):
    if 2 * w / V**2 >= m:
        return 0.0
    s = np.sqrt(1 - 2 * w / (m * V**2))
    qm, qp = m * V * (1 - s), m * V * (1 + s)
    f = lambda lq: float(P.eta(w / np.exp(lq) + np.exp(lq) / (2 * m)))
    return quad(f, np.log(qm), np.log(qp), limit=400)[0]

W = dict(GaAs=36.35e-3, LiF=77.2e-3, sapphire=109.9e-3)
for m in (30e3, 50e3, 0.1e6, 1e6, 10e6, 100e6, 1e9):
    print("m = %8.3g MeV: K_LiF/K_GaAs = %.3f, K_sap/K_GaAs = %.3f" % (m / 1e6, K(W["LiF"], m) / K(W["GaAs"], m),
          K(W["sapphire"], m) / K(W["GaAs"], m)))
for nm in ("LiF", "sapphire"):
    mm = brentq(lambda m: K(W[nm], m) / K(W["GaAs"], m) - 0.9, 0.2e6, 1e10)
    print("K_%s/K_GaAs = 0.9 at m = %.3g MeV" % (nm, mm / 1e6))
