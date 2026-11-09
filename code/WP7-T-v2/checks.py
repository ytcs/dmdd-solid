"""WP7-T-v2 (R12) checks (v1 = code/WP7-T/checks.py; vacuous C3d, C4c, C7c, C13a, C14f removed per REF-WP7-T-A/B; new C4c, C5c, C5d, C6e, C10c, C10d, C14b, C14d, C14e, C15, C16): low-temperature defect quantum kinetics (TLS, defectons, crowdions, tunnelling kinetics, release kernel).
Sympy/mpmath only (exact arithmetic where possible; evalf of exact expressions for the [E] numbers). No simulation.
Run:  python3 -I checks.py      Prints PASS/FAIL per check. Labels WP7T-Cn (CONVENTIONS sec. 14).
Units: hbar = c = k_B = 1 for the identities; eV and Angstrom for the numbers (hbar c = 1973.27 eV A)."""
import sympy as sp
import mpmath as mp
from sympy import Rational as Q, sqrt, pi, exp, symbols, simplify, integrate, oo, gamma, cos, sin, tanh, coth

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:86s} {note}")
def num(x, n=4): return sp.N(x, n)

hc = Q(197327, 100)             # eV A
amu = Q(931494102, 1)           # eV
eV_J = Q(1602176634, 10**28)    # J per eV

# ------------------------------------------------------------- C1 two-state reduction (TLS eigenbasis matrix elements)
das, dtun = symbols('Delta_as Delta_tun', real=True)
E = sqrt(das**2 + dtun**2)
H = sp.Matrix([[das, dtun], [dtun, -das]])/2          # position basis (R, L): H = (Delta_as sz + Delta_tun sx)/2
sz = sp.Matrix([[1, 0], [0, -1]])
evecs = H.eigenvects()
vg = [v for val, m, vs in evecs for v in vs if simplify(val + E/2) == 0][0]
ve = [v for val, m, vs in evecs for v in vs if simplify(val - E/2) == 0][0]
vg = vg/sqrt(simplify((vg.T*vg)[0])); ve = ve/sqrt(simplify((ve.T*ve)[0]))
offd = simplify((ve.T*sz*vg)[0]**2); diag = simplify((vg.T*sz*vg)[0]**2)
rep("WP7T-C1a |<e|sigma_z^(p)|g>|^2 = (Delta_tun/E)^2", simplify(offd - dtun**2/E**2) == 0)
rep("WP7T-C1b |<g|sigma_z^(p)|g>|^2 = (Delta_as/E)^2", simplify(diag - das**2/E**2) == 0)

# ------------------------------------------------------------- C2 STM ensemble average of (Delta_tun/E)^2
Ev, dl, P0 = symbols('E Delta P0', positive=True)
PE = P0*Ev/(dl*sqrt(Ev**2 - dl**2))                   # 1705.01108 Eq. (8)
avg = integrate(PE*(dl/Ev)**2, (dl, 0, Ev))
rep("WP7T-C2  int dDelta P(E,Delta)(Delta/E)^2 = P0 (Delta_min -> 0)", simplify(avg - P0) == 0)

# ------------------------------------------------------------- C3 Jaeckle one-phonon rate from CONVENTIONS sec.5 phonons
rho, c, gam, Qv, w = symbols('rho c gamma Q omega', positive=True)
# H_int = gamma*S*sigma_z (delta eps = 2 gamma S); longitudinal strain matrix element |<1|S|0>|^2 = Q^2/(2 rho V omega)
# Gamma_down(T=0) = 2pi * sum_Q |<e|H_int|g>|^2 delta(E - cQ);  sum_Q -> V int d^3Q/(2pi)^3
integrand = 2*pi*(gam**2*(dtun/Ev)**2)*Qv**2/(2*rho*c*Qv)*4*pi*Qv**2/(2*pi)**3
Gdown = simplify(integrand.subs(Qv, Ev/c)/c)          # delta(E - cQ) -> 1/c at Q = E/c
jaeckle = (gam**2/c**5)*(dtun/Ev)**2*Ev**3/(2*pi*rho)   # 2103.06977 Eq.(7), one branch, T = 0
rep("WP7T-C3a derived Gamma_down = (gamma^2/c^5)(Delta/E)^2 E^3/(2 pi rho)  [= 2103.06977 Eq.(7)]", simplify(Gdown - jaeckle) == 0)
Tt = symbols('T', positive=True)
nB = 1/(exp(Ev/Tt) - 1)
rep("WP7T-C3b Gamma_1 = Gamma_down(n+1) + Gamma_down n = Gamma_down coth(E/2T)", simplify((2*nB + 1) - coth(Ev/(2*Tt))).rewrite(exp).simplify() == 0)
hb = symbols('h', positive=True)
A_1610 = 8*pi**3/(rho*hb**4)                           # 1610.03974 Eq.(5) prefactor (with h = 2 pi hbar, hbar = 1)
rep("WP7T-C3c 1610.03974 Eq.(5) 8pi^3/(rho h^4) = 1/(2 pi rho hbar^4)", simplify(A_1610.subs(hb, 2*pi) - 1/(2*pi*rho)) == 0)
# same rate with the 2103.06977 Eq.(2) coupling read literally (H_int = gamma S sigma_z / 2): 4x smaller -> source inconsistency

