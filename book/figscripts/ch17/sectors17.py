"""Dominant-sector maps of silicon (Sect. 17.1, fig:17-sectors) and the multiphonon-Migdal crossover of WE 17.1.
Computes the rates and writes sectors17.npz and sectors17.log; fig17_sectors.py draws the figure from the npz.
Every number printed in Sect. 17.1 that rests on this model is in sectors17.log.

Natural units hbar = c = 1; energies and momenta in eV. Rates per unit target mass, events per kg and year.

Nucleon coupling (panel a). Equal couplings to protons and neutrons (operator O_1 of eq:8.1-nuclear, c_kappa = A),
heavy mediator, sigma_n = 1e-38 cm^2 (only ratios enter the map). Generic rate (as figscripts/ch12/mig12.py):
    dR/domega = rho_chi / (4 pi^2 rho_T m_chi) int dq q eta(v_min) D S(q, omega),  D = pi A^2 sigma_n / mu_n^2,
    v_min = omega/q + q/(2 m_chi)   (eq:1.3 kinematics, Delta_chi = 0),
with S per unit mass = (2 pi / M) s(q, omega) for the incoherent self response s of one nucleus.
  Sectors and responses (every input reused from the book's scripts, nothing recomputed from first principles):
  * one phonon, q <= q_BZ: coherent long-wavelength acoustic response eq:11.1-Sac with the Christoffel speeds and
    polarizations of the measured elastic tensor (figscripts/ch11/phon11.py, rate_per_mass, sigma_p = sigma_n,
    q cut at q_BZ = 2.25 keV); phonon energy omega = c_nu q.
  * q > q_BZ: incoherent harmonic response at T = 0 (eq:11.3-inc) of the PBE phonon density of states of Sect. 5.2
    (figscripts/ch11/imp11.py), split into the one-phonon term and the n >= 2 terms:
        s(q, omega) = sum_{n>=1} e^{-2W} (2W)^n / n! P_n(omega),   2W = q^2 <u_x^2>,  P_n = P_1 * ... * P_1.
    P_n is built by repeated DIRECT convolution on a 0.5-meV grid (positive arrays, no cancellation, so the Poisson tail
    is resolved to the floating-point underflow, not to an FFT noise floor), n <= 170, up to omega = 10.8 eV.
    Used for q <= Q_GAUSS = 300 keV (2W = 56; the Poisson weight beyond n = 170 is below 1e-20 there).
  * q > Q_GAUSS: impulse Gaussian eq:11.4-IAgauss (mean E_R, variance 4 E_R K, K = <omega>/4 = 10.2 meV), the
    form that Limit 11.4a validates near the peak; its tail beyond the endpoint is a model.
  * Nuclear form factor: Helm (eq:2.2-helm, Lewin-Smith parameters, imp11.helm) at all q.
  * Migdal: soft-limit probability per kick eq:12.3-soft, dP/domega_e = 4 alpha v_N^2 Q_Mig(omega_e), v_N = q/M, with
    the loss function with local fields and Z_ion(p) of Sect. 12.3 (figscripts/ch12/mig12.py; tables' scissor gap
    1.11 eV, omega_e <= 89 eV). By the sum rule of Sect. 12.4 it holds at every q. Lattice energy in v_min and in the
    deposited energy: the free-recoil value omega_l = q^2/2M (the mean of the lattice factor), so the deposited energy is
    omega = omega_e + q^2/2M. Zero-phonon share of the Migdal events at kick q: <exp(-2W(|q - p|))> over the momentum p
    of the electrons, weighted as in figscripts/ch12/fig12_4.py (Z_ion^2 L/omega^4, c^2 angular weight).
  Threshold omega_th on the total deposited energy (a calorimetric threshold).
  Lattice labels at each point: "one phonon" if the n = 1 rate above omega_th exceeds that of n >= 2; otherwise
  "multiphonon" if the rate-weighted median q of the lattice rate is below the impulse onset 92.5 keV (x_R = 4,
  Sect. 11.4), else "free recoil".

Electron coupling (panel b). Heavy mediator, reference cross section sigma_e = 1e-37 cm^2 (only ratios enter).
  * zero-phonon electron recoil: loss-function rate eq:10.2-rate with the random-phase loss function with local fields
    (figscripts/ch10/rate10_2.py, si_elf_binned.npz; scissor gap 1.11 eV), omega <= m v_max^2/2.
  * electron-following acoustic peak of an electron-only coupling (Sect. 10.2, Limit 10.2a): rate10_2.phonon_dRdq,
    the pedagogical model of that limit check (linear LA branch c_LA = 8.43 km/s to |q| = 2 pi/a = 2.28 keV, 28 electrons
    per cell following, no Debye-Waller factor, Umklapp, transverse branches or multiphonons). Absent for a dark photon
    (total charge): the acoustic weight of S_ZZ in silicon starts at O(q^4) (Sect. 8.4).
  * phonon-assisted window: no rate is computed here; the window is drawn from the masses of Table 13.1
    (onsets 0.3332/0.3374 MeV, first zero-phonon edge 0.405-0.408 MeV, phonon-assisted lead to 0.42-0.43 MeV,
    two-channel band 0.43-0.51 MeV) up to the largest deposit m v_max^2/2.
Halo: v0 = 238, v_esc = 544, v_E = 250.5 km/s, rho_chi = 0.3 GeV/cm^3 (Sect. 1.2), eta(v_min) of App. D.1.
Run: python sectors17.py   (numpy, scipy; about 2-4 min). Output: sectors17.npz, sectors17.log.
"""
import os
import sys
import numpy as np
from scipy.stats import poisson
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
for d in ("ch10", "ch11", "ch12"):
    sys.path.insert(0, os.path.join(HERE, "..", d))
