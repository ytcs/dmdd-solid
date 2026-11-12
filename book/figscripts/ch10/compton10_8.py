"""Dark Compton scattering on a free electron at rest (Sect. 10.8): checks of every statement of the text, Worked
example 10.8 and the numbers of Limit 10.8b.  Natural units, Heaviside-Lorentz, e^2 = 4 pi alpha.

Processes (tree level, one electron, both initial particles at rest):
  vector  V(k) + e(p) -> gamma(k') + e(p'),  coupling zeta e V_mu psibar gamma^mu psi (dark photon, Sect. 1.4)
  ALP     a(k) + e(p) -> gamma(k') + e(p'),  coupling g_aee a psibar i gamma^5 psi  (pseudoscalar form)
Amplitude (two diagrams, s- and u-channel electron propagator, metric (+,-,-,-)):
  vector: M = zeta e^2 ubar(p') [ eps'* (p+k+m)/(s-m^2) eps + eps (p-k'+m)/(u-m^2) eps'* ] u(p)
  ALP:    M = g e     ubar(p') [ eps'* (p+k+m)/(s-m^2) g5  + g5  (p-k'+m)/(u-m^2) eps'* ] u(p)
  (overall phases dropped).  Spin sums done numerically with explicit Dirac matrices (Dirac representation); the
  massive-vector polarization sum uses the three physical polarizations of V at rest; current conservation
  k_mu M^mu = 0 is checked numerically, so -g_mu,nu may replace the full massive sum.
Rate per incident particle at rest: sigma v = |M|^2_avg omega' / (16 pi m m_e (m + m_e))  (two-body phase space,
  isotropic after the polarization average; checked by averaging over 26 directions of k').
Sources compared (arXiv:2109.08168v2, PDF equation numbers):
  Eq. (2) = (12): sigma v = e^4 zeta^2 (m+2me)(m^2+2 me m+2me^2) / (24 pi me^2 (m+me)^3)  [their eps = our zeta]
  Eq. (9): spin-averaged |M|^2 of the vector case (as printed), evaluated at omega = m
  Eq. (3) = (17): sigma v = e^2 g^2 m (m+2me)^2 / (16 pi me^2 (m+me)^4) * m ... i.e. R = (ne rho/rhoT) e^2 g^2 m (m+2me)^2/(16 pi me^2 (m+me)^4)
            so sigma v = e^2 g^2 m^2 (m+2me)^2 / (16 pi me^2 (m+me)^4)
  Eq. (15): spin-averaged |M|^2 of the ALP case (as printed), evaluated at omega = m
Non-relativistic forms derived in the text:
  vector (seagull, NR recoil): sigma v = zeta^2 sigma_Th omega'/(m (1 + omega'/me)),  omega' + omega'^2/2me = m
  ALP (spin seagull):          sigma v = e^2 g^2 m omega' / (8 pi me^4 (1 + omega'/me)), same omega'
Silicon and germanium numbers: NIST XCOM photoelectric cross sections (files xcom_si.txt, xcom_ge.txt), Z/A
  from standard atomic weights (Si 28.0855, Ge 72.630); rho_chi = 0.3 GeV cm^-3 (Sect. 1.2).
Output: printed log (compton10_8.log).
"""
import itertools
import numpy as np
import sympy as sp

ALPHA = 1 / 137.035999084
E = np.sqrt(4 * np.pi * ALPHA)
ME = 510998.95  # eV

# ---------------- Dirac algebra (Dirac representation) ----------------
I2 = np.eye(2)
Z2 = np.zeros((2, 2))
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
G0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
GI = [np.block([[Z2, s], [-s, Z2]]) for s in SIG]
GAM = [G0] + GI
G5 = np.block([[Z2, I2], [I2, Z2]]).astype(complex)
METRIC = np.diag([1, -1, -1, -1])


def slash(a):
    return sum(METRIC[mu, mu] * a[mu] * GAM[mu] for mu in range(4))


def mdot(a, b):
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