# ------------------------------------------------------------- C4 resonant absorption 1/Q (phonon and electric)
S0, E0, pdip, epsr, P0s = symbols('S_0 E_0 p epsilon_r Pbar', positive=True)
# power per volume: omega * 2pi |<e|gamma S0/2 sigma_z|g>|^2 * <(Delta/E)^2>_STM * tanh ; <..> -> Pbar (C2)
Pabs = w*2*pi*(gam*S0/2)**2*P0s*tanh(w/(2*Tt))
Wst = rho*c**2*S0**2/2                                 # time-averaged acoustic energy density (traveling wave, strain amplitude S0)
Qinv_ph = simplify(Pabs/(w*Wst))
rep("WP7T-C4a 1/Q_ph = pi Pbar gamma^2 tanh(w/2T)/(rho c^2)", simplify(Qinv_ph - pi*P0s*gam**2*tanh(w/(2*Tt))/(rho*c**2)) == 0)
Pel = w*2*pi*(pdip*E0/2)**2/3*P0s*tanh(w/(2*Tt))      # delta eps = 2 p.E, orientation average 1/3
Qinv_el = simplify(Pel/(w*epsr*E0**2/2))               # HL units: peak electric energy density eps_r E0^2/2
rep("WP7T-C4b 1/Q_el = pi Pbar p^2 tanh/(3 eps_r) [= 1705.01108 Eq.(20), T->0, D0->Pbar]", simplify(Qinv_el - pi*P0s*pdip**2*tanh(w/(2*Tt))/(3*epsr)) == 0)
# C4c (new): 2103.06977 Eqs.(4),(12),(13),(15) read literally (tau_2 -> oo: tau2/(1+x^2 tau2^2) -> pi delta(x); M = gamma Delta/2E)
#   tan(delta) = <chi''>/(rho v^2), <chi''> = int dE dDelta P(E,Delta) 4 M^2 tanh(E/2T) pi delta(E - w)
chi2 = integrate(PE*4*(gam*dl/(2*Ev))**2, (dl, 0, Ev))*pi*tanh(Ev/(2*Tt))
tand_src = (chi2/(rho*c**2)).subs(Ev, w)
rep("WP7T-C4c 2103.06977 Eqs.(4)+(12)+(13)+(15) give pi P0 gamma^2 tanh/(rho v^2) = derived C4a (so 1705.01108 Eq.(20) phonon 1/2 is a slip)",
    simplify(tand_src - pi*P0*gam**2*tanh(w/(2*Tt))/(rho*c**2)) == 0)

# ------------------------------------------------------------- C5 dynamic elastic vertex (isotropic Green function)
lam, mu = symbols('lambda mu', positive=True)
qx, qy, qz = symbols('q_x q_y q_z', real=True)
qv = sp.Matrix([qx, qy, qz]); q2 = qx**2 + qy**2 + qz**2
cl2, ct2 = (lam + 2*mu)/rho, mu/rho
PL = qv*qv.T/q2; PT = sp.eye(3) - PL
G = PL/(rho*(cl2*q2 - w**2)) + PT/(rho*(ct2*q2 - w**2))   # retarded displacement Green function (omega -> omega + i0)
g11, g12, g13, g22, g23, g33 = symbols('g11 g12 g13 g22 g23 g33', real=True)
gm = sp.Matrix([[g11, g12, g13], [g12, g22, g23], [g13, g23, g33]])
# force density of the elastic-dipole change Delta D = -2 gamma:  F(q) = -i(-2gamma)q ; density change n0 * i q.u, u = G F
dn = simplify((qv.T*G*((-2*gm)*qv))[0])              # i q.(G(-i M q)) = q.G.M.q with M = -2 gamma
target = -2*(qv.T*gm*qv)[0]/(rho*(cl2*q2 - w**2))
rep("WP7T-C5a contraction q.G.M.q (M = -2gamma, v1 force sign; physical sign fixed by C5c): only the longitudinal branch survives", simplify(dn - target) == 0)
rep("WP7T-C5b static limit of the C5a contraction is q-independent (magnitude 2 qhat.gamma.qhat/(rho c_l^2); sign per C5c)", simplify(target.subs(w, 0) - (-2*(qv.T*gm*qv)[0]/q2/(lam + 2*mu))) == 0)
# C5c (new, sign; REF-B C-9): force pair +F x at +a x/2, -F x at -a x/2 (expansion for F>0): f(q) = i D q, D = F a xx.
Fp, ap, Sxx, n0 = symbols('F_p a_p S_xx n_0', positive=True)
fq = sp.series(Fp*(sp.exp(sp.I*qx*ap/2) - sp.exp(-sp.I*qx*ap/2)), ap, 0, 2).removeO()       # x-component of f(q)
Dxx = Fp*ap
dn_host = simplify(sp.I*n0*qx*fq/(rho*cl2*q2))                                               # i n0 q.u, u = G f (static, longitudinal)
E_int = -(Fp*Sxx*ap/2) - (-Fp)*(Sxx*(-ap/2))                                                 # -sum f.u_ext, u_ext = S.r
gxx = symbols('g_xx', real=True)
# Delta_as shift = E_R - E_L = -(D_R - D_L) S = 2 gamma S  =>  Delta D = -2 gamma ; host density change R - L:
dn_RL = simplify(dn_host.subs(Fp*ap, Dxx).subs(Fp, -2*gxx/ap))
rep("WP7T-C5c E_int = -D:S and dn = -n0 qhat.D.qhat/(rho c_l^2) => R-L host term = +2 n0 qhat.gamma.qhat/(rho c_l^2) (v1 sign corrected)",
    simplify(E_int + Dxx*Sxx) == 0 and simplify(dn_RL - 2*n0*gxx*qx**2/(q2*(lam + 2*mu))) == 0)
