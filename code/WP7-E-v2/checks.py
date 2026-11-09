"""WP7-E-v2 (R12) checks: time-resolved energy and charge balance (corrected after R11 REF-WP7-E-A/B).
Sympy/mpmath only; exact where possible, evalf for [E] numbers. No simulation.  Run: python3 -I checks.py
Labels WP7Ev2-Cn. Replaces v1's identity checks (C2a, C2c, C7b, C9c, C5b) by checks that can fail:
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
rep("Ev2-C1a d(E_pairs+E_trap)/dmu = N_h,tot - N_e,tot", simplify(sp.diff(Eq, mu) - (Nhf + Nht - Nef - Net)) == 0)
rep("Ev2-C1b neutral crystal: mu-independent", simplify(sp.diff(Eq.subs(Nhf, Nef + Net - Nht), mu)) == 0)
# one pair, electron collected at a contact with Fermi level mu_F (releases E_c - mu_F as contact heat), hole trapped:
heat_contact_e = Ec - muF
stored_single_h = (Ec - Ev) - heat_contact_e - eh        # E_g minus contact heat minus capture heat eps_h
rep("Ev2-C1c singly trapped hole stores mu_F - E_v - eps_h (contact-dependent, not E_g - eps_e - eps_h)",
    simplify(stored_single_h - (muF - Ev - eh)) == 0)
rep("Ev2-C1d it is mu_F-dependent (so 'any mu' is wrong once one carrier is collected)", sp.diff(stored_single_h, muF) != 0)

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
rep("Ev2-C2a field energy = Green's-function pair energy (incl. self-image) + V^2/2d (space-charge reservoir E_es complete)",
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
rep("Ev2-C2b energy theorem with space charge: V*dQ_electrode = dU_es + dissipated (NTL) heat", sp.simplify(Wb - dU - heat) == 0)
ramo = -s1*(b_ - a_)/d                                       # Ramo: induced charge change on top electrode, independent of sheet 2
rep("Ev2-C2c Ramo exact with space charge: dQ_electrode = -sigma (dz/d) (so W_bias = eV_b N^meas holds for the work)",
    sp.simplify((Qtop_m.subs(zz, b_) - Qtop_m.subs(zz, a_)) - ramo) == 0)
rep("Ev2-C2d but NTL heat = W_bias - dE_es != W_bias when another charge is present (space-charge correction)",
    sp.simplify(heat - Wb) != 0 and sp.simplify((heat - Wb).subs(s2, 0) + dU.subs(s2, 0)) == 0)
# image energy of a single trapped sheet (stored, z-dependent):
zp, sg = symbols('z_p sigma', positive=True)
Uimg = sg**2*zp*(d - zp)/(2*d)
rep("Ev2-C2e trapped single charge carries image energy sigma^2 z'(d-z')/2d (reservoir E_es, vanishes at contacts)",
    sp.simplify(Uimg.subs(zp, 0)) == 0 and sp.simplify(Uimg.subs(zp, d)) == 0)

# ======================================================================= C3 release kernels
t, G_, Gmin, Gmax, w, Dd, dd, rc = symbols('t Gamma Gamma_min Gamma_max w D_diff d r_c', positive=True)
rep("Ev2-C3a broad-lambda rate (e^{-Gmin t}-e^{-Gmax t})/(t ln(Gmax/Gmin)) from dN/dGamma = 1/(Gamma ln)",
    simplify(sp.expand(integrate(exp(-G_*t), (G_, Gmin, Gmax))/log(Gmax/Gmin) - (exp(-Gmin*t) - exp(-Gmax*t))/(t*log(Gmax/Gmin)))) == 0)
mp.mp.dps = 30
gmin, gmax = mp.mpf('1e-9'), mp.mpf('1e3')
Rn = lambda tt: (mp.e**(-gmin*tt) - mp.e**(-gmax*tt))/(tt*mp.log(gmax/gmin))
tot = mp.quad(Rn, [0, 1e-3, 1, 1e3, 1e6, 1e9, mp.inf])
rep("Ev2-C3b broad-lambda kernel normalised", abs(tot - 1) < 1e-10, f"{mp.nstr(tot, 12)}")
F1 = sp.erfc(dd/sqrt(4*Dd*w))
f1 = dd/sqrt(4*pi*Dd*w**3)*exp(-dd**2/(4*Dd*w))
rep("Ev2-C3c 1D (crowdion) first passage: P_rel = erfc(d/sqrt(4Dt)) -> 1",
    simplify(sp.diff(F1, w) - f1) == 0 and sp.limit(F1, w, oo) == 1)
F3 = (rc/dd)*sp.erfc((dd - rc)/sqrt(4*Dd*w))
# Smoluchowski: survival-density solution; flux into sphere r_c from point source at d gives this; check PDE route:
r, tt = symbols('r t', positive=True)
# density for absorbing sphere, point source at d (radially averaged Green's function, method of images in u = r p):
p = (1/(4*pi*r*dd*sqrt(4*pi*Dd*tt)))*(exp(-(r - dd)**2/(4*Dd*tt)) - exp(-(r + dd - 2*rc)**2/(4*Dd*tt)))
pde = simplify(sp.diff(p, tt) - Dd*(sp.diff(r**2*sp.diff(p, r), r))/r**2)
flux = simplify(4*pi*rc**2*Dd*sp.diff(p, r).subs(r, rc))
rep("Ev2-C3d 3D image solution solves diffusion and vanishes at r_c", pde == 0 and simplify(p.subs(r, rc)) == 0)
rep("Ev2-C3e 3D: capture flux = dP_rel/dt with P_rel = (r_c/d) erfc((d-r_c)/sqrt(4Dt)) -> r_c/d < 1",
    simplify(flux - sp.diff(F3, w).subs(w, tt)) == 0 and simplify(sp.limit(F3, w, oo) - rc/dd) == 0)

# ======================================================================= C4 Hecht by two independent routes
lam, L, x, v, dz = symbols('ell L x v d', positive=True)
route1 = (integrate(x*exp(-x/lam)/lam, (x, 0, L)) + L*exp(-L/lam))/dz          # E[min(X,L)]/d
route2 = integrate((v/dz)*exp(-v*t/lam), (t, 0, L/v))                         # Ramo current x survival, integrated over transit
rep("Ev2-C4a Hecht: order-statistics route = Ramo-current route = (ell/d)(1 - e^{-L/ell})",
    simplify(route1 - route2) == 0 and simplify(route1 - lam/dz*(1 - exp(-L/lam))) == 0)

# ======================================================================= C5 coax Ramo
a, b, r0, r1, Vb, qc, rr = symbols('a b r_0 r_1 V_b q r', positive=True)
work = integrate(qc*Vb/(rr*log(b/a)), (rr, r0, r1))
rep("Ev2-C5 coax: bias work = V_b q [U_R(r1) - U_R(r0)]", simplify(work - Vb*qc*(log(r1/a) - log(r0/a))/log(b/a)) == 0)

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
rep("Ev2-C6a F_meas^obs = (F_eh<m^2> + <Var xi|r>)/<xi> + <N> Var_r<xi|r>/<xi> (exact mixture)", sp.simplify(Fobs_exact - formula) == 0)
rep("Ev2-C6b the position term grows with N (non-Fano scaling)", sp.diff(formula, n) != 0)
ep = symbols('epsilon', positive=True)
rep("Ev2-C6c Bernoulli, single position: F_meas = eps F_eh + 1 - eps (= WP5v3-C2a)",
    sp.simplify(formula.subs({m1: ep, m2: ep, v1: ep*(1 - ep), v2: ep*(1 - ep)}) - (ep*Fe + 1 - ep)) == 0)

# ======================================================================= C7 two-channel reconstruction with ER calibration (1803.02903 Eq. (1))
om, DN, DE, yv, g = symbols('omega D_NR D_ER y g', positive=True)        # g = eV_b/eps_eff ; D = E_stored + E_esc + E_sl deficits
# ER calibration: phonon scale k*eps_coll chosen so that an ER of energy om reads E_phi = om(1+g) ; charge scale so E_Q(ER) = om
kc = om*(1 + g)/(om - DE + g*om)               # (N_ER^meas = om/eps_eff  ->  eV_b N_ER = g om)
NNR = yv*om/1                                  # NR measured charge in energy units: E_Q = y om  -> eV_b N_NR = g y om
Ephi = kc*(om - DN + g*yv*om)
Erec = Ephi - g*yv*om
eta_exact = sp.simplify(Erec/om)
dn, de = symbols('d_NR d_ER', positive=True)
eta_d = sp.simplify(eta_exact.subs({DN: dn*om, DE: de*om}))
ser = sp.series(eta_d.subs({dn: sp.Symbol('h')*dn, de: sp.Symbol('h')*de}), sp.Symbol('h'), 0, 2).removeO().subs(sp.Symbol('h'), 1)
rep("Ev2-C7a eta^phi_NR = 1 - d_NR + d_ER (1 + y g)/(1 + g) + O(d^2)  (exact algebra vs series)",
    sp.simplify(ser - (1 - dn + de*(1 + yv*g)/(1 + g))) == 0)
rep("Ev2-C7b eta^phi_NR independent of <xi>_NR except via D (charge enters only through y, which cancels at d = 0)",
    sp.simplify(eta_d.subs({dn: 0, de: 0}) - 1) == 0)
# data: eta = 0.952 (+0.009 -0.007), Si, 4 V/cm, g ~ 1.05 [E], y ~ 0.3 [E]
kap = (1 + 0.3*1.05)/(1 + 1.05)
rep("Ev2-C7c 1803.02903 data: d_NR - 0.64 d_ER = 0.048 (+0.007/-0.009) [E inputs g, y]", abs(kap - 0.6415) < 1e-3, f"kappa = {kap:.3f}")

# ======================================================================= C8 NRT / data inversion
psurv, Edam, ER, Est1, Ed = symbols('p_surv E_dam E_R E_st1 E_d', positive=True)
fDF = psurv*Q(4, 10)*(Edam/ER)*Est1/Ed
rep("Ev2-C8a NRT f_DF decreasing in E_d at fixed E_st,1", sp.diff(fDF, Ed).is_negative)
X_si = 0.048/(0.4*0.65); X_ge = 0.0608/(0.4*0.8)    # E_dam/E_R = 0.65 (Si, 10-100 keV), 0.8 (Pb in Ge) [E]
rep("Ev2-C8b upper bounds p_surv E_st,1/E_d: Si 0.18, Ge 0.19 (if the whole deficit were E_st) [E]",
    0.15 < X_si < 0.21 and 0.15 < X_ge < 0.22, f"Si {X_si:.3f}, Ge {X_ge:.3f}")
rep("Ev2-C8c implied p_surv <= 0.41 (Si: E_st,1/E_d = 9/20), <= 0.6 (Ge: 6/19.7) [E]", X_si/(9/20) < 0.45 and X_ge/(6/19.7) < 0.65,
    f"{X_si/(9/20):.2f}, {X_ge/(6/19.7):.2f}")

# ======================================================================= C9 windowed Y_H: ratio vs linear, Delta E_trap sign, NTL normalisation
DNR, DER = symbols('D_NR D_ER', positive=True)
Yratio = (om - DNR)/(om - DER)
Ylin = 1 - (DNR - DER)/om
h = sp.Symbol('h')
err = sp.series((Yratio - Ylin).subs({DNR: h*DNR, DER: h*DER}), h, 0, 3).removeO().subs(h, 1)
rep("Ev2-C9a ratio - linear = -(D_NR - D_ER) D_ER/omega^2 + O(D^3) (linear form is first order)",
    sp.simplify(err + (DNR - DER)*DER/om**2) == 0)
# Delta E_trap sign: equal omega, ER has more pairs; same trapped fraction phi -> Delta E_trap = phi*E1*(N_NR - N_ER) < 0
phi_t, E1t, yq = symbols('phi E_1 y_q', positive=True)
dEtrap = phi_t*E1t*(yq - 1)*om/3.8
rep("Ev2-C9b Delta E_trap = E_trap^NR - E_trap^ER < 0 when the trapped fraction is equal (y < 1)",
    sp.simplify(dEtrap.subs(yq, Q(3, 10))) < 0)
SN = om - DNR + g*yv*om; SE = om - DER + g*om
YNTL = sp.simplify(SN/SE)
rep("Ev2-C9c NTL: measured NR/ER phonon ratio at D=0 is (1 + y g)/(1 + g), not 1 + g(y-1)",
    sp.simplify(YNTL.subs({DNR: 0, DER: 0}) - (1 + yv*g)/(1 + g)) == 0)

# ======================================================================= C10 mK emission numbers (hbar c corrected)
mstar, E0, eF = symbols('m_star varepsilon_0 eF', positive=True)
SFN = 2*integrate(sqrt(2*mstar*(E0 - eF*x)), (x, 0, E0/eF))
rep("Ev2-C10a triangular-barrier WKB exponent = (4/3) sqrt(2m*) eps^{3/2}/(eF)", simplify(SFN - Q(4, 3)*sqrt(2*mstar)*E0**Q(3, 2)/eF) == 0)
hbarc_eVcm = 1.97327e-5            # eV cm (corrected; v1 used 1.97e-7)
me = 510998.95
Fneed = 4/3*mp.sqrt(2*0.3*me)*0.045**1.5/(30*hbarc_eVcm)
rep("Ev2-C10b field for exponent 30 (45 meV, m* = 0.3 m_e): 1.2e4 V/cm", 1.1e4 < Fneed < 1.3e4, f"{mp.nstr(Fneed,3)} V/cm")
e_SI, eps0 = 1.602176634e-19, 8.8541878128e-12
dPF = mp.sqrt(e_SI*1e4/(mp.pi*11.7*eps0))       # V, at 100 V/cm = 1e4 V/m, Si
rep("Ev2-C10c Poole-Frenkel lowering at 100 V/cm in Si ~ 2 meV << 45 meV", 1.5e-3 < dPF < 3e-3, f"{mp.nstr(dPF*1e3,3)} meV")
rep("Ev2-C10d thermal exponent eps/T at 50 mK, 45 meV > 1e4", 0.045/(8.617333e-5*0.05) > 1e4)

# ======================================================================= C11 visibility threshold (one criterion) and pockets
sigE = 3.86; Ethr = 4.2*sigE                     # 2007.14289 sigma [FT]; 4.2 sigma trigger [E, R11 referee reading]
ecoll, Est1v = 0.3, 9.0
rep("Ev2-C11a single Frenkel-pair release visible iff E_thr <= eps_coll E_st,1 = 2.7 eV; CPD E_thr ~ 16 eV: invisible",
    ecoll*Est1v < Ethr, f"{ecoll*Est1v:.1f} eV vs {Ethr:.1f} eV")
Na_min = Ethr/ecoll/0.2
rep("Ev2-C11b pocket recrystallisation visible for N_a >~ E_thr/(eps_coll*0.2 eV) ~ 270 atoms [E]", 200 < Na_min < 400, f"N_a >= {Na_min:.0f}")

# ======================================================================= C12 STM: per-unit-lambda vs total; power
Pbar, Vf, T1 = 1.6e19, 1e-5, 8.617333e-5
per_lam = (mp.pi**2/12)*Pbar*Vf*T1**2
Qdot = lambda s: per_lam/(2*s)*(mp.e**(-float(gmin)*s) - mp.e**(-float(gmax)*s))
rel = mp.quad(Qdot, [0, 1e-3, 1, 1e3, 1e6, 1e9, mp.inf])
dlam = mp.log(gmax/gmin)/2
rep("Ev2-C12a released total = per-unit-lambda excess x Delta lambda, Delta lambda = ln(Gmax/Gmin)/2", abs(rel/(per_lam*dlam) - 1) < 1e-8,
    f"{mp.nstr(rel,3)} eV, dlam = {mp.nstr(dlam,3)}")
rep("Ev2-C12b power at 10 d ~ 0.6 eV/s; quanta <~ 3 T1 ~ 3e-4 eV: >= 1e4 quanta per 10 eV event", 0.3 < Qdot(864000.0) < 1 and 10/(3*T1) > 1e4,
    f"{mp.nstr(Qdot(864000.0),3)} eV/s")

print(f"\n{sum(RES)}/{len(RES)} PASS")
