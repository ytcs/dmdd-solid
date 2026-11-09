"""Worked example 13.2 (we:13-exchange) and the adiabatic check of Sect. 13.2.
Prints every number of the worked example and of the adiabatic paragraph of Sect. 13.2 (log: we13_2.log).

Model (a labelled model, no silicon number): a two-band chain of N = 6 cells, lattice constant a = 1, spinless
electrons (the spin is diagonal in both vertices and only doubles a rate). Two orbitals per cell, A at x = 0 and B at
x = a/2, with on-site energies +Delta (A) and -Delta (B), intracell hopping t1 and intercell hopping t2 (the Rice-Mele
form). A twist Phi of the boundary condition shifts every crystal momentum by Phi/N, which lifts the k <-> -k degeneracy
of the ring and lets the frozen-displacement states be followed without degenerate mixing; it changes nothing else.
    Bloch states  psi_{nk}(R, alpha) = N^{-1/2} exp[i k (R + x_alpha)] phi_{alpha n}(k),  k = (2 pi j + Phi)/N.
The lower band is filled (valence v), the upper is empty (conduction c): the ground state is one Slater determinant.
Probe vertex: the density n_e(q) = sum_{R alpha} exp[i q (R + x_alpha)] n_{R alpha} (point orbitals), whose Bloch matrix
elements are rho_{mn}(k, q) of Sect. 3.2.
Phonon: one Einstein branch of energy omega_ph that modulates the on-site splitting, H_ep vertex
    V_Q = g0 sum_R exp(i Q R) (n_{RA} - n_{RB}),  g_{mn}(k, Q) = <psi_{m,k+Q}| V_Q |psi_{nk}>,
i.e. the vertex of eq:A.6-Hep with the zero-point length and the 1/sqrt(N) absorbed into the constant g0 (one mode,
T = 0, emission weight n + 1 = 1). Parameters: Delta = 0.4 eV, t1 = 1.6 eV, t2 = 1.0 eV (direct gap 1.44 eV at k = pi in
the untwisted chain), g0 = 0.2 eV, omega_ph = 0.06 eV (an optical-phonon scale), Phi = 0.3. All are illustrative choices.

(i) Exchange partners. The second-order amplitude between |i> (filled valence band) and |f> = c^dag_{c k'} c_{v k} |i>
(phonon emitted, k' = k + q + Q) is computed by brute force in the Fock space of 12 spin-orbitals and 6 electrons
(924 determinants), with all many-body intermediate states and fermion signs:
    T = sum_m <f|V_Q|m><m|n_q|i>/(E_i + w - E_m) + sum_m <f|n_q|m><m|V_Q|i>/(E_i - E_m - omega_ph),
and split by the kind of intermediate state (paths A, B: an electron in an empty band; C, D: a hole in a filled band).
It is compared with the one-electron sum over all bands p (eq:13.2-M) and with the sum over empty bands only.
(ii) On and off the energy shell: w = E_f - E_i + omega_ph (on shell) and w shifted by +0.10 eV (off shell).
(iii) Adiabatic form: the sum with omega_ph -> 0 against a central finite difference of the frozen-displacement
transition density <psi_{c k'}(u)| n_q |psi_{v k}(u)>, H(u) = H_0 + u (V_Q + V_Q^dag) (a real displacement wave), and
the relative error of the adiabatic form against omega_ph / delta_off for emission and absorption.
Run: python we13_2.py   (numpy only; < 5 s)
"""
import itertools
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "we13_2.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


N, Delta, t1, t2, g0, wph, Phi = 6, 0.4, 1.6, 1.0, 0.2, 0.06, 0.3
xs = np.array([0.0, 0.5])            # orbital positions in the cell
NO = 2 * N                           # orbitals (R, alpha), index 2R + alpha


def H_real(twist=Phi):
    H = np.zeros((NO, NO), complex)
    for R in range(N):
        H[2 * R, 2 * R] = Delta
        H[2 * R + 1, 2 * R + 1] = -Delta
        H[2 * R, 2 * R + 1] += -t1                       # A_R <- B_R
        H[2 * R + 1, 2 * R] += -t1
        Rn = (R + 1) % N
        ph = np.exp(-1j * twist) if R == N - 1 else 1.0  # twisted bond across the boundary
        H[2 * Rn, 2 * R + 1] += -t2 * ph                 # A_{R+1} <- B_R
        H[2 * R + 1, 2 * Rn] += -t2 * np.conj(ph)
    return H


