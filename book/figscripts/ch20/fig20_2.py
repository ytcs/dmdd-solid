"""Fig. 20.2 (fig:20-spectrum): phonon spectrum of a silicon event at 1, 10 and 100 ns, and the hard-part memory Delta_h(t)
for Si and Ge.  Log: fig20_2.log.  Run: python fig20_2.py > fig20_2.log  (a few minutes).
Model and inputs: phon20_2.py (isotropic-continuum cascade, x_L A f^5 for every phonon, Beta(3,3) daughters, no surfaces).
Births (MODELS, named in the caption): nuclear-recoil-like thermal spike (energy density ~ f^3 below the band top 15 THz);
electron-recoil-like optical-decay pairs (LA 42 meV + TA 22 meV, Gaussians of 10 % relative width) plus the soft fraction f_s = 1.71 % uniform in energy on
0.2-6 meV (phon20_2.birth_er_si).  Panel (b): Delta_h(t) as the largest TV distance between the evolved spectra of two line
births in the factor-two band [f_top/2, f_top] (six lines), and the TV distance of one pair concentrated near the top
(thermal spike against a Gaussian line at 0.95 f_top, width 0.05 f_top).  Si: A = 7.41e-56 s^4; Ge: A = 1.61e-55 s^4 (the
slowest published decay, [HP]), with the Ge band top 8.64 THz.  Crossings of 1e-3 found by brentq in ln t.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon20_2 as P  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
CT = {1e-9: "#2c6fbb", 1e-8: "#c0392b", 1e-7: "#27864a"}

fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.6, 3.1))
# ---------------- (a) Si spectra
m = P.MAT["Si"]
f, dln = P.grid(0.05e12, 1.2 * m["fD"], P.DLN)
G = P.operator(f, dln, m)
E = f * P.MEV_PER_THZ / 1e12
nr0 = P.birth_spike(f, m["fD"])
er0 = P.birth_er_si(f)
for t, c in CT.items():
    unr = P.evolve1(nr0, G, t)
    uer = P.evolve1(er0, G, t)
    k = 5
    sm = lambda u: np.convolve(u, np.ones(k) / k, mode="same") / dln     # energy per unit ln E
    ax.plot(E, sm(unr), color=c, lw=1.3, label=f"{t*1e9:.0f} ns")
    ax.plot(E, sm(uer), color=c, lw=1.1, ls="--")
    Es = m and P.fstar(t, m) * P.MEV_PER_THZ / 1e12
    ax.axvline(Es, color=c, lw=0.6, ls=":")
    tvt = P.tv(unr, uer)
    hard = E > 6.0
    tvh = P.tv(unr * hard, uer * hard)
    print(f"Si t = {t:.0e} s: E_* = {Es:.2f} meV; TV(NR-like, ER-like) whole spectrum = {tvt:.4f}; hard part (E > 6 meV) = {tvh:.2e}")
    print(f"   ER-like energy below 6 meV = {uer[E < 6].sum():.4f}; NR-like = {unr[E < 6].sum():.4f}")
for t in [3e-7, 1e-6, 1e-5]:
    unr = P.evolve1(nr0, G, t)
    uer = P.evolve1(er0, G, t)
    print(f"Si t = {t:.0e} s: E_* = {P.fstar(t, m)*P.MEV_PER_THZ/1e12:.2f} meV; TV(NR-like, ER-like) = {P.tv(unr, uer):.4f}; "
          f"hard part (E > 6 meV) = {P.tv(unr*(E > 6), uer*(E > 6)):.2e}")
for lim in [6.0, 10.0, 21.5]:
    print(f"births: energy below {lim} meV: NR-like {nr0[E < lim].sum():.4f}, ER-like {er0[E < lim].sum():.4f}; "
          f"L1 distance below = {np.abs(nr0 - er0)[E < lim].sum():.4f}")
ax.set_xscale("log")
ax.set_xlim(0.3, 80)
ax.set_yscale("log")
ax.set_ylim(1e-3, 10)
ax.set_xlabel(r"$E_{\mathrm{ath}}$ (meV)")
ax.set_ylabel(r"energy per unit $\ln E_{\mathrm{ath}}$ (fraction)")
ax.text(0.03, 0.95, "(a) Si", transform=ax.transAxes, va="top", fontsize=9)
ax.plot([], [], color="0.3", lw=1.3, label=r"$E^3$ birth")
ax.plot([], [], color="0.3", lw=1.1, ls="--", label="optical pairs + soft")
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.9))

# ---------------- (b) Delta_h(t), Si and Ge
times = np.logspace(-10, -5.3, 40)
out = {}
for name, col in [("Si", "#c0392b"), ("Ge", "#2c6fbb")]:
    mm = P.MAT[name]
    ff, dl = P.grid(0.05e12, 1.2 * mm["fD"], P.DLN)
    GG = P.operator(ff, dl, mm)
    ftop = mm["fD"]
    a0, b0 = P.birth_spike(ff, ftop), P.birth_top_line(ff, ftop)
    pair = lambda t: P.tv(P.evolve1(a0, GG, t), P.evolve1(b0, GG, t))
    band = lambda t: P.tau_lines(ff, GG, ftop / 2, ftop, t)
    tp = np.array([pair(t) for t in times])
    tb = np.array([band(t) for t in times])
    bx.plot(times * 1e9, tb, color=col, lw=1.3, label=f"{name}, two lines in [$f_{{\\rm top}}/2$, $f_{{\\rm top}}$]")
    bx.plot(times * 1e9, tp, color=col, lw=1.1, ls="--", label=f"{name}, spike vs line near top")
    tcp = P.crossing(pair, 1e-10, 1e-5)
    tcb = P.crossing(band, 1e-9, 4e-5)
    out[name] = (tcp, tcb)
    print(f"{name}: tau = 1e-3 for the near-top pair at t = {tcp*1e9:.1f} ns (E_* = {P.fstar(tcp, mm)*P.MEV_PER_THZ/1e12:.2f} meV);"
          f" for the factor-two band at t = {tcb*1e9:.0f} ns (E_* = {P.fstar(tcb, mm)*P.MEV_PER_THZ/1e12:.2f} meV,"
          f" E_*/E_lo = {P.fstar(tcb, mm)/(ftop/2):.3f})")
    for t in [1e-8, 3e-8, 1e-7, 1e-6]:
        print(f"   t = {t:.0e}: pair {pair(t):.2e}, band {band(t):.2e}")
    for A in mm["A_range"]:
        print(f"   A = {A:.3e}: near-top crossing scales as 1/A -> {tcp*mm['A']/A*1e9:.1f} ns; band {tcb*mm['A']/A*1e9:.0f} ns")
bx.axhline(1e-3, color="0.4", lw=0.8, ls=":")
bx.set_xscale("log")
bx.set_yscale("log")
bx.set_xlim(0.1, 5000)
bx.set_ylim(1e-7, 1.5)
bx.set_xlabel(r"$t$ (ns)")
bx.set_ylabel(r"$\Delta_{\mathrm{h}}(t)$")
bx.text(0.97, 0.95, "(b)", transform=bx.transAxes, fontsize=9, ha="right", va="top")
bx.legend(frameon=False, fontsize=7.5, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig20_2.pdf"))
print("wrote fig20_2.pdf")
