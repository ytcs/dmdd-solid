"""Worked example 11.10 (Sect. 11.9): the nuisance band on the silicon multiphonon rate at m_chi = 30 MeV.
Prints every number of the example and of the paragraphs around it.  Log: we11_10.log.

Rate (orientation-averaged, heavy mediator F_DM = 1, equal couplings to protons and neutrons, c_kappa = A):
  dR/domega = [rho_chi sigma_p A^2 / (2 m_chi mu_p^2)] (1/M) int dq q F_N(q)^2 s(q, omega) eta(omega/q + q/2 m_chi),
  per unit target mass, with s the response of one nucleus normalized to one (zero-phonon line excluded, omega > 0).  For
  s = delta(omega - q^2/2M) this is the free-recoil rate rho sigma_N F^2 eta/(2 m mu_N^2) of eq:11.4-LS (same normalization as
  limit11_4a.py, which takes the ratio).  rho_chi = 0.3 GeV/cm^3, sigma_p = 1e-40 cm^2 (the heavy-mediator normalization of
  Fig. 11.1), halo of Sect. 1.2 (v0, v_esc, v_E = 238, 544, 250.5 km/s; eta from phon11.py), Helm F_N (imp11.helm), A = 28.0855.
Response: incoherent T = 0 harmonic response of Sect. 11.3, all phonon orders, from the PBE density of states of Sect. 5.2
  (imp11.py: G, P1 = g/omega normalized, 2W = E_R <omega^-1>), P_n = n-fold convolution of P1 on a 0.1-meV grid
  (P1 placed on the grid points k h by linear interpolation; checked against imp11.spectrum below).
Threshold (environment variable WTH, eV; default 0.100): omega_th = 100 meV, above the one-phonon band (omega_max = 63.7 meV), so that every event counted has at least two
  phonons.  m_chi = 30 MeV: maximum momentum transfer 2 m v_max = 159 keV, free-recoil endpoint 0.48 eV.
Nuisance templates (delta_k = rate at the next order / rate - 1):
  (1) coherent remainder: exact harmonic omega-integrated n-phonon weight, factor 1 + delta^coh_n(q) per order (eq:11.3-weight),
      delta^coh_n from the pair sum of limit11_3a.py (T = 0 PBE B_kk'(dR) on 48^3, pairs to 40 A, exact direction average),
      n = 2..8 (|delta^coh_n| < 1e-3 beyond, printed).  One phonon does not reach 100 meV.  This is a computed next order:
      the central value moves; the residual is the pointwise distribution of the coherent weight inside each band.
  (2) harmonic inputs: all phonon frequencies scaled by 1 + eps.  Template size eps = 0.026, the mean absolute difference
      between the PBE and the eight measured frequencies at Gamma, X and L (Sect. 5.2); for comparison eps = 0.006 (zone-center
      optical mode, 63.7 vs 64.1 meV, Sect. 5.2) and eps = 0.021 (sphere-averaged longitudinal speed 8.83 vs 9.017 km/s,
      Sect. 11.1).  The deviations have both signs, so a uniform scaling by the mean absolute difference is an upper template.
  (3) anharmonic kinetic energy (n_A = 2): the nuclear kinetic energy changes by -0.137 % and +0.083 % in the two silicon-like
      single-site models of limit11_5a.log; template = dilation of each spectrum about E_R by (1 + dK/K)^(1/2) at fixed area and
      mean (changes the second moment by the computed amount, leaves zeroth and first moments exact); evaluated to first order
      through the analytic derivative of the rate with respect to the dilation (finite dilations of 1e-3 are below the grid).
  (4) anharmonic skewness (n_A = 2), estimate: third cumulant changed at relative order eta_anh^2 = 2.4e-3 (Sects. 5.7, 8.8);
      the whole harmonic shape beyond mean and variance moves the rate by R_inc/R_gauss - 1 (Gaussian with the same mean and
      variance, weight 1 - e^{-2W}); the estimate is eta_anh^2 times that.
  Evaluation-error comparison (not a nuisance): the free-recoil rate above the same threshold.
  Markov-Krein band (eq:C.10-band) on the weight above threshold at q = 120 keV, from the five exact moments (mk11.py).
"""
import os
import sys
import numpy as np
from scipy.special import spherical_jn
from numpy.polynomial import legendre as Lg

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402
import phon11 as P  # noqa: E402
import mph11 as MP  # noqa: E402
import mk11 as K  # noqa: E402

