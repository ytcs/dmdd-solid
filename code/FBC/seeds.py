"""FBC step 4: seeds. Final-state-resolved electron/hole distributions of
  DM : a dark-matter-electron transition at deposit omega, independent-particle pair weights of the density,
       |rho_cv(k2, q)|^2 delta(omega - e_c(k2+q) + e_v(k2)), q unreduced, q-averaged over the SHM halo with the rate
       weight q F_DM(q)^2 eta(v_min(q, omega)) (CONVENTIONS sec. 8, isotropic S), heavy (F = 1) and light
       (F = (alpha m_e/q)^2) mediator, m_chi = 100 MeV (FBC_MCHI);  also the book's single q0 = alpha m_e [100] seed;
  photon : q -> 0, vertical pairs weighted |r_cv|^2 = |p_cv|^2/(e_c - e_v)_model^2, polarisation-averaged.
Unscreened (as seeds18_3.py); the book's seed machinery (vertex, folding, Gaussian delta SIG = 0.1 eV) is reused with
the FBC bands (12^3 grid labels, so that every seed carrier has a crystal momentum and band for the cascade).
The q integral is sampled: radial bins of 0.15 (2pi/a) from QLO to QCUT, NQB random grid vectors q = p + G per bin
(uniform in q space), each with the full k2 sum.  Wave functions for the vertex use a larger plane-wave cutoff
(ECUT_SEED, |G|^2 <= 36 (2pi/a)^2) so that rho(q) is not truncated for |q| <= QCUT.
Outputs WORK/seeds_<tag>.npz: share histograms H[seed][omega_bin, E_e_bin] and labelled seed samples per target
omega: (k_e, b_e, k_h, b_h, E_e, E_h) with E_e + E_h = omega - E_g exactly (rescaled from grid energies).
Run: python3 seeds.py
"""
import fbc_common  # first: single-threaded BLAS before numpy loads  # noqa: F401
import os
import sys
import time
import numpy as np
import multiprocessing as mp
from fbc_common import (Grid, PW, grid_bands, EPM, MATERIALS, A_LAT, UNIT, EG, NV, WORK, B, DATA, json_load,
                        ALPHA, ME, model_edges)

VARIANT = os.environ.get("FBC_BANDS", "refit")
N_GRID = int(os.environ.get("FBC_N", 12))
NB = 20
ECUT_SEED = 36.0
SIG = 0.10
DBIN = 0.05
QLO, QCUT, DQ = 0.25, float(os.environ.get("FBC_QCUT", 4.0)), 0.15
NQB = int(os.environ.get("FBC_NQB", 60))
MCHI = float(os.environ.get("FBC_MCHI", 100e6))      # eV
NSEED = int(os.environ.get("FBC_NSEED", 20000))
OMEGAS = np.round(np.arange(2.0, 20.0 + 1e-9, 0.25), 3)
TAG = os.environ.get("FBC_TAG", f"{VARIANT}_n{N_GRID}_m{MCHI/1e6:g}_q{QCUT:g}")
KMS = 1 / 299792.458                                   # km/s in units of c
V0, VESC, VE = 238 * KMS, 544 * KMS, 250.5 * KMS
NBIN = int(22.0 / DBIN)
_G = {}


def eta(vmin):
    """SHM eta(v_min) (units 1/c), CONVENTIONS sec. 8 reference frame v_E = 250.5 km/s."""
    from scipy.special import erf
    x, y, z = vmin / V0, VE / V0, VESC / V0
    Nesc = erf(z) - 2 * z * np.exp(-z ** 2) / np.sqrt(np.pi)
    pre = 1 / (2 * Nesc * y * V0)
    a = erf(x + y) - erf(x - y) - 4 / np.sqrt(np.pi) * y * np.exp(-z ** 2)
    b = erf(z) - erf(x - y) - 2 / np.sqrt(np.pi) * (z + y - x) * np.exp(-z ** 2)
    return np.where(x < z - y, pre * a, np.where(x < z + y, pre * b, 0.0))