import rate10_2 as R  # noqa: E402
import imp11 as I  # noqa: E402
import mig12 as G  # noqa: E402
import phon11 as P  # noqa: E402

LOG = None                     # opened only when run as a script, so that importing this module keeps the log
SETUP = []


def out(*a):
    s = " ".join(str(x) for x in a)
    if LOG is None:
        SETUP.append(s)
        return
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


M = I.M                      # Si atomic mass, eV
A = G.A_SI                   # 28.0855
M_N = G.M_N
VMAX = R.VMAX
QBZ = 2.25e3
Q_IMP = np.sqrt(2 * M * 4 * I.W_MEAN)          # impulse onset, x_R = 4
Q_GAUSS = 300e3
SIG_N = 1e-38 * R.CM**2
KIN = I.kin_q(0)


def mu(a, b):
    return a * b / (a + b)


# ---- n-phonon spectra by direct convolution --------------------------------------------------------------------------
H = 0.5e-3
NB = int(np.ceil(0.0640 / H))
# P1 sampled at the points j H (j = 0..NB) as the bin average of the 0.1-meV density of imp11 over [jH - H/2, jH + H/2]
cw = np.concatenate([[0], np.cumsum(I.P1 * I.DW)])
xw = np.concatenate([[0], I.WG + I.DW / 2])
pts = np.arange(NB + 1) * H
P1 = (np.interp(pts + H / 2, xw, cw) - np.interp(np.maximum(pts - H / 2, 0), xw, cw)) / H
NMAX = 170
NW = NMAX * NB + 1
WGRID = np.arange(NW) * H                                # P_n of order n is supported on [0, n * 64 meV]
PN = np.zeros((NMAX + 1, NW))
PN[1, :NB + 1] = P1
cur = P1.copy()
for n in range(2, NMAX + 1):
    cur = np.convolve(cur, P1) * H                       # samples at iH and jH land at (i + j)H: no shift
    PN[n, :len(cur)] = cur[:NW]
norms = PN.sum(axis=1) * H
out("n-phonon spectra: grid %.1f meV, %d points to %.2f eV, n <= %d; Riemann norms n=1,2,10,100,170: %.6f %.6f %.6f %.6f %.6f"
    % (H * 1e3, NW, WGRID[-1], NMAX, norms[1], norms[2], norms[10], norms[100], norms[170]))
means = (PN * WGRID).sum(axis=1) * H / np.maximum(norms, 1e-300)
out("  mean of P_n / (n <omega^-1>^-1): n=1 %.5f, n=10 %.5f, n=100 %.5f  (P_1 = g/omega normalized, mean <omega^-1>^-1 = %.2f meV)"
    % (means[1] / I.W_INV, means[10] / (10 * I.W_INV), means[100] / (100 * I.W_INV), I.W_INV * 1e3))
