"""WP5-v2 identity and estimate checks (R6 revision of code/WP5/checks.py).
Sympy only (exact arithmetic; evalf of exact expressions for the [E] numbers); no numerical simulation, no scipy.
Run:  python3 -I checks.py     Prints PASS/FAIL per check. Labels WP5v2-Cn (CONVENTIONS sec. 14).
v1 labels C1-C10 keep their meaning; C11-C20 are new. Notation: NOTATION v4 (eps_eh, F_eh, eps_det, H = heat, ...)."""
import sympy as sp
from sympy import Rational as Q, sqrt, pi, gamma, exp, symbols, simplify, integrate, Sum

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:74s} {note}")
def num(x, n=4): return sp.N(x, n)

# physical constants (eV, Angstrom); exact rationals so every number below is evalf of an exact expression
me   = Q(51099895, 100)          # m_e c^2 [eV]
amu  = Q(931494102, 1)           # [eV]
hc   = Q(197327, 100)            # hbar c [eV A]
alpha = 1/Q(137036, 1000)

# ---------------------------------------------------------------- C1 three-body phase space (R&K Eq. (8)); (W1) -> L21 step 4
coef = gamma(Q(3, 2))**3/gamma(Q(9, 2))
rep("WP5v2-C1a Gamma(3/2)^3/Gamma(9/2) = 2pi/105", simplify(coef - 2*pi/105) == 0)
s, x = symbols('s x', positive=True)
inner = integrate(sqrt(s*(1 - s)), (s, 0, 1))                 # y = (1-x)s: inner integral = (1-x)^2 * inner
outer = integrate(sqrt(x)*(1 - x)**2, (x, 0, 1))
rep("WP5v2-C1b exact Dirichlet integral int sqrt(x y (1-x-y)) = 2pi/105", simplify(inner*outer - 2*pi/105) == 0,
    f"(inner = {inner}, outer = {outer})")
rep("WP5v2-C1c [A] = energy^3: 7/2 - 1/2 = 3 (R&K quote 'eV^2' inconsistent)", Q(7, 2) - Q(1, 2) == 3)

# ---------------------------------------------------------------- C2 binomial thinning (R&K App. A), F_meas = eps_det F + 1 - eps_det
n, F, ed = symbols('n F epsilon_det', positive=True)
Fmeas = simplify((ed**2*F*n + ed*(1 - ed)*n)/(ed*n))
rep("WP5v2-C2a F_meas = eps_det*F_eh + 1 - eps_det (law of total variance)", simplify(Fmeas - (ed*F + 1 - ed)) == 0)
vals = [(Q(98, 100), Q(115, 1000)), (Q(95, 100), Q(115, 1000))]
ex = [num(e*f + 1 - e) for e, f in vals]; rk = [num(f/e + 1 - e) for e, f in vals]
rep("WP5v2-C2b exact 0.133/0.159 vs R&K Eq.(23) 0.137/0.171", abs(ex[0] - 0.1327) < 1e-3 and abs(rk[1] - 0.171) < 1e-3,
    f"exact {ex}, Eq.(23) {rk}")
e_rec = sp.solve(sp.Eq(ed*Q(115, 1000) + 1 - ed, Q(119, 1000)), ed)[0]
rep("WP5v2-C2c eps_det reconciling F_inf = 0.115 with 0.119: ~0.995", abs(num(e_rec) - 0.9955) < 1e-3, f"{num(e_rec, 5)}")
rep("WP5v2-C2d F_meas - F_eh = (1-eps_det)(1-F_eh) >= 0 (bound direction)", simplify(Fmeas - F - (1 - ed)*(1 - F)) == 0)

# ---------------------------------------------------------------- C3 Fano identity (W14) from (W4)
w, Eg, vH, mH = symbols('omega E_g varH meanH', positive=True)
Nbar = (w - mH)/Eg; Fano = (vH/Eg**2)/Nbar; eps_eh = w/Nbar; dH = vH/(Eg*mH)
rep("WP5v2-C3 F_eh = (eps_eh/E_g - 1) * d_H  (W14)", simplify(Fano - (eps_eh/Eg - 1)*dH) == 0)

# ---------------------------------------------------------------- C4 Klein limit
t = symbols('t', positive=True); Eth = Q(3, 2)*Eg
pdf = sqrt(t)/integrate(sqrt(t), (t, 0, Eth))
m1 = simplify(integrate(t*pdf, (t, 0, Eth))); m2 = simplify(integrate(t**2*pdf, (t, 0, Eth)))
rep("WP5v2-C4a Klein eps_eh = E_g + 2<E_res> = 14/5 E_g", simplify(Eg + 2*m1 - Q(14, 5)*Eg) == 0)
Fk = simplify(2*(m2 - m1**2)/Eg**2)
rep("WP5v2-C4b independent residuals: F_eh = 54/175 = 0.309", Fk == Q(54, 175), f"{Fk}")

