"""Fig. 12.3 (Sect. 12.3): crystal and atomic Migdal spectra of silicon at the recoil energy E_R = 100 eV.
Output: tex/figures/ch12/fig12_3.pdf. Prints the totals quoted in the caption and the text.

Crystal (solid): soft-limit dP/domega_e = 4 alpha v_N^2 Q_Mig(omega_e) (eq:12.3-soft), v_N^2 = 2 E_R/M, with the loss function
  of Knapen, Kozaczuk and Lin with local fields (diagonal, direction-averaged; tables' scissor gap 1.11 eV; omega <= 89 eV,
  p <= 22.5 keV) and the valence ionization factor Z_ion(p) of mig12 (ld1 core orbitals). Dotted: Z_ion = 4 (point ion).
Atom (dashed): exclusive single ionization of the 3p shell of an isolated Si atom at dipole order, Dirac-Hartree-Fock tables
  of Cox, Dolan, McCabe and Quiney (arXiv:2208.12222, data release), read with the Sect. 12.2 loader (atom12_2.cox_dipole) at
  q_e = m_e x 1e-3 and rescaled by (q_e/q_e,ref)^2, q_e = m_e v_N (every dipole probability scales as q_e^2). The energy given
  to the electrons is omega_e = E_e + I, with I = 8.15 eV the measured first ionization energy of the Si atom (NIST ASD,
  8.15168 eV), the 3p threshold. The 3s, 2p, 2s and 1s shells are listed in the printout, not drawn (3s: its threshold is
  not that of the measured ionization energy; 2p, 2s, 1s lie above 100 eV).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mig12 as G  # noqa: E402
import atom12_2 as A  # noqa: E402

ER = 100.0
I_SI = 8.15168


def main():
    v = np.sqrt(2 * ER / G.M)
    w = G.OM
    sel = w >= G.EG
    cr = G.dP_domega(ER)
    cr4 = G.dP_domega(ER, zfix=4.0)
    Pc, Pc4 = np.trapezoid(cr[sel], w[sel]), np.trapezoid(cr4[sel], w[sel])
    s = (G.ME * v / A.QE_REF)**2
    sp = A.cox_dipole("Si")
    print(f"E_R = {ER} eV, v_N = {v:.4e}, q_e = m_e v_N = {G.ME*v:.2f} eV, scale (q_e/q_ref)^2 = {s:.4e}")
    print(f"crystal: P(omega >= {G.EG} eV) = {Pc:.3e} (Z_ion(p)), {Pc4:.3e} (Z_ion = 4)")
    tot = 0.0
    shells = {}
    for orb, (E, p) in sp.items():
        P = np.trapezoid(p, E) * s
        shells[orb] = P
        tot += P
        print(f"  atom {orb}: P = {P:.3e}")
    val = shells.get("3p", 0) + shells.get("3s", 0)
    print(f"  atom total {tot:.3e}, valence (3s + 3p) {val:.3e}; crystal / atomic valence = {Pc/val:.1f}, "
          f"crystal / atomic total = {Pc/tot:.1f}")
    E3p, p3p = sp["3p"]
    om3p = E3p + I_SI
    pa = p3p * s
    # crystal and atom per eV at a few energies
    for wc in [3.0, 5.0, 10.0, 20.0, 40.0]:
        print(f"  omega = {wc:4.0f} eV: crystal {np.interp(wc, w, cr):.3e} /eV, atom 3p {np.interp(wc, om3p, pa, left=0):.3e} /eV")
    i = np.argmax(w * cr)
    print(f"  crystal omega dP/domega peaks at {w[i]:.2f} eV; atom 3p at {om3p[np.argmax(om3p*pa)]:.2f} eV")
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.plot(w[sel], cr[sel], color="C3", lw=1.5, label=r"crystal, $Z_{\mathrm{ion}}(p)$")
    ax.plot(w[sel], cr4[sel], color="C3", lw=1.0, ls=":", label=r"crystal, $Z_{\mathrm{ion}} = 4$")
    m = om3p <= w[-1]
    ax.plot(om3p[m], pa[m], color="C0", lw=1.3, ls="--", label="isolated atom, 3p shell")
    ax.set_yscale("log")
    ax.set_xlim(0, 60)
    ax.set_ylim(1e-7, 3e-3)
    ax.set_xlabel(r"$\omega_e$ (eV)")
    ax.set_ylabel(r"$\mathrm{d}P/\mathrm{d}\omega_e$ (eV$^{-1}$)")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "fig12_3.pdf")
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
