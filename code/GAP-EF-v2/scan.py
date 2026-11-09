"""GAP-EF-v2 scan.py (unchanged from v1 except comments): baseline model (theta = 1, a = 1/2) on a (lam, w) grid; least-squares fits of
eps/E_g = f(lam, w) and F = g(eps/E_g, w); writes data/scan.json. Deterministic quadrature (~5 min)."""
import json, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import run
from scipy.optimize import least_squares

LAMS = [0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
WS = [0.01, 0.02, 0.035, 0.05, 0.075, 0.1]

def f_eps(p, lam, w):      # eps/E_g = c0 + c1 (lam w^g)^b   (GAP-EF (EF9))
    c0, c1, g, b = p
    return c0 + c1 * (lam * w ** g) ** b

def f_F(p, e, w):          # F = a0 + a1 e + a2 e^2 + a3 w,  e = eps/E_g   (GAP-EF (EF10))
    a0, a1, a2, a3 = p
    return a0 + a1 * e + a2 * e ** 2 + a3 * w

if __name__ == "__main__":
    t0 = time.time(); rows = []
    for w in WS:
        for lam in LAMS:
            r = run(lam, 1.0, w, X=25.0, Nmax=300, nwmin=1)     # E_g = 1, A = lam
            rows.append(dict(lam=lam, w=w, e=float(r["eps_over_Eg"]), F=float(r["F"]), N=r["N"]))
        print(w, time.time() - t0, flush=True)
    fit = [r for r in rows if r["lam"] <= 100.0]          # fit domain lam <= 100. X = 25 is NOT the asymptote for lam > 5
    # (predict.py uses X = 60 there): at lam = 100, w = 0.05 the X = 25 values are off by ~1% in F and ~0.2% in eps
    # (GAP-EF-v2-C24, REF-GAP-EF-A R5); this edge bias is inside the fits' stated max residuals (2.3% / 0.52%).
    # v2: scan.json is the v1 output, not re-run (no v1 scan row is affected by the grid fix: w >= 0.01 gives N <= 300).
    lam = np.array([r["lam"] for r in fit]); w = np.array([r["w"] for r in fit])
    e = np.array([r["e"] for r in fit]); F = np.array([r["F"] for r in fit])
    pe = least_squares(lambda p: (f_eps(p, lam, w) - e) / e, [1.6, 2.3, 1.0, 0.25]).x
    pF = least_squares(lambda p: (f_F(p, e, w) - F) / F, [0.02, 0.04, 0.0, 0.0]).x
    re = f_eps(pe, lam, w) / e - 1; rF = f_F(pF, e, w) / F - 1
    out = dict(rows=rows, p_eps=list(pe), p_F=list(pF), eps_fit_maxrel=float(np.max(np.abs(re))),
               eps_fit_rms=float(np.sqrt(np.mean(re ** 2))), F_fit_maxrel=float(np.max(np.abs(rF))), F_fit_rms=float(np.sqrt(np.mean(rF ** 2))))
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), exist_ok=True)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "scan.json"), "w"), indent=1)
    print(out["p_eps"], out["eps_fit_maxrel"], out["eps_fit_rms"], out["p_F"], out["F_fit_maxrel"], out["F_fit_rms"], time.time() - t0)