# C5d (new; REF-A 1.2, REF-B C-4): Lorentzian double pole = (pi/eta) delta + Hadamard fp(1/x^2) + O(eta); cross term -> PV + pi delta
phi = lambda y: mp.e**(-(y - mp.mpf('0.3'))**2)
fp_ = mp.quad(lambda y: (phi(y) + phi(-y) - 2*phi(0))/y**2, [0, 1, mp.inf])                  # Hadamard fp int phi/x^2
for eta_ in [mp.mpf('1e-3'), mp.mpf('1e-4')]:
    lor = mp.quad(lambda y: phi(y)/(y**2 + eta_**2), [-mp.inf, -1, -10*eta_, 0, 10*eta_, 1, mp.inf])
    okd = abs(lor - mp.pi/eta_*phi(0) - fp_) < 5*eta_
rep("WP7T-C5d int phi/(x^2+eta^2) = (pi/eta) phi(0) + fp int phi/x^2 + O(eta)  (double pole: fp, not PV)", okd)

# ------------------------------------------------------------- C6 ohmic (electron) bath: NIBA rate vs cond-mat/9409105 Eqs.(8)-(9)
for Kv in [Q(1, 20), Q(1, 5), Q(7, 20)]:
    K = Kv
    lhs = 2*cos(pi*K)*Q(1, 2)*gamma(1 - 2*K)*gamma(1 + K)/(K*gamma(1 - K))   # 2cos(piK)G(0)*Theta/(Delta^2 (Theta/wc)^2K)
    rhs = gamma(K)**2/(2*gamma(2*K))                                         # NIBA: (k_f+k_b)(eps=0) in the same units
    rep(f"WP7T-C6a 2cos(piK)G(0) = (D^2/2wc)(2piT/wc)^(2K-1)Gamma(K)^2/Gamma(2K), K={K}", abs(num(lhs - rhs, 20)) < 1e-15)
# numerical NIBA integral: k_f = (D^2/4) int dt e^{i eps t} [ (piT/wc)/sinh(piT|t|) ]^{2K} e^{-i pi K sgn t}  (scaling limit)
mp.mp.dps = 30
def kf_num(K, T, eps, wc=1.0):
    f = lambda t: 2*mp.cos(eps*t - mp.pi*K)*((mp.pi*T/wc)/mp.sinh(mp.pi*T*t))**(2*K)
    return 0.25*mp.quad(f, [0, 1e-6, 1, 10, 100, mp.inf])
def kf_closed(K, T, eps, wc=1.0):
    return 0.25/wc*(2*mp.pi*T/wc)**(2*K - 1)*abs(mp.gamma(K + 1j*eps/(2*mp.pi*T)))**2/mp.gamma(2*K)*mp.e**(eps/(2*T))
for (K, T, eps) in [(0.2, 0.01, 0.0), (0.2, 0.01, 0.03), (0.35, 0.02, 0.05)]:
    a, b = kf_num(K, T, eps), kf_closed(K, T, eps)
    rep(f"WP7T-C6b NIBA golden rule = closed form (K={K}, T={T}, eps={eps}) [units D=1, wc=1]", abs(a/b - 1) < 1e-6, f"{mp.nstr(a,8)} vs {mp.nstr(b,8)}")
Ks, ep = symbols('K epsilon', positive=True)
# T << eps limit: |Gamma(K+iy)|^2 -> 2pi y^{2K-1} e^{-pi y}; k_f -> pi D^2 (eps/wc)^{2K-1}/(2 Gamma(2K) wc); K->0: pi K D^2/eps
kT0 = pi*(ep)**(2*Ks - 1)/(2*gamma(2*Ks))              # D = wc = 1
rep("WP7T-C6c T<<eps, K->0: k_f -> pi K Delta^2/eps (Korringa/Black form, 2103.06977 Eq.(8) with W_el^2 = 4K)",
    simplify(sp.limit(kT0/Ks, Ks, 0) - pi/ep) == 0)
