"""WP5-v3 identity and estimate checks (R8 revision of code/WP5-v2/checks.py after the R7 hostile review).
Sympy only (exact arithmetic; evalf of exact expressions for the [E] numbers); no numerical simulation, no scipy.
Run:  python3 -I checks.py     Prints PASS/FAIL per check. Labels WP5v3-Cn (CONVENTIONS sec. 14).
C1-C20 keep their v2 subject; checks the R7 referees called vacuous or wrong are REPLACED (C1c, C2d, C5, C6, C7b, C14e,
C18, C20b, C20c; C15a updated to the 4 Delta_BCS cascade onset); C21-C30 are new (R8 derivations).
R9 clean-up: C18, C19, C20c, C26, C27 revised per VER-WP5-A/B.
Notation: NOTATION v4 (eps_eh, F_eh, eps_det, H = heat, ...)."""
import itertools
import sympy as sp
from sympy import Rational as Q, sqrt, pi, gamma, exp, log, symbols, simplify, integrate, I, oo

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:78s} {note}")
def num(x, n=4): return sp.N(x, n)

# physical constants (eV, Angstrom); exact rationals so every number below is evalf of an exact expression
me    = Q(51099895, 100)         # m_e c^2 [eV]
amu   = Q(931494102, 1)          # [eV]
hc    = Q(197327, 100)           # hbar c [eV A]
alpha = 1/Q(137036, 1000)
ASi, AGe = Q(2809, 100), Q(7263, 100)
MSi = ASi*amu

# ---------------------------------------------------------------- C1 three-body phase space (R&K Eq. (8)); L21 step 4
coef = gamma(Q(3, 2))**3/gamma(Q(9, 2))
rep("WP5v3-C1a Gamma(3/2)^3/Gamma(9/2) = 2pi/105", simplify(coef - 2*pi/105) == 0)
s, x = symbols('s x', positive=True)
inner = integrate(sqrt(s*(1 - s)), (s, 0, 1)); outer = integrate(sqrt(x)*(1 - x)**2, (x, 0, 1))
rep("WP5v3-C1b exact Dirichlet integral int sqrt(x y (1-x-y)) = 2pi/105", simplify(inner*outer - 2*pi/105) == 0)
# C1c (replaced; R7 B-V19: v2 C1c was 7/2 - 1/2 = 3). Dimensional analysis of R&K Eqs. (8)-(9) with exponents of (energy, length).
def dim(*pairs):  # product of (base, power) -> (energy exponent, length exponent)
    return (sum(p[0]*k for p, k in pairs), sum(p[1]*k for p, k in pairs))
EN, LEN, ONE = (1, 0), (0, 1), (0, 0)
hb2m = dim((EN, 1), (LEN, 2))                                   # hbar^2/2m ~ E L^2
VDelta_real = dim((LEN, 3), (LEN, 3)); VDelta_k = dim((LEN, 3), (LEN, -3))
A_eq9_real = (3*hb2m[0] - VDelta_real[0], 3*hb2m[1] - VDelta_real[1])  # |M|-ratio dimensionless
A_eq9_k = (3*hb2m[0] - VDelta_k[0], 3*hb2m[1] - VDelta_k[1])
a = symbols('a'); A_eq8 = sp.solve(sp.Eq(a + Q(1, 2) - Q(7, 2), 0), a)[0]   # Eq.(8) ratio dimensionless
rep("WP5v3-C1c Eq.(9) with real-space Delta gives [A]=E^3 = Eq.(8) requirement; k-space Delta would not",
    A_eq9_real == (3, 0) and A_eq8 == 3 and A_eq9_k != (3, 0), f"Eq9(real)={A_eq9_real}, Eq9(k)={A_eq9_k}, Eq8: E^{A_eq8}")

# ---------------------------------------------------------------- C2 binomial thinning (R&K App. A)
n, F, ed = symbols('n F epsilon_det', positive=True)
Fmeas = simplify((ed**2*F*n + ed*(1 - ed)*n)/(ed*n))
rep("WP5v3-C2a F_meas = eps_det*F_eh + 1 - eps_det (law of total variance)", simplify(Fmeas - (ed*F + 1 - ed)) == 0)
vals = [(Q(98, 100), Q(115, 1000)), (Q(95, 100), Q(115, 1000))]
ex = [num(e*f + 1 - e) for e, f in vals]; rk = [num(f/e + 1 - e) for e, f in vals]
rep("WP5v3-C2b exact 0.133/0.159 vs R&K Eq.(23) 0.137/0.171", abs(ex[0] - 0.1327) < 1e-3 and abs(rk[1] - 0.171) < 1e-3,
    f"exact {ex}, Eq.(23) {rk}")
