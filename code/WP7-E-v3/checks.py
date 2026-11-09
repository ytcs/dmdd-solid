"""WP7-E-v3 (R12 fix round) checks: time-resolved energy and charge balance (corrected after R11 REF-WP7-E-A/B and R12 VER-WP7-E-A/B).
v3: multiplicative collection (C7, C9), 95% C.L. bounds (C8), exciton reservoir and (W14) (C13), theta_tr^pr tilt (C14),
bias work before t_pr (C15), ZPE telescoping (C16), exciton field ionisation (C17).
Sympy/mpmath only; exact where possible, evalf for [E] numbers. No simulation.  Run: python3 -I checks.py
Labels Ev3-Cn. Replaces v1's identity checks (C2a, C2c, C7b, C9c, C5b) by checks that can fail:
independent routes to the same quantity (field energy vs Green's-function pair sum, battery work vs field energy + dissipation,
order statistics vs Ramo current, exact mixture variance vs formula, exact calibration algebra vs its series)."""
import sympy as sp
import mpmath as mp
from sympy import Rational as Q, sqrt, pi, exp, log, symbols, simplify, integrate, oo

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:92s} {note}")

# ======================================================================= C1 reference level: mu_F, singly trapped carrier
Ec, Ev, mu, ee, eh, muF = symbols('E_c E_v mu epsilon_e epsilon_h mu_F', real=True)
Nef, Nhf, Net, Nht = symbols('N_ef N_hf N_et N_ht', nonnegative=True)
Eq = Nef*(Ec - mu) + Nhf*(mu - Ev) + Net*(Ec - ee - mu) + Nht*(mu - Ev - eh)
rep("Ev3-C1a d(E_pairs+E_trap)/dmu = N_h,tot - N_e,tot", simplify(sp.diff(Eq, mu) - (Nhf + Nht - Nef - Net)) == 0)
rep("Ev3-C1b neutral crystal: mu-independent", simplify(sp.diff(Eq.subs(Nhf, Nef + Net - Nht), mu)) == 0)
# one pair, electron collected at a contact with Fermi level mu_F (releases E_c - mu_F as contact heat), hole trapped:
heat_contact_e = Ec - muF
stored_single_h = (Ec - Ev) - heat_contact_e - eh        # E_g minus contact heat minus capture heat eps_h
rep("Ev3-C1c singly trapped hole stores mu_F - E_v - eps_h (contact-dependent, not E_g - eps_e - eps_h)",
    simplify(stored_single_h - (muF - Ev - eh)) == 0)
rep("Ev3-C1d it is mu_F-dependent (so 'any mu' is wrong once one carrier is collected)", sp.diff(stored_single_h, muF) != 0)

# ======================================================================= C2 electrostatics, 1D planar, sheet charges (eps = area = 1)
# Electrodes at z=0 (phi=0) and z=d (phi=V). Sheets sigma_i at z_i. Solve Gauss exactly, compare independent energy routes.
d, V = symbols('d V', positive=True)
def field_solution(sig, zs):
    E0 = symbols('E0')
    # E(z) = E0 + sum_{z_i<z} sigma_i ; phi(d) = -int_0^d E dz = V
    pts = list(zip(zs, sig))          # caller passes positions in increasing order
    edges = [0] + [p[0] for p in pts] + [d]
    Es = [E0]; acc = E0
    for z_, s_ in pts:
        acc = acc + s_; Es.append(acc)
    phi_d = -sum(Es[k]*(edges[k+1] - edges[k]) for k in range(len(Es)))
    E0s = sp.solve(sp.Eq(phi_d, V), E0)[0]
    Es = [sp.simplify(e.subs(E0, E0s)) for e in Es]
    U = sum(Es[k]**2*(edges[k+1] - edges[k]) for k in range(len(Es)))/2
    Qtop = -Es[-1]                     # charge on the z=d electrode (outward normal -z): Q = -E(d^-)
    return Es, U, Qtop, edges
