"""Limit 12.4a (Sect. 12.4): the Migdal probability with phonon final states at leading order (Berghaus, Esposito, Essig
and Sholapurkar, 2210.06490 Eqs. (3.6), (3.8)) against the exact second-order amplitude of a bound nucleus, as a function
of xi = v_N p / omega_e. Output: tex/figures/ch12/limit12_4a.pdf. Prints every number of the box (log: limit12_4a.log).

Literature form: amplitude (q.p / M omega_e^2) <f|exp(i(q - p).X)|0>, summed over every lattice final state f: the
  probability is (q.p/M omega_e^2)^2 for any lattice potential (osc12_4.py).
Fuller result: the two time orderings with their exact energy denominators, for a Si nucleus in an isotropic Einstein well
  w0 = 30.42 meV (<omega^-1>^-1 of the PBE DOS, the Einstein frequency with the Debye-Waller factor of the full DOS,
  Sect. 11.3), summed over all final vibrational states, averaged over the direction of p (osc12_4.averaged).
  Electron energy omega_e = 1.2 eV (near the Si gap, where the denominators are smallest). Two momenta given to the
  electrons: p = 5.7 keV (median of the Si weight, Sect. 12.3) for q <= 300 keV, and p = 22.5 keV (edge of the loss-function
  tables) to reach large xi with a tractable number of phonons.
Free nucleus (dashed): both denominators exact, b/((omega - b + a)(omega + a)), b = q.p/M, a = p^2/2M (osc12_4).
Leading correction (dotted): 1 + (9/5) xi^2 from the third term of the expansion of the free amplitude, angle-averaged
  (<c^4>/<c^2> = 3/5), which is also the bound result for xi >> w0/omega_e.
Gray band: xi where the literature form is within 10 % of the exact bound result. Vertical marks: xi at the impulse onset
  q = 92.5 keV (p = 5.7 keV) and at q = 300 keV.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import osc12_4 as O  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch12")
M = O.M_SI
WE = 1.2


def xi(q, p):
    return q * p / (M * WE)


rows = []
for p, qs in [(5.7e3, np.geomspace(2e3, 300e3, 12)), (22.5e3, np.geomspace(5e3, 700e3, 16))]:
    for q in qs:
        r, rpm, tr, z = O.averaged(q, p, WE)
        rows.append((p, q, xi(q, p), r, tr, z))
        print("p = %5.1f keV, q = %6.1f keV, xi = %.4f: exact/lead = %.5f (lead/exact = %.5f), truncation %.1e, "
              "free exact/lead = %.5f, 1 + 9/5 xi^2 = %.5f, zero-phonon fraction %.4f"
              % (p / 1e3, q / 1e3, xi(q, p), r, 1 / r, tr, O.free_exact_ratio(q, p, WE), 1 + 1.8 * xi(q, p)**2, z))
rows = np.array(rows)

xg = np.geomspace(1e-4, 0.6, 300)
free = np.array([O.free_exact_ratio(x * M * WE / 5.7e3, 5.7e3, WE) for x in xg])
lead_corr = 1 + 1.8 * xg**2
# 10 % point of lead/exact on the bound points (interpolate in xi)
order = np.argsort(rows[:, 2])
xs, rs = rows[order, 2], 1 / rows[order, 3]
x10 = np.interp(0.9, rs[::-1], xs[::-1])
print("Literature form within 10 %% of the exact bound result for xi <= %.3f; analytic (9/5) xi^2 = 0.1 at xi = %.3f"
      % (x10, np.sqrt(0.1 / 1.8)))
print("Small-q regime: xi at q = 92.5 keV, p = 5.7 keV: %.4f (correction %.1e)" % (xi(92.5e3, 5.7e3), 1.8 * xi(92.5e3, 5.7e3)**2))
print("q at which xi = %.3f for p = 5.7 keV: %.2f MeV (E_R = %.0f eV)"
      % (x10, x10 * M * WE / 5.7e3 / 1e6, (x10 * M * WE / 5.7e3)**2 / (2 * M)))
for p in (5.7e3, 22.5e3):
    small = rows[(rows[:, 2] < 0.01) & (rows[:, 0] == p)]
    print("p = %.1f keV, xi < 0.01: lead/exact - 1 = %.2e; leading-order 2 p^2/(M omega_e) - 2 w0^2/omega_e^2 = %.2e"
          % (p / 1e3, np.mean(1 / small[:, 3] - 1), 2 * p**2 / (M * WE) - 2 * (O.W_EIN / WE)**2))

fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(1e-4, x10, color="0.88", lw=0)
ax.plot(xg, 1 / free, color="C0", lw=1.0, ls="--", label="free nucleus, exact denominators")
ax.plot(xg, 1 / lead_corr, color="k", lw=0.8, ls=":", label=r"$1/(1 + (9/5)\,\xi^2)$")
for p, mk, lab in [(5.7e3, "o", r"bound, $p = 5.7$ keV"), (22.5e3, "s", r"bound, $p = 22.5$ keV")]:
    s = rows[:, 0] == p
    ax.plot(rows[s, 2], 1 / rows[s, 3], mk, ms=3.2, mfc="none", color="C3" if p > 6e3 else "C1", label=lab)
ax.axvline(xi(92.5e3, 5.7e3), color="0.4", lw=0.6, ls="-.")
ax.text(xi(92.5e3, 5.7e3) * 1.12, 0.62, "impulse onset\n($p = 5.7$ keV)", fontsize=6, color="0.3")
ax.set_xscale("log")
ax.set_xlim(1e-4, 0.6)
ax.set_ylim(0.55, 1.05)
ax.set_xlabel(r"$\xi = v_Np/\omega_e$  ($\omega_e = 1.2$ eV, electronic energy transfer)")
ax.set_ylabel("leading form / exact")
ax.legend(fontsize=6, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit12_4a.pdf"))
print("wrote", os.path.join(OUT, "limit12_4a.pdf"))