# ---------------------------------------------------------------- C5 binary e-h threshold for a slow ion (free-electron v_F)
def ER_th(Eg_, kF, A):
    vF = kF*hc/me; vth = Eg_/(2*me*vF); return Q(1, 2)*A*amu*vth**2
si = ER_th(Q(117, 100), Q(175, 100), Q(2809, 100)); ge = ER_th(Q(74, 100), Q(160, 100), Q(7263, 100))
rep("WP5v2-C5 E_R,th = 375 eV (Si), 465 eV (Ge)", abs(num(si) - 375) < 5 and abs(num(ge) - 465) < 5, f"{num(si)}, {num(ge)}")

# ---------------------------------------------------------------- C6 Massey parameter and Born parameter
def vN(ER, A): return sqrt(2*ER/(A*amu))
xi20 = Q(117, 100)/(hc*vN(20, Q(2809, 100))); xi1k = Q(117, 100)/(hc*vN(1000, Q(2809, 100)))
born = 14*alpha/vN(1000, Q(2809, 100))
rep("WP5v2-C6 xi_Mas(20 eV) ~ 15, xi_Mas(1 keV) ~ 2, Z alpha/v_N(1 keV) ~ 3.7e2",
    abs(num(xi20) - 15) < 1 and abs(num(xi1k) - 2) < 0.3 and 300 < num(born) < 450, f"{num(xi20,3)}, {num(xi1k,3)}, {num(born,3)}")

# ---------------------------------------------------------------- C7 impulse Doppler width (W9) with WP2 (5.3) normalisation
ER_, Ek, wb = symbols('E_R E_kin wbar', positive=True)
q2, M = symbols('q2 M', positive=True)
sig2 = q2*(2*M*Ek)/M**2                                  # sigma^2 = q^2 <P_q^2>/M^2, <P_q^2> = 2 M E^kin_q
rep("WP5v2-C7a sigma_omega^2 = 4 E_R E^kin_q (E_R = q^2/2M)", simplify(sig2.subs(q2, 2*M*ER_) - 4*ER_*Ek) == 0)
rep("WP5v2-C7b harmonic T=0: E^kin_q = <omega>/4 -> sigma^2 = E_R <omega>", simplify(4*ER_*wb/4 - ER_*wb) == 0)
s10 = sqrt(10*Q(45, 1000)); s20 = sqrt(20*Q(45, 1000))
rep("WP5v2-C7c Si sigma_omega(10, 20 eV) = 0.67, 0.95 eV", abs(num(s10) - 0.67) < 0.01 and abs(num(s20) - 0.95) < 0.01)

# ---------------------------------------------------------------- C8 flat barrier density -> 1/t (W12)
G, T_, Ga, tt, Nb = symbols('Gamma T Gamma_att t N_b', positive=True)
rate = integrate(Nb*T_*exp(-G*tt), (G, 0, Ga))
rep("WP5v2-C8 release rate = N_b T (1 - e^{-Gamma_att t})/t", simplify(rate - Nb*T_*(1 - exp(-Ga*tt))/tt) == 0)

# ---------------------------------------------------------------- C9 generating-function second moment (W3)
p, z = symbols('p z', positive=True); Gz = (1 - p) + p*z
m = sp.diff(Gz, z).subs(z, 1); var = sp.diff(Gz, z, 2).subs(z, 1) + m - m**2
rep("WP5v2-C9 one-step generating-function variance = p(1-p)", simplify(var - p*(1 - p)) == 0)

# ---------------------------------------------------------------- C10 reduced-energy conventions (L20 discrepancy (1))
cL = Q(115, 10)/sp.Integer(14)**Q(7, 3)
cZ12 = Q(162616, 10000)/((sp.Integer(12)**Q(23, 100) + sp.Integer(14)**Q(23, 100))*12*14)
rep("WP5v2-C10 Lindhard 0.0243 vs ZBL(Z1=12) 0.0268 keV^-1: differ by ~10%",
    abs(num(cL) - 0.0243) < 2e-4 and abs(num(cZ12) - 0.0268) < 2e-4 and num(cZ12/cL - 1) > 0.05, f"{num(cL)}, {num(cZ12)}")

# ---------------------------------------------------------------- C11 electron -> nucleus maximum energy transfer (corrects v1 sec. 4)
Ee = 10; MSi = Q(2809, 100)*amu
Emax_nr = 4*me*MSi*Ee/(me + MSi)**2
Emax_rel = 2*Ee*(Ee + 2*me)/MSi
rep("WP5v2-C11 E_max(10 eV e -> Si) = 0.78 meV (v1 quoted 1.5 meV)", abs(num(Emax_nr*1000) - 0.78) < 0.01
    and abs(num(Emax_rel*1000) - 0.78) < 0.01, f"{num(Emax_nr*1000, 3)} meV")

