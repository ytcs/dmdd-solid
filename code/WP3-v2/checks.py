"""WP3-v2 identity checks (R6 revision of R5/WP3, with the consolidated M1/PAER theory).
Sympy only, exact arithmetic (numbers in C9 are evalf of exact expressions; no simulation).
Run:  python3 -I checks.py      Prints PASS/FAIL per check. Labels WP3v2-Cn (CONVENTIONS sec. 14).
C1-C10 keep the meaning of the v1 labels (WP0-v2 cites "WP3 [C1d]"); C11-C23 are new (M1 part, F1, F4, O6-2).
Notation: NOTATION v4 (v^g_n, p_nn, D^n, Xi^n, c_nu, E^Mig_1, E_cv, v_N, y_phi, ...)."""
import sympy as sp
from sympy import I, Rational as Q, Matrix, eye, zeros, sqrt, pi, exp, oo, simplify

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:84s} {note}")
def is0(e):
    if isinstance(e, sp.MatrixBase): return all(is0(x) for x in e)
    return sp.simplify(sp.expand_complex(sp.sympify(e))) == 0
def dag(M): return M.conjugate().T

# ============================================================ C1  X1 soft limit vs WP0 v1 (4.9); C7e branch  [§M8]
q, c, vc, vv, pc, pv, Dc, Dv = sp.symbols('q c_nu vg_c vg_v p_cc p_vv D_c D_v', real=True)
for s in (+1, -1):                                     # +1 = emission of -Q (upper sign), -1 = absorption
    Xc, Xv = Dc + vc*pc, Dv + vv*pv                    # Xi^n = D^n + v^g_n (x) p_nn  (X1 (X2))
    X1p = (q - pc + pv) + Xc/(vc + s*c) - Xv/(vv + s*c)                       # lab form (X1')
    X1 = q + (Dc - s*c*pc)/(vc + s*c) - (Dv - s*c*pv)/(vv + s*c)              # (M.15) = X1 (X1)
    rep(f"WP3v2-C1a lab form (X1') == comoving form (M.15), sign {s:+d}", is0(X1p - X1))
    lab = q + Xc/(vc + s*c) - Xv/(vv + s*c); com = q + Dc/(vc + s*c) - Dv/(vv + s*c)
    rep(f"WP3v2-C1b WP0 v1 (4.9) lab reading - X1 = p_cc - p_vv, sign {s:+d}", is0(lab - X1 - (pc - pv)))
    rep(f"WP3v2-C1c WP0 v1 (4.9) comoving reading - X1 != 0, sign {s:+d}", not is0(com - X1))
    ext = {vc: 0, vv: 0, pc: 0, pv: 0}
    rep(f"WP3v2-C1d both readings agree with X1 at band extrema, sign {s:+d}",
        is0((lab - X1).subs(ext)) and is0((com - X1).subs(ext)))
X1e = (q + (Dc - c*pc)/(vc + c) - (Dv - c*pv)/(vv + c)).subs({Dc: -vc*pc, Dv: -vv*pv})
rep("WP3v2-C1e C7e (Xi = 0, synthetic g = [A,H]) -> D2 form q - p_cc + p_vv", is0(X1e - (q - pc + pv)))

# ============================================================ C2  KKL (5)->(6); (W.5) scalar reduction   [§2 L7b]
al, w, k, V = sp.symbols('alpha omega k V', positive=True)
e2s, e1s = sp.symbols('epsilon_2 epsilon_1', real=True)
sum_rho = e2s*V*k**2/(4*pi**2*al)
kkl5 = (4*pi*al)**2/w**4/k**4*sum_rho/V/(e1s**2 + e2s**2); kkl6 = 4*al/(w**4*k**2)*e2s/(e1s**2 + e2s**2)
rep("WP3v2-C2a KKL 2011.09496 Eq.(5) == Eq.(6) integrand", is0(kkl5 - kkl6))
Z, p, M, qp, L = sp.symbols('Z p M qdotp L', positive=True)
e2 = 4*pi*al
urf = (1/(2*pi))*qp**2*(Z*e2/p**2)**2/(M**2*w**4)*(2*p**2/e2)*L
rep("WP3v2-C2b (W.5) with S_ee=(2p^2/e^2)L, U=Ze^2/p^2 == KKL dP/dw (prefactor 4 alpha)",
    is0(urf - 4*al*Z**2*qp**2/(M**2*w**4*p**2)*L))

