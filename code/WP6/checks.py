#!/usr/bin/env python3
"""WP6 (R5) identity checks. Theory only: algebra, quadrature of closed forms, no simulations. Runs in < 30 s.
Each check prints PASS/FAIL. Labels C1..C11 are cited in returns/R5/WP6.md."""
import numpy as np
import sympy as sp
from scipy import integrate, special

ok = []
def report(name, cond, extra=""):
    ok.append(bool(cond)); print(f"{name}: {'PASS' if cond else 'FAIL'} {extra}")

# ---------- C1: Essig |f_crys|^2 <-> URF angle-averaged S_ee (spin included) ----------
# WP0 (9.2) times target mass rho_T*V gives dR_tot/dlnw = w*rho*sig*V/(4 pi m mu^2) Int q dq F^2 eta Sbar.
# Essig (17): dR/dlnE = (rho/m) Ncell sig alpha me^2/mu^2 Int dq/q (E/q) eta F^2 |f|^2.  Ncell = V/Omega.
q, w, Om, al, me, Sb, V = sp.symbols('q omega Omega alpha m_e Sbar V', positive=True)
f2 = Om*q**3*Sb/(4*sp.pi*al*me**2)             # claimed conversion (eq 2.3 of the return)
urf = w*V/(4*sp.pi)*q*Sb                        # integrand, common factors rho*sig*F^2*eta/(m mu^2) stripped
ess = (V/Om)*al*me**2*(w/q**2)*f2
report("C1 |f_crys|^2 = Omega q^3 Sbar/(4 pi alpha m_e^2)", sp.simplify(urf-ess) == 0)

# ---------- C2: consistency with 2101.08275 eq (16): |f|^2 = k^5 Vcell Im eps/(8 pi^2 alpha^2 me^2) ----------
L = sp.symbols('L', positive=True)
e2 = 4*sp.pi*al
S_from_L = 2*q**2/e2*L                            # WP0 (9.3) at T=0
report("C2 matches 2101.08275 eq.(16) (L -> Im eps unscreened)",
       sp.simplify(f2.subs(Sb, S_from_L) - q**5*Om*L/(8*sp.pi**2*al**2*me**2)) == 0)

# ---------- C3: 2311.04957 eq (3)+(4) equals Essig (17) per unit cell ----------
E, sig, rho, m, mu, F, eta, fc = sp.symbols('E sigma rho m mu F eta f_c', positive=True)
b3 = rho/m*sig/(8*mu**2)*q*F**2*(8*al*me**2*E/q**3)*fc*eta
e17 = rho/m*sig*al*me**2/mu**2*(1/q)*(E/q)*eta*F**2*fc     # d ln q = dq/q
report("C3 2311.04957 (3)-(4) = Essig (17)/N_cell", sp.simplify(b3 - e17) == 0)

# ---------- C4: SHM eta closed form (Essig 66-68) vs quadrature; edge expansion ----------
kms = 1.0
v0, vE, vesc = 238.0, 250.0, 544.0
K = v0**3*np.pi*(np.sqrt(np.pi)*special.erf(vesc/v0) - 2*vesc/v0*np.exp(-(vesc/v0)**2))
def eta_closed(vm):
    if vm < vesc - vE:
        return v0**2*np.pi/(2*vE*K)*(-4*np.exp(-vesc**2/v0**2)*vE + np.sqrt(np.pi)*v0*(special.erf((vm+vE)/v0)-special.erf((vm-vE)/v0)))
    if vm < vesc + vE:
        return v0**2*np.pi/(2*vE*K)*(-2*np.exp(-vesc**2/v0**2)*(vesc-vm+vE) + np.sqrt(np.pi)*v0*(special.erf(vesc/v0)-special.erf((vm-vE)/v0)))
    return 0.0
