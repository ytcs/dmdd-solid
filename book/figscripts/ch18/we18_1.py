"""Numbers of Sect. 18.1 other than those of Fig. 18.1: Worked example 18.1 (we:18-toy), the generating function of a
two-step toy cascade, and the density estimates behind the independence hypothesis of the branching process.
Output: we18_1.log (every number printed in Sect. 18.1 outside Fig. 18.1 is in this log).

Toy (units of Eg; every value is a choice of the example, not a material value):
  threshold theta_ii = 3/2, phonon energy 1/2. A carrier at x = 2 ionizes with probability p_a, sharing x - 1 = 1
  among three carriers (all below threshold), or emits a phonon and sits at x = 3/2, where it ionizes with
  probability p_b (sharing 1/2) or emits a second phonon and stops at x = 1 (below threshold).
  Seed: one pair (counts as one) whose electron and hole both start at x = 2 and follow the same rules.
Estimates (assumptions named):
  Si lattice constant a = 5.431 A (book value, Table 3.1), 8 atoms per cubic cell, 4 valence electrons per atom.
  Exciton radius a_x = 4.2 nm (Sect. 10.5). Pairs spread uniformly over a sphere of radius 10 nm (an assumption of
  the estimate, stated in the text). Pair numbers at eps_eh = 3.75 eV (Sect. 1.5).
"""
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
L = []

s, pa, pb, u = sp.symbols("s p_a p_b u", positive=True)
# generating function of new pairs for one carrier at x = 2
G2 = pa * s + (1 - pa) * (pb * s + (1 - pb))
# joint with heat: E_heat = 2 - N (energy ledger, Eg = 1) -> e^{u E_heat}
G2j = pa * s * sp.exp(u * 1) + (1 - pa) * (pb * s * sp.exp(u * 1) + (1 - pb) * sp.exp(u * 2))
L.append("G_2(s) = %s" % sp.simplify(G2))
L.append("check ledger: G_2(s,u) - e^{2u} G_2(s e^{-u}) = %s" % sp.simplify(G2j - sp.exp(2 * u) * G2.subs(s, s * sp.exp(-u))))
GL = s * G2 ** 2
nbar = sp.diff(GL, s).subs(s, 1)
var = sp.simplify(sp.diff(GL, s, 2).subs(s, 1) + nbar - nbar ** 2)
L.append("pair seed: G_Lambda = s G_2^2; mean = %s; var = %s" % (sp.simplify(nbar), sp.factor(var)))
vals = {pa: sp.Rational(3, 5), pb: sp.Rational(2, 5)}
n_ = nbar.subs(vals)
v_ = var.subs(vals)
L.append("p_a = 3/5, p_b = 2/5: one carrier mean %s = %.4f" % (sp.diff(G2, s).subs(vals), float(sp.diff(G2, s).subs(vals))))
coeffs = sp.Poly(sp.expand(GL.subs(vals)), s).all_coeffs()[::-1]
L.append("   P(N_eh = 0..3) = %s = %s" % (coeffs, [float(c) for c in coeffs]))
omega = 5  # Eg + 2 + 2
L.append("   mean %s = %.4f, var %s = %.4f, omega = %d Eg, eps = omega/mean = %.4f Eg, var/mean = %.4f" %
         (n_, float(n_), v_, float(v_), omega, omega / float(n_), float(v_ / n_)))
# averaging the seed first: replacing the two carriers by one carrier of energy 4 is not this toy; instead show
# the generating function is not the generating function of the mean seed: a seed with all 4 units on the electron
# would need the rules above x = 2, which the toy does not define, so the comparison is made in Fig. 18.1's model.

# density estimates
a = 5.431e-8  # cm
ne = 4 * 8 / a ** 3
L.append("Si valence electron density = %.3e cm^-3; per eV over a 12 eV valence band: %.2e cm^-3 eV^-1" % (ne, ne / 12))
R = 10e-7  # cm
V = 4 / 3 * np.pi * R ** 3
ax = 4.2e-7
for E in (100.0, 1000.0):
    npair = E / 3.75
    n = npair / V
    L.append("deposit %.0f eV: %.0f pairs in a 10 nm sphere: n_pair = %.2e cm^-3, n_pair a_x^3 = %.2f, occupation per eV of states %.1e" %
             (E, npair, n, n * ax ** 3, n / (ne / 12)))

# density of states at the energies of the hot carriers (the final states that Pauli blocking would act on): parabolic
# conduction band of silicon, six valleys with m_par = 0.916, m_perp = 0.191 (tab:3-materials), density-of-states mass
# m_d = 6^(2/3) (m_par m_perp^2)^(1/3); g(E) = (2 m_d)^(3/2) E^(1/2)/(2 pi^2 hbar^3), spin included.
md = 6 ** (2 / 3) * (0.916 * 0.191 ** 2) ** (1 / 3)
hbarc = 1.97327e-5   # eV cm
mec2 = 0.51099895e6  # eV
for E in (1.0, 3.0):
    g = (2 * md * mec2) ** 1.5 * np.sqrt(E) / (2 * np.pi ** 2 * hbarc ** 3)
    L.append("conduction density of states at %.0f eV above the edge (m_d = %.3f m_e): %.2e cm^-3 eV^-1; 1 keV pair density "
             "%.2e cm^-3 fills %.1e of it per eV" % (E, md, g, 1000 / 3.75 / V, 1000 / 3.75 / V / g))

with open(os.path.join(HERE, "we18_1.log"), "w") as f:
    f.write("\n".join(L) + "\n")
print("\n".join(L))