e_rec = sp.solve(sp.Eq(ed*Q(115, 1000) + 1 - ed, Q(119, 1000)), ed)[0]
rep("WP5v3-C2c eps_det reconciling F_inf = 0.115 with 0.119: ~0.995", abs(num(e_rec) - 0.9955) < 1e-3, f"{num(e_rec, 5)}")
# C2d (replaced; R7 A-V14, B-V14): the bound direction compares R&K's formula with the exact one
diff23 = simplify((F/ed + 1 - ed) - Fmeas)
pos = all(diff23.subs({F: f_, ed: e_}) > 0 for f_ in (Q(1, 10), Q(1, 2)) for e_ in (Q(1, 10), Q(9, 10), Q(99, 100)))
rep("WP5v3-C2d Eq.(23) - exact = F(1-eps^2)/eps = F(1/eps - eps) >= 0: R&K's is an UPPER bound",
    simplify(diff23 - F*(1 - ed**2)/ed) == 0 and simplify(diff23 - F*(1/ed - ed)) == 0 and pos)
rep("WP5v3-C2e R&K's 0.130 at eps = 0.98 = exact formula with F = 0.112 (0.1298)",
    abs(num(Q(98, 100)*Q(112, 1000) + Q(2, 100)) - 0.1298) < 1e-4)

# ---------------------------------------------------------------- C3 Fano identity (W14) from (W4)
w, Eg, vH, mH = symbols('omega E_g varH meanH', positive=True)
Nbar = (w - mH)/Eg; Fano = (vH/Eg**2)/Nbar; eps_eh = w/Nbar; dH = vH/(Eg*mH)
rep("WP5v3-C3 F_eh = (eps_eh/E_g - 1) * d_H  (W14)", simplify(Fano - (eps_eh/Eg - 1)*dH) == 0)

# ---------------------------------------------------------------- C4 Klein limit
t = symbols('t', positive=True); Eth = Q(3, 2)*Eg
pdf = sqrt(t)/integrate(sqrt(t), (t, 0, Eth))
m1 = simplify(integrate(t*pdf, (t, 0, Eth))); m2 = simplify(integrate(t**2*pdf, (t, 0, Eth)))
rep("WP5v3-C4a Klein eps_eh = E_g + 2<E_res> = 14/5 E_g", simplify(Eg + 2*m1 - Q(14, 5)*Eg) == 0)
Fk = simplify(2*(m2 - m1**2)/Eg**2)
rep("WP5v3-C4b independent residuals: F_eh = 54/175 = 0.309", Fk == Q(54, 175), f"{Fk}")

# ---------------------------------------------------------------- C5 binary e-h threshold for a slow ion (CORRECTED inputs)
def kF_fe(a_):  # free-electron k_F for 4 valence e/atom, diamond lattice: n = 32/a^3
    return (3*pi**2*32/a_**3)**Q(1, 3)
kSi, kGe = kF_fe(Q(5431, 1000)), kF_fe(Q(5658, 1000))
def ER_th(Eg_, kF, A, keep_vN2=False):
    vF = kF*hc/me
    if keep_vN2:
        v = symbols('v', positive=True); vth = [r for r in sp.solve(2*me*v*(v + vF) - Eg_, v) if r.is_positive][0]
    else:
        vth = Eg_/(2*me*vF)
    return Q(1, 2)*A*amu*vth**2
si, ge = ER_th(Q(117, 100), kSi, ASi), ER_th(Q(74, 100), kGe, AGe)
si2, ge2 = ER_th(Q(117, 100), kSi, ASi, True), ER_th(Q(74, 100), kGe, AGe, True)
rep("WP5v3-C5a free-electron k_F = 1.808 (Si), 1.736 (Ge) A^-1 [v2 hard-coded 1.75, 1.60]",
    abs(num(kSi) - 1.808) < 1e-3 and abs(num(kGe) - 1.736) < 1e-3, f"{num(kSi)}, {num(kGe)}")
rep("WP5v3-C5b E_R,th = 352 eV (Si), 395 eV (Ge) [v2: 375, 465]", abs(num(si) - 352) < 2 and abs(num(ge) - 395) < 2,
    f"{num(si)}, {num(ge)}")
rep("WP5v3-C5c keeping v_N^2: 336 eV (Si), 382 eV (Ge)", abs(num(si2) - 336) < 2 and abs(num(ge2) - 382) < 2,
    f"{num(si2)}, {num(ge2)}")

