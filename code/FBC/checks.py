"""FBC checks (all must PASS). Run: python3 checks.py   (needs the cached tables of ii.py, exch.py, seeds.py, run_mc.py)

C1  bands: calibrated gap 1.160 eV; exact Oh symmetry of grid energies; rotated wave functions are eigenvectors.
C2  completeness sum rule of the density vertex: sum over all bands |rho_n'n(k,q)|^2 = 1 (Umklapp included).
C3  f-sum rule and eps_inf of the diagonal band RPA (small q).
C4  symmetry rotation of S_GG'(p, omega) against a direct evaluation (0.5 eV-integrated, relative).
C5  factorised direct impact-ionization rate (ii.py) against the brute-force sampled golden rule (exch.py).
C6  exchange amplitude = direct amplitude with the two final electrons relabelled.
C7  k-grid convergence of the shell-averaged rates (12^3 vs 10^3).
C8  phonon DOS normalisation (state count) and parabolic band-edge limit.
C9  the PRODUCTION engine mc.Model.run (book kernels swapped in) against the book's generating function (v2);
C9ref an independent reference MC against the same (v1 C9).
C10 seed energy sum rule E_e + E_h = omega - E_g, and q -> 0 limit of the DM vertex = optical (photon) vertex.
C11 MC: energy identity omega = N E_g + E_ph + E_res (asserted per event in run_mc.py), normalisation, and
    sample convergence with independent seed draws (random disjoint seed subsets, v2).
C12 casc18_3 failure mechanisms (grid-top extrapolation in Gat; NZ = 32 aliasing) and the fix (v2).
C2 is a unitarity sanity check only (trivial).
"""
import fbc_common  # noqa: F401
import os
import sys
import json
import numpy as np
from fbc_common import (Grid, PW, gset, grid_bands, make_epm, EG, NV, WORK, DATA, RY, B, UNIT, OMEGA, model_edges)

RES = []
TAG = "refit_n12_nb20_s8_sig0.1"


def report(name, ok, msg):
    RES.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}", flush=True)


def c1():
    for var in ("refit", "scissor"):
        si = make_epm(var)
        ev, ec, kc = model_edges(si)
        bd = grid_bands(12, 20, var)
        gap = float(bd["ecbm"])
        report(f"C1 gap ({var})", abs(gap - EG) < 2e-3, f"E_g = {gap:.4f} eV, CBM at {float(kc):.3f} X")
    bd = grid_bands(12, 20, "refit")
    g = Grid(12)
    dev = max(np.abs(bd["E"][g.perm[o]] - bd["E"]).max() for o in range(48))
    si = make_epm("refit")
    err = 0
    for j in (3, 101, 777, 1500):
        H = si.hamiltonian(g.k[j])
        w = np.linalg.eigvalsh(H)[:20]
        err = max(err, np.abs(H @ bd["C"][j] - bd["C"][j] * w[None, :]).max())
    report("C1 symmetry", dev < 1e-10 and err < 1e-9, f"max |E(Rk) - E(k)| = {dev:.1e} eV; max |H c - e c| = {err:.1e} Ry")


def c2():
    si = make_epm("refit")
    pw = PW(si)
    g = Grid(12)
    rng = np.random.default_rng(3)
    worst = 0
    for _ in range(4):
        k = rng.random(3) - 0.5
        q = (rng.random(3) - 0.5) * 3
        w1, v1 = np.linalg.eigh(si.hamiltonian(k))
        G0 = np.rint(k + q)                                   # integer cartesian shift (2pi/a units) of a lattice vector?
        # use an Umklapp G_U from the reciprocal lattice: choose k' = k + q - G_U with G_U = round in reduced coords
        red = (k + q) @ np.linalg.inv(B)
        mU = np.rint(red).astype(int)
        kp = k + q - mU @ B
        w2, v2 = np.linalg.eigh(si.hamiltonian(kp))
        ix = pw.shifted(mU)                                   # index of g - G_U
        ok = ix >= 0
        # rho_n'n = sum_g c*_n'(k', g) c_n(k, g - G_U): <k'+g| e^{iqr} |k + g - G_U>
        for n in (0, 3, 6):
            rho = v2[ok].conj().T @ v1[ix[ok], n]
            worst = max(worst, abs((np.abs(rho) ** 2).sum() - (np.abs(v1[ix[ok], n]) ** 2).sum()))
        tr = 1 - (np.abs(v1[ix[ok], 0]) ** 2).sum()
    report("C2 completeness (trivial: unitarity of eigh, not a truncation test)", worst < 1e-10, f"|sum_n' |rho|^2 - kept norm| = {worst:.1e} (basis-edge loss of the norm {tr:.1e})")