A = 28.0855
MCHI = 30e6
WTH = float(os.environ.get("WTH", "0.100"))
SIGP = 1e-40
H = 0.1e-3                       # eV, omega grid
NW = 2**15                       # 3.28 eV
NMAX = 60
W = np.arange(NW) * H
QMAX = 2 * MCHI * P.VMAX
PREF = P.RHO_CHI * SIGP * P.CM2 * A**2 / (2 * MCHI * P.mu(MCHI, P.M_P)**2) * P.KG * P.YEAR   # per eV of omega x eta


def pn_table(eps=0.0):
    """P_n(omega) on the grid W for n = 1..NMAX, phonon frequencies scaled by (1 + eps)."""
    g = np.interp(W, I.WG * (1 + eps), I.G, left=0, right=0)
    p1 = np.where(W > 0, g / np.maximum(W, 1e-12), 0.0)
    p1 /= p1.sum() * H
    winv = 1 / (np.sum(g / np.maximum(W, 1e-12) * (W > 0)) * H / (g.sum() * H))   # <omega^-1>^-1
    f = np.fft.rfft(p1 * H)
    out = np.empty((NMAX, NW))
    fn = np.ones_like(f)
    for n in range(NMAX):
        fn = fn * f
        out[n] = np.fft.irfft(fn, NW) / H
    return np.maximum(out, 0.0), winv


def poisson(x, nmax=NMAX):
    n = np.arange(1, nmax + 1)
    from scipy.special import gammaln
    return np.exp(-x + n * np.log(x) - gammaln(n + 1))


QS = np.geomspace(2e3, QMAX, 500)


def rate(PN, winv, wth=WTH, coh=None, dil=None, gauss=False):
    """Events per kg-yr above wth."""
    above = W >= wth
    vals = np.zeros(len(QS))
    for i, q in enumerate(QS):
        er = I.e_r(q)
        tw = er / winv
        if gauss:
            var = er * I.W_MEAN
            s = (1 - np.exp(-tw)) * np.exp(-(W - er)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)
        else:
            wts = poisson(tw)
            if coh is not None:
                wts = wts * (1 + coh(q))
            s = wts @ PN
        if dil is None:
            wv = W
        else:
            wv = er + dil * (W - er)
        sel = above if dil is None else (wv >= wth)
        et = P.eta(np.maximum(wv, 1e-12) / q + q / (2 * MCHI))
        vals[i] = q * I.helm(q, A)[0]**2 * np.sum(s[sel] * et[sel]) * H / I.M
    return PREF * np.trapezoid(vals, QS), vals


def rate_free(wth=WTH):
    mu = MCHI * I.M / (MCHI + I.M)
    emax = 2 * mu**2 * P.VMAX**2 / I.M
    E = np.linspace(wth, emax, 20000)
    qw = np.sqrt(2 * I.M * E)
    return PREF * np.trapezoid(I.helm(qw, A)[0]**2 * P.eta(qw / (2 * mu)), E), emax


