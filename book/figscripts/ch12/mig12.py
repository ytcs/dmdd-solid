"""Shared inputs of Sect. 12.3 (crystal Migdal effect at large momentum): the valence ionization factor Z_ion(k) of
silicon, the loss-function weight Q_Mig(omega), the soft-limit ionization probability and the Migdal rate integrals.
Used by fig12_3.py, limit12_3a.py, limit12_3b.py, limit12_3c.py and we12_3.py. Run directly to print the checks and
every number of Sect. 12.3 that the other scripts do not print.

Natural units hbar = c = 1, Heaviside-Lorentz e^2 = 4 pi alpha; energies and momenta in eV unless a name says keV.

Formulas (Sect. 12.3)
  Soft-limit Migdal probability per kick (eq:12.3-soft), isotropic loss function:
      dP/domega = 4 alpha int d^3k/(2pi)^3 Z_ion(k)^2 (v_N.k)^2 L(k, omega) / (omega^4 k^2) = 4 alpha v_N^2 Q_Mig(omega),
      Q_Mig(omega) = int d^3k/(2pi)^3 Z_ion(k)^2 L(k, omega) / (3 omega^4) = int dk k^2 Z_ion^2 L / (6 pi^2 omega^4),
      v_N = q/M, v_N^2 = 2 E_R / M.
  Rate per unit target mass (eq:8.2-spectrum with the nuclear row, isotropic response; the generic form
      dR/domega = rho_chi / (4 pi^2 rho_T m_chi) int dq q eta(v_min(q, omega)) D S(q, omega)
      reproduces eq:10.2-rate for D S = sigma_e q^2 L / (2 alpha mu^2)):
      D = |V_N|^2 = pi A^2 sigma_n / mu_n^2 (heavy mediator, F_N = 1), S_Mig = 2 pi n_kappa (dP/domega_e)(q)
      delta(omega - omega_e - omega_l) with omega_l = q^2/2M (free recoil) or distributed as the nuclear response.
Inputs (all reused)
  Loss functions: ../ch10/si_elf_binned.npz (Knapen-Kozaczuk-Lin GPAW tables via DarkELF; see ../ch10/si_elf_reduce.py):
      'lf' = Im[-(eps^-1)_GG(q_r, omega)] with local fields at |q + G| (diagonal, direction-averaged in 100-eV bins of
      |q|, 0.49-22.5 keV), 'rpa' = the same without local fields; omega = 0-89.2 eV; the tables' 1.11 eV scissor gap.
  Orbitals: ../ch03/ld1/si_r1.wfc, all-electron PBE scalar-relativistic free atom (Sect. 3.5), u_nl(r) = r R_nl(r) in
      bohr, normalized int u^2 dr = 1. Core form factor f_core(k) = sum_{1s,2s,2p} N_nl int u_nl^2 j_0(k r) dr;
      Z_ion(k) = Z - f_core(k) (the electrons of the core are frozen into the ion, the four valence electrons are
      in L). This is the book's own core form factor; Knapen et al. use the tabulated Si4+ form factor of the
      International Tables (their Ref. [32]).
  Constants, halo and eta(v_min): ../ch10/rate10_2.py (v0, v_esc, v_E = 238, 544, 250.5 km/s; rho_chi = 0.3 GeV/cm^3);
      Si mass, phonon DOS and incoherent nuclear response: ../ch11/imp11.py (M = 26.162 GeV, <omega> = 40.90 meV,
      impulse onset x_R = 4 at q = 92.5 keV).
"""
import os
import sys
import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import rate10_2 as R  # noqa: E402
import imp11 as IMP  # noqa: E402

ALPHA, ME, HBARC = R.ALPHA, R.ME, R.HBARC
M = IMP.M                                    # Si nuclear (atomic) mass, eV
A_SI = 28.0855
M_N = 939.0e6                                # nucleon mass used in mu_n (eV)
AU = 3728.94                                 # eV per bohr^-1
EG = R.EG                                    # 1.11 eV, the tables' scissor gap
EG_PHYS = 1.17                               # physical low-temperature gap (Sect. 3.3)
QBZ = 2.25e3                                 # eq:11.1-qBZ, eV
W_MEAN = IMP.W_MEAN                          # <omega> of the Si DOS, eV
Q_ONSET = np.sqrt(2 * M * 4 * W_MEAN)        # x_R = 4, Sect. 11.4
E_ONSET = 4 * W_MEAN
LD1 = os.path.join(HERE, "..", "ch03", "ld1", "si_r1.wfc")