z1, z2, s1, s2 = symbols('z_1 z_2 sigma_1 sigma_2', real=True)
Es, U, Qtop, edges = field_solution([s1, s2], [Q(1, 3)*d, Q(3, 4)*d])
# Green's function of the grounded planar capacitor: G(z,z') = z_<(d - z_>)/d ; pair energy + bias coupling + vacuum capacitor
def G(za, zb): return sp.Min(za, zb)*(d - sp.Max(za, zb))/d
sub = {z1: Q(1, 3)*d, z2: Q(3, 4)*d}
U_green = (Q(1, 2)*(s1**2*G(z1, z1) + s2**2*G(z2, z2)) + s1*s2*G(z1, z2)).subs(sub)
U_bias = (V**2/(2*d))
U_field = U
# energy of a charge system at fixed electrode potentials: U_field = U_green + U_bias (cross terms vanish in field energy? no):
# field energy includes cross term sigma*V*z/d? check that U_field - U_bias - U_green is the image-free cross term = 0 by superposition
cross = sp.simplify(U_field - U_bias - U_green)
rep("Ev3-C2a field energy = Green's-function pair energy (incl. self-image) + V^2/2d (space-charge reservoir E_es complete)",
    sp.simplify(cross) == 0, f"residual = {cross}")
# Battery work for a quasi-static move of sheet 1: W_batt = V * dQ_top ; dissipated heat = int (force) dz ; check W = dU + heat
zz = symbols('zeta', positive=True)
Es_m, U_m, Qtop_m, _ = field_solution([s1, s2], [zz, Q(3, 4)*d])
# force on sheet 1 at zz (zz < 3d/4): sigma_1 * (E_left + E_right)/2 ; E_left = Es_m[0], E_right = Es_m[1]
force = s1*(Es_m[0] + Es_m[1])/2
a_, b_ = Q(1, 5)*d, Q(1, 2)*d
heat = integrate(force, (zz, a_, b_))
dU = U_m.subs(zz, b_) - U_m.subs(zz, a_)
Wb = V*(Qtop_m.subs(zz, b_) - Qtop_m.subs(zz, a_))
rep("Ev3-C2b energy theorem with space charge: V*dQ_electrode = dU_es + dissipated (NTL) heat", sp.simplify(Wb - dU - heat) == 0)
ramo = -s1*(b_ - a_)/d                                       # Ramo: induced charge change on top electrode, independent of sheet 2
rep("Ev3-C2c Ramo exact with space charge: dQ_electrode = -sigma (dz/d) (so W_bias = eV_b N^meas holds for the work)",
    sp.simplify((Qtop_m.subs(zz, b_) - Qtop_m.subs(zz, a_)) - ramo) == 0)
rep("Ev3-C2d but NTL heat = W_bias - dE_es != W_bias when another charge is present (space-charge correction)",
    sp.simplify(heat - Wb) != 0 and sp.simplify((heat - Wb).subs(s2, 0) + dU.subs(s2, 0)) == 0)
# image energy of a single trapped sheet (stored, z-dependent):
zp, sg = symbols('z_p sigma', positive=True)
Uimg = sg**2*zp*(d - zp)/(2*d)
rep("Ev3-C2e trapped single charge carries image energy sigma^2 z'(d-z')/2d (reservoir E_es, vanishes at contacts)",
    sp.simplify(Uimg.subs(zp, 0)) == 0 and sp.simplify(Uimg.subs(zp, d)) == 0)

# ======================================================================= C3 release kernels
t, G_, Gmin, Gmax, w, Dd, dd, rc = symbols('t Gamma Gamma_min Gamma_max w D_diff d r_c', positive=True)
rep("Ev3-C3a broad-lambda rate (e^{-Gmin t}-e^{-Gmax t})/(t ln(Gmax/Gmin)) from dN/dGamma = 1/(Gamma ln)",
    simplify(sp.expand(integrate(exp(-G_*t), (G_, Gmin, Gmax))/log(Gmax/Gmin) - (exp(-Gmin*t) - exp(-Gmax*t))/(t*log(Gmax/Gmin)))) == 0)
mp.mp.dps = 30
gmin, gmax = mp.mpf('1e-9'), mp.mpf('1e3')
Rn = lambda tt: (mp.e**(-gmin*tt) - mp.e**(-gmax*tt))/(tt*mp.log(gmax/gmin))
tot = mp.quad(Rn, [0, 1e-3, 1, 1e3, 1e6, 1e9, mp.inf])
rep("Ev3-C3b broad-lambda kernel normalised", abs(tot - 1) < 1e-10, f"{mp.nstr(tot, 12)}")
F1 = sp.erfc(dd/sqrt(4*Dd*w))
f1 = dd/sqrt(4*pi*Dd*w**3)*exp(-dd**2/(4*Dd*w))
rep("Ev3-C3c 1D (crowdion) first passage: P_rel = erfc(d/sqrt(4Dt)) -> 1",
    simplify(sp.diff(F1, w) - f1) == 0 and sp.limit(F1, w, oo) == 1)
