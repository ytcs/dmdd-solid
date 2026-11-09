"""Limit 12.4b (Sect. 12.4): the phonon-mediated Migdal effect (Liang, Mo, Zheng and Zhang, 2205.03395 Eqs. (3.1)-(3.4)),
reduced to the electronic denominator 1/(eps_i - eps_j)^2 as in their Eq. (3.2) and rate Eq. (3.4), against the exact
second-order amplitude of a bound nucleus, as a function of omega_e / omega_ph. Output: tex/figures/ch12/limit12_4b.pdf.
Prints every number of the box (log: limit12_4b.log).

Literature form: amplitude (q.p/M omega_e^2) <f|exp(i q.X)|0> (virtual phonon reduced, multiphonon factor at q, T_0 included):
  probability (q.p / M omega_e^2)^2.
Their unreduced form (Eq. (3.1)): the propagator sum_nu (q.e)(p.e*)/(M (omega_e^2 - omega_nu^2)). For an Einstein site,
  (q.p)/(M (omega_e^2 - w0^2)); for the Si density of states (cubic site, incoherent; completeness of the polarizations)
  (q.p)/M * int dw g(w) / (omega_e^2 - w^2), g the normalized PBE DOS of Sect. 5.2 (imp11.G, band top 63.7 meV).
Fuller result: exact second order in an Einstein well w0 = 30.42 meV (osc12_4), q = 10 keV (E_R = 1.9 meV << w0), p = 5.7 keV,
  angle-averaged; omega_e from 1.15 w0 to 100 w0.
Gray band: omega_e where the reduced literature form is within 10 % of the exact Einstein result.
Leading correction: reduced/exact = 1 - 2 <w^2>/omega_e^2 (Einstein: <w^2> = w0^2; Si DOS: printed).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import osc12_4 as O  # noqa: E402
import imp11 as IMP  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch12")
W0 = O.W_EIN
Q, P = 10e3, 5.7e3

xs = np.concatenate([np.linspace(1.1513, 2.9913, 47), np.geomspace(3.05, 100, 40)])
ex, pm = [], []
for x in xs:
    r, rpm, tr, z = O.averaged(Q, P, x * W0)
    ex.append(r)
    pm.append(rpm)
    assert abs(tr) < 1e-8
ex, pm = np.array(ex), np.array(pm)
for x, r, rp in zip(xs[::6], ex[::6], pm[::6]):
    print("omega_e/w0 = %6.2f (omega_e = %.3f eV): reduced/exact = %.4f, propagator/exact = %.5f"
          % (x, x * W0, 1 / r, rp / r))
far = np.abs(xs - 2) > 0.1
print("max |propagator/exact - 1| away from the two-phonon resonance omega_e = 2 w0 (|x - 2| > 0.1): %.3f; "
      "nearest to it (x = %.3f): %.3f" % (np.max(np.abs(pm / ex - 1)[far]), xs[~far][np.argmax(np.abs(pm / ex - 1)[~far])],
                                       np.max(np.abs(pm / ex - 1)[~far])))
x10 = np.interp(0.9, (1 / ex), xs)
print("reduced form within 10 %% of exact for omega_e >= %.2f w0 = %.3f eV (analytic (1 - 1/x^2)^2 = 0.9 at x = %.2f)"
      % (x10, x10 * W0, 1 / np.sqrt(1 - np.sqrt(0.9))))

# Si density of states
wg, g = IMP.WG, IMP.G * IMP.DW
w2 = np.sum(g * wg**2)
print("Si DOS: <w^2>^(1/2) = %.2f meV, band top %.1f meV" % (np.sqrt(w2) * 1e3, wg[g > 0].max() * 1e3))
we = np.geomspace(0.075, 5.0, 400)
prop = np.array([np.sum(g / (w**2 - wg**2)) * w**2 for w in we])     # (omega_e^2 propagator), -> 1
red_over_prop = prop**-2
we10 = np.interp(0.9, red_over_prop, we)
print("Si DOS: reduced/propagator within 10 %% for omega_e >= %.3f eV (= %.2f x band top); at the gap 1.17 eV: %.5f; "
      "at 0.67 eV (Ge gap): %.5f" % (we10, we10 / wg[g > 0].max(), np.interp(1.17, we, red_over_prop),
                                     np.interp(0.67, we, red_over_prop)))
print("Si DOS leading correction 1 - 2<w^2>/omega_e^2 at 1.17 eV: %.5f" % (1 - 2 * w2 / 1.17**2))

fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(x10 * W0, 5.0, color="0.88", lw=0)
ax.plot(xs * W0, 1 / ex, "o", ms=2.6, mfc="none", color="C3", label=r"reduced / exact (Einstein, $\omega_0 = 30.4$ meV)")
ax.plot(xs * W0, pm / ex, "-", color="C0", lw=1.0, label="propagator / exact (Einstein)")
ax.plot(we, red_over_prop, "--", color="k", lw=0.9, label="reduced / propagator (Si density of states)")
ax.plot(xs * W0, 1 - 2 / xs**2, ":", color="C3", lw=0.8, label=r"$1 - 2\omega_0^2/\omega_e^2$")
ax.axvline(1.17, color="0.4", lw=0.6, ls="-.")
ax.text(1.22, 0.55, "Si gap", fontsize=6, color="0.3")
ax.axvline(wg[g > 0].max(), color="0.6", lw=0.6, ls=":")
ax.set_xscale("log")
ax.set_xlim(0.03, 5.0)
ax.set_ylim(0, 1.15)
ax.set_xlabel(r"$\omega_e$ (eV, electronic energy transfer)")
ax.set_ylabel("ratio of probabilities")
ax.legend(fontsize=6, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit12_4b.pdf"))
print("wrote", os.path.join(OUT, "limit12_4b.pdf"))