# weak-coupling golden rule in the eigenbasis: Gamma_1 = (Delta/E)^2 J(E)/2 coth, J = 2 pi K w  ->  pi K Delta^2/E coth
J = 2*pi*Ks*Ev
rep("WP7T-C6d one-boson Gamma_1 = (Delta/E)^2 J(E)/2 coth = pi K Delta^2 coth/E", simplify((dtun/Ev)**2*J/2 - pi*Ks*dtun**2/Ev) == 0)
K09, Wel = symbols('K_2009 W_el', positive=True)
rep("WP7T-C6e maps: 2009.03804 Eq.(4) 4 pi K D^2/E = pi alpha D^2/E => alpha_ohm = 4K; 2103.06977 Eq.(8) => W_el^2 = 4 alpha_ohm = 16K",
    sp.solve(sp.Eq(4*pi*K09, pi*Ks), Ks)[0] == 4*K09 and sp.solve(sp.Eq(pi/4*Wel**2, pi*4*K09), Wel**2)[0] == 16*K09)

# ------------------------------------------------------------- C7 Arrhenius / Vineyard and crossover from 2409.02820 Eqs.(1)-(3)
f_ = 3
wm = symbols('wm1:4', positive=True); wt = symbols('wt1:3', positive=True); beta, Vb, wb = symbols('beta V_b omega_b', positive=True)
Zr = sp.prod([1/(beta*x) for x in wm]); Zts = sp.prod([1/(beta*x) for x in wt])
kTST = 1/(2*pi*beta)*Zts/Zr*exp(-beta*Vb)
vine = sp.prod(wm)/sp.prod(wt)*exp(-beta*Vb)/(2*pi)
rep("WP7T-C7a 2409.02820 Eq.(1), kappa=1, classical harmonic Z -> Vineyard (WP5 (W12))", simplify(kTST - vine) == 0)
x = symbols('x', positive=True)
kPB = (x/2)/sin(x/2)
rep("WP7T-C7b kappa_PB = 1 + x^2/24 + O(x^4) (Wigner, Eq.(2)); x = beta*omega_b", simplify(sp.series(kPB, x, 0, 4).removeO() - (1 + x**2/24)) == 0)

# ------------------------------------------------------------- C8 STM heat release after cooling T1 -> T0 (1610.03974 Eq.(6))
T1, T0, tt, lam_ = symbols('T1 T0 t lambda', positive=True)
xF = symbols("x_F", positive=True)
Ix = sp.Sum((-1)**(sp.Symbol("n", integer=True)+1)/sp.Symbol("n", integer=True)**2, (sp.Symbol("n", integer=True), 1, oo)).doit()  # int x/(e^x+1) = eta(2)
rep("WP7T-C8a int_0^oo E/(e^{E/T}+1) dE = T^2 eta(2) = pi^2 T^2/12", simplify(Ix - pi**2/12) == 0 and abs(mp.quad(lambda y: y/(mp.e**y + 1), [0, mp.inf]) - mp.pi**2/12) < 1e-20)
G0 = symbols('Gamma_0', positive=True)
lamint = integrate((G0*exp(-2*lam_))*exp(-G0*exp(-2*lam_)*tt), (lam_, 0, oo))
rep("WP7T-C8b int dlambda Gamma e^{-Gamma t} (Gamma = G0 e^{-2lambda}) = (1 - e^{-G0 t})/(2t) -> 1/(2t)", simplify(lamint - (1 - exp(-G0*tt))/(2*tt)) == 0)
Qdot = P0s/(2*tt)*(pi**2*T1**2/12 - pi**2*T0**2/12)
rep("WP7T-C8c Qdot = (pi^2/24) Pbar (T1^2 - T0^2)/t per volume  [1610.03974 Eq.(6)]", simplify(Qdot - pi**2*P0s*(T1**2 - T0**2)/(24*tt)) == 0)

# ------------------------------------------------------------- C9 1D first passage (crowdion recombination) and 3D Smoluchowski
D_, d_ = symbols('D d', positive=True)
fp = d_/sqrt(4*pi*D_*tt**3)*exp(-d_**2/(4*D_*tt))
rep("WP7T-C9a 1D first-passage density normalised: int_0^oo f(t) dt = 1", simplify(integrate(fp, (tt, 0, oo)) - 1) == 0)
rep("WP7T-C9b tail f(t) ~ d/sqrt(4 pi D) t^{-3/2}", simplify(sp.limit(fp*tt**Q(3, 2), tt, oo) - d_/sqrt(4*pi*D_)) == 0)
rc, r0 = symbols('r_c r_0', positive=True)
cap = (rc/r0)*sp.erfc((r0 - rc)/sqrt(4*D_*tt))         # 3D capture probability by time t (Smoluchowski)
rep("WP7T-C9c 3D eventual capture probability = r_c/r_0 (< 1: survival 1 - r_c/r_0)", simplify(sp.limit(cap, tt, oo) - rc/r0) == 0)
rep("WP7T-C9d 3D capture-time density ~ t^{-3/2} tail",
    simplify(sp.limit(sp.diff(cap, tt)*tt**Q(3, 2), tt, oo) - rc*(r0 - rc)/(r0*sqrt(4*pi*D_))) == 0)

