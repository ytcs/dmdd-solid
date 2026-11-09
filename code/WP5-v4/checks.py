"""WP5-v4 identity and estimate checks (R13 WP5-ERR: copy of code/WP5-v3/checks.py, C1-C30 unchanged, plus C31-C46 for the
equations changed by the WP7-E-v3 amendment A-1..A-16). Original WP5-v3 header follows.
WP5-v3 identity and estimate checks (R8 revision of code/WP5-v2/checks.py after the R7 hostile review).
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

# ================================================================ R13 (WP5-v4): checks for the equations changed by A-1..A-16 of WP7-E-v3
# Names follow NOTATION "Rows added WP7-E": delta_coll, r_coll, g_Luke, y_ion, kappa_cal, X^oth, q-mark (frak q), m_ind, Delta E_X^b.
import mpmath as mp
mp.mp.dps = 30

# C31 (A-1, A-2, A-10; WP7-E-v3 (E1-pr) -> (E1-W4)): per-carrier deposits, each carrier once, by enumeration of fates
Ec, Ev, mu, Ete, Eth, Egs, Exb = symbols('E_c E_v mu_F E_tr_e E_tr_h E_g E_xb', real=True)
Eg_rel = Ec - Ev
ok_id, ok_mu, ok_neq, ok_once = True, True, False, True
for npairs in (1, 2, 3):
    for fe in itertools.product((0, 1), repeat=npairs):          # 1 = electron captured before t_pr
        for fh in itertools.product((0, 1), repeat=npairs):      # 1 = hole captured before t_pr
            for NX in range(0, npairs + 1):                        # bound pairs (post-prompt in practice; algebra kept general)
                Ntr_e, Ntr_h = sum(fe), sum(fh)
                Nf_e, Nf_h = npairs - Ntr_e, npairs - Ntr_h
                if NX > min(Nf_e, Nf_h): continue
                Nf_e_unb, Nf_h_unb = Nf_e - NX, Nf_h - NX          # unbound free carriers
                # route 1: sum of per-carrier deposits (mu_F referenced) + exciton reservoir E_X = N_X(E_g - E_x^b)
                dep = Nf_e_unb*(Ec - mu) + Nf_h_unb*(mu - Ev) + Ntr_e*(Ec - Ete - mu) + Ntr_h*(mu - Ev - Eth) + NX*(Eg_rel - Exb)
                # route 2: (E1-W4) right-hand side: N_eh E_g + E_pairs^unp + E_trap^pr + Delta E_X^b, N_eh = N_e^f(unbound) + N_X
                Neh = Nf_e_unb + NX
                Etrap = Ntr_e*(Ec - Ete - mu) + Ntr_h*(mu - Ev - Eth)
                Eunp = (Nf_h_unb - Nf_e_unb)*(mu - Ev)
                rhs = Neh*Eg_rel + Eunp + Etrap + (-NX*Exb)
                ok_id &= sp.expand(dep - rhs) == 0
                ok_mu &= sp.diff(sp.expand(Eunp + Etrap), mu) == 0      # neutrality (pairs born together) => mu_F-independent
                if (Ntr_e or Ntr_h) and Nf_e_unb != Nf_h_unb: ok_neq = True   # N_e^f != N_h^f with capture
                # once-per-carrier closure: a captured edge electron carries E_c - mu: E_trap deposit + capture heat E_tr = E_c - mu
                ok_once &= sp.expand((Ec - Ete - mu) + Ete - (Ec - mu)) == 0
dbl = sp.expand((Ec - mu) + (Ec - Ete - mu) + Ete)            # v2 wording: free deposit AND trap deposit for the same carrier
rep("WP5v4-C31 (E1-pr) per-carrier sum = N_eh E_g + E_pairs^unp + E_trap^pr + DeltaE_X^b (all fates, n<=3); mu_F-free; N_e^f != N_h^f with capture; double count = 2(E_c - mu)",
    ok_id and ok_mu and ok_neq and ok_once and sp.expand(dbl - 2*(Ec - mu)) == 0)
# counter-example: without neutrality (one extra hole injected) the same combination depends on mu_F
rep("WP5v4-C31b without neutrality d(E_pairs^unp + E_trap)/dmu_F = N_h - N_e != 0 (mu_F is physical only once carriers are collected)",
    all(sp.diff((nh_f - ne_f)*(mu - Ev) + ne_t*(Ec - Ete - mu) + nh_t*(mu - Ev - Eth), mu) == (nh_f + nh_t) - (ne_f + ne_t) != 0
        for ne_f, ne_t, nh_f, nh_t in [(1, 0, 2, 0), (0, 1, 2, 0), (2, 1, 1, 1)]))

# C32 (A-10): (W14) with H -> H_eff = H + E_trap^pr + E_es + E_pairs^unp + DeltaE_X^b - W_bias(t_pr); brute force over a discrete law
w14 = Q(100)                                                    # omega (eV), fixed
Egv = Q(117, 100)
laws = {Q(20): Q(1, 4), Q(21): Q(1, 2), Q(22): Q(1, 4)}       # P(N_eh)
Heff = {n_: w14 - n_*Egv for n_ in laws}                        # omega = N_eh E_g + H_eff exactly (E_st = E_esc = 0)
nbar = sum(p*n_ for n_, p in laws.items()); varN = sum(p*(n_ - nbar)**2 for n_, p in laws.items())
mH = sum(p*Heff[n_] for n_, p in laws.items()); vH = sum(p*(Heff[n_] - mH)**2 for n_, p in laws.items())
Feh_direct = varN/nbar; epsv = w14/nbar
Feh_w14 = (epsv/Egv - 1)*vH/(Egv*mH)
# the same law read with H alone (H = H_eff - E_trap^pr, E_trap^pr fluctuating with N) fails
Etr_n = {n_: Q(3, 10)*(22 - n_) for n_ in laws}
Hbare = {n_: Heff[n_] - Etr_n[n_] for n_ in laws}
mHb = sum(p*Hbare[n_] for n_, p in laws.items()); vHb = sum(p*(Hbare[n_] - mHb)**2 for n_, p in laws.items())
rep("WP5v4-C32 (W14) exact with H_eff (brute force: Var N/nbar = (eps_eh/E_g - 1) d_H[H_eff]); with bare H and fluctuating E_trap^pr it fails",
    simplify(Feh_direct - Feh_w14) == 0 and simplify(Feh_direct - (w14/nbar/Egv - 1)*vHb/(Egv*mHb)) != 0,
    f"F_eh = {num(Feh_direct)}")

# C33 (A-4): multiplicative Y_H; absolute eps_prim cancels; first-order bracket; E_st(t_win) decomposition by a master equation
ep, dc, DN, DE, om, rc, gL, yi = symbols('epsilon_prim delta_coll Dp_NR Dp_ER omega r_coll g_Luke y_ion', positive=True)
tt = symbols('t', positive=True)
YH = (ep*(1 - dc)*(om - DN))/(ep*(om - DE))
YH1 = sp.series(YH.subs({dc: tt*dc, DN: tt*DN, DE: tt*DE}), tt, 0, 2).removeO().subs(tt, 1)
rep("WP5v4-C33a Y_H = (1-delta_coll)(omega-D'_NR)/(omega-D'_ER): eps_prim cancels; first order 1 - delta_coll - (D'_NR - D'_ER)/omega",
    sp.diff(YH, ep) == 0 and simplify(sp.expand(YH1) - (1 - dc - (DN - DE)/om)) == 0)
YN = (ep*(1 - dc)*(om - DN) + ep*rc*gL*yi*om)/(ep*(om - DE) + ep*rc*gL*om)
rep("WP5v4-C33b NTL mode: eps_prim cancels; zero deficits, r_coll = 1: (1 + y_ion g_Luke)/(1 + g_Luke); unit quenching delta=0, D'_NR=D'_ER: Y_H = 1",
    simplify(sp.diff(YN, ep)) == 0 and simplify(YN.subs({dc: 0, DN: 0, DE: 0, rc: 1}) - (1 + yi*gL)/(1 + gL)) == 0
    and simplify(YH.subs({dc: 0, DN: DE})) == 1)
# master equation: seed c (E_c) -> 0 (rate G1, recombined, E=0) or -> b (rate G2, frozen, E_b); <E_st(t)> = sum N_i E_i
G1, G2, Ecv, Ebv = Q(3), Q(1), Q(8), Q(5)
Nc = lambda t_: exp(-(G1 + G2)*t_)
Nb = lambda t_: G2/(G1 + G2)*(1 - exp(-(G1 + G2)*t_))
Est = lambda t_: Nc(t_)*Ecv + Nb(t_)*Ebv
tw, to = Q(1, 5), Q(4)
Erel = Ecv - Est(to); Eunrel = Est(to); Prel = (Ecv - Est(tw))/Erel
rep("WP5v4-C33c <E_st(t_win)> = E_st^unrel(t_obs) + E_st^rel (1 - P_rel(t_win)) (two-exit chain, exact)",
    simplify(Est(tw) - (Eunrel + Erel*(1 - Prel))) == 0, f"P_rel = {num(Prel)}")

# C34 (A-4, A-9; WP7-E-v3 (E13)): eta^phi_NR from the two-channel calibration PROCEDURE (1803.02903 Eq. (1)), not from the closed forms
dNp, dEp = symbols('dprime_NR dprime_ER', real=True)
def Esig(ep_, dc_, dprime, ytrue):     # signal per unit omega: primary phonons (1-delta)(1-d') + NTL phonons r g y (eps_prim factored)
    return ep_*((1 - dc_)*(1 - dprime) + rc*gL*ytrue)
c_phi = (1 + gL)/Esig(ep, 0, dEp, 1)              # phonon scale fixed on ER (unity yield): c_phi Esig_ER - g_Luke*1 = 1
eta = c_phi*Esig(ep, dc, dNp, yi) - gL*yi         # NR: E_R^rec/omega = E_phi - E_Q eV_b/eps_eh, E_Q = y_ion omega
eta0 = simplify(eta.subs({dc: 0, dNp: 0, dEp: 0}))
kap = (1 + yi*gL)/(1 + gL)
lin = sp.expand(sp.series(eta.subs({dc: tt*dc, dNp: tt*dNp, dEp: tt*dEp}), tt, 0, 2).removeO().subs(tt, 1))
lin_r1 = sp.expand(lin.subs(rc, 1))
rep("WP5v4-C34a eta^phi_NR independent of eps_prim; eta_0 = 1 + g(1-r)(1-y)/(1+rg); r=1 first order: 1 - delta - d'_NR + kappa_cal d'_ER",
    simplify(sp.diff(eta, ep)) == 0 and simplify(eta0 - (1 + gL*(1 - rc)*(1 - yi)/(1 + rc*gL))) == 0
    and simplify(lin_r1 - (1 - dc - dNp + kap*dEp)) == 0)
cd_, cN_, cE_ = [simplify(lin.coeff(v)) for v in (dc, dNp, dEp)]
rep("WP5v4-C34b general r_coll, first order: coefficients -(1+g)/(1+rg) on delta, d'_NR and +(1+g)(1+rgy)/(1+rg)^2 on d'_ER (= 1, kappa_cal only at r=1)",
    simplify(cd_ + (1 + gL)/(1 + rc*gL)) == 0 and simplify(cN_ + (1 + gL)/(1 + rc*gL)) == 0
    and simplify(cE_ - (1 + gL)*(1 + rc*gL*yi)/(1 + rc*gL)**2) == 0)
vals = {gL: Q(4)/Q(382, 100), yi: Q(3, 10), rc: Q(1144, 1000)}
cvals = [num(-cd_.subs(vals), 4), num(cE_.subs(vals), 4), num(kap.subs(vals), 4)]
rep("WP5v4-C34c numbers: g_Luke = 4/3.82 = 1.047; kappa_cal(y=0.3) = 0.642; at r_coll = 1.144: 0.931 (delta, d'_NR), 0.576 (d'_ER)",
    abs(num(vals[gL]) - 1.047) < 1e-3 and abs(cvals[2] - 0.642) < 1e-3 and abs(cvals[0] - 0.931) < 1e-3 and abs(cvals[1] - 0.576) < 1e-3,
    f"{cvals}")
e0 = lambda yy, rr: 1 + vals[gL]*(1 - rr)*(1 - yy)/(1 + rr*vals[gL])
rng = [num(e0(Q(22, 100), Q(1144, 1000)), 4), num(e0(Q(35, 100), Q(1144, 1000)), 4)]
rep("WP5v4-C34d degeneracy: r_coll = 1.144 alone gives eta_0 = 0.952 (y = 0.3); y = 0.22..0.35 gives 0.947..0.955",
    abs(num(e0(Q(3, 10), Q(1144, 1000))) - 0.952) < 5e-4 and abs(rng[0] - 0.947) < 6e-4 and abs(rng[1] - 0.955) < 6e-4, f"{rng}")
sE = symbols('s_st', positive=True)       # E_st/omega with delta = 0, X^oth = 0: d'_NR = s, d'_ER = 0
lhs = 1 - lin.subs({dc: 0, dNp: sE, dEp: 0}) - sE
rep("WP5v4-C34e (B-d): 1 - eta - E_st/omega = g(r-1)[(1-y) - E_st/omega]/(1+rg) at first order (general r): bound needs E_st/omega <= 1-y",
    simplify(lhs - gL*(rc - 1)*((1 - yi) - sE)/(1 + rc*gL)) == 0)

# C35 (A-9; WP7-E-v3 sec. 3.2): bound arithmetic (95% C.L.), NRT reading, Delta ZPE shift (<= 1% [E])
bSi = Q(48, 1000) + Q(7, 1000); bGe = Q(608, 10000) + 2*Q(18, 10000)
ps = [bSi/(Q(4, 10)*Q(65, 100)), bGe/(Q(4, 10)*Q(8, 10))]
pv = [ps[0]/Q(9, 20), ps[1]/(Q(6)/Q(197, 10))]
rep("WP5v4-C35 bounds 0.055 (Si), 0.064 (Ge); p_surv E_st,1/E_d <= 0.21/0.20; p_surv <~ 0.47/0.66; x1.01 (Delta ZPE): 0.056/0.065, 0.48/0.67",
    bSi == Q(55, 1000) and bGe == Q(644, 10000) and abs(num(ps[0]) - 0.2115) < 1e-3 and abs(num(ps[1]) - 0.2013) < 1e-3
    and abs(num(pv[0]) - 0.470) < 1e-3 and abs(num(pv[1]) - 0.661) < 1e-3
    and abs(num(bSi*Q(101, 100)) - 0.0556) < 1e-4 and abs(num(bGe*Q(101, 100)) - 0.0650) < 1e-4
    and abs(num(pv[0]*Q(101, 100)) - 0.475) < 1e-3 and abs(num(pv[1]*Q(101, 100)) - 0.667) < 1e-3,
    f"{[num(p_) for p_ in ps]}, {[num(p_) for p_ in pv]}")

# C36 (A-10; WP7-E-v3 (E12)): F_meas^obs by brute-force enumeration over positions, N_eh and per-carrier marks frak-q
def law_sum(PN, marks):            # exact distribution of sum of N iid marks; marks: {value: prob}
    dist = {}
    for N_, pN in PN.items():
        for combo in itertools.product(marks.items(), repeat=N_):
            val = sum(c[0] for c in combo); pr = pN
            for c in combo: pr *= c[1]
            dist[val] = dist.get(val, 0) + pr
    return dist
PN = {1: Q(1, 5), 2: Q(1, 2), 3: Q(3, 10)}
pos = [(Q(1, 3), {Q(1): Q(9, 10), Q(1, 2): Q(1, 20), Q(0): Q(1, 20)}), (Q(2, 3), {Q(1): Q(1, 2), Q(1, 2): Q(1, 4), Q(0): Q(1, 4)})]
tot = {}
for wr, mk in pos:
    for v_, p_ in law_sum(PN, mk).items(): tot[v_] = tot.get(v_, 0) + wr*p_
mean_ = sum(v_*p_ for v_, p_ in tot.items()); var_ = sum((v_ - mean_)**2*p_ for v_, p_ in tot.items())
nb = sum(n_*p_ for n_, p_ in PN.items()); FN = sum((n_ - nb)**2*p_ for n_, p_ in PN.items())/nb
mr = [sum(v_*p_ for v_, p_ in mk.items()) for _, mk in pos]; vr = [sum((v_ - m_)**2*p_ for v_, p_ in mk.items()) for (_, mk), m_ in zip(pos, mr)]
wv = [wr for wr, _ in pos]
m1 = sum(w_*m_ for w_, m_ in zip(wv, mr)); m2 = sum(w_*m_**2 for w_, m_ in zip(wv, mr)); vbar = sum(w_*v_ for w_, v_ in zip(wv, vr))
Fobs = (FN*m2 + vbar)/m1 + nb*(m2 - m1**2)/m1
ed1 = Q(9, 10); single = law_sum(PN, {Q(1): ed1, Q(0): 1 - ed1})
ms = sum(v_*p_ for v_, p_ in single.items()); vs_ = sum((v_ - ms)**2*p_ for v_, p_ in single.items())
rep("WP5v4-C36 F_meas^obs = [F_eh<m_ind^2> + <Var frak-q>]/<frak-q> + <N_eh>Var_r(m_ind)/<frak-q> (exact enumeration); single position -> eps_det F_eh + 1 - eps_det",
    simplify(var_/mean_ - Fobs) == 0 and simplify(vs_/ms - (ed1*FN + 1 - ed1)) == 0, f"F_obs = {num(Fobs)}")

# C37 (A-11; WP6-v3 (5.1'')): theta_tr^pr = type T on a two-point measure
th, f0s, psis = symbols('theta f_0 psi', positive=True)
flog = f0s*exp(th*psis)/(f0s*exp(th*psis) + 1 - f0s)
lam0 = -log((1 - f0s) + f0s*exp(th*psis))          # zeroth-moment (normalisation) multiplier of the (5.1'') tilt
tilt1 = f0s*exp(th*psis + lam0)                      # S_c(1) exp(theta psi phi(1) + lambda_0), phi(1) = 1, phi(0) = 0
f1 = flog.subs({f0s: Q(1, 1000), psis: log(Q(1009, 100)), th: 1})
rep("WP5v4-C37 two-point type T = (5.1'') tilt with only the zeroth-moment constraint; f_0 = 1e-3, psi = ln 10.09: f(1) = 1.00%; f_0 = 0 never moves",
    simplify(tilt1 - flog) == 0 and abs(num(f1, 6) - Q(1, 100)) < 1e-5 and simplify(flog.subs(f0s, 0)) == 0, f"f(1) = {num(f1, 5)}")

# C38 (T-1 conditions (i), (iv), (v) against the sourced (W12)): two seeds, uphill hop, absorbing B0; leak counter-example; ZPE sum rule
Econf = [mp.mpf(0), mp.mpf(8), mp.mpf(6), mp.mpf(5)]       # 0 = B0 (recombined), 1 = seed c, 2 = close pair a, 3 = separated pair b
ZPE = [mp.mpf(0), mp.mpf('0.10'), mp.mpf('0.08'), mp.mpf('0.12')]
def run(leak):
    Gm = mp.matrix(4, 4)                                    # Gm[i, j] = Gamma_ij (i -> j)
    Gm[1, 0], Gm[1, 2], Gm[2, 1], Gm[2, 0], Gm[2, 3], Gm[3, 0] = 2, 1, mp.mpf('0.5'), 1, mp.mpf('0.3'), mp.mpf('0.05')  # 2->1 uphill
    A = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            if i != j: A[j, i] += Gm[i, j]; A[i, i] -= Gm[i, j]
    A[2, 2] -= leak                                          # loss from state 2 to an UNLISTED state (violates (iv))
    N0 = mp.matrix([0, mp.mpf('0.7'), mp.mpf('0.3'), 0])     # two seeds (classes c and a), linear superposition, delta sources at t = 0
    Nt = lambda t_: mp.expm(A*t_)*N0
    flux = lambda t_, tab: sum(Nt(t_)[i]*Gm[i, j]*(tab[i] - tab[j]) for i in range(4) for j in range(4) if i != j)
    T = mp.mpf(3)
    lhs_ = mp.quad(lambda t_: flux(t_, Econf), [0, 1, T])
    rhs_ = sum(N0[i]*Econf[i] for i in range(4)) - sum(Nt(T)[i]*Econf[i] for i in range(4))
    lz = mp.quad(lambda t_: flux(t_, ZPE), [0, 1, T]); rz = sum(N0[i]*ZPE[i] for i in range(4)) - sum(Nt(T)[i]*ZPE[i] for i in range(4))
    return lhs_, rhs_, lz, rz
l0, r0, lz0, rz0 = run(0); l1, r1, _, _ = run(mp.mpf('0.4'))
rep("WP5v4-C38 sourced (W12): int E R_rel = sum s_i E^conf_i - sum N_i(t) E^conf_i (uphill hop, two seeds, B0 listed); ZPE sum rule separately; a leak breaks it",
    abs(l0 - r0) < mp.mpf('1e-20') and abs(lz0 - rz0) < mp.mpf('1e-20') and abs(l1 - r1) > mp.mpf('1e-2'), f"leak defect {mp.nstr(r1 - l1, 4)} eV")

# C39 (A-3 reading, T-1 condition (ii)): E^ad_0(R_I(0)) for a Wigner-sampled lattice exceeds the basin minimum by ~3<omega>/4 per atom
xq, Mq, wq = symbols('x M w_q', positive=True)
psi0sq = sqrt(Mq*wq/pi)*exp(-Mq*wq*xq**2)                 # |psi_0|^2, hbar = 1
Vmean = integrate(Q(1, 2)*Mq*wq**2*xq**2*psi0sq, (xq, -oo, oo))
per_atom = 3*Q(45, 1000)/4                                  # eV, <omega> = 45 meV (WP5v3-C7c)
rep("WP5v4-C39 harmonic T=0: <V> = omega/4 per mode; 3<omega>/4 = 34 meV per atom; 4096-atom cell: 138 eV >> E_st (7-9 eV): both ends must be quenched",
    simplify(Vmean - wq/4) == 0 and abs(num(per_atom*4096) - 138.2) < 0.1, f"{num(per_atom*4096)} eV")

# C40 (A-12; WP7-E-v3 C15): bias work before t_pr = e E_b v_d t_pr [E]
wb = lambda Ef, vd, tp: Ef*vd*tp                             # V/cm * cm/s * s = eV per unit charge
rep("WP5v4-C40 pre-t_pr bias work: 4 V/cm, 1e6 cm/s, 100 ps -> 4e-4 eV; 250 V/cm, 1e7 cm/s -> 0.25 eV per carrier",
    wb(4, 10**6, Q(1, 10**10)) == Q(4, 10**4) and wb(250, 10**7, Q(1, 10**10)) == Q(1, 4))

# C41 (A-6; WP7-E-v3 (E14)): one visibility criterion eps_coll (eps^hop + dZPE) >= E_thr^det
ecoll = Q(3, 10)
rep("WP5v4-C41 single Frenkel pair: 0.3 x 9 eV = 2.7 eV < 3 eV (sub-threshold for E_thr^det > 3 eV, also with dZPE ~0.1 eV); pocket at 16.3 eV: N_a >~ 272 (0.2 eV/atom)",
    ecoll*9 == Q(27, 10) and ecoll*(9 + Q(1, 10)) < 3 and abs(num(Q(163, 10)/(ecoll*Q(2, 10))) - 271.7) < 0.1)

# C42 (A-4, Theorem E-3 of WP7-E-v3): mu_F-referenced trap energies; Delta E_trap may be negative
rep("WP5v4-C42 doubly trapped pair: (E_c - E_tr_e - mu) + (mu - E_v - E_tr_h) = E_g - E_tr_e - E_tr_h (mu-free); singly trapped hole depends on mu_F; Delta E_trap < 0 example",
    sp.expand((Ec - Ete - mu) + (mu - Ev - Eth) - (Eg_rel - Ete - Eth)) == 0 and sp.diff(mu - Ev - Eth, mu) == 1
    and Q(1, 10)*(20 - 26)*(Q(117, 100) - Q(3, 10)) < 0)

# C43 (A-16): (W6) cascade-level P_casc is the t = t_pr marginal of P(M, t | Lambda) = sum_N P_casc(N) P_det(M, t | N)
Pc = {0: Q(1, 4), 1: Q(1, 2), 2: Q(1, 4)}
Pdet_tpr = lambda M_, N_: 1 if M_ == N_ else 0             # detector stage at t = t_pr is the identity
Pdet_t = lambda M_, N_: sp.binomial(N_, M_)*Q(9, 10)**M_*Q(1, 10)**(N_ - M_) if M_ <= N_ else 0
PM_tpr = {M_: sum(Pc[N_]*Pdet_tpr(M_, N_) for N_ in Pc) for M_ in Pc}
PM_t = {M_: sum(Pc[N_]*Pdet_t(M_, N_) for N_ in Pc) for M_ in Pc}
rep("WP5v4-C43 (E3) at t = t_pr reduces to P_casc (marginal); at t > t_pr it is normalised and differs",
    PM_tpr == Pc and sum(PM_t.values()) == 1 and PM_t != Pc)

print(f"\n{sum(RES)}/{len(RES)} PASS")
