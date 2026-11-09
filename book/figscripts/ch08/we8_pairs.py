"""Worked example of Sect. 8.7 (we:8-pairs): the pair-resolved response of the silicon valence band at one momentum transfer.

Prints every number quoted in the worked example. No figure.

Model (the modelling choice behind the worked example, named in its text)
  Bands and states: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), as implemented in
     figscripts/ch03/epm.py (Sect. 3.3; form factors, a = 5.43 A and the 113-plane-wave basis are documented there). The same model
     gives Fig. 4.7 (figscripts/ch04/fig4_7_data.py). No spin-orbit coupling; spin enters as the factor 2.
  Momentum transfer: q = q0 = alpha m_e = 3.7289 keV (= 1/bohr) along [100], kept unreduced (App. A.3); in units of 2 pi/a it is
     (1.6331, 0, 0). Each k + q is folded back to the Wigner-Seitz cell, k' = k + q - G_U, and the density vertex is the
     plane-wave form eq:3.2-rhopw, rho_mn(k, q + G) = sum_G'' c*_{m k'}(G'' + G + G_U) c_{n k}(G'').
  Energy deposited: omega = 10 eV (and 5 eV for comparison).
  Independent particles: S(q, w; cvk) = (4 pi/V) |rho_cv(k, q)|^2 delta(w - e_{c,k+q} + e_{vk})   (eq:8.7-IP).
  Screening: RPA with local fields (f_xc = 0), R = R0 + R0 v_C R as matrices in G at fixed (q, w) (eq:4.6-tddft), with R0 the
     Adler-Wiser sum eq:4.6-R0 at T = 0, resonant and antiresonant terms, 4 valence and NC conduction bands; local-field set
     {G : |q + G|^2 <= GMAX2 (2 pi/a)^2}, centred on -q so that the Umklapp partner G = (-2, 0, 0) (|q + G| = 0.83 keV) is inside.
     Out-state (retarded) weight y_G = (eps^-1)_{G0} = delta_G0 + v_C(q + G) R_G0; in-state (advanced) weight
     x_G = delta_G0 + v_C(q + G) R_0G^*  (eq:8.7-screened and the text after it).
  Delta functions: the i0+ of R0 is a Lorentzian of half-width ETA (0.10 eV); the energy delta function of each pair is a
     Gaussian of standard deviation SIG (KERN=gauss, default). A Lorentzian pair kernel (KERN=lor) has tails that, times the
     optical 1/(e_c - e_v)^2 weight, admit strong transitions several eV below omega: with it the photon seed had
     <eps_e + eps_h> = 8.73 eV instead of omega - E_g = 9.18 eV. With the Gaussian every seed satisfies the balance to 0.01 eV.
  Carrier energies: eps_e = e_{c,k+q} - E_CBM, eps_h = E_VBM - e_{vk} (kinetic energies from the band edges, as in Sect. 6.5);
     E_VBM at Gamma, E_CBM the minimum of the lowest conduction band on Gamma-X (0.85 X in this model). Electron share of the
     excess energy x = eps_e/(eps_e + eps_h).
  Comparison seeds at the same omega: (a) the optical limit q -> 0 (photon absorption; vertical pairs weighted by
     |v^x_cv|^2/(e_c - e_v)^2, eq:3.2-optical); (b) the transverse paramagnetic current row y.j_e(q) at the same q0 along [100],
     matrix element sum_G'' c*_{c k'}(G'' + G_U) c_{v k}(G'') (k + G'')_y / m_e (eq:8.1-rows; the term q_y vanishes).
Numerical parameters: NK^3 shifted Monkhorst-Pack grid over the full zone (no symmetry), NC conduction bands, ETA, SIG, GMAX2.
Convergence record (Si, omega = 10 eV, Gaussian pair kernel; NK = 20 / 24 at SIG = 0.10 eV, and NK = 24 at SIG = 0.05 eV;
cached in we8_pairs_Si_NK*_gauss*_eta0.1.json and run_g010_20.log, run_g010_24.log, run_g005_24.log):
  (eps^-1)_00 = 0.548-0.161i / 0.551-0.160i / 0.551-0.160i (SIG-independent);  S0 = -2 Im R0_00 = 1.722e8 / 1.687e8 eV^2;
  S(RPA+LF) = -2 Im R_00 = 4.89e7 / 4.85e7 eV^2 (sum of pair weights 4.93e7 / 4.84e7 / 4.96e7); ratio 0.284 / 0.288;
  |eps^-1_00|^2 = 0.326 / 0.329; other |(eps^-1)_G0| <= 0.055 / 0.051; |eps^-1_00|^2 S_IP / S = 1.148 / 1.139 / 1.139 (12-13 %);
  <eps_e + eps_h> = 9.175-9.180 eV for every seed (omega - E_g = 9.176);
  screened (RET): <eps_e> = 4.81 / 4.79 / 4.76 eV, <eps_h> = 4.37 / 4.38 / 4.42 eV, P(x > 1/2) = 0.650 / 0.642 / 0.640,
     P(x < 1/4 or x > 3/4) = 0.442 / 0.451 / 0.450, valence bands 0.041/0.313/0.332/0.314, 0.043/0.319/0.339/0.299,
     0.042/0.324/0.349/0.285; IP fractions within 0.03 of RET at every setting;
  optical: <eps_e> = 5.76 / 5.72 / 5.63 eV, <eps_h> = 3.42 / 3.45 / 3.54 eV, P(x > 1/2) = 0.847 / 0.847 / 0.844;
     hole difference RET - optical 0.95 / 0.93 / 0.88 eV ("about 0.9 eV");
  transverse current: <eps_e> = 5.32 / 5.35 / 5.32 eV, <eps_h> = 3.85 / 3.83 / 3.86 eV, P(x<1/4 or >3/4) = 0.514 / 0.494 / 0.495;
  RET and ADV weights identical (sum |wR - wA| / sum wR ~ 2e-16) and max|R - R^T|/max|R| ~ 1e-16 (PT symmetry, origin at the
     bond center).
  GaAs (MAT=GaAs, NK = 20, SIG = 0.10): sum |wR - wA| / sum wR = 0.156; <eps_e> RET/ADV = 5.30 / 5.28 eV, <eps_h> 3.29 / 3.30 eV;
     max|R - R^T|/max|R| = 0.21. (Superseded Lorentzian record, NK = 12/16/20: 0.168 / 0.148 / 0.156.)
Superseded record (Lorentzian pair kernel, ETA = 0.10 eV; photon seed violates the energy balance): RET 4.84/4.42 eV,
  optical 5.43/3.30 eV, transverse current 5.41/3.85 eV at NK = 24.
Text quotes the NK = 24, SIG = 0.10 eV values (Si), rounded to the digits that the three settings share.
Run: NK=24 OMEGAS=10 python3 we8_pairs.py (Si, about 8 min single core; add SIG=0.05 for the kernel check);
     MAT=GaAs NK=20 OMEGAS=10 python3 we8_pairs.py.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B, HBARC   # noqa: E402

HA = 2 * RY                              # eV
ME = 510998.95                           # eV (CODATA 2022)
ALPHA = 1 / 137.035999177                # CODATA 2022
NK = int(os.environ.get("NK", 16))
NC = 26
NV = 4
NB = NV + NC
GMAX2 = 12.0
ETA = float(os.environ.get("ETA", 0.10))  # eV, Lorentzian half-width of the i0+ of R0 (the response and the column eps^-1)
KERN = os.environ.get("KERN", "gauss")    # pair kernel for the energy delta function of each pair: "gauss" or "lor"
SIG = float(os.environ.get("SIG", 0.10))  # eV, standard deviation of the Gaussian pair kernel (or half-width if KERN=lor)
OMEGAS = [float(x) for x in os.environ.get("OMEGAS", "10,5").split(",")]

t0 = time.time()
MAT = os.environ.get("MAT", "Si")
si = EPM(MAT)
a_A = si.a
a = a_A / BOHR                           # bohr
Omega = a**3 / 4                         # bohr^3
tpa = 2 * np.pi / a                      # bohr^-1 per unit of 2pi/a
Gb = si.G
NPW = len(Gb)
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
unit_eV = 2 * np.pi * HBARC / a_A        # 2pi/a in eV

q0 = ALPHA * ME                          # eV
qvec = np.array([q0 / unit_eV, 0.0, 0.0])
print(f"q0 = {q0:.2f} eV = {q0/unit_eV:.4f} (2pi/a) along [100]; 2pi/a = {unit_eV:.1f} eV")

# local-field set centred on -q
qG2 = ((qvec + Gb) ** 2).sum(1)
LF = np.where(qG2 <= GMAX2 + 1e-9)[0]
LF = LF[np.argsort(qG2[LF], kind="stable")]
i0 = int(np.where(np.all(np.isclose(Gb[LF], 0), axis=1))[0][0])   # position of G = 0 (the row n_e(q))
NG = len(LF)
vC = 4 * np.pi / (qG2[LF] * tpa**2)      # hartree bohr^3
print(f"NPW = {NPW}, local-field set NG = {NG}; G=0 at position {i0}; smallest |q+G| = "
      f"{np.sqrt(qG2[LF[0]])*unit_eV:.0f} eV at G = {Gb[LF[0]]}")

# candidate folding vectors
cand = Gb[(Gb**2).sum(1) <= 12.5]
_maps = {}


def shift_map(GU):
    """SM[a, j] = basis index of G_j + G_LF[a] + G_U (or -1)."""
    k_ = tuple(np.rint(GU).astype(int))
    if k_ not in _maps:
        M = -np.ones((NG, NPW), int)
        for a_, i in enumerate(LF):
            s = Gb[i] + GU
            for j, g in enumerate(Gb):
                M[a_, j] = key.get(tuple(np.rint(g + s).astype(int)), -1)
        _maps[k_] = M
    return _maps[k_]


def fold(kq):
    d = ((kq[None, :] - cand) ** 2).sum(1)
    return cand[np.argmin(d)]


# band edges
gx = np.linspace(0, 1, 401)[:, None] * np.array([1.0, 0, 0])
eb = si.bands(gx, nb=6)
E_VBM = eb[0, 3]
icbm = np.argmin(eb[:, 4])
E_CBM = eb[icbm, 4]
Eg = E_CBM - E_VBM
print(f"E_g (model, indirect) = {Eg:.3f} eV, CBM at {gx[icbm,0]:.3f} X")

# k grid
f = (np.arange(NK) + 0.5) / NK - 0.5
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
pref_au = 2.0 / (NKT * Omega)            # spin 2, 1/V
pref_eV = 4 * np.pi * HBARC**3 / (NKT * (a_A**3 / 4))   # (4 pi / V) in eV^3
AU_R_TO_EV2 = (HBARC / BOHR) ** 3 / HA   # response: 1/(hartree bohr^3) -> eV^2


def lor(x):
    return (ETA / np.pi) / (x**2 + ETA**2)


def kern(x):
    """Energy delta function of one pair. A Lorentzian tail times the optical 1/(e_c - e_v)^2 weight pulls in pairs far below
    omega (the photon seed then violates eps_e + eps_h = omega - E_g by 0.45 eV at ETA = 0.1 eV); the Gaussian has no tail."""
    if KERN == "lor":
        return (SIG / np.pi) / (x**2 + SIG**2)
    return np.exp(-x**2 / (2 * SIG**2)) / (np.sqrt(2 * np.pi) * SIG)


def states(ks):
    H = si.hamiltonian(ks)
    w, v = np.linalg.eigh(H)
    return w[:, :NB] * RY, v[:, :, :NB]


def kloop(func):
    chunk = 32
    for c0 in range(0, NKT, chunk):
        ks = kpts[c0:c0 + chunk]
        GUs = np.array([fold(k + qvec) for k in ks])
        kps = ks + qvec - GUs
        e1, c1 = states(ks)
        e2, c2 = states(kps)
        for i in range(len(ks)):
            SM = shift_map(GUs[i])
            pad = np.vstack([c2[i], np.zeros((1, NB))])
            cs = pad[SM]                                            # (NG, NPW, NB): c_{k'}(G'' + G + G_U)
            rho_cv = np.einsum("agc,gv->avc", cs[:, :, NV:].conj(), c1[i][:, :NV])   # <c,k+q| e^{i(q+G)r} |v,k>
            rho_vc = np.einsum("agv,gc->avc", cs[:, :, :NV].conj(), c1[i][:, NV:])   # <v,k+q| e^{i(q+G)r} |c,k>
            func(ks[i], e1[i], c1[i], e2[i], cs, rho_cv, rho_vc)


results = {}
for om in OMEGAS:
    tt = time.time()
    w_au = om / HA
    R0 = np.zeros((NG, NG), complex)

    def acc_R0(k, e1, c1, e2, cs, rho_cv, rho_vc):
        global R0
        dEr = (e2[NV:][None, :] - e1[:NV][:, None]) / HA            # (v, c): e_{c,k+q} - e_{vk}
        dEa = (e1[NV:][None, :] - e2[:NV][:, None]) / HA            # (v, c): e_{ck} - e_{v,k+q}
        A = rho_cv.reshape(NG, -1)
        Bm = rho_vc.reshape(NG, -1)
        dr = 1.0 / (w_au - dEr.reshape(-1) + 1j * ETA / HA)
        da = 1.0 / (w_au + dEa.reshape(-1) + 1j * ETA / HA)
        R0 += (A.conj() * dr) @ A.T - (Bm.conj() * da) @ Bm.T

    kloop(acc_R0)
    R0 *= pref_au
    R = np.linalg.solve(np.eye(NG) - R0 * vC[None, :], R0)           # R = R0 + R0 v R
    y = vC * R[:, i0]
    y[i0] += 1.0                                                     # (eps^-1)_{G0}, retarded (out-state)
    x = vC * R[i0, :].conj()
    x[i0] += 1.0                                                     # delta + v_C(q+G) R_0G^*, advanced (in-state)
    epsinv00 = y[i0]
    asym = np.abs(R - R.T).max() / np.abs(R).max()
    S_tot = -2 * R[i0, i0].imag * AU_R_TO_EV2
    S0_tot = -2 * R0[i0, i0].imag * AU_R_TO_EV2

    nbin = 20
    H = {s: np.zeros(nbin) for s in ("IP", "RET", "ADV", "OPT", "JT", "IPscal")}
    MOM = {s: np.zeros(4) for s in H}                                # sum w, sum w x, sum w eps_e, sum w eps_h
    VB = {s: np.zeros(NV) for s in H}
    TV = [0.0]                                                       # sum |w_RET - w_ADV|

    def acc_w(k, e1, c1, e2, cs, rho_cv, rho_vc):
        dE = e2[NV:][None, :] - e1[:NV][:, None]                     # (v, c), eV
        L = kern(om - dE)
        epse = e2[NV:][None, :] - E_CBM + 0 * dE
        epsh = E_VBM - e1[:NV][:, None] + 0 * dE
        xs = np.clip(epse / (epse + epsh), 0, 1)
        wIP = np.abs(rho_cv[i0]) ** 2 * L
        wR = np.abs(np.einsum("a,avc->vc", y, rho_cv)) ** 2 * L
        wA = np.abs(np.einsum("a,avc->vc", x, rho_cv)) ** 2 * L
        TV[0] += np.abs(wR - wA).sum()
        # transverse current (y) at the same q: G = 0 shift only
        kyG = (k[1] + Gb[:, 1]) * tpa                                 # bohr^-1, (k+G)_y; m_e = 1
        jT = np.einsum("gc,g,gv->vc", cs[i0][:, NV:].conj(), kyG, c1[:, :NV])
        wJ = np.abs(jT) ** 2 * L
        # optical limit at the same k (vertical)
        kxG = (k[0] + Gb[:, 0]) * tpa
        vx = np.einsum("gc,g,gv->vc", c1[:, NV:].conj(), kxG, c1[:, :NV])
        dEv = e1[NV:][None, :] - e1[:NV][:, None]
        Lv = kern(om - dEv)
        wO = np.abs(vx) ** 2 / dEv**2 * Lv
        epse_v = e1[NV:][None, :] - E_CBM + 0 * dEv
        epsh_v = E_VBM - e1[:NV][:, None] + 0 * dEv
        xs_v = np.clip(epse_v / (epse_v + epsh_v), 0, 1)
        for s, ww, xx, ee, hh in (("IP", wIP, xs, epse, epsh), ("RET", wR, xs, epse, epsh), ("ADV", wA, xs, epse, epsh),
                                  ("JT", wJ, xs, epse, epsh), ("OPT", wO, xs_v, epse_v, epsh_v)):
            H[s] += np.histogram(xx.ravel(), bins=nbin, range=(0, 1), weights=ww.ravel())[0]
            MOM[s] += [ww.sum(), (ww * xx).sum(), (ww * ee).sum(), (ww * hh).sum()]
            VB[s] += ww.sum(1)

    kloop(acc_w)
    out = dict(epsinv00=epsinv00, S_tot=S_tot, S0_tot=S0_tot, asym=float(asym),
               S_IP=MOM["IP"][0] * pref_eV, S_RET=MOM["RET"][0] * pref_eV, S_ADV=MOM["ADV"][0] * pref_eV,
               TV=TV[0] / MOM["RET"][0], H=H, MOM=MOM, VB=VB)
    results[om] = out
    print(f"\n=== omega = {om} eV  (NK = {NK}, {time.time()-tt:.0f} s) ===")
    print(f"{MAT}: max|R - R^T|/max|R| = {asym:.2e}")
    print(f"(eps^-1)_00 = {epsinv00.real:.4f} {epsinv00.imag:+.4f}i ; |eps^-1_00|^2 = {abs(epsinv00)**2:.4f}")
    print(f"S0 from -2 Im R0_00 = {S0_tot:.4e} eV^2 ; sum of IP pair weights = {out['S_IP']:.4e} eV^2")
    print(f"S (RPA+LF) from -2 Im R_00 = {S_tot:.4e} eV^2 ; sum RET = {out['S_RET']:.4e} ; sum ADV = {out['S_ADV']:.4e}")
    print(f"ratio S_RPA/S_IP = {out['S_RET']/out['S_IP']:.4f};  |eps^-1_00|^2 * S_IP / S_RPA = "
          f"{abs(epsinv00)**2*out['S_IP']/out['S_RET']:.4f}")
    print(f"total-variation distance between RET and ADV pair weights (sum|wR-wA|/sum wR) = {out['TV']:.2e}")
    # largest local-field components
    order = np.argsort(-np.abs(y))
    print("largest |(eps^-1)_G0|:", [(tuple(np.rint(Gb[LF[j]]).astype(int)), round(abs(y[j]), 4)) for j in order[:4]])
    for s in ("IP", "RET", "ADV", "JT", "OPT"):
        m = MOM[s]
        h = H[s] / H[s].sum()
        p_lo = h[:5].sum() + h[-5:].sum()                           # x < 0.25 or x > 0.75
        p_e = h[10:].sum()                                          # electron takes more than half
        vb = VB[s] / VB[s].sum()
        print(f"{s:4s}: <x> = {m[1]/m[0]:.3f}, <eps_e> = {m[2]/m[0]:.2f} eV, <eps_h> = {m[3]/m[0]:.2f} eV, "
              f"<eps_e + eps_h> = {(m[2]+m[3])/m[0]:.3f} eV (omega - E_g = {om-Eg:.3f}), "
              f"P(x>1/2) = {p_e:.3f}, P(x<1/4 or >3/4) = {p_lo:.3f}, valence bands 1-4: {np.round(vb,3)}")
        out.setdefault("summary", {})[s] = dict(x=m[1]/m[0], eps_e=m[2]/m[0], eps_h=m[3]/m[0], P_e_half=p_e, P_lopsided=p_lo,
                                                vb=[float(v) for v in vb])
print(f"\ntotal time {time.time()-t0:.0f} s")

# cache the printed numbers (json, a few kB) so that the worked example can be checked without rerunning
import json
_tag = f"{MAT}_NK{NK}_{KERN}{SIG:g}_eta{ETA:g}"
with open(os.path.join(HERE, f"we8_pairs_{_tag}.json"), "w") as fh:
    json.dump({f"{om:g}": dict(epsinv00=[float(r["epsinv00"].real), float(r["epsinv00"].imag)], S_tot=float(r["S_tot"]),
                              S0_tot=float(r["S0_tot"]), S_IP=float(r["S_IP"]), S_RET=float(r["S_RET"]), S_ADV=float(r["S_ADV"]),
                              TV=float(r["TV"]), asym=r["asym"], Eg=float(Eg), seeds=r["summary"],
                              hist={k: [float(v) for v in r["H"][k]] for k in r["H"]})
               for om, r in results.items()}, fh, indent=1)
print(f"cached we8_pairs_{_tag}.json")
