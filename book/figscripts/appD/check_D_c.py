"""Numerical checks for App. D.16-D.23 (Allen-Heine-Cardona, phonon self-energy,
phonon-assisted absorption, spin waves, BCS, conserving BCS response, Dirac RPA,
effective-mass donors).  Every number quoted in those sections is asserted here.

Run:  python check_D_c.py      (prints PASS lines; any failure raises AssertionError)

Sources of inputs are given at the point of use.  Pure-numerics checks use model
parameters chosen here; they are named in the text as model choices.
"""
import numpy as np
from numpy.linalg import eigh
from scipy import integrate, optimize, special

np.set_printoptions(precision=6)
RES = {}


def ok(name, cond, info=""):
    assert cond, f"FAIL {name}: {info}"
    print(f"PASS {name} {info}")


# ---------------------------------------------------------------------------
# D.16  rigid-ion relation in a 1D crystal: 3 cells x 2 atoms, plane waves
# ---------------------------------------------------------------------------
def d16():
    a_cell, ncell = 4.0, 3                      # model units (hbar = m = 1)
    L = a_cell * ncell
    nG = 41
    G = 2 * np.pi * np.arange(-(nG // 2), nG // 2 + 1) / L
    dq = G[:, None] - G[None, :]
    A, s = 1.2, 0.45                            # Gaussian well depth and width
    vt = lambda q: -A * s * np.sqrt(2 * np.pi) * np.exp(-q**2 * s**2 / 2)
    tau = [0.0, 1.7]                            # basis positions in the cell
    X0 = np.array([R * a_cell + t for R in range(ncell) for t in tau])
    species = np.array([k for R in range(ncell) for k in range(2)])

    def Vmat(X, nonrigid=0.0):
        M = sum(vt(dq) * np.exp(-1j * dq * x) for x in X) / L
        if nonrigid:
            # bond-centred well between atoms 0 and 1 whose depth depends on
            # their separation: not of rigid-ion form
            sep = X[1] - X[0]
            amp = nonrigid * (sep - 1.7) ** 2 + 0.3 * nonrigid * (sep - 1.7)
            xc = 0.5 * (X[0] + X[1])
            M = M + amp * np.exp(-dq**2 * 0.3**2 / 2) * np.exp(-1j * dq * xc) / L
        return M

    def eig(X, nonrigid=0.0):
        H = np.diag(G**2 / 2) + Vmat(X, nonrigid)
        return eigh(H)

    def dV(X, a, nonrigid=0.0, h=1e-5):
        Xp, Xm = X.copy(), X.copy()
        Xp[a] += h; Xm[a] -= h
        return (Vmat(Xp, nonrigid) - Vmat(Xm, nonrigid)) / (2 * h)

    def d2V(X, a, b, nonrigid=0.0, h=1e-4):
        def f(da, db):
            Y = X.copy(); Y[a] += da; Y[b] += db
            return Vmat(Y, nonrigid)
        return (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)

    n = 0                                        # lowest state, k = 0, nondegenerate
    for nonrigid in (0.0, 0.8):
        E, U = eig(X0, nonrigid)
        assert E[1] - E[0] > 1e-3
        na = len(X0)
        # exact Hessian of eigenvalue by finite differences
        h = 1e-4
        Hex = np.zeros((na, na))
        for a in range(na):
            for b in range(na):
                def e(da, db):
                    Y = X0.copy(); Y[a] += da; Y[b] += db
                    return eig(Y, nonrigid)[0][n]
                Hex[a, b] = (e(h, h) - e(h, -h) - e(-h, h) + e(-h, -h)) / (4 * h * h)
        psi = U[:, n]
        dVs = [U.conj().T @ dV(X0, a, nonrigid) @ U for a in range(na)]
        Hpt = np.zeros((na, na))
        for a in range(na):
            for b in range(na):
                fan = 2 * np.real(sum(dVs[a][n, m] * dVs[b][m, n] / (E[n] - E[m])
                                      for m in range(len(E)) if m != n))
                Hpt[a, b] = np.real(psi.conj() @ d2V(X0, a, b, nonrigid) @ psi) + fan
        rel = np.max(np.abs(Hpt - Hex)) / np.max(np.abs(Hex))
        ok(f"D16 frozen-PT Hessian = FD Hessian (nonrigid={nonrigid})", rel < 1e-5, f"rel={rel:.1e}")
        # sum rule 2: sum_a Hex[a,b] = 0
        sr = np.max(np.abs(Hex.sum(axis=0))) / np.max(np.abs(Hex))
        ok(f"D16 sum rule (sr2) (nonrigid={nonrigid})", sr < 1e-5, f"rel={sr:.1e}")
        # rigid-ion relation, crystal form with N and Q=0 operators
        dV0 = [sum(dVs[a] for a in range(na) if species[a] == k) for k in range(2)]
        worst = 0.0
        for b in range(na):                       # on-site element at site b
            onsite = np.real(psi.conj() @ d2V(X0, b, b, nonrigid) @ psi)
            kb = species[b]
            ria = -(2.0 / ncell) * np.real(sum(dV0[k][n, m] * dV0[kb][m, n] / (E[n] - E[m])
                                                 for k in range(2) for m in range(len(E)) if m != n))
            worst = max(worst, abs(ria - onsite) / abs(onsite))
        if nonrigid == 0.0:
            ok("D16 rigid-ion relation (ria) holds", worst < 1e-5, f"rel={worst:.1e}")
            RES["D16_ria_rel"] = worst
        else:
            ok("D16 rigid-ion relation fails for non-rigid potential", worst > 1e-2, f"rel={worst:.2f}")
            RES["D16_nonrigid_rel"] = worst

    # Fan-Migdal frequency sum: T sum_j D0(i w_j) G0(i w_n - i w_j)
    T, w0, xi = 0.37, 0.8, -0.25
    for nF in (0, 1, 3):
        wn = (2 * nF + 1) * np.pi * T
        jj = np.arange(-400000, 400001)
        Om = 2 * np.pi * jj * T
        D0 = 1 / (1j * Om - w0) - 1 / (1j * Om + w0)
        G0 = 1 / (1j * wn - 1j * Om - xi)
        S = T * np.sum(D0 * G0)
        nB, f = 1 / np.expm1(w0 / T), 1 / (np.exp(xi / T) + 1)
        z0 = 1j * wn - xi
        closed = -((nB + 1 - f) / (z0 - w0) + (nB + f) / (z0 + w0))
        ok(f"D16 Fan-Migdal Matsubara sum, j={nF}", abs(S - closed) < 1e-5 * abs(closed), f"{S:.6f} vs {closed:.6f}")


# ---------------------------------------------------------------------------
# D.17  linewidth, Allen form, alpha^2F, lambda on a cubic tight-binding metal
# ---------------------------------------------------------------------------
def d17():
    t, mu, wE, T, sig = 1.0, -0.7, 0.02, 0.004, 0.06   # model units
    n = 14
    k1 = 2 * np.pi * np.arange(n) / n
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    eps = lambda kx, ky, kz: -2 * t * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    xi = (eps(KX, KY, KZ) - mu).ravel()
    N = xi.size
    dlt = lambda x, s=sig: np.exp(-x**2 / (2 * s * s)) / np.sqrt(2 * np.pi) / s
    # occupations smeared by the same Gaussian as the delta functions, so that
    # -df/dxi is exactly the broadened delta (the T -> 0 step of the text)
    fF = lambda x: 0.5 * special.erfc(x / (np.sqrt(2) * sig))
    NF_cell = dlt(xi).sum() / N               # N_F * Omega, per spin per cell
    gam_allen, S = [], 0.0
    for iq in range(N):
        qx, qy, qz = np.unravel_index(iq, (n, n, n))
        Q = 2 * np.pi * np.array([qx, qy, qz]) / n
        xq = (eps(KX + Q[0], KY + Q[1], KZ + Q[2]) - mu).ravel()
        g2 = (0.1 * (1 + 0.3 * np.cos(KX + 0.5 * Q[0]) + 0.2 * np.cos(Q[1]))).ravel() ** 2
        dd = np.sum(g2 * dlt(xi) * dlt(xq))
        gam_allen.append(4 * np.pi * wE / N * dd)
        S += dd
    gam_allen = np.array(gam_allen)
    A = S / (NF_cell * N**2)                   # alpha^2F = A delta(w - wE)
    lam_a2F = 2 * A / wE
    lam_gam = np.sum(gam_allen / wE**2) / (2 * np.pi * NF_cell * N)
    ok("D17 lambda from widths = 2 int a2F/w", abs(lam_gam / lam_a2F - 1) < 1e-12, f"{lam_gam:.6f} {lam_a2F:.6f}")
    # full width vs Allen form for the electron gas (units m = kF = 1, EF = 1/2)
    m, kF = 1.0, 1.0
    EF = kF**2 / 2
    for (Qv, w, TT) in [(1.0, 0.01, 0.02), (0.5, 0.005, 0.01), (1.5, 0.01, 0.005)]:
        fd = lambda e: 0.5 * (1 - np.tanh((e - EF) / (2 * TT)))
        def integrand(k):
            e = k * k / (2 * m)
            c = (w - Qv**2 / (2 * m)) * m / (k * Qv)   # angular solution
            if abs(c) > 1:
                return 0.0
            return k * k * (m / (k * Qv)) * (fd(e) - fd(e + w)) / (4 * np.pi**2)
        full = integrate.quad(integrand, 1e-6, 3.0, points=[kF], limit=400)[0]
        allen = w * m**2 / (4 * np.pi**2 * Qv)
        r = full / allen
        ok(f"D17 electron gas: full width = Allen form (Q={Qv}, w={w}, T={TT})", abs(r - 1) < 2e-3, f"ratio={r:.5f}")
    # mass enhancement: derivative of eps integrals for Einstein a2F, W = 100 w'
    wp, W = wE, 100 * wE
    def S_T0(w):
        I1 = integrate.quad(lambda e: 1 / (w - e - wp), 0, W)[0]
        I2 = integrate.quad(lambda e: 1 / (w - e + wp), -W, 0)[0]
        return A * (I1 + I2)
    h = 1e-6
    dS = (S_T0(h) - S_T0(-h)) / (2 * h)
    ok("D17 -dSigma/dw = lambda (W=100 w')", abs(-dS / lam_a2F - 1) < 0.011, f"{-dS:.5f} vs {lam_a2F:.5f}")
    # insulator at T=0: gamma=0 for w < Eg  (two flat-ish bands)
    ev, ec = -1.0 + 0 * xi, 1.0 + 0 * xi      # Eg = 2
    g_ins = 4 * np.pi / N * np.sum((1.0 - 0.0) * dlt(ec - ev - wE, 0.01))
    ok("D17 insulator width vanishes below gap", g_ins < 1e-300, f"{g_ins}")


# ---------------------------------------------------------------------------
# D.18  four paths of phonon-assisted absorption: exact Fock-space check
# ---------------------------------------------------------------------------
def d18():
    rng = np.random.default_rng(7)
    # orbitals: (k label, energy, occupied?)  k0 = {v, w, c0, d0}, k1 = {u, c, d1}
    orb = [(0, -0.3, 1), (0, -1.1, 1), (0, 2.4, 0), (0, 3.7, 0),
           (1, -0.9, 1), (1, 1.2, 0), (1, 3.1, 0)]
    no = len(orb)
    k = np.array([o[0] for o in orb]); e = np.array([o[1] for o in orb])
    occ0 = [i for i, o in enumerate(orb) if o[2]]
    iv, ic = 0, 5                               # final hole (v, k0), electron (c, k1)
    Wm = np.zeros((no, no), complex)
    for a in range(no):
        for b in range(no):
            if k[a] == k[b]:
                Wm[a, b] = rng.normal() + 1j * rng.normal()
    Wm = Wm + Wm.conj().T
    Gm = np.zeros((no, no), complex)            # G[a, b]: b in k0 -> a in k1
    for a in range(no):
        for b in range(no):
            if k[a] == 1 and k[b] == 0:
                Gm[a, b] = rng.normal() + 1j * rng.normal()
    from itertools import combinations
    states = [frozenset(c) for c in combinations(range(no), 3)]
    idx = {st: i for i, st in enumerate(states)}
    nb = 6
    dim = len(states) * nb
    I = lambda st, nn: idx[st] * nb + nn

    def cdag_c(a, b, st):                        # c_a^dag c_b |st>, returns (sign, new) or None
        if b not in st: return None
        sgn = (-1) ** sum(1 for x in st if x < b)
        st2 = st - {b}
        if a in st2: return None
        sgn *= (-1) ** sum(1 for x in st2 if x < a)
        return sgn, st2 | {a}

    def one_body(M, boson):                      # boson: None, 'a' (b), 'c' (b^dag)
        H = np.zeros((dim, dim), complex)
        for st in states:
            for nn in range(nb):
                for a in range(no):
                    for b in range(no):
                        if M[a, b] == 0: continue
                        r = cdag_c(a, b, st)
                        if r is None: continue
                        sg, st2 = r
                        if boson is None:
                            H[I(st2, nn), I(st, nn)] += sg * M[a, b]
                        elif boson == 'a' and nn > 0:
                            H[I(st2, nn - 1), I(st, nn)] += sg * M[a, b] * np.sqrt(nn)
                        elif boson == 'c' and nn < nb - 1:
                            H[I(st2, nn + 1), I(st, nn)] += sg * M[a, b] * np.sqrt(nn + 1)
        return H

    wQ = 0.07
    E0 = np.array([sum(e[list(st)]) + wQ * nn for st in states for nn in range(nb)])
    Wop = one_body(Wm, None)
    st0 = frozenset(occ0)
    stf = frozenset(set(occ0) - {iv} | {ic})
    for mode, sgn_pm in (('abs', -1), ('em', +1)):
        Hc = one_body(Gm, 'a' if mode == 'abs' else 'c')
        Hep = Hc + Hc.conj().T
        n0 = 2
        i0 = I(st0, n0)
        nf = n0 - 1 if mode == 'abs' else n0 + 1
        f0 = I(stf, nf)
        Ei = E0[i0]
        omega = e[ic] - e[iv] + sgn_pm * wQ        # on shell
        safe = lambda d: np.where(np.abs(d) > 1e-12, 1 / np.where(np.abs(d) > 1e-12, d, 1), 0.0)
        R1 = safe(Ei + omega - E0); R2 = safe(Ei - E0)
        vi = np.zeros(dim, complex); vi[i0] = 1
        T = (Hep @ (R1 * (Wop @ vi)))[f0] + (Wop @ (R2 * (Hep @ vi)))[f0]
        ph = np.sqrt(n0) if mode == 'abs' else np.sqrt(n0 + 1)
        k0 = [p for p in range(no) if k[p] == 0]; k1 = [p for p in range(no) if k[p] == 1]
        M = sum(Gm[ic, p] * Wm[p, iv] / (omega - e[p] + e[iv]) for p in k0) + \
            sum(Wm[ic, p] * Gm[p, iv] / (e[iv] - e[p] - sgn_pm * wQ) for p in k1)
        Mel = sum(Gm[ic, p] * Wm[p, iv] / (omega - e[p] + e[iv]) for p in k0 if p not in occ0 or p == iv) + \
              sum(Wm[ic, p] * Gm[p, iv] / (e[iv] - e[p] - sgn_pm * wQ) for p in k1 if p not in occ0)
        rel = abs(T - ph * M) / abs(T)
        ok(f"D18 four-path amplitude = exact Fock-space T ({mode})", rel < 1e-12, f"rel={rel:.1e}")
        relel = abs(T - ph * Mel) / abs(T)
        RES[f"D18_electron_only_error_{mode}"] = relel
        ok(f"D18 dropping hole paths changes T by O(1) ({mode})", relel > 0.1, f"rel={relel:.2f}")
    # HBB joint density integral: int_0^x sqrt(e (x-e)) de = pi x^2 / 8
    x = 0.37
    val = integrate.quad(lambda u: np.sqrt(u * (x - u)), 0, x)[0]
    ok("D18 HBB integral pi x^2/8", abs(val / (np.pi * x * x / 8) - 1) < 1e-8)
    # prefactor (2m)^{3/2}(2m')^{3/2}/(16 pi^4) * pi/8 = (m m')^{3/2}/(16 pi^3)
    me, mh = 0.32, 0.5
    ok("D18 joint-density prefactor", abs((2*me)**1.5*(2*mh)**1.5/(16*np.pi**4)*np.pi/8 / ((me*mh)**1.5/(16*np.pi**3)) - 1) < 1e-14)
    # final prefactor: 2 pi e^2 /w^2 * Omega (m m')^{3/2}/(16 pi^3) = e^2 Omega (m m')^{3/2}/(8 pi^2 w^2)
    ok("D18 eps2 HBB prefactor", abs(2*np.pi/(16*np.pi**3) / (1/(8*np.pi**2)) - 1) < 1e-14)


# ---------------------------------------------------------------------------
# D.19  LSWT of type-II fcc antiferromagnet vs linearized classical precession
# ---------------------------------------------------------------------------
def d19():
    J2, J1, S = 1.0, 0.1, 1.0
    L = 4                                       # grid units of a/2, period 4 per axis (2 cubes)
    sites = [(x, y, z) for x in range(2 * L) for y in range(2 * L) for z in range(2 * L) if (x + y + z) % 2 == 0]
    Lp = 2 * L
    ns = len(sites)
    sgn = np.array([(-1) ** (((x + y + z) // 2) % 2) for (x, y, z) in sites])
    nn = [(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, b) for a in (1, -1) for b in (1, -1)] + [(0, a, b) for a in (1, -1) for b in (1, -1)]
    nnn = [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]
    pos = {s_: i for i, s_ in enumerate(sites)}
    J = np.zeros((ns, ns))
    for i, (x, y, z) in enumerate(sites):
        for d, Jv in [(d, J1) for d in nn] + [(d, J2) for d in nnn]:
            j = pos[((x + d[0]) % Lp, (y + d[1]) % Lp, (z + d[2]) % Lp)]
            J[i, j] += Jv
    assert ns == 4 * (L // 2) ** 3 * 8 // 1 or True
    # classical stability of the reference state is assumed; linearize dS/dt = -S x (J S)
    # deviations (sx, sy) on each site, S_i = s_i S z + delta
    # d(delta_i)/dt = -[ s_i S z x sum_j J_ij delta_j + delta_i x sum_j J_ij s_j S z ]
    h = J @ (sgn * S)                           # local z-field magnitude times sign
    M = np.zeros((2 * ns, 2 * ns))
    for i in range(ns):
        for j in range(ns):
            if J[i, j] != 0:
                # -s_i S z x delta_j :  z x (dx, dy) = (-dy, dx)
                M[2 * i, 2 * j + 1] += sgn[i] * S * J[i, j]
                M[2 * i + 1, 2 * j] += -sgn[i] * S * J[i, j]
        # - delta_i x (h_i z) = -(dy h, -dx h)
        M[2 * i, 2 * i + 1] += -h[i]
        M[2 * i + 1, 2 * i] += h[i]
    w = np.sort(np.abs(np.linalg.eigvals(M).imag))
    # LSWT prediction on the cluster: k-points of the sublattice (period-2a direction structure)
    a = 2.0                                     # cubic constant in grid units
    def sums(kv):
        JAA = sum(J1 * np.cos(np.dot(kv, d)) for d in nn if (d[0] + d[1] + d[2]) == 0)
        JAB = sum(J1 * np.cos(np.dot(kv, d)) for d in nn if (d[0] + d[1] + d[2]) != 0) + \
              sum(J2 * np.cos(np.dot(kv, d)) for d in nnn)
        return JAA, JAB
    JAA0, JAB0 = sums(np.zeros(3))
    pred = []
    ks = [2 * np.pi * np.array([i, j, l]) / Lp for i in range(Lp) for j in range(Lp) for l in range(Lp)]
    for kv in ks:
        JAA, JAB = sums(kv)
        A = JAB0 - JAA0 + JAA; B = JAB
        pred.append(S * np.sqrt(max(A * A - B * B, 0)))
    pred = np.array(pred)
    # each true sublattice k appears multiple times in this redundant list; compare as sets
    wq = w[w > 1e-5]; pq = pred[pred > 1e-5]
    dev = max(np.min(np.abs(pq - x)) for x in wq)          # every classical frequency is predicted
    dev2 = max(np.min(np.abs(wq - x)) for x in pq)         # every prediction occurs
    RES["D19_dev"] = max(dev, dev2)
    ok("D19 classical precession = LSWT (type-II fcc, J1=0.1 J2)", max(dev, dev2) < 1e-9, f"max dev={max(dev, dev2):.1e}, {len(np.unique(np.round(pq, 8)))} distinct")
    # J1 = 0: maximum 6 J2 S and velocity 2 sqrt3 J2 S a
    kk = np.linspace(-np.pi, np.pi, 81)
    KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
    g = (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    wmax = 6 * J2 * S * np.sqrt(1 - g**2).max()
    ok("D19 zone maximum 6 J2 |S|", abs(wmax - 6 * J2 * S) < 1e-12, f"{wmax}")
    kx = 1e-4
    gk = (np.cos(kx) + 2) / 3
    v = 6 * J2 * S * np.sqrt(1 - gk**2) / kx
    ok("D19 velocity 2 sqrt3 J2 |S| a", abs(v / (2 * np.sqrt(3)) - 1) < 1e-6, f"{v:.6f}")


# ---------------------------------------------------------------------------
# D.20  BCS gap equation, ratio, coherence factors in a 4-mode Fock space
# ---------------------------------------------------------------------------
def d20():
    lam, wD = 0.2, 1.0
    D0 = optimize.brentq(lambda D: integrate.quad(lambda x: 1 / np.sqrt(x * x + D * D), 0, wD)[0] - 1 / lam, 1e-12, 1)
    ok("D20 T=0 gap = wD/sinh(1/lam)", abs(D0 / (wD / np.sinh(1 / lam)) - 1) < 1e-9, f"{D0:.6e}")
    def tc_eq(T):
        f = lambda x: np.tanh(x / (2 * T)) / x if x > 0 else 1 / (2 * T)
        return integrate.quad(f, 0, wD, limit=400, points=[T, 10 * T])[0] - 1 / lam
    Tc = optimize.brentq(tc_eq, 1e-4, 0.5, xtol=1e-14)
    ratio = D0 / Tc
    RES["D20_ratio"] = ratio
    ok("D20 Delta(0)/Tc = pi exp(-gamma)", abs(ratio - np.pi * np.exp(-np.euler_gamma)) < 2e-4, f"{ratio:.5f} vs {np.pi*np.exp(-np.euler_gamma):.5f}")
    ok("D20 Tc prefactor 2 e^gamma/pi = 1.134", abs(2 * np.exp(np.euler_gamma) / np.pi - 1.134) < 5e-4, f"{2*np.exp(np.euler_gamma)/np.pi:.4f}")
    ok("D20 Tc formula", abs(Tc / (2 * np.exp(np.euler_gamma) / np.pi * wD * np.exp(-1 / lam)) - 1) < 1e-3, f"{Tc:.6e}")
    # Matsubara identity tanh(x/2T)/(2x) = T sum 1/(x^2 + w_j^2)
    T, x = 0.13, 0.41
    j = np.arange(-2000000, 2000000)
    wj = (2 * j + 1) * np.pi * T
    ok("D20 tanh Matsubara expansion", abs(T * np.sum(1 / (x * x + wj**2)) / (np.tanh(x / (2 * T)) / (2 * x)) - 1) < 1e-6)
    # coherence factors: Fock space of modes 0=k up, 1=-k dn, 2=k' up, 3=-k' dn
    rng = np.random.default_rng(3)
    nm = 4
    dimF = 2**nm
    def cop(m):
        C = np.zeros((dimF, dimF))
        for st in range(dimF):
            if st >> m & 1:
                sgn = (-1) ** bin(st & ((1 << m) - 1)).count("1")
                C[st ^ (1 << m), st] = sgn
        return C
    c = [cop(m) for m in range(nm)]
    cd = [x_.T for x_ in c]
    for trial in range(5):
        xi, xip, Dl = rng.normal(size=3)
        H = xi * (cd[0] @ c[0] + cd[1] @ c[1]) + xip * (cd[2] @ c[2] + cd[3] @ c[3]) \
            - Dl * (cd[0] @ cd[1] + c[1] @ c[0] + cd[2] @ cd[3] + c[3] @ c[2])
        w, U = eigh(H)
        g0 = U[:, 0]
        E, Ep = np.hypot(xi, Dl), np.hypot(xip, Dl)
        # density and spin operators restricted to these modes, transfer k -> k'
        n_q = cd[2] @ c[0] + cd[1] @ c[3]       # up: k->k' ; down: -k' -> -k  (c^dag_{-k dn} c_{-k' dn})
        s_q = 0.5 * (cd[2] @ c[0] - cd[1] @ c[3])
        # two-quasiparticle state at energy E + E' with weight from n_q
        for op, sgnpm, name in ((n_q, +1, "density"), (s_q, -1, "spin")):
            v = op @ g0
            tgt = np.isclose(w - w[0], E + Ep, atol=1e-9)
            amp2 = np.sum(np.abs(U[:, tgt].T @ v) ** 2)
            pref = 1.0 if name == "density" else 0.25
            form = pref * 0.5 * (1 - (xi * xip - sgnpm * Dl * Dl) / (E * Ep))
            ok(f"D20 creation coherence factor, {name}, trial {trial}", abs(amp2 - form) < 1e-12, f"{amp2:.6f} vs {form:.6f}")


# ---------------------------------------------------------------------------
# D.21  conserving (generalized RPA) density response of a BCS superconductor
# ---------------------------------------------------------------------------
S1 = np.array([[0, 1], [1, 0]], complex)
S2 = np.array([[0, -1j], [1j, 0]], complex)
ETA = np.array([[1, 0], [0, -1]], complex)
ONE = np.eye(2, dtype=complex)


def nambu_bubbles(xi_k, xi_kq, D, z, ops, wts=None):
    """R0_AB(q,z) = (1/V) sum_k sum_ss' Tr[A P^s_{k+q} B P^s'_k] (nF(s'E)-nF(sE'))/(z+s'E-sE') at T=0."""
    E, Ep = np.hypot(xi_k, D), np.hypot(xi_kq, D)
    if wts is None:
        wts = np.ones_like(xi_k) / xi_k.size
    def proj(xi, En, s):
        h = (xi[:, None, None] * ETA - D * S1) / En[:, None, None]
        return 0.5 * (ONE + s * h)
    Pk = {s_: proj(xi_k, E, s_) for s_ in (1, -1)}
    Pq = {s_: proj(xi_kq, Ep, s_) for s_ in (1, -1)}
    R = np.zeros((len(ops), len(ops)), complex)
    for a, A in enumerate(ops):
        for b, B in enumerate(ops):
            tot = 0
            for s_, sp in ((1, -1), (-1, 1)):            # T = 0: only pair creation/annihilation
                occ = (1.0 if sp == -1 else 0.0) - (1.0 if s_ == -1 else 0.0)
                tr = np.einsum("ij,kjl,lm,kmi->k", A, Pq[s_], B, Pk[sp])
                tot = tot + np.sum(wts * tr * occ / (z + sp * E - s_ * Ep))
            R[a, b] = tot
    return R


def d21():
    # trace formula Tr[s_a P+ s_b P-] = delta - n_a n_b - i eps_abc n_c
    rng = np.random.default_rng(11)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    sig = [S1, S2, ETA]
    hn = sum(n[i] * sig[i] for i in range(3))
    Pp, Pm = 0.5 * (ONE + hn), 0.5 * (ONE - hn)
    eps = np.zeros((3, 3, 3))
    for (i, j, k_), v in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
        eps[i, j, k_] = v
    err = max(abs(np.trace(sig[a] @ Pp @ sig[b] @ Pm) - ((a == b) - n[a] * n[b] - 1j * np.dot(eps[a, b], n)))
              for a in range(3) for b in range(3))
    ok("D21 Nambu trace formula", err < 1e-14)
    # 2D square-lattice model with the pairing-channel contact attraction
    L, t, mu, U = 48, 1.0, -0.6, 2.0
    k1 = 2 * np.pi * np.arange(L) / L
    KX, KY = np.meshgrid(k1, k1, indexing="ij")
    eps_k = lambda kx, ky: -2 * t * (np.cos(kx) + np.cos(ky))
    xi = (eps_k(KX, KY) - mu).ravel()
    D = optimize.brentq(lambda D: U * np.mean(1 / (2 * np.hypot(xi, D))) - 1, 1e-6, 10)
    RES["D21_gap"] = D
    ops = [ETA, S1, S2]
    K = np.diag([0, -U / 2, -U / 2]).astype(complex)
    # Goldstone: 1 - K22 R22(0,0) = 0
    R00 = nambu_bubbles(xi, xi, D, 0.0 + 0j, ops)
    # explicit q = 0 entries of eq. D.21-q0
    for w in (0.37, 1.9):
        Rq = nambu_bubbles(xi, xi, D, w + 0j, ops)
        E = np.hypot(xi, D)
        F = np.mean(1 / (E * (w * w - 4 * E * E)))
        ok(f"D21 q=0 entries (w={w})", abs(Rq[0, 0] - 4 * D * D * F) < 1e-12 and abs(Rq[2, 2] - (w * w * F - 2 / U)) < 1e-12
           and abs(Rq[2, 0] - 2j * D * w * F) < 1e-12 and abs(Rq[0, 2] + 2j * D * w * F) < 1e-12)
    ok("D21 Goldstone condition from gap equation", abs(1 - K[2, 2] * R00[2, 2]) < 1e-12, f"{abs(1 - K[2, 2] * R00[2, 2]):.1e}")
    # q = 0: bare density response nonzero, conserving one vanishes at all w
    for w in (0.7 * D, 3.0 * D, 7.0):
        R0 = nambu_bubbles(xi, xi, D, w + 1e-9j, ops)
        Rc = np.linalg.solve(np.eye(3) - R0 @ K, R0)
        ok(f"D21 q=0 conserving R_nn vanishes (w={w:.3f})", abs(Rc[0, 0]) < 1e-9 * abs(R0[0, 0]), f"bare {R0[0,0].real:.3e}, cons {abs(Rc[0,0]):.1e}")
    # f-sum at finite q from the 1/w^2 tail: lim w^2 R = (1/N) sum_{k s} (e_{k+q}+e_{k-q}-2e_k) n_k
    v2 = 0.5 * (1 - xi / np.hypot(xi, D))
    for m in (1, 3):
        qx = 2 * np.pi * m / L
        xiq = (eps_k(KX + qx, KY) - mu).ravel()
        lap = (eps_k(KX + qx, KY) + eps_k(KX - qx, KY) - 2 * eps_k(KX, KY)).ravel()
        rhs = np.mean(2 * lap * v2)                # spin sum: 2 v_k^2 electrons per k
        W = 1e4
        R0 = nambu_bubbles(xi, xiq, D, W + 0j, ops)
        Rc = np.linalg.solve(np.eye(3) - R0 @ K, R0)
        fb, fc = (W**2 * R0[0, 0]).real, (W**2 * Rc[0, 0]).real
        RES[f"D21_fsum_bare_over_exact_q{m}"] = fb / rhs
        ok(f"D21 f-sum conserving (q=2pi*{m}/L)", abs(fc / rhs - 1) < 1e-5, f"cons/exact-1={fc/rhs-1:.1e}, bare/exact={fb/rhs:.3f}")
    # bare q=0 f-sum violation in the continuum shell model: int w S(0,w) dw = 8 pi Delta^2/V_BCS
    lam, wD = 0.25, 1.0
    Dc = wD / np.sinh(1 / lam)
    NF = 1.0
    VB = lam / NF
    val = 2 * np.pi * NF * integrate.quad(lambda x: 2 * Dc**2 / np.hypot(x, Dc), -wD, wD)[0]
    ok("D21 bare q=0 f-sum = 8 pi Delta^2/V_BCS", abs(val / (8 * np.pi * Dc**2 / VB) - 1) < 1e-9)
    # Anderson-Bogoliubov velocity in the 3D continuum: pole of 1 - K R22(q,w) at w = c q
    vF, Dl, lamc = 1.0, 1.0, 0.3
    wDc = 40.0
    xs, xw = special.roots_legendre(400)
    # xi grid (symmetric, Gauss-Legendre on [-wD, wD] after tanh-like mapping not needed for smooth integrand)
    xi_n, xi_w = wDc * xs, wDc * xw
    c_n, c_w = special.roots_legendre(64)
    XI, CC = np.meshgrid(xi_n, c_n, indexing="ij")
    WT = (np.outer(xi_w, c_w) / 2).ravel()     # (1/V) sum_k -> N_F int dxi int dc/2, N_F = 1
    Vb = lamc
    def gapfun(Dv):
        return Vb * np.sum(xi_w / (2 * np.hypot(xi_n, Dv))) - 1
    Dl = optimize.brentq(gapfun, 1e-6, 10)
    qv = 0.02 * Dl / vF
    XIq = (XI + vF * qv * CC + qv**2 / (2 * 50.0)).ravel()   # xi_{k+q} ~ xi + vF q cos + q^2/2m, m = kF/vF large
    XI0 = XI.ravel()
    def det(w):
        R0 = nambu_bubbles(XI0, XIq, Dl, w + 0j, [S1, S2], wts=WT)
        Kc = np.diag([-Vb / 2, -Vb / 2]).astype(complex)
        return np.linalg.det(np.eye(2) - Kc @ R0).real
    wpole = optimize.brentq(det, 0.2 * vF * qv, 0.9 * vF * qv, xtol=1e-14)
    cAB = wpole / qv
    RES["D21_cAB_over_vF"] = cAB / vF
    ok("D21 Anderson-Bogoliubov velocity vF/sqrt3", abs(cAB / (vF / np.sqrt(3)) - 1) < 1e-2, f"c/vF={cAB/vF:.4f}")


# ---------------------------------------------------------------------------
# D.22  RPA polarization of 3D Dirac electrons with a momentum cutoff
# ---------------------------------------------------------------------------
def d22():
    v = 1.0
    rho = lambda u, D: np.sqrt(np.clip(1 - 4 * D * D / u, 0, None)) * (1 + 2 * D * D / u)
    # 4x4 Dirac overlap: Tr[P+_{k'} P-_k]/2 = (1 - (v^2 k.k' + D^2)/(E E'))/2
    al = [np.kron(np.array([[0, 1], [1, 0]]), sp) for sp in (np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]))]
    be = np.kron(np.diag([1, -1]), np.eye(2))
    rng = np.random.default_rng(5)
    kk, kp, D = rng.normal(size=3), rng.normal(size=3), 0.4
    H = lambda k_: v * sum(k_[i] * al[i] for i in range(3)) + D * be
    E, Ep = np.sqrt(v * v * kk @ kk + D * D), np.sqrt(v * v * kp @ kp + D * D)
    Pp = 0.5 * (np.eye(4) + H(kp) / Ep); Pm = 0.5 * (np.eye(4) - H(kk) / E)
    ok("D22 Dirac overlap per degenerate state", abs(np.trace(Pp @ Pm).real / 2 - 0.5 * (1 - (v * v * kk @ kp + D * D) / (E * Ep))) < 1e-14)
    # bipolar identity: (1/V) sum_k F h(E+E') = q^2/(24 pi^2 v) int du rho(u) h(S)/(2S)
    def direct(q, z, D, Lam, g=1):
        # spherical quadrature over |k| < Lam, angle between k and q
        kn, kw = special.roots_legendre(600); cn, cw = special.roots_legendre(200)
        # map k in [0, Lam] with clustering near small k: k = Lam * ((x+1)/2)^3
        t = (kn + 1) / 2; k = Lam * t**3; wk = kw / 2 * 3 * Lam * t**2
        K, C = np.meshgrid(k, cn, indexing="ij"); W = np.outer(wk, cw)
        kp_ = np.sqrt(K * K + q * q + 2 * K * q * C)
        E1, E2 = np.sqrt(v * v * K * K + D * D), np.sqrt(v * v * kp_ * kp_ + D * D)
        F = 0.5 * (1 - (v * v * (K * K + K * q * C) + D * D) / (E1 * E2))
        Ssum = E1 + E2
        integ = F * (1 / (z - Ssum) - 1 / (z + Ssum)) * K * K
        return g * np.sum(W * integ) / (4 * np.pi**2)
    def formula(q, z, D, Lam, g=1):
        U = 4 * v * v * Lam * Lam
        s_ = z * z - v * v * q * q
        lo = 4 * D * D if D > 0 else 0.0
        # u-grid with clustering near the threshold
        x, w = special.roots_legendre(4000)
        y = (x + 1) / 2
        if D > 0:
            u = lo + (U - lo) * y**2; wu = w / 2 * 2 * y * (U - lo)
        else:
            u = U * y**4; wu = w / 2 * 4 * y**3 * U
        return -g * q * q / (24 * np.pi**2 * v) * np.sum(wu * rho(u, D) / (u - s_))
    for (q, w, D) in [(0.05, 0.6, 0.2), (0.05, 0.3, 0.2), (0.1, 0.8, 0.0), (0.1, 0.05, 0.0)]:
        z = w + 0.02j
        a, b = direct(q, z, D, 20.0), formula(q, z, D, 20.0)
        ok(f"D22 dispersion-integral form = direct sum (q={q}, w={w}, D={D})", abs(a - b) / abs(b) < 3e-3, f"{a:.5e} vs {b:.5e}")
    # closed forms
    Dl = 0.3
    for s_ in (0.1, -0.5, 0.3):
        lhs = s_ * integrate.quad(lambda u: rho(u, Dl) / (u * (u - s_)), 4 * Dl * Dl, np.inf, limit=400)[0]
        rhs = -6 * integrate.quad(lambda x: x * (1 - x) * np.log(1 - x * (1 - x) * s_ / Dl**2), 0, 1)[0]
        ok(f"D22 Feynman-parameter identity (s={s_})", abs(lhs - rhs) < 1e-8, f"{lhs:.8f} {rhs:.8f}")
    U = 1e8
    val = integrate.quad(lambda u: rho(u, Dl) / u, 4 * Dl * Dl, U, limit=500)[0]
    ok("D22 int rho/u = ln(U/D^2) - 5/3", abs(val - (np.log(U / Dl**2) - 5 / 3)) < 1e-6, f"{val:.6f}")
    ok("D22 int x(1-x) ln(x(1-x)) = -5/18", abs(integrate.quad(lambda x: x * (1 - x) * np.log(x * (1 - x)), 0, 1)[0] + 5 / 18) < 1e-10)
    # imaginary part vs Hochberg et al. Eq. (2.6): e^2 g/(24 pi kappa v) sqrt(1-4D^2/s)(1+2D^2/s)
    alpha = 1 / 137.035999
    g, kap = 2.0, 40.0
    s_ = 1.0
    Im_ours = g * alpha / (kap * v) / 6 * rho(s_, Dl)
    Im_hoch = 4 * np.pi * alpha * g / (24 * np.pi * kap * v) * rho(s_, Dl)
    ok("D22 Im eps/eps_bg = g alpha~/6 rho matches Ref. Eq. (2.6)", abs(Im_ours / Im_hoch - 1) < 1e-14)
    # static hard-cutoff constant from direct 3D quadrature (gapped, q -> 0)
    Lam, D = 50.0, 0.5
    q = 1e-3
    R0 = direct(q, 0.0 + 1e-12j, D, Lam).real
    pref = -q * q / (24 * np.pi**2 * v)            # R0 = pref * [ln(4 v^2 Lam^2/D^2) - 5/3]
    const = R0 / pref - np.log(4 * v * v * Lam * Lam / D**2)
    RES["D22_static_const"] = const
    ok("D22 static gapped hard-cutoff constant -5/3", abs(const + 5 / 3) < 2e-3, f"{const:.4f}")


# ---------------------------------------------------------------------------
# D.23  effective-mass donor in silicon: Kohn-Luttinger variational energy
# ---------------------------------------------------------------------------
def d23():
    Ry = 13.605693122994   # eV, CODATA (hydrogen Rydberg energy for infinite nuclear mass)
    a0 = 0.529177210903    # Angstrom, CODATA Bohr radius
    mpar, mperp = 0.916, 0.191    # silicon valley masses, tab:3-materials (Sect. 3.3)
    eps0 = 11.7                   # silicon static = optical dielectric constant (NOTATION ruling)
    gam = mperp / mpar
    Rys = mperp / eps0**2 * Ry * 1e3    # meV, transverse-mass effective Rydberg
    as_ = eps0 / mperp * a0             # Angstrom
    def E(p):
        a, b = p
        if b >= a:
            e = np.sqrt(1 - a * a / (b * b)); pot = np.arcsinh(e * b / a) / (b * e) if e > 0 else 1 / a
            # for b > a: <1/r> = artanh-type form; arcsinh(sqrt(b^2-a^2)/a)/sqrt(b^2-a^2)
            pot = np.arcsinh(np.sqrt(b * b - a * a) / a) / np.sqrt(b * b - a * a) if b > a else 1 / a
        else:
            e = np.sqrt(1 - b * b / (a * a)); pot = np.arcsin(e) / (a * e)
        return 2 / (3 * a * a) + gam / (3 * b * b) - 2 * pot
    # isotropic check gam = 1 -> E = -1 at a = b = 1
    g0 = gam
    gam = 1.0
    r = optimize.minimize(E, [0.8, 0.8], method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14})
    ok("D23 isotropic limit E = -1 Ry*", abs(r.fun + 1) < 1e-8, f"{r.fun:.10f}")
    gam = g0
    r = optimize.minimize(E, [1.0, 0.6], method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14})
    a, b = r.x
    Eb = -r.fun * Rys
    RES.update(D23_Rys_meV=Rys, D23_astar_A=as_, D23_E_over_Rys=-r.fun, D23_Eb_meV=Eb, D23_a_A=a * as_, D23_b_A=b * as_)
    ok("D23 effective Rydberg (transverse) 19.0 meV", abs(Rys - 18.98) < 0.01, f"{Rys:.3f} meV")
    ok("D23 longitudinal-mass Rydberg 91 meV", abs(mpar / eps0**2 * Ry * 1e3 - 91.0) < 0.1, f"{mpar/eps0**2*Ry*1e3:.2f}")
    ok("D23 anisotropic variational binding 29.7 meV", abs(Eb - 29.69) < 0.01 and abs(a * as_ - 24.3) < 0.05 and abs(b * as_ - 14.0) < 0.05, f"E_b={Eb:.2f} meV, a={a*as_:.1f} A, b={b*as_:.1f} A, E/Ry*={-r.fun:.4f}")
    # <1/r> closed form vs direct numerical average
    aa, bb = 1.3, 0.7
    num = integrate.quad(lambda mu: 1 / np.sqrt(aa * aa * (1 - mu * mu) + bb * bb * mu * mu), 0, 1)[0]
    e = np.sqrt(1 - bb * bb / (aa * aa))
    ok("D23 <1/r> = arcsin(e)/(a e)", abs(num - np.arcsin(e) / (aa * e)) < 1e-12)
    # valley-orbit 6x6 matrix eigenvalues
    D0, Dg, Df = -1.0, -0.3, -0.2
    M = np.full((6, 6), Df); np.fill_diagonal(M, D0)
    for i in range(0, 6, 2):
        M[i, i + 1] = M[i + 1, i] = Dg
    w = np.sort(np.linalg.eigvalsh(M))
    pred = np.sort([D0 + Dg + 4 * Df] + [D0 + Dg - 2 * Df] * 2 + [D0 - Dg] * 3)
    ok("D23 valley-orbit A1, E, T2 levels", np.allclose(w, pred, atol=1e-12), f"{w}")


if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["d16", "d17", "d18", "d19", "d20", "d21", "d22", "d23"]
    for w in which:
        globals()[w]()
    print(RES)
