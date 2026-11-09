"""Boosted dark matter in silicon (Sect. 10.9, Limit 10.9b): the exact relativistic density row against the form of
Liang et al. (arXiv:2401.11971 Eqs. (4)-(6)), and the transverse row of the Fermi form (2608.20715 Eq. (2)).
Natural units, Heaviside-Lorentz; energies and momenta in eV.

Physics (derived in Sect. 10.9):
  exact density row (vector mediator, conserved currents):  D_nn = (pi sigma_e/mu^2) K (1 - w^2/Q^2)^2 [(q0^2 + mV^2)/(Q^2 - w^2 + mV^2)]^2
  source (2401.11971 Eq. (5)):                              D_nn = (pi sigma_e/mu^2) K [(q0^2 + mV^2)/(Q^2 - w^2 + mV^2)]^2
  K = [(2E - w)^2 - Q^2]/(4E(E - w)), common to both, so the ratio is (1 - w^2/Q^2)^2 at each (Q, w), for any mediator.
  Heavy mediator (mV -> infinity): weights Q^3 L (source) and Q^3 L (1 - w^2/Q^2)^2 (exact) per dQ dw.
  Light mediator (mV -> 0): source Q^3 L q0^4/(Q^2 - w^2)^2, exact q0^4 L / Q (Coulomb).
  Transverse row, light mediator, in medium (Fermi form, 2608.20715 Eq. (2)):
      L -> L + (v^2 - w^2/Q^2) Im[-Q^2/(w^2 eps_T - Q^2)]  in the exact weight q0^4 (...)/Q.
  Kinematics: a particle much heavier than the energies deposited and of speed v reaches Q >= w/v (Sect. 10.9:
  w <= v Q for any convex E(p)); the weights above are per dQ dw at fixed v, with the common phase-space factor of
  the delta function dropped (it cancels in every ratio).  Ratios are integrated over w from the tables' gap 1.11 eV
  to 89 eV (end of the tables) and over Q from w/v to 22.5 keV (end of the tables).
Inputs:
  L(Q, w): si_elf_binned.npz, RPA + LF (Knapen-Kozaczuk-Lin GPAW tables, directions averaged), held at the first bin
     (493 eV) below it, zero above 22.5 keV (modelling choice, as inel10_9.py).
  eps_T(Q, w) = eps(w) at Q -> 0 (Sect. 4.4: eps_T -> eps as Q -> 0), measured: Franta et al. 2017, 300 K, below 40 eV;
     Henke-Gullikson-Davis atomic scattering factors above (loaded by abs10_7.eps_si).  The transverse term matters only
     at Q ~ w sqrt(eps_1) <~ 0.3 keV, where the optical value applies; its value at larger Q falls as w^2 eps_2/Q^2.
     Mixing tabulated L with measured eps_T is a modelling choice: at 10 eV the table's first-bin L is 0.218, the
     measured L 0.247.
  The Cherenkov pole of the transverse term (Q^2 = w^2 eps_1, open for v^2 eps_1 > 1) is integrated exactly by the
     substitution Q^2 = a + b tan(theta), a = w^2 eps_1, b = w^2 eps_2:  int dQ/Q (v^2 - w^2/Q^2) Im[Q^2/(Q^2 - w^2 eps)]
     = (1/2) int dtheta (v^2 - w^2/Q^2(theta)).
Output: tex/figures/ch10/limit10_9b.pdf and the numbers quoted in Sect. 10.9.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rate10_2 as R
import inel10_9 as I
import abs10_7 as A

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
WG = np.arange(R.EG, 89.0, 0.05)
EPS = A.eps_si(WG)
QMAX = I.QTOP


def weights(v, nq=1500):
    """integrated weights over w and Q at speed v: source and exact, heavy and light; light transverse."""
    out = dict(src_h=0.0, ex_h=0.0, src_l=0.0, ex_l=0.0, tr_l=0.0)
    per_w = {k: np.zeros_like(WG) for k in out}
    for i, w in enumerate(WG):
        qmin = w / v
        if qmin >= QMAX:
            continue
        Q = np.geomspace(qmin * (1 + 1e-9), QMAX, nq)
        L = I.LF(Q, np.full_like(Q, w))
        f = (1 - w**2 / Q**2)**2
        per_w["src_h"][i] = np.trapezoid(Q**3 * L, Q)
        per_w["ex_h"][i] = np.trapezoid(Q**3 * L * f, Q)
        per_w["src_l"][i] = np.trapezoid(Q**3 * L / (Q**2 - w**2)**2, Q)
        per_w["ex_l"][i] = np.trapezoid(L / Q, Q)
        # transverse term, exact treatment of the pole
        a, b = w**2 * EPS[i].real, w**2 * EPS[i].imag
        th = np.linspace(np.arctan((qmin**2 - a) / b), np.arctan((QMAX**2 - a) / b), 20001)
        x = a + b * np.tan(th)
        per_w["tr_l"][i] = 0.5 * np.trapezoid(v**2 - w**2 / x, th)
    for k in out:
        out[k] = np.trapezoid(per_w[k], WG)
    return out, per_w


def main():
    vs = np.array([0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99])
    rh, rl, rt = [], [], []
    for v in vs:
        o, pw = weights(v)
        rh.append(o["ex_h"] / o["src_h"])
        rl.append(o["ex_l"] / o["src_l"])
        rt.append((o["ex_l"] + o["tr_l"]) / o["src_l"])
        lo = WG < 2.0
        pl = (WG > 10) & (WG < 20)
        hi = WG > 3.6
        print("v = %.2f: exact/source heavy %.4f, light %.4f; (density + transverse)/source light %.4f; bound (1-v^2)^2 = %.4f;"
              " transverse/density (light): all w %.3e, w < 2 eV %.3e, 10-20 eV %.3e, w > 3.6 eV %.3e"
              % (v, rh[-1], rl[-1], rt[-1], (1 - v**2)**2, o["tr_l"] / o["ex_l"],
                 np.trapezoid(pw["tr_l"][lo], WG[lo]) / np.trapezoid(pw["ex_l"][lo], WG[lo]),
                 np.trapezoid(pw["tr_l"][pl], WG[pl]) / np.trapezoid(pw["ex_l"][pl], WG[pl]),
                 np.trapezoid(pw["tr_l"][hi], WG[hi]) / np.trapezoid(pw["ex_l"][hi], WG[hi])))
    rh, rl, rt = map(np.array, (rh, rl, rt))
    assert np.all(rh >= (1 - vs**2)**2 - 1e-9) and np.all(rl >= (1 - vs**2)**2 - 1e-9)
    assert np.all(rh <= 1) and np.all(rl <= 1)
    # Cherenkov condition in silicon: v^2 eps_1 > 1 somewhere above the gap
    print("max eps_1 above the gap: %.1f at %.2f eV -> Cherenkov for v > %.3f; eps_1(1.2 eV) = %.2f -> v > %.3f"
          % (EPS.real.max(), WG[np.argmax(EPS.real)], 1 / np.sqrt(EPS.real.max()), EPS[2].real, 1 / np.sqrt(EPS[2].real)))
    within = vs[(np.abs(rl - 1) < 0.02) & (np.abs(rh - 1) < 0.02) & (np.abs(rt - 1) < 0.02)]
    print("all three within 2%% of the source for v in", within)

    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    fig, ax = plt.subplots(figsize=(4.6, 2.9))
    vv = np.linspace(0, 1, 200)
    ax.axvspan(0, 0.1, color="0.9", lw=0)
    ax.fill_between(vv, (1 - vv**2)**2, 1, color="C0", alpha=0.08, lw=0)
    ax.plot(vv, (1 - vv**2)**2, color="C0", lw=0.8, ls=":", label=r"bound $(1 - v^2)^2$")
    ax.axhline(1, color="0.45", lw=0.8, label="source form")
    ax.plot(vs, rh, color="C3", lw=1.6, ls=(0, (6, 2)), label="exact density row, heavy")
    ax.plot(vs, rl, color="C3", lw=1.2, ls="--", label="exact density row, light")
    ax.plot(vs, rt, color="k", lw=1.2, ls="-.", label="density + transverse, light")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.25)
    ax.set_xlabel(r"$v$")
    ax.set_ylabel(r"$\mathcal{R}/\mathcal{R}_{\rm source}$")
    ax.legend(frameon=False, fontsize=7, loc="lower left")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "limit10_9b.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
