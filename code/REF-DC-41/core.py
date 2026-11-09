"""REF-DC-41 independent core.  Delta = 1.  Nothing is imported from code/DC-41.
Direct path: Nambu bubble from PROJECTORS (not spinors), no delta-function roots, complex frequency z = y + i g:
  chi_ij(z) = Sum_k { tr[t_i P+(xi') t_j P-(xi)]/(z - W) - tr[t_i P-(xi') t_j P+(xi)]/(z + W) },  h = xi t3 + D t1, P+- = (1 +- h/E)/2
derived from T Sum_w tr[t_i G(k+q,iw+iv) t_j G(k,iw)], G = (iw - h)^-1.  Vertices t0 (carries s for the current), t1 amplitude, t2 phase, t3 density.
Closed path: my own evaluation of (DC41-1) with f(kappa) analytic in the cut plane (complex z allowed)."""
import numpy as np
T = [np.eye(2, dtype=complex), np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]

def proj(xi, D=1.0):
    E = np.sqrt(xi * xi + D * D)
    h = xi[:, None, None] * T[3] + D * T[1]
    return 0.5 * (np.eye(2) + h / E[:, None, None]), 0.5 * (np.eye(2) - h / E[:, None, None]), E

def gl_panels(b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    b = np.asarray(b); a, c = b[:-1, None], b[1:, None]
    return (0.5 * (c - a) * x + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * w).ravel()

def eta_grid(s, y, g, n=16):
    """break points on eta in [-L, L]: sinh grading about 0, +-s/2, and the root(s) W(eta) = y."""
    L = 1e5 * max(1, abs(s), abs(y))
    c = [0.0, abs(s) / 2]
    if y > np.sqrt(s * s + 4):                # W(eta) = y at eta0 ; W^2 = ...  solved by bisection-free closed form
        # W = y  <=>  eta^2 = (y^2-s^2)(y^2-4)/(4 y^2) * ... derive: E'+E = y, E'^2-E^2 = 2 eta s*... => E'-E = 2 eta s / y
        # E' = (y + 2 eta s/y)/2 ; E'^2 = (eta+s/2)^2+1 => eta^2 = (y^2/4 - s^2/4 - 1) / (1 - s^2/y^2)
        c.append(np.sqrt((y * y / 4 - s * s / 4 - 1) / (1 - s * s / y / y)))
    b = {0.0, L}
    h0 = max(g, 1e-3) / 8
    for p in c:
        b.add(p)
        t = h0
        while t < L:
            for v in (p - t, p + t):
                if 0 < v < L: b.add(v)
            t *= 1.5
    b = np.array(sorted(b))
    pos = b
    return np.concatenate([-pos[::-1][:-1], pos])

def bubble_fixed_s(z, s, pairs, n=16, D=1.0, wfun=None):
    """Int d xi of the bubble bracket at fixed s, xi = eta - s/2, xi' = eta + s/2.  pairs: list of (i,j).  wfun: optional DOS weight on eta (w(eta))."""
    b = eta_grid(s, z.real, z.imag, n)
    eta, w = gl_panels(b, n)
    if wfun is not None: w = w * wfun(eta)
    Pp, Pm, E = proj(eta - s / 2, D); Pp2, Pm2, E2 = proj(eta + s / 2, D)
    W = E + E2
    out = {}
    for (i, j) in pairs:
        A = np.einsum('ab,nbc,cd,nda->n', T[i], Pp2, T[j], Pm)
        B = np.einsum('ab,nbc,cd,nda->n', T[i], Pm2, T[j], Pp)
        out[(i, j)] = w @ (A / (z - W) - B / (z + W))
    return out

def s_nodes(y, Q, n=10, g=0.0):
    b = [0.0, Q]
    if y > 2:
        ss = np.sqrt(y * y - 4); b.append(ss)
        h = max(g, 1e-3)
        t = h
        while t < 2 * ss + 2:
            b += [ss - t, ss + t]; t *= 1.6
    b.append(y)
    t = 0.01
    while t < Q:
        b.append(t); t *= 1.6
    b = np.array(sorted({x for x in b if 0 <= x <= Q}))
    return gl_panels(b, n)

def direct(z, Q, n=16, ns=10, D=1.0):
    """Returns P33, P32, P23, Dn = [Pi22(0,0)-Pi22]/2N, plus P31, P21, and current bubbles Pj3, Pj2 (vertex s t0) ; average over mu in [-1,1]."""
    s, ws = s_nodes(z.real, Q, ns, z.imag); ws = ws / Q
    acc = {}
    pairs = [(3, 3), (3, 2), (2, 3), (2, 2), (3, 1), (2, 1), (0, 3), (0, 2)]
    for sg in (1, -1):
        for si, wi in zip(s, ws):
            sv = sg * si
            o = bubble_fixed_s(z, sv, pairs, n, D)
            # Pi22(0,0) at the same cutoff on the same nodes: integrand -2/(2E(eta)) x 2 traces ...  computed by same routine at z=0,s=0 on eta grid of THIS s
            b = eta_grid(sv, z.real, z.imag, n); eta, w = gl_panels(b, n)
            o22 = w @ (-2.0 / (2 * np.sqrt(eta ** 2 + D * D)) * 2 / 2 * 2 / 2) if False else None
            Pp, Pm, E = proj(eta, D)
            A = np.einsum('ab,nbc,cd,nda->n', T[2], Pp, T[2], Pm)
            B = np.einsum('ab,nbc,cd,nda->n', T[2], Pm, T[2], Pp)
            o0 = w @ (A / (0 - 2 * E) - B / (0 + 2 * E))
            for k in pairs:
                val = o[k] * (sv if k[0] == 0 else 1.0)
                acc[k] = acc.get(k, 0) + 0.5 * wi * val
            acc['d22'] = acc.get('d22', 0) + 0.5 * wi * (o0 - o[(2, 2)])
    h = lambda k: 0.5 * acc[k]
    return dict(P33=h((3, 3)), P32=h((3, 2)), P23=h((2, 3)), Dn=0.5 * acc['d22'], P31=h((3, 1)), P21=h((2, 1)), Pj3=h((0, 3)), Pj2=h((0, 2)))

# closed form, complex z
def f_of(k):
    k = np.asarray(k, complex)
    r = np.sqrt(k)
    small = np.abs(k) < 1e-6
    rs = np.where(small, 1.0, r)
    out = -np.arcsin(rs) / (rs * np.sqrt(1 - k + 0j))
    return np.where(small, -(1 + 2 * k / 3), out)

def closed_avgs(z, Q, ns=14, nodes=None):
    """<f>, <u^2 f>, <(1+f)/u^2>... for Im z >= 0; for real z>2 pass z + i tiny.  retarded branch: kappa = (z^2 - s^2)/4 with Im kappa >= 0."""
    if nodes is None:
        s, w = s_nodes(z.real, Q, ns, z.imag); w = w / Q
    else:
        s, w = nodes
    u2 = z * z - s * s
    k = u2 / 4
    if abs(z.imag) == 0: k = k + 1e-300j
    f = f_of(k)
    # branch check: for k real > 1 approached from Im k>0 : arcsin(r) = pi/2 + i arccosh(r) in numpy? enforced below by sign test in tests
    return w @ f, w @ (u2 * f), w @ ((s * s + z * z * f) / u2)

def closed(z, Q, **kw):
    F, UF, P33 = closed_avgs(z, Q, **kw)
    return P33, P33 - z * z * F * F / UF, F, UF
def lindhard(z, Q):
    x = z / Q
    return -1 + 0.5 * x * np.log((x + 1) / (x - 1))
