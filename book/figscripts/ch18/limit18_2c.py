"""Limit Check 18.2c (lim:18.2c, fig:18-limit-renewal): the renewal (uncorrelated final-state) Fano estimate against the full F_eh.
Log: limit18_2c.log.  Run: python limit18_2c.py > limit18_2c.log  (about 3 min).  Solver: mom18_2.py; scan from fig18_2.py.

Renewal estimate (Subashiev and Luryi, arXiv:0911.1532, Eq. (7), in the form of Sect. 18.2): each pair costs E_g plus the residual
energies of one terminal electron and one terminal hole plus the phonon energy emitted above threshold; the costs are taken
independent and identically distributed, the residuals with the computed one-carrier statistics of each type and the phonon number
Poisson, so  F_ren = [sigma_e^2 + sigma_h^2 + omega_AB <E_>>/<N>]/eps_eh^2.
Cases (eps_eh and F_eh by the moment recursions; lam_ph -> 0 rows by Richardson on h = 0.01, 0.005, order 1 without phonons):
  (1) random parking: constant electron density of states, delta hole density of states, theta_ii = 1, no phonons (limit18_2b.py);
  (2) parabolic bands, theta_ii = 1, no phonons;   (3) parabolic bands, theta_ii = 3/2, no phonons;
  (4) silicon, theta_ii = 1 (the one silicon set of si_cascade18.py: E_g = 1.160 eV, omega_AB = 63 meV, W_h = 12 eV,
      A_AB = 5.703 eV^3);
  (5) silicon, theta_ii = 3/2, A_AB recalibrated to eps_eh = 3.749 eV in the continuum (table18_4.py, read from table18_4.json);
  (6) germanium with the book constants E_g = 0.744 eV (low temperature, Sect. 3.3) and omega_AB = 37.6 meV (optical phonon,
      Sect. 5.3), theta_ii = 1, the silicon A_AB (one constant for all materials), hole density of states cut at the germanium
      valence-band width 12.6 eV (measured Gamma_1 valence level -12.6 +- 0.3 eV, as tabulated by Rideau et al.,
      cond-mat/0607510, Table II), X = 60.
Cases (4)-(6) are continuum values (steps E_g/74 and E_g/148, extrapolated in h^(3/2); si_cascade18.mom_cont).
Line: the theta_ii = 1 silicon kernel scanned in lam_ph at the silicon w_ph (fig18_2_scan.npy).
Plot: F_ren/F_eh against lam_ph; the band 0.9-1 (within 10 %) is drawn and stays empty.
"""
import os
import re
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mom18_2 import Cascade, run
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI, mom_cont
import json

OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch18"))
scan = np.load(os.path.join(HERE, "fig18_2_scan.npy"))
A = A_AB
EG, OM, WH = EG_SI, OM_SI, BH_SI
w = OM / EG


def rich(theta, a=(0.5, 0.5), hole_delta=False, X=30.0):
    r = []
    for h in (0.01, 0.005):
        c = Cascade(0.0, 0.05, X=X, h=h, a=a, hole_delta=hole_delta, theta=theta, phonon=False)
        r.append(c.slopes())
    return {k: 2 * r[1][k] - r[0][k] for k in ("eps", "F", "F_ren", "VR", "VP", "Cov2")}


cases = []
q = rich(1.0, a=(0.0, 0.0), hole_delta=True)
cases.append(("random parking", 0.0, q))
q = rich(1.0)
cases.append(("parabolic, theta_ii = 1, no phonons", 0.0, q))
q = rich(1.5)
cases.append(("parabolic, theta_ii = 3/2, no phonons", 0.0, q))
q = mom_cont(A / EG**3, w, WH / EG, X=40.0)
cases.append(("Si, theta_ii = 1", A / EG**3, q))