# ============================================================ C3  2603.13052 Eq.(4.7) vs KKL               [§2 L7c]
mN, qn = sp.symbols('m_N q', positive=True)
kkl_avg = 4*al*qn**2/(3*mN**2*w**4); bem = 2*al*qn**2/(3*w**4*mN)
rep("WP3v2-C3a 2603.13052 (4.7)/KKL = m_N/2 (dimensionful: typo m_N -> m_N^2, then 1/2)", is0(bem/kkl_avg - mN/2))
rep("WP3v2-C3b with m_N^2 and their dsigma/dq = 2x standard, the rate product is KKL's", is0(2*(bem/mN)/kkl_avg - 1))

# ============================================================ C4  Migdal energy moment = drag mass (HO atom)  [J3]
m, wo, kk = sp.symbols('m omega_0 k', positive=True); n = sp.symbols('n', integer=True, nonnegative=True)
lam = kk**2/(2*m*wo)
Es = sp.summation(n*wo*exp(-lam)*lam**n/sp.factorial(n), (n, 0, oo))
rep("WP3v2-C4a sum_n E_n |<n|e^{-ikx}|0>|^2 = k^2/2m (TRK, exact boost)", is0(Es - kk**2/(2*m)))
dM = 2*(m*wo**2)**2*(1/(2*m*wo))/wo**3
rep("WP3v2-C4b drag mass 2 sum |<n|dV|0>|^2/E_n^3 = m (bound electron fully dragged)", is0(dM - m))
Mn = sp.symbols('M', positive=True)
rep("WP3v2-C4c E^Mig_1 = q^2 dM/(2M^2) (dipole q_e = m q/M)", is0((m*qn/Mn)**2*wo/(2*m*wo) - qn**2*dM/(2*Mn**2)))

# ============================================================ C5  J7 electronic part of M1_eN, exact HO sum    [J7]
Mk, me_, w0, qq = sp.symbols('M m_e omega_0 q', positive=True)
mA = Mk + me_; mu = Mk*me_/mA; aa, bb = Mk/mA, me_/mA; x02 = 1/(2*mu*w0)
# <0|A^dag|n><n|B|0> with A = e^{+i a q rho}, B = e^{-i b q rho}: e^{-(a^2+b^2)q^2x0^2/2} (-a b q^2 x0^2)^n / n!
term = exp(-(aa**2 + bb**2)*qq**2*x02/2)*(-aa*bb*qq**2*x02)**n/sp.factorial(n)
sos = 2*sp.summation(n*w0*term, (n, 0, oo))
F = exp(-qq**2*x02/2)                                  # <e^{-i q rho}> in the HO ground state
rep("WP3v2-C5 electronic part of M1_eN = -(q^2/m_A) F(q)  (exact sum over states)",
    sp.simplify(sp.powsimp(sp.expand_power_exp(sos/(-qq**2/mA*F)))) == 1)

# ============================================================ C6  Williams-Lax vs URF; FC moments            [§5]
nB, Ecv, wq, M2 = sp.symbols('n E_cv omega_Q M2', positive=True)
rep("WP3v2-C6a (W.12): M1(URF) - M1(WL) = omega_Q |M|^2, T-independent",
    is0(M2*((nB + 1)*(Ecv + wq) + nB*(Ecv - wq)) - M2*(2*nB + 1)*Ecv - M2*wq))
S, wp = sp.symbols('S_HR omega_p', positive=True)
P = exp(-S)*S**n/sp.factorial(n)
m1 = sp.simplify(sp.summation(P*n*wp, (n, 0, oo))); m2 = sp.simplify(sp.summation(P*(n*wp)**2, (n, 0, oo)))
m3 = sp.simplify(sp.summation(P*(n*wp - S*wp)**3, (n, 0, oo)))
rep("WP3v2-C6b FC Poisson: exact first moment = Lax vertical S_HR omega_p", is0(m1 - S*wp))
rep("WP3v2-C6c FC Poisson: exact variance = Lax variance S_HR omega_p^2", is0(m2 - m1**2 - S*wp**2))
rep("WP3v2-C6d FC Poisson: third central moment = S_HR omega_p^3 (Lax Gaussian gives 0)", is0(m3 - S*wp**3))