# ---------- coherent remainder delta^coh_n(q), as limit11_3a.py ----------
def coherent_table(nlist, qk):
    Bd = MP.B_tensor(48)
    ux2 = Bd["B"][0, 0, 0, 0, 0].real[0, 0]
    d, kk, Bp = MP.pair_table(Bd, rmax=40.0)
    Bp = Bp.real / ux2
    r = np.linalg.norm(d, axis=1)
    ns = r > 1e-6
    d, Bp, r = d[ns], Bp[ns], r[ns]
    zh = d / r[:, None]
    tmp = np.where(np.abs(zh[:, 0:1]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
    xh = np.cross(zh, tmp)
    xh /= np.linalg.norm(xh, axis=1)[:, None]
    yh = np.cross(zh, xh)
    out = {}
    for n in nlist:
        mu, _ = Lg.leggauss(2 * n + 1)
        nphi = 4 * n + 4
        phi = 2 * np.pi * np.arange(nphi) / nphi
        vals = np.zeros((len(r), len(mu)))
        for i, m in enumerate(mu):
            s = np.sqrt(1 - m * m)
            qh = (s * np.cos(phi)[None, :, None] * xh[:, None, :] + s * np.sin(phi)[None, :, None] * yh[:, None, :]
                  + m * zh[:, None, :])
            b = np.einsum("pfa,pab,pfb->pf", qh, Bp, qh)
            vals[:, i] = (b ** n).mean(1)
        a = np.linalg.solve(Lg.legvander(mu, 2 * n), vals.T).T
        row = []
        for q in qk:
            x = q / MP.HBARC * r
            tot = 0.0
            for l in range(2 * n + 1):
                tot = tot + a[:, l] * ((-1j) ** l) * spherical_jn(l, x)
            row.append(np.real(tot.sum()) / MP.NAT)
        out[n] = np.array(row)
    return out


if __name__ == "__main__":
    print("m_chi = %.0f MeV, q_max = %.1f keV, E_R(q_max) = %.3f eV, x_R(q_max) = %.1f; threshold %.0f meV"
          % (MCHI / 1e6, QMAX / 1e3, I.e_r(QMAX), I.e_r(QMAX) / I.W_MEAN, WTH * 1e3))
    PN, winv = pn_table()
    print("grid check: <omega^-1>^-1 = %.2f meV (imp11 %.2f)" % (winv * 1e3, I.W_INV * 1e3))
    for qk in (50.0, 120.0):
        q = qk * 1e3
        tw = I.e_r(q) / winv
        s = poisson(tw) @ PN
        w2, s2, e0 = I.spectrum(q, h=I.DW, wtop=1.5)
        a1 = s[W >= WTH].sum() * H
        a2 = s2[w2 >= WTH].sum() * I.DW
        print("check q = %.0f keV: weight above threshold %.5f (convolution) vs %.5f (FFT of imp11); total %.5f vs 1-e^-2W %.5f"
              % (qk, a1, a2, s.sum() * H, 1 - np.exp(-tw)))
    R0, v0 = rate(PN, winv)
    Rfree, emax = rate_free()
    cum = np.cumsum(v0 * np.gradient(QS))
    cum /= cum[-1]
    qmed = np.interp(0.5, cum, QS)
    q10, q90 = np.interp(0.1, cum, QS), np.interp(0.9, cum, QS)
    print("central (incoherent, harmonic, PBE DOS): R = %.4g /kg/yr above %.0f meV (%.1f per kg-day)" % (R0, WTH * 1e3, R0 / 365.25))
    print("   rate-weighted q: median %.1f keV (x_R = %.2f), 10-90 %%: %.1f-%.1f keV (x_R %.2f-%.2f)"
          % (qmed / 1e3, I.e_r(qmed) / I.W_MEAN, q10 / 1e3, q90 / 1e3, I.e_r(q10) / I.W_MEAN, I.e_r(q90) / I.W_MEAN))
    for qc in (20e3, 30e3):
        sel = QS <= qc
        print("   share of the rate from q <= %.0f keV (E_R <= %.1f meV): %.1e" % (qc / 1e3, I.e_r(qc) * 1e3,
              np.trapezoid(v0[sel], QS[sel]) * PREF / R0))
    print("   free-recoil rate above threshold: %.4g /kg/yr (endpoint %.3f eV); free/crystal = %.3f" % (Rfree, emax, Rfree / R0))
    R1m, _ = rate(PN, winv, wth=1e-3)
    print("   for reference, same rate above 1 meV: %.4g /kg/yr" % R1m)

    # (1) coherent remainder
    nl = list(range(2, 9))
    qk = np.geomspace(2e3, QMAX, 70)
    D = coherent_table(nl, qk)
    for n in nl:
        sel = qk > 30e3
        print("delta^coh_%d: max |.| for q > 30 keV = %.2e; at 50, 100, 150 keV: %+.2e %+.2e %+.2e"
              % (n, np.abs(D[n][sel]).max(), *np.interp([50e3, 100e3, 150e3], qk, D[n])))

    def coh(q):
        c = np.zeros(NMAX)
        for n in nl:
            c[n - 1] = np.interp(q, qk, D[n])
        return c
    Rc, _ = rate(PN, winv, coh=coh)
    d_coh = Rc / R0 - 1
    print("(1) coherent remainder: R = %.4g, delta = %+.2e" % (Rc, d_coh))

    # (2) frequency scale
    for eps in (0.006, 0.021, 0.026):
        PNe, winve = pn_table(eps)
        Re, _ = rate(PNe, winve)
        print("(2) phonon frequencies x (1 + %.3f): <omega^-1>^-1 %.2f meV, R = %.4g, delta = %+.4f" % (eps, winve * 1e3, Re, Re / R0 - 1))
        if eps == 0.026:
            d_freq = Re / R0 - 1

    # (3) anharmonic kinetic energy
    # dilation omega -> E_R + lam (omega - E_R): derivative of the rate at lam = 1, evaluated analytically per q
    # (a finite dilation of 1e-3 moves the grid by less than one cell and is dominated by the discretization of the threshold):
    # dI/dlam = int_{w >= wth} s(w) (w - E_R) d eta/dv / q dw  -  s(wth) eta(wth/q + q/2m) (E_R - wth)
    dvals = np.zeros(len(QS))
    for i, q in enumerate(QS):
        er = I.e_r(q)
        s = poisson(er / winv) @ PN
        v = W / q + q / (2 * MCHI)
        dv = 1e-7
        deta = (P.eta(v + dv) - P.eta(v - dv)) / (2 * dv)
        ab = W >= WTH
        inner = np.sum(s[ab] * (W[ab] - er) * deta[ab] / q) * H
        bnd = np.interp(WTH, W, s) * P.eta(WTH / q + q / (2 * MCHI)) * (er - WTH)
        dvals[i] = q * I.helm(q, A)[0]**2 * (inner - bnd) / I.M
    dR = PREF * np.trapezoid(dvals, QS)
    c_dil = dR / R0
    print("(3) dilation coefficient d ln R / d ln(width) = %+.4f" % c_dil)
    d_kin = []
    for dk in (-0.137e-2, 0.083e-2):
        lam = np.sqrt(1 + dk)
        d_kin.append(c_dil * (lam - 1))
        print("(3) kinetic energy %+.3f %%: width x %.5f, delta = %+.2e" % (dk * 100, lam, c_dil * (lam - 1)))
    # (4) skewness estimate
    Rg, _ = rate(PN, winv, gauss=True)
    eta2 = 2.4e-3
    d_shape = R0 / Rg - 1
    d_skew = eta2 * d_shape
    print("(4) Gaussian of same mean and variance: R = %.4g; R_inc/R_gauss - 1 = %+.4f; times eta_anh^2 = %.1e: delta = %+.1e"
          % (Rg, d_shape, eta2, d_skew))

    # band
    ks = {"frequency scale (PBE vs measured)": d_freq, "anharmonic kinetic energy": max(d_kin, key=abs),
          "anharmonic skewness (est.)": d_skew}
    logs = {k: np.log1p(v) for k, v in ks.items()}
    sig = np.sqrt(sum(v**2 for v in logs.values()))
    for k, v in logs.items():
        print("   ln(1 + delta) %-36s %+.2e  (variance share %.3f)" % (k, v, v**2 / sig**2))
    Rcen = Rc
    print("central value after the computed coherent step: %.4g /kg/yr; residual coherent nuisance (pointwise) not in the band"
          % Rcen)
    print("sigma_ln R = %.2e; band %.4g to %.4g /kg/yr (factor %.4f)" % (sig, Rcen / np.exp(sig), Rcen * np.exp(sig), np.exp(sig)))
    print("free recoil against the band: (free - central)/central = %+.3f, %.0f band widths" % (Rfree / Rcen - 1, np.log(Rfree / Rcen) / sig))

    # Markov-Krein band on the weight above threshold at q where the rate peaks and at 120 keV
    for qkv in (qmed / 1e3, 120.0):
        q = qkv * 1e3
        w, s, e0, F, mu, num = K.si_response(q)
        zm, m1, sg = K.standardize(mu)
        xi = (WTH - m1) / sg
        lo, hi, rho, nmin = K.band(zm, [xi])
        true = 1 - np.interp(WTH, w, F)
        print("MK at q = %.1f keV (E_R %.0f meV, sigma %.0f meV): threshold at xi = %.2f; weight above in [%.3f, %.3f], harmonic %.3f"
              % (qkv, m1 * 1e3, sg * 1e3, xi, 1 - hi[0], 1 - lo[0], true))