# ---------------------------------------------------------------- C6 Massey parameter and Born parameter (CORRECTED velocity)
def vN(ER, A): return sqrt(2*ER/(A*amu))
xi20 = Q(117, 100)/(hc*vN(20, ASi)); xi1k = Q(117, 100)/(hc*vN(1000, ASi))
vFSi, vFGe = kSi*hc/me, kGe*hc/me
bornSi, bornGe = 14*alpha/vFSi, 32*alpha/vFGe
born_v2 = 14*alpha/vN(1000, ASi)
rep("WP5v3-C6a xi_Mas(20 eV) ~ 15, xi_Mas(1 keV) ~ 2", abs(num(xi20) - 15) < 1 and abs(num(xi1k) - 2) < 0.3,
    f"{num(xi20,3)}, {num(xi1k,3)}")
rep("WP5v3-C6b Born parameter Z alpha/v_F = 14.6 (Si), 34.8 (Ge); v_N << v_F at 1 keV",
    abs(num(bornSi) - 14.6) < 0.1 and abs(num(bornGe) - 34.8) < 0.2 and num(vN(1000, ASi)/vFSi) < 0.05,
    f"{num(bornSi,3)}, {num(bornGe,3)}; v_N/v_F = {num(vN(1000, ASi)/vFSi,2)}; v2's Z alpha/v_N = {num(born_v2,3)} (wrong velocity)")

# ---------------------------------------------------------------- C7 impulse Doppler width (W9)
ER_, Ek, wb = symbols('E_R E_kin wbar', positive=True)
q2, M = symbols('q2 M', positive=True)
sig2 = q2*(2*M*Ek)/M**2
rep("WP5v3-C7a sigma_omega^2 = 4 E_R E^kin_q (E_R = q^2/2M)", simplify(sig2.subs(q2, 2*M*ER_) - 4*ER_*Ek) == 0)
# C7b (replaced; R7 B-V19): derive E^kin = omega/4 per direction from the harmonic ground state, then average over D(omega)
X, Mo, wo = symbols('X M_o w_o', positive=True)
psi = exp(-Mo*wo*X**2/2)
p2 = integrate(psi*(-sp.diff(psi, X, 2)), (X, -oo, oo))/integrate(psi**2, (X, -oo, oo))
w1_, w2_, f1 = symbols('w_1 w_2 f_1', positive=True)
Ekin_mix = f1*(p2/(2*Mo)).subs(wo, w1_) + (1 - f1)*(p2/(2*Mo)).subs(wo, w2_)
rep("WP5v3-C7b harmonic T=0: <p^2> = M w/2 => E^kin_q = <omega>_D/4 (two-mode D check) => sigma^2 = E_R<omega>",
    simplify(p2 - Mo*wo/2) == 0 and simplify(Ekin_mix - (f1*w1_ + (1 - f1)*w2_)/4) == 0)
s10 = sqrt(10*Q(45, 1000)); s20 = sqrt(20*Q(45, 1000))
rep("WP5v3-C7c Si sigma_omega(10, 20 eV) = 0.67, 0.95 eV (Doppler part only: lower bound on P_FP width)",
    abs(num(s10) - 0.67) < 0.01 and abs(num(s20) - 0.95) < 0.01)

# ---------------------------------------------------------------- C8 flat barrier density -> 1/t (W12)
G, T_, Ga, tt, Nb = symbols('Gamma T Gamma_att t N_b', positive=True)
rate = integrate(Nb*T_*exp(-G*tt), (G, 0, Ga))
rep("WP5v3-C8 release rate = N_b T (1 - e^{-Gamma_att t})/t", simplify(rate - Nb*T_*(1 - exp(-Ga*tt))/tt) == 0)

# ---------------------------------------------------------------- C9 generating-function second moment (W3)
p, z = symbols('p z', positive=True); Gz = (1 - p) + p*z
m = sp.diff(Gz, z).subs(z, 1); var = sp.diff(Gz, z, 2).subs(z, 1) + m - m**2
rep("WP5v3-C9 one-step generating-function variance = p(1-p)", simplify(var - p*(1 - p)) == 0)

# ---------------------------------------------------------------- C10 reduced-energy conventions (L20 discrepancy (1); A/B disagreement)
cL = Q(115, 10)/sp.Integer(14)**Q(7, 3)
def cZBL(Z1, Z2=14): return Q(162616, 10000)/((sp.Integer(Z1)**Q(23, 100) + sp.Integer(Z2)**Q(23, 100))*Z1*Z2)
rep("WP5v3-C10a Lindhard 0.0243 vs ZBL(Z1=12) 0.0268 keV^-1: +10%",
    abs(num(cL) - 0.0243) < 2e-4 and abs(num(cZBL(12)) - 0.0268) < 2e-4 and abs(num(cZBL(12)/cL - 1) - 0.10) < 0.01,
    f"{num(cL)}, {num(cZBL(12))}")