def setup():
    if _G:
        return
    if VARIANT == "refit":
        vs = {int(k): v for k, v in json_load(os.path.join(DATA, "refit_formfactors.json"))["VS"].items()}
        MATERIALS["Si_fit"] = dict(a=A_LAT, VS=vs, VA={})
        si = EPM("Si_fit", ecut=ECUT_SEED)
    else:
        si = EPM("Si", ecut=ECUT_SEED)
    bd = grid_bands(N_GRID, NB, VARIANT)                    # energies and labels of the cascade tables
    g = Grid(N_GRID)
    C = np.zeros((g.N, len(si.G) + 1, NB), complex)
    for c0 in range(0, g.N, 64):
        w, v = np.linalg.eigh(si.hamiltonian(g.k[c0:c0 + 64]))
        C[c0:c0 + 64, :-1] = v[:, :, :NB]
    evbm, ecbm, _ = model_edges(si)
    Eraw = bd["Eraw"]
    _G.update(si=si, g=g, pw=PW(si), C=C, E=bd["E"], Eraw=Eraw, ecb=float(bd["ecbm"]))


def rho_q(jp, m):
    """rho_cv(k2, q) for all k2, q = jp/n + m (reduced): returns (N, nc, NV), folded indices iq."""
    g, pw, C = _G["g"], _G["pw"], _G["C"]
    iq, _ = g.fold(g.i + jp)
    Gf = np.rint(g.kr + jp / g.n - g.kr[iq]).astype(int)
    out = np.zeros((g.N, NB - NV, NV), complex)
    for gf in np.unique(Gf, axis=0):
        sel = np.where(np.all(Gf == gf, axis=1))[0]
        ix = pw.shifted(gf + m)
        ix = np.where(ix < 0, pw.npw, ix)
        Vs = C[sel][:, ix, :NV]
        Cc = C[iq[sel]][:, :pw.npw, NV:].conj().transpose(0, 2, 1)
        out[sel] = Cc @ Vs
    return out, iq


def qlist(rng):
    """sampled q vectors per radial bin: list of (jp, m, |q| in 2pi/a, bin index, n in bin)."""
    g = _G["g"]
    r = range(-6, 7)
    mm = np.array([(a, b, c) for a in r for b in r for c in r])
    edges = np.arange(QLO, QCUT + 1e-9, DQ)
    out = []
    allq = []
    for ip in range(g.N):
        red = g.i[ip] / g.n + mm
        q = np.linalg.norm(red @ B, axis=1)
        sel = (q >= edges[0]) & (q < edges[-1])
        for m, qq in zip(mm[sel], q[sel]):
            allq.append((ip, tuple(m), qq))
    qs = np.array([a[2] for a in allq])
    for b in range(len(edges) - 1):
        idx = np.where((qs >= edges[b]) & (qs < edges[b + 1]))[0]
        pick = rng.choice(idx, min(NQB, len(idx)), replace=False)
        for i in pick:
            out.append((allq[i][0], np.array(allq[i][1]), allq[i][2], b, len(pick)))
    return out, edges


def records(item):
    g, E = _G["g"], _G["E"]
    ip, m, q, b, nb = item
    rho, iq = rho_q(g.i[ip], m)
    w = np.abs(rho) ** 2                                        # (k2, c, v)
    dE = E[iq][:, NV:][:, :, None] - E[:, :NV][:, None, :]
    Ee = (E[iq][:, NV:] - _G["ecb"])[:, :, None] + 0 * dE
    return w, dE, Ee, iq


def qweights(q, dE, edges, b, nb):
    """rate weight per record: Delta q / n_b * q F^2 eta(v_min(q, dE)), heavy and light; q in 2pi/a units."""
    qe = q * UNIT * 1973.269804          # eV
    vmin = dE / qe + qe / (2 * MCHI)
    base = DQ / nb * q * eta(vmin)
    q0 = ALPHA * ME
    return {"heavy": base, "light": base * (q0 / qe) ** 4}


