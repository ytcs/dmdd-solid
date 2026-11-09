"""Fig. 12.2 (Sect. 12.2): atomic Migdal ionization spectra of isolated Si and Ge atoms at the recoil energy E_R = 1 keV.

Data: Cox, Dolan, McCabe and Quiney (arXiv:2208.12222) dipole tables per orbital (Dirac-Hartree-Fock), at q_e = m_e x 1e-3,
rescaled by (q_e/q_e,ref)^2 with q_e = m_e (2 E_R/m_A)^{1/2} (dipole order: every probability scales as q_e^2).
Dashed (Ge only): the total of Ibe et al. (arXiv:1707.07258), ancillary file Ge.dat, same rescaling.
x axis: the electronic energy transfer omega_e = E_ej + E_B (book convention: the energy the detector records), each
  shell shifted by its binding energy E_B. Measured values: cores from Sect. 3.5 / X-Ray Data Booklet as in mom12_5.py
  (Si 1s 1839, 2s 149.7, 2p 99.55 eV; Ge 1s 11103, 2s 1414.6, 2p 1227.4 (j-average), 3s 180.1, 3p 122.2 (j-average),
  3d 29.4 eV); valence shells at the measured first ionization energy of the atom (NIST ASD: Si 8.15168 eV, Ge 7.89943 eV),
  which is exact for the outer p shell and a lower limit for the valence s shell. The Ibe total (dashed) uses the same
  shifts. The total is summed on a common omega_e grid; integrated probabilities do not depend on the shift.
Prints the shell totals quoted in the text (also at the reference q_e, to compare with Ibe Table II).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atom12_2 as A  # noqa: E402

ER = 1e3
EB = {"Si": {"1s": 1839.0, "2s": 149.7, "2p": 99.55, "3s": 8.15168, "3p": 8.15168},
      "Ge": {"1s": 11103.0, "2s": 1414.6, "2p": (4 * 1217.0 + 2 * 1248.1) / 6, "3s": 180.1, "3p": (4 * 120.8 + 2 * 124.9) / 6,
             "3d": 29.4, "4s": 7.89943, "4p": 7.89943}}
WG = np.geomspace(1.0, 3e4, 1500)
COLORS = {"1s": "C7", "2s": "C5", "2p": "C2", "3s": "C4", "3p": "C1", "3d": "C3", "4s": "C9", "4p": "C0"}

if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.1), sharey=True)
    for ax, el in zip(axes, ("Si", "Ge")):
        s = (A.q_e(el, ER) / A.QE_REF)**2
        print(f"{el}: m_A = {A.MA[el] / 1e9:.4f} GeV, v = {A.v_recoil(el, ER):.4e}, q_e = {A.q_e(el, ER):.2f} eV, "
              f"(q_e/q_ref)^2 = {s:.5f}, xi(a0) = q_e a0 = {A.q_e(el, ER) / (A.ME * A.ALPHA):.4f}")
        sp = A.cox_dipole(el)
        tot = np.zeros_like(WG)
        Ptot = 0.0
        for orb in [o for o in COLORS if o in sp]:
            E, p = sp[orb]
            P = np.trapezoid(p, E)
            Ptot += P
            print(f"   {orb}: E_B = {EB[el][orb]:.2f} eV, P(q_ref) = {P:.3e}   P(E_R = 1 keV) = {P * s:.3e}")
            ax.loglog(E + EB[el][orb], p * s, color=COLORS[orb], lw=1.0, label=orb)
            tot += np.interp(WG, E + EB[el][orb], p * s, left=0.0, right=0.0)
        print(f"   total: P(q_ref) = {Ptot:.4e}, P(1 keV) = {Ptot * s:.4e} (on the omega_e grid {np.trapezoid(tot, WG):.4e})")
        ax.loglog(WG, np.where(tot > 0, tot, np.nan), color="k", lw=1.6, label="total")
        if el == "Ge":
            ib = A.ibe_spectra("Ge")
            Eg = ib[(1, 0)][0]
            ti = sum(np.interp(Eg, *ib[k]) for k in ib)
            tw = sum(np.interp(WG, ib[k][0] + EB[el][f"{k[0]}{A.LNAME[k[1]]}"], ib[k][1], left=0.0, right=0.0) for k in ib)
            ax.loglog(WG, np.where(tw > 0, tw * s, np.nan), color="k", ls="--", lw=1.0, label="total, local\npotential")
            print("   Ibe (FAC) total: P(q_ref) = %.4e, P(1 keV) = %.4e" % (np.trapezoid(ti, Eg), np.trapezoid(ti, Eg) * s))
            for k in sorted(ib):
                print("     Ibe %d%s: P(q_ref) = %.3e" % (k[0], A.LNAME[k[1]], np.trapezoid(ib[k][1], ib[k][0])))
        ax.set_xlim(5, 3e4)
        ax.set_ylim(1e-12, 3e-4)
        ax.set_xlabel(r"$\omega_e$ (electronic energy transfer, eV)")
        ax.text(0.95, 0.93, el, transform=ax.transAxes, ha="right", va="top", fontsize=10)
        ax.legend(fontsize=6.5, frameon=False, loc="lower left", ncol=2)
    axes[0].set_ylabel(r"$\mathrm{d}P/\mathrm{d}\omega_e$ (eV$^{-1}$)")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "fig12_2.pdf")
    fig.savefig(out)
    print("wrote", os.path.abspath(out))
