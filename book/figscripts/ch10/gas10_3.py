"""Sect. 10.3 (electron-gas models and plasmons): shared functions and every number quoted in the text and in
Worked example 10.3.  Run as a script to print and check them.  Natural units hbar = c = 1, Heaviside-Lorentz
e^2 = 4 pi alpha; energies and momenta in eV.

Inputs and their sources
  Constants, halo (v0 = 238, v_esc = 544, v_E = 250.5 km/s, v_max = 2.650e-3), rho_chi = 0.3 GeV/cm^3, rho_T, the
     silicon RPA + LF loss-function tables (Knapen-Kozaczuk-Lin, via DarkELF, binned in si_elf_binned.npz) and the rate
     integral: rate10_2.py (Sect. 10.2), reused unchanged.
  Electron gas at the silicon valence density n_e = 2.00e23 cm^-3 (App. A.2), r_s = 2.0: k_F = 3.570 keV,
     v_F = 6.986e-3, omega_p = 16.61 eV (book values 3.57 keV, 7.0e-3, 16.6 eV; Sects. 2.5, 4.3), as fig4_6.py.
  Lindhard function: eq:D.8-Rz (complex z) and eq:D.8-Re, eq:D.8-Im (real omega), App. D.8 = Knapen et al.
     arXiv:2101.08275 Eqs. (17)-(18).
  Mermin function: eq:4.5-mermin = Knapen et al. Eq. (19).
  Plasmon pole: eq:4.5-plasmonL; small-q forms Kozaczuk-Lin arXiv:2003.12077 Eqs. (5), (7).
  Gap 1.11 eV: the scissor of the silicon tables (Sect. 10.2; the physical low-temperature gap is 1.17 eV).
  Silicon lattice constant a = 5.431 A (2 pi/a = 2.283 keV); measured loss peak 16.4 eV and width 3.66 eV (Sect. 4.5,
     Worked example 4.10).
Modelling choices (named in the captions)
  * The gas rates are evaluated on the momentum bins of the silicon tables (|q| >= 0.49 keV, to 22.5 keV) so that the
    two are truncated alike; energies on a 0.05 eV grid from the threshold, the gas functions evaluated analytically
    there (no interpolation).
  * Mermin: one term, omega_p = 16.6 eV, gamma_rel = 3.66 eV, the full width of the measured silicon loss peak, a fit
    parameter and not a collision rate (Sect. 4.5).
  * The undamped plasmon of the gas (a delta function below q_c) is kinematically closed to halo dark matter and is
    absent from the gridded gas rates; the script checks that it is closed.
"""
import os
import sys
import numpy as np
from scipy import integrate, optimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

ME, ALPHA = R.ME, R.ALPHA
E2 = 4 * np.pi * ALPHA
HBARC_CM = 197.3269804e-7
NE = 2.00e23 * HBARC_CM**3
KF = (3 * np.pi**2 * NE) ** (1 / 3)
VF = KF / ME
NF = ME * KF / (2 * np.pi**2)
WP = np.sqrt(E2 * NE / ME)
GAMMA_SI = 3.66
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch10")


def _lg(w):
    return np.log((w + 1) / (w - 1))


def R0z(q, z):
    """eq:D.8-Rz, Im z > 0."""
    nup = z / (q * VF) + q / (2 * KF)
    num = z / (q * VF) - q / (2 * KF)
    return -2 * NF * (0.5 + KF / (4 * q) * ((1 - nup**2) * _lg(nup) - (1 - num**2) * _lg(num)))


def R0(q, w):
    """eq:D.8-Re and eq:D.8-Im, real w > 0."""
    nup = w / (q * VF) + q / (2 * KF)
    num = w / (q * VF) - q / (2 * KF)
    lr = lambda x: np.log(np.abs((x + 1) / (x - 1)))
    re = -2 * NF * (0.5 + KF / (4 * q) * ((1 - nup**2) * lr(nup) - (1 - num**2) * lr(num)))
    im = -np.pi * KF * NF / (2 * q) * ((1 - num**2) * (np.abs(num) < 1) - (1 - nup**2) * (np.abs(nup) < 1))
    return re + 1j * im


