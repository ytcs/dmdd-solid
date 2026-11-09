"""FBC step 2: direct impact-ionization rates W_ii(n,k) for electrons and holes on the full band structure.

Golden rule with a screened Coulomb interaction, crystal momentum conserved on the grid with Umklapp:
  Gamma_D(n1 k1) = (4 pi / hbar Omega^2) (1/N) sum_p sum_n1' sum_GG' A_G A*_G' S_GG'(p, omega),
  A_G = w(|p+G|, omega) rho_XY(k_Y, -(p+G))      (carrier vertex),
  S_GG'(p, omega) = (1/N) sum_{k2 v c} P_G P*_G' delta(omega - e_c(k2+p) + e_v(k2)),  P_G = rho_cv(k2, p+G).
This is the spin-summed direct term (factor 2 = pair spin; equal to the GW out-scattering rate with the model W at
first order, book eq:18.1-ii). The exchange term is added in exch.py as a factor R_x.
Electron carrier (n1,k1) -> (n1', k1-p): X = (n1', k1-p), Y = (n1, k1).  Hole carrier (v1,k1) -> (v', k1+p): the
active valence electron goes from Y = (v', k1+p) into X = (v1, k1).  The created pair carries momentum +p.
Symmetry: S is computed for irreducible p only and rotated, S(Rp; RG_a, RG_b) = e^{i(RG_a - RG_b).t} S(p; G_a, G_b)
for the space-group op {R|t} (checked against a direct evaluation in checks.py).
Screening: static Cappellini 'cap' (primary), static Resta 'resta', and the diagonal RPA of the same bands
('rpa0' static, 'rpaw' at the transferred omega): Im eps = (2 pi v(q)/Omega) S_GG, Re eps by Kramers-Kronig with
the f-sum remainder placed at EMAX + 5 eV.  Delta function: linear binning (DBIN) then a Gaussian (SIG).
Outputs (WORK): ii_<tag>.npz: tot_e[v, r, n1], tot_h[v, r, v1] (s^-1), tab_e[r, n1, p, n1'], tab_h[r, v1, p, v']
(primary screening, float32, for final-state sampling), pair tables pw/pde for irreducible p, eps diagnostics.
Run: python3 ii.py N   (env FBC_BANDS=refit|scissor, FBC_NB, FBC_SHELL, FBC_SIG, FBC_NPROC)
"""
import fbc_common  # first: single-threaded BLAS before numpy loads  # noqa: F401
import os
import sys
import time
import numpy as np
import multiprocessing as mp
from scipy.ndimage import convolve1d
from fbc_common import (Grid, PW, gset, grid_bands, make_epm, vscr, nonsymm_t, oh_ops, E2, OMEGA, HBAR, UNIT, EG,
                        NV, WORK, B, json_load, DATA)

N_GRID = int(sys.argv[1]) if len(sys.argv) > 1 else 12
VARIANT = os.environ.get("FBC_BANDS", "refit")
NB = int(os.environ.get("FBC_NB", 20))
SHELL = int(os.environ.get("FBC_SHELL", 8))
SIG = float(os.environ.get("FBC_SIG", 0.10))
DBIN = 0.05
EMAX = EG + 20.6
NBIN = int(EMAX / DBIN) + 3
SCR = ("cap", "resta", "rpa0", "rpaw")
TAG = os.environ.get("FBC_TAG", f"{VARIANT}_n{N_GRID}_nb{NB}_s{SHELL}_sig{SIG:g}")
_G = {}


def setup():
    if _G:
        return
    si = make_epm(VARIANT)
    bd = grid_bands(N_GRID, NB, VARIANT)
    g = Grid(N_GRID)
    pw = PW(si)
    mG, Gc = gset(SHELL)
    E = bd["E"]
    C = np.concatenate([bd["C"], np.zeros((g.N, 1, NB), complex)], axis=1)
    ce = np.arange(NV, NB)
    nk = int(np.ceil(4 * SIG / DBIN))
    xk = np.arange(-nk, nk + 1) * DBIN
    ker = np.exp(-xk ** 2 / (2 * SIG ** 2))
    ker /= ker.sum()
    om = np.arange(NBIN) * DBIN
    wp2 = 4 * np.pi * (8 / OMEGA) * E2 * 2 * 3.80998212
    VS = None
    if VARIANT == "refit":
        VS = {int(k): v for k, v in json_load(os.path.join(DATA, "refit_formfactors.json"))["VS"].items()}
    ts = nonsymm_t(VS)
    ops = oh_ops()
    # G-set permutation for each op: perm_G[o, a] = index of R^-1 G_a
    key = {tuple(m): i for i, m in enumerate(mG)}
    Binv = np.linalg.inv(B)
    permG = np.zeros((48, len(mG)), int)
    for o, R in enumerate(ops):
        for a in range(len(mG)):
            Gp = R.T @ Gc[a]
            permG[o, a] = key[tuple(np.rint(Gp @ Binv).astype(int))]
    phaseG = np.exp(2j * np.pi * (Gc @ ts.T)).T            # (48, NG): e^{i 2pi G_a . t_o}
    _G.update(si=si, g=g, pw=pw, mG=mG, Gc=Gc, E=E, C=C, ce=ce, ker=ker, om=om, wp2=wp2, ops=ops, ts=ts,
              permG=permG, phaseG=phaseG, Binv=Binv,
              Cv=np.ascontiguousarray(C[:, :, :NV]),
              CcH=np.ascontiguousarray(C[:, :pw.npw, NV:].conj().transpose(0, 2, 1)), shcache={})


