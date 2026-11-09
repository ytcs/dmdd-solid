"""Book-size example of the library: P(N | seed) for four materials, one-sided and symmetric X0 seeds, read through P_casc_lib.  data/P_seed_examples.csv"""
import csv, os
import numpy as np
from P_casc_lib import Lib
H = os.path.dirname(os.path.abspath(__file__))
w = csv.writer(open(os.path.join(H, "data", "P_seed_examples.csv"), "w", newline=""))
w.writerow(["material", "omega_over_Eg", "seed"] + ["P%d" % n for n in range(1, 15)] + ["mean"])
for mat in ("Si", "Ge", "GaAs", "Al2O3"):
    L = Lib(mat)
    for om in (1.5, 2.5, 3.0, 5.0, 10.0, 20.0):
        e = om - 1
        for lab, (xe, xh) in (("one-sided e", (e, 0.0)), ("symmetric", (e / 2, e / 2))):
            P = L.seed("m1", xe, xh)
            w.writerow([mat, om, lab] + ["%.5f" % v for v in P[1:15]] + ["%.4f" % (P @ np.arange(P.size))])