# ============================================================ C7  L7d virtual-phonon propagator             [§2 L7d]
we, wk = sp.symbols('omega_e omega_k', positive=True)
ser = sp.series((1/(2*Mn*wk))*2*wk/(we**2 - wk**2), wk, 0, 4).removeO()
rep("WP3v2-C7 (2M w_k)^-1 2w_k/(w_e^2 - w_k^2) = (M w_e^2)^-1 (1 + w_k^2/w_e^2 + ...)",
    is0(ser - (1/(Mn*we**2))*(1 + wk**2/we**2)))

# ============================================================ C8  crystal bremsstrahlung, atomic limit        [§6]
aw, fw = sp.symbols('alpha_pol f')
Zat = -m*w**2*aw/al
rep("WP3v2-C8a Z*_atom(w) = f(w) given alpha_pol = -alpha f/(m w^2) (Gaussian, 1607.01789)", is0(Zat.subs(aw, -al*fw/(m*w**2)) - fw))
rep("WP3v2-C8b w -> inf: Z* -> Z", is0(Zat.subs(aw, -Z*al/(m*w**2)) - Z))
vN, ER = sp.symbols('v_N E_R', positive=True)
rep("WP3v2-C8c K-P Eq.(8) == (2 alpha/3 pi w) v_N^2 f^2 with v_N^2 = 2E_R/M (n_r = 1)",
    is0((4*al/(3*pi*w)*ER/Mn*fw**2).subs(ER, Mn*vN**2/2) - 2*al/(3*pi*w)*vN**2*fw**2))

# ============================================================ C9  Si/Ge numbers (evalf of exact expressions)  [§2, J3]
amu, meV = Q(931494), Q(510999, 1000)                # keV
MSi, MGe = Q(280855, 10000)*amu, Q(72630, 1000)*amu  # keV
nums = {'q_imp Si [keV] = sqrt(2M*40meV)': sqrt(2*MSi*Q(4, 10**5)), 'q_imp Ge [keV] = sqrt(2M*25meV)': sqrt(2*MGe*Q(25, 10**6)),
        'q_EFT Si [keV] = sqrt(2M*1.12eV)': sqrt(2*MSi*Q(112, 10**5)), 'q_EFT Ge [keV] = sqrt(2M*0.67eV)': sqrt(2*MGe*Q(67, 10**5)),
        'dM/M Si (14 e, upper bound)': 14*meV/MSi, 'dM/M Ge (32 e, upper bound)': 32*meV/MGe,
        'v_N p/w_e (Si; q=100, p=5 keV, w_e=5 eV)': (100/MSi)*5*10**3/5}
for kx, vx in nums.items(): print(f"      C9  {kx:44s} {float(vx):.4g}")
rep("WP3v2-C9 Si EFT bound sqrt(2M E_g) in (230, 260) keV (2210.06490 fn.3: 242)", 230 < float(nums['q_EFT Si [keV] = sqrt(2M*1.12eV)']) < 260)

# ============================================================ C10 dark photon kappa_eff^2 sigma_1 = m Im(-1/eps)  [L9b]
s1, s2, mv = sp.symbols('sigma_1 sigma_2 m_V', positive=True)
Pi = -I*(s1 + I*s2)*mv; epsv = 1 - Pi/mv**2
rep("WP3v2-C10 1608.01994 (6),(7): kappa_eff^2 sigma_1 = kappa^2 m Im(-1/eps)",
    is0(mv**4*s1/((mv**2 - sp.re(Pi))**2 + sp.im(Pi)**2) - mv*sp.im(-1/epsv)))

# ============================================================ C11 Pauli/exchange theorem; q = 0 cancellation   [§M2, C1]
ev, ec, em, wQ, g, r = sp.symbols('e_v e_c e_m omega_Q g rho', real=True)
for s in (+1, -1):
    on = {w: ec - ev + s*wQ}
    Dp = -r*g/(-(ec - em + s*wQ)); Ap = g*r/(ev + w - em)     # path D (sign -1) vs A form
    Cp = -g*r/(w - ec + em);      Bp = r*g/(ev - em - s*wQ)    # path C (sign -1) vs B form
    rep(f"WP3v2-C11a hole path D == A form, m occupied, on shell (sign {s:+d})", is0((Dp - Ap).subs(on)))
    rep(f"WP3v2-C11b hole path C == B form, m occupied, on shell (sign {s:+d})", is0((Cp - Bp).subs(on)))
    gcv = sp.Symbol('g_cv')
    rep(f"WP3v2-C11c q=0: m=v (A) + m=c (B) delta-parts cancel (sign {s:+d})", is0((gcv/(ev + w - ev) + gcv/(ev - ec - s*wQ)).subs(on)))