def c3():
    from fbc_common import eps_cappellini
    d = np.load(os.path.join(WORK, f"ii_{TAG}.npz"))
    q, fs, e0 = d["qA"].ravel(), d["fsum"].ravel(), d["eps0"].ravel()
    worst_f, worst_e, msg = 1.0, 0.0, []
    for a, b in ((0.1, 0.25), (0.25, 0.4), (0.4, 0.7)):
        s = (q > a) & (q < b)
        qm = q[s].mean()
        worst_f = min(worst_f, fs[s].mean())
        r = e0[s].mean() / eps_cappellini(qm)
        worst_e = max(worst_e, abs(r - 1))
        msg.append(f"q = {qm:.2f}/A: eps_RPA = {e0[s].mean():.2f} (Cappellini {eps_cappellini(qm):.2f}), f-sum {fs[s].mean():.3f}")
    report("C3 f-sum / eps", worst_f > 0.95 and worst_e < 0.15, "; ".join(msg) +
           " (diagonal band RPA, window 0-21.8 eV; Cappellini eps(0) = 11.7)")


def c4():
    sys.argv = ["x", "12"]
    import ii
    ii.setup()
    g = ii._G["g"]
    S_irr, m0, _, _ = ii.phase_A()
    ii._G["S_irr"], ii._G["m0_irr"] = S_irr, m0
    worst = 0
    for ip in (101, 150, 777, 1333):
        S, m = ii.full_S(ip)
        P, dE, _ = ii.pair_block(g.i[ip], m)
        Sd = ii.bin_S(P, dE)
        # integrate over 0.5 eV windows
        nb = S.shape[0] // 10 * 10
        A = S[:nb].reshape(-1, 10, *S.shape[1:]).sum(1)
        Bd = Sd[:nb].reshape(-1, 10, *S.shape[1:]).sum(1)
        worst = max(worst, np.abs(A - Bd).max() / np.abs(Bd).max())
    report("C4 S rotation", worst < 0.02, f"max |S_rot - S_direct| / max S = {worst:.4f} (0.5 eV windows; residual = "
           "the fixed-sphere basis splitting the sticking bands on the zone faces by <= 0.06 eV)")


def c5():
    r = json.load(open(os.path.join(DATA, f"rates_{TAG}.json")))
    E = np.array(r["E"])
    out = []
    for t in "eh":
        W = np.array(r[f"W_{t}_cap"])
        Gs = np.array(r[f"GDsampled_{t}"])
        sel = (E > 3) & (E < (18 if t == "e" else 12)) & (W > 0)
        out.append(np.sum(Gs[sel]) / np.sum(W[sel]))
    report("C5 direct rate brute force", all(abs(x - 1) < 0.1 for x in out),
           f"sampled/factorised (pooled 3-18 eV e, 3-12 eV h) = {out[0]:.3f}, {out[1]:.3f}")