# ------------------------------------------------------------- C10 crowdion (Frenkel-Kontorova, 1806.11002 Eqs.(2),(6))
zz, z0, muF, aF, m_ = symbols('z z_0 mu a m', positive=True)
u = 2*aF/pi*sp.atan(exp(-muF*(zz - z0)))
du = simplify(sp.diff(u, z0))
Mcr = simplify(m_/aF*integrate((du**2).rewrite(exp).subs(zz, zz + z0), (zz, -oo, oo)))
rep("WP7T-C10a crowdion translation mass M_cr = m sum (du_n/dz0)^2 = 2 mu a m/pi^2", simplify(Mcr - 2*muF*aF*m_/pi**2) == 0)
# W numbers [E]: a = sqrt(3)/2 * 3.165 A; mu a = 0.5 (1806.11002: mu a < 1); E_mig = 1 meV (atomistic) / ~1 ueV (FK)
aW = sqrt(3)/2*Q(3165, 1000); MW = Q(18384, 100)*amu
Mcr_W = 2*Q(1, 2)*MW/pi**2
Erec = (pi*hc/aW)**2/(2*Mcr_W)
hw0 = pi*hc/aW*sqrt(2*Q(1, 1000)/Mcr_W)
rep("WP7T-C10b W crowdion: M_cr ~ 0.10 m_W, E_rec = (pi/a)^2/2M_cr ~ 0.16 meV, hbar w0/2 ~ 0.4 meV vs E_mig = 1 meV",
    0.1 < num(Mcr_W/MW) < 0.11 and 1e-4 < num(Erec) < 2e-4 and 3e-4 < num(hw0/2) < 5e-4, f"Erec={num(Erec*1e3)} meV, hw0/2={num(hw0/2*1e3)} meV")
V0f, betaf = symbols('V_0 beta_FK', positive=True)
mu_sub = pi*sqrt(2*V0f/betaf)/aF**2; E0f = 2*aF/pi*sqrt(2*V0f*betaf); cs2 = betaf*aF**2/m_
rep("WP7T-C10c M_cr = 2 mu a m/pi^2 = E0/c_s^2: the FK/sine-Gordon kink rest mass (Braun-Kivshar), not new", simplify((2*mu_sub*aF*m_/pi**2) - E0f/cs2) == 0)
def mathieu_E(Vr, k, N=20):   # H/E_rec in plane waves e^{i(pi/a)(k+2n)z}; V = Vr sin^2(pi z/a) = Vr/2 - (Vr/4)(e^{2i pi z/a} + c.c.)
    Hm = mp.matrix(2*N + 1)
    for i_ in range(2*N + 1):
        n_ = i_ - N; Hm[i_, i_] = (k + 2*n_)**2 + mp.mpf(Vr)/2
        if i_ > 0: Hm[i_, i_ - 1] = Hm[i_ - 1, i_] = -mp.mpf(Vr)/4
    return min(mp.eigsy(Hm)[0])
Vr = mp.mpf(1)/mp.mpf(num(Erec*1000, 15))        # E_mig/E_rec with E_mig = 1 meV
bw = (mathieu_E(Vr, 1) - mathieu_E(Vr, 0))*mp.mpf(num(Erec*1000, 15))
rep("WP7T-C10d W crowdion Mathieu ground band (E_mig = 1 meV, M_cr = 0.1 m_W) ~ 0.024 meV, not sub-meV", 0.02 < bw < 0.03, f"band = {mp.nstr(bw, 4)} meV, depth/E_rec = {mp.nstr(Vr, 3)}")

# ------------------------------------------------------------- C11 defecton response: arcsine kernel and free-gas limit
Jd, qa, om, kk = symbols('J qa omega k', positive=True)
wq = 2*Jd*sin(qa/2)
# uniform k over the 1D zone: P(omega) = <delta(omega - (-2J sin(qa/2) sin(k a + qa/2)))> = 1/(pi sqrt(wq^2 - omega^2))
arcs = 1/(pi*sqrt(wq**2 - om**2))
rep("WP7T-C11a 1D band kernel normalised: int_{-w}^{w} dω/(pi sqrt(w^2-ω^2)) = 1", simplify(integrate(1/(pi*sqrt(1 - om**2)), (om, -1, 1)) - 1) == 0)
mst, qq, Tq = symbols('m_st q T_q', positive=True)
Sfg = sqrt(mst/(2*pi*qq**2*Tq))*exp(-mst*(om - qq**2/(2*mst))**2/(2*qq**2*Tq))
rep("WP7T-C11b free-gas kernel: zeroth moment 1", simplify(integrate(Sfg, (om, -oo, oo)) - 1) == 0)
rep("WP7T-C11c free-gas kernel: first moment q^2/2m* (f-sum per defecton, WP0 (4.6) form)", simplify(integrate(om*Sfg, (om, -oo, oo)) - qq**2/(2*mst)) == 0)