rep("WP3v2-C11d off shell D != A form (theorem is on-shell only)", not is0(Dp - Ap))

# ============================================================ C12 isotropic halo factor eta/(2q); |f_crys|^2     [(M.6),(M.7)]
vv_, v0, qa, a_ = sp.symbols('v v_0 q a', positive=True); xx = sp.symbols('x', real=True)
fM = exp(-vv_**2/v0**2)                                  # any isotropic speed profile (shape only)
ang = 2*pi*sp.integrate(sp.DiracDelta(qa*vv_*xx - a_), (xx, -1, 1))   # = 2pi/(q v) for v > a/q
ang = sp.simplify(ang.subs(a_, qa*vv_/2))               # a point inside the support
vmin = sp.symbols('v_min', positive=True)
G = sp.integrate(vv_**2*fM*2*pi/(qa*vv_), (vv_, vmin, oo))
eta = sp.integrate(4*pi*vv_**2*fM/vv_, (vv_, vmin, oo))
rep("WP3v2-C12a angular integral 2pi int dx delta(q v x - a) = 2pi/(q v) inside support", is0(ang - 2*pi/(qa*vv_)))
rep("WP3v2-C12b velocity kernel G = eta(v_min)/(2q) (not eta/q; REF-A, CONVENTIONS sec.13 item 1)", is0(G - eta/(2*qa)))
rho_chi, sig, mchi, rhoT, mu_, Om, Sb, Fd, qv, wv = sp.symbols('rho_chi sigmabar m_chi rho_T mu Omega Sbar F q omega', positive=True)
mE, fcr = sp.symbols('m_e fcrys2', positive=True)
urf_int = rho_chi*sig/(4*pi*mchi*rhoT*mu_**2)*qv*Fd**2*Sb                    # (M.6) integrand per dq (eta stripped)
ess_int = rho_chi/(mchi*rhoT*Om)*sig*al*mE**2/mu_**2/qv**2*Fd**2*fcr        # 1509.01598 Eq.(17) per unit mass, per dq
sol = sp.solve(sp.Eq(urf_int, ess_int), fcr)[0]
rep("WP3v2-C12c |f_crys|^2 = Omega q^3 Sbar/(4 pi alpha m_e^2) (D1's 2 pi alpha corrected)", is0(sol - Om*qv**3*Sb/(4*pi*al*mE**2)))

# ============================================================ C13 Lorentzian = 2 pi delta + Gamma fp(1/D^2) + O(G^2)  [(M.10), O4.4]
Gm = sp.symbols('Gamma', positive=True); xg = sp.symbols('x', real=True)
fp_gauss = sp.integrate((exp(-xg**2) - 1)/xg**2, (xg, -oo, oo))       # fp int e^{-x^2}/x^2 = int (e^{-x^2}-1)/x^2
rep("WP3v2-C13a fp int e^{-x^2}/x^2 dx = -2 sqrt(pi) (negative: X+ not PSD outside the window)", is0(fp_gauss + 2*sqrt(pi)))
lor = 2*pi*exp(Gm**2/4)*sp.erfc(Gm/2)                                 # int Gamma e^{-x^2}/(x^2 + Gamma^2/4) dx, closed form
chk = sp.integrate(Gm*exp(-xg**2)/(xg**2 + Gm**2/4), (xg, -oo, oo))
rep("WP3v2-C13b closed form of the Lorentzian-Gaussian pairing", is0(sp.simplify(chk - lor)))
rep("WP3v2-C13c Lorentzian -> 2 pi phi(0) + Gamma <fp 1/x^2, phi> + O(Gamma^2)",
    is0(sp.series(lor, Gm, 0, 2).removeO() - (2*pi + Gm*fp_gauss)))
