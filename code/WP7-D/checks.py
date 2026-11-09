"""WP7-D checks (R10): extensions beyond single-vertex golden-rule rates.
Run:  python3 -I checks.py     Prints PASS/FAIL per check (labels WP7D-Cn, CONVENTIONS sec. 14). Sympy (+ mpmath quadrature for the
three numeric halo/occupation numbers). Units: hbar = c = 1, Heaviside-Lorentz e^2 = 4 pi alpha (CONVENTIONS sec. 1).
Each check names the equation of returns/R10/WP7-D.md it supports."""
import sympy as sp
import mpmath as mp
from sympy import I, Rational as Q, sqrt, pi, exp, sin, cos, oo, symbols, simplify, series, Matrix

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:86s} {note}")
def is0(e): return sp.simplify(sp.expand(e)) == 0

# ---------------------------------------------------------------- C1: classical field <-> quantum absorption (D.3)
w, phi0, y, rho, m, ImR = symbols('omega phi0 y rho m ImR', real=True)
# classical monochromatic field phi = phi0 cos(w t): time-averaged energy density rho = w^2 phi0^2/2 (m = w at k->0)
P_class = -(y**2*w*phi0**2/2)*ImR                       # (D.3) power per volume from Kubo with R of WP0 (3.2)
n_phi = (w**2*phi0**2/2)/w                              # quanta per volume
P_quant = w*n_phi*(-(y**2/w)*ImR)                      # omega * n * Gamma_net, WP0 (3.5)
rep("WP7D-C1a classical absorbed power == omega n_phi Gamma_net (WP0 (3.5))  (D.3)", is0(P_class - P_quant))
# explicit Kubo/Newton check on a damped oscillator: M(x''+g x'+W^2 x) = F cos(w t); <F cos * x'> = (F^2/2) w Im chi
t, F, M, g, W = symbols('t F M g W', positive=True)
wo = symbols('omega_o', positive=True)
chi = 1/(M*(W**2 - wo**2 - I*g*wo))
cR, cI = symbols('chi_R chi_I', real=True)
xt = F*(cR*cos(wo*t) + cI*sin(wo*t))                  # Re[chi F e^{-i w t}]
Pavg = sp.integrate(sp.expand(F*cos(wo*t)*sp.diff(xt, t)), (t, 0, 2*pi/wo))*wo/(2*pi)
chiI = sp.simplify(sp.im(sp.expand_complex(chi)))
rep("WP7D-C1b damped mode: <F x'> = (F^2/2) w Im chi(w) > 0, chi = -R  (D.3), sign of Im R",
    is0(Pavg - F**2/2*wo*cI) and is0(chiI - g*wo/(M*((W**2 - wo**2)**2 + g**2*wo**2))))

# ---------------------------------------------------------------- C2: field spectrum normalisation and Foster et al. Eq. (24) (D.1)
v, A = symbols('v A', positive=True)
fsp = sp.Function('f')
# S_phi(w>0) = (pi rho/m^2) F_phi(w), F_phi = f(v)/(m v), w = m(1+v^2/2); two-sided integral of dw/2pi gives rho/m^2
norm = 2*(1/(2*pi))*(pi*rho/m**2)                      # times int F dw = 1, both signs of w
rep("WP7D-C2a int dw/2pi S_phi = <phi^2> = rho/m^2  (D.1)", is0(norm - rho/m**2))
# 1711.10489 Eq. (12)-(15): Phi_SQUID = (alpha/2) sqrt(L/Lp) g B V m a  ->  <S_PhiPhi> = A pi f/(m v), A = (alpha^2/4)(L/Lp) g^2 B^2 V^2 rho
al, L, Lp, gg, B, VB = symbols('alpha_s L L_p g B V_B', positive=True)
Sa = pi*rho*fsp(v)/(m*v)/m**2
SPhi = (al/2)**2*(L/Lp)*(gg*B*VB*m)**2*Sa
Afos = al**2/4*(L/Lp)*gg**2*B**2*VB**2*rho
rep("WP7D-C2b <S_PhiPhi> = A pi f(v)/(m v) == 1711.10489 Eq. (24)", is0(SPhi - Afos*pi*fsp(v)/(m*v)))