def shifted(s):
    k = tuple(s)
    d = _G["shcache"]
    if k not in d:
        pw = _G["pw"]
        ix = pw.shifted(np.asarray(s))
        d[k] = np.where(ix < 0, pw.npw, ix)
    return d[k]


def rep_shift(jp):
    g = _G["g"]
    best, bm = 1e9, None
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                m0 = np.array([a, b, c])
                v = (jp / g.n + m0) @ B
                d = v @ v
                if d < best - 1e-12:
                    best, bm = d, m0
    return bm


def kk_re(eps2, om):
    d = om[1] - om[0]
    w = om + 0.5 * d
    K = om[None, :] / (om[None, :] ** 2 - w[:, None] ** 2)
    re_mid = (2 / np.pi) * d * eps2 @ K.T
    return np.concatenate([re_mid[..., :1], 0.5 * (re_mid[..., 1:] + re_mid[..., :-1])], axis=-1)


def pair_block(jp, m0):
    """P[k2, c, G, v] = rho_cv(k2, p+G), p = jp/n + m0 (reduced); pair energies dE[k2, c, v]."""
    g, mG, E, ce, Cv, CcH = _G["g"], _G["mG"], _G["E"], _G["ce"], _G["Cv"], _G["CcH"]
    npw = _G["pw"].npw
    iq, _ = g.fold(g.i + jp)
    Gf = np.rint(g.kr + jp / g.n - g.kr[iq]).astype(int)          # k2 + p = k_q + Gf (shortest reps)
    NG = len(mG)
    P = np.zeros((g.N, len(ce), NG, NV), complex)
    for gf in np.unique(Gf, axis=0):
        sel = np.where(np.all(Gf == gf, axis=1))[0]
        idx = np.stack([shifted(gf + m0 + m) for m in mG], axis=1)       # (npw, NG): index of g' - shift
        Vs = Cv[sel][:, idx, :].reshape(len(sel), npw, NG * NV)
        P[sel] = (CcH[iq[sel]] @ Vs).reshape(len(sel), len(ce), NG, NV)
    dE = E[iq][:, ce][:, :, None] - E[:, :NV][:, None, :]
    return P, dE, iq


def bin_S(P, dE):
    g, ker = _G["g"], _G["ker"]
    NG = P.shape[2]
    Pf = P.transpose(0, 1, 3, 2).reshape(-1, NG)
    x = dE.reshape(-1) / DBIN
    ok = x < NBIN - 2
    Pf, x = Pf[ok], x[ok]
    lo = np.floor(x).astype(int)
    f = x - lo
    S = np.zeros((NBIN, NG, NG), complex)
    for part, wgt in ((lo, 1 - f), (lo + 1, f)):
        order = np.argsort(part, kind="stable")
        bins = part[order]
        Pw = Pf[order] * np.sqrt(wgt[order])[:, None]
        cuts = np.flatnonzero(np.diff(bins)) + 1
        starts = np.concatenate([[0], cuts])
        ends = np.concatenate([cuts, [len(bins)]])
        for s0, e0 in zip(starts, ends):
            X = Pw[s0:e0]
            S[bins[s0]] += X.T @ X.conj()
    S /= g.N * DBIN
    return convolve1d(S.real, ker, axis=0, mode="constant") + 1j * convolve1d(S.imag, ker, axis=0, mode="constant")


