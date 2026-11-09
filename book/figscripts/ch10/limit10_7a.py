"""Limit 10.7a (Sect. 10.7), two panels.  Output: tex/figures/ch10/limit10_7a.pdf

(a) Dark-photon absorption with in-medium mixing, R = (rho_chi/(rho_T m)) zeta_eff^2 sigma_1 = (rho_chi/(rho_T m)) zeta^2 m L
    (Hochberg, Lin and Zurek, arXiv:1608.01994, Eq. (7)), against its vacuum-mixing limit zeta^2 sigma_1 (An, Pospelov,
    Pradler and Ritz, arXiv:1412.8378, Eq. (20), valid for m^2 >> |Pi_em|).  Plotted: their ratio 1/|eps(m)|^2 for
    silicon, and the first-order term 1 + 2(1 - eps_1) of the expansion of 1/|1 - Pi_em/m^2|^2 in Pi_em/m^2 = 1 - eps.
    Shaded: masses where 1/|eps|^2 lies within 10 % of one.  Data: abs10_7.eps_si (Franta et al. 2017 at 300 K below
    40 eV; Henke et al. 1993 above).  Finite p_phi = 1e-3 m changes the transverse and longitudinal rates by O(1e-6)
    (abs10_7.py), invisible here.
(b) ALP-photon absorption in a static field B0 (Berlin and Trickle, arXiv:2305.05681, Eqs. (6) and (7)):
    Gamma = (g_agg^2 B0^2 / m) B0hat . Im[-eps^{-1}(m)] . B0hat (tensor form, derived in Sect. 10.7), against the
    isotropic formula evaluated with the dielectric function along the field, Im[-1/(B0hat . eps . B0hat)].
    Uniaxial crystal: sapphire, eps = diag(eps_perp, eps_perp, eps_par) with the c axis along z, B0 at 45 degrees to it.
    Phonon model (Griffin, Knapen, Lin and Zurek, arXiv:1807.10291 v1, Eq. (37), Table II; eps_inf = 3.2 from Table I):
      eps(w) = eps_inf prod_nu (w_LO^2 - w^2 - i w g_LO)/(w_TO^2 - w^2 - i w g_TO)
    (signs for time dependence e^{-i w t}); ordinary ray (perp): LO 906.6, 629.5, 481.7, 387.6; widths 16, 4.4, 1.4, 1.4;
    TO 633.6, 569.0, 439.1, 385.0; widths 3.8, 3.2, 1.5, 1.4 cm^-1 (77 K widths).  Extraordinary ray (par): LO 881.1,
    510.9; TO 582.4, 397.5 cm^-1, widths borrowed by the source from the ordinary ray (16, 1.4; 3.2, 1.5).
    1 cm^-1 = 0.123984 meV.  Silicon is cubic, and the two curves coincide there.
    Shaded: masses where the isotropic formula lies within 10 % of the tensor form.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import abs10_7 as A

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
CM_MEV = 0.123984198
O = dict(wL=[906.6, 629.5, 481.7, 387.6], gL=[16, 4.4, 1.4, 1.4], wT=[633.6, 569.0, 439.1, 385.0], gT=[3.8, 3.2, 1.5, 1.4])
E = dict(wL=[881.1, 510.9], gL=[16, 1.4], wT=[582.4, 397.5], gT=[3.2, 1.5])
EPS_INF = 3.2


def eps_saph(w_meV, d):
    w = np.asarray(w_meV, float) / CM_MEV          # in cm^-1
    e = EPS_INF * np.ones_like(w, dtype=complex)
    for wl, gl, wt, gt in zip(d["wL"], d["gL"], d["wT"], d["gT"]):
        e *= (wl**2 - w**2 - 1j * w * gl) / (wt**2 - w**2 - 1j * w * gt)
    return e


def shade_runs(ax, x, mask, **kw):
    i = 0
    while i < len(x):
        if mask[i]:
            j = i
            while j + 1 < len(x) and mask[j + 1]:
                j += 1
            ax.axvspan(x[i], x[j], **kw)
            i = j + 1
        else:
            i += 1


def main():
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.5))
    # (a)
    m = np.logspace(np.log10(1.2), 4, 4000)
    eps = A.eps_si(m)
    ratio = 1 / np.abs(eps)**2
    first = 1 + 2 * (1 - eps.real)
    ax = axs[0]
    ax.loglog(m, ratio, color="C3", lw=1.2, label=r"in medium / vacuum, $1/|\varepsilon|^2$")
    hi = m >= 20.0
    ax.loglog(m[hi], first[hi], color="0.4", lw=0.8, ls="--", label=r"first order, $1 + 2(1 - \varepsilon_1)$")
    ax.axhline(1.0, color="k", lw=0.8, label=r"vacuum mixing, $\zeta^2\sigma_1$")
    ok = np.abs(ratio - 1) <= 0.1
    m_asym = m[np.where(~ok)[0].max() + 1]          # the asymptotic region only (a sliver near 12.4 eV also passes)
    shade_runs(ax, m, ok & (m >= m_asym), color="0.88", lw=0, zorder=0)
    print(f"(a) other masses within 10 %: {m[ok & (m < m_asym)].min():.2f}-{m[ok & (m < m_asym)].max():.2f} eV (crossing, not shaded)")
    ax.set_xlim(1.0, 1e4)
    ax.set_ylim(1e-4, 50)
    ax.set_xlabel(r"$m_\phi$  [eV]")
    ax.set_ylabel(r"$\zeta_{\mathrm{eff}}^2/\zeta^2$")
    ax.set_title("(a) dark photon, silicon", fontsize=10)
    ax.legend(fontsize=9, frameon=False, loc="lower right")
    bad = np.where(~ok)[0]
    print(f"(a) 1/|eps|^2 within 10% of 1 for all m above {m[bad.max()+1]:.1f} eV; first-order form within 10 % of the full"
          f" factor above {m[np.where(np.abs(first/ratio-1) > 0.1)[0].max()+1]:.1f} eV")
    for m0 in (3.0, 10.0, 16.45, 30.0, 100.0):
        e = A.eps_si(np.array([m0]))[0]
        print(f"    m = {m0}: 1/|eps|^2 = {1/abs(e)**2:.4g}, first order {1+2*(1-e.real):.4g}")
    # (b)
    w = np.linspace(40, 120, 4001)
    ep, ez = eps_saph(w, O), eps_saph(w, E)
    th = np.deg2rad(45.0)
    c2, s2 = np.cos(th)**2, np.sin(th)**2
    tensor = (c2 * (-1 / ez) + s2 * (-1 / ep)).imag
    proj = (-1 / (c2 * ez + s2 * ep)).imag
    ax = axs[1]
    ax.semilogy(w, (-1 / ep).imag, color="C0", lw=0.6, alpha=0.6, label=r"$\mathbf{B}_0 \perp c$ (both forms)")
    ax.semilogy(w, (-1 / ez).imag, color="C2", lw=0.6, alpha=0.6, label=r"$\mathbf{B}_0 \parallel c$ (both forms)")
    ax.semilogy(w, tensor, color="C3", lw=1.3, label=r"$45^\circ$: $\hat{\mathbf{B}}_0\cdot\mathrm{Im}[-\varepsilon^{-1}]\cdot\hat{\mathbf{B}}_0$")
    ax.semilogy(w, proj, color="k", lw=1.0, ls="--", label=r"$45^\circ$: $\mathrm{Im}[-1/(\hat{\mathbf{B}}_0\cdot\varepsilon\cdot\hat{\mathbf{B}}_0)]$")
    okb = np.abs(proj / tensor - 1) <= 0.1
    shade_runs(ax, w, okb, color="0.88", lw=0, zorder=0)
    ax.set_xlim(40, 120)
    ax.set_ylim(1e-3, 3e3)
    ax.set_xlabel(r"$m_\phi$  [meV]")
    ax.set_ylabel(r"$\mathit{\Gamma}\, m_\phi/(g_{a\gamma\gamma}B_0)^2$")
    ax.set_title(r"(b) ALP in a field, sapphire", fontsize=10)
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit10_7a.pdf"))
    # numbers
    print(f"(b) isotropic-with-projection within 10 % of the tensor form on {okb.mean()*100:.0f} % of 40-120 meV")
    for wl in sorted(O["wL"] + E["wL"]):
        x = wl * CM_MEV
        i = np.argmin(abs(w - x))
        print(f"    near LO {x:.1f} meV: tensor {tensor[i]:.3g}, projected {proj[i]:.3g}, ratio {proj[i]/tensor[i]:.3g}")
    i = np.argmax(tensor)
    print(f"    tensor peak {w[i]:.1f} meV, {tensor[i]:.3g}; projected peak {w[np.argmax(proj)]:.1f} meV, {proj.max():.3g}")
    # identity check: tensor = cos^2/eps_par + sin^2/eps_perp ; difference = c2 s2 (ez-ep)^2/(ez ep eBB)
    diff = (c2 / ez + s2 / ep) - 1 / (c2 * ez + s2 * ep)
    chk = c2 * s2 * (ez - ep)**2 / (ez * ep * (c2 * ez + s2 * ep))
    print(f"    identity residual max |diff - c2 s2 (Δε)^2/(ε_par ε_perp ε_BB)| = {np.max(abs(diff-chk)):.2e}")
    print("wrote limit10_7a.pdf")


if __name__ == "__main__":
    main()
