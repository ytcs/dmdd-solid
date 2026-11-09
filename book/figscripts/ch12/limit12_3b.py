"""Limit Check 12.3b (Sect. 12.3): the Migdal rate of silicon in the soft limit with free nuclear recoil (Liang, Mo,
Zheng and Zhang, arXiv:2011.13352, Eqs. (1), (7), (11), (12)), against two fuller results, as a function of the
dark-matter mass from 3 MeV to 1 GeV. Output: tex/figures/ch12/limit12_3b.pdf. Prints every number of the box and of
the validity paragraph of Sect. 12.3.

Literature form (their Eq. (11), soft limit of their Eq. (1)): amplitude factor (v_N.k)/omega^2 with v_N = q/M;
  v_min(q, omega) = q/2 mu_N + omega/q (their Eq. (8)). Their F(omega) (Eq. (12)) holds the G != G' terms of the
  symmetrized inverse dielectric matrix; here every curve uses the same diagonal loss function with local fields and
  Z_ion(k) (mig12), so that the ratios isolate the nuclear side.
Fuller result 1 (solid, "exact free-recoil amplitude"): the two time orderings for a free nucleus (their Eq. (1); the
  bracket of Eq. (12.4-corr)): with b = q.k/M and a = k^2/2M the energy denominators are omega - b + a (kick first)
  and omega + a (Coulomb exchange first), and the amplitude factor is B = b/[(omega - b + a)(omega + a)] exactly; its
  leading term is the soft limit b/omega^2, and the angle-averaged square is
  (b^2/omega^4)[1 - 2k^2/(M omega) + (9/5) v_N^2 k^2/omega^2 + ...]; there is no k^2/q^2 term. Angle average exact
  (Gauss-Legendre, 64 nodes). Where omega - b + a = 0 for some angle (v_N k >= omega + a) the second-order amplitude has
  a pole: the kicked nucleus, now moving, ionizes the electrons as a slow ion does (an on-shell two-step process, not
  a Migdal transition), and the expansion in the nuclear velocity has no meaning there. Such (omega, k) cells are
  excluded from BOTH rates of the ratio; their share of the soft-limit rate is printed and plotted (right axis).
  Energy balance as in the soft limit, omega_e + q^2/2M.
Leading correction (dotted): soft over soft x [1 - 2k^2/(M omega) + (9/5) v_N^2 k^2/omega^2], same cells.
Fuller result 2 (dashed with points, "bound nucleus"): soft-limit amplitude, nuclear factor = incoherent T = 0 response
  of a silicon nucleus at all phonon orders with its zero-phonon part (imp11.spectrum, PBE DOS of Sect. 5.2),
  omega = omega_e + omega_l in v_min; ten masses from 3 to 111 MeV (slow).
Plotted: soft over fuller, total rate omega_e >= 1.11 eV (tables), heavy mediator, sigma_n = 1e-38 cm^2, halo of
  Sect. 1.2, against m_chi; top axis E_R^max = 2 mu_N^2 v_max^2/M. Thin solid: the probability ratio at the
  end of the recoil spectrum, E_R = E_R^max. Gray band: masses where that ratio is within 10 % (every recoil the
  particle can produce).
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
import imp11 as IMP  # noqa: E402
import rate10_2 as R  # noqa: E402

MS = np.geomspace(3e6, 1e9, 48)
MB = np.geomspace(3e6, 150e6, 40)[::4]      # bound-nucleus masses, 3-111 MeV
SEL = G.OM >= G.EG
WE = G.OM[SEL]
K = G.KG[1:]
Z2 = G.ZG[1:]**2
LK = G.LF_G[SEL][:, 1:]                      # [omega, k]
CN, CW = np.polynomial.legendre.leggauss(64)
CW = CW / 2


def soft_dp(q):
    """dP/domega_e on WE for DM momentum transfer q, soft limit (= 4 alpha v_N^2 Q_Mig)."""
    return 4 * G.ALPHA * (q / G.M)**2 * G.qmig("lf")[SEL]


def cells(q):
    """Angle-averaged squared amplitude factors on [omega, k] for momentum transfer q: soft, exact, leading-corrected,
    and the mask of pole-free cells (v_N k < omega + k^2/2M)."""
    b = q * K[None, :] * CN[:, None] / G.M                               # [c, k]
    a = K[None, :]**2 / (2 * G.M)
    vN = q / G.M
    soft = np.empty((len(WE), len(K)))
    ex = np.empty_like(soft)
    for i, w in enumerate(WE):
        soft[i] = CW @ (b / w**2)**2
        ok = vN * K < w + K**2 / (2 * G.M)
        with np.errstate(divide="ignore", invalid="ignore"):
            e = CW @ (b / ((w - b + a) * (w + a)))**2
        ex[i] = np.where(ok, e, np.nan)
    lead = soft * (1 - 2 * K[None, :]**2 / (G.M * WE[:, None]) + 1.8 * (vN * K[None, :])**2 / WE[:, None]**2)
    good = np.isfinite(ex)
    return soft, np.nan_to_num(ex), lead, good


def dp(q):
    """dP/domega_e on WE: soft (all cells), soft (pole-free cells), exact, leading-corrected (pole-free cells)."""
    soft, ex, lead, good = cells(q)
    wt = (Z2[None, :] * LK) / (2 * np.pi**2) * 4 * G.ALPHA            # d^3k/(2pi)^3 Z^2 L/k^2 x k^2 dk
    f = lambda arr: np.trapezoid(wt * arr, K, axis=1)                # noqa: E731
    return f(soft), f(soft * good), f(ex * good), f(lead * good)


def rate(m, kind, nq=160):
    muN = G.mu(m, G.M)
    qmax = 2 * muN * R.VMAX
    q = np.geomspace(1e3, qmax, nq)
    tot = np.zeros((4, len(WE))) if kind == "free" else np.zeros_like(WE)
    for j in range(len(q)):
        qq = q[j]
        dq = qq * (np.log(q[1]) - np.log(q[0]))
        eta = R.eta(WE / qq + qq / (2 * muN))
        if kind == "free":
            tot += dq * qq * eta * np.array(dp(qq))
        elif kind == "soft":
            tot += dq * qq * eta * soft_dp(qq)
        elif kind == "bound":
            w, s, z = IMP.spectrum(qq)
            vm0 = WE / qq + qq / (2 * m)
            J = z * R.eta(vm0) + np.trapezoid(s[None, :] * R.eta((WE[:, None] + w[None, :]) / qq + qq / (2 * m)), w, axis=1)
            tot += dq * qq * J * soft_dp(qq)
    return np.trapezoid(tot, WE, axis=-1)


def main():
    print("Fixed recoil energy (probability, omega_e >= 1.11 eV): soft/exact and soft/leading-corrected on pole-free "
          "cells; pole share = soft probability in cells with v_N k >= omega + k^2/2M; (9/5)<v_N^2 k^2/omega^2>")
    for ER in [1, 3, 10, 30, 50, 100, 200, 300, 500, 1000]:
        q = np.sqrt(2 * G.M * ER)
        s_all, s_ok, ex, ld = [np.trapezoid(x, WE) for x in dp(q)]
        nine = np.trapezoid(np.trapezoid((Z2[None, :] * LK) * K[None, :]**2 / WE[:, None]**4 * 1.8 * (q / G.M * K[None, :])**2
                                         / WE[:, None]**2, K, axis=1), WE) / np.trapezoid(np.trapezoid(
                                         (Z2[None, :] * LK) * K[None, :]**2 / WE[:, None]**4, K, axis=1), WE)
        print(f"  E_R = {ER:5.0f} eV: soft/exact {s_ok/ex:.4f}, soft/leading {s_ok/ld:.4f}, pole share {1 - s_ok/s_all:.2e},"
              f" (9/5) term {nine:.4f}")
    ERs = np.geomspace(1, 1000, 200)
    r = []
    for ER in ERs:
        s_all, s_ok, ex, ld = [np.trapezoid(x, WE) for x in dp(np.sqrt(2 * G.M * ER))]
        r.append(s_ok / ex)
    r = np.array(r)
    print(f"  fixed E_R: soft within 10 % of exact for E_R <= {ERs[np.argmax(r < 0.9)]:.0f} eV")
    x = 2 * G.mu(MS, G.M)**2 * R.VMAX**2 / G.M
    res = np.array([rate(m, "free") for m in MS])                  # columns: soft all, soft ok, exact, lead
    r1 = res[:, 1] / res[:, 2]
    rl = res[:, 1] / res[:, 3]
    pole = 1 - res[:, 1] / res[:, 0]
    print(f"Rate: max |soft/exact - 1| for m_chi <= 150 MeV: {np.max(np.abs(r1[MS <= 150e6] - 1)):.1e}; "
          f"min soft/exact up to 1 GeV: {r1.min():.4f}; within 10 % at every mass: {bool(np.all(np.abs(r1 - 1) <= 0.1))}")
    pe = []
    for xx in x:
        s_all, s_ok, ex, ld = [np.trapezoid(v, WE) for v in dp(np.sqrt(2 * G.M * xx))]
        pe.append(s_ok / ex)
    pe = np.array(pe)
    bad = np.abs(pe - 1) > 0.10
    i1 = max(np.argmax(bad) - 1, 0) if bad.any() else len(MS) - 1
    print(f"Probability at the end of the recoil spectrum, E_R = E_R^max: within 10 % for m_chi <= {MS[i1]/1e6:.0f} MeV "
          f"(E_R^max = {x[i1]:.0f} eV); at 1 GeV ({x[-1]:.0f} eV) soft/exact {pe[-1]:.3f}")
    for f in [0.01, 0.10]:
        if (pole > f).any():
            i = np.argmax(pole > f)
            print(f"  pole share of the soft rate passes {f:.0%} at m_chi = {MS[i]/1e6:.0f} MeV (E_R^max = {x[i]:.0f} eV)")
    for m in [3e6, 5e6, 12e6, 16.5e6, 50e6, 150e6, 300e6, 500e6, 1e9]:
        i = np.argmin(abs(MS - m))
        print(f"  m = {MS[i]/1e6:7.1f} MeV, E_R^max = {x[i]:8.2f} eV: soft/exact {r1[i]:.4f}, soft/leading {rl[i]:.4f}, "
              f"pole share {pole[i]:.1e}")
    mb = MB
    xb = 2 * G.mu(mb, G.M)**2 * R.VMAX**2 / G.M
    rb = np.array([rate(m, "soft") / rate(m, "bound", nq=120) for m in mb])
    for m, xx, rr in zip(mb, xb, rb):
        print(f"  bound nucleus: m = {m/1e6:6.1f} MeV, E_R^max = {xx:7.3f} eV: free/bound {rr:.6f}")
    print(f"  max |free/bound - 1| = {np.max(np.abs(rb - 1)):.1e}")
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(MS[0] / 1e6, MS[i1] / 1e6, color="0.88", lw=0)
    ax.axhline(1.0, color="0.5", lw=0.6)
    ax.plot(MS / 1e6, r1, color="C3", lw=1.5, label="rate, over exact free-recoil amplitude")
    ax.plot(MS / 1e6, pe, color="C3", lw=0.9, label=r"probability at $E_R = E_R^{\max}$, same")
    ax.plot(MS / 1e6, rl, color="k", lw=0.9, ls=":", label=r"leading correction, $\frac{9}{5}v_N^2p^2/\omega_e^2 - 2p^2/M\omega_e$")
    ax.plot(mb / 1e6, rb, color="C0", lw=1.0, ls="--", marker="o", ms=2.5, label="over bound nucleus, all phonon orders")
    ax.set_xscale("log")
    ax.set_xlim(MS[0] / 1e6, MS[-1] / 1e6)
    ax.set_ylim(0.55, 1.05)
    ax.set_xlabel(r"$m_\chi$ (MeV)")
    ax.set_ylabel("soft-limit rate / fuller rate")
    ax2 = ax.twinx()
    ax2.plot(MS / 1e6, pole, color="C2", lw=0.9, ls="-.", label="pole share (right axis)")
    ax2.set_yscale("log")
    ax2.set_ylim(1e-6, 1)
    ax2.set_ylabel("pole share", color="C2")
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=6.3, frameon=False, loc="lower left")
    top = ax.secondary_xaxis("top", functions=(lambda mm: np.interp(mm, MS / 1e6, x),
                                               lambda xx: np.interp(xx, x, MS / 1e6)))
    top.set_xticks([0.1, 1, 10, 100])
    top.set_xticklabels(["0.1", "1", "10", "100"])
    top.set_xlabel(r"$E_R^{\max}$ (eV)")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_3b.pdf")
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