# ---------------------------------------------------------------- C3: Asimov TS (D.6) vs 1711.10489 Eq. (54)
T, lamB = symbols('T lambda_B', positive=True)
lam_s = A*pi*fsp(v)/(m*v)
TS_ours = T*sp.Integral((lam_s/lamB)**2*m*v/(2*pi), (v, 0, oo))     # T int dw/2pi (S_sig/S_n)^2, dw = m v dv
TS_fos = A**2*(T*pi/(2*m))*sp.Integral(fsp(v)**2/(v*lamB**2), (v, 0, oo))
rep("WP7D-C3 T int(dw/2pi)(S_sig/S_n)^2 == A^2 (T pi/2m) int dv f^2/(v lambda_B^2) (1711.10489 Eq. (54))",
    is0(sp.simplify(TS_ours.doit() - TS_fos.doit())) or sp.simplify((TS_ours.args[0]) - TS_fos.args[0]) == 0)

# ---------------------------------------------------------------- C4: short-time (Fejer) limit and crossover (D.6)
xx = symbols('x', real=True)
fe4 = sp.integrate((sin(xx/2)/(xx/2))**4, (xx, -oo, oo))
rep("WP7D-C4a int (sin(x/2)/(x/2))^4 dx = 4 pi/3  (Fejer^2 weight, D.6)", is0(fe4 - 4*pi/3))
Pw, Sn, tc = symbols('P S_n t_coh', positive=True)
TS_short = T*(Pw*T/Sn)**2*(4*pi/3)/(2*pi*T)            # T * (P T/S_n)^2 * int dw/2pi sinc^4(wT/2)
TS_long = T*tc*(Pw/Sn)**2                              # box line of width 2 pi/t_coh
rep("WP7D-C4b TS(t_int<<t_coh) = (2/3)(P t_int/S_n)^2", is0(TS_short - Q(2, 3)*(Pw*T/Sn)**2))
Tx = sp.solve(sp.Eq(TS_short, TS_long), T)
rep("WP7D-C4c crossover t_int = (3/2) t_coh; amplitude thresholds ~ t^-1/2 and (t t_coh)^-1/4 (1306.6089 Eqs. (8),(9))",
    any(is0(s - Q(3, 2)*tc) for s in Tx))

# ---------------------------------------------------------------- C5: Bloch linear response, transient and steady state (D.5)
Om, M0, T2, dl = symbols('Omega_a M_0 T_2 delta', positive=True)
tt = symbols('t', positive=True)
mt = I*Om*M0*(1 - exp(-(I*dl + 1/T2)*tt))/(I*dl + 1/T2)      # m' = -(i d + 1/T2) m + i Om M0, m(0) = 0
ode = sp.simplify(sp.diff(mt, tt) - (-(I*dl + 1/T2)*mt + I*Om*M0))
rep("WP7D-C5a m(t) solves the rotating-frame linearised Bloch equation (retarded convolution)", ode == 0)
mT2inf = sp.limit(mt, T2, oo)
rep("WP7D-C5b T2->oo: |m| = Om M0 |sin(d t/2)|/(d/2)  (vs 1306.6089 Eq. (1) sin(dt)/d; equal as d->0)",
    is0(sp.simplify(sp.Abs(sp.expand_complex(mT2inf))**2 - (Om*M0*2*sin(dl*tt/2)/dl)**2).rewrite(cos)))
mss = I*Om*M0/(I*dl + 1/T2)                               # t -> oo: the e^{-t/T2} transient has decayed
rep("WP7D-C5c t->oo: |m| = Om M0 T2/sqrt(1+d^2 T2^2) -> u M0 Om T2 at d = 0 (2101.01241 Eq. (1))",
    is0(sp.simplify(sp.expand_complex(mss*sp.conjugate(mss))) - (Om*M0*T2)**2/(1 + dl**2*T2**2)))