def xpos():
    return np.array([R + xs[al] for R in range(N) for al in range(2)])


X = xpos()


def bloch(kj):
    """Bloch eigenvectors (columns: band 0 = v, 1 = c) at k = (2 pi kj + Phi)/N, in the orbital basis."""
    k = (2 * np.pi * kj + Phi) / N
    h = -t1 * np.exp(1j * k / 2) - t2 * np.exp(-1j * k / 2)
    Hk = np.array([[Delta, h], [np.conj(h), -Delta]])
    e, U = np.linalg.eigh(Hk)
    vecs = np.zeros((NO, 2), complex)
    for n in range(2):
        for R in range(N):
            for al in range(2):
                vecs[2 * R + al, n] = np.exp(1j * k * (R + xs[al])) * U[al, n] / np.sqrt(N)
    return e, vecs


E = np.zeros((N, 2)); PSI = np.zeros((N, NO, 2), complex)
for j in range(N):
    E[j], PSI[j] = bloch(j)
H0 = H_real()
for j in range(N):            # the Bloch states diagonalize the twisted ring
    for n in range(2):
        assert np.allclose(H0 @ PSI[j][:, n], E[j, n] * PSI[j][:, n])


def nq_op(qj):
    q = 2 * np.pi * qj / N
    return np.diag(np.exp(1j * q * X))