F3 = (rc/dd)*sp.erfc((dd - rc)/sqrt(4*Dd*w))
# Smoluchowski: survival-density solution; flux into sphere r_c from point source at d gives this; check PDE route:
r, tt = symbols('r t', positive=True)
# density for absorbing sphere, point source at d (radially averaged Green's function, method of images in u = r p):
p = (1/(4*pi*r*dd*sqrt(4*pi*Dd*tt)))*(exp(-(r - dd)**2/(4*Dd*tt)) - exp(-(r + dd - 2*rc)**2/(4*Dd*tt)))
pde = simplify(sp.diff(p, tt) - Dd*(sp.diff(r**2*sp.diff(p, r), r))/r**2)
flux = simplify(4*pi*rc**2*Dd*sp.diff(p, r).subs(r, rc))
rep("Ev3-C3d 3D image solution solves diffusion and vanishes at r_c", pde == 0 and simplify(p.subs(r, rc)) == 0)
rep("Ev3-C3e 3D: capture flux = dP_rel/dt with P_rel = (r_c/d) erfc((d-r_c)/sqrt(4Dt)) -> r_c/d < 1",
    simplify(flux - sp.diff(F3, w).subs(w, tt)) == 0 and simplify(sp.limit(F3, w, oo) - rc/dd) == 0)

# ======================================================================= C4 Hecht by two independent routes
lam, L, x, v, dz = symbols('ell L x v d', positive=True)
route1 = (integrate(x*exp(-x/lam)/lam, (x, 0, L)) + L*exp(-L/lam))/dz          # E[min(X,L)]/d
route2 = integrate((v/dz)*exp(-v*t/lam), (t, 0, L/v))                         # Ramo current x survival, integrated over transit
rep("Ev3-C4a Hecht: order-statistics route = Ramo-current route = (ell/d)(1 - e^{-L/ell})",
    simplify(route1 - route2) == 0 and simplify(route1 - lam/dz*(1 - exp(-L/lam))) == 0)

# ======================================================================= C5 coax Ramo
a, b, r0, r1, Vb, qc, rr = symbols('a b r_0 r_1 V_b q r', positive=True)
work = integrate(qc*Vb/(rr*log(b/a)), (rr, r0, r1))
rep("Ev3-C5 coax: bias work = V_b q [U_R(r1) - U_R(r0)]", simplify(work - Vb*qc*(log(r1/a) - log(r0/a))/log(b/a)) == 0)

# ======================================================================= C6 F_meas with position mixture (exact two-position example)
# N ~ any law with mean n, var F n; at position k (prob pk) xi has mean m_k, var s_k. Compute exact Var of mixture.
n, Fe, p1 = symbols('n F_eh p_1', positive=True)
m1, m2, v1, v2 = symbols('m_1 m_2 v_1 v_2', positive=True)
p2 = 1 - p1
EX_k = [n*m1, n*m2]; VX_k = [n*v1 + m1**2*Fe*n, n*v2 + m2**2*Fe*n]
EX = p1*EX_k[0] + p2*EX_k[1]
EX2 = p1*(VX_k[0] + EX_k[0]**2) + p2*(VX_k[1] + EX_k[1]**2)
Fobs_exact = sp.simplify((EX2 - EX**2)/EX)
mbar = p1*m1 + p2*m2
var_m = p1*m1**2 + p2*m2**2 - mbar**2
Fsquare = (p1*m1**2 + p2*m2**2)                # <m^2> enters the F_eh term
formula = (Fe*Fsquare + p1*v1 + p2*v2)/mbar + n*var_m/mbar
rep("Ev3-C6a F_meas^obs = (F_eh<m^2> + <Var xi|r>)/<xi> + <N> Var_r<xi|r>/<xi> (exact mixture)", sp.simplify(Fobs_exact - formula) == 0)
rep("Ev3-C6b the position term grows with N (non-Fano scaling)", sp.diff(formula, n) != 0)
ep = symbols('epsilon', positive=True)
rep("Ev3-C6c Bernoulli, single position: F_meas = eps F_eh + 1 - eps (= WP5v3-C2a)",
    sp.simplify(formula.subs({m1: ep, m2: ep, v1: ep*(1 - ep), v2: ep*(1 - ep)}) - (ep*Fe + 1 - ep)) == 0)

