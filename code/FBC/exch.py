"""FBC step 2b: exchange term of impact ionization, and a brute-force check of the factorised direct rate of ii.py.

For an initial carrier state on the grid, ordered final configurations (k2, p) are sampled uniformly on the grid and
every band combination is summed with a Gaussian energy delta (SIG). Electron carrier: 1 = (n1,k1), 2 = (v,k2) ->
1' = (n1', k1-p), 2' = (c, k2+p).  Direct: 1->1', 2->2'.  Exchange: 1->2', 2->1' (transfer p_x = k1 - k2 - p).
Hole carrier (v1,k1): active electron a = (v', k1+p) fills the hole, pair (v,k2)->(c,k2+p); exchange a->(c,k2+p),
(v,k2)->(v1,k1) (transfer k2 - k1).
Spin-summed rates (Kane; Kotani-van Schilfgaarde arXiv:0812.2923 Eq. (5) with the identical-particle factor):
  Gamma_full = 2 pi/hbar sum_ord [|M_D|^2 + |M_E|^2 - Re(M_D M_E^*)] delta,   Gamma_D = 4 pi/hbar sum_ord |M_D|^2 delta,
so R_x = Gamma_full/Gamma_D = sum[|M_D|^2 + |M_E|^2 - Re M_D M_E^*] / (2 sum |M_D|^2), with R_x = 1/2 for a contact
interaction (same-spin channel cancels) and R_x = 1 when M_E is negligible.
Output: WORK/exch_<tag>.npz with, per irreducible k and band: sampled Gamma_D (s^-1, to compare with ii.py), R_x
(cap and resta screening) and the number of samples.
Run: python3 exch.py N K   (grid N, K samples per irreducible k; default 12, 1500)
"""
import fbc_common  # first: single-threaded BLAS before numpy loads  # noqa: F401
import os
import sys
import time
import numpy as np
from multiprocessing import Pool
from fbc_common import Grid, PW, gset, grid_bands, make_epm, vscr, OMEGA, HBAR, UNIT, NV, WORK, B

N_GRID = int(sys.argv[1]) if len(sys.argv) > 1 else 12
K = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
VARIANT = os.environ.get("FBC_BANDS", "refit")
NB = int(os.environ.get("FBC_NB", 20))
SHELL = int(os.environ.get("FBC_SHELL", 8))
SIG = float(os.environ.get("FBC_SIG", 0.10))
TAG = os.environ.get("FBC_TAG", f"{VARIANT}_n{N_GRID}_nb{NB}_s{SHELL}_sig{SIG:g}")
_G = {}


def setup():
    si = make_epm(VARIANT)
    bd = grid_bands(N_GRID, NB, VARIANT)
    g = Grid(N_GRID)
    C = np.concatenate([bd["C"], np.zeros((g.N, 1, NB), complex)], axis=1)
    mG, _ = gset(SHELL)
    _G.update(g=g, pw=PW(si), mG=mG, E=bd["E"], C=C, ce=np.arange(NV, NB))


def shortest(red):
    """reduced vector -> (shortest equivalent reduced vector)."""
    best, out = 1e9, None
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                v = red - np.round(red) + np.array([a, b, c])
                d = (v @ B) @ (v @ B)
                if d < best - 1e-12:
                    best, out = d, v
    return out


def rho(iX, iY, Qred, bX, bY):
    """rho[bx, G, by] = <X|e^{i(Q+G).r}|Y> for Q (reduced, any representative) and G in the set; X, Y grid indices."""
    g, pw, mG, C = _G["g"], _G["pw"], _G["mG"], _G["C"]
    base = g.kr[iY] + Qred - g.kr[iX]                           # must be an integer vector
    b0 = np.rint(base).astype(int)
    assert np.allclose(base, b0)
    idx = np.stack([pw.shifted(b0 + m) for m in mG])
    idx = np.where(idx < 0, pw.npw, idx)
    Ys = C[iY][idx][:, :, bY]
    Xc = C[iX][:pw.npw][:, bX].conj().T
    return np.einsum("xg,Ggy->xGy", Xc, Ys, optimize=True)


def wvec(Qred, model):
    q = np.linalg.norm((Qred + _G["mG"]) @ B, axis=1) * UNIT
    w = vscr(np.where(q < 1e-9, 1.0, q), model)
    return np.where(q < 1e-9, 0.0, w)


def gauss(x):
    return np.exp(-x ** 2 / (2 * SIG ** 2)) / (np.sqrt(2 * np.pi) * SIG)