rep("WP3v2-C13d no PV of 1/x^2: Hadamard fp needed (D1 sec.5.2 'P' corrected)", sp.integrate(1/xg**2, (xg, Q(1, 10), 1)) > 0)

# ============================================================ C14 Z + (1/2pi) fp int Gamma/dw^2 = 1 (Fan part)  [(M.11), O4 (vi)]
gg, W_, w0_ = Q(1, 3), Q(1), Q(1, 2)                                    # Sigma(z) = g^2/(z + i W): Lorentzian-continuum model
wpr = sp.symbols('w', real=True)
Gam = 2*gg**2*W_/(wpr**2 + W_**2); ReS = gg**2*wpr/(wpr**2 + W_**2)
dReS = sp.diff(ReS, wpr).subs(wpr, w0_)
G0, G1 = Gam.subs(wpr, w0_), sp.diff(Gam, wpr).subs(wpr, w0_)
xs, Lb = sp.symbols('x', real=True), sp.symbols('L', positive=True)   # fp over R = symmetric limit after subtracting f(0) + f'(0)x
fpint = sp.limit(sp.integrate(sp.cancel((Gam.subs(wpr, w0_ + xs) - G0 - G1*xs)/xs**2), (xs, -Lb, Lb)), Lb, oo)
rep("WP3v2-C14a KK: d_w Re Sigma = -(1/2pi) fp int Gamma(w')/(w'-w)^2 dw'", is0(dReS + fpint/(2*pi)))
Zres = 1/(1 - dReS)
rep("WP3v2-C14b Z + (1/2pi) fp int Gamma/dw^2 = 1 + O(g^4)", is0(sp.series((1/(1 - sp.Symbol('t')*dReS) - sp.Symbol('t')*dReS), sp.Symbol('t'), 0, 2).removeO() - 1))

# ============================================================ C15 coherent-potential limit of M~ (X2)        [(M.13)]
U, rr, chi0, vC = sp.symbols('U rho chi0 v_C')
Mt = U*rr + rr*(vC/(1 - vC*chi0))*(U*chi0)          # M[rho] + rho W T with M = U rho, T = U chi0, W = v/(1 - v chi0)
rep("WP3v2-C15 coherent potential (M = U rho for all pairs): M~ = M/eps(P,w_f)", is0(Mt - U*rr/(1 - vC*chi0)))

# ============================================================ C16 intraband 0/0 terms of the soft limit (REF-A sec.4)  [§M8]
Qs, ell, Xi_c, Xi_v, rcv = sp.symbols('Q ell Xi_c Xi_v rho_cv', positive=True)
for s in (+1, -1):
    Tc = (I*ell*Qs*Xi_c)*rcv/(Qs*vc + s*c*Qs)                 # g_cc rho/(eps_{c,k+q+Q} - eps_{c,k+q} +- w_Q)
    Tv = rcv*(I*ell*Qs*Xi_v)/(-Qs*vv - s*c*Qs)                # rho g_vv/(eps_vk - eps_{v,k+Q} -+ w_Q)
    rep(f"WP3v2-C16 intraband terms -> i ell rho [Xi_c/(v_c +- c) - Xi_v/(v_v +- c)], finite (sign {s:+d})",
        is0(sp.limit(Tc + Tv, Qs, 0) - I*ell*rcv*(Xi_c/(vc + s*c) - Xi_v/(vv + s*c))))