rep("WP7D-C5d d->0, t<<T2: |m| -> Om M0 t (resonant growth of 1306.6089 Eq. (1))",
    is0(sp.limit(sp.limit(mt, T2, oo), dl, 0) - I*Om*M0*tt))

# ---------------------------------------------------------------- C6: BAR Lorentzian vs DM line (D.7); SHM line-shape maximum
gm, Dl, wn = symbols('gamma Delta omega_n', positive=True)
rep("WP7D-C6a int dDelta gamma/(4 Delta^2+gamma^2) = pi/2 (narrow-mode limit)", is0(sp.integrate(gm/(4*Dl**2 + gm**2), (Dl, -oo, oo)) - pi/2))
rep("WP7D-C6b on resonance m^2 g/((m^2-wn^2)^2+wn^2 g^2) = 1/g = Q_s/m (2501.05504 Eqs. (7)->(8))",
    is0((m**2*gm/((m**2 - wn**2)**2 + wn**2*gm**2)).subs(m, wn) - 1/gm))
kms = 1/299792.458
v0, vo = 238*kms, 250.5*kms
def f_shm(u):  # 1711.10489 Eq. (9) speed distribution, no escape cut
    return u/(mp.sqrt(mp.pi)*v0*vo)*mp.e**(-(u + vo)**2/v0**2)*(mp.e**(4*u*vo/v0**2) - 1)
nrm = mp.quad(f_shm, [0, 0.01])
QDM = mp.pi/2*max(f_shm(u)/u for u in mp.linspace(1e-6, 3e-3, 3000))
def f_rest(u): return 4/mp.sqrt(mp.pi)*u**2/v0**3*mp.e**(-u**2/v0**2)
QDM0 = mp.pi/2*f_rest(v0/mp.sqrt(2))/(v0/mp.sqrt(2))
rep("WP7D-C6c effective Q_DM = (pi/2) m F_phi,max: SHM (boosted) and rest-frame Maxwellian",
    abs(nrm - 1) < 1e-8 and 0.5e6 < QDM < 3e6, f"SHM {float(QDM):.3g}; rest {float(QDM0):.3g}")

# ---------------------------------------------------------------- C7: occupation per de Broglie volume (D.0)
hbarc_cm = 1.973269804e-5  # eV cm
def NdB(m_eV, vv=v0):
    lam = 2*mp.pi/(m_eV*vv)*hbarc_cm   # cm
    return 0.3e9/m_eV*lam**3
mx = mp.findroot(lambda lm: mp.log(NdB(mp.e**lm)), mp.log(30))
rep("WP7D-C7 N_dB = (rho/m)(2pi/m v0)^3 = 1 at m ~ 30 eV (classical-field regime m << m_x)", 10 < mp.e**mx < 60,
    f"m_x = {float(mp.e**mx):.3g} eV; N_dB(1 eV) = {float(NdB(1)):.2e}")

# ---------------------------------------------------------------- C8: fermionic absorption lepton tensor (F.2)-(F.4)
g0 = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
s = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
def gi(k):
    Mx = sp.zeros(4); Mx[0:2, 2:4] = s[k]; Mx[2:4, 0:2] = -s[k]; return Mx
