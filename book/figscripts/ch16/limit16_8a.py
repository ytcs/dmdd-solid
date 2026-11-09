"""Limit Check 16.8a (lim:16.8a, fig:16-limit-tlsrel): relaxation of a two-level system by conduction electrons.

Panel (a): superconducting factor.  Literature form: the normal-state (Black) rate times 2/(1 + exp(Delta_BCS/T))
(Meissner et al., arXiv:2103.06977, Eq. (9), stated there for E << Delta_BCS).  Fuller result: the golden-rule
quasiparticle integral with the case-I coherence factor (App. D.42, tls16_8.rs_full), weak-coupling BCS gap Delta(T)
of aluminum (T_c = 1.18 K, Delta(0) = 1.764 T_c).  Plotted: ratio full/literature against E/T at T/T_c = 0.2, 0.5, 0.8.
Dotted: the closed form sinh(u) K_1(u), u = E/2T, valid for T, E << Delta (D.42).  Grey: ratio within 10 % of one.
All thresholds are root-found (brentq) on the full integral.

Panel (b): ohmic coupling.  Literature (Born) form alpha_ohm = 4 K_b, K_b = (N_F V_d Omega)^2 (Maillet et al.,
arXiv:2009.03804, Eq. (4) with Black's rate; per-spin density of states).  Fuller result: the eigenphase form
alpha_ohm = (1/2 pi^2) sum_sigma sum_nu dtilde_nu^2 (App. E.10, eq:E.10-ohm) for one s-wave contact channel per spin,
with phase shifts delta = -/+ arctan(pi N_F V_d Omega) in the two configurations (App. D.42):
alpha_ohm = (4/pi^2) arctan^2(pi sqrt(K_b)).  Plotted: alpha_ohm/(4 K_b) against K_b.  Dashed: the leading correction
1 - (2/3) pi^2 K_b.  Markers: the resonator fits K_b = 0.07 and 0.11 (Maillet et al., text after Eq. (4)).
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.special import k1
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tls16_8 as t  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
os.makedirs(FIG, exist_ok=True)

# ---------- panel (a)
x = np.geomspace(0.01, 10, 160)
ratios = {}
for tt in (0.2, 0.5, 0.8):
    T = tt * t.TC_AL * t.KB
    D = t.bcs_gap(T)
    xs = x[x * T < 2 * D]          # quasiparticle scattering only: E < 2 Delta (no pair breaking)
    r = np.array([t.rs_full(xx * T, T, D) for xx in xs]) / t.rs_lit(T, D)
    ratios[tt] = (xs, r)
    x10 = brentq(lambda xx: t.rs_full(xx * T, T, D) / t.rs_lit(T, D) - 0.9, 0.05, 5)
    print(f"(a) T/T_c = {tt}: Delta(T)/Delta(0) = {D/t.DELTA0_AL:.4f}, 2f(Delta) = {t.rs_lit(T, D):.4g}; "
          f"full/lit = 0.9 at E/T = {x10:.3f}; at E/T = 1, 2, 5: "
          + ", ".join((f"{t.rs_full(v*T, T, D)/t.rs_lit(T, D):.3f}" if v * T < 2 * D else "above 2 Delta") for v in (1, 2, 5))
          + f"; curve ends at E = 2 Delta(T), E/T = {2*D/T:.2f}")
sk = np.sinh(x / 2) * k1(x / 2)
u10 = brentq(lambda u: np.sinh(u) * k1(u) - 0.9, 0.01, 3)
print(f"(a) closed form sinh(u)K1(u) = 0.9 at u = {u10:.4f}, E/T = {2*u10:.3f}; at E/T = 1, 2, 5: "
      + ", ".join(f"{np.sinh(v/2)*k1(v/2):.3f}" for v in (1, 2, 5)))
for tD in (0.005, 0.02):
    T = tD * t.DELTA0_AL
    print(f"    check T = {tD} Delta(0): full/lit at E/T = 1, 2, 5: "
          + ", ".join(f"{t.rs_full(v*T, T, t.DELTA0_AL)/t.rs_lit(T, t.DELTA0_AL):.4f}" for v in (1, 2, 5))
          + "  (closed form " + ", ".join(f"{np.sinh(v/2)*k1(v/2):.4f}" for v in (1, 2, 5)) + ")")
for v in (0.5, 1.0):
    u = v / 2
    lead = 1 + 0.5 * u**2 * (np.log(u / 2) + np.euler_gamma - 1 / 6)
    print(f"    leading term 1 + (u^2/2)(ln(u/2) + gamma_E - 1/6) at E/T = {v}: {lead:.4f} (closed form {np.sinh(u)*k1(u):.4f})")

# ---------- panel (b)
K = np.geomspace(1e-4, 1.0, 300)
ra = (4 / np.pi**2) * np.arctan(np.pi * np.sqrt(K))**2 / (4 * K)
K10 = brentq(lambda k: (np.arctan(np.pi * np.sqrt(k)) / (np.pi * np.sqrt(k)))**2 - 0.9, 1e-4, 1)
print(f"(b) alpha_ohm/(4K_b) = 0.9 at K_b = {K10:.4f} (pi sqrt(K_b) = {np.pi*np.sqrt(K10):.4f}, alpha_ohm = {4*K10*0.9:.4f})")
for kb in (0.07, 0.11):
    a_ex = (4 / np.pi**2) * np.arctan(np.pi * np.sqrt(kb))**2
    # inverse: the contact strength that reproduces the Born-fitted alpha = 4 kb
    xb = np.pi * np.sqrt(kb)
    xe = np.tan(np.pi * np.sqrt(4 * kb) / 2)
    print(f"    K_b = {kb}: Born alpha = {4*kb:.2f}; eigenphase alpha at the same V_d = {a_ex:.4f} (ratio {a_ex/(4*kb):.3f}); "
          f"pi N V Omega reproducing alpha = {4*kb:.2f}: Born {xb:.3f}, eigenphase {xe:.3f} (x{xe/xb:.3f})")
print(f"    largest alpha for one channel per spin (dtilde = pi): {(1/(2*np.pi**2))*2*np.pi**2:.1f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9))
xa10 = brentq(lambda xx: t.rs_full(xx * 0.5 * t.TC_AL * t.KB, 0.5 * t.TC_AL * t.KB,
                                    t.bcs_gap(0.5 * t.TC_AL * t.KB)) / t.rs_lit(0.5 * t.TC_AL * t.KB,
                                    t.bcs_gap(0.5 * t.TC_AL * t.KB)) - 0.9, 0.05, 5)
a1.axvspan(x[0], xa10, color="0.88", lw=0)
for tt, col in zip((0.2, 0.5, 0.8), ("C3", "C0", "C2")):
    a1.plot(*ratios[tt], color=col, lw=1.4, label=rf"$T = {tt}\,T_c$")
a1.plot(x, sk, "k:", lw=1.2, label=r"$\sinh u\,K_1(u)$")
a1.axhline(1, color="k", lw=0.6)
a1.set_xscale("log")
a1.set_xlim(x[0], x[-1]); a1.set_ylim(0, 1.1)
a1.set_xlabel(r"$\Delta_{\mathrm{tl}}/T$")
a1.set_ylabel(r"full / $2f(\Delta_{\mathrm{BCS}})$ form")
a1.legend(frameon=False, fontsize=7.5, loc="lower left")
a1.text(0.97, 0.86, "(a)", transform=a1.transAxes, ha="right", va="top")

a2.axvspan(K[0], K10, color="0.88", lw=0)
a2.plot(K, ra, "C3", lw=1.4, label="eigenphase")
a2.plot(K, 1 - (2 / 3) * np.pi**2 * K, "k--", lw=0.9, label=r"$1 - \frac{2}{3}\pi^2K_{\mathrm{b}}$")
a2.axhline(1, color="k", lw=0.6)
for kb in (0.07, 0.11):
    a2.plot([kb], [(np.arctan(np.pi*np.sqrt(kb))/(np.pi*np.sqrt(kb)))**2], "ko", ms=3.5)
a2.set_xscale("log")
a2.set_xlim(K[0], K[-1]); a2.set_ylim(0, 1.1)
a2.set_xlabel(r"$K_{\mathrm{b}} = (\mathcal{N}_{\mathrm{F}}V_{\mathrm{d}}\Omega)^2$")
a2.set_ylabel(r"$\alpha_{\mathrm{ohm}}/4K_{\mathrm{b}}$")
a2.legend(frameon=False, fontsize=7.5, loc="lower left")
a2.text(0.97, 0.86, "(b)", transform=a2.transAxes, ha="right", va="top")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_8a.pdf"))
print("saved limit16_8a.pdf")
