"""Transfer-kernel bound of Sect. 20.2 (eq:20.2-bound) evaluated for the two model births of Fig. 20.2 in Si, and the
memory threshold E_*/E_m for births spread over the whole band above E_m.  Log: bound20_2.log.
Run: python bound20_2.py > bound20_2.log  (about a minute).
Model and births: phon20_2.py (same as fig20_2.py).  At a fixed time t one propagator exp(G t) serves every birth, so:
  (1) Delta_h(t; E_m) = largest TV distance at t between line births in [E_m, f_top] (lines every 0.05 in ln f);
  (2) E_m(t) = the lowest E_m with Delta_h <= 1e-3 (scan on the grid), reported as E_*(t)/E_m;
  (3) bound = int_0^{E_m} |Delta rho_0| + Delta_h(t; E_m) against the actual TV distance of the evolved model spectra, which
      is the largest difference |O_NR - O_ER| over all observables with weights in [0, 1] acting on the energy spectrum at t.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon20_2 as P  # noqa: E402

m = P.MAT["Si"]
f, dln = P.grid(0.05e12, 1.2 * m["fD"], P.DLN)
G = P.operator(f, dln, m)
E = f * P.MEV_PER_THZ / 1e12
nr0 = P.birth_spike(f, m["fD"])
er0 = P.birth_er_si(f)
step = int(round(0.05 / dln))
itop = np.argmin(np.abs(f - m["fD"]))
for t in [1e-7, 1e-6, 3e-6]:
    U = P.propagator(G, t)
    idx = list(range(itop, 0, -step))[::-1]
    resp = {i: U[:, i] / U[:, i].sum() for i in idx}

    def dh(ilo):
        sel = [i for i in idx if i >= ilo]
        lo = min(sel)
        # the extreme pairs dominate; check all pairs against the lowest and the highest line, and all pairs if few
        best = 0.0
        for a in sel:
            for b in sel:
                if b > a:
                    best = max(best, 0.5 * np.abs(resp[a] - resp[b]).sum())
        return best
    em_i = None
    for i in idx:                       # ascending energy: first E_m with Delta_h <= 1e-3
        if dh(i) <= 1e-3:
            em_i = i
            break
    Em = E[em_i]
    Es = P.fstar(t, m) * P.MEV_PER_THZ / 1e12
    dhv = dh(em_i)
    l1 = np.abs(nr0 - er0)[E < Em].sum()
    unr, uer = U @ nr0, U @ er0
    act = P.tv(unr, uer)
    print(f"t = {t:.0e} s: E_* = {Es:.2f} meV; lowest E_m with Delta_h(lines in [E_m, 62 meV]) <= 1e-3: {Em:.2f} meV "
          f"(E_*/E_m = {Es/Em:.3f}); Delta_h there = {dhv:.2e}")
    print(f"   bound: L1 of birth difference below E_m = {l1:.4f}; + Delta_h = {l1 + dhv:.4f}; actual TV of model spectra = {act:.4f}")
    # factor-two band check at the same time
    ilo2 = np.argmin(np.abs(f - m["fD"] / 2))
    print(f"   Delta_h for lines in [31 meV, 62 meV] at this time = {dh(min(i for i in idx if i >= ilo2)):.2e}")