def spinors(p, m):
    """u(p, s) for s = up, down (normalization ubar u = 2m)."""
    E_ = p[0]
    out = []
    for chi in (np.array([1, 0], complex), np.array([0, 1], complex)):
        sp_ = sum(p[i + 1] * SIG[i] for i in range(3))
        out.append(np.sqrt(E_ + m) * np.concatenate([chi, sp_ @ chi / (E_ + m)]))
    return out


def photon_pols(n):
    n = n / np.linalg.norm(n)
    a = np.array([1.0, 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(n, a); e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return [np.concatenate([[0], e1]), np.concatenate([[0], e2])]


def kinematics(m, n):
    wp = m * (m + 2 * ME) / (2 * (m + ME))       # omega' at threshold
    k = np.array([m, 0, 0, 0.0])
    p = np.array([ME, 0, 0, 0.0])
    kp = wp * np.concatenate([[1], n])
    pp = k + p - kp
    return k, p, kp, pp, wp


def msq(m, n, kind="vector", gauge_check=False):
    k, p, kp, pp, wp = kinematics(m, n)
    s = mdot(p + k, p + k); u = mdot(p - kp, p - kp)
    Sprop = (slash(p + k) + ME * np.eye(4)) / (s - ME**2)
    Uprop = (slash(p - kp) + ME * np.eye(4)) / (u - ME**2)
    ui = spinors(p, ME); uf = spinors(pp, ME)
    if kind == "vector":
        vpols = [np.array([0, 1.0, 0, 0]), np.array([0, 0, 1.0, 0]), np.array([0, 0, 0, 1.0])]
        if gauge_check:
            vpols = [k / m]   # timelike unit vector along k: amplitude must vanish
        vert = [slash(ev) for ev in vpols]
        coup = E**2
        navg = 3 * 2
    else:
        vert = [G5]
        coup = E
        navg = 2
    tot = 0.0
    gchk = 0.0
    for V in vert:
        for epp in photon_pols(n):
            Ep = slash(np.conj(epp))
            O = Ep @ Sprop @ V + V @ Uprop @ Ep
            for a in ui:
                for b in uf:
                    amp = coup * (b.conj() @ G0) @ O @ a
                    tot += abs(amp)**2
        # photon gauge check: eps' -> k'
        Ek = slash(kp)
        O = Ek @ Sprop @ V + V @ Uprop @ Ek
        for a in ui:
            for b in uf:
                gchk += abs((b.conj() @ G0) @ O @ a)**2
    return tot / navg, gchk, wp


def dirs(nd=26):
    out = []
    for v in itertools.product((-1, 0, 1), repeat=3):
        if v != (0, 0, 0):
            out.append(np.array(v, float) / np.linalg.norm(v))
    return out


def sv_trace(m, kind):
    vals = [msq(m, n, kind)[0] for n in dirs()]
    wp = m * (m + 2 * ME) / (2 * (m + ME))
    return np.mean(vals) * wp / (16 * np.pi * m * ME * (m + ME)), np.std(vals) / np.mean(vals)


def sv_eq2(m):          # per zeta^2
    return E**4 * (m + 2 * ME) * (m**2 + 2 * ME * m + 2 * ME**2) / (24 * np.pi * ME**2 * (m + ME)**3)


def sv_eq3(m):          # per g^2
    return E**2 * m**2 * (m + 2 * ME)**2 / (16 * np.pi * ME**2 * (m + ME)**4)


def sv_alp_corr(m):     # per g^2, the corrected form
    return E**2 * m**2 * (m + 2 * ME) / (16 * np.pi * ME**2 * (m + ME)**3)


def eq9(m):             # 2109.08168 Eq. (9) at omega = m (spin-averaged |M|^2 per zeta^2)
    w = m; wp = m * (m + 2 * ME) / (2 * (m + ME))
    br = ((2 * ME**2 + m**2) / wp**2 + 4 * ME * wp / (2 * ME * w + m**2)
          + 4 * (2 * ME**2 + m**2) * (ME**2 + 2 * ME * w + m**2) / (2 * ME * w + m**2)**2
          + (m**4 + 4 * ME**2 * (w**2 - m**2) - 8 * ME**3 * (w + ME)) / (ME * wp * (2 * ME * w + m**2)))
    return E**4 / 6 * br


def eq15(m):            # 2109.08168 Eq. (15) at omega = m (|M|^2 per g^2)
    w = m; wp = m * (m + 2 * ME) / (2 * (m + ME))
    br = (m**2 / wp**2 + (m**4 - 4 * m**2 * ME**2 + 4 * ME**2 * w**2) / (ME * wp * (m**2 + 2 * ME * w))
          + 4 * m**2 * ME**2 / (m**2 + 2 * ME * w)**2 + (4 * ME * wp - 8 * ME * w) / (m**2 + 2 * ME * w))
    return E**2 / 4 * br


def main():
    print("=== numerical Dirac traces at threshold (V or a at rest on e at rest) ===")
    n0 = np.array([0.3, -0.5, 0.81]); n0 /= np.linalg.norm(n0)
    for x in (1e-3, 0.01, 0.1, 0.1957, 0.5, 1.0, 2.0, 5.0):
        m = x * ME
        g_v, _, wp = msq(m, n0, "vector", gauge_check=True)
        mv, gph, _ = msq(m, n0, "vector")
        svt, spread = sv_trace(m, "vector")
        sva, spread_a = sv_trace(m, "alp")
        ma_, gph_a, _ = msq(m, n0, "alp")
        gph = gph * E**4 / 6; gph_a = gph_a * E**2 / 2   # same normalization as |M|^2_avg
        mv_req = sv_eq2(m) * 16 * np.pi * m * ME * (m + ME) / wp
        print(f"x = {x:7.4f}: vector k_mu M^mu check {g_v/mv:.1e}, photon check {gph/mv:.1e}; angular spread {spread:.1e};"
              f" trace/Eq.(2) = {svt/sv_eq2(m):.12f}; Eq.(9)/trace |M|^2 = {eq9(m)/mv:.6f};"
              f" |M|^2 from Eq.(2) / trace = {mv_req/mv:.12f}")
        print(f"            ALP photon check {gph_a/ma_:.1e}, spread {spread_a:.1e}; trace/corrected = {sva/sv_alp_corr(m):.12f};"
              f" Eq.(3)/trace = {sv_eq3(m)/sva:.10f}; (m+2me)/(m+me) = {(m+2*ME)/(m+ME):.10f}; Eq.(15)/trace |M|^2 = {eq15(m)/ma_:.6f}")

    print("\n=== closed forms and series (sympy), x = m/m_e, normalized to zeta^2 sigma_Th ===")
    x = sp.symbols("x", positive=True)
    F_exact = sp.Rational(1, 4) * (x + 2) * (x**2 + 2 * x + 2) / (x + 1)**3
    y = -1 + sp.sqrt(1 + 2 * x)                      # omega'/m_e with NR recoil
    F_nr = (y / x) / (1 + y)
    y2 = x * (x + 2) / (2 * (x + 1))                 # exact two-body omega'/m_e
    F_nr2 = (y2 / x) / (1 + y2)
    for name, F in (("Eq. (2) (exact)", F_exact), ("seagull, NR recoil", F_nr), ("seagull, exact omega'", F_nr2)):
        print(f"{name:24s}: {sp.series(F, x, 0, 4).removeO().expand()}")
    print("difference exact - NR recoil:", sp.series(F_exact - F_nr, x, 0, 5).removeO().expand())
    print("large x: Eq. (2) ->", sp.limit(F_exact, x, sp.oo), "; NR form ->", sp.limit(F_nr, x, sp.oo))
    Fa_exact = x**2 * (x + 2) / (x + 1)**3 / 2         # sigma v / (e^2 g^2 / (8 pi me^2))... normalized below
    # normalize ALP rates to e^2 g^2 m^2/(8 pi me^4) = (e^2 g^2/(8 pi me^2)) x^2
    Fa_ex = (x + 2) / (2 * (x + 1)**3)
    Fa_eq3 = (x + 2)**2 / (2 * (x + 1)**4)
    Fa_nr = (y / x) / (1 + y)
    for name, F in (("ALP exact tree", Fa_ex), ("ALP Eq. (3)", Fa_eq3), ("ALP spin seagull, NR recoil", Fa_nr)):
        print(f"{name:28s}: {sp.series(F, x, 0, 3).removeO().expand()}  (x -> 0: {sp.limit(F, x, 0)})")
    print("ratio Eq.(3)/exact:", sp.simplify(Fa_eq3 / Fa_ex))

    # numerical comparison for the plots
    for xv in (0.01, 0.05, 0.1, 0.1957, 0.3, 0.5, 1.0, 1.957):
        fe = float(F_exact.subs(x, xv)); fn = float(F_nr.subs(x, xv)); fn2 = float(F_nr2.subs(x, xv))
        print(f"x = {xv:6.4f} (m = {xv*ME/1e3:7.1f} keV): exact {fe:.5f}, NR {fn:.5f} (ratio {fn/fe:.5f}), "
              f"NR with exact omega' {fn2:.5f} (ratio {fn2/fe:.5f}); x^3 estimate 5/8 x^3 = {5/8*xv**3:.2e}, rel diff {fn/fe-1:.2e}")
    for xv in (0.02, 0.05):
        fe = float(F_exact.subs(x, xv)); fn = float(F_nr.subs(x, xv))
        print(f"   x = {xv}: |NR/exact - 1| = {abs(fn/fe-1):.2e}")
    # where NR within 1% and 10%
    xs = np.logspace(-3, 1, 4001)
    fe = sp.lambdify(x, F_exact)(xs); fn = sp.lambdify(x, F_nr)(xs)
    for tol in (0.01, 0.1):
        bad = np.where(np.abs(fn / fe - 1) > tol)[0]
        print(f"NR vector form within {tol:.0%} of Eq. (2) for x < {xs[bad.min()]:.4f} (m < {xs[bad.min()]*ME/1e3:.1f} keV)")
    fa = sp.lambdify(x, Fa_ex)(xs); fna = sp.lambdify(x, Fa_nr)(xs)
    for tol in (0.1,):
        bad = np.where(np.abs(fna / fa - 1) > tol)[0]
        print(f"NR ALP form within {tol:.0%} of the exact tree for x < {xs[bad.min()]:.4f} (m < {xs[bad.min()]*ME/1e3:.1f} keV)")
    i = np.argmax(sp.lambdify(x, x**2 * Fa_ex)(xs)); j = np.argmax(sp.lambdify(x, x**2 * Fa_eq3)(xs))
    print(f"maximum of rate per particle density (sigma v / m): exact at x = {xs[np.argmax(xs*Fa_ex.subs(x,1) if False else sp.lambdify(x, x*Fa_ex)(xs))]:.3f},"
          f" Eq. (3) at x = {xs[np.argmax(sp.lambdify(x, x*Fa_eq3)(xs))]:.3f}")

    print("\n=== Worked example 10.8: m = 100 keV ===")
    m = 100e3; xv = m / ME
    fac = (m + 2 * ME) / (m + ME)
    wp = m * (m + 2 * ME) / (2 * (m + ME)); wC = m - wp
    print(f"x = {xv:.4f}; factor (m+2me)/(m+me) = {fac:.4f}; sqrt = {np.sqrt(fac):.4f}; omega' = {wp/1e3:.3f} keV;"
          f" electron recoil omega_C = m^2/(2(me+m)) = {wC/1e3:.3f} keV")
    sth = E**4 / (6 * np.pi * ME**2)
    cm = 5.067731e4
    print(f"sigma_Th = {sth/cm**2:.4e} cm^2")
    print(f"vector: sigma v/(zeta^2 sigma_Th) exact {sv_eq2(m)/sth:.4f}; NR {float(F_nr.subs(x, xv)):.4f}")
    print(f"ALP: sigma v/g^2 exact {sv_alp_corr(m)/cm**2:.4e} cm^2, Eq.(3) {sv_eq3(m)/cm**2:.4e} cm^2;"
          f" NR spin seagull {E**2*m*wp/(8*np.pi*ME**4*(1+wp/ME))/cm**2:.4e} cm^2; m->0 form e^2 g^2 m^2/(8 pi me^4) = {E**2*m**2/(8*np.pi*ME**4)/cm**2:.4e}")
    # silicon and germanium: absorption vs Compton at 100 keV
    uamu_g = 1.66053907e-24
    rho_chi = 0.3e6  # keV cm^-3
    for el, Z, A, fn_ in (("Si", 14, 28.0855, "xcom_si.txt"), ("Ge", 32, 72.630, "xcom_ge.txt")):
        d = np.loadtxt(f"/home/user/dmdd-solid/book/figscripts/data/10.8/{fn_}", comments="#")
        Emev, coh, incoh, pe = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
        mupe = np.exp(np.interp(np.log(0.1), np.log(Emev), np.log(pe)))     # cm^2/g at 100 keV
        mu_inc = np.exp(np.interp(np.log(0.1), np.log(Emev), np.log(incoh)))
        ne_per_g = Z / (A * uamu_g)
        # ALP: absorption per g per s at g = 1: (rho/m) (3 m^2/(4 me^2 e^2)) mu_pe c  ; Compton: (rho/m) ne sigma v c
        c = 2.99792458e10
        abs_a = rho_chi / 100.0 * 3 * m**2 / (4 * ME**2 * E**2) * mupe * c
        comp_a = rho_chi / 100.0 * ne_per_g * sv_alp_corr(m) / cm**2 * c
        comp_a3 = rho_chi / 100.0 * ne_per_g * sv_eq3(m) / cm**2 * c
        abs_v = rho_chi / 100.0 * mupe * c
        comp_v = rho_chi / 100.0 * ne_per_g * sv_eq2(m) / cm**2 * c
        print(f"{el} at 100 keV: mu_PE/rho = {mupe:.4e} cm^2/g, incoherent photon {mu_inc:.4e}; n_e/rho_T = {ne_per_g:.4e} /g")
        print(f"   dark photon: Compton/absorption = {comp_v/abs_v:.3f};  ALP: corrected Compton/absorption = {comp_a/abs_a:.3f},"
              f" Eq.(3) Compton/absorption = {comp_a3/abs_a:.3f}; total ALP rate with Eq.(3) / corrected total = {(abs_a+comp_a3)/(abs_a+comp_a):.4f}")
        # where Compton = absorption (crossover), dark photon and ALP
        mm = np.logspace(np.log10(5e3), np.log10(1e6), 2000)
        mpe = np.exp(np.interp(np.log(mm / 1e6), np.log(Emev), np.log(pe)))
        rv = ne_per_g * sv_eq2(mm) / cm**2 / mpe
        ra = ne_per_g * sv_alp_corr(mm) / cm**2 / (3 * mm**2 / (4 * ME**2 * E**2) * mpe)
        ra3 = ne_per_g * sv_eq3(mm) / cm**2 / (3 * mm**2 / (4 * ME**2 * E**2) * mpe)
        for nm, r in (("dark photon", rv), ("ALP corrected", ra), ("ALP Eq.(3)", ra3)):
            k = np.where(np.diff(np.sign(r - 1)))[0]
            print(f"   {nm}: Compton = absorption at m = {', '.join(f'{mm[i]/1e3:.1f}' for i in k)} keV")


def extra():
    """Numbers quoted in the text that are not printed above."""
    EK_GE = 11103.0          # eV, Ge K edge (XCOM)
    print(f"\nomega_C = Ge K binding (11.1 keV) at m = {(EK_GE + np.sqrt(EK_GE**2 + 2*EK_GE*ME))/1e3:.1f} keV")
    d = np.loadtxt("/home/user/dmdd-solid/book/figscripts/data/10.8/xcom_si.txt", comments="#")
    Emev, tot = d[:, 0], d[:, 6]
    wg = 91.817e-3
    mu = np.exp(np.interp(np.log(wg), np.log(Emev), np.log(tot)))
    print(f"Si total attenuation (with coherent) at {wg*1e3:.1f} keV: {mu:.4f} cm^2/g; length 1/(mu rho) = {1/(mu*2.33):.2f} cm")
    wp_all = 31.1
    print(f"n_r - 1 = -omega_p^2/(2 omega^2) at 50 keV with omega_p = 31.1 eV: {-wp_all**2/(2*5e4**2):.2e}")


if __name__ == "__main__":
    extra()
    main()