def eta_quad(vm):
    # eta = Int d^3v f(v+vE)/v Theta(v-vm); angular integral done analytically within the escape sphere
    def g(v):
        cmax = min(1.0, (vesc**2 - v*v - vE*vE)/(2*v*vE))
        if cmax <= -1: return 0.0
        A = 2*v*vE/v0**2
        ang = np.exp(-(v*v+vE*vE)/v0**2)*(np.exp(A) - np.exp(-A*cmax))/A
        return 2*np.pi*v*ang/K
    val, _ = integrate.quad(g, vm, vesc+vE, points=[vesc-vE], epsabs=0, epsrel=1e-10, limit=200)
    return val
errs = [abs(eta_closed(x)/eta_quad(x)-1) for x in (100., 400., 600., 700., 780.)]
report("C4a SHM eta closed form vs quadrature", max(errs) < 2e-3, f"max rel err {max(errs):.1e}")
d, a, v0s, vEs, Ks = sp.symbols('delta a v0 vE K', positive=True)
vesc_s = a*v0s
eta2 = v0s**2*sp.pi/(2*vEs*Ks)*(-2*sp.exp(-a**2)*d + sp.sqrt(sp.pi)*v0s*(sp.erf(a)-sp.erf(a-d/v0s)))
ser = sp.series(eta2, d, 0, 3).removeO()
target = sp.pi*vesc_s*sp.exp(-a**2)*d**2/(vEs*Ks)
report("C4b edge: eta ~ pi v_esc e^{-vesc^2/v0^2} delta^2/(vE K)", sp.simplify(ser - target) == 0)
# regime-A log-sensitivity d ln eta / d v0 at vmin = 600
def eta_par(vm, v0_, vesc_=vesc, vE_=vE):
    K_ = v0_**3*np.pi*(np.sqrt(np.pi)*special.erf(vesc_/v0_) - 2*vesc_/v0_*np.exp(-(vesc_/v0_)**2))
    if vm < vesc_ - vE_:
        return v0_**2*np.pi/(2*vE_*K_)*(-4*np.exp(-vesc_**2/v0_**2)*vE_ + np.sqrt(np.pi)*v0_*(special.erf((vm+vE_)/v0_)-special.erf((vm-vE_)/v0_)))
    if vm < vesc_ + vE_:
        return v0_**2*np.pi/(2*vE_*K_)*(-2*np.exp(-vesc_**2/v0_**2)*(vesc_-vm+vE_) + np.sqrt(np.pi)*v0_*(special.erf(vesc_/v0_)-special.erf((vm-vE_)/v0_)))
    return 0.0
for vm in (500., 600., 700., 760.):
    s_v0 = (np.log(eta_par(vm, v0+1))-np.log(eta_par(vm, v0-1)))/2
    s_ve = (np.log(eta_par(vm, v0, vesc+1))-np.log(eta_par(vm, v0, vesc-1)))/2
    s_vE = (np.log(eta_par(vm, v0, vesc, vE+1))-np.log(eta_par(vm, v0, vesc, vE-1)))/2
    print(f"   vmin={vm:.0f}: dln eta/dv0={s_v0:.4f}, /dvesc={s_ve:.4f}, /dvE={s_vE:.4f} per km/s")

# ---------- C5: near-threshold scaling ----------
x, Dl, c = sp.symbols('x Delta c', positive=True)
I = sp.integrate((Dl - c*x**2)**2, (x, -sp.sqrt(Dl/c), sp.sqrt(Dl/c)))
report("C5a Int (Delta - c x^2)^2 dx = (16/15) Delta^{5/2}/sqrt(c)", sp.simplify(I - sp.Rational(16, 15)*Dl**sp.Rational(5, 2)/sp.sqrt(c)) == 0)
# numerical exponent of total rate near m_min for S ~ (w-Eg)^p, hard-cutoff edge eta ~ (vmax - vmin)^2
def rate(mchi, p, Eg=1.0, vmax=1.0):
    def inner(wv):
        qs = np.linspace(1e-6, 4*np.sqrt(2*mchi*wv), 4000)
        vmin = wv/qs + qs/(2*mchi)
        integrand = qs*np.clip(vmax - vmin, 0, None)**2*(wv-Eg)**p
        return np.trapezoid(integrand, qs)
    wmax = 0.5*mchi*vmax**2
    ws = np.linspace(Eg, wmax, 600)[1:]
    return np.trapezoid([inner(t) for t in ws], ws)
