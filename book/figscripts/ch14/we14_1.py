"""Worked example 14.1 (we:14-nio) and the numbers of Sect. 14.1 on the spin weights: the zero-point spin reduction
Delta S of NiO and of the simple-cubic antiferromagnet, the ratio W_par/W_perp, the sum-rule defect Delta S/|S|,
the zone averages that check eq:D.38-Wperp, and the near-Gamma and near-Q_AF weights.

Formulas (App. D.38):
  Delta S = N_s^-1 sum_k (v^M_k)^2  (average over a periodic cell of k),
  W_perp = |S|(1 + 2 Delta S), W_par = Delta S (1 + Delta S), W_par/W_perp = Delta S (1 + Delta S)/(|S| (1 + 2 Delta S)),
  sum-rule one-magnon weight (|S| - Delta S)(1 + 2 Delta S): defect Delta S/|S|;
  zone average of the one-magnon weight w_q = 1 + 2 Delta S (check of eq:D.38-weight).
Model and inputs: magnon14.py (Hutchings-Samuelsen J1, J2; a = 4.17 A; |S| = 1). Delta S does not depend on |S| in
linear spin-wave theory, since A_k and B_k do not.
Output: figscripts/ch14/we14_1.log (all printed numbers).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import magnon14 as m

LOG = open(os.path.join(HERE, "we14_1.log"), "w")


def out(s):
    print(s)
    LOG.write(s + "\n")


PER_FCC = 4 * np.pi / m.A_NIO          # period of the fcc reciprocal lattice along each cube axis
out("Zero-point spin reduction Delta S = <(v^M_k)^2> over the zone (offset midpoint grids)")
for n in (40, 60, 80, 100):
    k = m.zone_grid(n, PER_FCC)
    a, b = m.ab_nio(k)
    out(f"  NiO J1+J2, n = {n:3d}: Delta S = {m.v2(a, b).mean():.5f};  <w_q> = {m.weight(a, b).mean():.5f};"
        f"  1 + 2 Delta S = {1 + 2*m.v2(a, b).mean():.5f};  min(A^2 - B^2) = {np.min(a**2 - b**2):.3e} meV^2")
    a0, b0 = m.ab_nio(k, j1=0.0)
    out(f"  NiO J2 only,  n = {n:3d}: Delta S = {m.v2(a0, b0).mean():.5f}")
    ks = m.zone_grid(n, 2 * np.pi)
    a1, b1 = m.ab_sc(ks)
    out(f"  simple cubic, n = {n:3d}: Delta S = {m.v2(a1, b1).mean():.5f};  <w_q> over the sc zone = {m.weight(a1, b1).mean():.5f}")

n = 100
k = m.zone_grid(n, PER_FCC)
a, b = m.ab_nio(k)
dS = m.v2(a, b).mean()
ks = m.zone_grid(n, 2 * np.pi)
dS_sc = m.v2(*m.ab_sc(ks)).mean()
out(f"\nAdopted (n = {n}): Delta S(NiO) = {dS:.4f}, Delta S(sc) = {dS_sc:.4f}")
for name, d in (("NiO lattice", dS), ("simple cubic", dS_sc)):
    for S in (0.5, 1.0, 1.5, 2.0, 2.5):
        wperp = S * (1 + 2 * d)
        wpar = d * (1 + d)
        out(f"  {name:12s} |S| = {S:3.1f}: 1/(2|S|) = {1/(2*S):.3f}; W_perp = {wperp:.4f}; W_par = {wpar:.4f};"
            f" W_par/W_perp = {wpar/wperp:.4f}; defect Delta S/|S| = {d/S:.4f};"
            f" sum-rule W_perp = {(S - d)*(1 + 2*d):.4f}; total inelastic/LSWT = {1 - d**2/(S*(1 + 2*d)):.5f}")
S = m.S_NIO
out(f"\nNiO, |S| = 1: ordered moment <S^z> = |S| - Delta S = {S - dS:.4f} (fraction {(S - dS)/S:.4f})")
out(f"  Casimir check: W_perp(sum rule) + <S^z>^2 + W_par = {(S - dS)*(1 + 2*dS) + (S - dS)**2 + dS*(1 + dS):.6f}"
    f" = |S|(|S|+1) = {S*(S + 1):.6f}")
out(f"  validity |S| > 10 Delta S: |S| > {10*dS:.3f}, i.e. 1/(2|S|) < {1/(20*dS):.3f}")
out(f"  simple cubic: |S| > {10*dS_sc:.3f}, i.e. 1/(2|S|) < {1/(20*dS_sc):.3f}")

# near-Gamma and near-Q_AF weights: w ~ omega/omega_ex and omega_ex/omega, omega_ex = 2|S| J_AB(0)
jab0 = 6 * (m.J1 + m.J2)
wex = 2 * S * jab0
out(f"\nExchange energy 2|S| J_AB(0) = 2 x 6 (J1 + J2) = {wex:.1f} meV")
for d in ((1, 1, 1), (1, 0, 0), (1, 1, 0)):
    u = np.array(d, float) / np.linalg.norm(d)
    for target, k0 in (("Gamma", np.zeros(3)), ("Q_AF", m.Q_AF)):
        for eps in (0.003, 0.01):
            kk = (k0 + eps * u)[None, :]
            aa, bb = m.ab_nio(kk)
            om = m.omega(aa, bb)[0]
            w = m.weight(aa, bb)[0]
            est = om / wex if target == "Gamma" else wex / om
            out(f"  near {target:5s} along {d}: |dk| = {eps} A^-1, omega = {om:6.2f} meV, w = {w:.4f}, estimate {est:.4f}")
out(f"  w at omega = 5 meV near Gamma: 5/{wex:.1f} = {5/wex:.4f}; near Q_AF: {wex/5:.1f}")
out(f"  |Q_AF| = sqrt(3) pi/a = {np.linalg.norm(m.Q_AF):.3f} A^-1 = {np.linalg.norm(m.Q_AF)*m.HBARC_MEV_A/1e6:.3f} keV")
KB = 8.617333e-2   # meV/K
out(f"\nThermal magnons: omega/(k_B T) at the 4.54 meV gap: {4.54/(KB*0.010):.0f} at 10 mK; {4.54/(KB*1.0):.1f} at 1 K")

# magnon velocity of the J1 + J2 model near Gamma (direction dependence) and the kinematic edges it implies
# (c_M = 1.39e-4 of we:7-nio is the J2-only speed 2 sqrt(3) J2 |S| a; Sect. 14.1 eq:14.1-mmin, Sect. 14.2 eq:14.2-mratio)
VMAX = 794.5 / 299792.458
rng = np.random.default_rng(1)
dirs = rng.normal(size=(20000, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
dirs = np.vstack([dirs, np.array([[1, 1, 1], [1, 0, 0], [1, 1, 0]], float) / np.linalg.norm([[1, 1, 1], [1, 0, 0], [1, 1, 0]], axis=1)[:, None]])
eps = 1e-4
aa, bb = m.ab_nio(eps * dirs)
cM = m.omega(aa, bb) / eps / m.HBARC_MEV_A          # dimensionless (units of c)
out(f"\nMagnon velocity near Gamma, J1+J2 model (|k| = {eps} A^-1): min {cM.min():.4e}, max {cM.max():.4e};"
    f" [111] {cM[-3]:.4e}, [100] {cM[-2]:.4e}, [110] {cM[-1]:.4e}  (meV A: {cM.min()*m.HBARC_MEV_A:.0f} to {cM.max()*m.HBARC_MEV_A:.0f})")
c2 = 2 * np.sqrt(3) * m.J2 * m.S_NIO * m.A_NIO / m.HBARC_MEV_A
out(f"  J2-only speed 2 sqrt(3) J2 |S| a = {c2:.4e} (we:7-nio value 1.39e-4)")
for name, c in (("J2-only", 1.39e-4), ("J1+J2 fastest", cM.max())):
    for wth in (1.0, 5.0):
        mmin = wth * 1e-3 / (2 * c * (VMAX - c))    # eV
        out(f"  {name:14s} c = {c:.3e}: one-magnon edge for w_th = {wth} meV: {mmin/1e3:.2f} keV;"
            f" ratio v^2/(4c(v-c)) = {VMAX**2/(4*c*(VMAX - c)):.2f}; two-magnon edge 2 w_th/v^2 = {2*wth*1e-3/VMAX**2/1e3:.3f} keV;"
            f" v_max/c = {VMAX/c:.1f}")
# accidental zero of the undistorted J1-J2 model at X = (2 pi/a)(1, 0, 0)
X = np.array([[2 * np.pi / m.A_NIO, 0, 0]])
ax, bx = m.ab_nio(X)
out(f"X = (2pi/a)(1,0,0): A = {ax[0]:.3f} meV, B = {bx[0]:.3f} meV, 6 J2 - 2 J1 = {6*m.J2 - 2*m.J1:.3f}; omega = {m.omega(ax, bx)[0]:.3e} meV;"
    f" |X| = {2*np.pi/m.A_NIO*m.HBARC_MEV_A/1e6:.2f} keV")
# grid convergence of Delta S: successive differences scale as n^-2
d = {}
for n in (60, 80, 100, 120):
    d[n] = m.v2(*m.ab_nio(m.zone_grid(n, PER_FCC))).mean()
out("Delta S convergence: " + ", ".join(f"n={n}: {v:.5f}" for n, v in d.items()))
out(f"  differences 60->80 {d[80]-d[60]:.2e}, 80->100 {d[100]-d[80]:.2e}, 100->120 {d[120]-d[100]:.2e};"
    f" n^-2 extrapolation from 100, 120: {d[120] + (d[120]-d[100])*100**2/(120**2-100**2):.4f}")
# rate factor of the form factor at 10 MeV (fig14_1.log: F=1 1.745e4, Brown 1.531e3)
out(f"form-factor suppression at 10 MeV, 5 meV threshold: 1.745e4/1.531e3 = {1.745e4/1.531e3:.1f}")
LOG.close()