PN = PN / np.maximum(norms, 1e-300)[:, None]
PN[0] = 0.0


def s_incoh(q):
    """Incoherent spectra (one-phonon, n >= 2) on WGRID for an array q (eV): shapes (len(q), NW)."""
    tw = I.two_w(np.atleast_1d(q))
    n = np.arange(NMAX + 1)
    w = np.exp(poisson.logpmf(n[None, :], tw[:, None]))
    w1 = w[:, 1:2] * PN[1][None, :]
    wm = w.copy()
    wm[:, :2] = 0.0
    return w1, wm @ PN


def rev_cum(y, x):
    """R(> x_j) = int_{x_j}^{x_end} y dx along the last axis (trapezoid)."""
    seg = 0.5 * (y[..., 1:] + y[..., :-1]) * np.diff(x)
    c = np.cumsum(seg[..., ::-1], axis=-1)[..., ::-1]
    return np.concatenate([c, np.zeros(y.shape[:-1] + (1,))], axis=-1)


# ---- zero-phonon share of Migdal events (fig12_4 weighting) -----------------------------------------------------------
sel = G.OM >= G.EG
KK = G.KG[1:]
gk = np.trapezoid(G.LF_G[sel][:, 1:] / G.OM[sel][:, None]**4, G.OM[sel], axis=0)
wk = KK**2 * G.ZG[1:]**2 * gk
CN, CWt = np.polynomial.legendre.leggauss(48)
WT = wk[:, None] * (CN**2 * CWt / 2)[None, :] * np.gradient(KK)[:, None]
WT /= WT.sum()


def zp_share(q):
    q = np.atleast_1d(q)
    res = np.empty(len(q))
    for i, qq in enumerate(q):
        Q2 = qq**2 + KK[:, None]**2 - 2 * qq * KK[:, None] * CN[None, :]
        res[i] = np.sum(WT * np.exp(-I.two_w(1.0) * Q2))
    return res


# ---- rates for one mass -----------------------------------------------------------------------------------------------
W_BANDTOP = float(I.WG[I.G > 0].max())     # band top of the PBE phonon DOS, 63.7 meV
OM_E = G.OM[sel]
QMIG = G.qmig("lf")[sel]
CONV = R.to_per_kg_yr(1.0)
AV = P.averages("Si")