def stage1(item):
    ip, m, q, b, nb = item
    w, dE, Ee, iq = records(item)
    qw = qweights(q, dE, None, b, nb)
    H, spec = {}, {}
    xb = np.clip((dE / DBIN).astype(int), 0, NBIN - 1).ravel()
    eb = np.clip((Ee / DBIN).astype(int), 0, NBIN - 1).ravel()
    for s in ("heavy", "light"):
        ww = (w * qw[s]).ravel()
        H[s] = np.bincount(xb * NBIN + eb, weights=ww, minlength=NBIN * NBIN).reshape(NBIN, NBIN).astype(np.float32)
        spec[s] = np.bincount(xb, weights=ww, minlength=NBIN)
    return H, spec


def sample_records(w, dE, Ee, iq, omega, nsamp, rng):
    """draw nsamp records with prob ~ w * gauss(omega - dE); returns labels and energies (rescaled)."""
    g = _G["g"]
    p = (w * np.exp(-(omega - dE) ** 2 / (2 * SIG ** 2))).ravel()
    p /= p.sum()
    pick = rng.choice(p.size, nsamp, p=p)
    k2, c, v = np.unravel_index(pick, w.shape)
    Eh = -_G["E"][k2, v]
    Eev = Ee[k2, c, v]
    tot = np.maximum(Eev + Eh, 1e-9)
    f = (omega - EG) / tot
    return np.stack([iq[k2], c, k2, v]).T, np.stack([Eev * f, Eh * f]).T


def photon_records():
    g, si, C, E, Eraw = _G["g"], _G["si"], _G["C"], _G["E"], _G["Eraw"]
    kG = (g.k[:, None, :] + si.G[None]) * UNIT * 1973.269804          # eV (momentum), (N, npw, 3)
    Cc = C[:, :-1, NV:]
    Cv = C[:, :-1, :NV]
    p2 = np.zeros((g.N, NB - NV, NV))
    for a in range(3):
        pa = np.einsum("kgc,kg,kgv->kcv", Cc.conj(), kG[:, :, a], Cv, optimize=True)
        p2 += np.abs(pa) ** 2 / 3
    dEr = Eraw[:, NV:][:, :, None] - Eraw[:, :NV][:, None, :]
    w = p2 / dEr ** 2
    dE = E[:, NV:][:, :, None] - E[:, :NV][:, None, :]
    Ee = (E[:, NV:] - _G["ecb"])[:, :, None] + 0 * dE
    return w, dE, Ee, np.arange(g.N)


def q0_records():
    """book seed: q0 = alpha m_e along [100]."""
    g = _G["g"]
    q0 = ALPHA * ME / (UNIT * 1973.269804)
    red = np.array([q0, 0, 0]) @ np.linalg.inv(B)
    # nearest grid vector + G to q0 xhat (grid resolution 1/n): use exact q0 via the nearest grid p
    jp = np.rint(red * g.n)
    m = np.floor(jp / g.n).astype(int)
    jp = (jp - m * g.n).astype(int)
    w, iq = rho_q(jp, m)
    E = _G["E"]
    dE = E[iq][:, NV:][:, :, None] - E[:, :NV][:, None, :]
    Ee = (E[iq][:, NV:] - _G["ecb"])[:, :, None] + 0 * dE
    qgrid = np.linalg.norm((jp / g.n + m) @ B)
    return np.abs(w) ** 2, dE, Ee, iq, qgrid, q0


def hist_from(w, dE, Ee):
    xb = np.clip((dE / DBIN).astype(int), 0, NBIN - 1).ravel()
    eb = np.clip((Ee / DBIN).astype(int), 0, NBIN - 1).ravel()
    return np.bincount(xb * NBIN + eb, weights=w.ravel(), minlength=NBIN * NBIN).reshape(NBIN, NBIN)