rep("WP5v3-C10b ZBL(Z1=14) 0.0226 keV^-1: -7%; |difference| >= 7% for either Z1 reading",
    abs(num(cZBL(14)) - 0.0226) < 2e-4 and abs(num(cZBL(14)/cL - 1) + 0.07) < 0.01, f"{num(cZBL(14))}, {num(cZBL(14)/cL - 1, 2)}")

# ---------------------------------------------------------------- C11 electron -> nucleus maximum energy transfer
Ee = 10
Emax_nr = 4*me*MSi*Ee/(me + MSi)**2; Emax_rel = 2*Ee*(Ee + 2*me)/MSi
rep("WP5v3-C11 E_max(10 eV e -> Si) = 0.78 meV", abs(num(Emax_nr*1000) - 0.78) < 0.01
    and abs(num(Emax_rel*1000) - 0.78) < 0.01, f"{num(Emax_nr*1000, 3)} meV")

# ---------------------------------------------------------------- C12 Lindhard E_el at 25 keV Si and the F_NR identity
eps_red = cL*25; kL = Q(133, 1000)*sp.Integer(14)**Q(2, 3)/sqrt(ASi)
g = 3*eps_red**Q(15, 100) + Q(7, 10)*eps_red**Q(6, 10) + eps_red
Eel = 25*kL*g/(1 + kL*g)
rep("WP5v3-C12a Lindhard E_el(25 keV, Si) = 9.1 keV", abs(num(Eel) - 9.1) < 0.05, f"{num(Eel)} keV")
Fe, ee, mE, vE = symbols('F_eh eps_eh mE vE', positive=True)
FNR = simplify((Fe*mE/ee + vE/ee**2)/(mE/ee))
rep("WP5v3-C12b F_NR = F_eh + Var(E_el)/(eps_eh <E_el>)", simplify(FNR - (Fe + vE/(ee*mE))) == 0)
rel = sqrt(24*Q(375, 100)*num(Eel)*1000)/(num(Eel)*1000)
rep("WP5v3-C12c F_NR ~ 24 needs sigma(E_el)/<E_el> ~ 10%", abs(num(rel) - 0.099) < 0.005, f"{num(rel, 3)}")

# ---------------------------------------------------------------- C13 (W1) chain
pp, e2, L, r2, bw = symbols('p e2 L rho2 betaomega', positive=True)
vC = e2/pp**2
lhs = (vC**2*r2)*(2*pp**2/e2)*L/(1 - exp(-bw)); rhs = 2*vC*r2*L/(1 - exp(-bw))
rep("WP5v3-C13 v_C(p)^2 |rho|^2 S_cc = 2 v_C(p) |rho|^2 L/(1-e^{-beta omega})", simplify(lhs - rhs) == 0)

# ---------------------------------------------------------------- C14 Fano term (O4.7): sum rule, PT/Kramers zero, bound (W15), K_nu >= 0
Gv = symbols('G1:4', positive=True); cv = symbols('c1:4', real=True); Pv = symbols('P1:4', real=True)
Gs = sum(Gv); cbar = sum(Gi*ci for Gi, ci in zip(Gv, cv))/Gs
Fv = [2*pi*Gi*(cbar - ci) for Gi, ci in zip(Gv, cv)]
rep("WP5v3-C14a sum_nu F_nu = 0", simplify(sum(Fv)) == 0)
rep("WP5v3-C14b PT-real rho, a_off -> c_nu = 0 -> F_nu = 0 (definition record)", all(simplify(f.subs({c: 0 for c in cv})) == 0 for f in Fv))
mid = symbols('m', real=True)
dP = sum(f*P for f, P in zip(Fv, Pv)); dPm = sum(f*(P - mid) for f, P in zip(Fv, Pv))
rep("WP5v3-C14c sum_nu F_nu P_nu = sum_nu F_nu (P_nu - m) for any m", simplify(dP - dPm) == 0)
okb = True; ok2 = True; okK = True
cases = list(itertools.product([(1, 2, 3), (5, 1, 1)], [(Q(1, 10), -Q(1, 5), Q(3, 10)), (0, Q(1, 7), -Q(2, 7)), (Q(1, 20), Q(1, 20), -Q(1, 13))],
                               [(Q(1, 2), Q(1, 3), Q(9, 10)), (0, 1, Q(1, 2))]))
for G_, c_, P_ in cases:
    sub = dict(zip(Gv, G_)); sub.update(zip(cv, c_)); sub.update(zip(Pv, P_))
    sumF = sum(abs(f.subs(sub)) for f in Fv); cmax = max(abs(c) for c in c_)
    okb &= bool(Q(1, 2)*sumF*(max(P_) - min(P_)) - abs(dP.subs(sub)) >= 0)
    ok2 &= bool(2*pi*sum(G_)*cmax - Q(1, 2)*sumF >= 0)
    if 4*pi*cmax <= 1:
        okK &= all((Gi + f.subs(sub)) >= 0 for Gi, f in zip(G_, Fv))