# ======================================================================= C7 two-channel reconstruction, MULTIPLICATIVE collection (1803.02903 Eq. (1))
om, g, yv, r_, dl = symbols('omega g y r delta', positive=True)
dN, dE = symbols('dp_NR dp_ER', positive=True)          # pre-sensor fractional deficits D'/omega (small)
eps_p = symbols('epsilon_p', positive=True)             # ER primary-phonon collection efficiency (O(0.1-0.3), NOT small loss)
# signals: S = eps_prim*(omega - D') + eps_NTL*(NTL heat); eps_prim^NR = eps_p(1 - delta), delta = Delta eps/eps >= 0 ; eps_NTL = r eps_p
S_ER = eps_p*(1 - dE)*om + r_*eps_p*g*om
S_NR = eps_p*(1 - dl)*(1 - dN)*om + r_*eps_p*g*yv*om
k = om*(1 + g)/S_ER                                      # ER calibration of the phonon scale
Erec = k*S_NR - g*yv*om                                  # E_R^rec = E_phi - E_Q eV_b/eps (charge scale calibrated on ER)
eta = sp.simplify(Erec/om)
rep("Ev3-C7a eta is independent of the absolute collection eps_p (multiplicative: the 70-90% sensor loss cancels)", sp.diff(eta, eps_p) == 0)
eta0 = sp.simplify(eta.subs({dl: 0, dN: 0, dE: 0}))
rep("Ev3-C7b zero deficit: eta_0 = 1 + g(1-r)(1-y)/(1+rg) (NTL/primary collection ratio r alone shifts eta)",
    sp.simplify(eta0 - (1 + g*(1 - r_)*(1 - yv)/(1 + r_*g))) == 0)
h = sp.Symbol('h')
ser = sp.series(eta.subs({r_: 1, dl: h*dl, dN: h*dN, dE: h*dE}), h, 0, 2).removeO().subs(h, 1)
kap = (1 + yv*g)/(1 + g)
rep("Ev3-C7c r = 1: eta = 1 - delta - d'_NR + kappa d'_ER + O(d'^2, delta^2, delta d')", sp.simplify(ser - (1 - dl - dN + kap*dE)) == 0)
Est, XN, XE = symbols('E_st X_NR X_ER', nonnegative=True)  # D'_NR = E_st + X_NR, D'_ER = X_ER (ER has no E_st)
comb = ((Est + XN) - kap*XE)/om
rep("Ev3-C7d d'_NR - kappa d'_ER = [E_st + (X_NR - X_ER) + (1-kappa) X_ER]/omega (the (1-kappa)D'_ER term)",
    sp.simplify(comb - (Est + (XN - XE) + (1 - kap)*XE)/om) == 0)
rr = sp.nsolve(1 + 1.047*(1 - sp.Symbol('rr'))*(0.7)/(1 + sp.Symbol('rr')*1.047) - 0.952, sp.Symbol('rr'), 1.1)
rep("Ev3-C7e degeneracy: r = 1.14 alone reproduces eta = 0.952 (g = 1.047, y = 0.3) [E]", abs(float(rr) - 1.144) < 0.01, f"r = {float(rr):.3f}")
kapn = (1 + 0.3*1.047)/(1 + 1.047)
rep("Ev3-C7f kappa = 0.642 (g = 4/3.82, y = 0.3) [E]", abs(kapn - 0.642) < 1e-3, f"kappa = {kapn:.3f}")

e_ = symbols('e', positive=True)
eta_e = sp.simplify(eta.subs({dl: 0, dE: 0, dN: e_}))
rep("Ev3-C7g with only E_st (delta = X = 0): 1 - eta - e = g(r-1)(1-y-e)/(1+rg)  => bound E_st/omega <= 1-eta needs r >= 1 AND e <= 1-y",
    sp.simplify(1 - eta_e - e_ - g*(r_ - 1)*(1 - yv - e_)/(1 + r_*g)) == 0)
