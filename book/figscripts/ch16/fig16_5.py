"""Fig. 16.5 (fig:16-donor-lines): dark-photon absorption lines of Si:P, the loss function L = eps_2^D/eps_host^2 of
donors at n_D = 1e15 cm^-3 against the dark-photon mass, from the donor model of donor16_5.py (via donorspec16_5.py).
Solid: central-cell ground state (r_c = 3.2 A, 1s(A1) at 45.59 meV); dashed: effective-mass envelope with the same
measured transition energies.  Lines 1s(A1) -> np0, np+- (n = 2-4) drawn with a display width (Lorentzian, full width
0.1 meV); continuum and higher Rydberg states with a Gaussian of 1.5 meV (box discretization).  Dotted: the ionization
continuum of Du et al. (arXiv:2212.04504v1, Eq. (12) at q = 0, with their E_I = 45 meV, m* = 0.3 m_e, a* = 23 a.u.,
E_eff/E_0 = 2.2), at the same n_D and eps = 11.4 (they take |eps(0,0)| of silicon; the value cancels in the comparison of
shapes only up to (11.4/11.7)^2 = 0.95 if they used 11.7).
Printed: integrated line strengths, the continuum share, and the comparison numbers of the text.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import donorspec16_5 as S  # noqa: E402
import gos16_5 as G       # noqa: E402  (bracket, constants; runs its checks on import)

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
ND = 1e15
om = np.linspace(30.0, 80.0, 5001)

print("\n--- fig16_5 ---")
res = {}
for key in ("CC0.10", "EMT"):
    s = S.model(key)
    A = S.A_of_omega(s, om, 0.1, 1.5)
    L = S.L_lin(S.epsD(A, ND))
    res[key] = L
    print(f"[{key}] line strengths (cubic average |r|^2, A^2) and integrated L over each line (meV) at n_D = 1e15:")
    for ax, nm in (("z", "p0"), ("x", "p+-")):
        for n in range(3):
            r2, w = S.line_strength(s, ax, n)
            Lint = 4 * np.pi**2 * S.ALPHA * ND * 1e-24 * r2 / S.EPS**2 * S.HBARC * 1e3   # meV
            print(f"   {n+2}{nm:3s} at {w:6.2f} meV: |r|^2 = {r2:7.2f}, int L dw = {Lint:.3e} meV")
    sel = om > 45.59
    print(f"   continuum L at 50, 60, 70 meV: " + ", ".join(f"{np.interp(x, om, L):.2e}" for x in (50, 60, 70)))

sc, se = S.model("CC0.10"), S.model("EMT")
for ax, nm in (("z", "2p0"), ("x", "2p+-"), ("z", "3p0"), ("x", "3p+-")):
    n = 0 if nm.startswith("2") else 1
    print(f"   EMT envelope / central cell, {nm}: {S.line_strength(se, ax, n)[0]/S.line_strength(sc, ax, n)[0]:.2f}")

# Du et al. continuum at q = 0
kt = np.sqrt(np.clip(2 * G.MS * (om * 1e-3 - G.EI), 1e-30, None)) * G.AST / G.HBARC
pref = 4.84 * 2**10 * np.pi**2 * G.ALPHA * G.MS * (G.AST / G.HBARC)**4 / 3 * ND * 1e-24 * G.HBARC**3 / S.EPS**2
Ldu = np.where(om > 45.0, pref * G.bracket(1e-7, kt), np.nan)
for x in (50, 60, 70):
    print(f"   Du et al. Eq. (12), q = 0, at {x} meV: {np.interp(x, om, Ldu):.2e}  "
          f"(ratio to the central-cell model {np.interp(x, om, Ldu)/np.interp(x, om, res['CC0.10']):.2f}, "
          f"to the envelope model {np.interp(x, om, Ldu)/np.interp(x, om, res['EMT']):.2f})")

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.semilogy(om, res["CC0.10"], color="#2a78d6", lw=1.1, label="central-cell ground state")
ax.semilogy(om, res["EMT"], color="#2a78d6", lw=0.9, ls="--", label="effective-mass envelope")
ax.semilogy(om, Ldu, color="#d0452b", lw=1.2, ls=":", label="Du et al. continuum")
for lab, x, dx, ha in (("2p$_0$", 34.11, 0.0, "center"), ("2p$_\\pm$", 39.19, 0.0, "center"),
                       ("3p$_0$", 40.12, 0.2, "left"), ("3p$_\\pm$", 42.47, 0.0, "center")):
    win = abs(om - x) < 0.3
    yv = max(res["CC0.10"][win].max(), res["EMT"][win].max())   # label just above the taller of the two peaks
    ax.text(x + dx, yv * 1.15, lab, ha=ha, va="bottom", fontsize=7)
ax.axvline(45.59, color="0.5", lw=0.6)
ax.text(46.0, 3e-3, "ionization\n45.59 meV", fontsize=7, color="0.3")
ax.set_xlim(30, 80)
ax.set_ylim(1e-7, 1e-2)
ax.set_xlabel(r"dark-photon mass $m_\phi$ (meV)")
ax.set_ylabel(r"$L = \varepsilon_2^{\mathrm{D}}/\varepsilon_{\mathrm{host}}^2$ at $10^{15}$ cm$^{-3}$")
ax.legend(fontsize=7, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_5.pdf"))
print("wrote fig16_5.pdf")