def do_irr_p(j):
    """phase A: S and pair table for irreducible p number j."""
    g = _G["g"]
    ip = g.irr[j]
    jp = g.i[ip]
    m0 = rep_shift(jp)
    P, dE, iq = pair_block(jp, m0)
    S = bin_S(P, dE)
    qA = np.linalg.norm((jp / g.n + m0 + _G["mG"]) @ B, axis=1) * UNIT
    wc = np.where(qA < 1e-9, 0.0, vscr(np.where(qA < 1e-9, 1.0, qA), "cap"))
    pwt = np.einsum("kcgv,g->kcv", np.abs(P) ** 2, wc ** 2).astype(np.float32)
    return j, m0, S.astype(np.complex64), pwt, dE.astype(np.float32)


def screening(qA, S):
    om, wp2 = _G["om"], _G["wp2"]
    vC = 4 * np.pi * E2 / qA ** 2
    out = {}
    for v in ("cap", "resta"):
        out[v] = np.broadcast_to(vscr(qA, v)[None, :], (NBIN, len(qA)))
    eps2 = (2 * np.pi * vC[:, None] / OMEGA) * np.real(np.einsum("wgg->gw", S))
    re = 1 + kk_re(eps2, om)
    wt = EMAX + 5.0
    miss = np.maximum(0.5 * np.pi * wp2 - DBIN * (eps2 * om[None, :]).sum(1), 0)
    re = re + (2 / np.pi) * miss[:, None] / (wt ** 2 - om[None, :] ** 2)
    out["rpa0"] = np.broadcast_to((vC / re[:, 0])[None, :], (NBIN, len(qA)))
    out["rpaw"] = (vC[:, None] / (re + 1j * eps2)).T
    out["_eps0"] = re[:, 0]
    out["_fsum"] = DBIN * (eps2 * om[None, :]).sum(1) / (0.5 * np.pi * wp2)
    return out


def full_S(ip):
    """S, base vector m0 (reduced) for any grid p by rotation of the irreducible one."""
    g = _G["g"]
    j = g.irr_of[ip]
    o = g.op_from_irr[ip]
    R = _G["ops"][o]
    base_r = g.i[g.irr[j]] / g.n + _G["m0_irr"][j]
    base = (R @ (base_r @ B)) @ _G["Binv"]
    m0 = np.rint(base - g.i[ip] / g.n).astype(int)
    assert np.allclose(base - g.i[ip] / g.n, m0)
    pa = _G["permG"][o]
    ph = _G["phaseG"][o]
    Sr = _G["S_irr"][j].astype(complex)
    S = Sr[:, pa][:, :, pa] * (ph[:, None] * ph.conj()[None, :])[None]
    return S, m0


def vertex(kX, kY, GU_list, bX, bY):
    """rho[G, bx, by] = <X| e^{iQ.r} |Y>, k_Y + Q = k_X + G_U (one G_U per G)."""
    C = _G["C"]
    npw = _G["pw"].npw
    idx = np.stack([shifted(gu) for gu in GU_list])          # (NG, npw)
    Ys = C[kY][idx][:, :, bY]                               # (NG, npw, nby)
    Xc = C[kX][:npw][:, bX].conj().T                        # (nbx, npw)
    return np.matmul(Xc[None], Ys)                          # (NG, nbx, nby)


def interp_S(S, om_t):
    x = om_t / DBIN
    lo = np.clip(np.floor(x).astype(int), 0, NBIN - 2)
    f = np.clip(x - lo, 0, 1)[:, None, None]
    return S[lo] * (1 - f) + S[lo + 1] * f


def wfun(scr, v, om_t):
    x = np.clip(om_t / DBIN, 0, NBIN - 1.001)
    lo = np.floor(x).astype(int)
    f = (x - lo)[:, None]
    W = scr[v]
    return W[lo] * (1 - f) + W[lo + 1] * f


def quad(A, Si):
    return np.real(np.matmul(np.matmul(A[:, None, :], Si), A.conj()[:, :, None]))[:, 0, 0]


