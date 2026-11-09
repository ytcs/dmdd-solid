"""Worked example 15.1 (we:15-alrate): pair-breaking rate of aluminum at m_chi = 1 keV, with the bulk gap
Delta_BCS = 0.18 meV and with the film convention Delta_BCS = 0.30 meV, for a heavy (F_DM = 1) and a light
(F_DM = (alpha m_e/q)^2) mediator.

Rate: Eq. (10.2-rate) of the book, T = 0, isotropic target,
  dR/domega = rho_chi sigma_e/(8 pi^2 alpha rho_T m_chi mu^2) Int dq q^3 eta(v_min) F_DM^2 L(q, omega),
  v_min = omega/q + q/(2 m_chi); reference cross section sigma_e = 1e-40 cm^2 (rates scale linearly with it).
Loss functions (bcs15.py): conserving response; bare bubble; g_I L_nor; Lindhard L_nor cut at omega >= 2 Delta;
  and the normal metal L_nor with no cut.
Quadrature: omega = 2 Delta + (omega_max - 2 Delta) t^2 (t Gauss-Legendre, graded toward the edge), q Gauss-Legendre
  between the two roots of v_min(q, omega) = v_max; convergence checked by doubling both grids (printed).
Inputs: bcs15.py.  Output: we15_1.log.
"""
import os
import numpy as np
import bcs15 as b

out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


M = 1e3
SIG = 1e-40
WMAX = 0.5 * M * b.VMAX**2


def rates(D, nw=60, nq=40, wtop=None):
    """Return dict model -> (R_heavy, R_light) in events/kg/yr, and the fractions of each from y < 3."""
    tg, tw = b.gl(nw)
    t = 0.5 * (tg + 1)
    wt = 0.5 * tw
    tot = {k: np.zeros(2) for k in ("cons", "bare", "gIn", "nor_cut", "nor_all")}
    low = {k: np.zeros(2) for k in tot}
    qg, qw = b.gl(nq)

    def win(w):
        disc = b.VMAX**2 - 2 * w / M
        return M * (b.VMAX - np.sqrt(disc)), M * (b.VMAX + np.sqrt(disc))

    for lo_w, models in ((2 * D, ("cons", "bare", "gIn", "nor_cut")), (1e-9, ("nor_all",))):
        for ti, wi in zip(t, wt):
            top = WMAX if wtop is None else wtop
            if lo_w >= top:
                continue
            w = lo_w + (top - lo_w) * ti**2
            jac = (top - lo_w) * 2 * ti * wi
            q1, q2 = win(w)
            qq = 0.5 * (q2 - q1) * qg + 0.5 * (q2 + q1)
            qwt = 0.5 * (q2 - q1) * qw
            y = w / D
            ker = qq**3 * b.eta(w / qq + qq / (2 * M)) * qwt
            fl = (b.Q0 / qq) ** 4
            for k in models:
                Ls = np.zeros(len(qq))
                for j, q in enumerate(qq):
                    Q = q * b.VF / D
                    pn = b.P_nor(y, Q)
                    if k == "nor_cut" or k == "nor_all":
                        Ls[j] = b.loss(pn, Q, D)
                    elif k == "gIn":
                        Ls[j] = float(b.gI(y)) * b.loss(pn, Q, D)
                    else:
                        pb, pc = b.P_resp(y, Q, n=16)
                        Ls[j] = b.loss(pc if k == "cons" else pb, Q, D)
                val = np.array([np.sum(ker * Ls), np.sum(ker * fl * Ls)]) * jac
                tot[k] += val
                if y < 3:
                    low[k] += val
    pf = b.per_kg_yr(b.prefactor(M, SIG))
    return {k: tot[k] * pf for k in tot}, {k: low[k] / tot[k] for k in tot}


pr(f"m_chi = {M / 1e3:.0f} keV, sigma_e = {SIG:.0e} cm^2, omega_max = {WMAX * 1e3:.3f} meV, rho_T = 2.70 g/cm^3")
res = {}
for D, lab in ((b.DELTA_BULK, "bulk 0.18 meV"), (b.DELTA_FILM, "film 0.30 meV")):
    R, fl = rates(D)
    R2, _ = rates(D, nw=120, nq=80)
    res[lab] = R
    pr(f"\nDelta = {lab}:  (events per kg yr; heavy, light)")
    for k in R:
        pr(f"  {k:8s} heavy {R[k][0]:.4e}  light {R[k][1]:.4e}   | doubled grids: {R2[k][0]:.4e} {R2[k][1]:.4e}"
           f"  | fraction from y < 3: heavy {fl[k][0]:.3f}, light {fl[k][1]:.3f}")
    Rl, _ = rates(D, wtop=3 * D)
    Rl2, _ = rates(D, nw=120, nq=80, wtop=3 * D)
    pr(f"  share of the conserving rate from 2 Delta < omega < 3 Delta (separate quadrature of that interval): "
       f"heavy {Rl['cons'][0] / R['cons'][0]:.3f}, light {Rl['cons'][1] / R['cons'][1]:.3f} "
       f"(doubled grids: {Rl2['cons'][0] / R2['cons'][0]:.3f}, {Rl2['cons'][1] / R2['cons'][1]:.3f})")
    for k in ("bare", "gIn", "nor_cut"):
        pr(f"  ratio {k}/cons: heavy {R[k][0] / R['cons'][0]:.3f}, light {R[k][1] / R['cons'][1]:.3f}")
    pr(f"  ratio cons/nor_all (normal metal, no gap): heavy {R['cons'][0] / R['nor_all'][0]:.3f}, "
       f"light {R['cons'][1] / R['nor_all'][1]:.3f}; inverse nor_all/cons: heavy {R['nor_all'][0] / R['cons'][0]:.3f}, "
       f"light {R['nor_all'][1] / R['cons'][1]:.3f}")
pr("\nBulk over film (same model):")
for k in ("cons", "bare", "gIn", "nor_cut"):
    a, c = res["bulk 0.18 meV"][k], res["film 0.30 meV"][k]
    pr(f"  {k:8s} heavy {a[0] / c[0]:.3f}  light {a[1] / c[1]:.3f}")
with open(os.path.join(b.HERE, "we15_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")