rep("WP5v3-C14d |Delta P| <= (1/2) sum|F_nu| * spread(P) on exact test cases", okb)
# C14e (replaced; R7 B-V19 called v2 C14e an arithmetic restatement): second inequality of (W15) and positivity of K_nu
cn = symbols('c_n', real=True); cm = symbols('c_max', positive=True)
Kn_lower = 1 - 2*pi*2*cm                      # 1 + 2pi(cbar - c_nu) >= 1 - 2pi*2*c_max since |cbar - c_nu| <= 2 c_max
rep("WP5v3-C14e (1/2)sum|F| <= 2pi Gamma^ph max|c| (test cases); K_nu >= 0 whenever 4pi max|c| <= 1",
    ok2 and okK and sp.solve(sp.Eq(Kn_lower, 0), cm)[0] == 1/(4*pi))
# C14f (new; R7 A-V17(c)): with SOC, (PT)^2 = -1: Kramers blocks are quaternion-real; only the Kramers TRACE is real
a0, a1, a2, a3, b0, b1, b2, b3 = symbols('a0:4 b0:4', real=True)
sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])
qr = lambda c0, c1, c2, c3: c0*sp.eye(2) + I*(c1*sx + c2*sy + c3*sz)
Rb, Ab = qr(a0, a1, a2, a3), qr(b0, b1, b2, b3)
trace_im = sp.im(sp.expand((Rb.H*Ab).trace())); elem_im = sp.im(sp.expand(sp.conjugate(Rb[0, 0])*Ab[0, 0]))
rep("WP5v3-C14f SOC: Im tr(rho^dag a_off) = 0 over a Kramers pair, element-wise Im != 0",
    simplify(trace_im) == 0 and simplify(elem_im) != 0, f"element-wise Im = {simplify(elem_im)}")
# C14g (new; R7 A-V17(a)): dimension of the normalised c^F: Gamma*Im(rho* a_off)/|rho|^2 with [a_off] = [rho]/E is dimensionless
E_d, rho_d = symbols('E_dim rho_dim', positive=True)
cF_raw = rho_d*(rho_d/E_d); cF_norm = E_d*cF_raw/rho_d**2
rep("WP5v3-C14g c^F_raw ~ |rho|^2/E (not a pure number); c^F = Gamma Im(rho* a)/|rho|^2 is dimensionless",
    simplify(cF_norm) == 1 and simplify(cF_raw) != 1)
# ---------------------------------------------------------------- C15 eta_pb normalisation (W13); cascade onset at 4 Delta_BCS
D, om = symbols('Delta_BCS omega', positive=True)
eta5 = D*2/om
# a QP at E can emit a pair-breaking phonon (omega' >= 2 Delta) only if E - Delta >= 2 Delta; the hottest QP of the pair has E = omega - Delta
E_onset = sp.solve(sp.Eq(om - D - D, 2*D), om)[0]
rep("WP5v3-C15a N_qp = 2 for omega < 4 Delta_BCS (onset omega - Delta - Delta = 2 Delta); eta_pb = 2Delta/omega in [1/2, 1]",
    simplify(E_onset - 4*D) == 0 and simplify(eta5.subs(om, 2*D) - 1) == 0 and simplify(eta5.subs(om, 4*D) - Q(1, 2)) == 0)
eta4 = 2*D*2/om
rep("WP5v3-C15b v1 WP4 [4.6] 2Delta N_qp/omega gave 2 at omega = 2Delta (flag I1, CLOSED)", simplify(eta4.subs(om, 2*D) - 2) == 0, "record only")

# ---------------------------------------------------------------- C16 (W8)
E0, E = symbols('E0 E', positive=True); Gii = sp.Function('Gamma_ii'); Pw = sp.Function('Pw')
pno = exp(-sp.Integral(Gii(E)/Pw(E), (E, 1, E0)))
rep("WP5v3-C16 d p_no-ii/dE0 = -(Gamma_ii/(dE/dt|_ph)) p_no-ii  (W8)", simplify(sp.diff(pno, E0) + Gii(E0)/Pw(E0)*pno) == 0)

# ---------------------------------------------------------------- C17 sec. 3.2 / sec. 4 numbers
Tx_K = (Q(4135667, 10**9)*10)/(2*pi)/Q(8617333, 10**11)
uamp = sqrt(2*1/(MSi*Q(45, 1000)**2))*hc
lam = 2*pi*hc/sqrt(2*MSi*20)
rep("WP5v3-C17 T_x = 76 K; u(1 eV) = 0.38 A; lambda_dB(20 eV) = 0.012 A",
    abs(num(Tx_K) - 76) < 1.5 and abs(num(uamp) - 0.38) < 0.01 and abs(num(lam) - 0.0121) < 5e-4)