def main():
    t0 = time.time()
    setup()
    rng = np.random.default_rng(7)
    items, edges = qlist(rng)
    print(f"{len(items)} q samples, {time.time() - t0:.0f} s", flush=True)
    H = {s: np.zeros((NBIN, NBIN)) for s in ("heavy", "light")}
    spec = {s: np.zeros((len(items), NBIN)) for s in ("heavy", "light")}
    with mp.get_context("fork").Pool(int(os.environ.get("FBC_NPROC", 4))) as pool:
        for i, (h, sp) in enumerate(pool.imap(stage1, items, chunksize=4)):
            for s in H:
                H[s] += h[s]
                spec[s][i] = sp[s]
    print(f"stage 1 {time.time() - t0:.0f} s", flush=True)
    # photon and q0 seeds (single record sets)
    wph, dEph, Eeph, iqph = photon_records()
    Hph = hist_from(wph, dEph, Eeph)
    w0, dE0, Ee0, iq0, qg, q0 = q0_records()
    H0 = hist_from(w0, dE0, Ee0)
    if os.environ.get("FBC_STAGE1ONLY"):     # v2: share histograms only (matched-grid photon vs DM comparison)
        np.savez(os.path.join(WORK, f"seedsH_{TAG}.npz"), H_heavy=H["heavy"], H_light=H["light"], H_photon=Hph,
                 H_q0=H0, dbin=DBIN, nq=len(items))
        print(f"stage-1 histograms saved {time.time() - t0:.0f} s", flush=True)
        return
    # stage 2: labelled samples. counts per q sample for each omega from the smoothed spectra
    from scipy.ndimage import gaussian_filter1d
    out = {}
    plan = {}
    for s in ("heavy", "light"):
        sm = gaussian_filter1d(spec[s], SIG / DBIN, axis=1)
        for o in OMEGAS:
            pr = sm[:, int(round(o / DBIN))]
            pr = pr / pr.sum()
            cnt = rng.multinomial(NSEED, pr)
            for i in np.nonzero(cnt)[0]:
                plan.setdefault(i, []).append((s, o, cnt[i]))
    lab = {(s, o): [] for s in ("heavy", "light") for o in OMEGAS}
    eng = {(s, o): [] for s in ("heavy", "light") for o in OMEGAS}
    for n_, i in enumerate(sorted(plan)):
        w, dE, Ee, iq = records(items[i])
        for s, o, c in plan[i]:
            L, En = sample_records(w, dE, Ee, iq, o, c, rng)
            lab[(s, o)].append(L)
            eng[(s, o)].append(En)
    for s in ("heavy", "light"):
        for o in OMEGAS:
            out[f"lab_{s}_{o}"] = np.concatenate(lab[(s, o)]).astype(np.int32)
            out[f"eng_{s}_{o}"] = np.concatenate(eng[(s, o)]).astype(np.float32)
    for nm, (w, dE, Ee, iq) in (("photon", (wph, dEph, Eeph, iqph)), ("q0", (w0, dE0, Ee0, iq0))):
        for o in OMEGAS:
            L, En = sample_records(w, dE, Ee, iq, o, NSEED, rng)
            out[f"lab_{nm}_{o}"] = L.astype(np.int32)
            out[f"eng_{nm}_{o}"] = En.astype(np.float32)
    np.savez(os.path.join(WORK, f"seeds_{TAG}.npz"), H_heavy=H["heavy"], H_light=H["light"], H_photon=Hph,
             H_q0=H0, omegas=OMEGAS, dbin=DBIN, qgrid0=qg, q0=q0, edges=edges, nq=len(items), **out)
    print(f"total {time.time() - t0:.0f} s; q0 grid |q| = {qg:.4f} vs {q0:.4f} (2pi/a)", flush=True)


if __name__ == "__main__":
    main()
