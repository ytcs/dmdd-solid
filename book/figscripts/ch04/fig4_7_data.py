"""Data for Fig. 4.7 of Sect. 4.6 and Worked example 4.11: the macroscopic dielectric function of silicon at q -> 0
in three approximations, independent particles (IP, identical in eps_2 to the RPA without local fields), the RPA with local
fields, and adiabatic LDA (TDDFT), from one set of model Bloch states.  Writes fig4_7_data.npz next to this file.

Model (the modelling choice behind Fig. 4.7, named in its caption)
  Bands and states: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), as
     implemented in figscripts/ch03/epm.py (Sect. 3.3; form factors and plane-wave cutoff documented there).  The form
     factors were fitted to measured optical transition energies, so the band energies play the role that quasiparticle
     (or scissor-shifted Kohn-Sham) energies play in a first-principles calculation, and no scissor is applied.
     The potential is local, so v_mn = p_mn/m_e exactly (Sect. 3.2) and the f-sum rule holds for the full band sum.
     Local-field calculations with exactly this kind of model were first done by S. G. Louie, J. R. Chelikowsky and
     M. L. Cohen, Phys. Rev. Lett. 34, 155 (1975).
  Crystal bubble: the Adler-Wiser sum, eq:4.6-R0 of the book (= eq:E.6-R0), at T = 0, with both pair terms written
     out: the resonant term (v k -> c k+q) and the antiresonant term (pair c k, v k+q), as derived in Sect. 4.6.
  Optical limit q -> 0 along x (cubic crystal: the result does not depend on the direction): the G = 0 vertex is
     q.v_cv/(eps_c - eps_v) (eq:3.2-optical), the G != 0 vertices are rho_cv(k, G) at the same k.  The head of R^0 is
     O(q^2), the wings O(q).  We divide the G = 0 component of every vertex by q and use the form
     eps_mac = 1 - v_C(q) Rbar_00 of App. D.7, with Rbar = R^0 + R^0 (vbar + f_xc) Rbar, vbar = v_C without its G = 0
     element.  In the scaled variables the G = 0 row and column of (vbar + f_xc) drop out as q -> 0.
  Kernels: vbar_GG' = 4 pi/|G|^2 delta_GG' (Gaussian atomic units, e = 1).  ALDA: f_xc(r) = d^2(n eps_xc)/dn^2 at the
     valence (pseudo) density n(r) of the same states, with Slater exchange and the Perdew-Zunger parametrization of
     the Ceperley-Alder correlation energy, J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981), Eqs. (C1)-(C4)
     (unpolarized constants gamma = -0.1423, beta1 = 1.0529, beta2 = 0.3334 for r_s >= 1; A = 0.0311, B = -0.048,
     C = 0.0020, D = -0.0116 for r_s < 1, in hartree).  (f_xc)_GG' = f_xc(G - G'), the cell average of
     f_xc(r) exp(-i(G-G').r).
  Numerical parameters: shifted Monkhorst-Pack grid NK^3 over the full zone (no symmetry), 4 valence and NC
     conduction bands, local-field set of the reciprocal vectors with |G|^2 <= GMAX2 (2 pi/a)^2, Lorentzian
     broadening ETA of the energy denominators, transitions binned on a grid of width DE with linear weights.
     The convergence of eps_inf with NG is checked by repeating the static calculation with a larger set.
Units: hartree atomic units inside; energies printed in eV.
Output: fig4_7_data.npz (about 40 kB): eps_mac(omega) of the three approximations on 0-30 eV, the static values on the 59- and
  113-vector local-field sets, and a few diagnostics.  The large spectral matrices stay in memory only.
Convergence record (static eps_mac, 59 G; IP / RPA+LF / ALDA): NK = 8: 11.4585 / 10.2315 / 10.8183;
  NK = 20: 11.4507 / 10.2242 / 10.8106.  113 G at NK = 20: 11.4507 / 10.2175 / 10.7914.
Run: NK=20 python3 fig4_7_data.py  (single core, about 20 min on a loaded 4-core box, peak memory about 1 GB).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # single-threaded: runs beside the plane-wave jobs of the box without contention
import sys
import time
import numpy as np
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B   # noqa: E402

HA = 2 * RY                  # eV
NK = int(os.environ.get("NK", 20))
NC = 26                      # conduction bands (up to ~ 45 eV above the valence maximum)
GMAX2 = 12                   # local-field set |G|^2 <= 12 (2pi/a)^2: 59 vectors
GMAX2_CHECK = 20             # larger set for the static convergence check: 113 vectors
ETA = 0.10 / HA              # Lorentzian broadening, 0.10 eV
DE = 0.02 / HA               # bin width, 0.02 eV
EMAX_BIN = 50.0 / HA
W = np.linspace(0.0, 30.0, 1501) / HA   # output frequencies, 0-30 eV

t0 = time.time()
si = EPM("Si")
a = si.a / BOHR                          # bohr
Omega = a**3 / 4                         # primitive cell, bohr^3
tpa = 2 * np.pi / a                      # 2 pi / a in bohr^-1
Gb = si.G                                # basis vectors, units 2pi/a
NPW = len(Gb)
key = {tuple(np.rint(g * 1).astype(int)): i for i, g in enumerate(Gb)}   # G has integer components in 2pi/a units


def lf_set(gmax2):
    g2 = np.rint((Gb**2).sum(1)).astype(int)
    idx = np.where(g2 <= gmax2)[0]
    idx = idx[np.argsort(g2[idx], kind="stable")]
    assert np.allclose(Gb[idx[0]], 0)
    return idx


def shift_map(lf_idx):
    """For each LF vector G and basis vector G'', index of G'' + G in the basis (or -1)."""
    M = -np.ones((len(lf_idx), NPW), int)
    for a_, i in enumerate(lf_idx):
        for j, g in enumerate(Gb):
            M[a_, j] = key.get(tuple(np.rint(g + Gb[i]).astype(int)), -1)
    return M


# k grid: shifted MP grid in the full zone, crystal coordinates (j + 1/2)/NK - 1/2 along the reciprocal primitive vectors
f = (np.arange(NK) + 0.5) / NK - 0.5
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B                                         # units 2pi/a
NKT = len(kpts)
NV = 4
NB = NV + NC

LF = lf_set(GMAX2)
LFc = lf_set(GMAX2_CHECK)
NG, NGc = len(LF), len(LFc)
SM = shift_map(LFc)                                   # covers LF (LF is the leading part of LFc)
print(f"NPW = {NPW}, NG = {NG} (check {NGc}), NK = {NK}^3 = {NKT}, bands {NV}+{NC}")

# accumulators
nb = int(EMAX_BIN / DE) + 2
Ebins = np.arange(nb) * DE
Mres = np.zeros((nb, NG * NG), np.complex128)   # resonant spectral matrices  sum A_G A_G'^*
Mant = np.zeros((nb, NG * NG), complex)   # antiresonant                sum B_G B_G'^*
R0stat = np.zeros((NGc, NGc), complex)    # static R^0 (scaled), larger set
fsum_check = 0.0                          # sum over transitions of E |rho_head/q|^2 (f-sum, x direction)
Emin = np.inf
NR = 32                                   # real-space grid per primitive direction
MI = np.rint(Gb @ np.linalg.inv(B)).astype(int)   # integer coordinates of the basis on the reciprocal primitive vectors
assert np.allclose(MI @ B, Gb)
MI = MI % NR
dens = np.zeros((NR, NR, NR))

chunk = 16
for c0 in range(0, NKT, chunk):
    ks = kpts[c0:c0 + chunk]
    H = si.hamiltonian(ks)
    w, v = np.linalg.eigh(H)
    w = w[:, :NB] * (RY / HA)                       # hartree
    v = v[:, :, :NB]                                 # (nk, NPW, NB)
    buf_i, buf_R, buf_A = [], [], []
    for ik in range(len(ks)):
        c = v[ik]
        e = w[ik]
        # valence density coefficients n(G) ∝ sum_v sum_G'' c_v(G'')^* c_v(G''+G) for G in the basis
        # (accumulated for G in the check set; mapped later)
        # velocity x-component: p = (k + G) in bohr^-1, v = p/m_e = p (a.u.)
        kx = (ks[ik][0] + Gb[:, 0]) * tpa
        vx = np.einsum("gm,g,gn->mn", c.conj(), kx, c)              # v_mn, x component
        cv, cc = c[:, :NV], c[:, NV:]
        ev, ec = e[:NV], e[NV:]
        dE = ec[None, :] - ev[:, None]                               # (NV, NC), E_c - E_v
        Emin = min(Emin, dE.min())
        # vertices for G in the check set (q -> 0, same k):
        #   rho_cv(k, G) = sum_G'' c_c(G''+G)^* c_v(G'')      (resonant, A_G = rho_cv^*)
        #   rho_vc(k, G) = sum_G'' c_v(G''+G)^* c_c(G'')      (antiresonant, B_G = rho_vc^*)
        pad = np.vstack([c, np.zeros((1, NB))])                       # index -1 -> zero row
        cs = pad[SM]                                                  # (NGc, NPW, NB): c(G''+G)
        rho_cv = np.einsum("agc,gv->avc", cs[:, :, NV:].conj(), cv)   # (NGc, NV, NC)
        rho_vc = np.einsum("agv,gc->avc", cs[:, :, :NV].conj(), cc)   # (NGc, NV, NC)
        # head: rho_cv(k, q)/q -> v^x_cv/(E_c - E_v);  rho_vc(k, q)/q -> v^x_vc/(E_v - E_c)
        rho_cv[0] = vx[NV:, :NV].T / dE
        rho_vc[0] = vx[:NV, NV:] / (-dE)
        fsum_check += (dE * np.abs(rho_cv[0])**2).sum()
        A = rho_cv.reshape(NGc, -1).conj().T                          # (Nt, NGc)
        Bm = rho_vc.reshape(NGc, -1).conj().T
        Et = dE.reshape(-1)
        # static (scaled) R^0 on the larger set: -A A^+/E - B B^+/E
        R0stat += -(A.T / Et) @ A.conj() - (Bm.T / Et) @ Bm.conj()
        # binned spectral matrices on the LF set, linear weights to the two neighbouring bins (accumulated per chunk)
        x = Et / DE
        i0 = np.floor(x).astype(int)
        wt = x - i0
        keep = i0 < nb - 1
        i0, wt, Al, Bl = i0[keep], wt[keep], A[keep, :NG], Bm[keep, :NG]
        oR = (Al[:, :, None] * Al[:, None, :].conj()).reshape(len(i0), -1)
        oA = (Bl[:, :, None] * Bl[:, None, :].conj()).reshape(len(i0), -1)
        buf_i.append(np.concatenate([i0, i0 + 1]))
        buf_R.append(np.concatenate([(1 - wt)[:, None] * oR, wt[:, None] * oR]))
        buf_A.append(np.concatenate([(1 - wt)[:, None] * oA, wt[:, None] * oA]))
        # valence density on the real-space grid of the cell: |u_v(r)|^2 summed over v
        box = np.zeros((NV, NR, NR, NR), complex)
        box[:, MI[:, 0], MI[:, 1], MI[:, 2]] = cv.T
        u = np.fft.ifftn(box, axes=(1, 2, 3)) * NR**3
        dens += (np.abs(u)**2).sum(0)
    bi = np.concatenate(buf_i)
    order = np.argsort(bi, kind="stable")
    bi = bi[order]
    ub, start = np.unique(bi, return_index=True)
    Mres[ub] += np.add.reduceat(np.concatenate(buf_R)[order], start, axis=0)
    Mant[ub] += np.add.reduceat(np.concatenate(buf_A)[order], start, axis=0)
    if c0 == 0:
        print(f"  first chunk {time.time() - t0:.1f} s")
print(f"transitions done in {time.time() - t0:.0f} s; minimum transition energy {Emin * HA:.3f} eV")

dens *= 2.0 / (NKT * Omega)           # electrons per bohr^3 (2 for spin)
print(f"electrons per cell from the density: {dens.mean() * Omega:.6f}")
pref = 2.0 / (NKT * Omega)            # 2 for spin, 1/(N Omega)
Mres *= pref
Mant *= pref
R0stat *= pref
fsum_check *= pref

def pz_exc(n):
    """eps_xc per electron (hartree), Slater exchange + Perdew-Zunger 1981 correlation, unpolarized."""
    rs = (3 / (4 * np.pi * n)) ** (1 / 3)
    ex = -0.75 * (3 * n / np.pi) ** (1 / 3)
    hi = rs >= 1
    ec = np.empty_like(rs)
    r = rs[hi]
    ec[hi] = -0.1423 / (1 + 1.0529 * np.sqrt(r) + 0.3334 * r)
    r = rs[~hi]
    ec[~hi] = 0.0311 * np.log(r) - 0.048 + 0.0020 * r * np.log(r) - 0.0116 * r
    return ex + ec


def fxc_alda(n, h=1e-4):
    """d^2 (n eps_xc)/dn^2 by central differences in ln n."""
    F = lambda x: x * pz_exc(x)
    n1, n2 = n * (1 - h), n * (1 + h)
    return (F(n2) - 2 * F(n) + F(n1)) / (n * h) ** 2


def analyse(d, eta_eV=0.10, W=None):
    Mres, Mant, Eb = d["Mres"], d["Mant"], d["Ebins"]
    NG = int(d["NG"])
    LF = d["LF"]
    Gb = d["Gb"]
    a = float(d["a"])
    tpa = 2 * np.pi / a
    eta = eta_eV / HA
    if W is None:
        W = np.linspace(0, 30, 1501) / HA
    # R0(w) scaled, (Nw, NG*NG)
    g_res = 1.0 / (W[:, None] - Eb[None, :] + 1j * eta)
    g_ant = 1.0 / (W[:, None] + Eb[None, :] + 1j * eta)
    R0 = (g_res @ Mres - g_ant @ Mant).reshape(len(W), NG, NG)
    # kernels
    G = Gb[LF] * tpa
    G2 = (G**2).sum(1)
    vbar = np.zeros(NG)
    vbar[1:] = 4 * np.pi / G2[1:]
    # ALDA kernel from density on the grid
    dens, MI, NR = d["dens"], d["MI"], int(d["NR"])
    fr = fxc_alda(dens)
    fG = np.fft.fftn(fr) / NR**3          # coefficient of exp(+iG.r)
    mi = MI[LF]
    dm = (mi[:, None, :] - mi[None, :, :]) % NR
    Fxc = fG[dm[..., 0], dm[..., 1], dm[..., 2]]   # f(G - G')
    out = {}
    for name, K in [("ip", None), ("rpa", np.diag(vbar)), ("alda", np.diag(vbar) + Fxc)]:
        if K is None:
            Rb00 = R0[:, 0, 0]
        else:
            Kh = K.copy()
            Kh[0, :] = 0
            Kh[:, 0] = 0
            I = np.eye(NG)
            Rb = np.linalg.solve(I[None] - R0 @ Kh[None], R0)
            Rb00 = Rb[:, 0, 0]
        out[name] = 1 - 4 * np.pi * Rb00
    return W * HA, out, Fxc, vbar




# ---------------------------------------------------------------- spectra and static values (only these are saved)
d = dict(Mres=Mres, Mant=Mant, Ebins=Ebins, NG=NG, LF=LF, Gb=Gb, a=a, dens=dens, MI=MI, NR=NR)
wE, eps, Fxc, vbar = analyse(d, eta_eV=ETA * HA, W=W)
del Mres, Mant


def static(lf_idx, R0s):
    """eps_mac(q -> 0, 0) for the three approximations on the local-field set lf_idx, from the static scaled R^0."""
    G = Gb[lf_idx] * tpa
    G2 = (G**2).sum(1)
    vb = np.zeros(len(lf_idx))
    vb[1:] = 4 * np.pi / G2[1:]
    mi = MI[lf_idx]
    dm = (mi[:, None, :] - mi[None, :, :]) % NR
    fG = np.fft.fftn(fxc_alda(dens)) / NR**3
    F = fG[dm[..., 0], dm[..., 1], dm[..., 2]]
    res = {"ip": 1 - 4 * np.pi * R0s[0, 0].real}
    for name, K in [("rpa", np.diag(vb)), ("alda", np.diag(vb) + F)]:
        Kh = K.copy()
        Kh[0, :] = 0
        Kh[:, 0] = 0
        Rb = np.linalg.solve(np.eye(len(lf_idx)) - R0s @ Kh, R0s)
        res[name] = 1 - 4 * np.pi * Rb[0, 0].real
    return res


assert np.array_equal(LF, LFc[:NG])
st59 = static(LF, R0stat[:NG, :NG])
st113 = static(LFc, R0stat)
print("static eps_mac, 59 G:", st59)
print("static eps_mac, 113 G:", st113)
fsum_frac = 2 * fsum_check / (8 / Omega)   # (sum over all included transitions of E |rho/q|^2) / (n_e/2), the f-sum fraction
np.savez_compressed(os.path.join(HERE, "fig4_7_data.npz"), w=wE,
                    eps_ip=eps["ip"].astype(np.complex64), eps_rpa=eps["rpa"].astype(np.complex64),
                    eps_alda=eps["alda"].astype(np.complex64),
                    st59=np.array([st59[k] for k in ("ip", "rpa", "alda")]),
                    st113=np.array([st113[k] for k in ("ip", "rpa", "alda")]),
                    fsum_full=fsum_frac, Emin=Emin * HA, Omega=Omega, a=a, NK=NK, NG=NG, NGc=NGc, eta=ETA * HA,
                    nmin=dens.min(), nmax=dens.max(), fxc00=Fxc[0, 0].real)
print(f"saved fig4_7_data.npz; total {time.time() - t0:.0f} s")