def nucleon_rates(m, wth, nq=200):
    """Rates above each threshold in wth (array, eV), events/kg/yr at sigma_n = 1e-38 cm^2; and the rate-weighted
    median momentum transfer of the lattice rate above each threshold."""
    muN, mun = mu(m, M), mu(m, M_N)
    qmax = 2 * muN * VMAX
    D = np.pi * A**2 * SIG_N / mun**2
    pref = R.RHO_CHI / (4 * np.pi**2 * m) * D * 2 * np.pi / M * CONV
    res = {k: np.zeros(len(wth)) for k in ("one", "multi", "gauss", "mig0", "migp")}
    # one phonon, q <= q_BZ (coherent acoustic, phon11); sigma_p = sigma_n
    for i, w in enumerate(wth):
        # the linear branches run to q_BZ, where c_LA,max q_BZ = 70.2 meV exceeds every real phonon; cap the coherent
        # one-phonon deposit at the band top of the PBE density of states, omega_max = 63.7 meV (Sect. 5.2)
        if w < min(AV["cLAmax"] * P.KMS * QBZ, W_BANDTOP):
            res["one"][i] = P.rate_per_mass(m, "Si", "heavy", wth=w, sigp=1e-38, av=AV, nq=160)
    qparts, wparts = [], []                       # per-q rates above each threshold, for the median q
    # incoherent, q_BZ < q <= Q_GAUSS
    qhi = min(qmax, Q_GAUSS)
    if qhi > QBZ:
        q = np.geomspace(QBZ, qhi, nq)
        dq = np.gradient(q)
        F2 = I.helm(q, A)[0]**2
        s1, sm = s_incoh(q)
        vmin = WGRID[None, :] / q[:, None] + q[:, None] / (2 * m)
        ker = (q * F2 * dq)[:, None] * R.eta(vmin) * pref         # per-q-bin weight
        c1 = rev_cum(ker * s1, WGRID)                             # (nq, NW): rate above omega from each q bin
        cm = rev_cum(ker * sm, WGRID)
        j = np.clip(np.searchsorted(WGRID, wth), 0, NW - 1)
        f = (wth - WGRID[np.maximum(j - 1, 0)]) / H
        def at(c):
            lo = c[:, np.maximum(j - 1, 0)]
            hi = c[:, j]
            return np.where(wth[None, :] > WGRID[-1], 0.0, lo + (hi - lo) * np.clip(f, 0, 1)[None, :])
        a1, am = at(c1), at(cm)
        res["one"] += a1.sum(0)
        res["multi"] += am.sum(0)
        qparts.append(q)
        wparts.append(a1 + am)
    # impulse Gaussian, q > Q_GAUSS
    if qmax > Q_GAUSS:
        q = np.geomspace(Q_GAUSS, qmax, nq)
        dq = np.gradient(q)
        F2 = I.helm(q, A)[0]**2
        ER = q**2 / (2 * M)
        sig = np.sqrt(4 * ER * KIN)
        wg = np.geomspace(1e-3, ER[-1] + 12 * sig[-1], 4000)
        vmin = wg[None, :] / q[:, None] + q[:, None] / (2 * m)
        gs = np.exp(-(wg[None, :] - ER[:, None])**2 / (2 * sig[:, None]**2)) / np.sqrt(2 * np.pi * sig[:, None]**2)
        ker = (q * F2 * dq)[:, None] * R.eta(vmin) * pref * gs
        cg = rev_cum(ker, wg)
        ag = np.array([np.interp(wth, wg, cg[i], left=cg[i, 0], right=0.0) for i in range(len(q))])
        res["gauss"] = ag.sum(0)
        qparts.append(q)
        wparts.append(ag)
    qmed = np.full(len(wth), np.nan)
    if qparts:
        qa = np.concatenate(qparts)
        wa = np.concatenate(wparts, axis=0)
        cwa = np.cumsum(wa, axis=0)
        for i in range(len(wth)):
            if cwa[-1, i] > 0:
                qmed[i] = np.interp(0.5, cwa[:, i] / cwa[-1, i], qa)
    res["qmed_lat"] = qmed
    # Migdal: zero-phonon and phonon-dressed parts
    q = np.geomspace(100.0, qmax, nq)
    f0 = zp_share(q)
    ER = q**2 / (2 * M)
    wtot = OM_E[None, :] + ER[:, None]
    vmin = wtot / q[:, None] + q[:, None] / (2 * m)
    integ = q[:, None] * R.eta(vmin) * 4 * G.ALPHA * (q**2 / M**2)[:, None] * QMIG[None, :]
    lnq = np.log(q)
    for i, w in enumerate(wth):
        a = np.trapezoid(np.where(wtot >= w, integ, 0.0), OM_E, axis=1)
        res["mig0"][i] = np.trapezoid(a * f0 * q, lnq) * pref
        res["migp"][i] = np.trapezoid(a * (1 - f0) * q, lnq) * pref
    return res


# electron coupling
DATA = R.load()


def electron_rates(m, wth):
    w, s = R.spectrum(m, "lf", DATA)
    s = np.where(w <= m * VMAX**2 / 2, s, 0.0)
    seg = 0.5 * (s[1:] + s[:-1]) * np.diff(w)
    cer = np.concatenate([np.cumsum(seg[::-1])[::-1], [0.0]])
    er = np.where(wth <= w[0], cer[0], np.interp(wth, w, cer, right=0.0))
    qph = np.linspace(1.0, R.Q_X, 6000)
    dRdq = R.phonon_dRdq(qph, m) * CONV
    cq = np.concatenate([np.cumsum((0.5 * (dRdq[1:] + dRdq[:-1]) * np.diff(qph))[::-1])[::-1], [0.0]])
    ac = np.interp(wth / R.C_LA, qph, cq, left=cq[0], right=0.0)
    return er, ac


def cross_log(x, y1, y2):
    """First crossing (from below in x) where y1 - y2 changes sign, by linear interpolation in log y on a fine grid."""
    with np.errstate(divide="ignore"):
        d = np.log(np.maximum(y1, 1e-300)) - np.log(np.maximum(y2, 1e-300))
    idx = np.where(np.sign(d[:-1]) != np.sign(d[1:]))[0]
    if len(idx) == 0:
        return np.nan
    i = idx[0]
    t = d[i] / (d[i] - d[i + 1])
    return np.exp(np.log(x[i]) + t * (np.log(x[i + 1]) - np.log(x[i])))


