"""Limit 10.5a (the Bethe-Salpeter exciton rate) of Sect. 10.5: comparison plot and the numbers quoted with it.

Output: tex/figures/ch10/limit10_5a.pdf.  The loss-function rate of Sect. 10.2 (eq:10.2-rate) is linear in L, so the
ratio of two evaluations of L at the same (q, omega) is the ratio of the rates they give there.  The plot shows, against
|q| at fixed omega, the loss function of a resonant-only response (one time ordering) divided by that of the response
with both time orderings:
    eps1 - 1      = (2/pi) P int_0^inf dw' w' eps2(w') / (w'^2 - w^2)      (both orderings; Kramers-Kronig)
    eps1_res - 1  = (1/pi) P int_0^inf dw' eps2(w') / (w' - w)            (resonant poles only)
    L_res / L     = (eps1^2 + eps2^2) / (eps1_res^2 + eps2^2)              (eps2 the same at w > 0)
  derived in Sect. 10.5 from eq:4.9-epsmac.  One-oscillator check (dashed): a single pole at E0(q) carrying the whole
  valence f-sum, eps1(q,0) - 1 = omega_p^2/E0^2, gives (eps1_res - 1)/(eps1 - 1) = (E0 + w)/(2 E0)  (eq:10.5-res).
Input: eps2 of the macroscopic dielectric function with local fields (eps2 of eps_mac = 1/(eps^-1)_00), averaged over
  directions in bins of 100 eV in |q|, from the silicon RPA tables of Knapen, Kozaczuk and Lin (arXiv:2101.08275,
  distributed with DarkELF, arXiv:2104.12786), reduced by si_elf_reduce.py to si_elf_binned.npz (key "e2lf"; the
  tables carry a scissor that puts the gap at 1.11 eV).  The tables end at 89 eV; the Kramers-Kronig static value is
  checked against the tabulated static step 1 - 1/eps(q, 0) (asserted to 1 %), which fixes the truncation error.
  omega_p = 16.6 eV (valence, Sect. 4.3).  Model comparison: Cappellini et al., Phys. Rev. B 47, 9892 (1993), static
  eps_C(q) with eps_inf = 11.7, k_TF = 4.12 keV, alpha_C = 1.563 (as fig10_2.py), fed to the one-oscillator formula.
Plot choices: omega = 1.3 eV (the energy of the phonon-assisted window at |q| ~ 0.7 A^-1 = 1.38 keV, Sect. 13.3) and
  3 eV; the band 1 +- 0.10 is the estimated coupling-block error of a retarded Tamm-Dancoff calculation (Sect. 10.5,
  eq:10.5-coupling); shaded: |q| where the resonant-only form is within 15 % of the full one.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch10")
d = R.load()
om, q = d["omega"], d["q"]
E2 = d["e2lf"]
WP = R.WP_VAL
HBARC = R.HBARC
wf = np.arange(0.0, om[-1], 0.002)


def kk(e2col, w):
    """Full and resonant-only eps1 at w from eps2 on the table grid (linear interpolation, subtracted PV)."""
    e2 = np.interp(wf, om, e2col)
    e2w = np.interp(w, om, e2col)
    X = wf[-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        # resonant: (1/pi) PV int e2(x)/(x - w)
        g = np.where(np.abs(wf - w) > 1e-9, (e2 - e2w) / (wf - w), 0.0)
        pv_res = np.trapezoid(g, wf) + (e2w * np.log((X - w) / w) if w > 0 else 0.0)
        # full: (2/pi) PV int x e2(x)/(x^2 - w^2) = (1/pi) PV int e2 [1/(x - w) + 1/(x + w)]
        pv_ant = np.trapezoid(e2 / (wf + w), wf) if w > 0 else np.trapezoid(np.where(wf > 0, e2 / np.maximum(wf, 1e-12), 0), wf)
    if w == 0:
        e1 = 1 + 2 / np.pi * pv_ant
        return e1, 1 + 1 / np.pi * pv_ant, 0.0
    return 1 + (pv_res + pv_ant) / np.pi, 1 + pv_res / np.pi, e2w


def eps_C(qq):
    return 1 + 1 / (1 / (11.7 - 1) + 1.563 * (qq / 4120.0)**2 + qq**4 / (4 * R.ME**2 * 16.6**2))


def one_osc(e0s, w):
    """Ratio L_res/L of a single oscillator with static eps(q,0) = e0s and the whole valence f-sum (eps2 ~ 0 at w)."""
    E0 = WP / np.sqrt(e0s - 1)
    e1 = 1 + (e0s - 1) * E0**2 / (E0**2 - w**2)
    e1r = 1 + (e1 - 1) * (E0 + w) / (2 * E0)
    return (e1 / e1r)**2, e1, e1r, E0


# --- check: Kramers-Kronig static value against the tabulated static step --------------------------------------------
worst = 0.0
for j in range(0, len(q), 5):
    e1s, _, _ = kk(E2[:, j], 0.0)
    tab = 1 / (1 - d["step_lf"][j])
    worst = max(worst, abs(e1s / tab - 1))
print("KK static eps(q,0) vs table static step: max relative difference %.2e" % worst)
assert worst < 0.01

curves = {}
for w in (1.3, 3.0):
    rat = np.empty(len(q))
    for j in range(len(q)):
        e1, e1r, e2 = kk(E2[:, j], w)
        rat[j] = (e1**2 + e2**2) / (e1r**2 + e2**2)
        if w == 1.3 and abs(q[j] - 1381) < 50:
            print("q = %.0f eV (%.2f A^-1), w = %.1f eV: eps1 = %.3f, eps1_res = %.3f, eps2 = %.1e, L_res/L = %.3f"
                  % (q[j], q[j] / HBARC, w, e1, e1r, e2, rat[j]))
            e0s = 1 / (1 - d["step_lf"][j])
            r1, a1, b1, E0 = one_osc(e0s, w)
            print("   one oscillator: eps(q,0) = %.3f, E0 = %.2f eV, eps1 = %.3f, eps1_res = %.3f, ratio %.3f"
                  % (e0s, E0, a1, b1, r1))
            ec = eps_C(q[j])
            r2, a2, b2, E0c = one_osc(ec, w)
            print("   Cappellini static %.3f: E0 = %.2f eV, eps1 = %.3f, eps1_res = %.3f, ratio %.3f" % (ec, E0c, a2, b2, r2))
    curves[w] = rat
osc = np.array([one_osc(1 / (1 - d["step_lf"][j]), 1.3)[0] for j in range(len(q))])
capp = np.array([one_osc(eps_C(qq), 1.3)[0] for qq in q])
for qq in (500, 1000, 1381, 2000, 3730, 5000, 8000, 12000):
    j = np.argmin(abs(q - qq))
    print("q = %5.0f eV: L_res/L = %.3f (1.3 eV), %.3f (3 eV); one oscillator %.3f; Cappellini %.3f"
          % (q[j], curves[1.3][j], curves[3.0][j], osc[j], capp[j]))
# validity: resonant-only within 15 % at 1.3 eV
ok = curves[1.3] <= 1.15
# first q above which every value is within 15 %
idx = np.where(~ok)[0]
qstar = q[idx.max() + 1] if len(idx) else q[0]
print("resonant-only within 15 %% of the full form at 1.3 eV for q >= %.0f eV" % qstar)
j0 = np.argmin(abs(q - 500))
print("at the smallest tabulated q (%.0f eV): L_res/L = %.2f; q -> 0 limit with eps = 11.7: [2 eps/(eps + 1)]^2 = %.2f"
      % (q[j0], curves[1.3][j0], (2 * 11.7 / 12.7)**2))
assert 1.6 < curves[1.3][np.argmin(abs(q - 1381))] < 2.4

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(qstar / 1e3, 22.5, color="0.92", lw=0)
ax.fill_between([0.4, 22.5], 0.9, 1.1, color="C0", alpha=0.18, lw=0, label=r"coupling block, $\pm 10\%$")
ax.plot(q / 1e3, curves[1.3], color="C3", lw=1.6, label=r"resonant-only, $\omega = 1.3$ eV")
ax.plot(q / 1e3, curves[3.0], color="C3", lw=1.0, ls=(0, (4, 2)), label=r"resonant-only, $\omega = 3$ eV")
ax.plot(q / 1e3, osc, color="k", lw=0.9, ls=":", label=r"one oscillator, $\omega = 1.3$ eV")
ax.axhline(1.0, color="C0", lw=1.2, label="both time orderings")
ax.axvline(1.381, color="0.4", lw=0.6, ls="-.")
ax.text(1.43, 2.75, r"$0.7\,\mathrm{\AA}^{-1}$", fontsize=7, color="0.3")
ax.set_xscale("log")
ax.set_xlim(0.45, 22.5)
ax.set_ylim(0.8, 3.2)
ax.set_xlabel(r"$|\boldsymbol{q}|$ [keV]")
ax.set_ylabel(r"$L/L^{\mathrm{full}}$")
ax.legend(frameon=False, fontsize=7, loc="upper right")
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "limit10_5a.pdf"))
print("written limit10_5a.pdf")