# ------------------------------------------------------------- C12 Franck-Condon conditional phonon occupation of a release event
# two modes, Poisson weights; A(eps) = sum_{n1,n2} p(n1)p(n2) delta(eps - n1 w1 - n2 w2); check <n1>_eps = S1 A(eps - w1)/A(eps)
S1, S2 = Q(3, 2), Q(7, 10); w1, w2 = 2, 3
def pois(n, S): return exp(-S)*S**n/sp.factorial(n)
def A(epsv):
    return sum(pois(n1, S1)*pois(n2, S2) for n1 in range(0, 20) for n2 in range(0, 20) if n1*w1 + n2*w2 == epsv)
ok = True
for epsv in [7, 9, 12, 13]:
    lhs = sum(n1*pois(n1, S1)*pois(n2, S2) for n1 in range(0, 20) for n2 in range(0, 20) if n1*w1 + n2*w2 == epsv)/A(epsv)
    ok &= simplify(lhs - S1*A(epsv - w1)/A(epsv)) == 0
rep("WP7T-C12  <n_k>_eps = S_HR,k A(eps - w_k)/A(eps) (energy-conditioned FC occupation)", ok)

# ------------------------------------------------------------- C13 rate prefactor and halo identity
v, v0s = symbols('v v_0', positive=True)
# int_0^oo v' eta(v') dv' = <|v|>/2 : check for an isotropic Maxwellian f = e^{-v^2/v0^2}/(pi^{3/2} v0^3)
vp = symbols('vp', positive=True)
fM = exp(-v**2/v0s**2)/(pi**Q(3, 2)*v0s**3)
eta = integrate(4*pi*v*fM, (v, vp, oo))                  # eta(vmin) = int d^3v f/|v| Theta(|v| - vmin)
lhs = integrate(vp*eta, (vp, 0, oo)); vmean = integrate(4*pi*v**3*fM, (v, 0, oo))
rep("WP7T-C13b int_0^oo v eta(v) dv = <|v|>/2, i.e. xi(0) = <|v|> (CONVENTIONS sec.8 xi)", simplify(lhs - vmean/2) == 0)

# ------------------------------------------------------------- C14 numbers [E]
# a-SiO2: n_at = 6.6e22 cm^-3, rho = 2.2 g/cm^3, c_l = 5.8 km/s, Zbar = 10, C_l = Pbar gamma_l^2/(rho c_l^2) = 3e-4
rho_c2_eVcm3 = Q(2200)*Q(5800)**2/eV_J*Q(1, 10**6)       # Pa = J/m^3 -> eV/cm^3
nat = Q(66, 10)*10**22
vertex = 2*Q(10)*nat*1/rho_c2_eVcm3                      # |f_e| for gamma = 1 eV, qhat.gamma.qhat = 1 eV
rep("WP7T-C14a a-SiO2 static electron vertex |f_e| = 2 Zbar n_at gamma/(rho c_l^2) ~ 2.9 (gamma = 1 eV)", 2.5 < num(vertex) < 3.3, f"{num(vertex)}")
eff = Q(10)**2*nat**2*Q(3, 10**4)/rho_c2_eVcm3           # Pbar|f_e|^2/4 = Zbar^2 n^2 C_l/(rho c_l^2) [eV^-1 cm^-3]
per_g = eff/Q(22, 10)
flux_sig = Q(3, 10)*10**9/10**6*Q(33, 10)*10**7*Q(1, 10**38)   # n_chi<v>sigma for m=1 MeV, <v>=330 km/s, sigma=1e-38 cm^2 [s^-1]
rate = flux_sig*per_g*1000*86400/1000                    # host term only, m_chi << m_e form (v1)
me_ = Q(51099895, 100)
fac = (1 + Q(10)**6/me_)**2                               # (m_chi/mu_chie)^2, REF-B C-2
# one consistent halo (R12 clean-up, VER-A N2 / VER-B 3(i)): boosted Maxwellian, v0 = 238, v_E = |v_sun| = 250.5 km/s, no escape cut [E]
cl_ = mp.mpf(299792.458); v0n = 238/cl_; vEn = mp.mpf('250.5')/cl_; mchi = 1e6; dA = 1.0
etaM = lambda uu: (mp.erf((uu + vEn)/v0n) - mp.erf((uu - vEn)/v0n))/(2*vEn)
vmean_h = 2*mp.quad(lambda uu: uu*etaM(uu), [0, mp.inf])           # xi(0) = <|v|> of the same halo
qA = lambda uu: 2*mchi*uu/float(hc)
Rcore = mp.quad(lambda uu: uu*etaM(uu)*2*64*(1 - mp.sin(qA(uu)*dA)/(qA(uu)*dA)), [0, mp.mpf('1e-3'), mp.inf])/mp.quad(lambda uu: uu*etaM(uu)*num(vertex)**2, [0, mp.inf])
host2 = num(rate*fac)*(vmean_h*cl_/330)                           # v1 number used <|v|> = 330 km/s; rescale to this halo
rate2 = host2*(1 + Rcore)
rep("WP7T-C14b a-SiO2 TLS rate, m=1 MeV, sigma_e=1e-38, boosted SHM: host x (m/mu)^2 ~ 1.0e-2; + O-core (Re(a*B)=0, exact sum) R_core ~ 2.6 -> ~3.7e-2 /(kg day meV)",
    8.5 < num(fac) < 9 and 340 < vmean_h*cl_ < 375 and 0.95e-2 < host2 < 1.15e-2 and 2.2 < Rcore < 2.9 and 3.2e-2 < rate2 < 4.2e-2,
    f"fac={num(fac)}, <v>={mp.nstr(vmean_h*cl_,4)} km/s, Rcore={mp.nstr(Rcore,3)}, rate={mp.nstr(rate2,3)}")
