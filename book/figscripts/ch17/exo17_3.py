"""Sect. 17.3 (exothermic and inelastic dark matter across channels): Fig. 17.3, Worked example 17.3 and every number
of the section.  Run directly; all numbers go to exo17_3.log.  Natural units hbar = c = 1, Heaviside-Lorentz
e^2 = 4 pi alpha; energies and momenta in eV, speeds in units of c.

Rate of a dispersing mode (Sect. 17.3, derived in the text).  With sum_ab D_ab S_ab = (2 pi/Omega) sum_nu Y_nu(q)
delta(omega - omega_nu(q)) inserted in eq:8.2-spectrum and Delta < 0:
  exact (orientation-averaged crystal, isotropic halo kernel eta(v_min)/2q of eq:A.8-eta):
     R = (rho_chi/(4 pi^2 m_chi)) int q dq < sum_nu |V|^2 C_nu(q, qhat) eta(|(omega_nu + Delta)/q + q/2m|) >_qhat ,
  where C_nu = int domega S/rho_T for the line of mode nu (per unit target mass);
  shell (v -> 0):  R = (rho_chi/m_chi) (1/(2 pi)^3) 4 pi < sum_roots q_nu^2 |V|^2 C_nu / |q_nu/m + u_nu| >_qhat ,
     q_nu the roots of |Delta| - q^2/2m = omega_nu(q) along qhat, u_nu = d omega_nu/dq the radial group velocity.
Channels and inputs (all reused from earlier chapters, nothing recomputed from first principles):
  [Si phonons] PBE force constants of Sect. 5.2 interpolated by figscripts/ch05/si_ifc.py; one-phonon nuclear response
     int domega S1/rho_T = (pi/2 m_u^2) sum_nu |sum_k e^{i q.tau_k} q.e*_k nu|^2 e^{-2W}/omega_nu  (eq:11.1-S1, as
     figscripts/ch11/limit11_1a.py), 2W = q^2 <u_x^2>, <u_x^2> = 2.45e-3 A^2 (WE 5.7); nucleon coupling, heavy mediator,
     |V_N|^2 = pi sigma_p/mu_chip^2 (eq:11.1-rate), sigma_p = 1e-40 cm^2; threshold omega >= 1 meV (as Sect. 11.1);
     directions: Gauss-Legendre 24 x 48 (phon11.sphere_grid); q log grid 0.3 eV - 40 keV.
  [Si electrons] figscripts/ch10/inel10_9.py unchanged (Knapen-Kozaczuk-Lin RPA+LF tables, eq:10.9-inel with |v_min|,
     threshold = the tables' 1.11 eV, L held at the first bin below 493 eV), sigma_e = 1e-37 cm^2, heavy mediator.
  [Si plasmon] electron gas at the valence density of Si (figscripts/ch10/gas10_3.py): exact Lindhard pole omega_pl(q),
     weight pi/(d eps_1/d omega) (eq:10.3-plrate with Delta in v_min), q < q_c = 2.60 keV; same coupling as [Si electrons].
  [GaAs LO] measured omega_T = 33.62, omega_L = 36.35 meV, eps_inf = 10.88 (WE 5.6; Strauch-Dorner via Dehghani et al.,
     Lockwood et al.), rho_T = 5.361 g/cm^3 (WE 11.3); L = (pi omega_L/2)(1 - omega_T^2/omega_L^2)/eps_inf delta(omega -
     omega_L(q)) (eq:11.2-onebranch, splitting route); LO dispersion from the DFPT phonons of Sect. 5.5 along [100],
     [110], [111] (cached matdyn output figscripts/ch11/gaas11_2_work/lim2a_*.npz, q in 2 pi/a, a = 5.638 A), shifted
     to the measured omega_L at Gamma; dark photon, sigma_e = 1e-40 cm^2 (as Sect. 11.2), light and heavy mediator.
  [NiO magnons] figscripts/ch14/magnon14.py unchanged (J1, J2 of Hutchings-Samuelsen, |S| = 1, Ni2+ <j0>), O_4 heavy
     mediator with |c_4|^2 = 16 pi sigma_e/(3 mu_chie^2) (eq:14.1-sigma), sigma_e = 1e-40 cm^2 (as Fig. 14.1).
  Halo: v0 = 238, v_esc = 544, v_E = 250.5 km/s, rho_chi = 0.3 GeV/cm^3 (Sect. 1.2), eta of App. D.1 (rate10_2.eta).
Outputs: tex/figures/ch17/fig17_3.pdf; exo17_3.log.
"""
import os
import sys
import numpy as np
from scipy import integrate, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ("ch05", "ch10", "ch11", "ch14"):
    sys.path.insert(0, os.path.join(HERE, "..", sub))
