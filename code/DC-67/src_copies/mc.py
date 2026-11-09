"""GAP-EF-v3 mc.py: independent Monte Carlo of the exact (continuous-energy) GAP-EF cascade at the TRUE omega_0, for Si, Ge and diamond
(V0: theta_ii = 1, a_DOS = 1/2, the v3-calibrated A_ph).  It shares no code with cascade.py/model.py: no grid, no recursion.
Process (GAP-EF-v2 (H-EF1)-(H-EF7), units E_g = 1): a carrier of type t (0 = e, 1 = h) at x >= theta does ii with probability
  p_t(x) = 1/(1 + lam rho_t(x - w)/Phi_t(x - 1)),  rho_t(x) = sqrt(x) (hole: times 1[x <= W], W = W_v/E_g for Si, infinite otherwise),
  Phi_0(y) = (pi/8) int_0^min(y,W) s^(1/2)(y - s)^2 ds (e, e, h products; closed form below), Phi_1(y) = (2 pi/105) y^(7/2) (h, h, e; a hole
  never exceeds W, so its products are untruncated),
and then splits x - 1 into (t, t, tbar) with density rho_t rho_t rho_tbar: Dirichlet(3/2, 3/2, 3/2), rejecting rows with a hole above W.
Otherwise it emits one phonon, x -> x - w.  Below theta it is terminal.  N = number of ii events from one electron seed at x0
(the quantity m_0(x0), s_0(x0) - m_0(x0)^2 of cascade.py).
Output data/mc.json: per material and x0 in {10, 20, X/2, X} (X = 40, 60, 25 as in predict.py): mean and variance of N with standard
errors; the secant slopes between x0 = 10 and 20; and eps_MC, F_MC from the secant over the asymptotic window [X/2, X].  M = 10^6 histories per point (chunks of 2 x 10^5; vectorised; ~2-4 min in all)."""
import json, os, sys, time
import numpy as np

def phi0(y, W):
    m = np.minimum(y, W) if W is not None else y
    return (np.pi / 8) * (y * y * (2 / 3) * m ** 1.5 - 2 * y * (2 / 5) * m ** 2.5 + (2 / 7) * m ** 3.5)

def phi1(y):
    return (2 * np.pi / 105) * y ** 3.5

def cascade_mc(lam, w, x0, M, W=None, theta=1.0, seed=1):
    rng = np.random.default_rng(seed)
    cnt = np.zeros(M)
    E = np.full(M, float(x0)); T = np.zeros(M, np.int8); H = np.arange(M)
    while E.size:
        keep = E >= theta
        E, T, H = E[keep], T[keep], H[keep]
        if not E.size: break
        y = E - 1.0; xm = E - w
        rho = np.sqrt(np.maximum(xm, 0.0))
        if W is not None:
            rho = np.where((T == 1) & (xm > W), 0.0, rho)
            assert not np.any((T == 1) & (E > W + 1e-12))
        Phi = np.where(T == 0, phi0(y, W), phi1(y))
        with np.errstate(divide="ignore", invalid="ignore"):
            p = np.where(Phi > 0, 1.0 / (1.0 + lam * rho / np.where(Phi > 0, Phi, 1.0)), 0.0)
        ii = rng.random(E.size) < p
        cnt += np.bincount(H[ii], minlength=M)
        # ii products
        yi, ti, hi = y[ii], T[ii], H[ii]
        n = yi.size
        D = np.empty((n, 3))
        todo = np.arange(n)
        while todo.size:
            g = rng.gamma(1.5, size=(todo.size, 3)); g /= g.sum(1, keepdims=True)
            g *= yi[todo, None]
            if W is not None:
                types = np.stack([ti[todo], ti[todo], 1 - ti[todo]], 1)
                ok = ~np.any((types == 1) & (g > W), axis=1)
            else:
                ok = np.ones(todo.size, bool)
            D[todo[ok]] = g[ok]; todo = todo[~ok]
        Ech = D.ravel(); Tch = np.stack([ti, ti, 1 - ti], 1).ravel().astype(np.int8); Hch = np.repeat(hi, 3)
        # phonon branch
        ph = ~ii
        E = np.concatenate([E[ph] - w, Ech]); T = np.concatenate([T[ph], Tch]); H = np.concatenate([H[ph], Hch])
    return cnt

CASES = {  # material: (E_g [eV], omega_0 [eV], W_v [eV] or None, X) -- the V0 runs of predict.py (Si calibration row, Ge and C validation rows)
    "Si": (1.164, 0.063, 12.0, 40.0),
    "Ge": (0.73, 0.037, None, 60.0),
    "C": (5.47, 0.163, None, 25.0),
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    A = json.load(open(os.path.join(here, "data", "results.json")))["variants"]["V0"]["A"]
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
    out = dict(A=A, M=M, cases={}); t0 = time.time()
    for k, (Eg, om, Wv, X) in CASES.items():
        lam = A / Eg ** 3; w = om / Eg; W = None if Wv is None else Wv / Eg
        row = dict(Eg=Eg, om0=om, lam=lam, w=w, W=W, X=X, pts={})
        for i, x0 in enumerate(sorted({10.0, 20.0, X / 2, X})):
            CH = 200000
            c = np.concatenate([cascade_mc(lam, w, x0, min(CH, M - j), W=W, seed=100000 * (1 + list(CASES).index(k)) + 1000 * i + j // CH)
                                for j in range(0, M, CH)])
            m = c.mean(); v = c.var(ddof=1)
            m4 = np.mean((c - m) ** 4)
            row["pts"][str(x0)] = dict(mean=m, se_mean=np.sqrt(v / M), var=v, se_var=np.sqrt(max(m4 - v * v * (M - 3) / (M - 1), 0) / M))
        a, b = row["pts"]["10.0"], row["pts"]["20.0"]
        row["slope_N"] = (b["mean"] - a["mean"]) / 10.0; row["se_slope_N"] = np.hypot(a["se_mean"], b["se_mean"]) / 10.0
        row["slope_V"] = (b["var"] - a["var"]) / 10.0; row["se_slope_V"] = np.hypot(a["se_var"], b["se_var"]) / 10.0
        a, b = row["pts"][str(X / 2)], row["pts"][str(X)]          # the asymptotic window [X/2, X] of predict.py / model.run
        row["asym_slope_N"] = (b["mean"] - a["mean"]) / (X / 2); row["se_asym_slope_N"] = np.hypot(a["se_mean"], b["se_mean"]) / (X / 2)
        row["asym_slope_V"] = (b["var"] - a["var"]) / (X / 2); row["se_asym_slope_V"] = np.hypot(a["se_var"], b["se_var"]) / (X / 2)
        row["eps_MC_eV"] = Eg / row["asym_slope_N"]; row["F_MC"] = row["asym_slope_V"] / row["asym_slope_N"]
        row["se_eps_MC_eV"] = row["eps_MC_eV"] * row["se_asym_slope_N"] / row["asym_slope_N"]
        row["se_F_MC"] = row["F_MC"] * np.hypot(row["se_asym_slope_V"] / row["asym_slope_V"], row["se_asym_slope_N"] / row["asym_slope_N"])
        out["cases"][k] = row; print(k, row["eps_MC_eV"], row["se_eps_MC_eV"], row["F_MC"], row["se_F_MC"], time.time() - t0, flush=True)
    out["runtime_s"] = time.time() - t0
    json.dump(out, open(os.path.join(here, "data", "mc.json"), "w"), indent=1, default=float)