def do_k(r):
    g, E, ce = _G["g"], _G["E"], _G["ce"]
    k1 = g.irr[r]
    rng = np.random.default_rng(1000 + r)
    vb = np.arange(NV)
    ne = len(ce)
    acc = {s: np.zeros((4, ne)) for s in ("cap", "resta")}      # electron: [D, full, n] per n1
    acch = {s: np.zeros((4, NV)) for s in ("cap", "resta")}
    for _ in range(K):
        k2, ip = rng.integers(g.N, size=2)
        p = shortest(g.i[ip] / g.n)
        # ---------------- electron carrier
        k1p = g.index(g.i[k1] - g.i[ip])
        k2p = g.index(g.i[k2] + g.i[ip])
        px = shortest(g.i[k1] / g.n - g.i[k2] / g.n - p)
        r1 = rho(k1p, k1, -p, ce, ce)            # (n1', G, n1)    <n1',k1-p| e^{-i(p+G)r} |n1,k1>  (G -> -G below)
        r2 = rho(k2p, k2, p, ce, vb)             # (c, G, v)       <c,k2+p| e^{i(p+G)r} |v,k2>
        r3 = rho(k2p, k1, -px, ce, ce)           # (c, G, n1)
        r4 = rho(k1p, k2, px, ce, vb)            # (n1', G, v)
        # rho(.., -p, ..) is evaluated at -p + G; pair the terms with the same |p+G|: index G of r2 <-> -G of r1.
        # The G set is inversion symmetric; build the inversion permutation once.
        inv = _G.setdefault("inv", np.array([int(np.where(np.all(_G["mG"] == -m, axis=1))[0][0]) for m in _G["mG"]]))
        r1 = r1[:, inv, :]
        r3 = r3[:, inv, :]
        dEn = (E[k1, ce][None, None, None, :] + E[k2, :NV][None, None, :, None]
               - E[k1p, ce][:, None, None, None] - E[k2p, ce][None, :, None, None])     # (n1', c, v, n1)
        wgt = gauss(dEn)
        for s in ("cap", "resta"):
            wp, wx = wvec(p, s), wvec(px, s)
            MD = np.einsum("aGn,cGv,G->acvn", r1, r2, wp, optimize=True)
            ME = np.einsum("cGn,aGv,G->acvn", r3, r4, wx, optimize=True)
            d = (wgt * np.abs(MD) ** 2).sum((0, 1, 2))
            f = (wgt * (np.abs(MD) ** 2 + np.abs(ME) ** 2 - np.real(MD * ME.conj()))).sum((0, 1, 2))
            acc[s][0] += d
            acc[s][1] += f
            acc[s][2] += d ** 2
            acc[s][3] += f * d
        # ---------------- hole carrier (v1, k1): a = (v', k1+p)
        ka = g.index(g.i[k1] + g.i[ip])
        qx = shortest(g.i[k2] / g.n - g.i[k1] / g.n)
        h1 = rho(k1, ka, -p, vb, vb)             # (v1, G, v')  <v1,k1| e^{-i(p+G)r} |v',k1+p>
        h3 = rho(k2p, ka, qx, ce, vb)            # (c, G, v')   <c,k2+p| e^{i(qx+G)r} |v',k1+p>
        h4 = rho(k1, k2, -qx, vb, vb)            # (v1, G, v)   <v1,k1| e^{-i(qx+G)r} |v,k2>
        h1 = h1[:, inv, :]
        h4 = h4[:, inv, :]
        dEh = (E[ka, :NV][None, None, None, :] + E[k2, :NV][None, None, :, None]
               - E[k1, :NV][:, None, None, None] - E[k2p, ce][None, :, None, None])     # (v1, c, v, v')
        wgh = gauss(dEh)
        for s in ("cap", "resta"):
            wp, wx = wvec(p, s), wvec(qx, s)
            MD = np.einsum("aGb,cGv,G->acvb", h1, r2, wp, optimize=True)
            ME = np.einsum("cGb,aGv,G->acvb", h3, h4, wx, optimize=True)
            d = (wgh * np.abs(MD) ** 2).sum((1, 2, 3))            # per v1
            f = (wgh * (np.abs(MD) ** 2 + np.abs(ME) ** 2 - np.real(MD * ME.conj()))).sum((1, 2, 3))
            acch[s][0] += d
            acch[s][1] += f
            acch[s][2] += d ** 2
            acch[s][3] += f * d
    pref = 4 * np.pi / (HBAR * OMEGA ** 2) / K
    return r, {s: (pref * acc[s][0], acc[s][1] / (2 * np.maximum(acc[s][0], 1e-300)), acc[s]) for s in acc}, \
        {s: (pref * acch[s][0], acch[s][1] / (2 * np.maximum(acch[s][0], 1e-300)), acch[s]) for s in acch}


def main():
    t0 = time.time()
    setup()
    g = _G["g"]
    rs = [int(x) for x in os.environ["FBC_KLIST"].split(",")] if os.environ.get("FBC_KLIST") else list(range(len(g.irr)))
    ne = NB - NV
    out = {f"{c}_{q}_{s}": np.full((len(g.irr), ne if c == "e" else NV), np.nan)
           for c in ("e", "h") for q in ("GD", "Rx") for s in ("cap", "resta")}
    raw = {f"{c}_raw_{s}": np.zeros((len(g.irr), 4, ne if c == "e" else NV)) for c in ("e", "h") for s in ("cap", "resta")}
    with Pool(int(os.environ.get("FBC_NPROC", 4)), initializer=setup) as pool:
        for r, de, dh in pool.imap_unordered(do_k, rs):
            for s in ("cap", "resta"):
                out[f"e_GD_{s}"][r], out[f"e_Rx_{s}"][r], raw[f"e_raw_{s}"][r] = de[s]
                out[f"h_GD_{s}"][r], out[f"h_Rx_{s}"][r], raw[f"h_raw_{s}"][r] = dh[s]
            print(f"k {r} done {time.time() - t0:.0f} s", flush=True)
    np.savez(os.path.join(WORK, f"exch_{TAG}_K{K}.npz"), K=K, klist=np.array(rs), **out, **raw)
    print(f"total {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