def c6():
    """relabelling symmetry in expectation: over uniformly sampled ordered configurations, sum g|M_E|^2 must equal
    sum g|M_D|^2 (M_E of one configuration is M_D of another); tests the exchange momentum and Umklapp bookkeeping."""
    sys.argv = ["x", "12", "10"]
    import exch
    exch.setup()
    g, E, ce = exch._G["g"], exch._G["E"], exch._G["ce"]
    vb = np.arange(NV)
    inv = np.array([int(np.where(np.all(exch._G["mG"] == -m, axis=1))[0][0]) for m in exch._G["mG"]])
    rng = np.random.default_rng(5)
    sD = sE = 0.0
    for _ in range(600):
        k1 = g.irr[rng.integers(len(g.irr))]
        k2, ip = rng.integers(g.N, size=2)
        p = exch.shortest(g.i[ip] / g.n)
        k1p = g.index(g.i[k1] - g.i[ip])
        k2p = g.index(g.i[k2] + g.i[ip])
        px = exch.shortest(g.i[k1] / g.n - g.i[k2] / g.n - p)
        r1 = exch.rho(k1p, k1, -p, ce, ce)[:, inv, :]
        r2 = exch.rho(k2p, k2, p, ce, vb)
        r3 = exch.rho(k2p, k1, -px, ce, ce)[:, inv, :]
        r4 = exch.rho(k1p, k2, px, ce, vb)
        MD = np.einsum("aGn,cGv,G->acvn", r1, r2, exch.wvec(p, "cap"))
        ME = np.einsum("cGn,aGv,G->acvn", r3, r4, exch.wvec(px, "cap"))
        dEn = (E[k1, ce][None, None, None, :] + E[k2, :NV][None, None, :, None]
               - E[k1p, ce][:, None, None, None] - E[k2p, ce][None, :, None, None])
        wgt = np.exp(-dEn ** 2 / (2 * 0.3 ** 2)) * (E[k1, ce] - EG > 4)[None, None, None, :]
        sD += (wgt * np.abs(MD) ** 2).sum()
        sE += (wgt * np.abs(ME) ** 2).sum()
    report("C6 exchange relabelling", abs(sE / sD - 1) < 0.25,
           f"sum g|M_E|^2 / sum g|M_D|^2 = {sE / sD:.3f} over 600 sampled configurations (initial electrons > 4 eV; "
           f"expectation 1, sampling noise ~0.1-0.2)")


def c7():
    f10 = os.path.join(DATA, "rates_refit_n10_nb20_s8_sig0.1.json")
    f8a = os.path.join(DATA, "rates_refit_n8_nb20_s8_sig0.1.json")
    f8b = os.path.join(DATA, "rates_refit_n8_nb20_s11_sig0.1.json")
    if not all(os.path.exists(f) for f in (f10, f8a, f8b)):
        report("C7 k-grid / G set", False, "rates for n = 10 or the n = 8 G-shell pair missing")
        return
    a = json.load(open(os.path.join(DATA, f"rates_{TAG}.json")))
    b, c8a, c8b = json.load(open(f10)), json.load(open(f8a)), json.load(open(f8b))
    ph = np.load(os.path.join(DATA, "phonon_refit.npz"))
    E = np.array(a["E"])
    msg, ok = [], True
    for t, hi, dos in (("e", 18, ph["dos_e"]), ("h", 12, ph["dos_h"])):
        wa, wb = np.array(a[f"W_{t}_cap"]), np.array(b[f"W_{t}_cap"])
        xs = np.arange(3, hi)
        r = np.array([wa[(E >= x) & (E < x + 1)].mean() / wb[(E >= x) & (E < x + 1)].mean() for x in xs])
        wdos = np.array([np.interp(x + 0.5, ph["E"], dos) for x in xs])
        mean_dev = float(np.sum(wdos * np.abs(np.log(r))) / wdos.sum())
        sa, sb = np.array(c8a[f"W_{t}_cap"]), np.array(c8b[f"W_{t}_cap"])
        rg = np.array([sb[(E >= x) & (E < x + 1)].mean() / sa[(E >= x) & (E < x + 1)].mean() for x in xs])
        ok = ok and mean_dev < 0.10 and np.max(np.abs(np.log(r))) < np.log(1.6) and np.max(np.abs(np.log(rg))) < np.log(1.1)
        msg.append(f"{t}: DOS-weighted mean |ln W12/W10| = {mean_dev:.3f}, max factor {np.exp(np.max(np.abs(np.log(r)))):.2f} "
                   f"at {xs[np.argmax(np.abs(np.log(r)))]}-{xs[np.argmax(np.abs(np.log(r)))] + 1} eV; G shells 11 vs 8 (n = 8): "
                   f"max {np.exp(np.max(np.abs(np.log(rg)))):.3f}")
    # threshold windows (informational; v2, ref. A sec. 2e): the onset is grid-sensitive
    thr = []
    for t in ("e", "h"):
        wa, wb = np.array(a[f"W_{t}_cap"]), np.array(b[f"W_{t}_cap"])
        for x0, x1 in ((1.5, 2.0), (2.0, 2.5), (2.5, 3.0), (3.0, 4.0)):
            s_ = (E >= x0) & (E < x1)
            thr.append(f"{t} {x0}-{x1}: {wa[s_].mean() / max(wb[s_].mean(), 1e-300):.2f}")
    msg.append("threshold windows W12/W10 (not tested; onset quoted +-0.2 eV): " + ", ".join(thr))
    report("C7 k-grid / G set", ok, "; ".join(msg))