import si_ifc            # noqa: E402
import phon11 as P       # noqa: E402
import rate10_2 as R     # noqa: E402
import inel10_9 as IN    # noqa: E402
import gas10_3 as GAS    # noqa: E402
import magnon14 as MAG   # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch17")
LOG = open(os.path.join(HERE, "exo17_3.log"), "w")


def out(s=""):
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


HBARC = 1973.269804            # eV A
ME = R.ME
MU_EV = 931.494e6              # m_u in eV
MP = 938.272e6
CM = R.CM                      # 1 cm in eV^-1
VMAX = R.VMAX
eta = R.eta
TO_KGYR = R.to_per_kg_yr


def mu(a, b):
    return a * b / (a + b)


# ---------------------------------------------------------------------------------------------------------------------
# halo moments
def lab_moments():
    """<v> and <1/v> = eta(0) of the book halo in the laboratory frame (truncated Maxwellian, boosted by v_E)."""
    v0, ve, vesc = R.V0, R.VE, R.VESC

    def f(u, c):  # galactic speed u, cos angle c with -v_E; lab speed |u - v_E|
        return u**2 * np.exp(-u**2 / v0**2)
    num = integrate.dblquad(lambda c, u: f(u, c) * np.sqrt(u**2 + ve**2 - 2 * u * ve * c), 0, vesc, -1, 1)[0]
    den = integrate.dblquad(lambda c, u: f(u, c), 0, vesc, -1, 1)[0]
    v2 = integrate.dblquad(lambda c, u: f(u, c) * (u**2 + ve**2 - 2 * u * ve * c), 0, vesc, -1, 1)[0]
    return num / den / R.CKM, float(eta(0.0)), np.sqrt(v2 / den) / R.CKM


VMEAN, ETA0, VRMS = lab_moments()

# ---------------------------------------------------------------------------------------------------------------------
# silicon one-phonon tables
UX2 = 2.45e-3                  # A^2 (WE 5.7)
TWO_PI_A_SI = 2 * np.pi / 5.431 * HBARC     # eV per unit 2pi/a
QBZ_SI = (6 * np.pi**2 / (5.431**3 / 4))**(1 / 3) * HBARC


def si_tables(nq=420, nt=24, nphi=48):
    qh, wq = P.sphere_grid(nt, nphi)
    q = np.geomspace(0.3, 4.0e4, nq)
    W = np.empty((nq, len(qh), 6))
    C = np.empty((nq, len(qh), 6))
    for i, qq in enumerate(q):
        qv = qq / TWO_PI_A_SI * qh
        w, ev = si_ifc.phonons(qv)
        w = np.maximum(w, 1e-4) * 1e-3                        # eV
        ph = np.exp(2j * np.pi * (qv @ si_ifc.TAU.T))
        amp = np.zeros((len(qh), 6), complex)
        for k in range(2):
            amp += ph[:, k:k + 1] * np.einsum("ni,nij->nj", qq * qh, np.conj(ev[:, 3 * k:3 * k + 3, :]))
        W[i] = w
        C[i] = np.pi * np.abs(amp)**2 * np.exp(-(qq / HBARC)**2 * UX2) / (2 * MU_EV**2 * w)
    return q, qh, wq, W, C


def phonon_rate(m, delta, tab, sigp=1e-40, wth=1e-3, branches=range(6)):
    """exact orientation-averaged one-phonon rate (events/kg/yr), heavy mediator, nucleon coupling."""
    q, qh, wq, W, C = tab
    V2 = np.pi * sigp * CM**2 / mu(m, MP)**2
    acc = np.zeros(len(q))
    for nu in branches:
        vmin = np.abs((W[:, :, nu] + delta) / q[:, None] + q[:, None] / (2 * m))
        acc += ((C[:, :, nu] * eta(vmin) * (W[:, :, nu] >= wth)) * wq[None, :]).sum(1)
    val = R.RHO_CHI / (4 * np.pi**2 * m) * V2 * np.trapezoid(q * acc, q)
    return TO_KGYR(val)


def phonon_shell(m, delta, tab, sigp=1e-40, wth=1e-3, branches=range(6), spectrum=False):
    """v -> 0 shell rate (events/kg/yr) for delta < 0; optionally the line energies and weights."""
    q, qh, wq, W, C = tab
    V2 = np.pi * sigp * CM**2 / mu(m, MP)**2
    tot = 0.0
    lines = []
    for nu in branches:
        g = -delta - q[:, None]**2 / (2 * m) - W[:, :, nu]            # (nq, ndir)
        s = np.sign(g)
        idx_q, idx_d = np.where(s[:-1] * s[1:] < 0)
        for i, d in zip(idx_q, idx_d):
            t = g[i, d] / (g[i, d] - g[i + 1, d])
            qs = q[i] + t * (q[i + 1] - q[i])
            ws = W[i, d, nu] + t * (W[i + 1, d, nu] - W[i, d, nu])
            cs = C[i, d, nu] + t * (C[i + 1, d, nu] - C[i, d, nu])
            dg = abs((g[i + 1, d] - g[i, d]) / (q[i + 1] - q[i]))       # |q/m + u_nu|
            if ws < wth:
                continue
            contrib = wq[d] * 4 * np.pi * qs**2 * V2 * cs / dg / (2 * np.pi)**3
            tot += contrib
            lines.append((ws, contrib))
    val = TO_KGYR(R.RHO_CHI / m * tot)
    if spectrum:
        return val, np.array(lines)
    return val