def VQ_op(Qj):
    Q = 2 * np.pi * Qj / N
    s = np.array([1.0 if (i % 2 == 0) else -1.0 for i in range(NO)])
    Rv = np.array([i // 2 for i in range(NO)])
    return g0 * np.diag(np.exp(1j * Q * Rv) * s)


def me(op, j1, m, j2, n):
    return PSI[j1 % N][:, m].conj() @ op @ PSI[j2 % N][:, n]


# Kinematics: E_min(q) on the grid
Emin = [min(E[(j + qj) % N, 1] - E[j, 0] for j in range(N)) for qj in range(N)]
out("Model: N = %d, Delta = %.2f, t1 = %.2f, t2 = %.2f eV, g0 = %.2f eV, omega_ph = %.3f eV, twist %.2f" % (N, Delta, t1, t2, g0, wph, Phi))
out("bands: valence %s" % np.round(E[:, 0], 4))
out("       conduction %s" % np.round(E[:, 1], 4))
out("E_min(q) for q = 2 pi j/N, j = 0..5: %s eV" % np.round(Emin, 4))

# choice of final state: q = 2 (2 pi/N), Q chosen so that the pair is low and the zero-phonon line at q closed
qj, Qj, kj = 2, 4, 3      # k' = k + q + Q = k (mod 6): q + Q = 6 = 0 mod N: a vertical final pair at the direct gap
kq, kQ, kp = (kj + qj) % N, (kj + Qj) % N, (kj + qj + Qj) % N
nq = nq_op(qj); VQ = VQ_op(Qj)
Ef_pair = E[kp, 1] - E[kj, 0]
w_on = Ef_pair + wph
out("final state: hole (v, j=%d), electron (c, j=%d), phonon emitted; q = %d, Q = %d (units 2 pi/N)" % (kj, kp, qj, Qj))
out("pair energy %.4f eV, on-shell energy deposited w = %.4f eV, E_min(q) = %.4f eV, E_min(q) - w = %.4f eV"
    % (Ef_pair, w_on, Emin[qj], Emin[qj] - w_on))

v, c = 0, 1


def one_electron(w, wq, sign=+1, bands=(0, 1)):
    """Return dict of the A-form and B-form terms for each intermediate band p (eq:13.2-M).
    sign=+1: emission (phonon energy +wq in the phonon-first denominator); -1: absorption."""
    terms = {}
    for p in bands:
        A = me(VQ, kp, c, kq, p) * me(nq, kq, p, kj, v) / (w - E[kq, p] + E[kj, v])
        B = me(nq, kp, c, kQ, p) * me(VQ, kQ, p, kj, v) / (E[kj, v] - E[kQ, p] - sign * wq)
        terms[p] = (A, B)
    return terms


# ---------- convention of the phonon vertex (R4): phase at the cell origin (used above) or at the orbital ----------
def VQ_op_orbital(Qj):
    Q = 2 * np.pi * Qj / N
    sgn = np.array([1.0 if (i % 2 == 0) else -1.0 for i in range(NO)])
    return g0 * np.diag(np.exp(1j * Q * X) * sgn)


def conv_sum(VQx, bands):
    tot = 0
    for p in bands:
        tot += me(VQx, kp, c, kq, p) * me(nq, kq, p, kj, v) / (w_on - E[kq, p] + E[kj, v])
        tot += me(nq, kp, c, kQ, p) * me(VQx, kQ, p, kj, v) / (E[kj, v] - E[kQ, p] - wph)
    return tot


for lab, VQx in (("cell origin, exp(iQR) (used in the example)", VQ), ("orbital, exp(iQx), Q = -q", VQ_op_orbital(-qj)),
                 ("orbital, exp(iQx), Q = -q + 2 pi", VQ_op_orbital(Qj))):
    full, emp = conv_sum(VQx, (0, 1)), conv_sum(VQx, (1,))
    out("vertex phase at the %s: |M| = %.4f, empty-only |M|^2/|M|^2 = %.3f, factor in the rate %.2f"
        % (lab, abs(full), abs(emp) ** 2 / abs(full) ** 2, abs(full) ** 2 / abs(emp) ** 2))
out("twist Phi = %.2f rad of the boundary condition shifts each k by Phi/N = %.3f rad; untwisted gap %.4f eV"
    % (Phi, Phi / N, 2 * np.sqrt(Delta ** 2 + (t1 - t2) ** 2)))


# ---------- Fock space ----------
orb = [(j, n) for j in range(N) for n in range(2)]
idx = {o: i for i, o in enumerate(orb)}
eps = np.array([E[j, n] for (j, n) in orb])


def single_particle_matrix(op):
    M = np.zeros((NO, NO), complex)
    for a, (ja, na) in enumerate(orb):
        for b, (jb, nb) in enumerate(orb):
            M[a, b] = PSI[ja][:, na].conj() @ op @ PSI[jb][:, nb]
    M[np.abs(M) < 1e-14] = 0
    return M


def apply_cdag_c(a, b, det):
    """c^dag_a c_b |det>; returns (sign, newdet) or None."""
    if not (det >> b) & 1:
        return None
    s = (-1) ** bin(det & ((1 << b) - 1)).count("1")
    d1 = det & ~(1 << b)
    if (d1 >> a) & 1:
        return None
    s *= (-1) ** bin(d1 & ((1 << a) - 1)).count("1")
    return s, d1 | (1 << a)


def apply_op(M, vec):
    outv = {}
    nz = np.argwhere(M != 0)
    for det, amp in vec.items():
        for a, b in nz:
            r = apply_cdag_c(int(a), int(b), int(det))
            if r is None:
                continue
            s, d = r
            outv[d] = outv.get(d, 0) + s * M[a, b] * amp
    return outv


def energy(det):
    return sum(eps[i] for i in range(NO) if (det >> i) & 1)


gs = sum(1 << idx[(j, 0)] for j in range(N))
Ei = energy(gs)
r = apply_cdag_c(idx[(kp, 1)], idx[(kj, 0)], gs)
sf, fdet = r                                              # |f> = c^dag_c c_v |i> = sf |fdet>
Mn, MV = single_particle_matrix(nq), single_particle_matrix(VQ)
ndet = len(list(itertools.combinations(range(NO), N)))


def classify(det):
    """Name the intermediate pair: (electron orbital, hole orbital)."""
    det = int(det); ex = det & ~gs; ho = gs & ~det
    if bin(ex).count("1") != 1:
        return None
    return orb[ex.bit_length() - 1], orb[ho.bit_length() - 1]


def many_body(w, wq, sign=+1):
    """Fock-space second-order amplitude, split by intermediate state kind."""
    parts = {"A": 0j, "B": 0j, "C": 0j, "D": 0j, "other": 0j}
    v1 = apply_op(Mn, {gs: 1.0})                           # density first
    for m, amp in v1.items():
        den = Ei + w - energy(m)
        x = apply_op(MV, {m: amp / den}).get(fdet, 0) * sf
        cl = classify(m)
        key = "other"
        if cl == ((kq, 1), (kj, 0)):
            key = "A"                                      # electron in empty band at k+q, hole (v,k)
        elif cl == ((kp, 1), (kQ, 0)):
            key = "C"                                      # final electron, hole in filled band at k+Q
        parts[key] += x
    v2 = apply_op(MV, {gs: 1.0})                           # phonon first
    for m, amp in v2.items():
        den = Ei - energy(m) - sign * wq
        x = apply_op(Mn, {m: amp / den}).get(fdet, 0) * sf
        cl = classify(m)
        key = "other"
        if cl == ((kQ, 1), (kj, 0)):
            key = "B"
        elif cl == ((kp, 1), (kq, 0)):
            key = "D"
        parts[key] += x
    return parts


def fmt(z):
    return "%+.5f%+.5fi" % (z.real, z.imag)


out("\nFock space: %d determinants of %d orbitals with %d electrons" % (ndet, NO, N))
for label, w in (("ON SHELL", w_on), ("OFF SHELL (w + 0.10 eV)", w_on + 0.10)):
    mb = many_body(w, wph)
    oe = one_electron(w, wph)
    A_c, B_c = oe[c]                                       # empty intermediate band: electron paths
    A_v, B_v = oe[v]                                       # filled intermediate band: Pauli-blocked forms
    total_mb = sum(mb.values())
    full = A_c + B_c + A_v + B_v
    restr = A_c + B_c
    out("\n%s, w = %.4f eV" % (label, w))
    out("  path A (density first, electron in c at k+q):  many-body %s   one-electron %s" % (fmt(mb["A"]), fmt(A_c)))
    out("  path B (phonon first, electron in c at k+Q):   many-body %s   one-electron %s" % (fmt(mb["B"]), fmt(B_c)))
    out("  path C (density first, hole in v at k+Q):      many-body %s   blocked B-form p = v %s" % (fmt(mb["C"]), fmt(B_v)))
    out("  path D (phonon first, hole in v at k+q):       many-body %s   blocked A-form p = v %s" % (fmt(mb["D"]), fmt(A_v)))
    out("  other intermediate states: %s" % fmt(mb["other"]))
    out("  many-body total %s | unrestricted one-electron %s | empty bands only %s" % (fmt(total_mb), fmt(full), fmt(restr)))
    out("  |total|^2 = %.6e, |unrestricted|^2 = %.6e, |empty only|^2 = %.6e, ratio empty-only/total = %.4f"
        % (abs(total_mb) ** 2, abs(full) ** 2, abs(restr) ** 2, abs(restr) ** 2 / abs(total_mb) ** 2))
    out("  |many-body - unrestricted| = %.2e, relative to |many-body| = %.4f; |total| = %.4f"
        % (abs(total_mb - full), abs(total_mb - full) / abs(total_mb), abs(total_mb)))
    if label.startswith("ON"):
        dens = {"A": w - E[kq, c] + E[kj, v], "B": E[kj, v] - E[kQ, c] - wph,
                "C (as B-form)": E[kj, v] - E[kQ, v] - wph, "D (as A-form)": w - E[kq, v] + E[kj, v],
                "C (own)": w - E[kp, c] + E[kQ, v], "D (own)": -(E[kp, c] - E[kq, v] + wph)}
        for k_, d in dens.items():
            out("    denominator %-14s %+.4f eV" % (k_, d))
        out("  numerators: g_cc(k+q,Q) rho_cv(k,q) = %s; rho_cc(k+Q,q) g_cv(k,Q) = %s"
            % (fmt(me(VQ, kp, c, kq, c) * me(nq, kq, c, kj, v)), fmt(me(nq, kp, c, kQ, c) * me(VQ, kQ, c, kj, v))))
        out("              g_cv(k+q,Q) rho_vv(k,q) = %s; rho_cv(k+Q,q) g_vv(k,Q) = %s"
            % (fmt(me(VQ, kp, c, kq, v) * me(nq, kq, v, kj, v)), fmt(me(nq, kp, c, kQ, v) * me(VQ, kQ, v, kj, v))))
        out("  |rho_cv(k,q)|^2 = %.4f, |rho_vv(k,q)|^2 = %.4f" % (abs(me(nq, kq, c, kj, v)) ** 2, abs(me(nq, kq, v, kj, v)) ** 2))
        out("  projection of each term on the total, Re(term/total): A %.3f B %.3f C %.3f D %.3f"
            % tuple((x / full).real for x in (A_c, B_c, B_v, A_v)))
        out("  |C + D| = %.4f, |A + B| = %.4f, |M| = %.4f, |C + D|/|M| = %.3f"
            % (abs(B_v + A_v), abs(A_c + B_c), abs(full), abs(B_v + A_v) / abs(full)))
        dmin = min(abs(d) for d in (dens["A"], dens["B"], dens["C (as B-form)"], dens["D (as A-form)"]))
        out("  smallest |denominator| delta_off = %.4f eV; bound min(E_min(q) - w, E_g - omega) = %.4f eV"
            % (dmin, min(Emin[qj] - w, min(Emin) - wph)))

# ---------- (iii) adiabatic form ----------
out("\nADIABATIC FORM")


def M_amp(wq, sign):
    w = Ef_pair + sign * wq
    oe = one_electron(w, wq, sign)
    return sum(a + b for a, b in oe.values())


Mad = M_amp(0.0, +1)
# finite difference of the frozen-displacement transition density
pert = VQ + VQ.conj().T


def follow(Hu, ref):
    e, U = np.linalg.eigh(Hu)
    i = np.argmax(np.abs(U.conj().T @ ref))
    vec = U[:, i]
    ov = vec.conj() @ ref
    return vec * (ov / abs(ov)), e[i]


def rho_u(u):
    Hu = H0 + u * pert
    psi_c, _ = follow(Hu, PSI[kp][:, c])
    psi_v, _ = follow(Hu, PSI[kj][:, v])
    return psi_c.conj() @ nq @ psi_v


h = 1e-4
fd = (rho_u(h) - rho_u(-h)) / (2 * h)
out("sum over states with omega_ph -> 0: M_ad = %s" % fmt(Mad))
out("finite difference d rho_cv/du (u = +-%.0e): %s" % (h, fmt(fd)))
out("relative difference |FD - M_ad|/|M_ad| = %.2e" % (abs(fd - Mad) / abs(Mad)))
dA = Ef_pair - (E[kq, c] - E[kj, v])          # adiabatic density-first denominator for p = c (zero-phonon detuning)
out("off-shell distances in the adiabatic form: zero-phonon pair at q: %.4f eV; others >= %.4f eV"
    % (abs(dA), min(abs(Ef_pair - (E[kq, v] - E[kj, v])), abs(E[kj, v] - E[kQ, c]), abs(E[kj, v] - E[kQ, v]))))
for wq in (0.015, 0.03, 0.06, 0.12):
    Me, Ma = M_amp(wq, +1), M_amp(wq, -1)
    # delta_off on shell for emission
    w = Ef_pair + wq
    dmin = min(abs(w - E[kq, c] + E[kj, v]), abs(E[kj, v] - E[kQ, c] - wq), abs(E[kj, v] - E[kQ, v] - wq), abs(w - E[kq, v] + E[kj, v]))
    out("omega_ph = %.3f eV: |M+/M_ad - 1| = %.4f, |M-/M_ad - 1| = %.4f, |M+|^2/|M-|^2 = %.4f, omega_ph/delta_off = %.4f (delta_off = %.4f eV)"
        % (wq, abs(Me / Mad - 1), abs(Ma / Mad - 1), abs(Me) ** 2 / abs(Ma) ** 2, wq / dmin, dmin))
out("\nADIABATIC ERROR AGAINST THE WINDOW MARGIN (final pair as above, omega_ph = %.3f eV, emission)" % wph)
for qq in (1, 2, 3):
    QQ = (N - qq) % N
    kq_, kQ_ = (kj + qq) % N, (kj + QQ) % N
    nq_, VQ_ = nq_op(qq), VQ_op(QQ)

    def amp(wq, sign):
        w = Ef_pair + sign * wq
        tot = 0j
        for p in (0, 1):
            tot += me(VQ_, kp, c, kq_, p) * me(nq_, kq_, p, kj, v) / (w - E[kq_, p] + E[kj, v])
            tot += me(nq_, kp, c, kQ_, p) * me(VQ_, kQ_, p, kj, v) / (E[kj, v] - E[kQ_, p] - sign * wq)
        return tot
    w = Ef_pair + wph
    out("q = %d: E_min(q) - w = %.4f eV, |M+/M_ad - 1| = %.4f, |M-/M_ad - 1| = %.4f, omega_ph/(E_min(q) - w) = %.4f"
        % (qq, Emin[qq] - w, abs(amp(wph, 1) / amp(0, 1) - 1), abs(amp(wph, -1) / amp(0, 1) - 1), wph / (Emin[qq] - w)))
LOG.close()