def do_p(ip):
    g, mG, E, ce = _G["g"], _G["mG"], _G["E"], _G["ce"]
    jp = g.i[ip]
    S, m0 = full_S(ip)
    qA = np.linalg.norm((jp / g.n + m0 + mG) @ B, axis=1) * UNIT
    zero = qA < 1e-9
    scr = screening(np.where(zero, 1.0, qA), S)
    nr, ne = len(g.irr), len(ce)
    tot_e = np.zeros((len(SCR), nr, ne))
    tot_h = np.zeros((len(SCR), nr, NV))
    tab_e = np.zeros((nr, ne, ne), np.float32)
    tab_h = np.zeros((nr, NV, NV), np.float32)
    pref = 4 * np.pi / (HBAR * OMEGA ** 2)
    lo_om = EG - 5 * SIG
    for r, k1 in enumerate(g.irr):
        for kind in ("e", "h"):
            if kind == "e":
                kX, _ = g.fold(g.i[k1] - jp)
                Gf = g.umk(k1, -jp / g.n, kX)
                rho = vertex(kX, k1, [Gf - m0 - m for m in mG], ce, ce)          # (G, n1', n1)
                om = E[k1, ce][None, :] - E[kX, ce][:, None]                   # (n1', n1)
            else:
                kY, _ = g.fold(g.i[k1] + jp)
                Gf = g.umk(kY, -jp / g.n, k1)
                rho = vertex(k1, kY, [Gf - m0 - m for m in mG], np.arange(NV), np.arange(NV))   # (G, v1, v')
                om = E[kY, :NV][None, :] - E[k1, :NV][:, None]                  # (v1, v')
            sel = np.flatnonzero((om.ravel() > lo_om) & (om.ravel() < EMAX))
            if len(sel) == 0:
                continue
            om_t = om.ravel()[sel]
            Rt = rho.reshape(len(mG), -1)[:, sel].T                            # (T, G)
            Si = interp_S(S, om_t)
            for iv, v in enumerate(SCR):
                A = Rt * wfun(scr, v, om_t)
                A[:, zero] = 0
                val = np.zeros(om.size)
                val[sel] = pref * quad(A, Si)
                val = val.reshape(om.shape)
                if kind == "e":
                    tot_e[iv, r] = val.sum(0)
                    if iv == 0:
                        tab_e[r] = val.T
                else:
                    tot_h[iv, r] = val.sum(1)
                    if iv == 0:
                        tab_h[r] = val
    return ip, tot_e, tot_h, tab_e, tab_h, (qA, scr["_eps0"], scr["_fsum"])


def phase_A():
    g = _G["g"]
    nI = len(g.irr)
    path = os.path.join(WORK, f"Sirr_{TAG}.npz")
    if os.path.exists(path):
        d = np.load(path)
        return d["S"], d["m0"], d["pw"], d["pde"]
    S = np.zeros((nI, NBIN, len(_G["mG"]), len(_G["mG"])), np.complex64)
    m0 = np.zeros((nI, 3), int)
    pw_t = np.zeros((nI, g.N, len(_G["ce"]), NV), np.float32)
    pde_t = np.zeros_like(pw_t)
    with mp.get_context("fork").Pool(int(os.environ.get("FBC_NPROC", 4))) as pool:
        for j, m, s, pw_, de in pool.imap_unordered(do_irr_p, range(nI)):
            S[j], m0[j], pw_t[j], pde_t[j] = s, m, pw_, de
    np.savez(path, S=S, m0=m0, pw=pw_t, pde=pde_t)
    return S, m0, pw_t, pde_t


def main():
    t0 = time.time()
    setup()
    g, ce = _G["g"], _G["ce"]
    S_irr, m0_irr, pw_t, pde_t = phase_A()
    _G["S_irr"], _G["m0_irr"] = S_irr, m0_irr
    print(f"phase A (irreducible S, {len(g.irr)} p) {time.time() - t0:.0f} s", flush=True)
    nr, ne = len(g.irr), len(ce)
    tot_e = np.zeros((len(SCR), nr, ne))
    tot_h = np.zeros((len(SCR), nr, NV))
    tab_e = np.zeros((nr, ne, g.N, ne), np.float32)
    tab_h = np.zeros((nr, NV, g.N, NV), np.float32)
    eps0 = np.zeros((g.N, len(_G["mG"])))
    fsum = np.zeros((g.N, len(_G["mG"])))
    qAll = np.zeros((g.N, len(_G["mG"])))
    with mp.get_context("fork").Pool(int(os.environ.get("FBC_NPROC", 4))) as pool:
        for cnt, (ip, te, th, tbe, tbh, eq) in enumerate(pool.imap_unordered(do_p, range(g.N), chunksize=8)):
            tot_e += te / g.N
            tot_h += th / g.N
            tab_e[:, :, ip, :] = tbe / g.N
            tab_h[:, :, ip, :] = tbh / g.N
            qAll[ip], eps0[ip], fsum[ip] = eq
            if cnt % 200 == 0:
                print(f"{cnt}/{g.N} p, {time.time() - t0:.0f} s", flush=True)
    np.savez(os.path.join(WORK, f"ii_{TAG}.npz"), tot_e=tot_e, tot_h=tot_h, tab_e=tab_e, tab_h=tab_h,
             pw=pw_t, pde=pde_t, irr=g.irr, ce=ce, E=_G["E"], scr=np.array(SCR), n=g.n,
             qA=qAll, eps0=eps0, fsum=fsum)
    print(f"total {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
