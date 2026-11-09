"""R3/X1 checks of the acoustic Q->0 limit of the PAER amplitude (D1 eq. 1).

Model: 1D continuum electron (m_e = 1, G = 2pi/a = 1) in a monatomic lattice with ion form factor W(K)
(even, W(0)=w0, W(1)=V1, W'(1)=V1p), truncated to two plane waves {kappa, kappa-1} at every k-point.
This truncation is internally exact for every identity used here: p is diagonal, e^{iqx} maps PW n -> PW n,
and the Q=0 displacement vertex equals [A,H] with A = -i l p (ASR) element by element.
Phonon: u_j = l e^{iQ X_j} (l factored out, set to 1), omega_Q = c|Q|.
  dV: <kappa+Q+n'|dV|kappa+n> = -i (Q+n'-n) W(Q+n'-n)

Checks
  A. Xi^n = D^n + v_n P_n : lab-frame intraband slope of g_nn equals the frozen-strain deformation potential
     plus the Galilean piece (Hellmann-Feynman D^n = <n|dH/d eta|n>, fixed reduced k).
  B. Direct limit of the full two-band sum (1), Q = sigma*1e-20, against the closed formula
       M/l -> i rho_cv { q - (P_c - P_v) + Xi^c/(v_c + s sigma c) - Xi^v/(v_v + s sigma c) }
     for emission/absorption (s = +-1), both directions sigma, sub- and supersonic c; and against the
     D1 form i q rho_cv and the D2 form i (q - dP) rho_cv (both should FAIL).
  C. Exact finite-Q Ward identity:  M[g] = M[g'] + i q rho_cv(k, q+Q),
       g'_mn(kap,Q) = g_mn + i s_mn (e_n(kap) - e_m(kap+Q) - s w_Q),  s_mn = <m,kap+Q| {e^{iQx},p}/2 |n,kap>.
Precision: mpmath, 60 digits. Runtime < 2 s.
"""
import mpmath as mp

mp.mp.dps = 60
w0, V1, V1p = mp.mpf(-1) / 5, mp.mpf(1) / 7, mp.mpf(1) / 11
# W(K) = w0 + al K^2 + be K^4 with W(1)=V1, W'(1)=V1p
be = (V1p - 2 * (V1 - w0)) / 2
al = V1 - w0 - be
W = lambda K: w0 + al * K**2 + be * K**4
Wp = lambda K: 2 * al * K + 4 * be * K**3
NS = [0, -1]


def H(kap):
    return mp.matrix([[kap**2 / 2 + w0, V1], [V1, (kap - 1) ** 2 / 2 + w0]])


_ref = {}


def eig(kap, ref=None):
    E, U = mp.eigsy(H(kap))
    idx = sorted(range(2), key=lambda i: E[i])
    E = [E[i] for i in idx]
    U = [[U[j, i] for j in range(2)] for i in idx]  # U[band] = PW vector
    for b in range(2):  # smooth gauge: positive overlap with reference vectors
        r = ref[b] if ref is not None else [1, 1]
        if sum(U[b][j] * r[j] for j in range(2)) < 0:
            U[b] = [-x for x in U[b]]
    return E, U


def dV(Q):
    return [[-1j * (Q + NS[a] - NS[b]) * W(Q + NS[a] - NS[b]) for b in range(2)] for a in range(2)]


def bil(u1, Mx, u2):
    return sum(u1[a] * Mx[a][b] * u2[b] for a in range(2) for b in range(2))


def g(kap, Q, m, n, st):
    (_, Uq), (_, U0) = st[kap + Q], st[kap]
    return bil(Uq[m], dV(Q), U0[n])


def rho(kap, q, m, n, st):
    return sum(st[kap + q][1][m][j] * st[kap][1][n][j] for j in range(2))


def smat(kap, Q, m, n, st):
    return sum(st[kap + Q][1][m][j] * st[kap][1][n][j] * (kap + NS[j] + Q / 2) for j in range(2))


def states(k, q, Q):
    st = {}
    for kap in (k, k + q):
        st[kap] = eig(kap)
    st[k + Q] = eig(k + Q, st[k][1])
    st[k + q + Q] = eig(k + q + Q, st[k + q][1])
    st[k + Q + q] = st[k + (q + Q)] = st[k + q + Q]  # same k-point, guard against float key order
    return st