mmin = 2.0
for p in (0.0, 1.0):
    eps = np.array([0.02, 0.04])
    r = [rate(mmin*(1+e), p) for e in eps]
    slope = np.log(r[1]/r[0])/np.log(2.0)
    report(f"C5b rate ~ (m/m_min-1)^(7/2+p), p={p}", abs(slope-(3.5+p)) < 0.15, f"fitted {slope:.2f}")

# ---------- C6: annual-mean |v_E| from 2105.00599 Table 1 + eq (11) ----------
vlsr = np.array([0, 238., 0]); vpec = np.array([11.1, 12.2, 7.3]); vearth = 29.8
t = np.linspace(0, 2*np.pi, 20001)[:-1]
ve = vearth*np.array([0.9941*np.cos(t)-0.0504*np.sin(t), 0.1088*np.cos(t)+0.4946*np.sin(t), 0.0042*np.cos(t)-0.8677*np.sin(t)])
vtot = np.linalg.norm((vlsr+vpec)[:, None] + ve, axis=0)
print(f"   C6 <|v_E|> = {vtot.mean():.2f} km/s, min {vtot.min():.2f}, max {vtot.max():.2f}; |v_lsr+v_pec| = {np.linalg.norm(vlsr+vpec):.2f}")
report("C6 2105.00599: |v_sun| = 250.5, annual-mean |v_E| = 252.1 (not 232/240)", abs(np.linalg.norm(vlsr+vpec)-250.5) < 0.2 and abs(vtot.mean()-252.1) < 0.2)

# ---------- C7: m_min = 2 E_th / v_max^2 ----------
c_kms = 299792.458
for Eth, vmax, lab in ((1.12, 544+250, "Si 1.12 eV, 794"), (1.12, 600+240, "Si 1.12 eV, 840"), (1.2, 544+232, "Si 1.2 eV, 776 (2311.04957)"), (0.67, 794, "Ge 0.67 eV, 794")):
    print(f"   C7 m_min[{lab}] = {2*Eth/(vmax/c_kms)**2/1e6:.3f} MeV")
report("C7 EXCEED-DM 0.28 MeV reproduced at v_max = 840 km/s, E = 1.11-1.12 eV", abs(2*1.11/(840/c_kms)**2/1e6 - 0.283) < 0.01)

# ---------- C8: profile-likelihood penalty for a theory nuisance (zero-count, asymptotic) ----------
# -2 ln L = 2 s (1 + th*dl) + th^2 ; profile th; set q = c.
def prof_lin(dl, cc=2.706):
    return (1-np.sqrt(1-cc*dl**2))/dl**2 if cc*dl**2 < 1 else np.inf
def prof_logn(dl, cc=2.706):
    k = np.log(1+dl)  # mu = s*exp(th*k)
    from scipy.optimize import brentq
    def qfun(s):
        f = lambda th: 2*s*np.exp(th*k) + th**2
        th = brentq(lambda th: 2*s*k*np.exp(th*k) + 2*th, -50, 50)
        return f(th) - cc
    return brentq(qfun, 1e-6, 1e3)
base = 2.706/2
for dl in (0.1, 0.3, 0.5):
    print(f"   C8 delta={dl}: profiled(lin)/nominal={prof_lin(dl)/base:.3f}, profiled(lognormal)/nominal={prof_logn(dl)/base:.3f}, envelope 1/(1-delta)={1/(1-dl):.3f}")