# ---------------------------------------------------------------- C18 step model offset and heuristic failure point (R9: b_N not assumed)
bN = Q(1, 2) - Q(117, 100)/Q(375, 100)
nfail = 1/(4*Q(119, 1000))
wf = [Q(375, 100)*(nfail - bb) for bb in (Q(3, 10), -Q(3, 10))]   # URF b_N unknown; |b_N| <= 0.3 [E] (VER-WP5-A N2)
rep("WP5v3-C18 matching b_N = 0.19 (Si); sigma_N >= 1/2 at nbar = 2.1 -> omega in [6.8, 9.0] eV for |b_N| <= 0.3 (not 2 E_g)",
    abs(num(bN) - 0.188) < 2e-3 and abs(num(nfail) - 2.1) < 0.01 and abs(num(wf[0]) - 6.75) < 0.05 and abs(num(wf[1]) - 9.0) < 0.05
    and num(wf[0]) > 2*1.17*2, f"omega_fail in [{num(wf[0],3)}, {num(wf[1],3)}] eV")

# ---------------------------------------------------------------- C19 phonon shot-noise Fano estimates (L23 (iii), [E, inconsistent model])
fsi = (Q(3749, 1000)/Q(116, 100) - 1)*Q(63, 1000)/Q(116, 100)
fge = (Q(296, 100)/Q(73, 100) - 1)*Q(37, 1000)/Q(73, 100)
a_k = Q(3, 2)*Q(116, 100); res_var = Q(12, 175)*a_k**2            # per-carrier residual variance 12a^2/175, Si
shot = [Q(63, 1000)*hp for hp in (Q(1, 4), Q(1, 2))]               # R9 (VER-WP5-B N1): omega0 x phonon heat per carrier (0.25-0.5 eV)
rep("WP5v3-C19 F_shot = 0.121 (Si), 0.155 (Ge); residual var 0.21 eV^2 >> omega0 x phonon heat 0.016-0.032 eV^2 (inconsistent model)",
    abs(num(fsi) - 0.121) < 1e-3 and abs(num(fge) - 0.155) < 1e-3 and abs(num(res_var) - 0.208) < 0.01
    and abs(num(shot[0]) - 0.0158) < 5e-4 and abs(num(shot[1]) - 0.0315) < 5e-4 and res_var > 5*shot[1],
    f"res {num(res_var,3)}, shot {num(shot[0],3)}-{num(shot[1],3)} eV^2")

# ---------------------------------------------------------------- C20 absorbed phonons and the Migdal/GS moment bookkeeping (sec. 3.1)
w1, w2, wa, nc1, nc2, na = symbols('w1 w2 wa n1 n2 na', positive=True)
rho = [(w1, nc1), (w2, nc2), (-wa, na)]
heat_net = sum(wv*nv for wv, nv in rho); heat_abs = sum(abs(wv)*nv for wv, nv in rho)
rep("WP5v3-C20a omega' < 0 = absorption: H = int omega' rho (net), != int |omega'| rho", simplify(heat_abs - heat_net - 2*wa*na) == 0)
# C20b (replaced; R7 A-V18, B-V11): exact bare-mass f-sum = GS + X; X events carry omega_e AND the recoil q^2/2M
qq, MM, dM, Pm = symbols('q M_kappa deltaM P_Mig', positive=True)
EMig = qq**2*dM/(2*MM**2)
fsum = qq**2/(2*MM)
M1X = EMig + Pm*qq**2/(2*MM)                     # impulse regime: Migdal events carry electronic energy + recoil
M1GS_exact = fsum - M1X
M1GS_presc = (1 - Pm)*qq**2/(2*(MM + dM))        # prescription: (1 - P_Mig) S^GS with M -> M + delta M
eps_ = symbols('epsilon', positive=True)
resid = sp.series((M1GS_presc - M1GS_exact).subs({dM: eps_*dM, Pm: eps_*Pm}), eps_, 0, 3).removeO()
lead = sp.expand(resid.coeff(eps_, 2))
rep("WP5v3-C20b (1-P_Mig) S^GS with M+dM reproduces f-sum - E_Mig - P_Mig q^2/2M to 2nd order (P dM, dM^2)",
    simplify(resid.coeff(eps_, 1)) == 0 and simplify(lead - qq**2*(Pm*dM/MM**2 + dM**2/MM**3)/2) == 0, f"residual O(eps^2): {simplify(lead)}")
