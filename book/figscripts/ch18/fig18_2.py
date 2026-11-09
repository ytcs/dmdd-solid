"""Fig. 18.2 (fig:18-decomp): F_eh and its three variance terms against the phonon-loss parameter lam_ph, silicon phonon energy.
Log: fig18_2.log.  Run: python fig18_2.py > fig18_2.log  (about 2 min).  Solver: mom18_2.py (energy-only cascade, Sect. 18.1).

Inputs (all as in the book):
  E_g = 1.160 eV, silicon at 123 K, the temperature of the measurement (Ramanathan and Kurinsky, arXiv:2004.10709, Eq. (11);
        App. E.13);
  omega_AB = 63 meV, the single optical phonon of the Alig-Bloom model (2004.10709 Sect. II; App. E.13);
  W_h = 12 eV, valence bandwidth cut on the hole density of states (the hole-energy constraint E_h < W of 2004.10709 Sect. III);
  theta_ii = 1, parabolic densities of states rho ~ x^(1/2) for electrons and holes;
  A_AB = 5.703 eV^3, the continuum calibration on eps_eh = 3.749 eV (si_cascade18.py, the one silicon set of Chap. 18).
lam_ph = A_AB/E_g^3 and w_ph = omega_AB/E_g = 0.05431.  The scan varies lam_ph at this w_ph.
Every value is the continuum limit: steps E_g/74 and E_g/148, extrapolated in h^(3/2) (si_cascade18.mom_cont).
Asymptote: slopes over [X/2, X], X = 40 E_g (lam_ph <= 5) and 60 E_g above.
Decomposition: F_eh = V_< + V_> + 2 V_<>, with 2 V_<> from the recursion for E_< - E_> (independent route) and checked against
the remainder F_eh - V_< - V_>.
"""
import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI, EPS_MEAS, mom_cont

OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch18"))
os.makedirs(OUT, exist_ok=True)

EG, OM, WH = EG_SI, OM_SI, BH_SI
w = OM / EG
t0 = time.time()


def solve(lam, decomp=True):
    X = 40.0 if lam <= 5 else 60.0
    return mom_cont(lam, w, WH / EG, X=X, decomp=decomp)


A = A_AB
lamSi = A / EG**3
print("w_ph = omega_AB/E_g = %.5f" % w)
print("A_AB = %.3f eV^3 (continuum calibration on eps_eh = %.3f eV at E_g = %.3f eV, si_cascade18.log); lam_ph(Si) = %.4f"
      % (A, EPS_MEAS, EG, lamSi))
r = solve(lamSi)
print("Si point: eps/E_g = %.4f, eps = %.4f eV, F_eh = %.4f (pair-number route), %.4f (heat route)" %
      (r["eps"], r["eps"] * EG, r["F"], r["F_heat"]))
print("   V_< = %.4f, V_> = %.4f, 2V_<> = %.4f (E_<-E_> route), %.4f (remainder); sum = %.4f" %
      (r["VR"], r["VP"], r["Cov2"], r["Cov2_rem"], r["VR"] + r["VP"] + r["Cov2"]))
print("   cancellation -2V_<>/V_> = %.3f; carriers per pair = %.4f; mean residual per carrier rbar_c/E_g = %.4f;"
      " phonon heat per pair = %.4f E_g = %.3f eV" % (-r["Cov2"] / r["VP"], r["carriers_per_pair"],
                                                         r["resid_per_pair"] / 2, r["phon_per_pair"], r["phon_per_pair"] * EG))
print("   identity eps/E_g = 1 + 2 rbar_c + phonon heat per pair: %.5f vs %.5f" %
      (1 + r["resid_per_pair"] + r["phon_per_pair"], r["eps"]))
print("   Poisson phonon number: Var E_> = omega_AB <E_>>, V_>^Poisson = w_ph * (phonon heat per pair/E_g) = %.4f; V_>/Poisson = %.2f" %
      (w * r["phon_per_pair"], r["VP"] / (w * r["phon_per_pair"])))
print("   renewal estimate F_ren = %.4f, ratio F_ren/F_eh = %.3f; offset b_N = %.3f" % (r["F_ren"], r["F_ren"] / r["F"], r["bN"]))
print("   phonons emitted above threshold per pair r = %.2f" % (r["phon_per_pair"] / w))
print("   sensitivity: 1 %% error in V_> alone moves F_eh by %.2f %%" % (100 * 0.01 * r["VP"] / r["F"]))
print("   phonon/ionization rate ratio one gap above threshold (x = 2 E_g): (105/2pi) sqrt(2 - w) lam = %.2f lam" %
      (105 / (2 * np.pi) * np.sqrt(2 - w)))

lams = [0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 2.0, lamSi, 6.0, 10.0, 20.0, 30.0]
rows = []
print("\nscan (w_ph = %.5f): lam_ph, eps/E_g, F_eh, V_<, V_>, 2V_<>, |2V_<> - remainder|, F_ren, F_ren/F_eh" % w)
for lam in lams:
    q = r if lam == lamSi else solve(lam)
    rows.append((lam, q["eps"], q["F"], q["VR"], q["VP"], q["Cov2"], q["F_ren"]))
    print("  %8.4f  %.4f  %.4f  %.4f  %.4f  %+.4f  %.1e  %.4f  %.3f" % (lam, q["eps"], q["F"], q["VR"], q["VP"], q["Cov2"],
                                                                       abs(q["Cov2"] - q["Cov2_rem"]), q["F_ren"],
                                                                       q["F_ren"] / q["F"]))
rows = np.array(rows)
np.save(os.path.join(HERE, "fig18_2_scan.npy"), rows)

fig, ax = plt.subplots(figsize=(6.0, 3.9))
L = rows[:, 0]
ax.plot(L, rows[:, 2], "k-", lw=1.8, label=r"$F_{\mathrm{eh}}$")
ax.plot(L, rows[:, 3], "C0--", lw=1.3, label=r"$\mathcal{V}_<$ (residual energy below threshold)")
ax.plot(L, rows[:, 4], "C3-.", lw=1.3, label=r"$\mathcal{V}_>$ (phonon energy above threshold)")
ax.plot(L, rows[:, 5], "C2:", lw=1.6, label=r"$2\mathcal{V}_{<>}$ (covariance)")
ax.axhline(0, color="0.6", lw=0.5)
ax.axvline(lamSi, color="0.5", lw=0.7, ls=":")
ax.text(lamSi * 1.08, 0.40, "Si", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlabel(r"phonon-loss parameter $\lambda_{\mathrm{AB}} = A_{\mathrm{AB}}/E_{\mathrm{g}}^3$")
ax.set_ylabel("contribution to the Fano factor")
ax.set_xlim(L[0], L[-1])
ax.legend(fontsize=7.5, loc="lower left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig18_2.pdf"))
print("\nwrote fig18_2.pdf; %.0f s" % (time.time() - t0))
