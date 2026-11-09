"""Shared model for Sect. 14.6 (coherent fields and precessing nuclear spins).  Imported by we14_6.py, fig14_6.py,
limit14_6a.py, limit14_6b.py and limit14_6c.py; prints nothing itself.

Units.  Energies of the field line are measured from the rest energy m_phi in units of m_phi v0^2, so that
    x = (omega - m_phi)/(m_phi v0^2) = v^2/(2 v0^2),
and times in units of the coherence time t_coh = 1/(m_phi v0^2) (book definition, eq:14.6-tcoh; NOTATION row t_coh;
Ch11 ruling R7).  Some papers use 2 pi/(m v^2) (Budker et al. 1306.6089 p.1; Centers et al. 1905.13650); the scripts
never do.

Halo.  Standard halo model of Sect. 1.2 (eq:1.2-fgal): Maxwellian with v0 = 238 km/s truncated at v_esc = 544 km/s in
the galactic frame, boosted by the Earth's speed v_E = 250.5 km/s (v_E^ref, Sect. 1.2; Baxter et al. 2105.00599 Table 1).
The laboratory speed distribution F_chi(v) is computed by integrating the boosted, truncated Maxwellian over the angle
between v and v_E (the escape cut is applied in the galactic frame).  The field's energy distribution is
    F_phi(omega) d omega = F_chi(v) dv  (book eq:11.8 F_phi; eq:14.6-Fphi),
i.e. in x units F_x(x) = F_chi(v) v0^2 / v with v = v0 sqrt(2x).

Field.  phi(t) = Re[Phi(t) e^{-i m t}] with Phi a stationary complex Gaussian process of unit mean square
(<|Phi|^2> = 1 in units of phi_0^2 = 2 rho_chi/m^2) whose power spectrum, in the x variable, is 2 pi F_x(x):
    <Phi(t) Phi*(0)> = int dx F_x(x) e^{-i x t}  (t in units of t_coh).
Monte Carlo realizations are sums of N_modes plane-wave modes with velocities drawn from the boosted, truncated
Maxwellian, equal amplitudes and uniform random phases (central-limit construction of Foster, Rodd and Safdi,
1711.10489 Eqs. (3)-(10)).
"""
import numpy as np
from scipy import stats, optimize

KMS = 1.0 / 299792.458          # km/s in units of c
V0 = 238.0                      # km/s, Sect. 1.2
VESC = 544.0                    # km/s, Sect. 1.2
VE = 250.5                      # km/s, v_E^ref, Sect. 1.2
HBAR = 6.582119569e-16          # eV s (CODATA)
HBARC = 1.973269804e-7          # eV m (CODATA)
H_PLANCK = 4.135667696e-15      # eV s (CODATA)


def speed_pdf(v, v0=V0, vesc=VESC, ve=VE, nc=801):
    """Laboratory speed distribution F_chi(v) in (km/s)^-1, normalized numerically."""
    v = np.atleast_1d(v).astype(float)
    c = np.linspace(-1.0, 1.0, nc)
    vv = v[:, None]
    vg2 = vv ** 2 + ve ** 2 + 2.0 * vv * ve * c[None, :]
    integ = np.exp(-vg2 / v0 ** 2) * (vg2 < vesc ** 2)
    f = 2.0 * np.pi * v ** 2 * np.trapezoid(integ, c, axis=1)
    return f


_vgrid = np.linspace(0.0, VESC + VE, 6001)
_fgrid = speed_pdf(_vgrid)
_norm = np.trapezoid(_fgrid, _vgrid)
_fgrid = _fgrid / _norm


def speed_pdf_norm(v):
    return np.interp(v, _vgrid, _fgrid, right=0.0)


def Fx(x):
    """Energy distribution of the field line in x = (omega - m)/(m v0^2); integrates to 1."""
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    pos = x > 0
    v = V0 * np.sqrt(2.0 * x[pos])
    out[pos] = speed_pdf_norm(v) * V0 ** 2 / v
    return out


XMAX = ((VESC + VE) / V0) ** 2 / 2.0
xg = np.concatenate([np.linspace(0.0, 0.05, 2001)[1:], np.linspace(0.05, XMAX, 40000)[1:]])
Fg = Fx(xg)
NORM_X = np.trapezoid(Fg, xg)        # should be 1 to numerical accuracy
X_PEAK = xg[np.argmax(Fg)]
F_PEAK = Fg.max()
X_MEAN = np.trapezoid(xg * Fg, xg)
DW_EQ = 1.0 / np.trapezoid(Fg ** 2, xg)  # equivalent width of the line in x units (Delta omega_eq t_coh)


def fejer_mean(x0, T):
    """Mean periodogram of the unit-power field at x0 for a record of length T (t_coh units), divided by 2 pi:
    int dx F(x) (T/2pi) sinc^2((x - x0) T/2).  Equals F(x0) for T -> infinity."""
    d = (xg - x0) * T / 2.0
    k = (T / (2.0 * np.pi)) * np.sinc(d / np.pi) ** 2
    return np.trapezoid(Fg * k, xg)