def eps_lin(q, w):
    return 1 - E2 / q**2 * R0(q, w)


def eps_mer(q, w, g=GAMMA_SI):
    """eq:4.5-mermin (Knapen et al. Eq. (19))."""
    el = 1 - E2 / q**2 * R0z(q, w + 1j * g)
    e0 = eps_lin(q, 1e-9 * np.ones_like(w)).real
    return 1 + (1 + 1j * g / w) * (el - 1) / (1 + (1j * g / w) * (el - 1) / (e0 - 1))


def L_lin(q, w):
    return np.imag(-1 / eps_lin(q, w))


def L_mer(q, w, g=GAMMA_SI):
    return np.imag(-1 / eps_mer(q, w, g))


def wplus(q):
    return q * VF + q * q / (2 * ME)


def wminus(q):
    return np.maximum(0.0, q * q / (2 * ME) - q * VF)


QC = optimize.brentq(lambda q: eps_lin(q, wplus(q) * (1 + 1e-12)).real, 0.1 * KF, 1.5 * KF, xtol=1e-9)


def wpl_quad(q):
    return np.sqrt(WP**2 + 0.6 * VF**2 * q**2)


QC_QUAD = optimize.brentq(lambda q: wpl_quad(q) - wplus(q), 500.0, 5000.0)
QC_CONST = optimize.brentq(lambda q: WP - wplus(q), 500.0, 5000.0)


def wpl(q):
    """Exact zero of Re eps_Lin above the continuum, q < QC."""
    return optimize.brentq(lambda w: eps_lin(q, w).real, wplus(q) * (1 + 1e-10), 10 * WP, xtol=1e-12)


def pole_share(q):
    """First moment of the pole term of eq:4.5-plasmonL over the f-sum (pi/2) omega_p^2: 2 omega_pl/(omega_p^2 de1/dw)."""
    w = wpl(q)
    h = 1e-5 * w
    de = (eps_lin(q, w + h).real - eps_lin(q, w - h).real) / (2 * h)
    return 2 * w / (WP**2 * de)


def ZL(q):
    """Kozaczuk-Lin Eq. (7): Z_L = 1 - (3/5) q^2 v_F^2/omega_p^2."""
    return 1 - 0.6 * q**2 * VF**2 / WP**2


def gas_spectrum(m, kind, q, light=False, wth=R.EG, wmax=89.2, dw=0.05):
    """dR/domega [events/kg/yr/eV] from eq:10.2-rate with the gas loss function on the momenta q (the table bins)."""
    w = np.arange(wth, wmax, dw)
    W, Q = np.meshgrid(w, q, indexing="ij")
    L = L_lin(Q, W) if kind == "lin" else L_mer(Q, W)
    integ = Q**3 * R.eta(W / Q + Q / (2 * m)) * R.fdm2(Q, light) * L
    return w, R.to_per_kg_yr(np.trapezoid(integ, q, axis=1) * R.prefactor(m))


def table_spectrum(m, d, light=False, w=None):
    if w is None:
        w = np.arange(R.EG, d["omega"][-1], 0.05)
    return R.spectrum(m, "lf", d, light, wfine=w)


def maxwell_tail(u):
    """Fraction of an untruncated Maxwellian (v0, boosted by v_E) above the lab speed u [km/s]."""
    v0, vE = R.V0, R.VE
    f = lambda v: v / (np.sqrt(np.pi) * v0 * vE) * (np.exp(-(v - vE)**2 / v0**2) - np.exp(-(v + vE)**2 / v0**2))
    tot = integrate.quad(f, 0, 5000)[0]
    vv = np.linspace(u, u + 800, 40001)
    return np.trapezoid(f(vv), vv) / tot