def c8():
    ph = np.load(os.path.join(DATA, "phonon_refit.npz"))
    E = ph["E"]
    vol = (5.43e-8) ** 3 / 4
    nh = np.trapezoid(ph["dos_h"], E) * vol        # holes: 4 bands -> 4 states per spin per cell
    x = 0.3
    m = 0.32
    g_par = 6 * (1 / (2 * np.pi ** 2)) * (m / 3.80998212) ** 1.5 * np.sqrt(x) * 1e24     # per eV cm^3 (6 valleys)
    gx = np.interp(x, E, ph["dos_e"])
    report("C8 phonon DOS", abs(nh - 4) < 0.05 and abs(gx / g_par - 1) < 0.3,
           f"valence states per spin per cell = {nh:.3f} (4); electron DOS at 0.3 eV / parabolic (m_d = 0.32, 6 valleys) "
           f"= {gx / g_par:.2f}")


def c9():
    """the PRODUCTION engine mc.Model.run, with only its kernels swapped for the book's energy-only random-k model:
    per-state W_ii = p_ii/(1 - p_ii) against W_ph = 1 (one 63.04 meV phonon), and II products drawn from the book's
    Dirichlet(3/2) split (hole <= W_h) through the label energies that run() rescales.  Compared with the book's
    generating function (casc18_3.Casc.pair)."""
    sys.path.insert(0, os.path.join(fbc_common.HERE, "..", "..", "book", "figscripts", "ch18"))
    import casc18_3 as bk
    import mc
    c = bk.Casc()
    nw = c.nw * c.h * bk.EG
    rng = np.random.default_rng(13)

    class BookKernels(mc.Model):
        def __init__(s):
            s.de = 0.0005
            x = np.arange(0, 26, s.de) + s.de / 2
            xh = x[x <= bk.WH]
            s.Ek = [x[:, None], xh[:, None]]
            s.nb = [1, 1]
            s.sorted = [(x, np.arange(len(x))), (xh, np.arange(len(xh)))]
            pe = np.interp(x / bk.EG, c.x, c.p[0])
            ph = np.interp(xh / bk.EG, c.x, c.p[1])
            s.Wii = [(pe / (1 - pe))[:, None], (ph / (1 - ph))[:, None]]
            s.phE = np.array([0.0, 30.0])
            s.phW = [np.array([[1.0, 1.0], [0.0, 0.0]])] * 2          # row 1 = the (unused) acoustic slot
            s.phL = [np.array([[nw, nw], [0.0, 0.0]])] * 2
            s.E = np.zeros((len(x), NV + 1))
            s.pend = None

        def _idx(s, t, v):
            return np.clip(np.floor(v / s.de).astype(int), 0, len(s.Ek[t]) - 1)

        def sample_ii(s, t, k, b, rng_):
            y = s.Ek[t][k, 0] - bk.EG
            out = np.zeros((len(y), 3))
            todo = np.arange(len(y))
            while len(todo):
                u = rng_.dirichlet([1.5, 1.5, 1.5], len(todo)) * y[todo, None]
                hole = u[:, 2] if t == 0 else u[:, 0:2].max(1)
                ok = hole <= bk.WH
                out[todo[ok]] = u[ok]
                todo = todo[~ok]
            s.pend = (out, t)
            return s._idx(t, out[:, 0]), np.zeros(len(y), int), np.zeros(len(y), int)

        def sample_pair(s, p, omega, rng_):
            out, t = s.pend
            xe, xh = (out[:, 1], out[:, 2]) if t == 0 else (out[:, 2], out[:, 1])
            z = np.zeros(len(p), int)
            return s._idx(0, xe), z, s._idx(1, xh), z

    M = BookKernels()
    dw0 = mc.DW
    mc.DW = 0.0005
    worst, msg = 0, []
    try:
        for Ee, Eh in ((8.84, 0.0), (4.42, 4.42), (2.5, 1.34), (15.0, 3.84)):
            n = 30000
            ke, be = M.relabel(0, np.full(n, Ee), rng)
            kh, bh = M.relabel(1, np.full(n, Eh), rng)
            r = M.run(dict(Ee=np.full(n, Ee), Eh=np.full(n, Eh), ke=ke, be=be, kh=kh, bh=bh), rng)
            err = np.abs(r["N"] * bk.EG + r["Eph"] + r["Eres"] - (Ee + Eh + bk.EG)).max()
            d = bk.tv(np.bincount(r["N"], minlength=12)[:12] / n, c.pair(Ee, Eh)[:12])
            worst = max(worst, d if err < 1e-9 else 1.0)
            msg.append(f"({Ee},{Eh}): TV = {d:.4f}")
    finally:
        mc.DW = dw0
    report("C9 production MC engine vs book generating function", worst < 0.015,
           "; ".join(msg) + " (mc.Model.run with book kernels, 30000 events each; energy identity < 1e-9 eV)")


