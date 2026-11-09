"""Limit 11.2a (Sect. 11.2): the Born-charge one-phonon structure factor of GaAs against the momentum transfer.

Formula (literature, zone center): S_ZZ = (pi q^2 Z*^2/(Omega mu eps_inf^2 omega_L)) delta(omega - omega_L), one LO branch with
the zone-center eigenvector (eq:11.2-onebranch).
Fuller result: eq:11.2-SZZ with the DFPT frequencies and eigenvectors at the actual q (gaas11_2.py: force constants of
Sect. 5.5, matdyn.x, site phases exp(i q.tau)), all six branches, rigid Born charges Z*_Ga = -Z*_As at every q.
Plotted: the weight of the three optical branches, sum_nu |sum_kappa e^{i q.tau} qhat.Z*.e*/sqrt(M)|^2/(2 omega_nu),
divided by its zone-center LO value Z*^2/(2 mu omega_L) (solid), and the acoustic weight in the same units (dotted), along
[100], [110], [111]. Both ratios are independent of Z* and eps_inf.
Modelling choice: the Born charges are held at their q = 0 value; the dynamical quadrupoles that complete the acoustic
(piezoelectric) charge and correct the optical vertex at order q a are not included.
Shaded: q < 0.04 (2 pi/a) = 88 eV, where the optical weight is within 1e-4 of the formula and the acoustic weight at most
1.06 % (along [110]).
Marked: q = omega_L/v_max = 13.7 eV, the smallest momentum transfer that reaches the LO phonon.
Output: tex/figures/ch11/limit11_2a.pdf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import gaas11_2 as G
import pol11_2 as P

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_2a.pdf")
QUNIT = 2 * np.pi / G.A_ANG * P.HBARC


def main():
    x = np.geomspace(1e-3, 0.6, 60)
    mu = G.M_GA * G.M_AS / (G.M_GA + G.M_AS)
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    styles = {"100": "C0", "110": "C2", "111": "C3"}
    for name, d in (("100", [1, 0, 0]), ("110", [1, 1, 0]), ("111", [1, 1, 1])):
        d = np.array(d, float) / np.linalg.norm(d)
        qs = x[:, None] * d
        w, e = G.run_matdyn(qs, "lim2a_" + name)
        B = G.born_weights(qs, w, e)
        w0, e0 = G.run_matdyn(1e-4 * d[None], "lim2a_g" + name)
        B0 = 1.0 / (2 * mu * w0[0, 5])
        opt, ac = B[:, 3:].sum(1) / B0, B[:, :3].sum(1) / B0
        ax.loglog(x, opt, color=styles[name], lw=1.4, label=f"optical, [{name}]")
        ax.loglog(x, ac, color=styles[name], lw=1.0, ls=":", label=f"acoustic, [{name}]")
        for xi in (0.04, 0.1, 0.2, 0.5):
            i = np.argmin(abs(x - xi))
            print(f"[{name}] q = {x[i]:.3f} (2pi/a) = {x[i]*QUNIT:6.0f} eV: optical/formula {opt[i]:.5f}, acoustic {ac[i]:.4f},"
                  f" omega_LO {w[i,5]:.2f} meV")
    ax.axvspan(1e-3, 0.04, color="0.9", zorder=0)
    ax.axvline(13.7 / QUNIT, color="0.4", lw=0.6, ls="--")
    ax.text(13.7 / QUNIT * 1.08, 0.15, r"$\omega_{\mathrm{L}}/v_{\mathrm{max}}$", fontsize=7, color="0.3")
    ax.set_xlim(1e-3, 0.6)
    ax.set_ylim(1e-4, 60)
    ax.set_xlabel(r"$q$ [$2\pi/a$]")
    ax.set_ylabel("one-phonon weight / zone-center LO")
    top = ax.secondary_xaxis("top", functions=(lambda t: t * QUNIT / 1e3, lambda t: t * 1e3 / QUNIT))
    top.set_xlabel(r"$q$ [keV]")
    ax.legend(fontsize=6.5, frameon=False, loc="upper right", ncol=2)
    fig.tight_layout()
    fig.savefig(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
