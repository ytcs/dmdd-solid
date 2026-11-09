"""Numbers printed in the running text of Sect. 18.2 that are not produced by the figure scripts.
Log: num18_2.log.  Run: python num18_2.py > num18_2.log  (about 2 min).  Solver: mom18_2.py; silicon model of fig18_2.py.

(1) Opening: 5.9 keV in silicon at 123 K, eps_eh = 3.749 eV and F_eh = 0.119 (Rodrigues et al., arXiv:2004.11499; App. E.13).
(2) Energy constraint in the renewal estimate, for the uniform-in-k terminal population below theta_ii = 3/2 (Klein's population,
    Sect. 18.4): residual density ~ x^(1/2) on [0, theta E_g], two carriers per pair, eps_eh = (14/5) E_g.
(3) Sensitivity of F_eh to an error in V_> (silicon terms from fig18_2.log).
(4) Stability of the asymptotic slopes (silicon): top energy X = 40 against 80 E_g; fit windows [X/2, X] against [3X/4, X].
(5) Size of the constant term at a 10 eV deposit: b_N against omega/eps_eh.
(6) The identity checks of the moment recursions (App. D.43) on the production grid E_g/74.
Silicon set of si_cascade18.py (A_AB = 5.703 eV^3); (4)-(6) on the production grid E_g/74.
"""
import os
import re
import sys
from fractions import Fraction as Fr
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mom18_2 import Cascade, lagrange, run
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI

E = 5900.0
eps, F = 3.749, 0.119
n = E / eps
print("(1) 5.9 keV: <N> = %.1f, sigma = sqrt(F <N>) = %.2f, Poisson sqrt(<N>) = %.2f" % (n, np.sqrt(F * n), np.sqrt(n)))

th = Fr(3, 2)
mean = Fr(3, 5) * th
var = Fr(12, 175) * th**2
s2 = 2 * var
e = 1 + 2 * mean
print("(2) theta = 3/2: <x> = %s E_g, Var x = %s E_g^2, sigma_pair^2 = %s E_g^2 = %.4f, eps = %s E_g; "
      "N fixed: F = %.4f (%.2f x 0.119); constrained F = %s = %.4f (0.119/F = %.2f)" %
      (mean, var, s2, float(s2), e, float(s2), float(s2) / 0.119, s2 / e**2, float(s2 / e**2), 0.119 / float(s2 / e**2)))

log = open(os.path.join(HERE, "fig18_2.log")).read()
VP = float(re.search(r"V_> = ([0-9.]+)", log).group(1))
Fsi = float(re.search(r"F_eh = ([0-9.]+) \(pair-number", log).group(1))
A = A_AB
print("(3) 1 %% error in V_> = %.4f moves F_eh = %.4f by %.2f %%" % (VP, Fsi, 100 * 0.01 * VP / Fsi))

EG, OM, WH = EG_SI, OM_SI, BH_SI
w = OM / EG
lam = A / EG**3
for X in (40.0, 80.0):
    for frac in (0.5, 0.75):
        r = run(lam, w, X=X, W=(None, WH / EG), decomp=False, frac=frac)
        print("(4) X = %2.0f E_g, window [%.2f X, X]: eps/E_g = %.6f, F_eh = %.6f, b_N = %.4f" % (X, frac, r["eps"], r["F"], r["bN"]))

r = run(lam, w, X=40.0, W=(None, WH / EG), decomp=False)
om = 10.0 / EG
print("(5) omega = 10 eV = %.3f E_g: omega/eps = %.3f, b_N = %.3f, b_N/(omega/eps) = %.1f %%" %
      (om, om / r["eps"], r["bN"], 100 * r["bN"] / (om / r["eps"])))

r = run(lam, w, X=40.0, W=(None, WH / EG), decomp=True)
print("(6) checks of the energy identity (silicon): |F(pair deposit) - F(heat deposits)| = %.1e; "
      "|2V_<> (E_< - E_> route) - (F - V_< - V_>)| = %.1e; carriers per pair = %.6f" %
      (abs(r["F"] - r["F_heat"]), abs(r["Cov2"] - r["Cov2_rem"]), r["carriers_per_pair"]))
c = Cascade(lam, round(w * 74) / 74, X=40.0, h=1 / 74, W=(None, WH / EG))
x = c.x
tot = c.mean("N") + c.mean("R") + c.mean("P")
sel = x >= 2
print("    one grid node: max |x - (N_sub E_g + <E_<> + <E_>>)|/x over x >= 2 E_g = %.1e" % np.max(np.abs(x[sel] - tot[sel]) / x[sel]))
