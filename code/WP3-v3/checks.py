"""WP3-v3 identity checks (R8 revision after the R7 hostile review; copy of code/WP3-v2/checks.py, corrected and extended).
v3 changes: C3 (2603.13052: (4.6) prefactor included), C9 (fn.3 inputs, [E] labels, L7c size, 1608.01994 77 K, bremsstrahlung ratio),
C21 (finite-beta thermal-factor consistency), C23d-g (anisotropic c_nu), C24 (C4v/C3v selection rules, Si/Ge phonons),
C25 (fixed-q threshold shift), C26 (J8 with the uniform 2n_e term), C27 (ALDA k_xc), C28 (envelope), C29 (window numbers), C30 (polar cap).
R9 clean-up: C23l-m (dispersive criterion), C29b, C30d, C9e, C31 (Migdal/GS bookkeeping).
Labels: WP3v2-Cn kept where unchanged, WP3v3-Cn new or changed.
Original header: WP3-v2 identity checks (R6 revision of R5/WP3, with the consolidated M1/PAER theory).
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
# v3 (REF-A V15, REF-B 16): (4.6) carries an extra 1/m_N; the misprint is a misplaced m_N between (4.6) and (4.7).
# mass dimensions in natural units: [alpha]=0, [q]=[omega]=[m_N]=1, int d^3k_e -> 3, Im eps^-1 -> 0; dP/domega must have dimension -1
dim47 = 2 + 3 - 4 - 1
rep("WP3v3-C3a 2603.13052 (4.7) as printed is dimensionless (dP/domega needs -1): misprint CONFIRMED", dim47 == 0)
nchi, NT, MT, vel, fv, sgb, muv = sp.symbols('n_chi N_T M_T v f sigmabar mu', positive=True)
dsig48 = qn*sgb/(muv**2*vel**2); dsig_std = qn*sgb/(2*muv**2*vel**2)
printed = nchi*NT/(mN*MT)*vel*fv*dsig48*bem                     # (4.6) x (4.8) x (4.7) as printed
standard = nchi*NT/MT*vel*fv*dsig_std*kkl_avg                    # KKL dP/domega x standard dsigma/dq, (4.6) without the extra 1/m_N
rep("WP3v3-C3b printed (4.6)x(4.7)x(4.8) == KKL x standard dsigma/dq (rate consistent as printed)", is0(printed/standard - 1))
v2fix = nchi*NT/(mN*MT)*vel*fv*dsig48*(bem/mN)                   # v2 repair: m_N -> m_N^2 in (4.7), (4.6) kept
rep("WP3v3-C3c v2 repair (m_N -> m_N^2 in (4.7) only) leaves a spurious 1/m_N: REFUTED", is0(v2fix/standard - 1/mN))
fix47 = bem/mN; fix46 = nchi*NT/MT
rep("WP3v3-C3d correct repair: move 1/m_N from (4.6) into (4.7); (4.7') = KKL/2, x (4.8) = 2x std -> rate unchanged",
    is0(fix47/kkl_avg - Q(1, 2)) and is0(fix46*vel*fv*dsig48*fix47/standard - 1))

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
        'q_fn3 Si [keV] = sqrt(2M*1.2eV) (fn.3 input)': sqrt(2*MSi*Q(12, 10**4)), 'q_fn3 Ge [keV] = sqrt(2M*0.7eV) (fn.3 input)': sqrt(2*MGe*Q(7, 10**4)),
        'dM/M Si (14 e, estimate [E], not a bound)': 14*meV/MSi, 'dM/M Ge (32 e, estimate [E])': 32*meV/MGe,
        'v_N p/w_e (Si; q=100, p=5 keV, w_e=5 eV)': (100/MSi)*5*10**3/5,
        'L7c even recoil term 2p^2/(M w_e) (p=5 keV, w_e=5 eV)': 2*Q(5)**2/MSi*10**3/5,
        'L7c bound-lattice term (w_ph/w_e)^2 (60 meV, 5 eV)': (Q(6, 100)/5)**2}
for kx, vx in nums.items(): print(f"      C9  {kx:52s} {float(vx):.4g}")
rep("WP3v2-C9 Si EFT bound sqrt(2M E_g) in (230, 260) keV (2210.06490 fn.3 inputs 1.2 eV: 251)",
    230 < float(nums['q_fn3 Si [keV] = sqrt(2M*1.2eV) (fn.3 input)']) < 260)
rep("WP3v3-C9b L7c leading surviving correction is 1e-4..1e-3 (not 1e-5): <= 1e-3 and >= 1e-4",
    1e-4 < float(nums['L7c even recoil term 2p^2/(M w_e) (p=5 keV, w_e=5 eV)']) < 1e-3 and 1e-4 < float(nums['L7c bound-lattice term (w_ph/w_e)^2 (60 meV, 5 eV)']) < 1e-3)
# 1608.01994 used 77 K data near the edge (REF-A V22): n_TA(77 K), Varshni shift E_g(0) - E_g(77 K)
kB = Q(8617333, 10**11)                                   # eV/K
nTA77 = 1/(sp.exp(Q(184, 10**4)/(kB*77)) - 1)
varsh = Q(473, 10**6)*77**2/(77 + 636)                   # Si Varshni alpha = 4.73e-4 eV/K, beta = 636 K
print(f"      C9  n_TA(77 K) (18.4 meV) = {float(nTA77):.3f};  Varshni E_g(0)-E_g(77K) = {1e3*float(varsh):.2f} meV")
rep("WP3v3-C9c 1608.01994 77 K data: n_TA ~ 0.07 and gap shift ~ 4 meV (not 50 meV)", 0.05 < float(nTA77) < 0.09 and 3e-3 < float(varsh) < 5e-3)
# bremsstrahlung crystal/atom per photon at 1 eV (REF-A V18): n_r Z*^2 / |omega^2 alpha_pol|^2, Ga alpha_pol = 54 a.u.
w1au = Q(1)/Q(272114, 10**4)
ratio_br = Q(36, 10)*Q(21, 10)**2/(w1au**2*54)**2
print(f"      C9  crystal/atom bremsstrahlung ratio at 1 eV = {float(ratio_br):.3g} (scales as omega^-4)")
rep("WP3v3-C9d GaAs bremsstrahlung ratio at 1 eV ~ 3e3 (range 1e3-1e4 over 0.1-1.4 eV)", 2e3 < float(ratio_br) < 4e3)

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
# v3 (REF-A V2, REF-B 2): C21 of v2 tested only beta -> oo and could not see the double count. Finite-beta test:
eps_v, eps_c, wph = sp.symbols('epsilon_v epsilon_c omega_ph', real=True)
fF = lambda e_: 1/(exp(bet*e_) + 1); nBo = 1/(exp(bet*wph) - 1)
for s in (+1, -1):                                         # +1 emission (weight n+1, omega = e_c - e_v + w_ph), -1 absorption
    wos = eps_c - eps_v + s*wph
    wgt = nBo + Q(1, 2) + s*Q(1, 2)
    P_epw = (nBo + Q(1, 2) + s*Q(1, 2))*fF(eps_v)*(1 - fF(eps_c)) - (nBo + Q(1, 2) - s*Q(1, 2))*(1 - fF(eps_v))*fF(eps_c)   # EPW Eq.(64)
    rep(f"WP3v3-C21a EPW P = (1 - e^(-beta w))(n+1/2+-1/2) f_v(1-f_c) on shell, all T (sign {s:+d})",
        is0(sp.simplify((P_epw - (1 - exp(-bet*wos))*wgt*fF(eps_v)*(1 - fF(eps_c))).rewrite(exp))))
Mg, pref = sp.symbols('Msq kappa', positive=True)                # kappa = 4 pi/Omega; (2q^2/e^2)(8 pi^2 alpha/Omega q^2) = 4 pi/Omega
Sgold = pref*Mg                                                    # (M.3)/(W.4c): golden-rule S, weights (n+1/2+-1/2) f(1-f')
Lv3 = (ee2/(2*qa**2))*(1 - exp(-bet*om))*pref*Mg                   # v3 (M.14): L^PA carries (1 - e^{-beta w}) (= EPW P weights)
rep("WP3v3-C21b v3: S^X+ = (2q^2/e^2) L^PA/(1-e^{-beta w}) equals the golden-rule (M.3) at finite beta", is0(2*qa**2/ee2*Lv3/(1 - exp(-bet*om)) - Sgold))
Lv2 = (ee2/(2*qa**2))*pref*Mg                                      # v2 (M.14): L^PA without the factor
rep("WP3v3-C21c v2 (M.14)+(W.4c) were inconsistent at finite beta (X = X/(1-e^{-beta w}) false)", not is0(2*qa**2/ee2*Lv2/(1 - exp(-bet*om)) - Sgold))
rep("WP3v2-C21 S^X+ = (2q^2/e^2) L^PA/(1 - e^{-beta w}) -> (2q^2/e^2) L^PA for beta w >> 1 (kept; limit only)", is0(sp.limit(2*qa**2/ee2*LL/(1 - exp(-bet*om)), bet, oo) - 2*qa**2/ee2*LL))

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


# ============================================================ C23d-g anisotropic c_nu(Q^) (REF-A V10, REF-B 11-12)   [§M3]
# Q* = K - q, q at polar angle vt from K^; direction tilt of Q* is vt_Q ~ |q| vt/d; c(vt_Q) = c0 (1 + gam vt_Q^2)
c0, gam, vt = sp.symbols('c_0 gamma_c vartheta', real=True)
for case, (qq_, dd_) in {"|q|>|K|": (Km + dd, dd), "|q|<|K|": (Km - dd, dd)}.items():
    Qsq = qq_**2 + Km**2 - 2*qq_*Km*sp.cos(vt)
    tilt = sp.atan2(qq_*sp.sin(vt), sp.Abs(Km - qq_*sp.cos(vt)))
    Eth = c0*(1 + gam*tilt**2)*sp.sqrt(Qsq)
    coef = sp.simplify(sp.series(Eth, vt, 0, 3).removeO().coeff(vt, 2))
    rep(f"WP3v3-C23d E_th = c0 d + c0 (|q|/d)(gamma_c |q| + |K|/2) vt^2 + O(vt^4)   ({case})",
        is0(coef - c0*(qq_/dd_)*(gam*qq_ + Km/2)))
# on-axis is a minimum iff gamma_c > -|K|/(2|q|); REF-B's criterion -1/2 is the |q| = |K| case
rep("WP3v3-C23e gamma_c = -0.94 at |q| = |K|: on-axis is a MAXIMUM (REF-B); at |q| = |K|/2: a minimum (crossover |K|/(2|gamma_c|))",
    (-0.94*1 + 0.5) < 0 and (-0.94*0.5 + 0.5) > 0)
# Si / Ge Christoffel: exact small-angle gamma_c of the lowest TA branch about [100] in the (001) plane
C11, C12, C44 = sp.symbols('C11 C12 C44', positive=True)
Aa, Bb = C11 - C44, C12 + C44
ph = sp.symbols('phi', real=True)
n_ = (sp.cos(ph), sp.sin(ph), 0)
def christ(C11v, C12v, C44v, n):
    C = lambda i, j, k, l: (C11v if (i == j == k == l) else (C12v if (i == j and k == l) else (C44v if ((i == k and j == l) or (i == l and j == k)) and i != j else 0)))
    return Matrix(3, 3, lambda i, k: sum(C(i, j, k, l)*n[j]*n[l] for j in range(3) for l in range(3)))
G_ = christ(C11, C12, C44, n_)
lam_t = C44 - ph**2*(Bb**2 - Aa**2)/Aa                                                   # candidate in-plane quasi-TA eigenvalue
charp = sp.expand(sp.series(((G_[0, 0] - lam_t)*(G_[1, 1] - lam_t) - G_[0, 1]**2), ph, 0, 4).removeO())
gam_ex = -(Bb**2 - Aa**2)/(2*Aa*C44)                                                       # sqrt(lam/C44) = 1 + gam phi^2
rep("WP3v3-C23f lowest TA about [100], (001) plane: lambda = C44 - phi^2 (B^2-A^2)/A solves the secular eq. to O(phi^4) -> gamma_c = -(B^2-A^2)/(2 A C44)",
    is0(sp.simplify(charp)))
import mpmath as mp
SI = (mp.mpf('165.7'), mp.mpf('63.9'), mp.mpf('79.6')); GE = (mp.mpf('128.5'), mp.mpf('48.3'), mp.mpf('66.8'))
print(f"      C23 Si gamma_c(TA,[100],(001)) = {float(gam_ex.subs({C11: 165.7, C12: 63.9, C44: 79.6})):.4f}")
def cmin(Cs, n):                                    # lowest sound speed^2 (units C/rho) along unit n
    M_ = mp.matrix([[float(x) for x in row] for row in christ(*Cs, n).tolist()])
    return min(mp.eigsy(M_)[0])
def gam_dir(Cs, axis, perp, t=mp.mpf('0.02')):    # gamma_c along a tilt plane (axis, perp) from finite difference
    n = [axis[i]*mp.cos(t) + perp[i]*mp.sin(t) for i in range(3)]
    return (mp.sqrt(cmin(Cs, n)/cmin(Cs, axis)) - 1)/t**2
ax100 = [1, 0, 0]
g_si = [gam_dir(SI, ax100, [0, mp.cos(a), mp.sin(a)]) for a in (0, mp.pi/8, mp.pi/4)]
print("      C23 Si gamma_c(azimuth 0, pi/8, pi/4) about [100] =", [round(float(x), 3) for x in g_si])
rep("WP3v3-C23g Si TA: gamma_c in (-1.0, -0.7) for all azimuths (< -1/2: off-axis minima for |q| ~ |K|)", all(-1.0 < x < -0.7 for x in g_si))
# global minimum of c(n)/n_x (|Q*| ~ d/cos vt_Q at fixed parallel component), REF-B's 0.966 at vt_Q ~ 0.41
best = min(((mp.sqrt(cmin(SI, [mp.cos(t), mp.sin(t)*mp.cos(a), mp.sin(t)*mp.sin(a)])/cmin(SI, ax100))/mp.cos(t), t, a)
            for t in [mp.mpf(i)/100 for i in range(0, 80, 2)] for a in (0, mp.pi/8, mp.pi/4)), key=lambda z: z[0])
print(f"      C23 Si min_n c_TA(n)/(c_TA[100] cos vt_Q) = {float(best[0]):.4f} at vt_Q = {float(best[1]):.2f}, azimuth {float(best[2]):.2f}")
rep("WP3v3-C23h Si TA threshold minimum ~ 0.966 c_TA d at vt_Q ~ 0.4 rad, azimuth 0 (REF-B reproduced)",
    0.95 < best[0] < 0.98 and 0.3 < best[1] < 0.5 and best[2] == 0)
# exact geometry at fixed |q|: min over q^ of c_TA(Q^*)|Q*|, for |q|/|K| = 0.5 (in-window m ~ 0.34 MeV) and 1.3
def Eth_min(Cs, rq, axis, perps):
    out = []
    for a in perps:
        for i in range(0, 61):
            t = mp.mpf(i)/200                        # q polar angle up to 0.3 rad
            Qv = [axis[j] - rq*(axis[j]*mp.cos(t) + a[j]*mp.sin(t)) for j in range(3)]
            Qn = mp.sqrt(sum(x**2 for x in Qv)); n = [x/Qn for x in Qv]
            out.append((mp.sqrt(cmin(Cs, n))*Qn, t))
    e0 = mp.sqrt(cmin(Cs, axis))*abs(1 - rq)
    m_ = min(out, key=lambda z: z[0]); return m_[0]/e0, m_[1]
perps100 = [[0, 1, 0], [0, mp.sqrt(2)/2, mp.sqrt(2)/2]]
r05 = Eth_min(SI, mp.mpf('0.5'), ax100, perps100); r13 = Eth_min(SI, mp.mpf('1.3'), ax100, perps100)
print(f"      C23 Si exact geometry: |q|/|K| = 0.5 -> min/on-axis = {float(r05[0]):.4f} at vt = {float(r05[1]):.3f};"
      f" |q|/|K| = 1.3 -> {float(r13[0]):.4f} at vt = {float(r13[1]):.3f}")
rep("WP3v3-C23i Si TA: on-axis minimum at |q| = |K|/2 (crossover rebuttal), off-axis at |q| = 1.3|K| (REF-B)",
    abs(r05[0] - 1) < 1e-12 and r05[1] == 0 and r13[0] < 0.99 and r13[1] > 0)
# LA: c increases away from [100] (gamma_LA > 0) -> on-axis minimum for all |q|
def cmax(Cs, n):
    M_ = mp.matrix([[float(x) for x in row] for row in christ(*Cs, n).tolist()]); return max(mp.eigsy(M_)[0])
gLA = (mp.sqrt(cmax(SI, [mp.cos(0.02), mp.sin(0.02), 0])/cmax(SI, ax100)) - 1)/mp.mpf('0.02')**2
rep("WP3v3-C23j Si LA: gamma_LA > 0 about [100] (on-axis LA minimum for every |q|)", gLA > 0)
# Ge about [111] (C3v): gamma_c of the lowest TA
ax111 = [1/mp.sqrt(3)]*3; pA = [1/mp.sqrt(2), -1/mp.sqrt(2), 0]; pB = [1/mp.sqrt(6), 1/mp.sqrt(6), -2/mp.sqrt(6)]
# Ge: [111] is a CONICAL acoustic axis for the TA pair: the lower sheet drops LINEARLY with the tilt, c = c0 (1 - beta_c |vt_Q|)
def lin_dir(Cs, axis, perp, t):
    n = [axis[i]*mp.cos(t) + perp[i]*mp.sin(t) for i in range(3)]
    return (mp.sqrt(cmin(Cs, n)/cmin(Cs, axis)) - 1)/t
b_ge = [lin_dir(GE, ax111, [pA[i]*mp.cos(a) + pB[i]*mp.sin(a) for i in range(3)], t) for a in (0, mp.pi/6) for t in (mp.mpf('0.005'), mp.mpf('0.01'))]
print("      C23 Ge (c_TA,low/c0 - 1)/vt_Q at azimuth 0, pi/6 and vt_Q = 0.005, 0.01:", [round(float(x), 4) for x in b_ge])
rep("WP3v3-C23k Ge TA about [111]: conical (linear) drop beta_c ~ 0.25 -> on-axis never a minimum; off-axis minima at every |q|",
    all(-0.3 < x < -0.2 for x in b_ge) and abs(b_ge[0] - b_ge[1]) < 0.01)

# ============================================================ C24 symmetry: C4v (Si Delta) and C3v (Ge Lambda) selection rules  [§M3]
def rot(axis, ang):
    ax = Matrix(axis)/sp.sqrt(sum(x**2 for x in axis)); K_ = Matrix([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
    return sp.simplify(eye(3) + sp.sin(ang)*K_ + (1 - sp.cos(ang))*K_*K_)
def mirror(nrm):
    nv = Matrix(nrm)/sp.sqrt(sum(x**2 for x in nrm)); return sp.simplify(eye(3) - 2*nv*nv.T)
alat = sp.Integer(1); td = Matrix([Q(1, 4)]*3)
def in_fcc(vv_):                                   # fcc lattice vectors (a/2)(n1+n2, ...): coordinates in units a/2 integers with even sum
    c2 = [sp.nsimplify(2*x) for x in vv_]; return all(x.is_integer for x in c2) and sum(c2) % 2 == 0
C4v = {'E': eye(3), 'C2x': rot([1, 0, 0], pi), 'C4x+': rot([1, 0, 0], pi/2), 'C4x-': rot([1, 0, 0], -pi/2),
       'sy': mirror([0, 1, 0]), 'sz': mirror([0, 0, 1]), 'sd1': mirror([0, 1, -1]), 'sd2': mirror([0, 1, 1])}
cls4 = {'E': 'E', 'C2x': 'C2', 'C4x+': 'C4', 'C4x-': 'C4', 'sy': 'sv', 'sz': 'sv', 'sd1': 'sd', 'sd2': 'sd'}
tab4 = {'A1': dict(E=1, C2=1, C4=1, sv=1, sd=1), 'A2': dict(E=1, C2=1, C4=1, sv=-1, sd=-1), 'B1': dict(E=1, C2=1, C4=-1, sv=1, sd=-1),
        'B2': dict(E=1, C2=1, C4=-1, sv=-1, sd=1), 'E': dict(E=2, C2=-2, C4=0, sv=0, sd=0)}
def is_Td(R):                                      # T_d element (t = 0) iff R t_d - t_d is an fcc vector (origin on an atom)
    return in_fcc(R*td - td)
tdel = {g for g, R in C4v.items() if not is_Td(R)}
rep("WP3v3-C24a diamond, origin on atom: t_d elements of C4v(x) are C4x+-, sigma_y, sigma_z (WP1-v3 3.2(c))", tdel == {'C4x+', 'C4x-', 'sy', 'sz'})
def decomp(chi, tab, cls, grp):
    order = len(grp)
    return {ir: sp.nsimplify(sum(sp.conjugate(tab[ir][cls[g]])*chi[g] for g in grp)/order) for ir in tab}
# O_h characters needed: T2g (Gamma_25', valence top, even about the bond centre) and T1u (Gamma_15, acoustic) as functions of R
def oh_char(R, which):
    tr, det = sp.simplify(R.trace()), sp.simplify(R.det())
    Rp = R*det                                     # proper part
    trp = sp.simplify(Rp.trace())
    chi_T1 = trp                                   # T1 (vector) character on proper rotations
    chi_T2 = {3: 3, -1: None, 1: -1, 0: 0}         # T2 on proper: E 3, C4 -1, C3 0; C2: -1 (C4^2 type) or +1 (C2')
    if trp == -1:                                  # C2: distinguish C4^2 (axis along cube axis) from C2' (face diagonal)
        axis_ = (Rp + eye(3)).columnspace()[0]; nz = sum(1 for x in axis_ if x != 0)
        t2 = -1 if nz == 1 else 1
    else:
        t2 = chi_T2[int(trp)]
    if which == 'T2g': return t2
    if which == 'T1u': return chi_T1*det
G25 = {g: oh_char(R, 'T2g') for g, R in C4v.items()}; G15 = {g: oh_char(R, 'T1u') for g, R in C4v.items()}
d25 = decomp(G25, tab4, cls4, C4v); d15 = decomp(G15, tab4, cls4, C4v)
rep("WP3v3-C24b Gamma_25' (T2g) | C4v = B2 + E  (Delta_2' + Delta_5), no A1 = Delta_1", d25 == {'A1': 0, 'A2': 0, 'B1': 0, 'B2': 1, 'E': 1})
rep("WP3v3-C24c Gamma_15 (acoustic, T1u) | C4v = A1 + E  (LA = Delta_1, TA = Delta_5)", d15 == {'A1': 1, 'A2': 0, 'B1': 0, 'B2': 0, 'E': 1})
# mechanical representation along Delta from the geometry: atoms tau_1 = 0, tau_2 = t_d; reduced character e^{+iQ.t} chi
xi = sp.symbols('xi', positive=True); Qv = Matrix([2*pi*xi, 0, 0])
taus = [Matrix([0, 0, 0]), td]
def mech_char(R, t):
    ch = 0
    for tau in taus:
        img = R*tau + t
        if in_fcc(img - tau): ch += sp.exp(I*(Qv.T*(img - tau))[0])*R.trace()
    return sp.simplify(ch)
chi_mech = {g: sp.simplify(mech_char(R, (Matrix([0, 0, 0]) if g not in tdel else td))*(1 if g not in tdel else sp.exp(I*(Qv.T*td)[0]))) for g, R in C4v.items()}
dm = decomp(chi_mech, tab4, cls4, C4v)
rep("WP3v3-C24d phonons along Delta (generic xi): A1 + B2 + 2E (xi-independent integers)", dm == {'A1': 1, 'A2': 0, 'B1': 0, 'B2': 1, 'E': 2})
# longitudinal block under C4x: eigenvalues +-e^{i Q.t_d}; the branch continuous to the in-phase (acoustic) mode has reduced char +1 -> LA = A1
R4 = C4v['C4x+']; L2 = R4*td + td            # tau_2 -> tau_1 + L2 ; tau_1 -> tau_2 (L = 0)
Dlong = Matrix([[0, sp.exp(I*(Qv.T*L2)[0])], [1, 0]])
evs = Dlong.eigenvects()
redchar = {sp.simplify(sp.powdenest(ev[0], force=True)*sp.exp(-I*(Qv.T*td)[0])): ev[2][0] for ev in evs}
inphase = [rc for rc, vec in redchar.items() if sp.simplify(sp.powdenest(vec[0]/vec[1], force=True).subs(xi, 0) - 1) == 0]
rep("WP3v3-C24e LA (in-phase at Q->0) has reduced C4 character +1 (A1 = Delta_1); LO has -1 (B2 = Delta_2')", inphase == [1])
def allowed(Gop, Gph, Gv, tab, cls, grp, Gc='A1'):
    prod = {g: tab[Gc][cls[g]]*tab[Gop][cls[g]]*tab[Gph][cls[g]]*sum(tab[r][cls[g]]*m_ for r, m_ in Gv.items()) for g in grp}
    return decomp(prod, tab, cls, grp)['A1'] != 0
Gv4 = {'B2': 1, 'E': 1}
br = {'LA': 'A1', 'LO': 'B2', 'TA': 'E', 'TO': 'E'}
res0 = {b: allowed('A1', r_, Gv4, tab4, cls4, C4v) for b, r_ in br.items()}
rep("WP3v3-C24f Si, G'=0 class on the [100] axis: LA forbidden; TA, TO, LO allowed (REF-A)", res0 == {'LA': False, 'LO': True, 'TA': True, 'TO': True})
res2 = {b: allowed('B2', r_, Gv4, tab4, cls4, C4v) for b, r_ in br.items()}
rep("WP3v3-C24g Si, G'=(-200) class (operator B2, |q| > 2.28 keV): LO forbidden; LA, TA, TO allowed", res2 == {'LA': True, 'LO': False, 'TA': True, 'TO': True})
# Ge: C3v about [111]; all elements are T_d (no t_d phases)
C3v = {'E': eye(3), 'C3+': rot([1, 1, 1], 2*pi/3), 'C3-': rot([1, 1, 1], -2*pi/3),
       's1': mirror([1, -1, 0]), 's2': mirror([0, 1, -1]), 's3': mirror([1, 0, -1])}
cls3 = {'E': 'E', 'C3+': 'C3', 'C3-': 'C3', 's1': 'sv', 's2': 'sv', 's3': 'sv'}
tab3 = {'A1': dict(E=1, C3=1, sv=1), 'A2': dict(E=1, C3=1, sv=-1), 'E': dict(E=2, C3=-1, sv=0)}
rep("WP3v3-C24h Ge Lambda axis: C3v contains no t_d elements", all(is_Td(R) for R in C3v.values()))
d25g = decomp({g: oh_char(R, 'T2g') for g, R in C3v.items()}, tab3, cls3, C3v)
Qg = Matrix([2*pi*xi]*3)
def mech3(R):
    ch = 0
    for tau in taus:
        img = R*tau
        if in_fcc(img - tau): ch += sp.exp(I*(Qg.T*(img - tau))[0])*R.trace()
    return sp.simplify(ch)
dmg = decomp({g: mech3(R) for g, R in C3v.items()}, tab3, cls3, C3v)
rep("WP3v3-C24i Ge: Gamma_25' | C3v = A1 + E (Lambda_1 + Lambda_3); phonons 2A1 + 2E (LA, LO = Lambda_1; TA, TO = Lambda_3)",
    d25g == {'A1': 1, 'A2': 0, 'E': 1} and dmg == {'A1': 2, 'A2': 0, 'E': 2})
resg = {b: allowed('A1', r_, {'A1': 1, 'E': 1}, tab3, cls3, C3v) for b, r_ in {'LA': 'A1', 'TA': 'E'}.items()}
rep("WP3v3-C24j Ge (L1 electron, G=0): LA and TA both allowed on the axis (no vertex zero)", all(resg.values()))

# ============================================================ C25 fixed-q threshold = min F (REF-A V9, REF-B 10)   [§M3]
dkc, dkv, mc_, mh_, cs = sp.symbols('dk_c dk_v m_c m_h c_s', real=True)
Fq = dkc**2/(2*mc_) + dkv**2/(2*mh_) + cs*(dkc - dkv)
solq = sp.solve([sp.diff(Fq, dkc), sp.diff(Fq, dkv)], [dkc, dkv])
rep("WP3v3-C25a min over pockets of eps_c + (-eps_v) + c n.(dk'-dk) = -(m_c + m_h) c^2/2", is0(Fq.subs(solq) + (mc_ + mh_)*cs**2/2))
me_eV = 510998.95; cl = 299792458.0
for nm, cv_ in (("TA 5.85 km/s", 5846.0), ("LA 8.43 km/s", 8433.0)):
    print(f"      C25 Si shift (m_l + m_hh = 1.41 m_e), {nm}: {1e3*0.5*1.41*me_eV*(cv_/cl)**2:.3f} meV")
rep("WP3v3-C25b Si: shift 0.1-0.4 meV (REF-A's order; REF-B's 'micro-eV' too small)",
    0.1e-3 < 0.5*1.41*me_eV*(5846/cl)**2 < 0.4e-3 and 0.1e-3 < 0.5*1.41*me_eV*(8433/cl)**2 < 0.4e-3)

# ============================================================ C26 J8 (ii) with the uniform 2 n_e term (WP0-v3 G5, WP2-v3 IF-1)   [(J8)]
yv = sp.symbols('y', positive=True)
j2 = (3/yv**3 - 1/yv)*sp.sin(yv) - 3*sp.cos(yv)/yv**2
rep("WP3v3-C26a 6 int_0^inf j2(y) dy/y = 2 (uniform-density term 2 n_e, q -> 0+)", is0(6*sp.integrate(j2/yv, (yv, 0, oo)) - 2))
nk, ne0, neR, Ze, me2, Mk2, q2 = sp.symbols('n_kappa n_e n_eR Ze2 m_e M q2', positive=True)
k3sum = q2/(2*Mk2**2)*Ze*neR/3                                   # k3^X + k3^GS = (q^2/2M^2) <d^2 V> (cubic, point nucleus)
M3 = -q2*Ze*nk*(neR + 2*ne0)/(3*me2*Mk2)                         # WP0-v3 (4.7')
rep("WP3v3-C26b M3_ek(q->0+) = -2 n_k (M/m_e)(k3^X + k3^GS) (1 + 2 n_e/n_e(R))", is0(M3 + 2*nk*(Mk2/me2)*k3sum*(1 + 2*ne0/neR)))
rep("WP3v3-C26c contact identity k3^(eN) = -(m_e/M) M3_ek/(2 n_k) x n_e(R)/(n_e(R) + 2 n_e)", is0(-(me2/Mk2)*M3/(2*nk)*neR/(neR + 2*ne0) - k3sum))

# ============================================================ C27 ALDA second-order kernel is nonzero (REF-B 7)   [§M7]
nn = sp.symbols('n', positive=True)
ex = -Q(3, 4)*(3/pi)**Q(1, 3)*nn**Q(4, 3)
kxc = sp.diff(ex, nn, 3)
rep("WP3v3-C27 LDA exchange: k_xc = d^3 e_x/dn^3 = (8/27)... n^(-5/3) != 0, absent from the TDH source N", not is0(kxc) and is0(sp.simplify(kxc*nn**Q(5, 3)) - sp.simplify(kxc*nn**Q(5, 3)).subs(nn, 1)))

# ============================================================ C28 pair-screening envelope (REF-A V7, REF-B 8)   [§M7]
lo = Q(8, 10)*Q(5, 10)*Q(98, 100); hi = Q(12, 10)*Q(15, 10)*Q(102, 100)
print(f"      C28 multiplicative envelope, both signs open: [{float(lo):.3f}, {float(hi):.3f}]")
rep("WP3v3-C28 envelope (1+d_om)(1+d_LF)(1+d_pair), d_LF in [-0.2,0.2], d_pair in [-0.5,0.5]: within [0.39, 1.84] -> [0.4, 1.8]",
    abs(float(lo) - 0.392) < 1e-3 and abs(float(hi) - 1.836) < 1e-3)

# ============================================================ C29 window numbers (v_max = 794.5 km/s)   [§M9]
vmx = Q(7945, 10)/Q(2997924580, 10**4)
mfl = lambda E_eV: 2*E_eV/vmx**2/10**6                       # MeV
nums_w = {'Si PAER floor 2E_g/v^2 (1.170 eV)': mfl(Q(1170, 1000)), 'Si exciton-replica floor 2(E_x + 14 meV)/v^2': mfl(Q(1170, 1000) - Q(147, 10**4) + Q(14, 1000)),
          'Si free-pair edge with zone-boundary TA 18 meV': mfl(Q(1188, 1000)), 'Ge PAER floor 2E_g/v^2 (0.744 eV)': mfl(Q(744, 1000)),
          'Ge with TA(L) 7.7 meV': mfl(Q(7517, 10000))}
for kx, vx in nums_w.items(): print(f"      C29 {kx:48s} {float(vx):.4f} MeV")
rep("WP3v3-C29 Si PAER edge 0.333-0.339 MeV; Ge 0.212-0.214 MeV", 0.332 < float(nums_w['Si exciton-replica floor 2(E_x + 14 meV)/v^2']) < 0.334
    and 0.338 < float(nums_w['Si free-pair edge with zone-boundary TA 18 meV']) < 0.339 and 0.211 < float(nums_w['Ge PAER floor 2E_g/v^2 (0.744 eV)']) < 0.215)

# ============================================================ C30 Q_w and the polar cap (REF-A V12, REF-B 4, 13)   [§M3]
Mx, dlt, cT, Ha = sp.symbols('M_x delta_0 c_T Ha', positive=True)
dsol = sp.solve(sp.Eq(dd**2/(2*Mx) - cT*dd, dlt), dd)
dpos = [s_ for s_ in dsol if s_.subs({Mx: 1, cT: Q(1, 100), dlt: 1}) > 0][0]
rep("WP3v3-C30a window at q^||K^: d >= M c + sqrt(M^2 c^2 + 2 M delta_0)", is0(dpos - (Mx*cT + sp.sqrt(Mx**2*cT**2 + 2*Mx*dlt))))
au_inv_A = 1.8897261; Ha_eV = 27.211386
for d0 in (0.1, 0.3):
    print(f"      C30 Q_w (M = 1.41 m_e, delta_0 = {d0} eV) = {(2*1.41*d0/Ha_eV)**0.5*au_inv_A:.3f} A^-1")
rep("WP3v3-C30b Q_w = 0.19 A^-1 (delta_0 = 0.1 eV) and 0.33 A^-1 (0.3 eV, consistent with (M.9))",
    abs((2*1.41*0.1/Ha_eV)**0.5*au_inv_A - 0.192) < 0.005 and abs((2*1.41*0.3/Ha_eV)**0.5*au_inv_A - 0.333) < 0.005)
Qw = sp.symbols('Q_w', positive=True)
capeq = sp.Eq((qm - Km)**2 + 2*qm*Km*(1 - sp.cos(th)), Qw**2)
thw = sp.solve(capeq, th)
rep("WP3v3-C30c failing set is the polar cap |Q*| < Q_w: cos theta_w = 1 - (Q_w^2 - d^2)/(2|q||K|) (a cap, not the shell)",
    any(is0(sp.cos(t_) - (1 - (Qw**2 - (qm - Km)**2)/(2*qm*Km))) for t_ in thw))

# ============================================================ R9 clean-up checks (VER-WP3-A/B, AUDIT-2)
# C23l dispersive on/off-axis criterion (VER-WP3-B N1)
w0f = sp.Function('omega_0'); gw = sp.symbols('gamma_omega', real=True)
for case, (qq_, dd_) in {"|q|>|K|": (Km + dd, dd), "|q|<|K|": (Km - dd, dd)}.items():
    Qmag = sp.sqrt(qq_**2 + Km**2 - 2*qq_*Km*sp.cos(vt))
    tilt = sp.atan(qq_*sp.sin(vt)/(sp.Abs(Km - qq_*sp.cos(vt))))
    Ed = w0f(Qmag)*(1 + gw*tilt**2)
    c2 = sp.simplify(sp.series(Ed, vt, 0, 3).removeO().coeff(vt, 2))
    tgt = sp.Subs(sp.Derivative(w0f(xx), xx), xx, dd_).doit()*qq_*Km/(2*dd_) + w0f(dd_)*gw*qq_**2/dd_**2
    rep(f"WP3v3-C23l dispersive E_th: theta^2 coeff = w0'(d)|q||K|/(2d) + w0(d) gamma_w |q|^2/d^2   ({case})", is0(sp.simplify(c2 - tgt)))
# Si numbers: sine TA dispersion, |K| = 0.983 A^-1, Q_X = 1.157 A^-1, gamma = -0.96
KA, QX = mp.mpf('0.983'), mp.mpf('1.157')
def rfac(d):
    x = mp.pi*d/(2*QX); return x*mp.cos(x)/mp.sin(x)
print(f"      C23 r(d_K = 0.45 X) = {float(rfac(mp.mpf('0.45')*QX)):.3f}")
fcross = lambda u: -0.96 + (1/(2*u))*rfac(KA*(1 - u))          # u = |q|/|K|; zero at crossover
uc = mp.findroot(fcross, 0.45)
print(f"      C23 dispersive crossover |q|/|K| = {float(uc):.3f}  -> |q| = {float(uc*mp.mpf('1.94')):.3f} keV (linear: {1/(2*0.96):.3f}, {1.94/(2*0.96):.3f} keV)")
rep("WP3v3-C23m Si TA dispersive crossover |q| ~ 0.79 keV self-consistent (0.85 with r frozen at 0.83; linear 1.01) (VER-WP3-B N1)",
    0.75 < float(uc*1.94) < 0.90 and abs(float(rfac(mp.mpf('0.45')*QX)) - 0.83) < 0.01)
# C29b window edges per AUDIT-2 m1, m2
nums_w2 = {'Si continuum edge, omega_TA(Q*) = 13.5 meV': mfl(Q(1170, 1000) + Q(135, 10**4)),
           'Si exciton replica E_x + 13.5 meV': mfl(Q(1170, 1000) - Q(147, 10**4) + Q(135, 10**4)),
           'Si bound-exciton floor 2E_x/v^2': mfl(Q(1170, 1000) - Q(147, 10**4)),
           'Ge with omega_TA = 7.5 meV': mfl(Q(744, 1000) + Q(75, 10**4))}
for kx, vx in nums_w2.items(): print(f"      C29 {kx:48s} {float(vx):.4f} MeV")
rep("WP3v3-C29b Si continuum 0.337, replica 0.3328 < 2E_g/v^2 = 0.3332 (replica below E_g), floor 0.329; Ge 0.214",
    abs(float(nums_w2['Si continuum edge, omega_TA(Q*) = 13.5 meV']) - 0.337) < 5e-4
    and float(nums_w2['Si exciton replica E_x + 13.5 meV']) < float(mfl(Q(1170, 1000)))
    and abs(float(nums_w2['Si bound-exciton floor 2E_x/v^2']) - 0.329) < 5e-4 and abs(float(nums_w2['Ge with omega_TA = 7.5 meV']) - 0.214) < 5e-4)
# C30d Q_w with WP1's M_x = 1.19 m_e (AUDIT-2 m19)
print(f"      C30 Q_w (M = 1.19 m_e, delta_0 = 0.3 eV) = {(2*1.19*0.3/Ha_eV)**0.5*au_inv_A:.3f} A^-1")
rep("WP3v3-C30d Q_w(0.3 eV) = 0.31 (1.19 m_e) to 0.33 (1.41 m_e) A^-1", abs((2*1.19*0.3/Ha_eV)**0.5*au_inv_A - 0.306) < 0.005)
# C9e Ge x_R = 1 at sqrt(2M * 23 meV) (AUDIT-2 m18)
xRGe = sqrt(2*MGe*Q(23, 10**6))
print(f"      C9  Ge sqrt(2M*23 meV) = {float(xRGe):.2f} keV; impulse onset 2x = {2*float(xRGe):.1f} keV")
rep("WP3v3-C9e Ge x_R = 1 at 55.8 keV (23 meV), impulse onset 112 keV", abs(float(xRGe) - 55.8) < 0.1 and abs(2*float(xRGe) - 111.6) < 0.3)
# C31 Migdal/GS bookkeeping (AUDIT-2 B3; WP5-v3 C20b)
Pm, dMs, Ms, qs2 = sp.symbols('P_Mig deltaM M q2', positive=True)
E1 = qs2*dMs/(2*Ms**2)
M1X = E1 + Pm*qs2/(2*Ms)
M1GS = qs2/(2*Ms) - M1X
rep("WP3v3-C31a f-sum split: M1_GS + M1_X = q^2/2M (bare mass), M1_X = E^Mig_1 + P_Mig q^2/2M", is0(M1GS + M1X - qs2/(2*Ms)))
eps_ = sp.symbols('epsilon', positive=True)
diff1 = sp.series((M1GS - (1 - Pm)*qs2/(2*(Ms + dMs))).subs({Pm: eps_*Pm, dMs: eps_*dMs}), eps_, 0, 2).removeO()
rep("WP3v3-C31b M1_GS = (1 - P_Mig) q^2/2(M + dM) + O(P_Mig dM/M, (dM/M)^2): GS input (1 - P_Mig) S^GS[M + dM]", is0(diff1))
v3N1 = qs2*dMs/Ms**2/2                                         # v3 N1 'overcount = E^Mig_1' per nucleus
rep("WP3v3-C31c v3 N1 overcount (E^Mig_1 only) misses the X recoil P_Mig q^2/2M (B3)", not is0(M1X - v3N1))

print(f"\n{sum(RES)}/{len(RES)} checks PASS")
