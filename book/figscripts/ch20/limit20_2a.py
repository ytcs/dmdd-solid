"""Limit Check 20.2a (lim:20.2a, fig:20-limit-scaling): down-conversion and the scaling spectrum.  Log: limit20_2a.log.
Run: python limit20_2a.py > limit20_2a.log  (about a minute).
Formula: with Gamma_anh = A (E/h)^5 for longitudinal phonons and isotope mixing to the equilibrium L share x_L, the energy
spectrum tends to u(E, t) = (E_prompt/E_*) phi(E/E_*), E_*(t) = h (x_L A t)^(-1/5) (derived in Sect. 20.2), so that every
moment scales with E_*: the energy-weighted mean <E>(t) = c_phi E_*(t), with c_phi a property of the daughter kernel only.
Fuller result: the cascade of phon20_2.py (isotropic continuum, x_L A f^5, Beta(3,3) daughters, no surfaces) from three
hard births in Si (MODELS): a line at the band top 15 THz (62 meV); the thermal spike (f^3 energy density below 15 THz);
the optical-decay pairs LA 42 meV + TA 22 meV.  Plotted: <E>(t)/[c_phi E_*(t)] against t.  c_phi is read from the line birth
at t = 1 ms (where the ratio is constant to 1e-4).  Leading correction at early times: an undecayed line has <E> = E_0, so the
ratio is (x_L A f_0^5 t)^(1/5)/c_phi (dotted).  Validity: the time after which all three births are within 10 % (shaded),
found by brentq in ln t.  Si: A = 7.41e-56 s^4, x_L = 0.093.
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
m = P.MAT["Si"]
f, dln = P.grid(0.01e12, 1.2 * m["fD"], P.DLN)
G = P.operator(f, dln, m)
births = {
    "line at 62 meV": (P.line(f, m["fD"]), "#c0392b", "-"),
    "thermal spike": (P.birth_spike(f, m["fD"]), "#2c6fbb", "-"),
    "optical-decay pairs": (P.birth_er_si(f, soft=0.0), "#27864a", "-"),
}


def mean_ratio(u0, t):
    u = P.evolve1(u0, G, t)
    return np.sum(u * f) / np.sum(u) / P.fstar(t, m)


cphi = mean_ratio(births["line at 62 meV"][0], 1e-3)
print(f"c_phi = <E>/E_* at 1 ms (line birth) = {cphi:.5f}; at 100 us: {mean_ratio(births['line at 62 meV'][0], 1e-4):.5f}")
for nm, (u0, _, _) in births.items():
    print(f"  {nm}: c at 100 us = {mean_ratio(u0, 1e-4):.5f}")
# kernel check: second scaling moment (energy-weighted rms of ln E) at 1 ms
u = P.evolve1(births["line at 62 meV"][0], G, 1e-3)
y = f / P.fstar(1e-3, m)
w = u / u.sum()
print(f"scaling spectrum at 1 ms: energy-weighted median E/E_* = {np.interp(0.5, np.cumsum(w), y):.3f}; "
      f"10/90 % points {np.interp(0.1, np.cumsum(w), y):.3f} / {np.interp(0.9, np.cumsum(w), y):.3f}")
times = np.logspace(-11.5, -5, 90)
fig, ax = plt.subplots(figsize=(4.6, 3.1))
rat = {nm: np.zeros(len(times)) for nm in births}
for i, t in enumerate(times):
    for nm, (u0, c, ls) in births.items():
        rat[nm][i] = mean_ratio(u0, t) / cphi
for nm, (u0, c, ls) in births.items():
    ax.plot(times * 1e9, rat[nm], color=c, ls=ls, lw=1.3, label=nm)
# leading correction for the top line
r0 = (m["xL"] * m["A"] * m["fD"] ** 5 * times) ** 0.2 / cphi
ax.plot(times * 1e9, r0, color="k", ls=":", lw=1.0, label="undecayed line")


def tval(nm):
    u0 = births[nm][0]
    g = lambda t: abs(mean_ratio(u0, t) / cphi - 1)
    # last crossing of 10 %: scan, then brentq on the bracket
    tt = times
    v = np.abs(rat[nm] - 1)
    idx = np.where(v > 0.1)[0]
    if len(idx) == 0:
        return tt[0]
    i = idx[-1]
    return P.crossing(lambda t: g(t) + 1e-30, tt[i], tt[i + 1], level=0.1)


t10 = {nm: tval(nm) for nm in births}
for nm, t in t10.items():
    print(f"  {nm}: within 10 % of the scaling law after t = {t*1e9:.3f} ns (E_* = {P.fstar(t, m)*P.MEV_PER_THZ/1e12:.1f} meV)")
tv10 = max(t10.values())
print(f"validity (all three within 10 %): t >= {tv10*1e9:.3f} ns; initial decay time 1/(x_L A f_top^5) = {1/(m['xL']*m['A']*m['fD']**5)*1e9:.3f} ns")
for nm in births:
    for t in [1e-9, 1e-8, 1e-7]:
        print(f"  {nm}: ratio at {t:.0e} s = {np.interp(np.log(t), np.log(times), rat[nm]):.4f}")
ax.axvspan(tv10 * 1e9, 1e4, color="0.88", lw=0)
ax.axhline(1.0, color="0.3", lw=0.8)
ax.set_xscale("log")
ax.set_xlim(times[0] * 1e9, times[-1] * 1e9)
ax.set_ylim(0.4, 2.2)
ax.set_xlabel(r"$t$ (ns)")
ax.set_ylabel(r"$\langle E_{\mathrm{ath}}\rangle / (0.667\,E_*)$")
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_2a.pdf"))
print("wrote limit20_2a.pdf")
