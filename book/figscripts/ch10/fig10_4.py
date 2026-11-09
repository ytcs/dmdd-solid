"""Fig. 10.4 of Sect. 10.5: the loss function of silicon at |q| = 0.91 keV along [100], with and without the
electron-hole attraction, from the model transition-basis calculation of fig10_4_data.py (read its docstring for every
modelling choice: empirical pseudopotential of Cohen and Bergstresser, 4 + 4 bands, 10^3 shifted grid, 59 G, model
screened interaction of Cappellini et al. with eps_inf = 11.7, Lorentzian 0.15 eV).  Prints every number quoted in
Sect. 10.5 about the figure.  Output: tex/figures/ch10/fig10_4.pdf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
d = np.load(os.path.join(HERE, "fig10_4_data.npz"))
w = d["w"]
L = lambda e: (-1 / e).imag
Lip, Llf, Lbse, Lfull = L(d["eps_ip"]), L(d["eps_lf"]), L(d["eps_bse"]), L(d["eps_lf_full"])
Lres = L(d["epsres_bse"])
print("|q| = %.0f eV = %.3f A^-1; model gap %.3f eV; lowest pair at q %.3f eV; K^d diag mean %.1f meV; K^x mean %.2f meV"
      % (d["q"], d["qA"], d["egap"], d["Emin"], d["Kd_mean"] * 1e3, d["Kx_mean"] * 1e3))
print("static eps(q,0): head-only RPA %.3f, RPA+LF %.3f, BSE %.3f" % (d["st_ip"], d["st_lf"], d["st_bse"]))
print("checks: IP Haydock vs direct %.1e; resonant Dyson vs resolvent %.1e; coupling error RPA+LF eps2 %.1f%%, L %.1f%%"
      % (d["errip"], d["errdy"], 100 * d["cpl_e2"], 100 * d["cpl_L"]))
iw = lambda x: int(np.argmin(abs(w - x)))
for x in (1.3, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0):
    j = iw(x)
    print("w = %.1f: L_RPA %.5f L_LF %.5f L_BSE %.5f  BSE/LF %.3f  LF/RPA %.3f  res/full(BSE) %.3f" %
          (x, Lip[j], Llf[j], Lbse[j], Lbse[j] / Llf[j], Llf[j] / Lip[j], Lres[j] / Lbse[j]))
for lo, hi in ((0, 2.5), (0, 3.0), (0, 3.5), (3.5, 6.0), (6.0, 10.0)):
    m = (w >= lo) & (w < hi)
    print("int L over [%.1f, %.1f): BSE/LF = %.3f, LF/RPA = %.3f" % (lo, hi, Lbse[m].sum() / Llf[m].sum(),
                                                                    Llf[m].sum() / Lip[m].sum()))
m = w < 10
for nm, LL in (("RPA", Lip), ("LF", Llf), ("BSE", Lbse)):
    print("first moment int_0^10 w L: %s %.4f" % (nm, np.trapezoid(w[m] * LL[m], w[m])))
mm = (w > 1.0) & (w < 10)
print("mean energy of L below 10 eV: RPA %.2f, LF %.2f, BSE %.2f eV"
      % tuple(np.trapezoid(w[mm] * x[mm], w[mm]) / np.trapezoid(x[mm], w[mm]) for x in (Lip, Llf, Lbse)))
for nm in ("ip", "lf", "bse"):
    e2 = d["eps_" + nm].imag
    m3 = w < 3.0
    print("eps2 %s: peak %.2f at %.2f eV; int_0^3 eps2 = %.3f" % (nm, e2.max(), w[e2.argmax()], np.trapezoid(e2[m3], w[m3])))
if "spec_trip" in d.files:
    st, si = d["spec_trip"], d["spec_ip"]
    for lo, hi in ((0, 2.5), (0, 3.0), (2.5, 4.0), (4.0, 7.0)):
        m = (w >= lo) & (w < hi)
        print("triplet/IP spectral weight [%.1f, %.1f): %.3f" % (lo, hi, st[m].sum() / si[m].sum()))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.7))
s = (w > 1.0) & (w <= 7.0)
for ax in (a1, a2):
    ax.axvspan(1.0, d["Emin"], color="0.92", lw=0)
    ax.set_xlim(1, 7)
    ax.set_xlabel(r"$\omega$ [eV]")
a1.plot(w[s], d["eps_ip"].imag[s], color="0.5", ls="--", lw=1.0, label="independent pairs")
a1.plot(w[s], d["eps_lf"].imag[s], color="C0", lw=1.3, label="RPA + local fields")
a1.plot(w[s], d["eps_bse"].imag[s], color="C3", lw=1.5, label="Bethe\u2013Salpeter")
a1.set_ylabel(r"$\varepsilon_2(\boldsymbol{q},\omega)$")
a1.set_ylim(0, 30)
a1.legend(frameon=False, fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.9))
a1.text(0.03, 0.92, "(a)", transform=a1.transAxes)
a2.plot(w[s], Lip[s], color="0.5", ls="--", lw=1.0)
a2.plot(w[s], Llf[s], color="C0", lw=1.3)
a2.plot(w[s], Lbse[s], color="C3", lw=1.5)
a2.set_ylabel(r"$L(\boldsymbol{q},\omega)$")
a2.set_ylim(0, 0.14)
a2.text(0.03, 0.92, "(b)", transform=a2.transAxes)
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "fig10_4.pdf"))
print("written fig10_4.pdf")