def c9ref():
    """independent reference MC (v1 C9), kept as a second implementation."""
    sys.path.insert(0, os.path.join(fbc_common.HERE, "..", "..", "book", "figscripts", "ch18"))
    import casc18_3 as bk
    c = bk.Casc()
    rng = np.random.default_rng(11)
    lam, nw = c.lam, c.nw * c.h * bk.EG                     # A_AB/E_g^3, phonon step (63.04 meV)

    def p_ii(t, E):
        return np.interp(E / bk.EG, c.x, c.p[t])

    def split(t, y):
        """(x1, x2, x3) ~ rho_t rho_t rho_tbar on the simplex (rejection from Dirichlet(3/2)); hole <= W_h."""
        out = np.zeros((len(y), 3))
        todo = np.arange(len(y))
        while len(todo):
            u = rng.dirichlet([1.5, 1.5, 1.5], len(todo)) * y[todo, None]
            hole = u[:, 2] if t == 0 else u[:, 0:2].max(1)
            ok = hole <= bk.WH
            out[todo[ok]] = u[ok]
            todo = todo[~ok]
        return out

    def mc(Ee, Eh, n):
        E = np.concatenate([np.full(n, Ee), np.full(n, Eh)])
        t = np.concatenate([np.zeros(n, int), np.ones(n, int)])
        ev = np.concatenate([np.arange(n)] * 2)
        N = np.ones(n, int)
        while len(E):
            keep = E >= bk.EG * bk.THETA
            E, t, ev = E[keep], t[keep], ev[keep]
            if not len(E):
                break
            pr = np.where(t == 0, p_ii(0, E), p_ii(1, E))
            ii_ = rng.random(len(E)) < pr
            E[~ii_] -= nw
            new = []
            for tt in (0, 1):
                m = np.flatnonzero(ii_ & (t == tt))
                if not len(m):
                    continue
                xs = split(tt, E[m] - bk.EG)
                E[m] = xs[:, 0]
                np.add.at(N, ev[m], 1)
                new.append((xs[:, 1], np.full(len(m), tt), ev[m]))
                new.append((xs[:, 2], np.full(len(m), 1 - tt), ev[m]))
            for a, b_, e_ in new:
                E, t, ev = np.concatenate([E, a]), np.concatenate([t, b_]), np.concatenate([ev, e_])
        return np.bincount(N, minlength=12)[:12] / n

    worst = 0
    msg = []
    for Ee, Eh in ((8.84, 0.0), (4.42, 4.42), (2.5, 1.34), (15.0, 3.84)):
        P_mc = mc(Ee, Eh, 30000)
        P_gf = c.pair(Ee, Eh)[:12]
        d = bk.tv(P_mc, P_gf)
        worst = max(worst, d)
        msg.append(f"({Ee},{Eh}): TV = {d:.4f}")
    report("C9ref reference MC vs book generating function", worst < 0.015, "; ".join(msg) + " (30000 events each)")


