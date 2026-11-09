"""Worked example 13.6 (we:13-soft) and the checks of App. D.37: the soft acoustic limit of the phonon-assisted amplitude.

Model (labelled; no silicon number): nearly free electrons in a one-dimensional crystal of point-mass ions, solved in
plane waves. Lattice constant a = 3.0 A, one ion per cell of mass 28.0855 u, ionic potential a Gaussian well
v_ion(x) = -V0 exp(-x^2 / 2 s^2), V0 = 2.5 eV, s = 0.5 A (rigid ions: the potential moves with its ion, so the
acoustic sum rule of the vertex, eq:6.2-asr, holds exactly). Spinless electrons, one per cell: band 1 filled (v),
band 2 empty (c). One longitudinal acoustic branch with omega_Q = c_nu |Q|, c_nu = 5.0 km/s (a model value; the
identity of App. D.37 holds for any omega_Q, the limit needs only omega_Q -> 0 linearly). Units: hbar = 1, energies eV,
lengths A; kinetic energy (hbar c)^2 k^2 / (2 m_e c^2) = 3.81 eV A^2 k^2.

The LAB-FRAME vertex is computed directly from the displaced ions, independently of any comoving construction:
    u_j = ell_Q e^{iQ X_j},  dV(x) = -sum_j u_j v_ion'(x - X_j),
    g_mn(k, Q) = < m, k+Q | dV | n, k >,   ell_Q = (2 M_cell omega_Q)^{-1/2}   (eq:A.6-ell, 1/sqrt(N) outside).
Density vertex rho_mn(k, q) = < m, k+q | e^{iqx} | n, k > (eq:3.2-rho), q unfolded.
Amplitude: eq:13.2-M, sum over every band p (40 plane-wave bands), upper sign = emission of -Q,
    omega = eps_{c,k+q+Q} - eps_{vk} +- omega_Q  (on the energy shell by construction).
Checks printed:
 (1) the exact on-shell identity of App. D.37, M[g] = M[g - dg] + i ell (e.q) rho_cv(k, q+Q), with the comoving
     s = i ell (1/2){e^{iQx}, p} and dg_mn = (eps_{m,k+Q} - eps_{nk} +- omega_Q) s_mn, at finite Q;
 (2) the comoving vertex g^c = g - dg vanishes at Q -> 0 for every band pair (acoustic sum rule);
 (3) the lab intraband slope Xi^n = D^n + v^g_n p_nn, with D^n the frozen-strain shift at fixed reduced k
     (finite difference of the strained crystal, a -> a(1+S), ions and potential strained with it);
 (4) the soft limit eq:13.6-soft against the full amplitude, both signs of Q and both emission and absorption, in two
     configurations: B, away from the band extrema (k = 0.80 pi/a, q = 0.30 x 2pi/a), at |Q| = 1e-2, 1e-3, 1e-4 (2pi/a);
     A, both states at band extrema (k = pi/a, q = 2pi/a, Umklapp), at |Q| = 1e-6, 1e-7, 1e-8 (2pi/a), because at an
     extremum the intraband detuning is linear in Q only for |Q| << 2 m* c_nu (printed: conduction curvature mass and
     m* c_nu); the relative deviation falls linearly in |Q| in both;
 (5) the share of the recoil term e.q, of the deformation terms and of the velocity terms in the bracket, and the
     error made if the interband vertices are set to zero near Q = 0 (as codes do for acoustic modes at Q = 0), at the
     middle |Q| of each configuration.
Every number of worked example 13.6 (we:13-soft) and of the one-dimensional check in App. D.37 is printed here.
Run: python we13_6.py  (numpy only; a few seconds). Output: we13_6.log.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "we13_6.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804           # eV A
ME = 510998.95                # eV
KIN = HBARC ** 2 / (2 * ME)   # 3.81 eV A^2
MOVERH2 = ME / HBARC ** 2     # m_e / hbar^2 in eV^-1 A^-2: p_nn (1/A) = MOVERH2 * v_n (eV A) for a local potential
U = 931.49410242e6            # eV
MCELL = 28.0855 * U
A = 3.0
G1 = 2 * np.pi / A
V0, SIG = 2.5, 0.5
CS = 5.0e3 / 299792458.0 * HBARC     # sound speed in eV A (5.0 km/s)
NG = 20
Gs = G1 * np.arange(-NG, NG + 1)


def vhat(K, scale=1.0):
    """Fourier transform int v_ion(x) e^{-iKx} dx of the Gaussian well (ion size scales with the strain)."""
    s = SIG * scale
    return -V0 * s * np.sqrt(2 * np.pi) * np.exp(-(K * s) ** 2 / 2)


def solve(k, S=0.0):
    """Bands at unfolded momentum k (plane waves k + G). S: uniform strain (a -> a(1+S)), k given at fixed reduced k,
    i.e. pass k = k0/(1+S). Returns energies and coefficient matrix (columns = bands)."""
    a = A * (1 + S)
    G = Gs / (1 + S)
    H = np.diag(KIN * (k + G) ** 2)
    dG = G[:, None] - G[None, :]
    # periodic potential of ions at X_j = j a: V_G = vhat(G)/a; ions keep their shape (scale = 1)
    H = H + vhat(dG) / a
    e, C = np.linalg.eigh(H)
    return e, C


def fix_gauge(C_ref, C):
    """Rotate the phase of each column of C so that its overlap with C_ref (same G components) is real positive."""
    ov = np.sum(np.conj(C_ref) * C, axis=0)
    return C * np.exp(-1j * np.angle(ov))[None, :]


def vertex_lab(k, Q, ell):
    """g_mn(k, Q) = <m, k+Q| dV |n, k>, dV components at K = Q + G'' equal to -i K vhat(K) / a, times ell."""
    ek, Ck = solve(k)
    eq, Cq = solve(k + Q)
    dG = Gs[:, None] - Gs[None, :]           # row: G' of the k+Q state, column: G of the k state, K = Q + G' - G
    K = Q + dG
    Vm = -1j * K * vhat(K) / A
    return ell * (np.conj(Cq).T @ Vm @ Ck)


def s_comoving(k, Q, ell):
    """s_mn = i ell <m, k+Q| (1/2){e^{iQx}, p} |n, k> = i ell sum_G c*_m(k+Q; G) c_n(k; G) (k + G + Q/2)."""
    _, Ck = solve(k)
    _, Cq = solve(k + Q)
    return 1j * ell * (np.conj(Cq).T @ (Ck * (k + Gs + Q / 2)[:, None]))


def rho(k, q):
    _, Ck = solve(k)
    _, Cq = solve(k + q)
    return np.conj(Cq).T @ Ck


def amplitude(k, q, Q, sign, g_fn, NB=40, c=1, v=0, Cfin=None, Cini=None):
    """eq:13.2-M with all bands p < NB. g_fn(kk, QQ) returns the vertex matrix g_mn(kk, QQ).
    Gauge: final state (c, k+q+Q) and initial (v, k) as returned by solve(), optionally rotated (Cfin, Cini given
    as the reference columns to align with)."""
    wQ = CS * abs(Q)
    e_k, C_k = solve(k)
    e_kq, C_kq = solve(k + q)
    e_kQ, C_kQ = solve(k + Q)
    e_f, C_f = solve(k + q + Q)
    if Cfin is not None:
        C_f = fix_gauge(Cfin, C_f)
    if Cini is not None:
        C_k = fix_gauge(Cini, C_k)
    w = e_f[c] - e_k[v] + sign * wQ                  # on shell
    # density vertices with the fixed gauges
    rho_pv = np.conj(C_kq).T @ C_k                    # <p, k+q| e^{iqx} | v, k>
    rho_cp = np.conj(C_f).T @ C_kQ                    # <c, k+q+Q| e^{iqx} | p, k+Q>
    gA = g_fn(k + q, Q, C_kq, C_f)                    # <m, k+q+Q| . |p, k+q>
    gB = g_fn(k, Q, C_k, C_kQ)                        # <p, k+Q| . |v, k>
    tot = 0j
    for p in range(NB):
        tot += gA[c, p] * rho_pv[p, v] / (w - e_kq[p] + e_k[v])
        tot += rho_cp[c, p] * gB[p, v] / (e_k[v] - e_kQ[p] - sign * wQ)
    return tot, w, e_f[c] - e_k[v]


def make_g_lab(ell):
    def g(kk, QQ, Cin, Cout):
        dG = Gs[:, None] - Gs[None, :]
        K = QQ + dG
        Vm = -1j * K * vhat(K) / A
        return ell * (np.conj(Cout).T @ Vm @ Cin)
    return g


def make_s(ell):
    def s(kk, QQ, Cin, Cout):
        return 1j * ell * (np.conj(Cout).T @ (Cin * (kk + Gs + QQ / 2)[:, None]))
    return s


def make_g_comoving(ell, sign):
    glab, sop = make_g_lab(ell), make_s(ell)
    wQ_of = lambda QQ: CS * abs(QQ)

    def g(kk, QQ, Cin, Cout):
        e_in = solve(kk)[0]
        e_out = solve(kk + QQ)[0]
        dE = e_out[:, None] - e_in[None, :] + sign * wQ_of(QQ)
        return glab(kk, QQ, Cin, Cout) - dE * sop(kk, QQ, Cin, Cout)
    return g


out("Model: a = %.2f A, V0 = %.2f eV, s = %.2f A, M = 28.0855 u, c_nu = %.5f eV A (5.0 km/s), %d plane waves"
    % (A, V0, SIG, CS, len(Gs)))
eZB, _ = solve(np.pi / A)
e0, _ = solve(0.0)
out("  gap at the zone boundary: %.4f eV; band 1 width %.3f eV; band 2 bottom %.3f eV above band-1 top"
    % (eZB[1] - eZB[0], eZB[0] - e0[0], eZB[1] - eZB[0]))

# --- helpers -------------------------------------------------------------------------------------------------------
def bandderiv(kk, n, h=1e-5):
    return (solve(kk + h)[0][n] - solve(kk - h)[0][n]) / (2 * h)


def pnn(kk, n):
    e, C = solve(kk)
    return float(np.real(np.sum(np.abs(C[:, n]) ** 2 * (kk + Gs))))


def Dstrain(kred, n, h=1e-5):
    """Frozen-strain shift d eps_n / dS at fixed reduced k (k = kred/(1+S)), ions strained with the lattice."""
    return (solve(kred / (1 + h), h)[0][n] - solve(kred / (1 - h), -h)[0][n]) / (2 * h)


def ell_of(Q):
    return HBARC / np.sqrt(2 * MCELL * CS * abs(Q))        # A; (2 M omega_Q)^{-1/2} with hbar c restored


def g_intra_only(ell):
    glab = make_g_lab(ell)

    def g(kk, QQ, Cin, Cout):
        return np.diag(np.diag(glab(kk, QQ, Cin, Cout)))
    return g


v, c = 0, 1
CONFIGS = (("B: away from the extrema (k = 0.80 pi/a, q = 0.30 x 2pi/a)", 0.80 * np.pi / A, 0.30 * G1,
            (1e-2, 1e-3, 1e-4)),
           ("A: both states at band extrema (k = pi/a, q = 2pi/a, Umklapp)", np.pi / A, G1, (1e-6, 1e-7, 1e-8)))
for title, k0, q0, QLIST in CONFIGS:
    out("")
    out("Configuration " + title)
    e_k, C_k0 = solve(k0)
    e_kq, C_kq0 = solve(k0 + q0)
    rho0 = (np.conj(C_kq0).T @ C_k0)[c, v]
    vv, vc = bandderiv(k0, v), bandderiv(k0 + q0, c)
    pv, pc = pnn(k0, v), pnn(k0 + q0, c)
    Dv, Dc = Dstrain(k0, v), Dstrain(k0 + q0, c)
    out("  E_cv(k, q) = %.4f eV; |rho_cv(k, q)| = %.4f" % (e_kq[c] - e_k[v], abs(rho0)))
    out("  v^g_v = %.4f, v^g_c = %.4f eV A (%.1f, %.1f c_nu); p_vv = %.5f, p_cc = %.5f 1/A (m v^g: %.5f, %.5f)"
        % (vv, vc, vv / CS, vc / CS, pv, pc, MOVERH2 * vv, MOVERH2 * vc))
    curv = (solve(k0 + q0 + 1e-3)[0][c] + solve(k0 + q0 - 1e-3)[0][c] - 2 * e_kq[c]) / 1e-6
    mst = 2 / curv
    out("  conduction curvature mass m*_c = %.4f m_e; Cherenkov scale m*_c c_nu = %.2e 1/A = %.1e x 2pi/a; "
        "band velocities linear over Q only for |Q| << |v^g|/(d^2 eps/dk^2) or, at an extremum, |Q| << 2 m* c_nu"
        % (mst / MOVERH2, mst * CS, mst * CS / G1))
    out("  frozen-strain D^v = %.4f eV, D^c = %.4f eV; |D^c - D^v|/c_nu = %.1f 1/A against q = %.4f 1/A"
        % (Dv, Dc, abs(Dc - Dv) / CS, q0))
    # (3) lab intraband slope
    for n, kk in ((v, k0), (c, k0 + q0)):
        Q = 1e-5 * G1
        ell = ell_of(Q)
        e_in, C_in = solve(kk)
        e_out, C_out = fix_gauge(C_in, solve(kk + Q)[1]), None
        gl = make_g_lab(ell)(kk, Q, C_in, e_out)
        Xi = (gl[n, n] / (1j * ell * Q)).real
        Dn, vn, pn = Dstrain(kk, n), bandderiv(kk, n), pnn(kk, n)
        out("  (3) band %d: lab slope Xi = %.5f eV; D^n + v^g_n p_nn = %.5f + %.5f = %.5f eV"
            % (n + 1, Xi, Dn, vn * pn, Dn + vn * pn))
    # (2) comoving vertex vanishes at Q = 0
    for Qf in (1e-2, 1e-4):
        Q = Qf * G1
        ell = ell_of(Q)
        e_in, C_in = solve(k0)
        e_out, C_out = solve(k0 + Q)
        gl = make_g_lab(ell)(k0, Q, C_in, C_out)[:6, :6]
        gc = make_g_comoving(ell, +1)(k0, Q, C_in, C_out)[:6, :6]
        out("  (2) |Q| = %.0e x 2pi/a: max |g_lab| = %.3e eV (interband, rigid translation); max |g^c| = %.3e eV "
            "= %.2f eV x ell|Q|" % (Qf, np.abs(gl).max(), np.abs(gc).max(), np.abs(gc).max() / (ell * abs(Q))))
    # (1) exact identity
    for Qf, sign in ((0.10, +1), (-0.25, -1)):
        Q = Qf * G1
        ell = ell_of(Q)
        Mlab, w, _ = amplitude(k0, q0, Q, sign, make_g_lab(ell))
        Mcom, _, _ = amplitude(k0, q0, Q, sign, make_g_comoving(ell, sign))
        e_f, C_f = solve(k0 + q0 + Q)
        contact = 1j * ell * q0 * (np.conj(C_f).T @ C_k0)[c, v]
        out("  (1) Q = %+.2f x 2pi/a, %s: |M| = %.4e; |M - M[g^c] - contact| / |M| = %.1e; |contact|/|M| = %.3f"
            % (Qf, "emission" if sign > 0 else "absorption", abs(Mlab), abs(Mlab - Mcom - contact) / abs(Mlab),
               abs(contact) / abs(Mlab)))
    # (4) soft limit
    for sign in (+1, -1):
        for Qh in (+1, -1):
            Kd = (Qh * Dc) / (Qh * vc + sign * CS) - (Qh * Dv) / (Qh * vv + sign * CS)
            Kv = (-sign * CS * pc) / (Qh * vc + sign * CS) - (-sign * CS * pv) / (Qh * vv + sign * CS)
            K = q0 + Kd + Kv
            devs = []
            for Qf in QLIST:
                Q = Qh * Qf * G1
                ell = ell_of(Q)
                M, w, _ = amplitude(k0, q0, Q, sign, make_g_lab(ell), Cfin=C_kq0, Cini=C_k0)
                devs.append(abs(M / (1j * ell * rho0 * K) - 1))
            out("  (4) %s, Q %s: K = %+.4f 1/A [recoil %+.4f, deformation %+.4f, velocity %+.2e]; "
                "|M/M_soft - 1| = %.1e, %.1e, %.1e"
                % ("emission  " if sign > 0 else "absorption", "+" if Qh > 0 else "-", K, q0, Kd, Kv, *devs))
    # (5) codes that zero the interband acoustic vertex near Q = 0
    Q = QLIST[1] * G1
    ell = ell_of(Q)
    M, _, _ = amplitude(k0, q0, Q, +1, make_g_lab(ell), Cfin=C_kq0, Cini=C_k0)
    Mi, _, _ = amplitude(k0, q0, Q, +1, g_intra_only(ell), Cfin=C_kq0, Cini=C_k0)
    K = q0 + (Dc - CS * pc) / (vc + CS) - (Dv - CS * pv) / (vv + CS)
    out("  (5) interband vertices zeroed (emission, Q = +%.0e x 2pi/a)" % QLIST[1] + ": |M_intra/M - 1| = %.3f; "
        "predicted |q - p_cc + p_vv|/|K| = %.3f; |M_intra|^2/|M|^2 = %.3f" % (abs(Mi / M - 1), abs((q0 - pc + pv) / K),
                                                                          abs(Mi) ** 2 / abs(M) ** 2))
    Qm = -QLIST[1] * G1
    ellm = ell_of(Qm)
    M, _, _ = amplitude(k0, q0, Qm, +1, make_g_lab(ellm), Cfin=C_kq0, Cini=C_k0)
    Mi, _, _ = amplitude(k0, q0, Qm, +1, g_intra_only(ellm), Cfin=C_kq0, Cini=C_k0)
    out("  (5) interband vertices zeroed (emission, Q = -%.0e x 2pi/a)" % QLIST[1] + ": |M_intra|^2/|M|^2 = %.3f"
        % (abs(Mi) ** 2 / abs(M) ** 2))
    out("  (6) per band, velocity / deformation term c_nu |p_nn| / |D^n|: valence %.2e, conduction %.2e"
        % (CS * abs(pv) / abs(Dv), CS * abs(pc) / abs(Dc)))
out("")
out("Deviations in (4) are at the three |Q| of each configuration: linear in |Q|, the O(|Q|) relative correction of D.37.")
LOG.close()
