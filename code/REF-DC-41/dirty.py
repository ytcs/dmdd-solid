"""REF-DC-41: T = 0 BCS density response with Born scalar impurities (rate 1/tau = 2 Gam, Gam in units of Delta), GRPA phase ladder and impurity ladder, real frequency.
Derivation (own): G = (z~ - D~ t1 - xi t3)^-1, z~/D~ = z/Delta, R = sqrt(z~^2 - D~^2) = r + i Gam, r = sqrt(z^2 - 1) (retarded, Im > 0).  M = t3 A has eigenvalues +-R, so
  Int dxi G(xi+s; +) V G(xi; -) = 2 pi i Sum_{sg=+-} Pi+_{sg} t3 V Pi-_{-sg} t3 / (T - sg s),  T = R+ + R- ,  Pi_sg = (1 + sg (z t3 - i t2)/r)/2 ,
and <1/(T -+ s)>_mu = (1/2Q) ln((T+Q)/(T-Q)).  Impurity ladder: V_tot = V + (Gam/pi) t3 <K[V_tot]> t3 (s-wave).
Sum over Matsubara -> P_ij = (1/2) Int de/(4 pi i) { t(e)[F_RR - F_RA] + t(e+y)[F_RA - F_AA] },  F_ab = tr[t_i Kt_ab[t_j]], plus the quasiclassical static term -1 in P33."""
import numpy as np, core as c
TAU = c.T
T3 = np.diag([1, -1, -1, 1]).astype(complex)
def sup(A, B):
    """4x4 matrix of X -> A X B in the tau basis: out[l,j] = (1/2) tr[t_l A t_j B]; A,B arrays (n,2,2)."""
    o = np.empty((A.shape[0], 4, 4), complex)
    for l in range(4):
        for j in range(4):
            o[:, l, j] = 0.5 * np.einsum('ab,nbc,cd,nda->n', TAU[l], A, TAU[j], B)
    return o
def rr(e, kind, Dl):
    """r(e), Im >= 0 root; kind R or A"""
    a = e * e - Dl * Dl
    r = np.where(a >= 0, np.sign(e) * np.sqrt(np.abs(a)), 1j * np.sqrt(np.abs(a)))
    return r if kind == 'R' else -np.conj(r)
def Pmat(e, kind, Dl):
    r = rr(e, kind, Dl)
    Mh = (e / r)[:, None, None] * TAU[3] + (-1j * Dl / r)[:, None, None] * TAU[2]
    I = np.eye(2)
    return 0.5 * (I + Mh), 0.5 * (I - Mh), r
def F(e, y, Q, Gam, a, b, Dl):
    """returns Kt (n,4,4) and Jt = current row (n,4)."""
    Pp, Pm, r1 = Pmat(e + y, a, Dl); Qp, Qm, r2 = Pmat(e, b, Dl)
    Tt = r1 + r2 + 2j * Gam + 1e-13j
    L = np.log((Tt + Q) / (Tt - Q)) / (2 * Q) if Q > 0 else 1 / Tt
    A1 = Pp @ TAU[3]; B1 = Qm @ TAU[3]        # sg = +
    A2 = Pm @ TAU[3]; B2 = Qp @ TAU[3]        # sg = -
    S1, S2 = sup(A1, B1), sup(A2, B2)
    K = 2j * np.pi * L[:, None, None] * (S1 + S2)
    Ks = 2j * np.pi * ((-1 + Tt * L)[:, None, None] * S1 + (1 - Tt * L)[:, None, None] * S2)   # <s K>
    X = np.eye(4) - (Gam / np.pi) * (T3 @ K)
    Xi = np.linalg.inv(X)
    return K @ Xi, Ks @ Xi
def grid(y, E=3e5, Dl=1.0, n=10, g=1e-7):
    c0 = sorted({Dl, -Dl, Dl - y, -Dl - y, 0.0, -y})
    b = {-E - y / 2, E - y / 2}
    for p in c0:
        b.add(p); t = g
        while t < 4 * (1 + y):
            b |= {p - t, p + t}; t *= 2
    t = 4.0 * (1 + y)
    while t < E:
        b |= {t - y / 2, -t - y / 2}; t *= 1.6
    b = np.array(sorted(x for x in b if -E - y / 2 <= x <= E - y / 2))
    return c.gl_panels(b, n)
def resp(y, Q, Gam, Dl=1.0, E=3e5):
    """P33, P32, P23, D22 = [Pi22(0,0)-Pi22]/2N, D11, current bubbles."""
    e, w = grid(y, E, Dl)
    RR, JRR = F(e, y, Q, Gam, 'R', 'R', Dl); AA, JAA = F(e, y, Q, Gam, 'A', 'A', Dl); RA, JRA = F(e, y, Q, Gam, 'R', 'A', Dl)
    t1 = np.sign(e)[:, None, None]; t2 = np.sign(e + y)[:, None, None]
    M = np.einsum('n,nij->ij', w, t1 * (RR - RA) + t2 * (RA - AA)) * 2 / (4j * np.pi) * 0.5
    J = np.einsum('n,nij->ij', w, t1 * (JRR - JRA) + t2 * (JRA - JAA)) * 2 / (4j * np.pi) * 0.5
    e0, w0 = grid(0.0, E, Dl)
    def st(kind):                                # static q = 0: blocks (t0,t1) rank one, t2 scalar; ladder solved analytically (LU loses the cancellation at the edge)
        Pp, Pm, r = Pmat(e0, kind, Dl); Tt = 2 * r + 2j * Gam
        S = sup(Pp @ TAU[3], Pm @ TAU[3]) + sup(Pm @ TAU[3], Pp @ TAU[3])
        K = 2j * np.pi / Tt[:, None, None] * S
        k2 = K[:, 2, 2]; k1 = K[:, 1, 1]
        return k2 / (1 + (Gam / np.pi) * k2), k1 / (1 + (Gam / np.pi) * k2)
    r2, r1 = st('R'); a2, a1 = st('A')
    M0 = np.zeros((4, 4), complex); pre = 2 / (4j * np.pi) * 0.5
    M0[2, 2] = (w0 * np.sign(e0)) @ (r2 - a2) * pre; M0[1, 1] = (w0 * np.sign(e0)) @ (r1 - a1) * pre
    return M, M0, J
def Pfull(y, Q, Gam, Dl=1.0, E=3e5):
    M, M0, J = resp(y, Q, Gam, Dl, E)
    P33 = M[3, 3] - 1
    if Dl == 0: return P33, P33, M
    D = M0[2, 2] - M[2, 2]
    D1 = M0[2, 2] - M[1, 1]
    Pt = P33 + M[3, 2] * M[2, 3] / D
    return P33, Pt, dict(M=M, D=D, D1=D1, J=J)