def c10():
    S = np.load(os.path.join(WORK, "seeds_refit_n12_m100_q4.npz"))
    worst = 0
    for ty in ("heavy", "light", "photon", "q0"):
        for o in S["omegas"][::8]:
            en = S[f"eng_{ty}_{o}"].astype(float)
            worst = max(worst, np.abs(en.sum(1) - (o - EG)).max())
    # q -> 0: |rho_cv(k, q)|^2 / q^2 -> |p_cv . qhat|^2 / (m Delta e)^2  (hbar = 1, model energies)
    si = make_epm("refit")
    pw = PW(si)
    rng = np.random.default_rng(2)
    k = rng.random(3) - 0.5
    qd = np.array([1.0, 0.3, -0.2])
    qd /= np.linalg.norm(qd)
    q = 1e-4 * qd
    w1, v1 = np.linalg.eigh(si.hamiltonian(k))
    w2, v2 = np.linalg.eigh(si.hamiltonian(k + q))
    rho = v2[:, NV:8].conj().T @ v1[:, :NV]                   # (c, v)
    kG = (k + si.G) * UNIT * 1973.269804                      # eV
    pq = v1[:, NV:8].conj().T @ ((kG @ qd)[:, None] * v1[:, :NV])
    dE = (w1[NV:8, None] - w1[None, :NV]) * RY
    lhs = np.abs(rho) ** 2 / (1e-4 * UNIT * 1973.269804) ** 2
    rhs = np.abs(pq) ** 2 / (511e3 * 0 + 510998.95) ** 2 / (dE / 1.0) ** 2 * 1.0
    # |q.p|^2/(m^2 dE^2) has units eV^-2 * eV^2 ... ratio check only
    big = rhs > 1e-3 * rhs.max()
    rat = (lhs[big] / rhs[big])
    report("C10 seeds", worst < 1e-4 and np.all(np.abs(rat - 1) < 0.02),
           f"max |E_e + E_h - (omega - E_g)| = {worst:.1e} eV; q->0 DM vertex / optical vertex = "
           f"{rat.min():.4f}-{rat.max():.4f}")