_d = R.load()
OM = _d["omega"]
QT = _d["q"]
LF = np.maximum(_d["lf"], 0.0)
RPA = np.maximum(_d["rpa"], 0.0)


def _orbitals():
    heads = open(LD1).readline().split()[2:]
    d = np.loadtxt(LD1)
    return d[:, 0], {h: d[:, i + 1] for i, h in enumerate(heads)}


_R, _U = _orbitals()
CORE = {"1S": 2, "2S": 2, "2P": 6}


def f_core(k):
    """Form factor of the ten core electrons of Si at momentum k (eV)."""
    k = np.atleast_1d(np.asarray(k, float))
    kr = np.outer(k / AU, _R)
    out = np.zeros_like(k)
    for h, n in CORE.items():
        u2 = _U[h]**2
        norm = np.trapezoid(u2, _R)
        out += n * np.trapezoid(u2[None, :] * spherical_jn(0, kr), _R, axis=1) / norm
    return out


def z_ion(k):
    return 14.0 - f_core(k)


# fine k grid: below the first table bin the loss function is held at its first-bin value (weight k^2)
KG = np.concatenate([np.linspace(0, QT[0], 25)[:-1], QT])
ZG = z_ion(KG)


def _on_grid(tab):
    out = np.empty((len(OM), len(KG)))
    for i in range(len(OM)):
        out[i] = np.interp(KG, QT, tab[i])
    return out


LF_G = _on_grid(LF)
RPA_G = _on_grid(RPA)


