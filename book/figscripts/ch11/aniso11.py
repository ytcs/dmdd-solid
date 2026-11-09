"""Shared inputs for Sect. 11.7 (anisotropy and daily modulation): cubic harmonics, halo moments, laboratory geometry.
Used by elf11_7.py, lat11_7.py, limit11_7a.py, fig11_7.py and we11_8.py. Run directly to print the checks.

Halo: the book's standard halo model (App. A.8; Baxter et al., arXiv:2105.00599, Table 1): v0 = 238, v_esc = 544,
  |v_E| = v_E^ref = 250.5 km/s; f_chi(v) = f_gal(v + v_E) with f_gal = exp(-u^2/v0^2) Theta(v_esc - u) / N_esc (eq:1.2-flab).
Halo moments (eq:11.7-ups): for a momentum transfer q at angle arccos(x) to v_E, the velocity integral is
  int d^3v f_chi(v) delta(omega - omega_q) = (1/q) fhat(v_* + v_E x),  v_* = omega/q + q/(2 m_chi),
  fhat(s) = (pi v0^2/N_esc) [exp(-s^2/v0^2) - exp(-v_esc^2/v0^2)] Theta(v_esc - |s|)   (Radon transform of the truncated Maxwellian),
  Upsilon_l(v_*) = int_{-1}^{1} dx P_l(x) fhat(v_* + v_E x);  Upsilon_0 = eta(v_min = v_*) (checked below against App. D.1).
  (Same object as Al-Adulrazzaq et al., arXiv:2607.06005, Eqs. (13), (17), up to their normalization 2 pi Y_l0.)
Cubic harmonics: Y^c_l(n) = N_l [P_l(n_x) + P_l(n_y) + P_l(n_z)], l = 0, 4, 6, 8, 10 (the unique O_h invariant at these l), N_l from
  numerical normalization on the sphere; Y^c_4 equals eq:C.3-cubic (checked below).
Laboratory geometry (Sect. 1.2): the direction of v_sun in (east, north, up) axes at latitude lat and hour angle h (eq:1.2-local),
  declination delta_E = 47.5 deg (eq:1.2-thetaE); h advances at the sidereal rate.  We use the direction of v_sun for v_E(t)
  (Sect. 1.2: the orbital motion moves it by a few degrees over the year) and |v_E| = 250.5 km/s.
"""
import numpy as np
from scipy.special import erf, eval_legendre

C_KMS = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
_Z = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))   # (km/s)^3, eq:1.2-nesc
DELTA_E = np.radians(47.5)


def fhat(s):
    """Radon transform of the truncated Maxwellian, (km/s)^-1, s in km/s."""
    s = np.asarray(s, float)
    return np.where(np.abs(s) < VESC, np.pi * V0**2 / NESC * (np.exp(-s**2 / V0**2) - np.exp(-_Z**2)), 0.0)


_XG, _WG = np.polynomial.legendre.leggauss(400)


def upsilon(l, vstar_kms, ve=VE):
    """Upsilon_l(v_*) in (km/s)^-1; vstar may be an array. Gauss-Legendre in x on [-1, 1], with the support split."""
    vs = np.atleast_1d(np.asarray(vstar_kms, float))
    out = np.zeros(vs.shape)
    for i, v in enumerate(vs.ravel()):
        lo = max(-1.0, (-VESC - v) / ve)
        hi = min(1.0, (VESC - v) / ve)
        if hi <= lo:
            continue
        x = 0.5 * (hi - lo) * _XG + 0.5 * (hi + lo)
        out.ravel()[i] = 0.5 * (hi - lo) * np.sum(_WG * eval_legendre(l, x) * fhat(v + ve * x))
    return out.reshape(np.shape(vstar_kms)) if np.ndim(vstar_kms) else out[0]


def ycub(l, n):
    """Cubic harmonic Y^c_l for unit vectors n (..., 3), l in {0, 4, 6, 8, 10}."""
    n = np.asarray(n, float)
    if l == 0:
        return np.full(n.shape[:-1], 1 / np.sqrt(4 * np.pi))
    f = eval_legendre(l, n[..., 0]) + eval_legendre(l, n[..., 1]) + eval_legendre(l, n[..., 2])
    return _NORM[l] * f


def sphere_grid(nt=64, nphi=128):
    x, w = np.polynomial.legendre.leggauss(nt)
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    X, P = np.meshgrid(x, ph, indexing="ij")
    W = np.repeat(w[:, None], nphi, axis=1) * (2 * np.pi / nphi)      # sums to 4 pi
    s = np.sqrt(1 - X**2)
    q = np.stack([s * np.cos(P), s * np.sin(P), X], axis=-1).reshape(-1, 3)
    return q, W.reshape(-1)