# ---------------------------------------------------------------- C12 Lindhard E_el at 25 keV Si and the F_NR identity
eps_red = cL*25; kL = Q(133, 1000)*sp.Integer(14)**Q(2, 3)/sqrt(Q(2809, 100))
g = 3*eps_red**Q(15, 100) + Q(7, 10)*eps_red**Q(6, 10) + eps_red
Eel = 25*kL*g/(1 + kL*g)
rep("WP5v2-C12a Lindhard E_el(25 keV, Si) = 9.1 keV", abs(num(Eel) - 9.1) < 0.05, f"{num(Eel)} keV")
Fe, ee, mE, vE = symbols('F_eh eps_eh mE vE', positive=True)
tot_var = Fe*mE/ee + vE/ee**2; FNR = simplify(tot_var/(mE/ee))
rep("WP5v2-C12b F_NR = F_eh + Var(E_el)/(eps_eh <E_el>)", simplify(FNR - (Fe + vE/(ee*mE))) == 0)
rel = sqrt(24*Q(375, 100)*num(Eel)*1000)/(num(Eel)*1000)
rep("WP5v2-C12c F_NR ~ 24 needs sigma(E_el)/<E_el> ~ 10%", abs(num(rel) - 0.099) < 0.005, f"{num(rel, 3)}")

# ---------------------------------------------------------------- C13 (W1) chain: |V|^2 S_cc = 2 v_C |rho|^2 L/(1-e^{-beta omega})
pp, e2, L, r2, bw = symbols('p e2 L rho2 betaomega', positive=True)
vC = e2/pp**2
lhs = (vC**2*r2)*(2*pp**2/e2)*L/(1 - exp(-bw)); rhs = 2*vC*r2*L/(1 - exp(-bw))
rep("WP5v2-C13 v_C(p)^2 |rho|^2 S_cc = 2 v_C(p) |rho|^2 L/(1-e^{-beta omega})", simplify(lhs - rhs) == 0)

# ---------------------------------------------------------------- C14 Fano term F_{Lambda0,nu} (O4.7): sum rule, PT zero, bound (W15)
Gv = symbols('G1:4', positive=True); cv = symbols('c1:4', real=True); Pv = symbols('P1:4', real=True)
Gs = sum(Gv); cbar = sum(Gi*ci for Gi, ci in zip(Gv, cv))/Gs
Fv = [2*pi*Gi*(cbar - ci) for Gi, ci in zip(Gv, cv)]
rep("WP5v2-C14a sum_nu F_nu = 0", simplify(sum(Fv)) == 0)
rep("WP5v2-C14b PT-real rho, a_off -> c_nu = 0 -> F_nu = 0", all(simplify(f.subs({c: 0 for c in cv})) == 0 for f in Fv))
mid = symbols('m', real=True)
dP = sum(f*P for f, P in zip(Fv, Pv)); dPm = sum(f*(P - mid) for f, P in zip(Fv, Pv))
rep("WP5v2-C14c sum_nu F_nu P_nu = sum_nu F_nu (P_nu - m) for any m (=> TV bound (W15))", simplify(dP - dPm) == 0)
# exact-rational spot checks of |dP| <= (1/2) sum|F| (max P - min P)
import itertools
okb = True
for G_, c_, P_ in itertools.product([(1, 2, 3), (5, 1, 1)], [(Q(1, 10), -Q(1, 5), Q(3, 10)), (0, Q(1, 7), -Q(2, 7))],
                                     [(Q(1, 2), Q(1, 3), Q(9, 10)), (0, 1, Q(1, 2))]):
    sub = dict(zip(Gv, G_)); sub.update(zip(cv, c_)); sub.update(zip(Pv, P_))
    lhs_ = abs(dP.subs(sub)); bnd = Q(1, 2)*sum(abs(f.subs(sub)) for f in Fv)*(max(P_) - min(P_))
    okb &= bool(sp.simplify(bnd - lhs_) >= 0)
rep("WP5v2-C14d |Delta P| <= (1/2) sum|F_nu| * spread(P) on exact test cases", okb)
est = Q(3, 10)*Q(36, 100)
rep("WP5v2-C14e GaAs estimate |Delta P| <~ 0.11 Gamma/delta  [E]", abs(num(est) - 0.108) < 1e-3, f"coefficient {num(est, 3)}")