# ---------------------------------------------------------------------------------------------------------------------
# silicon electrons and plasmon
def electron_rate(m, delta, light=False):
    wg = None
    top = min(IN.WTOP, m * VMAX**2 / 2 - delta)
    if top <= R.EG:
        return 0.0
    wg = np.arange(R.EG, top, 0.05)
    w, s = IN.spectrum(m, delta, light=light, wgrid=wg, nq=700)
    return IN.total(w, s)


_QPL = np.linspace(5.0, GAS.QC * (1 - 1e-4), 260)
_WPL = np.array([GAS.wpl(x) for x in _QPL])


def _dε(qq, w):
    h = 1e-5 * w
    return (GAS.eps_lin(qq, w + h).real - GAS.eps_lin(qq, w - h).real) / (2 * h)


_RES = np.array([np.pi / _dε(x, w) for x, w in zip(_QPL, _WPL)])      # pi/(d eps_1/d omega)


def plasmon_rate(m, delta, light=False):
    vmin = np.abs((_WPL + delta) / _QPL + _QPL / (2 * m))
    integ = _QPL**3 * eta(vmin) * R.fdm2(_QPL, light) * _RES
    return TO_KGYR(R.prefactor(m) * np.trapezoid(integ, _QPL))


def plasmon_shell(m, delta):
    """v -> 0: roots of |Delta| - q^2/2m = omega_pl(q)."""
    g = -delta - _QPL**2 / (2 * m) - _WPL
    i = np.where(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]
    if len(i) == 0:
        return 0.0, np.nan, np.nan
    i = i[0]
    t = g[i] / (g[i] - g[i + 1])
    qs = _QPL[i] + t * (_QPL[i + 1] - _QPL[i])
    ws = _WPL[i] + t * (_WPL[i + 1] - _WPL[i])
    rs = _RES[i] + t * (_RES[i + 1] - _RES[i])
    dg = abs((g[i + 1] - g[i]) / (_QPL[i + 1] - _QPL[i]))
    # Gamma/rho_T = (1/(2pi)^3) 4 pi q^2 |V|^2 S-weight / |g'|, S-weight = (2 q^2/e^2) * rs ; |V|^2 = pi sigma/mu^2
    mue = mu(m, ME)
    V2 = np.pi * R.SIGMA_REF / mue**2
    val = R.RHO_CHI / (m * R.RHO_T) * 4 * np.pi * qs**2 * V2 * (2 * qs**2 / (4 * np.pi * R.ALPHA)) * rs / dg / (2 * np.pi)**3
    return TO_KGYR(val), qs, ws