def bloch_ms(t, T2, x_lar):
    """Ensemble mean of |M_+|^2 / (M0 Omega_rms)^2 at time t for the linearized Bloch equation driven by the
    Gaussian field (t, T2 in t_coh units; Larmor frequency at x_lar):
        int dx F(x) |1 - exp(-(i D + g) t)|^2 / (D^2 + g^2),  D = x_lar - x, g = 1/T2."""
    g = 0.0 if np.isinf(T2) else 1.0 / T2
    D = x_lar - xg
    num = 1.0 - 2.0 * np.exp(-g * t) * np.cos(D * t) + np.exp(-2.0 * g * t)
    den = D ** 2 + g ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        r = np.where(den > 1e-300, num / den, t ** 2)
    return np.trapezoid(Fg * r, xg)


def absorbed_ratio(t, T2, x_lar):
    """Mean energy absorbed by the linearly driven spins up to t, divided by (golden-rule rate) x t:
    int dx F(x) int_0^t Re[(1 - e^{-(iD+g)t'})/(iD+g)] dt' / (t int dx F(x) g/(D^2+g^2)).
    For g -> 0 the golden-rule denominator is pi F(x_lar)."""
    g = 0.0 if np.isinf(T2) else 1.0 / T2
    D = xg - x_lar
    if g == 0.0:
        # int_0^t sin(D t')/D dt' = (1 - cos D t)/D^2 = (t^2/2) sinc^2(D t/2)
        inner = 0.5 * t ** 2 * np.sinc(D * t / (2.0 * np.pi)) ** 2
        return np.trapezoid(Fg * inner, xg) / (t * np.pi * np.interp(x_lar, xg, Fg))
    z = 1j * D + g
    # int_0^t (1 - e^{-z t'})/z dt' = t/z - (1 - e^{-z t})/z^2
    inner = np.real(t / z - (1.0 - np.exp(-z * t)) / z ** 2)
    gr = np.trapezoid(Fg * g / (D ** 2 + g ** 2), xg)
    return np.trapezoid(Fg * inner, xg) / (t * gr)


def sample_velocities(n, rng):
    """Draw n laboratory velocities (km/s, 3-vectors) from the truncated Maxwellian boosted by v_E along z."""
    out = np.empty((0, 3))
    while len(out) < n:
        vg = rng.normal(0.0, V0 / np.sqrt(2.0), size=(2 * n, 3))
        vg = vg[np.sum(vg ** 2, axis=1) < VESC ** 2]
        out = np.vstack([out, vg - np.array([0.0, 0.0, VE])])
    return out[:n]


def mc_periodogram(T, xk, n_modes, n_real, rng):
    """Monte Carlo periodograms P(x_k) = |int_0^T Phi(t) e^{i x_k t} dt|^2 / T / (2 pi) of the unit-power field,
    exact continuous-time transform of each plane-wave mode.  Returns an array (n_real, len(xk))."""
    res = np.empty((n_real, len(xk)))
    for r in range(n_real):
        v = sample_velocities(n_modes, rng)
        xj = np.sum(v ** 2, axis=1) / (2.0 * V0 ** 2)
        ph = rng.uniform(0.0, 2.0 * np.pi, n_modes)
        a = np.exp(1j * ph) / np.sqrt(n_modes)
        d = xk[None, :] - xj[:, None]          # e^{-i x_j t} e^{i x_k t}
        with np.errstate(invalid="ignore", divide="ignore"):
            kern = np.where(np.abs(d) > 1e-12, (np.exp(1j * d * T) - 1.0) / (1j * d), T)
        amp = np.sum(a[:, None] * kern, axis=0)
        res[r] = np.abs(amp) ** 2 / T / (2.0 * np.pi)
    return res


# ---- sensitivity model of Limit Check 14.6c (box line with N_eff bins; exact Neyman, median 95 % CL upper limit)
def n_eff(T):
    """Participation number of the Fejer-windowed bin powers for a record T (t_coh units)."""
    dk = 2 * np.pi / T
    kmax = int(np.ceil((XMAX + 40.0 / T) / dk)) + 2
    kmin = -int(np.ceil((X_PEAK + 40.0 / T) / dk)) - 2
    if kmax - kmin > 4000:
        # long records: bins much narrower than the line, N_eff -> T DW/2pi with the Fejer smoothing negligible
        xk = np.arange(0.0, XMAX, dk / 4.0)
        p = Fx(xk)
        return T * DW_EQ / (2 * np.pi) * (1.0 + 0.0 * p.sum())
    ks = np.arange(kmin, kmax + 1)
    xk = X_PEAK + ks * dk
    p = np.array([fejer_mean(x, T) for x in xk])
    p = p / p.sum()
    return 1.0 / np.sum(p ** 2)


def s_up_stoch(N, b=1.0):
    qmed = stats.gamma.median(N, scale=b)
    f = lambda s: stats.gamma.cdf(qmed, N, scale=b + s / N) - 0.05
    return optimize.brentq(f, 1e-9, 1e6)


def s_up_det(N, b=1.0):
    qmed = stats.gamma.median(N, scale=b)
    f = lambda s: stats.ncx2.cdf(2 * qmed / b, 2 * N, 2 * s / b) - 0.05
    return optimize.brentq(f, 1e-9, 1e6)