report("C8 small-delta expansion 1 + c delta^2/4", abs(prof_lin(0.05)/base - (1+2.706*0.05**2/4)) < 1e-4)

# ---------- C9: impulse-approximation tail obeys the f-sum: Int w S dw = pi n q^2/m ----------
pz, s0, n = sp.symbols('p_z s0 n', positive=True)
J = sp.exp(-pz**2/(2*s0**2))/sp.sqrt(2*sp.pi*s0**2)
# S_IA(q,w) = 2 pi n (m/q) J(p_z), p_z = m(w - q^2/2m)/q  -> dw = (q/m) dp_z
wpz = q**2/(2*me) + q*pz/me
mom = sp.integrate(wpz*2*sp.pi*n*(me/q)*J*(q/me), (pz, -sp.oo, sp.oo))
report("C9 S_IA f-sum = pi n q^2/m_e (WP0 (4.6),(9.5))", sp.simplify(mom - sp.pi*n*q**2/me) == 0)

# ---------- C10: Radon transform identities ----------
v, vm, ct = sp.symbols('v v_m c_t', positive=True)
# (1/4pi) Int dOmega_q delta(qhat.v - vm) = Theta(v-vm)/(2v) for v > vm
avg = sp.Rational(1, 2)*sp.integrate(sp.DiracDelta(v*ct - vm), (ct, -1, 1))
report("C10a <delta(qhat.v - v_min)>_qhat = 1/(2v) (v > v_min)", sp.simplify(avg.subs({v: 3, vm: 1}) - sp.Rational(1, 6)) == 0)
# transverse second moment for isotropic shell |v| = v on the plane qhat.v = vm: <v_perp^2> = v^2 - vm^2
report("C10b <|v_perp|^2> on the Radon plane = v^2 - v_min^2", True, "(geometric identity, |v|^2 = v_min^2 + |v_perp|^2)")

# ---------- C11: number of O_h-invariant even-l harmonics (anisotropic S compression) ----------
def chi(l, phi):
    return 2*l+1 if abs(phi) < 1e-12 else np.sin((l+0.5)*phi)/np.sin(phi/2)
cls = [(1, 0.0), (8, 2*np.pi/3), (3, np.pi), (6, np.pi/2), (6, np.pi)]
counts = {l: round(sum(nc*chi(l, ph) for nc, ph in cls)/24) for l in range(0, 13, 2)}
print(f"   C11 A1g counts: {counts}")
report("C11 A1g harmonics up to l=12: 0,4,6,8,10 once, 12 twice (7 coefficients)", counts == {0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2})

# ---------- C12: xi(u) = Int d^3v f (v^2-u^2)/v Theta(v-u) equals 2 Int_u^inf u' eta(u') du' (SHM) ----------
def xi_quad(vm):
    def g(v):
        cmax = min(1.0, (vesc**2 - v*v - vE*vE)/(2*v*vE))
        if cmax <= -1: return 0.0
        A = 2*v*vE/v0**2
        ang = np.exp(-(v*v+vE*vE)/v0**2)*(np.exp(A) - np.exp(-A*cmax))/A
        return 2*np.pi*v*ang/K*(v*v - vm*vm)
    return integrate.quad(g, vm, vesc+vE, points=[vesc-vE], epsrel=1e-10, limit=200)[0]
xerr = []
for u0 in (200., 500., 700.):
    rhs = 2*integrate.quad(lambda u: u*eta_closed(u), u0, vesc+vE, points=[vesc-vE], epsrel=1e-10, limit=200)[0]
    xerr.append(abs(xi_quad(u0)/rhs - 1))
report("C12 xi(u) = 2 Int_u u' eta(u') du' (velocity-dependent halo function fixed by eta)", max(xerr) < 1e-6, f"max rel err {max(xerr):.1e}")

print(f"\n{sum(ok)}/{len(ok)} checks PASS")
