"""DC-67 convergence record.  (i) every material, V0 (m1): max|dP| at equal x (multiples of 0.25, linear in x on each fine grid) between N and 2N (and 4N if N <= 120) at X = 12.  (ii) Si with the exact commensurate w = 21/388
(no interpolation): N = 388, 776, 1552: eps, F, observed order, continuum by order-p extrapolation, and the A_ph that gives eps = 3.749 eV in the continuum.  data/conv_h.csv, data/si_exact.json."""
import csv, json, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "src_copies")]
import build_library as BL
from cascade import Cascade
M = BL.materials()
A0 = BL.A["V0"]; Eg, om, Wv = 1.164, 0.063, 12.0

def si(A, N, X=40.0):
    c = Cascade(A / Eg ** 3, om / Eg, X=X, h=1.0 / N, a=(.5, .5), W=(None, Wv / Eg), theta=(1., 1.), sets=("N",))
    e, F, b = c.asym(0, 0.5); return e * Eg, F, b

if __name__ == "__main__":
    t0 = time.time(); r = {}
    if os.path.exists(os.path.join(HERE, "data", "si_exact.json")):
        sys.argv.append("skip_si")
    for N in (() if "skip_si" in sys.argv else (388, 776, 1552)):
        r[N] = si(A0, N); print(N, r[N], time.time() - t0, flush=True)
    if "skip_si" not in sys.argv:
        e = [r[N][0] for N in (388, 776, 1552)]; F = [r[N][1] for N in (388, 776, 1552)]
        p_e = np.log2(abs((e[0] - e[1]) / (e[1] - e[2]))); p_F = np.log2(abs((F[0] - F[1]) / (F[1] - F[2])))
        ext = lambda f, p: f[2] + (f[2] - f[1]) / (2 ** p - 1)
        e_inf, F_inf = ext(e, 1.5), ext(F, 1.5)
        # recalibrate: secant in A at N = 776 with the same error offset
        dA = 0.05; e2 = si(A0 + dA, 388); dedA = (e2[0] - e[0]) / dA; dFdA = (e2[1] - F[0]) / dA
        A_inf = A0 + (3.749 - e_inf) / dedA
        out = dict(A0=A0, rows={str(k): v for k, v in r.items()}, p_eps=p_e, p_F=p_F, eps_inf=e_inf, F_inf=F_inf, dedA=dedA, dFdA=dFdA, A_inf=A_inf, F_at_A_inf=F_inf + dFdA * (A_inf - A0), w=om / Eg, w_frac="21/388")
        json.dump(out, open(os.path.join(HERE, "data", "si_exact.json"), "w"), indent=1); print(out, flush=True)
    rows = []
    f = open(os.path.join(HERE, "data", "conv_h.csv"), "w", newline=""); wr = csv.writer(f); wr.writerow(["material", "N", "dP_N_2N", "dP_2N_4N", "p_obs", "t_s"])
    for mat, m in M.items():
        t1 = time.time(); cfg = dict(BL.configs(m))["m1"]; w = m["om"] / m["Eg"]; N = BL.grid(w, nwmin=1)[0]
        X = 12.0
        idx = np.arange(1, 12 * 4 + 1)
        def tab(Nn):
            r_ = BL.solve_cfg(m, cfg, N=Nn, X=X, Nz=32); xs = idx * .25
            return np.stack([np.interp(xs, r_["x"], r_["Pe"][:, n]) for n in range(r_["Pe"].shape[1])], 1)
        P1, P2 = tab(N), tab(2 * N)
        P3 = tab(4 * N) if N <= 120 else None
        d12 = np.abs(P1 - P2).max(); d24 = np.abs(P2 - P3).max() if P3 is not None else float("nan")
        wr.writerow([mat, N, "%.3e" % d12, "%.3e" % d24, "%.3f" % (np.log2(d12 / d24) if P3 is not None else float("nan")), round(time.time() - t1, 1)]); f.flush()
        print(mat, N, d12, d24, time.time() - t1, flush=True)