gam = [g0, gi(0), gi(1), gi(2)]
g5 = I*gam[0]*gam[1]*gam[2]*gam[3]
PR, PL = (sp.eye(4) + g5)/2, (sp.eye(4) - g5)/2
eta = sp.diag(1, -1, -1, -1)
mc, qq, om = symbols('m_chi q omega', positive=True)
def slash(p): return sum(((eta[mu, mu]*p[mu])*gam[mu] for mu in range(4)), sp.zeros(4))
pchi = [mc, 0, 0, 0]
kvec = [qq, 0, 0, -qq]                       # massless nu~ with k = p_chi - q, q along +z, v -> 0  (E_nu = q)
Lt = [[sp.simplify(Q(1, 2)*(slash(kvec)*gam[a]*PR*(slash(pchi) + mc*sp.eye(4))*PL*gam[b]).trace()) for b in range(4)] for a in range(4)]
# target current J^mu = (n, J_x, J_y, J_L) with q.J = omega n  ->  J_L = (omega/q) n ; contract L^{mu nu} J*_mu J_nu
n_, jx, jy = symbols('n J_x J_y')
Jup = [n_, jx, jy, om/qq*n_]
Jlo = [eta[a, a]*Jup[a] for a in range(4)]
con = sp.expand(sum(Lt[a][b]*sp.conjugate(Jlo[a])*Jlo[b] for a in range(4) for b in range(4)))
con_sym = sp.expand(sp.simplify((con + con.subs({jx: sp.conjugate(jx), jy: sp.conjugate(jy)}, simultaneous=True)) / 2))
dens = sp.simplify(con.coeff(n_*sp.conjugate(n_)).subs(om, mc - qq))
rep("WP7D-C8a vector op: density coefficient of L J*J = m_chi (q+omega)^2/q = m_chi^3/q at v=0  (F.4)", is0(dens - mc**3/qq))
trans = sp.simplify(con.coeff(jx*sp.conjugate(jx)))
rep("WP7D-C8b vector op: transverse coefficient = m_chi q  (F.4)", is0(trans - mc*qq))
anti = sp.simplify(con.coeff(sp.conjugate(jx)*jy) - con.coeff(jx*sp.conjugate(jy)))
rep("WP7D-C8c vector op: J_T x J_T antisymmetric (P_R, epsilon) term present, odd under P  (F.4)", anti != 0, f"{anti}")
Ls = sp.simplify(Q(1, 2)*(slash(kvec)*PL*(slash(pchi) + mc*sp.eye(4))*PR).trace())
rep("WP7D-C8d scalar op: L_S = E_nu m_chi = q m_chi  (F.5)", is0(Ls - qq*mc))

# ---------------------------------------------------------------- C9: NC nuclear limit (1905.12635 Eq. (4)) and its leading correction
Mn, Lam, nk, AF2 = symbols('M Lambda n_kappa AF2', positive=True)
q0 = Mn*(sqrt(1 + 2*mc/Mn) - 1)                         # m_chi = q + q^2/2M
Gam = (1/(4*Lam**4))*(mc**2/q0**2)*(4*pi*q0**2/(2*pi)**3)*2*pi*nk*AF2/(1 + q0/Mn)
sigNC = mc**2/(4*pi*Lam**4)
ratio = sp.simplify(Gam/(nk*AF2*sigNC))
rep("WP7D-C9 Gamma = n A^2F^2 sigma_NC (1 - m_chi/M + ...), sigma_NC = m^2/(4 pi Lambda^4)  (F.6)",
    is0(sp.series(ratio.subs(mc, sp.Symbol('e')*Mn), sp.Symbol('e'), 0, 2).removeO() - (1 - sp.Symbol('e'))))

