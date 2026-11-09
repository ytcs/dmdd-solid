"""Shared inputs of the Sect. 16.2 scripts (low-dimensional plasmons and layered stacks).

Units: hbar = c = 1, energies and momenta in eV, Heaviside-Lorentz e^2 = 4 pi alpha (book convention, App. A.2).
Response normalization of Sect. 4.2: S = -2 Im R at T = 0, with 2 pi delta inside S.

Kernels (Sect. 16.2):
  * sheet between half spaces eps_a, eps_b:  v2D(q) = e^2/((eps_a + eps_b) q)   (images, Sect. 15.3);
  * cylindrical shell of radius r_t in a medium eps_env:  v1D(q) = 2 alpha I0(q r_t) K0(q r_t)/eps_env
    (m = 0 Fourier-Bessel term of 1/|r - r'|; 2607.15338 uses the same shell profile, its Eq. after (4)).
Inputs (every number sourced):
  * alpha = 1/137.035999, m_e = 510998.95 eV, hbar c = 197.3269804 eV nm (CODATA);
  * v_max = 794.5 km/s (Eq. 1.2-vmax of the book);
  * graphene: nearest-neighbor hopping t = 2.8 eV and carbon-carbon distance a_cc = 1.42 A, Castro Neto et al.
    arXiv:0709.1163 (text after Eqs. (1), (5) and (7)); v_D = 3 t a_cc/2 = 3.02e-3, the one graphene velocity of the
    book (Sects. 16.2, 16.3).  (Das, Jang, Min arXiv:2312.00866 quote gamma_0 = 3.16 eV for their bilayer model; not
    used here.)
  * metallic nanotube: N_ch = 4 channels (spin x valley); radius r_t = 0.7 nm, inside the commercial diameter range
    1.2-1.7 nm quoted by Zhang and Chen arXiv:2607.15338 (p. 2); eps_env = 1 (isolated tube), a model choice;
  * silicon valence gas: omega_p = 16.6 eV, k_F = 3.57 keV (Sect. 4.5, WE 4.10).
"""
import numpy as np
from scipy.special import i0e, k0e

ALPHA = 1 / 137.035999
E2 = 4 * np.pi * ALPHA          # e^2 in Heaviside-Lorentz units
ME = 510998.95                  # eV
HBARC = 197.3269804             # eV nm
C_KMS = 299792.458
VMAX = 794.5 / C_KMS            # Eq. 1.2-vmax
EULER = 0.5772156649

A_CC = 0.142                    # nm, 0709.1163
T_HOP = 2.8                     # eV, 0709.1163 (text after Eq. (5))
V_D = 1.5 * A_CC * T_HOP / HBARC    # Dirac velocity of graphene (dimensionless), 3.022e-3
N_CH = 4
R_T = 0.7 / HBARC               # tube radius in eV^-1
EPS_ENV = 1.0

WP_SI = 16.6                    # eV, Sect. 4.5
KF_SI = 3570.0                  # eV
VF_SI = KF_SI / ME


def v1D(q, rt=R_T, eps_env=EPS_ENV):
    """Coulomb kernel of a cylindrical shell, 2 alpha I0(q r_t) K0(q r_t)/eps_env (scaled Bessels for stability)."""
    x = np.abs(q) * rt
    return 2 * ALPHA * i0e(x) * k0e(x) / eps_env


def v1D_log(q, rt=R_T, eps_env=EPS_ENV):
    """Long-wavelength form 2 alpha [ln(2/(q r_t)) - gamma_E]/eps_env."""
    return 2 * ALPHA * (np.log(2 / (np.abs(q) * rt)) - EULER) / eps_env


def g_c(q, nch=N_CH, v=V_D, kern=v1D):
    """Luttinger charge parameter of the linear-band RPA, [1 + N_ch v1D(q)/(pi v)]^(-1/2)."""
    return 1 / np.sqrt(1 + nch * kern(q) / (np.pi * v))


def v2D(q, eps_a=1.0, eps_b=1.0):
    return E2 / ((eps_a + eps_b) * q)


# ---- small-q (q << k_F) Lindhard functions, normalized to minus the total density of states at E_F ----
def f3(nu):
    """3D: R0/(-2N_F) at q -> 0, nu = omega/(q v_F) real > 0 (Eq. 4.5-lindhard, q << k_F)."""
    nu = np.asarray(nu, dtype=float)
    re = 1 - 0.5 * nu * np.log(np.abs((1 + nu) / (1 - nu)))
    im = np.where(nu < 1, 0.5 * np.pi * nu, 0.0)
    return re + 1j * im


def f2(nu):
    """2D: R0/(-N_tot) at q -> 0: 1 + i nu/sqrt(1-nu^2) (nu < 1), 1 - nu/sqrt(nu^2-1) (nu > 1)."""
    nu = np.asarray(nu, dtype=float)
    out = np.empty(nu.shape, dtype=complex)
    lo = nu < 1
    out[lo] = 1 + 1j * nu[lo] / np.sqrt(1 - nu[lo] ** 2)
    out[~lo] = 1 - nu[~lo] / np.sqrt(nu[~lo] ** 2 - 1)
    return out