Pbar_con = Q(3, 10**4)*rho_c2_eVcm3                       # P = C rho c^2/gamma^2, gamma = 1 eV
rep("WP7T-C14b' consistent Pbar for C_TLS = 3e-4, gamma_l = 1 eV: 1.4e20 eV^-1 cm^-3 = 8.6e44 J^-1 m^-3", 1.3e20 < num(Pbar_con) < 1.5e20 and 8e44 < num(Pbar_con*10**6/eV_J) < 9.2e44)
# tunnelling window: Gamma ~ w0 e^{-2lambda} >= 1/yr with w0 = 1e13 s^-1 -> lambda <= 24; Si mass, d = 1 A -> V <= 43 meV
lam_max = sp.log(Q(10)**13*Q(31557600))/2
MSi = Q(2809, 100)*amu
Vmax = (2*lam_max*hc/1)**2/(2*MSi)                       # Phillips/Jaeckle lambda = (d/2) sqrt(2MV)
rep("WP7T-C14d mK window lambda_P <= 23.6 for 1/yr (Gamma_att = 1e13/s); Si mass, d = 1 A: V <= ~166 meV (Phillips convention)", 23 < num(lam_max) < 25 and 0.15 < num(Vmax) < 0.18, f"lam={num(lam_max)}, V={num(Vmax*1000)} meV")
lamH = Q(117, 200)*sqrt(2*Q(93827, 100)*10**6*Q(1, 10))/hc     # H in Nb: d=1.17 A, V=0.1 eV
lamFP = Q(15, 20)*sqrt(2*MSi*Q(1, 10))/hc                       # Si close pair: d=1.5 A, V=0.1 eV
lamAl = Q(14, 20)*sqrt(2*Q(2698, 100)*amu*Q(1, 10))/hc          # Al SIA: d=1.4 A, V=0.1 eV [UNVERIFIED inputs]
rep("WP7T-C14e lambda_P: H/Nb ~ 4.1, Si FP ~ 27.5 (quartic x4/3: 37), Al ~ 25 -> at the window edge, not robustly frozen",
    3.8 < num(lamH) < 4.4 and 27 < num(lamFP) < 28 and 24 < num(lamAl) < 26 and 36 < num(lamFP*Q(4, 3)) < 37.5, f"{num(lamH)}, {num(lamFP)}, {num(lamAl)}")
# photon vs phonon emission of a TLS relaxation: ratio ~ (4/3) alpha d^2 rho c^5 ... order (c_l/c)^5 * (rho d^2 ...) -> check (c_l/c)^5
# dark-photon absorption on TLS: Im(-1/eps) = eps2/|eps|^2 = tan(delta)/eps_r/(1 + tan^2) -> tan(delta)/eps_r
e1, td = symbols('epsilon_1 tdelta', positive=True)
rep("WP7T-C14g Im(-1/eps) = tan(delta)/(eps_1(1+tan^2 delta))", simplify(sp.im(-1/(e1 + sp.I*e1*td)) - td/(e1*(1 + td**2))) == 0)

