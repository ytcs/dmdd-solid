"""Phonon wavevectors for the dispersion of Fig. 5.2, in Cartesian units of 2pi/a (matdyn, q_in_cryst_coord=.false.).
Segments (the three lines on which Nilsson and Nelin, Phys. Rev. B 6, 3777 (1972), measured silicon):
  Delta: Gamma (0,0,0) -> X (0,0,1)                      [00z],  z = 0..1
  Sigma: X' (1,1,0) -> K (3/4,3/4,0) -> Gamma           [zz0],  z = 1..0 (X' is equivalent to X)
  Lambda: Gamma -> L (1/2,1/2,1/2)                        [zzz],  z = 0..1/2
Plus small-Q points along each line for the sound speeds (z = 0.005 ... 0.05).
Printed format: number of points, then one line 'qx qy qz' per point. Imported by fig5_2_data.py.
"""
import numpy as np

SMALL = np.array([0.005, 0.01, 0.02, 0.03, 0.04, 0.05])


def segments():
    d = [np.array([0, 0, z]) for z in np.linspace(0, 1, 61)]
    s = [np.array([z, z, 0]) for z in np.linspace(1, 0, 81)]
    l = [np.array([z, z, z]) for z in np.linspace(0, 0.5, 41)]
    small = ([np.array([0, 0, z]) for z in SMALL] + [np.array([z, z, 0]) / np.sqrt(2) for z in SMALL]
             + [np.array([z, z, z]) / np.sqrt(3) for z in SMALL])
    return d, s, l, small


if __name__ == "__main__":
    d, s, l, small = segments()
    pts = d + s + l + small
    print(len(pts))
    for p in pts:
        print(f"{p[0]:.8f} {p[1]:.8f} {p[2]:.8f}")
