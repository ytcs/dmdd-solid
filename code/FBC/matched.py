"""Energy-only (book) cascade recalibrated to the full-band pair energy: A_AB such that the book model's one-sided
eps_eh equals the full-band value (full-band slope 50-100 eV; book-model slope 20-40 E_g), then the distance of
the full-band P(N|omega) from the recalibrated energy-only cascade (book DM seed and the full-band computed split),
from Ramanathan-Kurinsky alpha = 1 / inf and from the step model with the full-band eps.  Writes data/matched.json.
Run: python3 matched.py
"""
import fbc_common  # noqa: F401
import os
import sys
import json
import numpy as np
from scipy.optimize import brentq
from fbc_common import DATA, WORK, EG, HERE

sys.path.insert(0, os.path.join(HERE, "..", "..", "book", "figscripts", "ch18"))
import casc18_3 as bk   # noqa: E402


def eps_of(A):
    bk.AAB = A
    c = bk.Casc(X=46.0)
    # slope between 20 and 40 E_g (the book's window; at 100 eV the NZ = 32 root-of-unity extraction aliases)
    m = [(c.pair(o - EG, 0.0) * np.arange(bk.NZ)).sum() for o in (20 * EG, 40 * EG)]
    return 20 * EG / (m[1] - m[0]), c


def tv(P, Q):
    m = max(len(P), len(Q))
    return 0.5 * np.abs(np.pad(P, (0, m - len(P))) - np.pad(Q, (0, m - len(Q)))).sum()


def main():
    S = json.load(open(os.path.join(DATA, "summary.json")))
    target = S["he"]["eps"]
    e0, _ = eps_of(5.6737)
    A = brentq(lambda a: eps_of(a)[0] - target, 5.0, 30.0, xtol=1e-3)
    eA, c = eps_of(A)
    bk.AAB = A
    c = bk.Casc()
    oms = np.array(S["omegas"])
    sd = json.load(open(os.path.join(HERE, "..", "..", "book", "figscripts", "ch18", "seeds18_3.json")))
    exc = np.array(sd["exc"])
    Sd = np.load(os.path.join(WORK, "seeds_refit_n12_m100_q4.npz"))
    H = Sd["H_heavy"]
    Ph = np.array(S["P_heavy"])
    res = {k: [] for k in ("bookDM", "split", "rk1", "rkinf", "step")}
    Pm = {k: [] for k in res}
    for i, o in enumerate(oms):
        ex = o - EG
        jj = min(max(int(np.searchsorted(exc, ex)) - 1, 0), len(exc) - 2)
        f = np.clip((ex - exc[jj]) / (exc[jj + 1] - exc[jj]), 0, 1)
        h = (1 - f) * np.array(sd["hist"]["DM"][jj]) + f * np.array(sd["hist"]["DM"][jj + 1])
        P = {"bookDM": c.pair(*bk.share_seed(h, ex)), "rk1": c.pair(*bk.beta_seed(1.0, ex)),
             "rkinf": c.pair(*bk.beta_seed(np.inf, ex))}
        j = int(round(o / 0.05))
        row = H[j - 2:j + 3].sum(0)
        Ee = (np.arange(len(row)) + 0.5) * 0.05
        ok = (Ee < ex) & (row > 0)
        P["split"] = c.pair(Ee[ok], ex - Ee[ok], row[ok])
        st = np.zeros(16)
        st[1 + int(np.floor(ex / target))] = 1
        P["step"] = st
        for k in res:
            res[k].append(float(tv(Ph[i], P[k])))
            Pm[k].append(float(1 - P[k][0] - P[k][1]))
    win = (oms >= 4.4) & (oms <= 21)
    out = dict(A_matched=A, eps_matched=eA, eps_book_A5674=e0, target=target,
               maxtv={k: float(np.array(v)[win].max()) for k, v in res.items()},
               at={k: float(oms[win][np.argmax(np.array(v)[win])]) for k, v in res.items()},
               tv=res, Pge2=Pm,
               rep={f"{o}": {k: res[k][int(np.argmin(np.abs(oms - o)))] for k in res} for o in (5, 6, 8, 10, 12, 15, 20)})
    json.dump(out, open(os.path.join(DATA, "matched.json"), "w"), indent=0)
    print(f"A_AB matched = {A:.3f} eV^3 (eps {eA:.4f} vs target {target:.4f}; book A = 5.674 gives {e0:.4f} by this slope)")
    print("max TV (4.4-21 eV):", out["maxtv"], out["at"])
    print("rep:", json.dumps(out["rep"]))
    i5 = int(np.argmin(np.abs(oms - 5)))
    print("P(>=2) at 5 eV: full", S["Pge2"]["heavy"][i5], {k: Pm[k][i5] for k in Pm})


if __name__ == "__main__":
    main()
