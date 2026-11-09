"""Direction dependence of the nuclear response for Sect. 11.7: silicon (coherent terms) and sapphire, 2H-SiC (incoherent part with
site tensors).  Run directly: writes lat11_7.npz and prints every number quoted (log: lat11_7.log).  Natural units, eV.

(1) Silicon, cubic sites.  The incoherent part is exactly isotropic (B_kappa = <u_x^2> 1 and q-projected DOS = g_ph/3); the check
    prints the site tensors of the published DarkELF table (darkelf_Si_pDoS_anisotropic.dat) and of GaAs.
    The anisotropy is in the coherent terms (Sect. 11.3):
    * one phonon, all six branches and Umklapp (q unreduced), from the PBE force constants of Sect. 5.2 (figscripts/ch05/si_ifc.py):
        r1(q, qhat) = sum_nu |sum_k e^{i q.tau_k} qhat.e*_k nu(q)|^2 / (2 M omega) / (n_at <u_x^2>)     (as limit11_3a.py, per direction)
    * two phonons, real-space pair sum of eq:11.3-weight per direction (no direction average), B_kk'(dR) at T = 0 on a 32^3 grid
      (mph11.py), pairs |d| <= 20 A (checked against 30 A at three q):  r2 = 1 + (1/n_at) sum_pairs cos(q.d) [qhat.B.qhat/<u_x^2>]^2.
    Cubic-harmonic components s_{n,l}(q) = int dOmega Y^c_l(qhat) r_n(q, qhat) on a Gauss-Legendre x uniform-phi grid (ND below);
    s_{n,0} = sqrt(4 pi)(1 + delta^coh_n).  Continuum check (long wavelength): f(qhat) = sum_nu (qhat.e_nu)^2 / c_nu(qhat) with the
    elastic constants of Sect. 11.1 (phon11.py), the quantity App. E.17 quotes (l = 4 at 2.2 % of the isotropic part).
(2) Sapphire (Al2O3) and 2H-SiC: per-site density-of-states tensors D^{ij}_kappa(omega) of Stratman and Lin, arXiv:2411.03433,
    Eqs. (20)-(23), from the public DarkELF data (github.com/tongylin/DarkELF, commit 2f01cd5501d8f9c0dfdc3a011973dab9da718498,
    data/Al2O3/Al2O3_pDoS_anisotropic.dat, data/SiC/SiC_pDoS_anisotropic.dat; copied here as darkelf_*.dat): projected DOS along
    x, y, z, x+y, x+z, y+z for each inequivalent site, z along the c axis; sapphire: Al (4 equivalent sites) and three O classes
    (2 sites each); 2H-SiC: Si and C (2 sites each).  Phonons from first-principles force constants (sapphire: those distributed with
    phonopy; 2H-SiC: the DFT calculation of Griffin et al., arXiv:2008.08560), as stated in 2411.03433 Sect. II and App. C.
    D^{xy} = D(x+y) - (D^{xx} + D^{yy})/2 (their Eq. (23)) etc.  Projected DOS D^{qhat} = qhat.D.qhat; at T = 0
       2W_kappa(q) = q^2 int dw D^{qhat}_kappa(w) / (2 M_kappa w)      (eq:5.6-W; their Eq. (19)),
       P^kappa_1(qhat, w) = D^{qhat}_kappa(w)/w normalized, P_n its n-fold convolution (eq:11.3-inc; their Eqs. (24)-(25)).
    Coupling c_kappa = A_kappa (equal couplings to protons and neutrons; Al 27, O 16, Si 28, C 12; masses 26.98, 16.00, 28.09, 12.01 u).
    omega-integrated response above a threshold w_th:  Sigma(q, qhat) = sum_kappa mult A^2 e^{-2W} sum_{n>=1} (2W)^n/n! int_{w_th} P_n.
    Rate at fixed wind direction vhat (heavy mediator):
       R(vhat) proportional to int q dq int dOmega_q fhat(v_min + v_E qhat.vhat) Sigma(q, qhat)       (eq:11.7-rate before the expansion)
    with v_min = q/2m_chi + wbar(q)/q, wbar(q) the mean energy deposited above threshold at q (direction-averaged first moment
    over Sigma): the omega/q term at first order (it is not small at the lowest q, where the rate is small).
    computed on a direction grid with c along z.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import aniso11 as AN  # noqa: E402
import phon11 as P  # noqa: E402

U_EV = 931.494e6
HBARC = 1973.269804             # eV A
C_KMS = AN.C_KMS


# ------------------------------------------------------------------------------------------------- site tensors (DarkELF)
def load_tensor(fname, classes):
    d = np.loadtxt(os.path.join(HERE, fname))
    w = d[:, 0]
    out = []
    for i, (name, mult, A, M) in enumerate(classes):
        p = d[:, 1 + 6 * i:7 + 6 * i]
        D = np.zeros((len(w), 3, 3))
        D[:, 0, 0], D[:, 1, 1], D[:, 2, 2] = p[:, 0], p[:, 1], p[:, 2]
        D[:, 0, 1] = D[:, 1, 0] = p[:, 3] - (p[:, 0] + p[:, 1]) / 2
        D[:, 0, 2] = D[:, 2, 0] = p[:, 4] - (p[:, 0] + p[:, 2]) / 2
        D[:, 1, 2] = D[:, 2, 1] = p[:, 5] - (p[:, 1] + p[:, 2]) / 2
        out.append(dict(name=name, mult=mult, A=A, M=M * U_EV, D=D))
    return w, out


SAPPHIRE = [("Al", 4, 27, 26.98), ("O_a", 2, 16, 16.00), ("O_b", 2, 16, 16.00), ("O_c", 2, 16, 16.00)]
SIC2H = [("Si", 2, 28, 28.09), ("C", 2, 12, 12.01)]


class Incoherent:
    """Anisotropic incoherent response (T = 0) of a crystal from site tensors, on a fine uniform omega grid."""

    def __init__(self, fname, classes, dw=2.5e-4, nmax=14):
        w, sites = load_tensor(fname, classes)
        self.sites = sites
        self.dw = dw
        self.wg = np.arange(dw / 2, w.max() * nmax + dw, dw)
        self.nmax = nmax
        pos = w > 1e-5
        for s in sites:
            # integrand D(w)/w on the fine grid (linear interpolation of the table, zero outside)
            Dw = np.zeros((len(self.wg), 3, 3))
            for i in range(3):
                for j in range(3):
                    Dw[:, i, j] = np.interp(self.wg, w[pos], s["D"][pos, i, j] / w[pos], left=0, right=0)
            s["Dw"] = Dw
            s["B"] = Dw.sum(0) * dw / (2 * s["M"])         # eV^-2: 2W = q.B.q (T = 0)

    def weights(self, q, qh, wth, moment=False):
        """Sigma(q, qhat) per cell [arbitrary units: sum mult A^2 ...], for arrays q (nq,) and qh (nd, 3). Returns (nq, nd).
        With moment=True also returns the first energy moment above threshold, int_{w_th} w S (same shape), for the w/q part
        of v_min."""
        out = np.zeros((len(q), len(qh)))
        mom = np.zeros((len(q), len(qh)))
        nfft = 1 << int(np.ceil(np.log2(2 * len(self.wg))))
        mask = self.wg >= wth
        for s in self.sites:
            Dq = np.einsum("di,wij,dj->dw", qh, s["Dw"], qh)          # D^{qhat}(w)/w  (nd, nw)
            b = np.einsum("di,ij,dj->d", qh, s["B"], qh)               # 2W/q^2
            p1 = Dq / (Dq.sum(1, keepdims=True) * self.dw)             # normalized P_1
            F1 = np.fft.rfft(p1 * self.dw, nfft, axis=1)
            frac = np.zeros((self.nmax + 1, len(qh)))                  # int_{w_th} P_n
            fmom = np.zeros((self.nmax + 1, len(qh)))                  # int_{w_th} w P_n
            Fn = np.ones_like(F1)
            for n in range(1, self.nmax + 1):
                Fn = Fn * F1
                pn = np.fft.irfft(Fn, nfft, axis=1)[:, :len(self.wg)]
                frac[n] = pn[:, mask].sum(1)
                fmom[n] = (pn[:, mask] * self.wg[mask]).sum(1)
            x = q[:, None]**2 * b[None, :]                              # 2W (nq, nd)
            tot = np.zeros_like(x)
            tm = np.zeros_like(x)
            term = np.exp(-x)
            for n in range(1, self.nmax + 1):
                term = term * x / n
                tot += term * frac[n][None, :]
                tm += term * fmom[n][None, :]
            out += s["mult"] * s["A"]**2 * tot
            mom += s["mult"] * s["A"]**2 * tm
        return (out, mom) if moment else out

    def single(self, q, qh, wth, moment=False):
        """n = 1 term only (optionally with its first energy moment above threshold)."""
        out = np.zeros((len(q), len(qh)))
        mom = np.zeros((len(q), len(qh)))
        mask = self.wg >= wth
        for s in self.sites:
            Dq = np.einsum("di,wij,dj->dw", qh, s["Dw"], qh)
            b = np.einsum("di,ij,dj->d", qh, s["B"], qh)
            frac = Dq[:, mask].sum(1) / Dq.sum(1)
            fm = (Dq[:, mask] * self.wg[mask]).sum(1) / Dq.sum(1)
            x = q[:, None]**2 * b[None, :]
            out += s["mult"] * s["A"]**2 * x * np.exp(-x) * frac[None, :]
            mom += s["mult"] * s["A"]**2 * x * np.exp(-x) * fm[None, :]
        return (out, mom) if moment else out


def rate_vs_direction(sig, q, qh, wq, m_chi, vhats, wbar=None):
    """R(vhat) ~ int q dq int dOmega fhat(v_min + v_E qhat.vhat) Sigma(q, qhat); q (nq,) uniform in log; returns (nv,).
    v_min = q/2m + wbar(q)/q, wbar = mean energy deposited above threshold at q (direction-averaged; 0 if None)."""
    vstar = (q / (2 * m_chi) + (0 if wbar is None else wbar / q)) * C_KMS   # km/s
    lq = np.log(q)
    dlq = np.gradient(lq)
    out = []
    for vh in vhats:
        x = qh @ vh
        K = AN.fhat(vstar[:, None] + AN.VE * x[None, :])  # (nq, nd)
        out.append(np.sum((q**2 * dlq)[:, None] * wq[None, :] * K * sig))
    return np.array(out)


def proj_real(sig, qh, wq, lmax):
    """Real-Y_lm coefficients of sig(q, qhat) for l <= lmax (even), returns dict l -> (2l+1, nq)."""
    return {l: np.einsum("md,qd,d->mq", AN.ylm_real(l, qh), sig, wq) for l in range(0, lmax + 1, 2)}


def recon(coef, n, lmax):
    tot = 0.0
    for l in range(0, lmax + 1, 2):
        tot = tot + np.einsum("mq,m->q", coef[l], AN.ylm_real(l, n))
    return tot


# ------------------------------------------------------------------------------------------------- silicon coherent terms
def si_one_phonon(q_keV, qh):
    import si_ifc
    import mph11 as MP
    qA = q_keV * 1e3 / MP.HBARC
    out = np.zeros(len(qh))
    for c in np.array_split(np.arange(len(qh)), max(1, len(qh) // 6000)):
        qv = qA * qh[c] / (2 * np.pi / MP.A_ANG)
        w, ev = si_ifc.phonons(qv)
        w = np.maximum(w, 1e-3) * 1e-3
        ph = np.exp(2j * np.pi * (qv @ MP.TAU.T))
        amp = np.zeros((len(c), 6), complex)
        for k in range(2):
            amp += ph[:, k:k + 1] * np.einsum("ni,nij->nj", qh[c], np.conj(ev[:, 3 * k:3 * k + 3, :]))
        out[c] = (np.abs(amp)**2 / (2 * MP.M_SI * w)).sum(1) * MP.HBARC**2
    return out / (MP.NAT * 2.4499e-3)


def si_pairs(rmax):
    import mph11 as MP
    cache = os.path.join(HERE, "lat11_7_B32.npz")
    if os.path.exists(cache):
        z = np.load(cache)
        d, Bp = z["d"], z["Bp"]
    else:
        Bd = MP.B_tensor(32)
        ux2 = Bd["B"][0, 0, 0, 0, 0].real[0, 0]
        d, kk, Bp = MP.pair_table(Bd, rmax=30.0)
        Bp = Bp.real / ux2
        np.savez(cache, d=d, Bp=Bp, ux2=ux2)
    r = np.linalg.norm(d, axis=1)
    sel = (r > 1e-6) & (r <= rmax)
    return d[sel], Bp[sel]


def si_two_phonon(q_keV, qh, d, Bp):
    qA = q_keV * 1e3 / HBARC
    out = np.ones(len(qh))
    for c in np.array_split(np.arange(len(qh)), max(1, len(qh) // 256)):
        b = np.einsum("da,pab,db->dp", qh[c], Bp, qh[c])
        ph = np.cos(qA * (qh[c] @ d.T))
        out[c] += (ph * b**2).sum(1) / 2
    return out


def cubic_components(f, qh, wq, ls=(0, 4, 6, 8)):
    return {l: np.sum(wq * AN.ycub(l, qh) * f, axis=-1) for l in ls}


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    # ---- (0) site tensors of the cubic crystals: isotropy check
    for fn, cl in (("darkelf_Si_pDoS_anisotropic.dat", [("Si", 2, 28, 28.09)]),
                   ("darkelf_GaAs_pDoS_anisotropic.dat", [("Ga", 1, 69, 69.72), ("As", 1, 75, 74.92)])):
        inc = Incoherent(fn, cl)
        for s in inc.sites:
            B = s["B"] * HBARC**2
            print("%s %s: B (A^2) diag %s, max off-diag %.1e, (max-min)/mean of diag %.1e"
                  % (fn[7:11], s["name"], np.diag(B), np.abs(B - np.diag(np.diag(B))).max(), np.ptp(np.diag(B)) / np.diag(B).mean()))
    # ---- (1a) continuum estimate, Si
    av = P.averages("Si")
    fcont = (av["proj2"] / av["c"]).sum(1)
    qh0, wq0 = AN.sphere_grid(48, 96)
    c, ev = P.christoffel(P.ctensor(*P.MATS["Si"][:3]), P.density("Si"), qh0)
    fc = (np.einsum("ni,nik->nk", qh0, ev)**2 / c).sum(1)
    cc = cubic_components(fc, qh0, wq0)
    print("continuum (Si elastic constants): S4/S0 = %+.4f, S6/S0 = %+.5f, S8/S0 = %+.5f; f[100]/fbar = %.4f, f[111]/fbar = %.4f"
          % (cc[4] / cc[0], cc[6] / cc[0], cc[8] / cc[0],
             (np.einsum("i,ik->k", [1, 0, 0], P.christoffel(P.ctensor(*P.MATS["Si"][:3]), P.density("Si"), np.array([[1, 0, 0.]]))[1][0])**2
              / P.christoffel(P.ctensor(*P.MATS["Si"][:3]), P.density("Si"), np.array([[1, 0, 0.]]))[0][0]).sum() / (cc[0] / np.sqrt(4 * np.pi)),
             (np.einsum("i,ik->k", np.ones(3) / np.sqrt(3), P.christoffel(P.ctensor(*P.MATS["Si"][:3]), P.density("Si"), np.ones((1, 3)) / np.sqrt(3))[1][0])**2
              / P.christoffel(P.ctensor(*P.MATS["Si"][:3]), P.density("Si"), np.ones((1, 3)) / np.sqrt(3))[0][0]).sum() / (cc[0] / np.sqrt(4 * np.pi))))
    # ---- (1b) silicon coherent one- and two-phonon components
    import mph11 as MP
    qbz = MP.QBZ_KEV
    qgrid = np.geomspace(0.1 * qbz, 25 * qbz, 160)
    ND = (64, 128)
    qh, wq = AN.sphere_grid(*ND)
    s1 = {l: [] for l in (0, 4, 6, 8)}
    for qk in qgrid:
        cmp = cubic_components(si_one_phonon(qk, qh), qh, wq)
        for l in s1:
            s1[l].append(cmp[l])
    s1 = {l: np.array(v) for l, v in s1.items()}
    # direction-grid check of the one-phonon l = 4 component
    qh2, wq2 = AN.sphere_grid(96, 192)
    for xv in (0.3, 1.0, 2.0, 5.0, 10.0):
        a = cubic_components(si_one_phonon(xv * qbz, qh), qh, wq)
        b = cubic_components(si_one_phonon(xv * qbz, qh2), qh2, wq2)
        print("one phonon q = %4.1f q_BZ: S4/S0 = %+.4f (64x128), %+.4f (96x192); S6/S0 %+.4f %+.4f"
              % (xv, a[4] / a[0], b[4] / b[0], a[6] / a[0], b[6] / b[0]))
    d20, B20 = si_pairs(20.0)
    d30, B30 = si_pairs(30.0)
    qhs, wqs = AN.sphere_grid(32, 64)
    s2 = {l: [] for l in (0, 4, 6, 8)}
    for qk in qgrid:
        cmp = cubic_components(si_two_phonon(qk, qhs, d20, B20), qhs, wqs)
        for l in s2:
            s2[l].append(cmp[l])
    s2 = {l: np.array(v) for l, v in s2.items()}
    for xv in (0.5, 2.0, 5.0):
        a = cubic_components(si_two_phonon(xv * qbz, qhs, d20, B20), qhs, wqs)
        b = cubic_components(si_two_phonon(xv * qbz, qhs, d30, B30), qhs, wqs)
        print("two phonons q = %3.1f q_BZ: S4/S0 = %+.5f (pairs to 20 A), %+.5f (30 A); 1+delta_2 = %.4f, %.4f"
              % (xv, a[4] / a[0], b[4] / b[0], a[0] / np.sqrt(4 * np.pi), b[0] / np.sqrt(4 * np.pi)))
    for i in range(0, len(qgrid), 12):
        print("q = %6.2f keV (%5.2f q_BZ): one phonon S4/S0 = %+.4f S6/S0 = %+.4f S8/S0 = %+.4f | two phonons S4/S0 = %+.5f S6/S0 = %+.5f"
              % (qgrid[i], qgrid[i] / qbz, s1[4][i] / s1[0][i], s1[6][i] / s1[0][i], s1[8][i] / s1[0][i],
                 s2[4][i] / s2[0][i], s2[6][i] / s2[0][i]))
    # ---- (2) sapphire and 2H-SiC: site tensors
    sap = Incoherent("darkelf_Al2O3_pDoS_anisotropic.dat", SAPPHIRE)
    sic = Incoherent("darkelf_SiC_pDoS_anisotropic.dat", SIC2H)
    for tag, inc in (("sapphire", sap), ("2H-SiC", sic)):
        Bsum = sum(s["mult"] * s["A"]**2 * s["B"] for s in inc.sites) / sum(s["mult"] * s["A"]**2 for s in inc.sites) * HBARC**2
        for s in inc.sites:
            B = s["B"] * HBARC**2
            print("%s %s: B (A^2) = %s" % (tag, s["name"], np.array2string(B, precision=6)))
        print("%s: A^2-weighted mean B: xx %.4e yy %.4e zz %.4e, off-diag max %.1e A^2; (B_zz - B_xx)/B_xx = %+.4f"
              % (tag, Bsum[0, 0], Bsum[1, 1], Bsum[2, 2], np.abs(Bsum - np.diag(np.diag(Bsum))).max(), Bsum[2, 2] / Bsum[0, 0] - 1))
    np.savez(os.path.join(HERE, "lat11_7.npz"), qgrid=qgrid, qbz=qbz,
             s1=np.array([s1[l] for l in (0, 4, 6, 8)]), s2=np.array([s2[l] for l in (0, 4, 6, 8)]))
    print("wrote lat11_7.npz")