if __name__ == "__main__":
    LOG = open(os.path.join(HERE, "sectors17.log"), "w")
    for line in SETUP:
        out(line)
    out("Si inputs: M = %.4f GeV, <omega> = %.2f meV, <omega^-1>^-1 = %.2f meV, K = %.2f meV, impulse onset q = %.1f keV, "
        "q_BZ = %.2f keV, v_max = %.4e" % (M / 1e9, I.W_MEAN * 1e3, I.W_INV * 1e3, KIN * 1e3, Q_IMP / 1e3, QBZ / 1e3, VMAX))
    out("phonon band top of the PBE DOS: %.1f meV; tables' gap %.2f eV; Migdal kinematic floor 2 E_g / v_max^2 = %.3f MeV "
        "(%.3f MeV with the physical 1.17 eV)" % (I.WG[I.G > 0].max() * 1e3, G.EG, 2 * G.EG / VMAX**2 / 1e6,
                                                 2 * 1.17 / VMAX**2 / 1e6))
    # ---- WE 17.1: multiphonon-Migdal crossover on a fine threshold grid ------------------------------------------
    WF = np.geomspace(0.03, 60.0, 1400)
    out("Multiphonon/free-recoil vs Migdal crossover (total deposited energy threshold; fine grid of %d thresholds, "
        "spacing %.2f %%):" % (len(WF), 100 * (WF[1] / WF[0] - 1)))
    for m in (1e6, 3e6, 6.3e6, 10e6, 17.5e6, 30e6, 100e6, 300e6):
        r = nucleon_rates(m, WF)
        lat = r["one"] + r["multi"] + r["gauss"]
        mig = r["mig0"] + r["migp"]
        wx = cross_log(WF, lat, mig)
        qmax = 2 * mu(m, M) * VMAX
        ermax = qmax**2 / (2 * M)
        k = np.argmin(abs(WF - wx)) if np.isfinite(wx) else 0
        k2 = min(max(k, 1), len(WF) - 2)
        slope = -(np.log(lat[k2 + 1]) - np.log(lat[k2 - 1])) / (WF[k2 + 1] - WF[k2 - 1]) if np.isfinite(wx) else np.nan
        slm = -(np.log(mig[k2 + 1]) - np.log(mig[k2 - 1])) / (WF[k2 + 1] - WF[k2 - 1]) if np.isfinite(wx) else np.nan
        out("    log-slopes at the crossover: -dlnR_lat/domega = %.3g /eV, -dlnR_Mig/domega = %.3g /eV; a factor 2 in the "
            "lattice rate moves omega_x by %.4f eV" % (slope, slm, np.log(2) / max(slope - slm, 1e-30)))
        out("  m = %6.1f MeV: q_max = %6.1f keV, E_R^max = %8.4f eV, 2W(q_max) = %6.2f, x_R(q_max) = %6.2f; total lattice "
            "%.3e, Migdal %.3e (zero-phonon share %.3f); crossover omega_x = %.3f eV = %.2f E_R^max = %.1f omega_top; "
            "rate there %.3e /kg/yr; lattice part at omega_x: multiphonon %.3f, Gaussian %.3f"
            % (m / 1e6, qmax / 1e3, ermax, I.two_w(qmax), ermax / I.W_MEAN, lat[0], mig[0], r["mig0"][0] / mig[0], wx,
               wx / ermax, wx / 0.06365, np.interp(wx, WF, mig), r["multi"][k] / max(lat[k], 1e-300),
               r["gauss"][k] / max(lat[k], 1e-300)))
    # WE numbers at 10 MeV: Poisson-tail estimate
    m = 10e6
    qmax = 2 * mu(m, M) * VMAX
    tw = I.two_w(qmax)
    ermax = qmax**2 / (2 * M)
    pmig = G.p_total(ermax)
    out("WE 17.1 (m = 10 MeV): Migdal probability per kick at the endpoint E_R = %.4f eV: %.3e (%.3e per eV of recoil)"
        % (ermax, pmig, pmig / ermax))
    for N in range(6, 14):
        out("  Poisson tail at 2W = %.3f: P(n >= %2d) = %.3e  -> energy %.3f eV at %.1f meV per phonon"
            % (tw, N, poisson.sf(N - 1, tw), N * 0.06365, 63.65))
    r = nucleon_rates(m, np.array([0.1, 0.2, 0.3, 0.5]))
    for j, w in enumerate((0.1, 0.2, 0.3, 0.5)):
        out("  10 MeV, omega_th = %.1f eV: lattice %.3e, Migdal %.3e (zero-phonon %.3e, phonon-dressed %.3e) /kg/yr"
            % (w, r["one"][j] + r["multi"][j] + r["gauss"][j], r["mig0"][j] + r["migp"][j], r["mig0"][j], r["migp"][j]))
    # spectrum check: n-phonon order that dominates the lattice spectrum near the crossover at q_max
    s1, sm = s_incoh(np.array([qmax]))
    n = np.arange(NMAX + 1)
    wts = np.exp(poisson.logpmf(n, tw))
    for wq in (0.2, 0.3, 0.4):
        j = int(round(wq / H))
        contrib = wts * PN[:, j]
        out("  q_max, omega = %.1f eV: dominant phonon number %d (share %.2f); s = %.3e /eV" %
            (wq, contrib.argmax(), contrib.max() / contrib.sum(), contrib.sum()))
    # ---- maps ------------------------------------------------------------------------------------------------------
    MS = np.geomspace(3e3, 1e9, 64)
    WTH = np.geomspace(1e-3, 50.0, 96)
    keys = ("one", "multi", "gauss", "mig0", "migp", "qmed_lat")
    NUC = {k: np.zeros((len(MS), len(WTH))) for k in keys}
    for i, m in enumerate(MS):
        r = nucleon_rates(m, WTH)
        for k in keys:
            NUC[k][i] = r[k]
    ER = np.zeros((len(MS), len(WTH)))
    AC = np.zeros((len(MS), len(WTH)))
    for i, m in enumerate(MS):
        ER[i], AC[i] = electron_rates(m, WTH)
    np.savez(os.path.join(HERE, "sectors17.npz"), MS=MS, WTH=WTH, ER=ER, AC=AC, **NUC)
    out("grid: %d masses 3 keV-1 GeV, %d thresholds 1 meV-50 eV; saved sectors17.npz" % (len(MS), len(WTH)))
    # ---- boundaries on fine mass grids ----------------------------------------------------------------------------
    MF = np.geomspace(0.1e6, 1e9, 400)
    w1 = np.array([1e-3])
    one, mul, mz, mp, er, ac = [], [], [], [], [], []
    for m in MF:
        r = nucleon_rates(m, w1, nq=120)
        one.append(r["one"][0]); mul.append(r["multi"][0] + r["gauss"][0]); mz.append(r["mig0"][0]); mp.append(r["migp"][0])
        e, a = electron_rates(m, w1)
        er.append(e[0]); ac.append(a[0])
    one, mul, mz, mp, er, ac = map(np.array, (one, mul, mz, mp, er, ac))
    out("At omega_th = 1 meV (fine mass grid of %d points, 0.1 MeV-1 GeV):" % len(MF))
    out("  one-phonon = multiphonon (n >= 2 incl. impulse) at m = %.2f MeV" % (cross_log(MF, one, mul) / 1e6))
    hi = MF >= 1e6                 # below 1 MeV both Migdal parts approach zero at the kinematic floor
    out("  zero-phonon Migdal = phonon-dressed Migdal at m = %.2f MeV" % (cross_log(MF[hi], mz[hi], mp[hi]) / 1e6))
    out("  electron coupling: zero-phonon electron recoil = electron-following acoustic peak (model) at m = %.1f MeV"
        % (cross_log(MF, ac, er) / 1e6))
    for mm in (1e6, 10e6, 100e6):
        k = np.argmin(abs(MF - mm))
        out("  m = %.0f MeV: acoustic peak / electron recoil = %.3g; lattice / Migdal (nucleon) = %.3g"
            % (MF[k] / 1e6, ac[k] / max(er[k], 1e-300), (one[k] + mul[k]) / (mz[k] + mp[k])))
    LOG.close()
