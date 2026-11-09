"""Limits 11.2c and 11.2d (Sect. 11.2). Two outputs: tex/figures/ch11/limit11_2c.pdf and limit11_2d.pdf.

11.2c: eps_0 - eps_inf = e^2 Z*^2/(Omega mu omega_T^2) for one TO branch (eq:5.5-eps at omega = 0).
  Fuller result: eps_0 - eps_inf = sum_nu S_nu, the oscillator strengths of all polar branches on one axis, here from the
  lossless factorized eps of sapphire (ordinary and extraordinary rays; Griffin et al. 2018 v1 Tables I and II, as pol11_2.py).
  The one-branch formula applied to branch nu returns S_nu, i.e. the fraction S_nu/sum S of the full value (vertical axis).
  Horizontal axis: the share of the same branch in 1/eps_inf - 1/eps_0, w_nu/sum w, which is what the single-phonon rate uses.
  GaAs (one polar branch) sits at (1, 1). Shaded: both shares above 0.95.
11.2d: Z*/eps_inf from the LO-TO splitting, [Omega mu (omega_L^2 - omega_T^2)/(e^2 eps_inf)]^(1/2) (eq:11.2-Zeps), against the
  static route, which uses eps_0: Z*_static = [Omega mu omega_T^2 (eps_0 - eps_inf)/e^2]^(1/2). With measured inputs that miss
  the LST relation by r = (eps_0/eps_inf)/(omega_L/omega_T)^2 - 1, the ratio static/splitting is
  [((1 + r) omega_L^2 - omega_T^2)/(omega_L^2 - omega_T^2)]^(1/2). Plotted against r for GaAs (measured omega_L/omega_T of WE 5.6)
  and for LiF (omega_L/omega_T = 77.2/33.5 of Griffin et al. 2020 Table I). Marked: GaAs measured r = 1.186/1.169 - 1.
  Shaded: |r| below the value where the GaAs routes differ by 1 %.
GaAs inputs (WE 5.6): omega_T 33.62, omega_L 36.35 meV, eps_inf 10.88, eps_0 12.9, Omega = a^3/4 with a = 5.638 A,
  mu = 36.11 u. Error budget of eq:11.2-Zeps printed for 0.1 % frequency errors and 1 % in eps_inf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pol11_2 as P

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch11")


def limit_c():
    fig, ax = plt.subplots(figsize=(4.4, 3.4))
    for name, d, mk in (("sapphire, ordinary", P.SAPH_O, "o"), ("sapphire, extraordinary", P.SAPH_E, "s")):
        wp, eps0, S = P.factorized_weights(d["wL"], d["wT"], d["epsinf"])
        x, y = wp / wp.sum(), S / S.sum()
        print(name, "eps0 - einf =", round(S.sum(), 3), "; per branch (TO, LO meV; static share; loss share):")
        for i in range(len(x)):
            print(f"   {d['wT'][i]*1e3:6.2f} {d['wL'][i]*1e3:6.2f}  {y[i]:.3f}  {x[i]:.4f}")
        ax.plot(x, y, mk, mfc="none", color="C3" if mk == "o" else "C0", label=name)
    ax.plot([1], [1], "k*", ms=9, label="GaAs (one polar branch)")
    ax.plot([0, 1], [0, 1], color="0.6", lw=0.6, ls=":")
    ax.axvspan(0.95, 1.05, ymin=0.95 / 1.05, ymax=1, color="0.85", zorder=0)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(-0.02, 1.05)
    ax.set_xlabel(r"branch share of $1/\varepsilon_\infty - 1/\varepsilon_0$")
    ax.set_ylabel(r"one-branch formula / $(\varepsilon_0 - \varepsilon_\infty)$")
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit11_2c.pdf"))


def limit_d():
    g = P.GAAS
    Om = (g["a"]**3 / 4) / P.HBARC**3
    mu = P.mu_red(P.M_GA, P.M_AS) * P.U_EV
    dw2 = g["wL"]**2 - g["wT"]**2
    zeps = np.sqrt(Om * mu * dw2 / (P.E2 * g["epsinf"]))
    zs_split = zeps * g["epsinf"]
    zs_static = np.sqrt(Om * mu * g["wT"]**2 * (g["eps0"] - g["epsinf"]) / P.E2)
    r_gaas = (g["eps0"] / g["epsinf"]) / (g["wL"] / g["wT"])**2 - 1
    print(f"GaAs: Omega = {Om:.4e} eV^-3, mu = {mu:.4e} eV, wL^2 - wT^2 = {dw2:.4e} eV^2")
    print(f"Z*/eps_inf (splitting) = {zeps:.4f}; Z* = {zs_split:.3f}; static route Z* = {zs_static:.3f} ({zs_static/zs_split-1:+.3%});"
          f" LST residual r = {r_gaas:+.4f}")
    amp = g["wL"]**2 / dw2
    e_w = np.hypot(g["wL"]**2 * 1e-3, g["wT"]**2 * 1e-3) / dw2
    print(f"amplification omega_L^2/(omega_L^2 - omega_T^2) = {amp:.2f}; 0.1 % uncorrelated frequency errors -> {e_w:.4f};"
          f" with 1 % in eps_inf -> {np.hypot(e_w, 0.005):.4f}")
    r = np.linspace(-0.03, 0.03, 301)
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    rr = {}
    for name, wl, wt, col in (("GaAs", g["wL"], g["wT"], "k"), ("LiF", 77.2e-3, 33.5e-3, "C0")):
        ratio = np.sqrt(((1 + r) * wl**2 - wt**2) / (wl**2 - wt**2))
        rr[name] = ratio
        ax.plot(r * 100, ratio, color=col, lw=1.3, label=f"{name}: static / splitting")
    ax.axhline(1, color="0.5", lw=0.6, ls="--", label="splitting route (no $\\varepsilon_0$)")
    r1 = 0.02 * dw2 / g["wL"]**2
    print(f"GaAs routes within 1 % for |r| < {r1:.4f}")
    ax.axvspan(-r1 * 100, r1 * 100, color="0.88", zorder=0)
    ax.plot([r_gaas * 100], [zs_static / zs_split], "ko", ms=5)
    ax.annotate("GaAs, measured inputs", (r_gaas * 100, zs_static / zs_split), (0.3, 1.13), fontsize=7,
                arrowprops=dict(arrowstyle="-", lw=0.5))
    ax.set_xlabel(r"LST residual of the inputs, $r$ [%]")
    ax.set_ylabel(r"$Z^*$ (static) / $Z^*$ (splitting)")
    ax.set_xlim(-3, 3)
    ax.legend(fontsize=7, frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit11_2d.pdf"))


if __name__ == "__main__":
    limit_c()
    limit_d()
    print("wrote limit11_2c.pdf, limit11_2d.pdf")