_QS, _WS = sphere_grid()
_NORM = {}
for _l in (4, 6, 8, 10):
    _f = sum(eval_legendre(_l, _QS[:, i]) for i in range(3))
    _NORM[_l] = 1 / np.sqrt(np.sum(_WS * _f**2))


def ylm_real(l, n):
    """Real spherical harmonics (l, m = -l..l) for unit vectors n, Condon-Shortley; returns (2l+1, ...)."""
    from scipy.special import sph_harm_y
    n = np.asarray(n, float)
    th = np.arccos(np.clip(n[..., 2], -1, 1))
    ph = np.arctan2(n[..., 1], n[..., 0])
    out = []
    for m in range(-l, l + 1):
        Y = sph_harm_y(l, abs(m), th, ph)
        if m == 0:
            out.append(Y.real)
        elif m > 0:
            out.append(np.sqrt(2) * (-1)**m * Y.real)
        else:
            out.append(np.sqrt(2) * (-1)**m * Y.imag)
    return np.array(out)


def vhat_local(lat_deg, h):
    """Direction of v_sun in (east, north, up) axes, eq:1.2-local; h = hour angle (rad), array allowed."""
    lat = np.radians(lat_deg)
    d = DELTA_E
    e = -np.cos(d) * np.sin(h)
    nn = np.cos(lat) * np.sin(d) - np.sin(lat) * np.cos(d) * np.cos(h)
    u = np.sin(lat) * np.sin(d) + np.cos(lat) * np.cos(d) * np.cos(h)
    return np.stack([e, nn, u], axis=-1)


def vhat_crystal(lat_deg, h, R=np.eye(3)):
    """Direction of v_E in crystal axes; rows of R are the crystal axes in (east, north, up) components."""
    return vhat_local(lat_deg, h) @ np.asarray(R).T


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import phon11 as P
    # check 1: Upsilon_0 = eta (App. D.1)
    for v in (0.0, 100.0, 300.0, 500.0, 700.0, 790.0):
        print("v_* = %5.0f km/s: Upsilon_0 = %.6e, eta = %.6e (km/s)^-1" % (v, upsilon(0, v), P.eta_kms(v)))
    # check 2: Y^c_4 against eq:C.3-cubic
    n = _QS[::997]
    c3 = 5 / 8 * np.sqrt(21 / np.pi) * ((n**4).sum(1) - 3 / 5)
    print("max |Y^c_4 - eq:C.3-cubic| = %.1e" % np.abs(ycub(4, n) - c3).max())
    for l in (4, 6, 8):
        print("Y^c_%d at [100], [110], [111]: %+.4f %+.4f %+.4f" % (
            l, ycub(l, np.array([1, 0, 0.])), ycub(l, np.array([1, 1, 0.]) / np.sqrt(2)), ycub(l, np.ones(3) / np.sqrt(3))))
    for l in (4, 6):
        for l2 in (0, 4, 6, 8):
            print("  <Y^c_%d Y^c_%d> = %+.2e" % (l, l2, np.sum(_WS * ycub(l, _QS) * ycub(l2, _QS))))
    # halo moments relative to Upsilon_0
    for v in (100, 300, 500, 600, 700):
        print("v_* = %d: Upsilon_l/Upsilon_0, l = 1..6: %s" % (v, np.round([upsilon(l, v) / upsilon(0, v) for l in range(1, 7)], 4)))


def fit_cubic(dirs, vals, ls=(0, 4, 6, 8)):
    """Least-squares cubic-harmonic components from values at directions dirs (nd, 3) of the irreducible wedge.
    vals: (nd, ...). Returns (coeffs dict l -> array(...), rms residual relative to the l = 0 part)."""
    dh = np.asarray(dirs, float)
    dh = dh / np.linalg.norm(dh, axis=1)[:, None]
    A = np.stack([ycub(l, dh) for l in ls], axis=1)          # (nd, nl)
    v = np.asarray(vals, float).reshape(len(dh), -1)
    c, *_ = np.linalg.lstsq(A, v, rcond=None)
    res = v - A @ c
    rel = np.sqrt((res**2).mean(0)) / np.abs(c[0] / np.sqrt(4 * np.pi))
    shp = np.shape(vals)[1:]
    return {l: c[i].reshape(shp) for i, l in enumerate(ls)}, rel.reshape(shp)