# ---------------------------------------------------------------------------------------------------------------------
def main():
    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    out("v_max = %.4e; lab <v> = %.4e (%.1f km/s); <v^2>^(1/2) = %.3e; eta(0) = <1/v> = %.1f"
        % (VMAX, VMEAN, VMEAN * R.CKM, VRMS, ETA0))
    uhalf = optimize.brentq(lambda x: float(eta(x)) - ETA0 / 2, 1e-6, VMAX)
    out("eta(u) = eta(0)/2 at u = %.4e (%.1f km/s) = %.3f v_max: FWHM of the line profile = %.3f x its full width"
        % (uhalf, uhalf * R.CKM, uhalf / VMAX, uhalf / VMAX))

    # =============== general kinematics: parabolic modes ===============================================================
    out("\n== Parabolic mode omega = omega0 + q^2/(2 m*): q_nu^2 = 2 mu (|Delta| - omega0), line omega0 + (mu/m*)(|Delta| - omega0)")
    EF = GAS.KF**2 / (2 * ME)
    alpha_pl = 0.6 * EF / GAS.WP
    mstar_pl = ME / (2 * alpha_pl)
    out("Si valence gas: k_F = %.1f eV, E_F = %.2f eV, omega_p = %.2f eV, alpha_pl = 3E_F/5omega_p = %.4f, m*_pl = m_e/(2 alpha_pl) = %.1f keV"
        % (GAS.KF, EF, GAS.WP, alpha_pl, mstar_pl / 1e3))
    out("q_c (exact Lindhard) = %.0f eV, quadratic-dispersion cutoff = %.0f eV" % (GAS.QC, GAS.QC_QUAD))
    # quadratic omega_pl approx used in wpl_quad: sqrt(wp^2 + 0.6 vF^2 q^2) ~ wp + 0.3 vF^2 q^2/wp = wp + q^2/(2 m*)
    out("check: 0.3 v_F^2/omega_p = %.4e = 1/(2 m*_pl) = %.4e" % (0.3 * GAS.VF**2 / GAS.WP, 1 / (2 * mstar_pl)))
    # cutoff of the parabolic dispersion omega_p + q^2/2m* used in the text: where it meets the upper edge of the
    # pair continuum, omega_+ = q v_F + q^2/2m_e
    qc_par = optimize.brentq(lambda qq: GAS.WP + qq**2 / (2 * mstar_pl) - (qq * GAS.VF + qq**2 / (2 * ME)), 500.0, 5000.0)
    out("parabolic dispersion omega_p + q^2/2m* meets q v_F + q^2/2m_e at q = %.0f eV; window at 1 MeV closes %.2f eV above omega_p"
        % (qc_par, qc_par**2 / (2 * mu(1e6, mstar_pl))))
    for m in (0.1e6, 1e6, 10e6):
        mu_pl = mu(m, mstar_pl)
        out("  m_chi = %5.2f MeV: mu_pl = %.1f keV, mu/m* = %.3f, deposited fraction of |Delta| - omega_p = %.3f; "
            "|Delta| - omega_p at q_nu = q_c(quad): %.2f eV"
            % (m / 1e6, mu_pl / 1e3, mu_pl / mstar_pl, mu_pl / mstar_pl, GAS.QC_QUAD**2 / (2 * mu_pl)))
    m = 1e6
    mu_pl = mu(m, mstar_pl)
    for D in (17.0, 18.0, 20.0, 22.0):
        qn = np.sqrt(2 * mu_pl * (D - GAS.WP))
        wline = GAS.WP + (mu_pl / mstar_pl) * (D - GAS.WP)
        width = 2 * mu_pl * qn * VMAX / mstar_pl
        r, qs, ws = plasmon_shell(m, -D)
        out("  1 MeV, |Delta| = %.0f eV: parabolic q_nu = %.0f eV, line %.2f eV, full halo width 2 mu q v_max/m* = %.2f eV, "
            "v_nu = q_nu/mu = %.2e (v_max/v_nu = %.2f); exact pole root q = %.0f eV, omega = %.2f eV"
            % (D, qn, wline, width, qn / mu_pl, VMAX / (qn / mu_pl), qs, ws))
    # threshold |Delta| for the plasmon at v_max (closest approach, WE 10.3: 14.7 eV)
    gap = np.min(_WPL - _QPL * VMAX)
    out("  min over q of omega_pl(q) - q v_max (exact pole, q < q_c) = %.2f eV" % gap)

    # =============== endothermic thresholds ===========================================================================
    out("\n== Endothermic thresholds (lightest mass)")

    def m_gap(D, w0):
        return 2 * (D + w0) / VMAX**2

    def m_lin(D, c, wth):
        """gapless linear mode omega = c q with threshold wth; minimise v_min = (D + c q)/q + q/2m over q >= wth/c."""
        def ok(mm):
            qq = np.geomspace(wth / c, 1e7, 20000)
            return np.min((D + c * qq) / qq + qq / (2 * mm)) <= VMAX
        lo, hi = 1.0, 1e12
        for _ in range(200):
            mid = np.sqrt(lo * hi)
            lo, hi = (lo, mid) if ok(mid) else (mid, hi)
        return hi

    def m_lin_formula(D, c, wth):
        a = 2 * D / (VMAX - c)**2
        if np.sqrt(2 * a * D) >= wth / c:
            return a
        return wth / (2 * c * (VMAX - c - c * D / wth))
    c_si = 9.35 / R.CKM          # c_LA,max of Si (Sect. 11.1)
    c_nio = 1.36e-4               # fastest magnon speed of NiO in the J1-J2 model (Sect. 14.1; the J2-only 1.39e-4 is superseded)
    for D in (0.0, 0.01, 1.0):
        out("  Delta = %.2f eV:" % D)
        out("    Si pairs, E_g = 1.17 eV: %.3f MeV (1.11 eV: %.3f MeV)" % (m_gap(D, 1.17) / 1e6, m_gap(D, 1.11) / 1e6))
        out("    Si optical phonon 64.1 meV: %.2f keV" % (m_gap(D, 0.0641) / 1e3))
        out("    GaAs LO 36.35 meV: %.2f keV" % (m_gap(D, 0.03635) / 1e3))
        out("    Si LA, c = 9.35 km/s, omega_th = 1 meV: %.2f keV (formula %.2f keV)"
            % (m_lin(D, c_si, 1e-3) / 1e3, m_lin_formula(D, c_si, 1e-3) / 1e3))
        out("    NiO magnon, c_M = 1.36e-4, omega_th = 5 meV: %.2f keV (formula %.2f keV)"
            % (m_lin(D, c_nio, 5e-3) / 1e3, m_lin_formula(D, c_nio, 5e-3) / 1e3))
        out("    Si plasmon (flat at omega_p): %.2f MeV > m*_pl -> never with dispersion" % (m_gap(D, GAS.WP) / 1e6))
    out("  crossover Delta = omega_th^2/(2 m c^2) at the Delta = 0 edge mass: Si %.2e eV, NiO %.2e eV"
        % (1e-6 / (2 * m_lin(0, c_si, 1e-3) * c_si**2), 25e-6 / (2 * m_lin(0, c_nio, 5e-3) * c_nio**2)))

    # =============== silicon: Fig. 17.3 ===============================================================================
    out("\n== Silicon, m_chi = 1 MeV (Fig. 17.3)")
    tab = si_tables()
    m = 1e6
    out("q_BZ(Si) = %.0f eV; (1/2) m v_max^2 = %.3f eV" % (QBZ_SI, m * VMAX**2 / 2))
    Dex = np.geomspace(1e-3, 80.0, 34)
    ph_ex = np.array([phonon_rate(m, -D, tab) for D in Dex])
    ph_ac = np.array([phonon_rate(m, -D, tab, branches=range(3)) for D in Dex])
    ph_sh = np.array([phonon_shell(m, -D, tab) for D in Dex])
    ph_el = phonon_rate(m, 0.0, tab)
    Den = np.geomspace(1e-3, 3.6, 30)
    ph_en = np.array([phonon_rate(m, D, tab) for D in Den])
    out("one-phonon (nucleon, sigma_p = 1e-40, heavy, omega >= 1 meV): elastic %.4g /kg/yr" % ph_el)
    for D, a, b, c in zip(Dex, ph_ex, ph_ac, ph_sh):
        qn = np.sqrt(2 * m * D)
        out("  |Delta| = %8.4f eV: exact %.4g, acoustic share %.3f, shell %.4g (shell/exact %.3f), q_nu ~ %.0f eV = %.2f q_BZ, "
            "v_max/v_nu = %.2f, 2W(q_nu) = %.3e" % (D, a, b / a, c, c / a, qn, qn / QBZ_SI, VMAX * m / qn, (qn / HBARC)**2 * UX2))
    for D, a in zip(Den, ph_en):
        out("  endothermic Delta = %.4f eV: %.4g" % (D, a))
    # shell regime closed forms
    for D in (10.0, 50.0):
        qn = np.sqrt(2 * m * D)
        out("  check: rate ratio exact(%.0f eV)/elastic = %.2f" % (D, phonon_rate(m, -D, tab) / ph_el))
    # deposited energy spectrum at |Delta| = 10 eV (shell)
    r10, lines = phonon_shell(m, -10.0, tab, spectrum=True)
    wl, cl = lines[:, 0], lines[:, 1]
    out("  1 MeV, |Delta| = 10 eV, shell: mean deposited %.1f meV, share above 40 meV %.2f"
        % (1e3 * np.sum(wl * cl) / cl.sum(), cl[wl > 0.040].sum() / cl.sum()))

    el_ex = np.array([electron_rate(m, -D) for D in Dex])
    el_el = electron_rate(m, 0.0)
    el_en = np.array([electron_rate(m, D) for D in Den])
    pl_ex = np.array([plasmon_rate(m, -D) for D in Dex])
    out("electrons (sigma_e = 1e-37, heavy, omega >= 1.11 eV): elastic %.4g /kg/yr" % el_el)
    for D, a, b in zip(Dex, el_ex, pl_ex):
        out("  |Delta| = %8.4f eV: pairs %.4g, plasmon pole (gas) %.4g" % (D, a, b))
    for D, a in zip(Den, el_en):
        out("  endothermic Delta = %.4f eV: %.4g" % (D, a))
    thr = optimize.minimize_scalar(lambda x: np.interp(x, _QPL, _WPL) - x * VMAX + x**2 / (2 * m),
                                   bounds=(_QPL[0], _QPL[-1]), method="bounded")
    out("  plasmon threshold at 1 MeV: min_q [omega_pl - q v_max + q^2/2m] = %.2f eV at q = %.0f eV" % (thr.fun, thr.x))
    Dp = np.linspace(14.0, 34.0, 201)
    Rp = np.array([plasmon_rate(m, -D) for D in Dp])
    out("  plasmon pole opens (rate > 0) at |Delta| = %.2f eV; peak %.4g at %.2f eV; last nonzero grid point %.2f eV"
        % (Dp[np.argmax(Rp > 0)], Rp.max(), Dp[np.argmax(Rp)], Dp[np.where(Rp > 0)[0][-1]]))
    for D in (18.0, 20.0, 22.0):
        out("  |Delta| = %.0f eV: plasmon %.4g, pairs (tables) %.4g, ratio %.3f; shell plasmon %.4g"
            % (D, plasmon_rate(m, -D), electron_rate(m, -D), plasmon_rate(m, -D) / electron_rate(m, -D), plasmon_shell(m, -D)[0]))

    # ---- figure ----
    fig, axs = plt.subplots(1, 2, figsize=(6.3, 2.9), sharex=True)
    ax = axs[0]
    ax.loglog(Dex, ph_ex, color="C3", lw=1.5, label="exothermic")
    ax.loglog(Dex, ph_ac, color="C3", lw=0.9, ls="-.", label="acoustic branches")
    ok = ph_sh > 0
    ax.loglog(Dex[ok], ph_sh[ok], color="k", lw=1.0, ls=":", label=r"shell form ($v \to 0$)")
    okn = ph_en > 0
    ax.loglog(Den[okn], ph_en[okn], color="C0", lw=1.3, ls="--", label="endothermic")
    ax.axhline(ph_el, color="0.5", lw=0.7)
    ax.set_title(r"(a) single phonons, $\sigma_p = 10^{-40}\,$cm$^2$", fontsize=9)
    ax.set_ylabel(r"events / (kg yr)")
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    ax = axs[1]
    oke = el_ex > 0
    ax.loglog(Dex[oke], el_ex[oke], color="C3", lw=1.5, label="pairs, exothermic")
    okp = Rp > 0
    ax.loglog(Dp[okp], Rp[okp], color="C2", lw=1.3, label="plasmon pole (gas)")
    okn = el_en > 0
    ax.loglog(Den[okn], el_en[okn], color="C0", lw=1.3, ls="--", label="pairs, endothermic")
    ax.axhline(el_el, color="0.5", lw=0.7)
    ax.axvline(1.11, color="0.5", lw=0.6, ls=":")
    ax.set_title(r"(b) electrons, $\bar\sigma_e = 10^{-37}\,$cm$^2$", fontsize=9)
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    for ax in axs:
        ax.set_xlabel(r"$|\Delta_\chi|$ (eV)")
        ax.set_xlim(1e-3, 80)
    axs[0].set_ylim(1e0, 1e6)
    axs[1].set_ylim(1e-2, 1e8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig17_3.pdf"))
    plt.close(fig)

    # =============== GaAs LO: Worked example 17.3 ======================================================================
    out("\n== GaAs LO (Worked example 17.3)")
    WT, WL, EINF = 0.03362, 0.03635, 10.88
    RHO_GAAS = 5.361e-3 * R.KG_EV / CM**3
    LW = (np.pi * WL / 2) * (1 - WT**2 / WL**2) / EINF            # integrated weight of the LO line in L
    out("integrated LO weight of L: (pi omega_L/2)(1 - omega_T^2/omega_L^2)/eps_inf = %.4e eV; (1/eps_inf - 1/eps_0) splitting route = %.5f"
        % (LW, (1 - WT**2 / WL**2) / EINF))
    a_gaas = 5.638
    tpa = 2 * np.pi / a_gaas * HBARC
    disp = []
    for d in ("100", "110", "111"):
        z = np.load(os.path.join(HERE, "..", "ch11", "gaas11_2_work", "lim2a_%s.npz" % d))
        qq = np.linalg.norm(z["q"], axis=1) * tpa
        disp.append((qq, z["w"][:, 5] * 1e-3))
    w0_dfpt = disp[0][1][0]
    out("DFPT LO at Gamma %.3f meV (measured 36.35)" % (w0_dfpt * 1e3))

    def wlo(qq):
        """direction average of the DFPT LO dispersion, shifted to the measured omega_L."""
        return WL + np.mean([np.interp(qq, a, b) - b[0] for a, b in disp], axis=0)

    def wlo_dir(qq):
        return [WL + np.interp(qq, a, b) - b[0] for a, b in disp]
    E2 = 4 * np.pi * R.ALPHA
    Q0 = R.Q0
    for mg, D in ((30e3, 1.0), (30e3, 0.5), (10e3, 1.0), (100e3, 1.0)):
        qn = optimize.brentq(lambda x: D - x**2 / (2 * mg) - wlo(x), 1e-3, 1e5)
        h = 1e-3 * qn
        ug = (wlo(qn + h) - wlo(qn - h)) / (2 * h)
        vn = qn / mg
        mue = mu(mg, ME)
        res = {}
        for light in (False, True):
            F2 = (Q0 / qn)**4 if light else 1.0
            # shell: R = rho sigma q^3 F^2 L_w / (pi e^2 rho_T mu^2) / (1 + u/v)   [eq:10.9-shell with L = L_w delta]
            sh = R.RHO_CHI * 1e-40 * CM**2 * qn**3 * F2 * LW / (np.pi * E2 * RHO_GAAS * mue**2) / (1 + ug / vn)
            # exact: rho sigma/(8 pi^2 alpha rho_T m mu^2) int dq q^3 F^2 eta(v_min) L_w
            qg = np.geomspace(1e-2, 2 * mg * VMAX + 2 * qn, 6000)
            vmin = np.abs((wlo(qg) - D) / qg + qg / (2 * mg))
            F2g = (Q0 / qg)**4 if light else 1.0
            ex = R.RHO_CHI * 1e-40 * CM**2 / (8 * np.pi**2 * R.ALPHA * RHO_GAAS * mg * mue**2) * \
                np.trapezoid(qg**3 * F2g * eta(vmin) * LW, qg)
            # elastic (Delta = 0)
            vmin0 = np.abs(wlo(qg) / qg + qg / (2 * mg))
            el = R.RHO_CHI * 1e-40 * CM**2 / (8 * np.pi**2 * R.ALPHA * RHO_GAAS * mg * mue**2) * \
                np.trapezoid(qg**3 * F2g * eta(vmin0) * LW, qg)
            res[light] = (TO_KGYR(sh), TO_KGYR(ex), TO_KGYR(el))
        wd = wlo_dir(qn)
        qlo, qhi = qn - mg * VMAX, qn + mg * VMAX
        out("m = %.0f keV, |Delta| = %.2f eV: q_nu = %.1f eV (= %.3f x 2pi/a), v_nu = %.3e, v_max/v_nu = %.3f, "
            "2.5<v^2>/v_nu^2 = %.3f; u_LO = %.2e"
            % (mg / 1e3, D, qn, qn / tpa, vn, VMAX / vn, 2.5 * VRMS**2 / vn**2, ug))
        out("   line: omega_LO(q_nu) = %.3f meV (directions %s), shift %.3f meV; halo width 2 |u| m v_max = %.3f meV; "
            "LO over q_nu -+ m v_max: %.3f - %.3f meV"
            % (wlo(qn) * 1e3, np.round(np.array(wd) * 1e3, 3), (wlo(qn) - WL) * 1e3, 2 * abs(ug) * mg * VMAX * 1e3,
               wlo(max(qlo, 0)) * 1e3, wlo(qhi) * 1e3))
        for light, tag in ((False, "heavy"), (True, "light")):
            sh, ex, el = res[light]
            out("   %s: shell %.4g, exact %.4g /kg/yr (shell/exact %.3f); elastic at this mass %.4g; exo/elastic %.3g"
                % (tag, sh, ex, sh / ex, el, ex / el if el > 0 else np.inf))
    out("GaAs edge masses 2 omega_L/v_max^2 = %.2f keV" % (2 * WL / VMAX**2 / 1e3))
    out("GaAs gap 1.52 eV (low T): |Delta| = 1 eV opens no electronic channel")

    # =============== NiO magnons ======================================================================================
    out("\n== NiO magnons, O_4 heavy mediator, sigma_e = 1e-40 cm^2")
    rho_nio = 4 * (58.693 + 15.999) * 1.66053907e-24 / (MAG.A_NIO * 1e-8)**3
    RHO_NIO = rho_nio * 1e-3 * R.KG_EV / CM**3
    OM_NIO = MAG.A_NIO**3 / 4 / HBARC**3
    SIG = 1e-40 * CM**2

    def fib(n):
        i = np.arange(n) + 0.5
        th = np.arccos(1 - 2 * i / n)
        ph = np.pi * (1 + 5**0.5) * i
        return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], -1)
    dirs = fib(1500)

    def nio_exact(mm, D, wth=5e-3, nq=1500):
        qg = np.geomspace(1.0, 6e4, nq)
        mue = mu(mm, ME)
        c4 = 16 * np.pi * SIG / (3 * mue**2)
        acc = np.zeros(nq)
        for i, qq in enumerate(qg):
            a, b = MAG.ab_nio(dirs * qq / HBARC)
            om = MAG.omega(a, b) * 1e-3
            w = MAG.weight(a, b)
            vmin = np.abs((om + D) / qq + qq / (2 * mm))
            acc[i] = np.mean(w * eta(vmin) * (om >= wth)) * MAG.fmag_ni2(qq / HBARC)**2
        pref = R.RHO_CHI / (mm * RHO_NIO) * np.pi * c4 * MAG.S_NIO / (2 * OM_NIO)
        return TO_KGYR(pref / (4 * np.pi**2) * np.trapezoid(qg * acc, qg))

    def nio_weights(mm, D, wth=5e-3, nq=1500):
        """rate-weighted means of the mode weight w^M and of |F^mag|^2 over the full integral, and the rate without F"""
        qg = np.geomspace(1.0, 6e4, nq)
        aw, a1, f2q = np.zeros(nq), np.zeros(nq), np.zeros(nq)
        for i, qq in enumerate(qg):
            a, b = MAG.ab_nio(dirs * qq / HBARC)
            om = MAG.omega(a, b) * 1e-3
            w = MAG.weight(a, b)
            vmin = np.abs((om + D) / qq + qq / (2 * mm))
            k = eta(vmin) * (om >= wth)
            aw[i] = np.mean(w * k)
            a1[i] = np.mean(k)
            f2q[i] = MAG.fmag_ni2(qq / HBARC)**2
        wbar = np.trapezoid(qg * aw * f2q, qg) / np.trapezoid(qg * a1 * f2q, qg)
        fbar = np.trapezoid(qg * aw * f2q, qg) / np.trapezoid(qg * aw, qg)
        return wbar, fbar

    def nio_shell(mm, D, wth=5e-3):
        mue = mu(mm, ME)
        # q_nu along each direction: solve |D| - q^2/2m = omega(q) by fixed point
        qn = np.full(len(dirs), np.sqrt(2 * mm * (-D)))
        for _ in range(60):
            a, b = MAG.ab_nio(dirs * qn[:, None] / HBARC)
            om = MAG.omega(a, b) * 1e-3
            qn = np.sqrt(2 * mm * np.maximum(-D - om, 0))
        w = MAG.weight(a, b)
        f2 = MAG.fmag_ni2(qn / HBARC)**2
        h = 1e-3 * qn
        a2, b2 = MAG.ab_nio(dirs * (qn + h)[:, None] / HBARC)
        a1, b1 = MAG.ab_nio(dirs * (qn - h)[:, None] / HBARC)
        ug = (MAG.omega(a2, b2) - MAG.omega(a1, b1)) * 1e-3 / (2 * h)
        y = f2 * w * (om >= wth) / (1 + ug * mm / qn)
        val = 4 * R.RHO_CHI * SIG * MAG.S_NIO * qn * y / (3 * OM_NIO * RHO_NIO * mue**2)
        return TO_KGYR(np.mean(val)), np.mean(qn), np.mean(w), np.mean(f2), np.mean(om), np.std(om), np.mean(ug)
    zg = MAG.zone_grid(40, 4 * np.pi / MAG.A_NIO)
    a, b = MAG.ab_nio(zg)
    out("zone average of w^M (40^3 grid of the 4pi/a cube) = %.4f (1 + 2 Delta S = 1.157)" % np.mean(MAG.weight(a, b)))
    for mm, D in ((1e6, -1.0), (1e6, -10.0), (1e5, -1.0)):
        ex = nio_exact(mm, D)
        sh, qn, wm, f2, om, oms, ugm = nio_shell(mm, D)
        el = nio_exact(mm, 0.0)
        out("m = %.1f MeV, |Delta| = %.0f eV: exact %.4g, shell %.4g (shell/exact %.3f) /kg/yr; elastic %.4g; exo/elastic %.3f; "
            "q_nu = %.0f eV (|Q_AF| = %.0f eV), <w> on shell %.3f, <|F|^2> %.3f, mean magnon energy %.1f +- %.1f meV, v_nu/<v> = %.3f"
            % (mm / 1e6, -D, ex, sh, sh / ex, el, ex / el, qn, np.linalg.norm(MAG.Q_AF) * HBARC, wm, f2, om * 1e3, oms * 1e3,
               qn / mm / VMEAN))
        out("   v_max/v_nu = %.3f; mean radial group velocity %.3e; halo width 2 u m v_max = %.1f meV"
            % (VMAX * mm / qn, ugm, 2 * abs(ugm) * mm * VMAX * 1e3))
        wel, fel = nio_weights(mm, 0.0)
        out("   elastic, rate-weighted: <w> = %.3f, <|F|^2> = %.3f; decomposition (v_nu/<v>) (<F^2>_shell/<F^2>_el) "
            "(<w>_shell/<w>_el) = %.3f x %.3f x %.3f = %.3f against shell/elastic %.3f"
            % (wel, fel, qn / mm / VMEAN, f2 / fel, wm / wel, qn / mm / VMEAN * f2 / fel * wm / wel, sh / el))


if __name__ == "__main__":
    main()
