"""Shared model of Sect. 12.4: the exact second-order Migdal amplitude of a nucleus bound in an isotropic harmonic
(Einstein) well, against its two published truncations. Used by limit12_4a.py, limit12_4b.py and we12_4.py; run directly
for the checks (log: osc12_4.log).

Natural units hbar = c = 1; energies and momenta in eV.

Model. One nucleus of mass M in the well H_N = P^2/2M + M w0^2 X^2/2 (three dimensions, isotropic). The dark matter kicks it
with B = exp(i q.X), q along z; the nucleus passes the momentum p to the electrons through A = exp(-i p.X) (the
X-dependence of one Fourier component of its potential, eq:12.1-force), and the electrons gain omega (= omega_e). The
electronic matrix element and the vertex are common factors and are dropped. Second-order amplitude into the vibrational
final state f, the two time orderings (2210.06490 Eq. (3.1); eq:2.4 second-order amplitude):
    M_f = sum_l <f|A|l><l|B|0> / (omega + E_f - E_l)  -  sum_l <f|B|l><l|A|0> / (omega + E_l - E_0) .
Expanding in 1/omega, the 1/omega term is <f|[A,B]|0>/omega = 0, and the 1/omega^2 term is the double commutator
    M_f^(2) = <f|[[A,H_N],B]|0>/omega^2 = (q.p/M) <f|exp(i(q - p).X)|0> / omega^2          (Berghaus et al. Eq. (3.6))
whatever the potential; it is the leading form ("sudden", lattice factor at q - p). Its sum over f is (q.p/M omega^2)^2.
The phonon-mediated form of Liang et al. (2205.03395 Eqs. (3.1), (3.3)) for one Einstein mode:
    M_f^(PM) = (q.p/M) <f|exp(i q.X)|0> / (omega^2 - w0^2) ,
which is exact at first order in p for a harmonic well (Sect. 12.4); its reduction (their Eq. (3.2)) is w0 -> 0.

Numerics. The well separates in z (along q) and x (p has components p_z = p c, p_x = p s, c = cos theta). B acts on z only.
Then, with E_f = (f_z + f_x) w0,
    M_f = <f_x|e^{-i p_x x}|0> [ sum_l Az[f_z,l] Bz[l,0] / (omega + (f_z + f_x - l) w0)
                                 - sum_l Bz[f_z,l] Az[l,0] / (omega + (l + f_x) w0) ] .
The displacement matrices <m|exp(i k z)|n> are built from the eigenvectors of the position operator in a truncated
oscillator basis (size NB), kept on the lowest NK < NB levels, where they are exact to rounding. The truncation is checked
by the sum rule sum_f |M_f^(2)|^2 = (q p_z / M omega^2)^2 (printed, 1e-10 or better). Angle average over the direction of
p with 24 Gauss-Legendre nodes in c, weight dc/2 (isotropic electrons).
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

M_SI = 26161474737.0          # eV, natural Si atomic mass 28.0855 u (imp11.M)
W_EIN = 0.030421              # eV, <omega^-1>^-1 of the Si PBE DOS (imp11.W_INV, Sect. 11.3): same 2W as the full DOS


def _xbasis(nb):
    """Eigen-decomposition of the dimensionless position a + a^dagger in an nb-level basis."""
    off = np.sqrt(np.arange(1, nb))
    lam, vec = eigh_tridiagonal(np.zeros(nb), off)
    return lam, vec


_CACHE = {}


def disp(k, ell, nk, nb):
    """<m|exp(i k z)|n> for m, n < nk, with z = ell (a + a^dagger)."""
    if nb not in _CACHE:
        _CACHE[nb] = _xbasis(nb)
    lam, vec = _CACHE[nb]
    top = vec[:nk, :]
    return (top * np.exp(1j * k * ell * lam)[None, :]) @ top.T


def poisson_amp(k, ell, nmax):
    """<n|exp(i k x)|0> for n = 0..nmax: e^{-b^2/2} (i b)^n / sqrt(n!), b = k ell."""
    from math import factorial
    b = k * ell
    from scipy.special import gammaln
    n = np.arange(nmax + 1)
    mag = np.exp(-b * b / 2 + n * np.log(abs(b) + 1e-300) - 0.5 * gammaln(n + 1))
    return mag * (1j * np.sign(b))**n


def sizes(q, p, w0, M):
    nmean = (q + p)**2 / (2 * M * w0)
    nk = int(nmean + 12 * np.sqrt(nmean + 1) + 40)
    return nk, nk + 120


def probs(q, p, c, omega, w0=W_EIN, M=M_SI, nfx=None):
    """For one direction c of p: (P_exact, P_lead, P_PM, P_lead_check, zero-phonon fraction of exact), sums over f."""
    ell = 1 / np.sqrt(2 * M * w0)
    pz, px = p * c, p * np.sqrt(max(0.0, 1 - c * c))
    nk, nb = sizes(q, p, w0, M)
    if nfx is None:
        nx = px**2 / (2 * M * w0)
        nfx = int(nx + 8 * np.sqrt(nx + 1) + 6)
    Az = disp(-pz, ell, nk, nb)
    Bz = disp(q, ell, nk, nb)
    Cz = disp(q - pz, ell, nk, nb)
    ax = poisson_amp(-px, ell, nfx)
    v = Bz[:, 0]
    u = Az[:, 0]
    fz = np.arange(nk)
    Pex = 0.0
    zp = 0.0
    for fx in range(nfx + 1):
        d1 = omega + (fz[:, None] + fx - fz[None, :]) * w0          # [f_z, l]
        t1 = (Az / d1) @ v
        d2 = omega + (fz + fx) * w0                                  # [l]
        t2 = Bz @ (u / d2)
        Mf = ax[fx] * (t1 - t2)
        Pex += np.sum(np.abs(Mf)**2)
        if fx == 0:
            zp = np.abs(Mf[0])**2
    lead = (q * pz / (M * omega**2))**2
    check = lead * np.sum(np.abs(Cz[:, 0])**2) * np.sum(np.abs(ax)**2)
    pm = (q * pz / (M * (omega**2 - w0**2)))**2
    return Pex, lead, pm, check, zp / Pex if Pex > 0 else 0.0


CN, CW = np.polynomial.legendre.leggauss(24)
CW = CW / 2


def averaged(q, p, omega, w0=W_EIN, M=M_SI):
    """Angle-averaged ratios: exact / lead, PM / lead, check / lead - 1 (truncation), exact zero-phonon fraction."""
    tot = np.zeros(4)
    zf = 0.0
    for c, w in zip(CN, CW):
        Pex, lead, pm, chk, z = probs(q, p, c, omega, w0, M)
        tot += w * np.array([Pex, lead, pm, chk])
        zf += w * z * Pex
    return tot[0] / tot[1], tot[2] / tot[1], tot[3] / tot[1] - 1, zf / tot[0]


def free_exact_ratio(q, p, omega, M=M_SI):
    """Free nucleus, both denominators exact: amplitude b/((omega - b + a)(omega + a)), b = q.p/M, a = p^2/2M,
    against the leading b/omega^2; angle-averaged ratio of squares with weight (q.p)^2 of the leading term."""
    b = q * p * CN / M
    a = p * p / (2 * M)
    ex = (b / ((omega - b + a) * (omega + a)))**2
    ld = (b / omega**2)**2
    return (CW @ ex) / (CW @ ld)


def kkl_bracket_ratio(q, p, omega, M=M_SI):
    """The bracket with the final ion momentum and the recoil terms dropped, 1/(omega - y) - 1/omega,
    y = (q - p).p/M, against the same leading term."""
    y = (q * p * CN - p * p) / M
    br = (1 / (omega - y) - 1 / omega)**2
    ld = (q * p * CN / (M * omega**2))**2
    return (CW @ br) / (CW @ ld)


if __name__ == "__main__":
    print("Model constants: M = %.6e eV, w0 = %.4f eV (Si <omega^-1>^-1), ell0 = %.4e eV^-1"
          % (M_SI, W_EIN, 1 / np.sqrt(2 * M_SI * W_EIN)))
    p = 5.7e3
    print("\nCheck 1: exact sum vs leading and phonon-mediated forms, p = 5.7 keV, omega = 4.4 eV")
    for q in [2e3, 5e3, 10e3, 50e3, 100e3]:
        r, rpm, tr, z = averaged(q, p, 4.4)
        print("  q = %6.1f keV: exact/lead = %.8f, PM/lead = %.8f, truncation %.1e, exact zero-phonon fraction %.4f"
              % (q / 1e3, r, rpm, tr, z))
    print("\nCheck 2: nearly free nucleus (w0 = 2e-3 eV) vs the analytic free amplitude, omega = 4.4 eV")
    for q in [2e3, 5e3, 10e3]:
        r, _, tr, _ = averaged(q, p, 4.4, w0=2e-3)
        print("  q = %5.1f keV: Einstein exact/lead = %.6f (trunc %.1e); free exact/lead = %.6f; "
              "bracket (q-p).p with recoil dropped / lead = %.4f"
              % (q / 1e3, r, tr, free_exact_ratio(q, p, 4.4), kkl_bracket_ratio(q, p, 4.4)))
