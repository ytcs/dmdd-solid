"""Phonon wavevectors for Fig. 5.3, in Cartesian units of 2pi/a (matdyn, q_in_cryst_coord=.false.).
Path: the dispersion path of Fig. 5.2 (fig5_2_qpath.segments: Gamma-X, X'-K-Gamma, Gamma-L), then a fine set along [100]
near Gamma for the acoustic-sum-rule panel (z = 0 ... 0.15 in steps of 0.005), then the three off-grid check points
OFFGRID at which fig5_3_qe.sh also runs ph.x directly: midpoints of Delta, Sigma (Gamma-K-X' line) and Lambda lines that lie on
none of the 2^3, 3^3, 6^3 grids.
Printed format: number of points, then one line 'qx qy qz' per point. Imported by fig5_3_data.py.
"""
import numpy as np
from fig5_2_qpath import segments

FINE = np.round(np.arange(0.0, 0.1501, 0.005), 4)
OFFGRID = [np.array([0.0, 0.0, 0.5]), np.array([0.5, 0.5, 0.0]), np.array([0.25, 0.25, 0.25])]
OFFNAME = ["Delta(0,0,1/2)", "Sigma(1/2,1/2,0)", "Lambda(1/4,1/4,1/4)"]


def points():
    d, s, l, _ = segments()
    fine = [np.array([0.0, 0.0, z]) for z in FINE]
    return d, s, l, fine, OFFGRID


if __name__ == "__main__":
    d, s, l, fine, off = points()
    pts = d + s + l + fine + off
    print(len(pts))
    for p in pts:
        print(f"{p[0]:.8f} {p[1]:.8f} {p[2]:.8f}")
