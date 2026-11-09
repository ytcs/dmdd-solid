"""DC-67 reader of the P_casc library (WP6 `P_casc/URF-energy-only`).  data/lib/<material>.npz holds, per config c:
  x_c   carrier kinetic energies in units of E_g (grid points nearest to multiples of 0.05 below 5, of 0.25 above),
  Pe_c  P(N_sub = n | electron at x), rows x, columns n (ii events in the subtree),
  Ph_c  the same for a hole; absent when rho_e = rho_h, where Ph = Pe.
Composition (CW7-153b): P(N | x_e, x_h) = sum_{n1 + n2 = N - 1} Pe(n1 | x_e) Ph(n2 | x_h); the primary pair is counted once, P(0 | Lambda) = 0.
Sector map in the energy-only level (H-EF1): Lambda = (c, v, k) -> x_e = (eps_ck - E_CBM)/E_g, x_h = (E_VBM - eps_vk)/E_g.  X0 seed: x_e + x_h = (omega - E_g)/E_g;
X+ seed: x_e + x_h = (omega - omega_Q - E_g)/E_g.  Band-resolved partitions of that energy need the S_Lambda library; this file takes (x_e, x_h) as given.
Between table rows P is interpolated linearly in x (error measured in data/x_interp_error.json); x beyond the table raises (use gaussian_match, whose error is recorded in returns/R18/DC-67.md)."""
import os
import numpy as np
from scipy.stats import norm
LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "lib")


class Lib:
    def __init__(self, material):
        self.d = np.load(os.path.join(LIB, material + ".npz"))
        self.material = material

    def configs(self):
        return sorted(k[2:] for k in self.d.files if k.startswith("x_"))

    def carrier(self, cfg, x, t="e"):
        key = ("P%s_%s" % (t, cfg))
        P = self.d[key] if key in self.d.files else self.d["Pe_" + cfg]
        xs = self.d["x_" + cfg]
        if not 0 <= x <= xs[-1]:
            raise ValueError("x = %g outside the table [0, %g]" % (x, xs[-1]))
        i = min(np.searchsorted(xs, x, side="right") - 1, len(xs) - 2)
        a = (x - xs[i]) / (xs[i + 1] - xs[i])
        return (1 - a) * P[i] + a * P[i + 1]

    def seed(self, cfg, x_e, x_h, nmax=20):
        """P(N | x_e, x_h), N = 0..nmax; mass above nmax is not folded in."""
        P = np.concatenate([[0.0], np.convolve(self.carrier(cfg, x_e, "e"), self.carrier(cfg, x_h, "h"))])
        out = np.zeros(nmax + 1); k = min(P.size, nmax + 1); out[:k] = P[:k]
        return out


def gaussian_match(om_over_Eg, eps_over_Eg, F, b, nmax=20):
    """Discretised Gaussian beyond the table: mean om/eps + b, variance F om/eps (CW7 sec. 4 property (c)); b is seed dependent."""
    mean = om_over_Eg / eps_over_Eg + b; sd = np.sqrt(F * om_over_Eg / eps_over_Eg); n = np.arange(nmax + 1)
    return norm.cdf((n + .5 - mean) / sd) - norm.cdf((n - .5 - mean) / sd)