# Si, theta_ii = 3/2, recalibrated in the continuum by table18_4.py (N = 74 makes 3/2 commensurate)
A15 = json.load(open(os.path.join(HERE, "table18_4.json")))["A_theta32"]
q = mom_cont(A15 / EG**3, w, WH / EG, X=40.0, theta=1.5)
print("Si theta_ii = 3/2: recalibrated A_AB = %.4f eV^3 (table18_4.json), eps = %.4f eV" % (A15, q["eps"] * EG))
cases.append(("Si, theta_ii = 3/2", A15 / EG**3, q))

EGe, OMe, BHe = 0.744, 0.0376, 12.6
q = mom_cont(A / EGe**3, OMe / EGe, BHe / EGe, X=60.0, N=None)
print("Ge (book constants, hole band cut at %.1f eV): lam_ph = %.3f, w_ph = %.5f, eps = %.4f eV" % (BHe, A / EGe**3, OMe / EGe,
                                                                                                   q["eps"] * EGe))
qn = run(A / EGe**3, OMe / EGe, X=60.0)
print("   same without the hole cut (one grid): F_ren/F_eh = %.3f" % (qn["F_ren"] / qn["F"]))
cases.append(("Ge, theta_ii = 1", A / EGe**3, q))

print("\ncase, lam_ph, eps/E_g, V_<, V_>, 2V_<>, F_eh, F_ren, F_ren/F_eh")
for name, lam, q in cases:
    print("  %-40s %7.3f  %.4f  %.4f  %.4f  %+.4f  %.4f  %.4f  %.3f" % (name, lam, q["eps"], q["VR"], q["VP"], q["Cov2"], q["F"],
                                                                       q["F_ren"], q["F_ren"] / q["F"]))
rat = scan[:, 6] / scan[:, 2]
print("\nscan, theta_ii = 1 silicon kernel: F_ren/F_eh from %.3f (lam_ph = %.3g) to %.3f (lam_ph = %.3g); max %.3f" %
      (rat[0], scan[0, 0], rat[-1], scan[-1, 0], rat.max()))
print("largest ratio over all cases and the scan: %.3f; F_ren <= F_eh in every case" %
      max(rat.max(), max(q["F_ren"] / q["F"] for _, _, q in cases)))

fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.axhspan(0.9, 1.0, color="0.88", lw=0)
ax.semilogx(scan[:, 0], rat, "k-", lw=1.6, label=r"parabolic bands, $\theta_{\mathrm{ii}} = 1$, silicon $w_{\mathrm{AB}}$")
xl = 1.2e-3
mk = ["o", "s", "^", "D", "v", "P"]
for (name, lam, q), m in zip(cases, mk):
    lab = {"random parking": "random parking",
           "parabolic, theta_ii = 1, no phonons": r"parabolic, $\theta_{\mathrm{ii}} = 1$, no phonons",
           "parabolic, theta_ii = 3/2, no phonons": r"parabolic, $\theta_{\mathrm{ii}} = 3/2$, no phonons",
           "Si, theta_ii = 1": r"Si, $\theta_{\mathrm{ii}} = 1$",
           "Si, theta_ii = 3/2": r"Si, $\theta_{\mathrm{ii}} = 3/2$",
           "Ge, theta_ii = 1": r"Ge, $\theta_{\mathrm{ii}} = 1$"}[name]
    ax.semilogx(lam if lam > 0 else xl, q["F_ren"] / q["F"], m, ms=6, mfc="none", mew=1.2, label=lab)
ax.axhline(1.0, color="0.4", ls=":", lw=0.8)
ax.text(1.55e-3, 0.80, r"$\leftarrow\ \lambda_{\mathrm{AB}} \to 0$", fontsize=8, color="0.3", va="center")
ax.set_xlim(8e-4, 40)
ax.set_ylim(0, 1.08)
ax.set_xlabel(r"phonon-loss parameter $\lambda_{\mathrm{AB}}$")
ax.set_ylabel(r"$F_{\mathrm{ren}}/F_{\mathrm{eh}}$")
ax.legend(fontsize=7, frameon=False, loc="lower left", ncol=1)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit18_2c.pdf"))
print("wrote limit18_2c.pdf")
