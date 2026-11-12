"""Fig. 16.5 (fig:16-donor-lines): dark-photon absorption lines of Si:P, the loss function L = eps_2^D/eps_host^2 of
donors at n_D = 1e15 cm^-3 against the dark-photon mass, from the donor model of donor16_5.py (via donorspec16_5.py).
Central-cell ground state (r_c = 3.2 A, 1s(A1) at 45.59 meV).  The effective-mass envelope is computed for the log only and
not drawn (removed from the text as a dominated model).  Lines 1s(A1) -> np0, np+- (n = 2-4) drawn with a display width (Lorentzian, full width
0.1 meV); continuum and higher Rydberg states with a Gaussian of 1.5 meV (box discretization).
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

fig, ax = plt.subplots(figsize=(5.6, 3.4))
ax.semilogy(om, res["CC0.10"], color="#2a78d6", lw=1.1)
for lab, x, dx, ha in (("2p$_0$", 34.11, 0.0, "center"), ("2p$_\\pm$", 39.19, 0.0, "center"),
                       ("3p$_0$", 40.12, 0.2, "left"), ("3p$_\\pm$", 42.47, 0.0, "center")):
    win = abs(om - x) < 0.3
    yv = res["CC0.10"][win].max()   # label just above the peak
    ax.text(x + dx, yv * 1.15, lab, ha=ha, va="bottom", fontsize=7)
ax.axvline(45.59, color="0.5", lw=0.6)
ax.text(46.0, 3e-3, "ionization\n45.59 meV", fontsize=7, color="0.3")
ax.set_xlim(30, 80)
ax.set_ylim(1e-7, 1e-2)
ax.set_xlabel(r"dark-photon mass $m_\phi$ (meV)")
ax.set_ylabel(r"$L = \varepsilon_2^{\mathrm{D}}/\varepsilon_{\mathrm{host}}^2$ at $10^{15}$ cm$^{-3}$")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_5.pdf"))
print("wrote fig16_5.pdf")