# ============================================================ C17 F1: out-state (retarded) external LFE weight, no inversion  [§M7]
def cm(a, b): return Q(a) + I*Q(b)
rho1, rho2 = Matrix([cm(1, 2), cm(-1, 1)]), Matrix([cm(2, -1), cm(1, 3)])   # pair vertices rho_p(q+G), G in {0,G1}: no symmetry
f = sp.diag(Q(3, 5), Q(1, 7)); wfr, eta_ = Q(13, 10), Q(1, 10); E1, E2 = Q(6, 5), Q(3, 2)    # pair 1 open-ish, pair 2 off
den = lambda Ep: 1/(wfr - Ep + I*eta_)
R0 = rho1.conjugate()*rho1.T*den(E1) + rho2.conjugate()*rho2.T*den(E2)      # R0_{GG'} = sum rho*_G rho_G' /(w - E + i eta), (3.2) order
R = (eye(2) - R0*f).inv()*R0                                                   # R = R0 + R0 f R
lhs = ((R - dag(R))/(2*I))[0, 0]
wout = Matrix([(eye(2) + f*R)[gi, 0] for gi in range(2)])                       # w^out_G = delta_G0 + f(q+G) R_G0 (retarded)
win = Matrix([sp.conjugate((eye(2) + R*f)[0, gi]) for gi in range(2)])         # w^in_G = [(1 + R f)_0G]^*  (advanced)
im = lambda Ep: sp.im(sp.expand_complex(den(Ep)))
tot = lambda wv: sum(abs(sp.expand_complex((wv.T*rp)[0]))**2*im(Ep) for rp, Ep in ((rho1, E1), (rho2, E2)))
rep("WP3v2-C17a Im R_00 = sum_pairs |sum_G w^out_G rho_p(q+G)|^2 Im(...) (retarded out-state, (7.2))", is0(lhs - tot(wout)))
rep("WP3v2-C17b same total with the in-state weight [(1+Rf)_0G]^* (WP0-v2 CC-1)", is0(lhs - tot(win)))
w1 = Matrix([(eye(2) + R*f)[0, gi] for gi in range(2)])
rep("WP3v2-C17c WP1 [E2] as printed, |sum (1+Rv)_0G rho|^2, misses the total without inversion", not is0(lhs - tot(w1)))
p1 = abs(sp.expand_complex((wout.T*rho1)[0]))**2; p1i = abs(sp.expand_complex((win.T*rho1)[0]))**2
rep("WP3v2-C17d pair-resolved out/in weights differ where pairs are open (seeding, not rates)", not is0(p1 - p1i))

# ============================================================ C18 F4: third moment of the Migdal sector     [(J8)]
R_, E, a1, a2, t1, t2, t3, s11, s22 = sp.symbols('R E a_1 a_2 t_1 t_2 t_3 s_1 s_2', real=True)
H = Matrix([[0, R_*t1, R_*t2], [R_*t1, a1 + R_**2*s11, R_*t3], [R_*t2, R_*t3, a2 + R_**2*s22]])   # H(R), <0|dH|0> = 0
Fch = (H - E*eye(3)).det()
E1d = -sp.diff(Fch, R_)/sp.diff(Fch, E)                     # implicit dE0/dR
E2d = (sp.diff(E1d, R_) + sp.diff(E1d, E)*E1d)              # d^2E0/dR^2
E2d0 = sp.simplify(E2d.subs({R_: 0, E: 0}))
d2H00 = sp.diff(H, R_, 2)[0, 0].subs(R_, 0)
rep("WP3v2-C18a d^2E0 = <d^2V> - 2 sum |<a|dV|0>|^2/(E_a - E0)  (3-level, implicit, exact)",
    is0(E2d0 - (d2H00 - 2*(t1**2/a1 + t2**2/a2))))
qM = sp.symbols('q_over_M', positive=True)
mom3 = sum((qM*t)**2/ea**4*ea**3 for t, ea in ((t1, a1), (t2, a2)))   # sum_a |A_a|^2 w_a^3, A_a = (q/M)<a|dV|0>/w_a^2
rep("WP3v2-C18b E^Mig_3 = (q^2/2M^2)(<d^2V> - d^2E0) = WP2 (5.2) kappa_3^X", is0(mom3 - qM**2/2*(d2H00 - E2d0)))
Ep, rh = sp.symbols('E_p rho2', positive=True)
R00 = rh*(1/(0 - Ep) - 1/(0 + Ep))                          # static response of one pole, T = 0
rep("WP3v2-C18c KK step: int_0^inf (dw/2pi) S/w = -R(0)/2 (S = 2 pi rho2 delta(w - E_p))", is0(rh/Ep + R00/2))

# ============================================================ C19 WP6 O6-2: PAER onset exponent             [§M3]
xe, Eo = sp.symbols('x E', positive=True)
rep("WP3v2-C19a free pairs, two parabolic pockets: int_0^E sqrt(x) sqrt(E-x) dx = pi E^2/8 (p_on = 2)",
    is0(sp.integrate(sqrt(xe)*sqrt(Eo - xe), (xe, 0, Eo)) - pi*Eo**2/8))