# C20c (replaced): sizes. P_Mig ~ 2 m_e (m_e/M) E_R <r^2> [E, REF-A form, <r^2> = 1 A^2]; deltaM/M = 14 m_e/M
r2A = 1/hc**2
PMig = lambda ER: 2*me*(me/MSi)*ER*r2A
dMM = 14*me/MSi
Ecross = sp.solve(sp.Eq(2*me*(me/MSi)*symbols('x')*r2A, dMM), symbols('x'))[0]
rep("WP5v3-C20c P_Mig(1 keV) ~ 5e-3, (10 keV) ~ 5e-2 >> deltaM/M = 2.7e-4; crossover E_R ~ 53 eV [E]",
    abs(num(PMig(1000)) - 5.1e-3) < 2e-4 and abs(num(PMig(10000)) - 5.1e-2) < 2e-3 and abs(num(dMM) - 2.73e-4) < 2e-6 and abs(num(Ecross) - 53) < 2,
    f"P_Mig(1keV) = {num(PMig(1000),3)}, dM/M = {num(dMM,3)}, E_cross = {num(Ecross,3)} eV")

# ================================================================ new checks (R8 derivations)
# C21 local fields (R7 B-V1(ii)): W = eps^-1 v (right), not v eps^-1; kernel = Im(rho^dag W rho) = rho^dag[(W - W^dag)/2i]rho
v1, v2 = symbols('v1 v2', positive=True)
chi = sp.Matrix(2, 2, symbols('x11 x12 x21 x22'))
Vd = sp.diag(v1, v2); epsinv = sp.eye(2) + Vd*chi; Wtrue = Vd + Vd*chi*Vd
rep("WP5v3-C21a W_{GG'} = eps^-1_{GG'} v_C(p+G'); v_C(p+G) eps^-1_{GG'} differs unless v1 = v2",
    simplify(epsinv*Vd - Wtrue) == sp.zeros(2) and simplify((Vd*epsinv - Wtrue).subs(v2, v1)) == sp.zeros(2)
    and simplify(Vd*epsinv - Wtrue) != sp.zeros(2))
wr = symbols('w_r0:4', real=True); wi = symbols('w_i0:4', real=True); rr = symbols('r_r0:2', real=True); ri = symbols('r_i0:2', real=True)
Wc = sp.Matrix(2, 2, [wr[k] + I*wi[k] for k in range(4)]); rv = sp.Matrix([rr[0] + I*ri[0], rr[1] + I*ri[1]])
quad = sp.expand((rv.H*Wc*rv)[0]); aH = (Wc - Wc.H)/(2*I)
quad_aH = sp.expand((rv.H*aH*rv)[0]); quad_elem = sp.expand((rv.H*Wc.applyfunc(sp.im)*rv)[0])
rep("WP5v3-C21b Im(rho^dag W rho) = rho^dag[(W-W^dag)/2i]rho (real); element-wise Im W differs for non-symmetric W",
    simplify(sp.im(quad) - quad_aH) == 0 and simplify(sp.im(quad_aH)) == 0 and simplify(quad_elem - quad_aH) != 0)

# C22 thermal factors (R7 A-V1a, B-V1(i)): (W1) = Gamma_out ~ (1-f)(1+n_B); 2|Im Sigma| ~ 1 - f + n_B = Gamma_out + Gamma_in
fo, bo = symbols('f beta_omega', positive=True); nB = 1/(exp(bo) - 1)
rep("WP5v3-C22 1/(1-e^{-bw}) = 1+n_B; (1-f)(1+n_B) + f n_B = 1 - f + n_B (in-scattering term f n_B)",
    simplify(1/(1 - exp(-bo)) - (1 + nB)) == 0 and simplify((1 - fo)*(1 + nB) + fo*nB - (1 - fo + nB)) == 0)

# C23 (H-t)/(H-m) (R7 A-V4): branching fixed points; minimal non-negative root = termination probability
sG = symbols('s'); pG = symbols('p', positive=True)
roots = sp.solve(sp.Eq((1 - pG) + pG*sG**2, sG), sG)
r_hi = [r for r in roots if simplify(r - 1) == 0]; r_lo = [r for r in roots if simplify(r - 1) != 0][0]
rep("WP5v3-C23 GW f(s)=(1-p)+p s^2: roots 1 and (1-p)/p; p=3/4 -> minimal root 1/3 < 1 (no a.s. termination)",
    len(r_hi) == 1 and simplify(r_lo - (1 - pG)/pG) == 0 and r_lo.subs(pG, Q(3, 4)) == Q(1, 3) and r_lo.subs(pG, Q(1, 4)) > 1)