# photon vs phonon branch of a TLS relaxation: Gamma_rad/Gamma_ph = (8 pi/3) alpha d^2 rho c_t^5 / gamma^2 (HL, p = e d, one transverse branch)
cm = Q(50677307, 1000)                                    # 1 cm in eV^-1 (1/(hbar c))
rho_nat = Q(22, 10)*Q(560958865, 10**9)*10**33/cm**3       # 2.2 g/cm^3 in eV^4
dnat = Q(1, 10**8)*cm; ct = Q(3750)/Q(299792458); alpha = 1/Q(137036, 1000)
ratio = Q(8, 3)*pi*alpha*dnat**2*rho_nat*ct**5/1
rep("WP7T-C14h Gamma_rad/Gamma_ph ~ 5e-14 (d = 1 A, gamma = 1 eV, a-SiO2 transverse)", 1e-14 < num(ratio) < 1e-13, f"{num(ratio)}")


# ------------------------------------------------------------- C15 energy-gap law vs strong coupling (REF-A 1.10, REF-B C-7)
pgap = exp(-1)*Q(1)**17/sp.factorial(17)
rep("WP7T-C15a weak coupling (S_HR = 1, eps = 1 eV, w_p = 60 meV, p = 17): Poisson weight ~ 1.0e-15 -> extra Delta lambda ~ 17.2",
    0.9e-15 < num(pgap) < 1.2e-15 and 17 < num(-sp.log(pgap)/2) < 17.5, f"{num(pgap)}")
# strong coupling: Poisson(S) -> Gaussian of mean S, variance S (local CLT) : check at S = 400, n = S
Sbig = 400
pois_max = mp.e**(-Sbig)*mp.mpf(Sbig)**Sbig/mp.factorial(Sbig)
rep("WP7T-C15b strong coupling S_HR >> 1: Poisson peak -> 1/sqrt(2 pi S) (Gaussian/Marcus, no gap suppression at eps = E_reorg)",
    abs(pois_max*mp.sqrt(2*mp.pi*Sbig) - 1) < 1e-3)

# ------------------------------------------------------------- C16 release-path sum rule (WP7-E IF-E2): telescoping identity
# absorbing Markov chain: transient {1,2,3} (start 1), absorbing {4 (perfect), 5 (frozen)}; energies E_i; rates exact rationals
Econf = [None, Q(5), Q(3), Q(4), Q(0), Q(2)]
Rt = {(1,2):Q(3),(1,3):Q(1),(2,1):Q(1,2),(2,4):Q(2),(2,5):Q(1),(3,2):Q(2),(3,5):Q(1,3),(3,1):Q(1,5)}
tr = [1,2,3]; ab = [4,5]
out = {i: sum(v for (a_,b_),v in Rt.items() if a_ == i) for i in tr}
P = sp.zeros(3,3); B = sp.zeros(3,2)
for (a_,b_),v in Rt.items():
    if b_ in tr: P[tr.index(a_), tr.index(b_)] = v/out[a_]
    else: B[tr.index(a_), ab.index(b_)] = v/out[a_]
Nf = (sp.eye(3) - P).inv()                                  # expected visits
absP = Nf*B
expected_release = sum(Nf[0, tr.index(i)]*sum(v/out[i]*(Econf[i] - Econf[j]) for (a_,j),v in Rt.items() if a_ == i) for i in tr)
rhs = Econf[1] - sum(absP[0, k]*Econf[ab[k]] for k in range(2))
rep("WP7T-C16 sum_path P_path eps_path = E_st - <E_st^unrel(t->oo)> exactly (uphill hops with eps < 0; Sum N_i = 1)", simplify(expected_release - rhs) == 0, f"{expected_release} = {rhs}")

# C16b: Theorem T-1 with time-dependent (stimulated) rates Gamma_ij(t) = Gamma_ij (1 + 0.8 sin 3t): released energy up to t
#       equals E_c - sum_i N_i(t) E_i, and sum_i N_i stays 1 (closed linear single-seed chain)
Ef = [float(x) for x in Econf[1:]]
Rf = {(a_-1, b_-1): float(v) for (a_, b_), v in Rt.items()}
def rhs_ode(t, y):
    N = y[:5]; f = 1 + 0.8*mp.sin(3*t)
    dN = [mp.mpf(0)]*5; rel = mp.mpf(0)
    for (a_, b_), v in Rf.items():
        flux = v*f*N[a_]; dN[a_] -= flux; dN[b_] += flux; rel += flux*(Ef[a_] - Ef[b_])
    return dN + [rel]
sol = mp.odefun(rhs_ode, 0, [1, 0, 0, 0, 0, 0])
yT = sol(mp.mpf(2))
lhs16 = yT[5]; rhs16 = Ef[0] - sum(yT[i]*Ef[i] for i in range(5))
rep("WP7T-C16b T-1 holds for time-dependent stimulated rates; Sum N_i(t) = 1", abs(lhs16 - rhs16) < 1e-10 and abs(sum(yT[:5]) - 1) < 1e-10, f"{mp.nstr(lhs16,10)} vs {mp.nstr(rhs16,10)}")

print(f"\n{sum(RES)}/{len(RES)} PASS")
import sys; sys.exit(0 if all(RES) else 1)