# ---------------------------------------------------------------- C10: electron targets (2011.01940 Eqs. (7), (9), (10), (30))
me, ER, fion2, M2, mu, sig, eta_ = symbols('m_e E_R fion2 M2 mu sigma_e eta', positive=True)
# dictionary from 1509.01598 Eq. (52) vs (D-L0): per-atom S_bar = pi |f_ion|^2/(2 E_R)
lhs = ER*(sig/(4*pi*mu**2))*pi*fion2/(2*ER)            # E_R dGamma/domega integrand / (q dq eta F^2)
rep("WP7D-C10a per-atom S_bar = pi|f_ion|^2/(2E_R) reproduces 1509.01598 Eq. (52) (sigma/8mu^2)", is0(lhs - sig*fion2/(8*mu**2)))
Sbar = pi*fion2/(2*ER)
dGdE_gen = qq*(M2/(4*me**2))*Sbar/(8*pi**2*mc)          # (F.3) density row, frak L = |M|^2/(4 m_e^2), isotropic
rep("WP7D-C10b (F.3) with frak L = |M|^2/4m_e^2 == 2011.01940 Eq. (7)/(30)", is0(dGdE_gen - M2/(64*pi*mc*me**2)*qq/ER*fion2))
dGdE_S = qq**2/(8*pi**2*Lam**4)*Sbar                   # scalar: Gamma = int d^3q/(2pi)^3 S/(4 Lambda^4)
sige = mc**2/(4*pi*Lam**4)
rep("WP7D-C10c scalar operator: URF == 2011.01940 Eq. (10) exactly", is0(dGdE_S - sige*qq**2/(4*ER*mc**2)*fion2))
dGdE_V = mc**2/(8*pi**2*Lam**4)*Sbar
br = 2*me*mc*(2*me + mc) - 2*me**2*qq - qq**2*(2*me + mc)
paperV = sige/(8*me**2*mc**2)*qq/ER*fion2*br
ratV = sp.simplify(paperV/dGdE_V)                      # = q*br/(2 m_e^2 m_chi^2)
ratfree = sp.series(ratV.subs(qq, me*(sqrt(1 + 2*mc/me) - 1)).subs(mc, sp.Symbol('e')*me), sp.Symbol('e'), 0, 2).removeO()
rep("WP7D-C10d vector: 2011.01940 Eq. (9) / URF = 1 + O(m_chi^2/m_e^2) at free kinematics", is0(ratfree - 1))
ratb = sp.expand(sp.series(ratV.subs(qq, mc - om), me, oo, 2).removeO())
rep("WP7D-C10e vector, bound q = m_chi - omega: Eq. (9)/URF = 1 - w^2/m^2 + w(m-w)(2m-w)/(m^2 m_e) + O(m_e^-2)",
    is0(ratb - (1 - om**2/mc**2 + om*(mc - om)*(2*mc - om)/(mc**2*me))), f"{sp.factor(ratb)}")

# ---------------------------------------------------------------- C11: free 2->2 exactness of the kinematics (F.3)
pf = ((mc + me)**2 - me**2)/(2*(mc + me))                # exact CM = lab momentum (initial at rest, massless nu~)
rep("WP7D-C11 relativistic q0 from m+m_e = q + sqrt(q^2+m_e^2) equals the CM momentum (lab = CM)",
    is0(sp.simplify(pf + sqrt(sp.factor(pf**2 + me**2)) - mc - me)))

# ---------------------------------------------------------------- C12: dark Compton (2109.08168 Eq. (2)) from the seagull row (T.3)
xm = symbols('x', positive=True)
# polarisation average: 3 dark-photon pols (isotropic), 2 photon pols: <sum |eps.eps'|^2> = 2/3
ev = [Matrix([1, 0, 0]), Matrix([0, 1, 0]), Matrix([0, 0, 1])]
kh = Matrix([0, 0, 1]); e1, e2 = Matrix([1, 0, 0]), Matrix([0, 1, 0])
avg = sum(((e.T*e1)[0])**2 + ((e.T*e2)[0])**2 for e in ev)/3
rep("WP7D-C12a <sum_lambda' |eps.eps'|^2> = 2/3", is0(avg - Q(2, 3)))
e_ = symbols('e', positive=True)
sigTh = e_**4/(6*pi*me**2)
mv_ = symbols('m_V', positive=True)
wp = me*(sqrt(1 + 2*mv_/me) - 1)                         # omega' + omega'^2/2m_e = m_V
Gam_seag = (e_**2/me)**2*Q(2, 3)/(2*mv_)*(4*pi*wp**2/((2*pi)**3*2*wp))*2*pi/(1 + wp/me)
rURF = sp.simplify(Gam_seag/sigTh)
rpap = (mv_ + 2*me)*(mv_**2 + 2*me*mv_ + 2*me**2)/(mv_ + me)**3/4
sU = sp.series(rURF.subs(mv_, xm*me), xm, 0, 2).removeO(); sP = sp.series(rpap.subs(mv_, xm*me), xm, 0, 2).removeO()
rep("WP7D-C12b NR seagull + free S_nn: kappa^2 sigma_Th (1 - 3x/2 + ...) == Eq. (2) through O(m_V/m_e)",
    is0(sU - sP) and is0(sU - (1 - Q(3, 2)*xm)), f"URF {sU}, paper {sP}")