rep("WP3v2-C19b forbidden edge (|M|^2 ~ x): int x^{1/2}(E-x)^{1/2} x dx ~ E^3 (p_on = 3)",
    is0(sp.simplify(sp.integrate(xe**Q(3, 2)*sqrt(Eo - xe), (xe, 0, Eo))/Eo**3) - pi/16))

# ============================================================ C20 F8: Fano term redistributes, does not create  [§M4]
G1_, G2_, c1_, c2_ = sp.symbols('Gamma_1 Gamma_2 c_1 c_2', positive=True)
cbar = (G1_*c1_ + G2_*c2_)/(G1_ + G2_)
rep("WP3v2-C20 sum_nu F_nu = sum 2 pi Gamma_nu (cbar - c_nu) = 0", is0(2*pi*G1_*(cbar - c1_) + 2*pi*G2_*(cbar - c2_)))

# ============================================================ C21 thermal factor of (W.4c) and S<->L (F7)    [(W.4c)]
bet, om, ee2, LL = sp.symbols('beta omega e2 L', positive=True)
Sfull = 2*qa**2/ee2*LL/(1 - exp(-bet*om))
rep("WP3v2-C21 S^X+ = (2q^2/e^2) L^PA/(1 - e^{-beta w}) -> (2q^2/e^2) L^PA for beta w >> 1", is0(sp.limit(Sfull, bet, oo) - 2*qa**2/ee2*LL))

# ============================================================ C22 M1 bookkeeping: D1 (2),(4) == D2 (2.2); spin 2  [(M.4),(M.5)]
Nn, Om_, M1sq = sp.symbols('N Omega M1sq', positive=True)
Vv = Nn*Om_
S_D1 = 4*pi/Om_*M1sq                                         # (4 pi/Omega) <<|M_D1|^2>> per (k,Q)-averaged weight
eps2_D2 = 2*pi*e2/(q**2*Vv)*Nn**2*(M1sq/Nn)                # D2 (2.2): (2 pi e^2/q^2 V) sum_{kQ} |M_D2|^2, M_D2 = M_D1/sqrt N
rep("WP3v2-C22a eps2^PA (D2 2.2) == (e^2/2q^2) S^PA (D1 2) == 8 pi^2 alpha/(Omega q^2) <<|M|^2>> (D1 4)",
    is0(eps2_D2 - e2/(2*q**2)*S_D1) and is0(eps2_D2 - 8*pi**2*al/(Om_*q**2)*M1sq))
eps2_doc = pi*e2/(q**2*Vv)*Nn**2*(M1sq/Nn)
rep("WP3v2-C22b D2 script docstring (pi e^2/q^2 V) is per spin: half of (2.2)", is0(eps2_D2 - 2*eps2_doc))

# ============================================================ C23 AUDIT A1: angle-averaged onset at fixed |q|   [§M3]
qm, Km, th, aq, Eo2, pp = sp.symbols('q K theta a E p', positive=True)
Qs2 = (qm - Km)**2 + 2*qm*Km*(1 - sp.cos(th))
dd = sp.symbols('d', positive=True)
ser = sp.series(sp.sqrt(Qs2.subs(qm, Km + dd)), th, 0, 3).removeO()
rep("WP3v2-C23a |Q*|(theta) = d + |q||K| theta^2/(2d) + O(theta^4): isolated quadratic minimum at q^ || K^",
    is0(sp.simplify(ser - (dd + (Km + dd)*Km*th**2/(2*dd)))))
for p0 in (Q(1, 2), 2, 3):
    I0 = sp.integrate(th*(Eo2 - aq*th**2)**p0, (th, 0, sqrt(Eo2/aq)))
    I2 = sp.integrate(th**3*(Eo2 - aq*th**2)**p0, (th, 0, sqrt(Eo2/aq)))
    rep(f"WP3v2-C23b angle average: fixed-q exponent {p0} -> {p0+1} (generic vertex)", is0(sp.simplify(sp.diff(sp.log(I0), Eo2)*Eo2) - (p0 + 1)))
    rep(f"WP3v2-C23c angle average: fixed-q exponent {p0} -> {p0+2} (|M|^2 ~ theta^2 on the minimum)", is0(sp.simplify(sp.diff(sp.log(I2), Eo2)*Eo2) - (p0 + 2)))

print(f"\n{sum(RES)}/{len(RES)} checks PASS")