def close(a, b, rtol, name):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:66s} {a:.4g}   (quoted {b})")


if __name__ == "__main__":
    d = R.load()
    q, om = d["q"], d["omega"]
    print("Gas at the silicon valence density")
    close(KF / 1e3, 3.57, 2e-3, "k_F [keV]")
    close(VF, 7.0e-3, 3e-3, "v_F")
    close(WP, 16.6, 3e-3, "omega_p [eV]")
    close(KF * R.VMAX, 9.46, 3e-3, "k_F v_max [eV]")

    print("Momentum scales of the plasmon")
    close(QC / 1e3, 2.60, 3e-3, "q_c exact Lindhard [keV] (Sect. 4.5)")
    close(wplus(QC), 24.8, 3e-3, "omega_pl(q_c) [eV]")
    close(QC_QUAD / 1e3, 2.24, 3e-3, "q_c of the quadratic dispersion [keV]")
    close(wplus(QC_QUAD), 20.6, 3e-3, "omega_pl there [eV]")
    close(QC_CONST / 1e3, 1.88, 3e-3, "q_c with constant omega_p [keV]")
    close(WP / VF / 1e3, 2.38, 3e-3, "omega_p/v_F [keV]")
    close(2 * np.pi / R.A_SI * R.HBARC / 1e3, 2.28, 3e-3, "2 pi/a [keV]")
    close(2 * np.pi / 5e3 * R.HBARC, 2.48, 3e-3, "length with 2 pi/l = 5 keV [A]")
    close(0.6 * (QC_QUAD * VF)**2 / WP**2, 0.53, 1e-2, "(3/5)(q_c v_F)^2/omega_p^2 at 2.24 keV")
    close(WP / R.VMAX / 1e3, 6.27, 3e-3, "omega_p / v_max [keV]")

    print("Pole residue and Z_L")
    for x in [0.1, 0.3]:
        qq = x * KF
        w = wpl(qq)
        res_exact = pole_share(qq) * (np.pi / 2) * WP**2 / w
        res_kl = np.pi * wpl_quad(qq) / 2 * ZL(qq)
        print(f"  q = {x} k_F: residue exact {res_exact:.6f}, (pi omega_pl/2) Z_L {res_kl:.6f}, rel diff "
              f"{res_kl / res_exact - 1:.2e}, (q v_F/omega_p)^4 = {(qq * VF / WP)**4:.2e}")
    close(pole_share(0.5 * KF), 0.957, 2e-3, "pole share of the f-sum at 0.5 k_F (Sect. 4.5)")
    for x in [0.5, 0.8, 0.9, 0.95, 0.99]:
        print(f"  pole share at q/q_c = {x}: exact {pole_share(x * QC):.3f}, "
              f"formula {wpl_quad(x * QC)**2 * ZL(x * QC) / WP**2:.3f}")
    close(pole_share(0.5 * QC), 0.99, 2e-3, "pole share at 0.5 q_c")
    close(pole_share(0.9 * QC), 0.77, 5e-3, "pole share at 0.9 q_c")
    close(pole_share(0.9999 * QC), 0.2, 0.5, "pole share at 0.9999 q_c (falls to zero logarithmically)")

    print("Threshold speed of the pole")
    qs = np.linspace(0.05, 0.999, 400) * QC
    ratio = np.array([wpl(x) / x for x in qs])
    imin = np.argmin(ratio)
    print(f"  omega_pl/q is smallest at q = {qs[imin]/QC:.3f} q_c, value {ratio[imin]:.5e}; at q_c {wplus(QC)/QC:.5e}")
    assert np.all(np.diff(ratio[:imin]) < 0) and qs[imin] > 0.98 * QC
    assert abs(ratio[imin] / (wplus(QC) / QC) - 1) < 1e-3
    vth = wplus(QC) / QC
    vthq = wplus(QC_QUAD) / QC_QUAD
    close(vth, VF + QC / (2 * ME), 1e-9, "v_th = v_F + q_c/2m_e")
    close(vth, 9.54e-3, 2e-3, "v_th exact [c]")
    close(vth * R.CKM, 2860, 2e-3, "v_th exact [km/s]")
    close(vthq, 9.18e-3, 2e-3, "v_th quadratic [c]")
    close(vthq * R.CKM, 2750, 2e-3, "v_th quadratic [km/s]")
    close(vth / R.VMAX, 3.60, 3e-3, "v_th / v_max (exact)")
    close(vthq / R.VMAX, 3.46, 3e-3, "v_th / v_max (quadratic)")
    for m in [10e6, 100e6, 1e9]:
        vm = min(wpl(x) / x + x / (2 * m) for x in qs)
        print(f"  m = {m/1e6:.0f} MeV: smallest v_min over the pole = {vm:.4e} = {vm / R.VMAX:.2f} v_max")
    t1, t2 = maxwell_tail(vthq * R.CKM), maxwell_tail(vth * R.CKM)
    print(f"  untruncated Maxwellian above 2750 km/s: {t1:.2e}; above 2860 km/s: {t2:.2e}")
    assert 1e-50 < t1 < 1e-48 and 1e-54 < t2 < 1e-52
    qx = np.linspace(1.0, 0.9999 * QC, 3000)
    gapx = np.array([wpl(x) for x in qx]) - qx * R.VMAX
    print(f"  exothermic: smallest omega_pl(q) - q v_max on q < q_c = {gapx.min():.2f} eV at q = {qx[np.argmin(gapx)]:.0f} eV")
    close(gapx.min(), 14.7, 1e-2, "|Delta_chi| that opens the pole at v_max, m -> infinity [eV]")
    close(QC_QUAD * R.VMAX, 5.94, 3e-3, "reach at q = 2.24 keV, q v_max [eV]")
    close(QC * R.VMAX, 6.90, 3e-3, "reach at q = 2.60 keV, q v_max [eV]")

    print("Silicon tables near q_c")
    for qq, peak_q, Lr in [(2240, 22.3, 0.069), (2600, 23.1, 0.085)]:
        j = np.argmin(abs(q - qq))
        Lj = d["lf"][:, j]
        ipk = np.argmax(Lj)
        wr = q[j] * R.VMAX
        wf = np.linspace(0, wr, 3000)
        share = np.trapezoid(wf * np.interp(wf, om, Lj), wf) / (np.pi / 2 * 16.6**2)
        print(f"  bin {q[j]:.0f} eV: peak {om[ipk]:.1f} eV; L(q v_max = {wr:.2f} eV)/L(peak) = "
              f"{np.interp(wr, om, Lj) / Lj[ipk]:.3f}; f-sum share below the reach {share:.2e}")
        close(om[ipk], peak_q, 1e-2, "  peak position [eV]")
        close(np.interp(wr, om, Lj) / Lj[ipk], Lr, 3e-2, "  L(reach)/L(peak)")
    for j in [0, 16, 27, 37, 43]:
        Lj = d["lf"][:, j]
        ipk = np.argmax(Lj)
        ab = om[Lj > Lj[ipk] / 2]
        print(f"  ridge: q = {q[j]:.0f} eV, peak {om[ipk]:.1f} eV, half maximum from {ab.min():.1f} to {ab.max():.1f} eV")
    wf = np.arange(R.EG, om[-1], 0.05)
    for m in [100e6]:
        rf = np.array([np.interp(wf, om, d["lf"][:, j]) for j in range(len(q))]).T
        W, Q = np.meshgrid(wf, q, indexing="ij")
        for light in [False, True]:
            integ = Q**3 * R.eta(W / Q + Q / (2 * m)) * R.fdm2(Q, light) * rf
            tot = np.trapezoid(np.trapezoid(integ, q, axis=1), wf)
            for qc in [QC_QUAD, QC]:
                sel = np.trapezoid(np.trapezoid(np.where(Q < qc, integ, 0), q, axis=1), wf)
                print(f"  m = 100 MeV, light = {light}: share of the rate from q < {qc:.0f} eV: {sel / tot:.2e}")

    print("Gas against silicon tables: integrated rates above 1.11 eV, per kg-yr at 1e-37 cm^2")
    for m in [1e6, 10e6, 100e6]:
        for light in [False, True]:
            ws, ss = table_spectrum(m, d, light)
            Rs = np.trapezoid(ss, ws)
            wg, sg = gas_spectrum(m, "lin", q, light)
            Rg = np.trapezoid(sg, wg)
            wm, sm = gas_spectrum(m, "mer", q, light)
            Rm = np.trapezoid(sm, wm)
            print(f"  m = {m/1e6:5.0f} MeV light={light!s:5}: Si {Rs:.3g}, Lindhard {Rg:.3g} ({Rg/Rs:.2f}), "
                  f"Mermin {Rm:.3g} ({Rm/Rs:.2f})")
    print("Spectral ratios at 100 MeV, heavy")
    wq = np.array([2.0, 3.0, 4.4, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0])
    _, ss = table_spectrum(100e6, d, False, w=wq)
    for wv, sv in zip(wq, ss):
        wg, sg = gas_spectrum(100e6, "lin", q, False, wth=wv, wmax=wv + 0.01, dw=0.02)
        wm, sm = gas_spectrum(100e6, "mer", q, False, wth=wv, wmax=wv + 0.01, dw=0.02)
        print(f"  omega = {wv:5.1f} eV: Lindhard/Si = {sg[0]/sv:.2f}, Mermin/Si = {sm[0]/sv:.2f}")
    # free-recoil gap of the gas: at fixed omega the halo needs q >= omega/v_max; empty below omega_- there
    for wv in [20.0, 25.0, 30.0]:
        qmin = wv / R.VMAX
        print(f"  omega = {wv} eV: q >= {qmin:.0f} eV, omega_-(q) = {wminus(qmin):.1f} eV")

    qgap = 2 * ME * (VF + R.VMAX)
    close(qgap / 1e3, 9.85, 3e-3, "q above which omega_-(q) > q v_max, 2 m_e (v_F + v_max) [keV]")
    print("Kurinsky et al. cutoff, applied to silicon (light mediator, v = 0.1, q_min = omega_p/v)")
    qmin = 16.6 / 0.1
    close(qmin, 166, 1e-3, "q_min [eV]")
    for qc in [QC, QC_QUAD]:
        print(f"  ln(5 keV/q_min)/ln({qc:.0f}/q_min) = {np.log(5000 / qmin) / np.log(qc / qmin):.3f}")
    close(np.log(5000 / qmin) / np.log(QC / qmin), 1.24, 5e-3, "log ratio with q_c = 2.60 keV")
    close(np.log(5000 / qmin) / np.log(QC_QUAD / qmin), 1.31, 5e-3, "log ratio with 2.24 keV")
    close((5000 / QC)**2, 3.7, 1e-2, "(5 keV/q_c)^2")
    # pole weight lost near q_c in the 1/q measure (constant omega_p line shape replaced by the exact share)
    xs = np.geomspace(qmin, 0.9999 * QC, 600)
    sh = np.array([pole_share(x) for x in xs])
    lost = 1 - np.trapezoid(sh / xs, xs) / np.log(QC / qmin)
    print(f"  share of the 1/q integral lost to the falling pole weight below q_c: {lost:.3f}")
    print("Pairs from a plasmon (eq:1.5-step, E_g = 1.11 eV, eps_eh = 3.6 eV)")
    for w in [16.6, 16.4]:
        print(f"  omega = {w}: N_eh = {1 + int((w - 1.11) // 3.6)}")