def M(k, q, Q, s, c, prime=False):
    st, wQ, v, cb = states(k, q, Q), c * abs(Q), 0, 1
    E = lambda kap, b: st[kap][0][b]
    tot = 0
    for m in range(2):
        gA, gB = g(k + q, Q, cb, m, st), g(k, Q, m, v, st)
        if prime:
            gA += 1j * smat(k + q, Q, cb, m, st) * (E(k + q, m) - E(k + q + Q, cb) - s * wQ)
            gB += 1j * smat(k, Q, m, v, st) * (E(k, v) - E(k + Q, m) - s * wQ)
        tot += gA * rho(k, q, m, v, st) / (E(k + q + Q, cb) - E(k + q, m) + s * wQ)
        tot += rho(k + Q, q, cb, m, st) * gB / (E(k, v) - E(k + Q, m) - s * wQ)
    return tot, st


def band_data(kap, b):
    E, U = eig(kap)
    u = U[b]
    P = u[0] ** 2 * kap + u[1] ** 2 * (kap - 1)  # <p> = v (local potential)
    dH = [[-kap**2 - w0, -(Wp(1) + W(1))], [-(Wp(1) + W(1)), -(kap - 1) ** 2 - w0]]
    D = bil(u, dH, u)  # frozen homogeneous strain, fixed reduced k
    h = mp.mpf(10) ** -25
    st = {kap: eig(kap), kap + h: eig(kap + h, eig(kap)[1])}
    Xi = (g(kap, h, b, b, st) / (1j * h)).real  # lab-frame intraband slope
    return P, D, Xi


worst = {"A": 0, "B": 0, "C": 0}
for k, q in [(mp.mpf(3) / 10, mp.mpf(7) / 5), (mp.mpf(11) / 20, mp.mpf(-13) / 9)]:
    Pv, Dv, Xv = band_data(k, 0)
    Pc, Dc, Xc = band_data(k + q, 1)
    for (P, D, X) in [(Pv, Dv, Xv), (Pc, Dc, Xc)]:
        worst["A"] = max(worst["A"], abs(X - (D + P * P)))
    st0 = states(k, q, mp.mpf(0))
    r = rho(k, q, 1, 0, st0)
    print(f"k={float(k):.3f} q={float(q):.3f}: v_v={float(Pv):+.3f} v_c={float(Pc):+.3f} "
          f"Xi_v={float(Xv):+.4f} Xi_c={float(Xc):+.4f} D_v={float(Dv):+.4f} D_c={float(Dc):+.4f} rho_cv={float(r):+.4f}")
    for c in (mp.mpf(1) / 50, mp.mpf(3)):  # subsonic and supersonic phonon
        for s in (1, -1):
            for sig in (1, -1):
                Q = sig * mp.mpf(10) ** -20
                Mex, _ = M(k, q, Q, s, c)
                pred = 1j * r * (q - (Pc - Pv) + Xc / (Pc + s * sig * c) - Xv / (Pv + s * sig * c))
                d1, d2 = 1j * r * q, 1j * r * (q - (Pc - Pv))
                worst["B"] = max(worst["B"], abs(Mex - pred))
                print(f"  c={float(c):5.2f} s={s:+d} sigma={sig:+d}: M/l={complex(Mex):.6f}  formula err={float(abs(Mex-pred)):.1e}"
                      f"  |M-D1|={float(abs(Mex-d1)):.3f} |M-D2|={float(abs(Mex-d2)):.3f}")
    for Q in (mp.mpf(1) / 10, mp.mpf(-3) / 7):  # finite-Q Ward identity
        for s in (1, -1):
            c = mp.mpf(1) / 50
            Ml, st = M(k, q, Q, s, c)
            Mp, _ = M(k, q, Q, s, c, prime=True)
            worst["C"] = max(worst["C"], abs(Ml - Mp - 1j * q * rho(k, q + Q, 1, 0, st)))

print("A  max|Xi - (D + vP)|          =", mp.nstr(worst["A"], 3))
print("B  max|lim M/l - formula|      =", mp.nstr(worst["B"], 3))
print("C  max|M[g]-M[g']-iq rho(q+Q)| =", mp.nstr(worst["C"], 3))