rep("WP7D-C12c sigma_Th = e^4/(6 pi m_e^2) = 8 pi alpha^2/(3 m_e^2) (HL)", is0(sigTh.subs(e_, sqrt(4*pi*sp.Symbol('alpha'))) - 8*pi*sp.Symbol('alpha')**2/(3*me**2)))

# ---------------------------------------------------------------- C13: pair-absorption phase-space normalisation (2507.14287 Eq. (8))
bc = 7.8e-4
def fnorm(xi):   # int d^3p/(2pi)^3 g f  in units of rho/m, cut at p = 2.5 m beta_c
    return xi/(2*bc**3)*mp.quad(lambda u: 4*mp.pi*u**2*mp.e**(-u**2/bc**2), [0, 2.5*bc])/(2*mp.pi)**3
xi_half = mp.findroot(lambda xi: fnorm(xi) - 0.5, 40)
rep("WP7D-C13 2507.14287 Eq. (8) with xi = 44.8 normalises each of chi, chi-bar to rho/(2m)  (T.1)",
    abs(xi_half - 44.8) < 0.1, f"xi(rho/2m) = {float(xi_half):.4g}")

# ---------------------------------------------------------------- C14: stopping power from the master formula (S.1)-(S.2)
Z, vN, al_ = symbols('Z v_N alpha', positive=True)
k, wq, Lf = symbols('k omega_k L_f', positive=True)
# dE/dx = (1/v)int d^3k/(2pi)^3 omega |Z e^2/k^2|^2 (2k^2/e^2) L ;  d^3k = 2pi k^2 dk dmu, omega = k v mu
pref = sp.simplify((1/vN)*(Z*e_**2)**2*2/e_**2*(2*pi)/(2*pi)**3/(vN))   # coefficient of int dk/k int_0^{kv} domega omega L
rep("WP7D-C14a Lindhard dielectric stopping prefactor = 2 Z^2 alpha/(pi v^2) (WP5-v3 1.1(e))", is0(pref.subs(e_, sqrt(4*pi*al_)) - 2*Z**2*al_/(pi*vN**2)))
wpe, ne_, Iex = symbols('omega_pe n_e I', positive=True)
bethe = pref*(pi/2)*wpe**2*sp.log(2*me*vN**2/Iex)
rep("WP7D-C14b f-sum (9.5) -> Bethe: 4 pi Z^2 alpha^2 n_e/(m_e v^2) ln(2 m_e v^2/I)",
    is0(sp.simplify(bethe.subs(wpe, sqrt(e_**2*ne_/me)).subs(e_, sqrt(4*pi*al_)) - 4*pi*Z**2*al_**2*ne_/(me*vN**2)*sp.log(2*me*vN**2/Iex))))

# ---------------------------------------------------------------- C15: modulus scaling (D.8): a ~ 1/(alpha m_e), hydrogenic check
r_, me_, a_ = symbols('r m_e alpha', positive=True)
psi = exp(-r_*a_*me_)                                     # trial 1s, exact for H = p^2/2m - alpha/r
E1 = sp.simplify(sp.integrate(psi*(-(1/(2*me_))*(sp.diff(r_**2*sp.diff(psi, r_), r_)/r_**2) - a_/r_*psi)*r_**2, (r_, 0, oo))/sp.integrate(psi**2*r_**2, (r_, 0, oo)))
rep("WP7D-C15 hydrogenic: E = -alpha^2 m_e/2, length 1/(alpha m_e) => h = -dln alpha - dln m_e (1508.01798 Eq. (7))", is0(E1 + a_**2*me_/2))

print(f"\n{sum(RES)}/{len(RES)} PASS")