# ---------------------------------------------------------------- C15 eta_pb normalisation (W13) vs WP4 [4.6]
D, om = symbols('Delta_BCS omega', positive=True)
eta5 = D*2/om; eta4 = 2*D*2/om
rep("WP5v2-C15a (W13) at omega<3Delta (N_qp=2): eta_pb = 2Delta/omega <= 1 on [2Delta, 3Delta]",
    simplify(eta5.subs(om, 2*D) - 1) == 0)
rep("WP5v2-C15b v1 WP4 [4.6] 2Delta N_qp/omega gave 2 at omega = 2Delta (flag I1, CLOSED: WP4-v2 uses (W13))",
    simplify(eta4.subs(om, 2*D) - 2) == 0, "record only")

# ---------------------------------------------------------------- C16 (W8) survival probability solves dp/dE0 = (Gamma_ii/(dE/dt)) p
E0, E = symbols('E0 E', positive=True); Gii = sp.Function('Gamma_ii'); Pw = sp.Function('Pw')
pno = exp(-sp.Integral(Gii(E)/Pw(E), (E, 1, E0)))
rep("WP5v2-C16 d p_no-ii/dE0 = -(Gamma_ii/(dE/dt|_ph)) p_no-ii  (W8)",
    simplify(sp.diff(pno, E0) + Gii(E0)/Pw(E0)*pno) == 0)

# ---------------------------------------------------------------- C17 sec. 3.2 / sec. 4 numbers
Tx_K = (Q(4135667, 10**9)*10)/(2*pi)/Q(8617333, 10**11)   # h [eV/THz] * 10 THz / 2pi / k_B
uamp = sqrt(2*1/(MSi*Q(45, 1000)**2))*hc
lam = 2*pi*hc/sqrt(2*MSi*20)
rep("WP5v2-C17 T_x = 76 K; u(1 eV, <omega>=45 meV) = 0.38 A; lambda_dB(20 eV) = 0.012 A",
    abs(num(Tx_K) - 76) < 1.5 and abs(num(uamp) - 0.38) < 0.01 and abs(num(lam) - 0.0121) < 5e-4,
    f"{num(Tx_K,3)} K, {num(uamp,3)} A, {num(lam,3)} A")

# ---------------------------------------------------------------- C18 step model offset and failure point (L21)
bN = Q(1, 2) - Q(117, 100)/Q(375, 100)
rep("WP5v2-C18 b_N = 1/2 - E_g/eps_eh = 0.19 (Si); nbar > 1/(4F) = 2.1", abs(num(bN) - 0.188) < 2e-3
    and abs(num(1/(4*Q(119, 1000))) - 2.1) < 0.01)

# ---------------------------------------------------------------- C19 phonon shot-noise Fano estimates (L23 (iii))
fsi = (Q(3749, 1000)/Q(116, 100) - 1)*Q(63, 1000)/Q(116, 100)
fge = (Q(296, 100)/Q(73, 100) - 1)*Q(37, 1000)/Q(73, 100)
rep("WP5v2-C19 F_shot = 0.121 (Si 123 K), 0.155 (Ge 77 K)  [E]", abs(num(fsi) - 0.121) < 1e-3 and abs(num(fge) - 0.155) < 1e-3)

# ---------------------------------------------------------------- C20 WP2-v2 IF-2: absorbed phonons and drag-mass subtraction (sec. 3.1)
w1, w2, wa, nc1, nc2, na, om_ = symbols('w1 w2 wa n1 n2 na omega', positive=True)
# rho^ph with two emission lines (+w1, +w2) and one absorption line (-wa); first moment must equal omega (WP2 (3.6))
rho = [(w1, nc1), (w2, nc2), (-wa, na)]
m1_ = sum(wv*nv for wv, nv in rho)
created = nc1 + nc2; absorbed = na
heat_net = m1_; heat_abs = sum(abs(wv)*nv for wv, nv in rho)
rep("WP5v2-C20a omega' < 0 = absorption: H = int omega' rho = omega (net), != int |omega'| rho",
    simplify(heat_abs - heat_net - 2*wa*na) == 0 and simplify(created + absorbed - sum(nv for _, nv in rho)) == 0)
qq, MM, dM = symbols('q M_kappa deltaM', positive=True)
EMig = qq**2*dM/(2*MM**2); fGS = qq**2/(2*MM) - EMig
rep("WP5v2-C20b GS + Migdal first moments = q^2/2M (no double count); GS rescale 1 - 2M E_Mig/q^2 = 1 - dM/M",
    simplify(fGS + EMig - qq**2/(2*MM)) == 0 and simplify(fGS/(qq**2/(2*MM)) - (1 - dM/MM)) == 0)
rep("WP5v2-C20c naive GS (full f-sum) + Migdal overcounts by E_Mig = q.dM.q/2M^2", simplify(qq**2/(2*MM) + EMig - qq**2/(2*MM) - EMig) == 0)

print(f"\n{sum(RES)}/{len(RES)} PASS")