e0h = [float(eta0.subs({g: Q(4000, 3820), r_: Q(1144, 1000), yv: yy})) for yy in (Q(22, 100), Q(35, 100))]
rep("Ev3-C7h r = 1.144: eta_0 = 0.947 (y = 0.22) .. 0.955 (y = 0.35), inside the 95% band [0.945, 0.961]: degenerate with E_st",
    0.945 < e0h[0] < 0.948 and 0.954 < e0h[1] < 0.957 and all(0.945 <= v <= 0.961 for v in e0h), f"{e0h[0]:.4f} .. {e0h[1]:.4f}")

# ======================================================================= C8 NRT / data inversion
psurv, Edam, ER, Est1, Ed = symbols('p_surv E_dam E_R E_st1 E_d', positive=True)
fDF = psurv*Q(4, 10)*(Edam/ER)*Est1/Ed
rep("Ev3-C8a NRT f_DF decreasing in E_d at fixed E_st,1", sp.diff(fDF, Ed).is_negative)
X_si = 0.055/(0.4*0.65); X_ge = (0.0608 + 2*0.0018)/(0.4*0.8)    # 95% C.L. deficits; E_dam/E_R = 0.65 (Si), 0.8 (Pb in Ge) [E]
rep("Ev3-C8b 95% C.L. bounds p_surv E_st,1/E_d: Si <= 0.21, Ge <= 0.20 (given Delta eps >= 0, r >= 1, X_NR >= kappa X_ER) [E]",
    abs(X_si - 0.21) < 0.01 and abs(X_ge - 0.20) < 0.01, f"Si {X_si:.3f}, Ge {X_ge:.3f}")
rep("Ev3-C8c implied p_surv <= 0.47 (Si: 9/20), <= 0.66 (Ge: 6/19.7) [E]", abs(X_si/(9/20) - 0.47) < 0.01 and abs(X_ge/(6/19.7) - 0.66) < 0.01,
    f"{X_si/(9/20):.2f}, {X_ge/(6/19.7):.2f}")

zs = 0.99
rep("Ev3-C8d DeltaZPE <= 1% of E_st widens bounds <= 1%: 0.056 (Si), 0.065 (Ge); 0.21/0.20; p_surv <= 0.48/0.67 [E]",
    abs(0.055/zs - 0.056) < 6e-4 and abs(0.0644/zs - 0.065) < 6e-4 and abs(X_si/zs - 0.21) < 6e-3 and abs(X_ge/zs - 0.20) < 6e-3
    and abs(X_si/zs/(9/20) - 0.48) < 6e-3 and abs(X_ge/zs/(6/19.7) - 0.67) < 6e-3,
    f"{0.055/zs:.4f}, {0.0644/zs:.4f}, {X_si/zs:.3f}, {X_ge/zs:.3f}, {X_si/zs/(9/20):.3f}, {X_ge/zs/(6/19.7):.3f}")

# ======================================================================= C9 windowed Y_H, multiplicative collection; Delta E_trap sign; NTL normalisation
YH = (1 - dl)*(1 - dN)/(1 - dE)
serY = sp.series(YH.subs({dl: h*dl, dN: h*dN, dE: h*dE}), h, 0, 2).removeO().subs(h, 1)
rep("Ev3-C9a zero field: Y_H = (1-delta)(1-d'_NR)/(1-d'_ER) = 1 - delta - (d'_NR - d'_ER) + O(2) (eps_p cancels)",
    sp.simplify(serY - (1 - dl - dN + dE)) == 0)
phi_t, E1t, yq = symbols('phi E_1 y_q', positive=True)
rep("Ev3-C9b Delta E_trap < 0 at equal trapped fraction (y < 1)", sp.simplify(phi_t*E1t*(yq - 1)*om/3.8).subs(yq, Q(3, 10)) < 0)
YN = sp.simplify(S_NR/S_ER)
rep("Ev3-C9c NTL ratio at zero deficit, r = 1: (1 + y g)/(1 + g)", sp.simplify(YN.subs({dl: 0, dN: 0, dE: 0, r_: 1}) - (1 + yv*g)/(1 + g)) == 0)