def qmig(resp="lf", zfix=None, kmax=None, kmin=0.0):
    """Q_Mig(omega) on the table energies OM (eV^-1 ... units eV^-2 per unit of 4 alpha v_N^2: dP/domega = 4 alpha v^2 Q).
    resp: 'lf' or 'rpa'; zfix: constant Z_ion instead of Z_ion(k); kmax/kmin: momentum window (eV)."""
    tab = LF_G if resp == "lf" else RPA_G
    z2 = (np.full_like(KG, zfix) if zfix is not None else ZG)**2
    m = (KG >= kmin) & (KG <= (kmax if kmax is not None else KG[-1]))
    integ = np.trapezoid(KG[m]**2 * z2[m] * tab[:, m], KG[m], axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        q = integ / (6 * np.pi**2 * OM**4)
    q[OM < EG] = 0.0
    return q


def dP_domega(ER, resp="lf", **kw):
    """Soft-limit dP/domega (eV^-1) for a Si nucleus kicked to recoil energy ER (eV)."""
    v2 = 2 * ER / M
    return 4 * ALPHA * v2 * qmig(resp, **kw)


def p_total(ER, wmin=None, **kw):
    w = OM
    y = dP_domega(ER, **kw)
    m = w >= (EG if wmin is None else wmin)
    return np.trapezoid(y[m], w[m])


def mu(a, b):
    return a * b / (a + b)


def rate_free(m, qmin=0.0, exact=True, q_n=4000):
    """dR/domega_e on OM, events kg^-1 yr^-1 eV^-1, sigma_n = 1e-38 cm^2, Si, heavy mediator, soft limit,
    free recoil omega_l = q^2/2M. exact=False drops omega_e from v_min (the per-mass form)."""
    sig_n = 1e-38 * R.CM**2
    muN, mun = mu(m, M), mu(m, M_N)
    qmax = 2 * muN * R.VMAX
    if qmin >= qmax:
        return np.zeros_like(OM)
    q = np.linspace(max(qmin, 1.0), qmax, q_n)
    D = np.pi * A_SI**2 * sig_n / mun**2
    pref = R.RHO_CHI / (4 * np.pi**2 * m) * D * 2 * np.pi / M      # (1/rho_T) * 2 pi n_kappa = 2 pi / M
    out = np.zeros_like(OM)
    for i, w in enumerate(OM):
        if w < EG:
            continue
        wtot = (w if exact else 0.0) + q**2 / (2 * M)
        vmin = wtot / q + q / (2 * m)
        integ = q * R.eta(vmin) * 4 * ALPHA * q**2 / M**2
        out[i] = np.trapezoid(integ, q)
    return R.to_per_kg_yr(pref * out * qmig("lf"))


if __name__ == "__main__":
    print(f"Si: M = {M/1e9:.4f} GeV, <omega> = {W_MEAN*1e3:.2f} meV, impulse onset q = {Q_ONSET/1e3:.1f} keV, "
          f"E_R = {E_ONSET*1e3:.0f} meV; q_BZ = {QBZ/1e3:.2f} keV")
    for k in [0, 2e3, 5e3, 7.5e3, 10e3, 15e3, 20e3, 30e3]:
        print(f"  Z_ion({k/1e3:4.1f} keV) = {z_ion(k)[0]:.3f}")
    kk = np.linspace(0, 30e3, 3001)
    zz = z_ion(kk)
    print(f"  Z_ion leaves 4 by 5 % at k = {kk[np.argmax(zz > 4.2)]/1e3:.2f} keV, by 10 % at {kk[np.argmax(zz > 4.4)]/1e3:.2f} keV")
    assert abs(z_ion(0)[0] - 4) < 1e-3
    # f-sum of the table (fraction of (pi/2) omega_p^2 with all 14 electrons, and with the 4 valence electrons)
    WP_VAL = R.WP_VAL
    for kq in [2e3, 5e3, 10e3, 15e3, 20e3]:
        j = np.argmin(abs(QT - kq))
        f = np.trapezoid(OM * LF[:, j], OM) / (np.pi / 2 * WP_VAL**2)
        print(f"  table f-sum at {QT[j]/1e3:5.2f} keV: {f:.3f} of the valence value")
    Q = qmig("lf")
    m = OM >= EG
    for ER in [100.0, 500.0, 1000.0]:
        print(f"E_R = {ER:6.0f} eV: v_N = {np.sqrt(2*ER/M):.3e}, P(omega >= {EG} eV) = {p_total(ER):.3e}, "
              f"P(Z_ion = 4) = {p_total(ER, zfix=4.0):.3e}")
    P1 = p_total(1000.0)
    # where the probability lives
    w = OM
    y = dP_domega(1000.0)
    cum = np.cumsum(np.r_[0, 0.5 * (y[1:] + y[:-1]) * np.diff(w)]) / np.trapezoid(y[m], w[m])
    print(f"  median omega of dP/domega: {np.interp(0.5, cum, w):.2f} eV; peak of dP/dln omega at "
          f"{w[np.argmax(w*y)]:.2f} eV")
    for wc in [5, 10, 20, 30, 50]:
        print(f"  fraction of P below {wc} eV: {np.interp(wc, w, cum):.3f}")
    # k distribution of Q (all omega above the gap)
    tot = np.trapezoid(Q[m], OM[m])
    for kc in [QBZ, 5e3, 10e3, 15e3]:
        part = np.trapezoid(qmig("lf", kmin=kc)[m], OM[m])
        print(f"  fraction of P from k > {kc/1e3:5.2f} keV: {part/tot:.3f}")
    part = np.trapezoid(qmig("lf", kmax=QT[0])[m], OM[m])
    print(f"  fraction from k < first table bin ({QT[0]/1e3:.2f} keV, held constant): {part/tot:.4f}")
    # tail above the table's 89 eV: f-sum bound int_{w_top}^inf L/w^4 <= (pi/2) w_p^2 / w_top^5 per k, all electrons
    wtop = OM[-1]
    print(f"  omega_top = {wtop:.1f} eV; Z_ion and L ratio etc. printed by the box scripts")
    print(f"  Z_ion(k) vs Z_ion = 4: P ratio {P1/p_total(1000.0, zfix=4.0):.3f} (Knapen et al.: 1.6 for Si)")
    print(f"  rpa / lf P ratio at 1 keV: {p_total(1000.0, resp='rpa')/P1:.3f}")