def fwhm(w, L):
    """Peak position and full width at half maximum of a sampled positive line, with linear interpolation."""
    i = int(np.argmax(L))
    h = L[i] / 2
    j = i
    while j > 0 and L[j] > h:
        j -= 1
    k = i
    while k < len(L) - 1 and L[k] > h:
        k += 1
    wl = w[j] + (h - L[j]) * (w[j + 1] - w[j]) / (L[j + 1] - L[j])
    wr = w[k - 1] + (h - L[k - 1]) * (w[k] - w[k - 1]) / (L[k] - L[k - 1])
    return w[i], wr - wl


# ---- layered stack (Sect. 16.2.4) ----
def stack_inplane(epsA, epsB, f, ka):
    """Exact head of eps^-1 for k in the plane of the layers (closed form of Sect. 16.2):
    1/eps = f/epsA + (1-f)/epsB - (2/ka)(epsA-epsB)^2 tA tB/[epsA epsB (epsA tA + epsB tB)], t = tanh(k d/2)."""
    tA = np.tanh(ka * f / 2)
    tB = np.tanh(ka * (1 - f) / 2)
    return f / epsA + (1 - f) / epsB - (2 / ka) * (epsA - epsB) ** 2 * tA * tB / (epsA * epsB * (epsA * tA + epsB * tB))


def emt_inv(epsA, epsB, f, cth):
    """Effective medium, Lasenby-Prabhu Eq. (16): eps_par (axis) harmonic mean, eps_perp (plane) arithmetic mean,
    eps_L = eps_par cos^2(theta) + eps_perp sin^2(theta), theta measured from the stacking axis."""
    epar = 1 / (f / epsA + (1 - f) / epsB)
    eperp = f * epsA + (1 - f) * epsB
    return 1 / (epar * cth ** 2 + eperp * (1 - cth ** 2))


def stack_general(epsA, epsB, dA, dB, k, cth):
    """Exact head eps^-1_{00}(k) of a periodic two-layer stack for a source exp(i k.r), by matching the potential
    psi(x) exp(i kpar z) layer by layer (x along the stacking axis, kx = k cos theta, kpar = k sin theta):
       psi_j = exp(i kx x)/(eps_j k^2) + A_j exp(kpar (x - c_j)) + B_j exp(-kpar (x - c_j)),
    continuity of psi and eps psi' at x = dA, Bloch condition psi(x + a) = exp(i kx a) psi(x) at x = a,
    then eps^-1_{00} = k^2 (1/a) Int_0^a psi exp(-i kx x) dx  (unit source density)."""
    a = dA + dB
    kx = k * cth
    kp = k * np.sqrt(max(1 - cth ** 2, 0.0))
    cA, cB = dA / 2, dA + dB / 2
    PA, PB = 1 / (epsA * k ** 2), 1 / (epsB * k ** 2)
    ph = np.exp(1j * kx * a)

    def basis(x, c):
        return np.exp(kp * (x - c)), np.exp(-kp * (x - c))

    eA0p, eA0m = basis(0.0, cA)
    eAdp, eAdm = basis(dA, cA)
    eBdp, eBdm = basis(dA, cB)
    eBap, eBam = basis(a, cB)
    M = np.zeros((4, 4), dtype=complex)
    rhs = np.zeros(4, dtype=complex)
    # psi_A(dA) = psi_B(dA)
    M[0] = [eAdp, eAdm, -eBdp, -eBdm]
    rhs[0] = -(PA - PB) * np.exp(1j * kx * dA)
    # epsA psi_A'(dA) = epsB psi_B'(dA); particular parts: eps_j P_j i kx = i kx/k^2 equal on both sides
    M[1] = [epsA * kp * eAdp, -epsA * kp * eAdm, -epsB * kp * eBdp, epsB * kp * eBdm]
    rhs[1] = 0.0
    # psi_B(a) = ph psi_A(0)
    M[2] = [-ph * eA0p, -ph * eA0m, eBap, eBam]
    rhs[2] = ph * PA - PB * np.exp(1j * kx * a)
    # epsB psi_B'(a) = ph epsA psi_A'(0); particular parts equal (i kx exp(i kx a)/k^2 both sides)
    M[3] = [-ph * epsA * kp * eA0p, ph * epsA * kp * eA0m, epsB * kp * eBap, -epsB * kp * eBam]
    rhs[3] = 0.0
    A1, B1, A2, B2 = np.linalg.solve(M, rhs)

    def integ(s, x0, x1, c):
        # Int_x0^x1 exp(s (x - c)) exp(-i kx x) dx
        z = s - 1j * kx
        if abs(z) < 1e-14:
            return (x1 - x0) * np.exp(-s * c)
        return np.exp(-s * c) * (np.exp(z * x1) - np.exp(z * x0)) / z

    tot = PA * dA + PB * dB
    tot += A1 * integ(kp, 0, dA, cA) + B1 * integ(-kp, 0, dA, cA)
    tot += A2 * integ(kp, dA, a, cB) + B2 * integ(-kp, dA, a, cB)
    return k ** 2 * tot / a