# ======================================================================= C10 mK emission numbers (hbar c corrected)
mstar, E0, eF = symbols('m_star varepsilon_0 eF', positive=True)
SFN = 2*integrate(sqrt(2*mstar*(E0 - eF*x)), (x, 0, E0/eF))
rep("Ev3-C10a triangular-barrier WKB exponent = (4/3) sqrt(2m*) eps^{3/2}/(eF)", simplify(SFN - Q(4, 3)*sqrt(2*mstar)*E0**Q(3, 2)/eF) == 0)
hbarc_eVcm = 1.97327e-5            # eV cm (corrected; v1 used 1.97e-7)
me = 510998.95
Fneed = 4/3*mp.sqrt(2*0.3*me)*0.045**1.5/(30*hbarc_eVcm)
rep("Ev3-C10b field for exponent 30 (45 meV, m* = 0.3 m_e): 1.2e4 V/cm", 1.1e4 < Fneed < 1.3e4, f"{mp.nstr(Fneed,3)} V/cm")
e_SI, eps0 = 1.602176634e-19, 8.8541878128e-12
dPF = mp.sqrt(e_SI*1e4/(mp.pi*11.7*eps0))       # V, at 100 V/cm = 1e4 V/m, Si
rep("Ev3-C10c Poole-Frenkel lowering at 100 V/cm in Si ~ 2 meV << 45 meV", 1.5e-3 < dPF < 3e-3, f"{mp.nstr(dPF*1e3,3)} meV")
rep("Ev3-C10d thermal exponent eps/T at 50 mK, 45 meV > 1e4", 0.045/(8.617333e-5*0.05) > 1e4)

# ======================================================================= C11 visibility threshold (one criterion) and pockets
sigE = 3.86; Ethr = 4.2*sigE                     # 2007.14289 sigma [FT]; 4.2 sigma trigger [E, R11 referee reading]
ecoll, Est1v = 0.3, 9.0
rep("Ev3-C11a single Frenkel-pair release visible iff E_thr <= eps_coll E_st,1 = 2.7 eV; CPD E_thr ~ 16 eV: invisible",
    ecoll*Est1v < Ethr, f"{ecoll*Est1v:.1f} eV vs {Ethr:.1f} eV")
Na_min = Ethr/ecoll/0.2
rep("Ev3-C11b pocket recrystallisation visible for N_a >~ E_thr/(eps_coll*0.2 eV) ~ 270 atoms [E]", 200 < Na_min < 400, f"N_a >= {Na_min:.0f}")

# ======================================================================= C12 STM: per-unit-lambda vs total; power
Pbar, Vf, T1 = 1.6e19, 1e-5, 8.617333e-5
per_lam = (mp.pi**2/12)*Pbar*Vf*T1**2
Qdot = lambda s: per_lam/(2*s)*(mp.e**(-float(gmin)*s) - mp.e**(-float(gmax)*s))
rel = mp.quad(Qdot, [0, 1e-3, 1, 1e3, 1e6, 1e9, mp.inf])
dlam = mp.log(gmax/gmin)/2
rep("Ev3-C12a released total = per-unit-lambda excess x Delta lambda, Delta lambda = ln(Gmax/Gmin)/2", abs(rel/(per_lam*dlam) - 1) < 1e-8,
    f"{mp.nstr(rel,3)} eV, dlam = {mp.nstr(dlam,3)}")
rep("Ev3-C12b power at 10 d ~ 0.6 eV/s; quanta <~ 3 T1 ~ 3e-4 eV: >= 1e4 quanta per 10 eV event", 0.3 < Qdot(864000.0) < 1 and 10/(3*T1) > 1e4,
    f"{mp.nstr(Qdot(864000.0),3)} eV/s")

# ======================================================================= C13 exciton reservoir and (W14) with prompt capture
Nef, Nhf, Net, Nht, NX = symbols('N_ef N_hf N_et N_ht N_X', nonnegative=True)
Exb, et_e, et_h, Hh, Est2, Eesc2, Ees, Wb = symbols('E_xb eps_e eps_h H E_st E_esc E_es W', real=True)
Eg = Ec - Ev
lhs_res = Nef*(Ec - muF) + Nhf*(muF - Ev) + NX*(Eg - Exb) + Net*(Ec - et_e - muF) + Nht*(muF - Ev - et_h) + Ees + Hh + Est2 + Eesc2
omega_ = lhs_res - Wb                                  # (E1) at t_pr: omega + W = reservoirs
neutral = {Nhf: Nef + Net - Nht}                       # excitons neutral
Neh = Nef + NX                                          # band electrons, bound or not
Etrap = Net*(Ec - et_e - muF) + Nht*(muF - Ev - et_h)
Eunp = (Nhf - Nef)*(muF - Ev)
Ex = -NX*Exb
rhs = Hh + Etrap + Ees + Eunp + Ex - Wb
rep("Ev3-C13a (W14) substitution: omega - N_eh E_g - E_st - E_esc = H + E_trap^pr + E_es + E_pairs^unp + E_x - W (E_x = -N_X E_x^b <= 0)",
    sp.simplify((omega_ - Neh*Eg - Est2 - Eesc2 - rhs).subs(neutral)) == 0)