# C24 renewal hypotheses (R7 A-V8, B-V18)
dlt, Ev = symbols('d E', positive=True); kk = symbols('k', integer=True, nonnegative=True)
mE_lat = sp.floor(Ev/dlt)                  # deterministic (lattice) loss d: counts
osc = [simplify((mE_lat - Ev/dlt).subs(Ev, dlt*(k_ + Q(1, 2)))) for k_ in range(1, 6)]
Wm, Wmin = symbols('W W_min', positive=True)
sec_mom = integrate(Wm**2*Wm**-2, (Wm, Wmin, Ev/2))
rep("WP5v3-C24 lattice loss: m(E) - E/d = -1/2 at E = (k+1/2)d for all k (periodic, not o(1)); W^-2 tail: int W^2 dF ~ E/2",
    all(o == -Q(1, 2) for o in osc) and simplify(sec_mom - (Ev/2 - Wmin)) == 0)

# C25 (B2) densities (R7 A-V5, B-V6) [E]
n_sphere = 300/(Q(4, 3)*pi*(Q(1, 10**6))**3); n_cube = 300/(Q(1, 10**6))**3
aX = Q(4, 10**7)                                        # a_X ~ 4 nm [UNVERIFIED]
rep("WP5v3-C25 300 pairs: 7.2e19 (r=10 nm), 3e20 (10 nm cube) cm^-3; n a_X^3 = 4.6, 19; Pauli occupation 3e20/1e22 = 3%",
    abs(num(n_sphere/10**19) - 7.16) < 0.02 and n_cube == 3*10**20 and abs(num(n_sphere*aX**3) - 4.58) < 0.05
    and abs(num(n_cube*aX**3) - 19.2) < 0.1 and n_cube/10**22 == Q(3, 100), f"{num(n_sphere,3)}, {num(n_cube,3)}")

# C26 L20: under approximation (D) the cross term vanishes identically (R9: the dsigma_n-weighted <T_n> argument is withdrawn, VER-WP5-A N1)
Tn, Te, w_n, w_e = symbols('T_n T_e w_n w_e', positive=True)
# (D): the collision measure is a mixture of purely nuclear (T_e = 0) and purely electronic (T_n = 0) events with weights w_n, w_e
cross = w_n*(Tn*0) + w_e*(0*Te)
gen = w_n*Tn*Te                                                    # a correlated event (both nonzero) would contribute
rep("WP5v3-C26 (D) => int T_n Sum T_e dsigma_{n,e} = 0 identically; nonzero only with correlated events (not in (D))",
    cross == 0 and simplify(gen) != 0)

# C27 undamped plasmon pole carries the whole f-sum (R7 B-V3): -1/eps = -w^2/(w^2 - wp^2); Im part at w+i0 = pi*Res delta
ww, wp = symbols('w w_p', positive=True)
resid_pl = sp.residue(ww**2/(ww**2 - wp**2), ww, wp)
rep("WP5v3-C27 q->0 Drude/RPA pole: Im[-1/eps] = (pi w_p/2) delta(w - w_p); first moment = pi w_p^2/2 = f-sum (q -> 0 only)",
    simplify(resid_pl - wp/2) == 0 and simplify(wp*pi*resid_pl - pi*wp**2/2) == 0)

# C28 R&K "temperature only through E_g(T)" is CONFIRMED; URF T-dependence check: thermal factor of (W1) at omega>0, T->0 -> 1
rep("WP5v3-C28 (1-e^{-beta omega})^{-1} -> 1 (T -> 0, omega > 0); -> T/omega (T >> omega): T-dependence beyond E_g(T)",
    sp.limit(1/(1 - exp(-bo)), bo, oo) == 1 and sp.limit(bo/(1 - exp(-bo)), bo, 0) == 1)

# C29 K_nu sum: first-emission probabilities sum to Gamma^ph/Gamma^tot with the Fano term
Gt = symbols('Gamma_tot', positive=True)
Ksum = sum((Gi + f)/Gt for Gi, f in zip(Gv, Fv))
rep("WP5v3-C29 sum_nu K_nu = Gamma^ph/Gamma^tot (Fano term redistributes only)", simplify(Ksum - Gs/Gt) == 0)

# C30 (W14) identity with an exciton offset: E_g -> E_g - E_x^b leaves the form of (W14) unchanged (consistency of sec. 1.2 remark)
Exb = symbols('E_xb', positive=True); Egp = Eg - Exb
Nb2 = (w - mH)/Egp
rep("WP5v3-C30 (W14) holds with E_g -> E_g - E_x^b (exciton counting)",
    simplify((vH/Egp**2)/Nb2 - ((w/Nb2)/Egp - 1)*vH/(Egp*mH)) == 0)

print(f"\n{sum(RES)}/{len(RES)} PASS")