def c11():
    """normalisation, and MC sample convergence with INDEPENDENT seed draws: halfA and halfB use disjoint
    slices [0, 10^4) and [10^4, 2x10^4) of a fixed random permutation of the 2x10^4 stored seed samples (not index
    halves, which are q-ordered), with different cascade RNGs; v2 primary kernels."""
    msg, ok = [], True
    f = os.path.join(DATA, "mc_v2primary.npz")
    if os.path.exists(f):
        d = np.load(f)
        norm = max(np.abs(d[f"{t}_P"].sum(1) - 1).max() for t in ("heavy", "light", "photon"))
        ok = ok and norm < 1e-9
        msg.append(f"max |sum P - 1| = {norm:.1e}")
    fa, fb = os.path.join(DATA, "mc_halfA.npz"), os.path.join(DATA, "mc_halfB.npz")
    if not (os.path.exists(fa) and os.path.exists(fb)):
        report("C11 MC", False, "mc_halfA/halfB missing")
        return
    a, b = np.load(fa), np.load(fb)
    n = 10000
    dmax, zmax = 0.0, 0.0
    for t in ("heavy", "photon"):
        Pa, Pb = a[f"{t}_P"], b[f"{t}_P"]
        d = 0.5 * np.abs(Pa - Pb).sum(1)
        pm = 0.5 * (Pa + Pb)
        sig = 0.5 * np.sqrt(2 * pm * (1 - pm) / n).sum(1)          # ~ expected TV of two independent samples
        dmax = max(dmax, d.max())
        zmax = max(zmax, (d / np.maximum(sig, 1e-6)).max())
    ok = ok and zmax < 3.5
    msg.append(f"independent seed draws and RNGs (10^4 events per omega each): max TV = {dmax:.4f}, "
               f"max TV / expected-noise = {zmax:.2f} over 73 omegas x 2 seeds (pass < 3.5)")
    report("C11 MC normalisation / statistics", ok, "; ".join(msg))


def c12():
    """IF-FBC-8 (v2): casc18_3 failure mechanisms and fix. (i) Casc.Gat extrapolates linearly beyond the grid top
    X E_g (53.4 eV for X = 46); (ii) NZ = 32 aliasing at <N> + several sigma >= 32 (above ~85 eV). Fixed = grid
    covering the energy (X = 90) and NZ = 64."""
    sys.path.insert(0, os.path.join(fbc_common.HERE, "..", "..", "book", "figscripts", "ch18"))
    import casc18_3 as bk
    nz0 = bk.NZ

    def mv(c, o):
        P = c.pair(o - bk.EG, 0.0)
        n = np.arange(bk.NZ)
        m = (P * n).sum()
        return m, (P * n * n).sum() - m * m
    try:
        bk.NZ = 32
        c46 = bk.Casc(X=46.0)
        c90 = bk.Casc(X=90.0)
        v46_60 = mv(c46, 60.0)[1]
        m50, v50 = mv(c90, 50.0)
        m100, v100 = mv(c90, 100.0)
        F32 = (v100 - v50) / (m100 - m50)
        bk.NZ = 64
        c90b = bk.Casc(X=90.0)
        r60 = mv(c90b, 60.0)[1]
        m50, v50 = mv(c90b, 50.0)
        m100, v100 = mv(c90b, 100.0)
        eps64, F64 = 50 / (m100 - m50), (v100 - v50) / (m100 - m50)
    finally:
        bk.NZ = nz0
    ok = abs(v46_60 - r60) > 0.5 and F32 > 0.2 and abs(F64 - 0.1142) < 0.002 and abs(eps64 - 3.7495) < 0.005
    report("C12 casc18_3 domain/aliasing flag", ok,
           f"Var(60 eV): X = 46 grid {v46_60:.3f} vs fixed {r60:.3f}; F(50->100 eV): NZ = 32 {F32:.3f}, "
           f"NZ = 64 & X = 90 {F64:.4f} (eps {eps64:.4f}); 20-40 E_g values 3.7495/0.1142")


if __name__ == "__main__":
    which = sys.argv[1:] or ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c9ref", "c10", "c11", "c12"]
    for w in which:
        globals()[w]()
    npass = sum(ok for _, ok in RES)
    print(f"\n{npass}/{len(RES)} checks PASS")
    sys.exit(0 if npass == len(RES) else 1)