rep("Ev3-C13b E_pairs^unp + E_trap^pr is mu_F-independent under neutrality", sp.simplify(sp.diff((Eunp + Etrap).subs(neutral), muF)) == 0)
rep("Ev3-C13c exciton formation deposit: (N_ef,N_hf,N_X) -= (1,1,-1), H += E_x^b conserves (E1)",
    sp.simplify((Ec - muF) + (muF - Ev) - (Eg - Exb) - Exb) == 0)

# ======================================================================= C14 theta_tr^pr tilt on the two-point measure
f0, psi, th = symbols('f_0 psi theta', positive=True)
ftilt = f0*exp(th*psi)/(f0*exp(th*psi) + 1 - f0)
psi_v = sp.log(Q(1, 100)*(1 - Q(1, 1000))/(Q(1, 1000)*Q(99, 100)))
rep("Ev3-C14a f_0 = 1e-3, psi = ln(10.09) gives 1% at theta = 1", abs(float(ftilt.subs({f0: Q(1, 1000), psi: psi_v, th: 1})) - 0.01) < 1e-12,
    f"psi = {float(psi_v):.3f}")
rep("Ev3-C14b f_0 = 0 cannot move under tilting (v2 prior defect)", sp.simplify(ftilt.subs(f0, 0)) == 0)

# ======================================================================= C15 bias work before t_pr
w_lo = 4.0*1e6*1e-10; w_hi = 250.0*1e7*1e-10       # eV per carrier: e*E[V/cm]*v[cm/s]*t_pr[s]
rep("Ev3-C15 bias work before t_pr = e E v_d t_pr: 4e-4 eV (4 V/cm) to 0.25 eV (250 V/cm, saturated) per carrier [E]",
    abs(w_lo - 4e-4) < 1e-9 and abs(w_hi - 0.25) < 1e-9, f"{w_lo:.0e} .. {w_hi:.2f} eV")

# ======================================================================= C16 ZPE correction telescopes on a master equation (same structure as T-1)
Gm = sp.Matrix([[0, 3, 1, 0], [0, 0, 2, Q(1, 2)], [0, 1, 0, 4], [0, 0, 0, 0]])  # Gamma_ij, i -> j ; state 3 absorbing
zpe = sp.Matrix([Q(1, 10), Q(3, 20), Q(1, 20), 0])
Mgen = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        if i != j:
            Mgen[j, i] += Gm[i, j]; Mgen[i, i] -= Gm[i, j]
N0 = sp.Matrix([1, 0, 0, 0])
tt_ = sp.Symbol('t', positive=True)
Nt = (Mgen*tt_).exp()*N0
flux = sum(Nt[i]*Gm[i, j]*(zpe[i] - zpe[j]) for i in range(4) for j in range(4) if i != j)
T_end = 2
lhs_z = sp.N(sp.Integral(flux, (tt_, 0, T_end)).evalf(30), 25)
rhs_z = sp.N(zpe[0] - sum(Nt[i].subs(tt_, T_end)*zpe[i] for i in range(4)), 25)
rep("Ev3-C16 released ZPE correction int sum N_i Gamma_ij (Z_i - Z_j) = Z_c - sum N_i(t) Z_i (telescopes, as T-1 for E^conf)",
    abs(lhs_z - rhs_z) < 1e-15, f"{float(lhs_z):.6f} vs {float(rhs_z):.6f}")

# ======================================================================= C17 exciton field ionisation scale
Fion = 0.015/4e-7
rep("Ev3-C17 exciton field-ionisation scale E_x^b/(e a_X) ~ 4e4 V/cm >> detector fields (formation limited by drift separation instead)",
    Fion > 1e4, f"{Fion:.2e} V/cm")

print(f"\n{sum(RES)}/{len(RES)} PASS")
