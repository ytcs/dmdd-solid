"""Limit 12.3d (Sect. 12.3): the Wannier picture of the Migdal boost against the energy-weighted amplitude that rigid
Wannier following gives, in a tight-binding chain. Output: tex/figures/ch12/limit12_3d.pdf. Prints every number of the box
and of the text on the ordering of the projector.

Model (a labelled model, not silicon): open chain of N_s = 81 sites, lattice constant a, one valence orbital |n s> and
  one conduction orbital |n p> per site; on-site energies 0 and Delta, nearest-neighbour hoppings -t_s and +t_p
  (bandwidths W = 4 t_s and W_c = 4 t_p; W_c = W here); position operator x|n s> = n a |n s>, x|n p> = n a |n p>,
  <n s|x|n p> = d (intra-site dipole). The valence band is filled. With no s-p hopping the valence Wannier functions are
  exactly the |n s>, and the site-0 projector is p_0 = |0 s><0 s| (site 0 at the centre of the chain).
  Force operator: in a one-body tight-binding model the identity sum_i grad_i V = m_e [h, [h, x]] of a local Hamiltonian
  is taken as the definition of the force on the electrons; then <c|F|m> = m_e (e_c - e_m)^2 x_cm.
Amplitudes per unit (m_e q / M) for an interband transition v -> c, omega_cv = e_c - e_v:
  rigid Wannier following (energy-weighted, eq:12.3-AW):  A_W(c, v) = sum_{v'} [(e_c - e_v')^2 / omega_cv^2] x_cv' (p_0)_v'v
  Wannier picture of the boost (Liang et al., arXiv:1912.13484, Eqs. (2.7)-(2.8), first order in q_e):
                                                          A_b(c, v) = <c| x p_0 |v>
  Probabilities P = sum_{c,v} |A|^2. Plotted: P_b / P_W against x = W / omega_min, omega_min = E_g = Delta - (W + W_c)/2 the
  smallest omega_cv. Band: the absolute bound |A_W - A_b| <= (2 x' + x'^2) sum_v' |x_cv'| |(p_0)_v'v|, x' = W/omega_cv
  (eq:12.3-AWbound); for this p_0 of rank one the sum equals |A_b|, so per transition A_W/A_b lies in [1 - b, 1 + b],
  b = 2x + x^2 at omega_cv = omega_min, and P_b/P_W in [(1 + b)^-2, (1 - b)^-2]. Gray band: x where the bound is within 10 %.
Checks printed: (i) the site sum of A_W over all projectors p_n equals the full boost x_cv (acoustic sum rule, up to the
  chain ends); (ii) the symmetrized ordering (1/2){F, p_0} gives exactly half of A_W for interband transitions.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NS = 81
D = 0.3            # intra-site dipole in units of a
DELTA = 10.0       # centre separation of the bands, energy unit


def model(W, Wc=None):
    Wc = W if Wc is None else Wc
    ts, tp = W / 4, Wc / 4
    n = NS
    H = np.zeros((2 * n, 2 * n))
    X = np.zeros((2 * n, 2 * n))
    for i in range(n):
        H[i, i] = 0.0
        H[n + i, n + i] = DELTA
        X[i, i] = X[n + i, n + i] = i - n // 2
        X[i, n + i] = X[n + i, i] = D
        if i + 1 < n:
            H[i, i + 1] = H[i + 1, i] = -ts
            H[n + i, n + i + 1] = H[n + i + 1, n + i] = tp
    e, U = np.linalg.eigh(H)
    v = np.arange(n)            # lower n states: valence (no s-p hopping, so the bands separate exactly)
    c = np.arange(n, 2 * n)
    return e, U, X, v, c


def amplitudes(W, site=None):
    e, U, X, v, c = model(W)
    n = NS
    s0 = n // 2 if site is None else site
    xm = U.T @ X @ U                              # x in the eigenbasis
    p0 = np.outer(U[s0, :], U[s0, :])            # <a|0s><0s|b>
    ecv = e[c][:, None] - e[v][None, :]
    # rigid Wannier following, ket-side projector: sum over v' in the valence manifold
    wgt = (e[c][:, None] - e[v][None, :])**2      # (e_c - e_v')^2, indexed [c, v']
    AW = (wgt * xm[np.ix_(c, v)]) @ p0[np.ix_(v, v)] / ecv**2
    Ab = xm[np.ix_(c, v)] @ p0[np.ix_(v, v)]
    return e, ecv, AW, Ab, xm, p0, U, v, c


def main():
    # checks at one width
    W0 = 2.0
    e, ecv, AW, Ab, xm, p0, U, v, c = amplitudes(W0)
    # (i) site sum (acoustic sum rule): sum_n A_W(site n) = x_cv
    tot = np.zeros_like(AW)
    for s in range(NS):
        tot += amplitudes(W0, site=s)[2]
    full = xm[np.ix_(c, v)]
    err = np.max(np.abs(tot - full)) / np.max(np.abs(full))
    print(f"site sum of A_W against the full boost x_cv: max relative deviation {err:.2e}")
    assert err < 1e-8
    # (ii) symmetrized ordering: (1/2)<c|F p0 + p0 F|v>; p0 F has <c|p0 = 0 for c in conduction
    F = (e[:, None] - e[None, :])**2 * xm         # <a|F|b> / m_e = (e_a - e_b)^2 x_ab
    sym = 0.5 * (F @ p0 + p0 @ F)[np.ix_(c, v)] / ecv**2
    ratio = np.max(np.abs(sym - 0.5 * AW)) / np.max(np.abs(AW))
    print(f"symmetrized ordering minus half of A_W: max relative {ratio:.2e}")
    assert ratio < 1e-10
    # scan of the width
    xs, rs, bs = [], [], []
    for W in np.linspace(0.02, 4.5, 120):
        e, ecv, AW, Ab, *_ = amplitudes(W)
        Eg = DELTA - W            # W_c = W
        x = W / Eg
        PW, Pb = np.sum(AW**2), np.sum(Ab**2)
        ok = np.abs(AW) > 1e-14
        b_tr = 2 * (W / ecv) + (W / ecv)**2
        viol = np.max((np.abs(AW - Ab) - b_tr * np.abs(Ab))[ok])
        assert viol < 1e-10, viol
        xs.append(x)
        rs.append(Pb / PW)
        bs.append(2 * x + x**2)
    xs, rs, bs = map(np.array, (xs, rs, bs))
    lo = 1 / (1 + bs)**2
    hi = np.where(bs < 1, 1 / np.clip(1 - bs, 1e-9, None)**2, np.inf)
    xin = xs[np.argmax((hi > 1.1) | (lo < 1 / 1.1))]
    print(f"bound within 10 % for x = W/E_g <= {xin:.4f}")
    for xx in [0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.8]:
        print(f"  x = {xx:4.2f}: P_b/P_W = {np.interp(xx, xs, rs):.4f}, bound [{np.interp(xx, xs, lo):.3f}, "
              f"{np.interp(xx, xs, np.minimum(hi, 99)):.3f}]")
    xr = xs[np.argmax(np.abs(rs - 1) > 0.1)] if np.any(np.abs(rs - 1) > 0.1) else np.nan
    print(f"actual ratio leaves 10 % at x = {xr:.3f}")
    # silicon valence numbers for the text: W ~ 12 eV, omega 20-100 eV
    for om in [20.0, 50.0, 100.0]:
        xx = 12.0 / om
        print(f"  Si valence, W = 12 eV, omega_cv = {om:.0f} eV: bound b = {2*xx + xx**2:.2f}")
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(0, xin, color="0.88", lw=0)
    ax.fill_between(xs, lo, np.minimum(hi, 5), color="C0", alpha=0.18, lw=0, label="absolute bound")
    ax.axhline(1.0, color="k", ls="--", lw=1.0, label="rigid Wannier following (energy-weighted)")
    ax.plot(xs, rs, color="C3", lw=1.5, label="Wannier picture of the boost")
    ax.set_xlim(0, xs[-1])
    ax.set_ylim(0, 2.5)
    ax.set_xlabel(r"$W_{\mathrm{v}}/E_{\mathrm{g}}$")
    ax.set_ylabel("Migdal probability ratio")
    ax.legend(fontsize=6.5, frameon=False, loc="upper left")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_3d.pdf")
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
