"""WP3 (R5) identity checks. Theory-only campaign: sympy/numpy identities, < 30 s total.
Run: python3 -I checks.py   (each check prints PASS/FAIL and the residual)
Labels C1..C10 are cited in returns/R5/WP3.md.
"""
import numpy as np
import sympy as sp
from math import factorial

ok = []
def report(name, cond, info=""):
    ok.append(bool(cond)); print(f"{name:58s} {'PASS' if cond else 'FAIL'} {info}")

# ---------------------------------------------------------------- C1  X1 vs WP0 (4.9)
# scalar projections along e (polarisation) and Qhat; vc=Qhat.v_c, Pc=e.P_c, Dc=Qhat.D^c.e, etc.
q, c, vc, vv, Pc, Pv, Dc, Dv = sp.symbols('q c v_c v_v P_c P_v D_c D_v', real=True)
for s in (+1, -1):                       # s=+1 emission (upper sign), -1 absorption
    Xic, Xiv = Dc + vc*Pc, Dv + vv*Pv     # X1 eq. (X2): lab-frame slope Xi = D + v (x) P
    X1p = (q - Pc + Pv) + Xic/(vc + s*c) - Xiv/(vv + s*c)                    # X1 eq. (X1')
    X1  = q + (Dc - s*c*Pc)/(vc + s*c) - (Dv - s*c*Pv)/(vv + s*c)            # X1 eq. (X1)
    report(f"C1a X1' == X1 (sign {s:+d})", sp.simplify(X1p - X1) == 0)
    WP0_lab = q + Xic/(vc + s*c) - Xiv/(vv + s*c)                             # WP0 (4.9), Xi read as lab slope
    WP0_com = q + Dc/(vc + s*c) - Dv/(vv + s*c)                               # WP0 (4.9), Xi read as D
    d_lab = sp.simplify(WP0_lab - X1); d_com = sp.simplify(WP0_com - X1)
    report(f"C1b WP0(4.9)-X1 (lab reading) = Pc-Pv (sign {s:+d})", sp.simplify(d_lab - (Pc - Pv)) == 0, str(d_lab))
    report(f"C1c WP0(4.9)-X1 (comoving reading) != 0 (sign {s:+d})", d_com != 0, str(sp.factor(d_com)))
    ext = {vc: 0, vv: 0, Pc: 0, Pv: 0}
    report(f"C1d agree at band extrema (sign {s:+d})", sp.simplify((WP0_lab - X1).subs(ext)) == 0 and
           sp.simplify((WP0_com - X1).subs(ext)) == 0)
# C7e synthetic branch: g=[A,H] => g_nn = 0 => D = -v P (Xi=0), omega_Q->0 gives D2 form q-(Pc-Pv)
X1e = (q + (Dc - c*Pc)/(vc + c) - (Dv - c*Pv)/(vv + c)).subs({Dc: -vc*Pc, Dv: -vv*Pv})
report("C1e C7e (Xi=0) -> D2 form q - Pc + Pv", sp.simplify(X1e - (q - Pc + Pv)) == 0)

# ---------------------------------------------------------------- C2  KKL eq.(5)->(6) and URF normalisation
al, w, k, V = sp.symbols('alpha omega k V', positive=True)
eps2, eps1 = sp.symbols('epsilon_2 epsilon_1', real=True)
# KKL (5): (4 pi a)^2/w^4 * |vN.k|^2/k^4 * (1/V) sum|rho|^2 delta / |eps|^2,  Lindhard: eps2 = 4 pi^2 a/(V k^2) sum|rho|^2 delta
sum_rho = eps2*V*k**2/(4*sp.pi**2*al)
kkl5 = (4*sp.pi*al)**2/w**4/k**4*sum_rho/V/(eps1**2 + eps2**2)
kkl6 = 4*al/(w**4*k**2)*eps2/(eps1**2 + eps2**2)
report("C2a KKL (5) == (6) integrand", sp.simplify(kkl5 - kkl6) == 0)
# URF: S^X = (1/2pi) (q.p)^2 U^2/(M^2 w^4) S_ee S^G,  U = Z e^2/p^2, S_ee = (2p^2/e^2) Im(-1/eps), e^2 = 4 pi alpha
Z, p, M, qq, L = sp.symbols('Z p M qdotp L', positive=True)
e2 = 4*sp.pi*al
urf = (1/(2*sp.pi))*qq**2*(Z*e2/p**2)**2/(M**2*w**4)*(2*p**2/e2)*L
kkl = 4*al*Z**2*qq**2/(M**2*w**4*p**2)*L
report("C2b URF S^X/S^G == KKL dP/dw integrand", sp.simplify(urf - kkl) == 0)

# ---------------------------------------------------------------- C3  2603.13052 eq.(4.7) vs KKL
mN, Q = sp.symbols('m_N q', positive=True)
kkl_avg = 4*al*Q**2/(3*mN**2*w**4)        # KKL (6) after <(qhat.khat)^2> = 1/3
bem_47  = 2*al*Q**2/(3*w**4*mN)           # 2603.13052 (4.7) as printed
ratio = sp.simplify(bem_47/kkl_avg)
report("C3a 2603.13052(4.7)/KKL = mN/2 (dimensionful => typo + factor 1/2)", sp.simplify(ratio - mN/2) == 0, str(ratio))
# their dsigma/dq = q sigma/(mu^2 v^2) vs standard q sigma/(2 mu^2 v^2): factor 2 compensates
report("C3b product dsigma/dq * dP/dw invariant if m_N->m_N^2", sp.simplify(2*(bem_47/mN) / kkl_avg - 1) == 0)

# ---------------------------------------------------------------- C4  Migdal energy sum rule = drag mass (HO 'atom')
m, wo, kk = sp.symbols('m omega_0 k', positive=True)
lam = kk**2/(2*m*wo)                                  # |<n|e^{-ikx}|0>|^2 = e^{-lam} lam^n/n!  (HO)
n = sp.symbols('n', integer=True, nonnegative=True)
Esum = sp.summation(n*wo*sp.exp(-lam)*lam**n/sp.factorial(n), (n, 0, sp.oo))
report("C4a sum_n E_n |<n|e^{-ik x}|0>|^2 = k^2/2m (exact boost)", sp.simplify(Esum - kk**2/(2*m)) == 0)
# Born-Huang drag mass: 2 sum |<n|dV/dR|0>|^2/E_n^3, V = m w^2 (x-R)^2/2 -> only n=1, |<1|x|0>|^2 = 1/(2 m w)
dM = 2*(m*wo**2)**2*(1/(2*m*wo))/wo**3
report("C4b drag mass 2 sum|dV|^2/dE^3 = m_e (bound electron dragged)", sp.simplify(dM - m) == 0)
# Migdal omega_e-moment (dipole, q_e = m q/M) equals q^2 dM/(2 M^2)
Mn = sp.symbols('M', positive=True)
mom = (m*Q/Mn)**2*wo*(1/(2*m*wo))
report("C4c W_e = q^2 dM/(2M^2)", sp.simplify(mom - Q**2*dM/(2*Mn**2)) == 0)

# ---------------------------------------------------------------- C5  partial mixed e-N sum rule (J7), numerical SOS
def ho_matrix_exp(a, N, mu, w0):
    """<m|exp(-i a rho)|n> for a 1D HO (mass mu, freq w0) in an N-state basis, via expm of the position matrix."""
    x0 = 1/np.sqrt(2*mu*w0)
    X = np.zeros((N, N))
    for j in range(N-1):
        X[j, j+1] = X[j+1, j] = x0*np.sqrt(j+1)
    ev, U = np.linalg.eigh(X)
    return (U*np.exp(-1j*a*ev)) @ U.T.conj()
Mnuc, me, w0, qv = 50.0, 1.0, 1.0, 0.9
mA = Mnuc + me; mu = Mnuc*me/mA; alpha_, beta_ = Mnuc/mA, me/mA
N = 160
A = ho_matrix_exp(-alpha_*qv, N, mu, w0)    # e^{+i alpha q rho}  (n_e internal part)
B = ho_matrix_exp(beta_*qv, N, mu, w0)      # e^{-i beta q rho}   (n_N internal part)
E = w0*np.arange(N)
Adag = A.conj().T
sos = np.sum((E - E[0])*(Adag[0, :]*B[:, 0] + B[0, :]*Adag[:, 0])).real
F = np.exp(-qv**2/(4*mu*w0))                # <e^{-i q rho}> for HO ground state
pred = -(qv**2/mA)*F
report("C5  electronic part of M1_eN = -(q^2/m_A) F(q)", abs(sos - pred) < 1e-8, f"sos={sos:.10f} pred={pred:.10f}")

# ---------------------------------------------------------------- C6  Williams-Lax vs exact
nB, Dl, wq, Mq = sp.symbols('n Delta omega_Q M2', positive=True)
exact_m1 = Mq*((nB+1)*(Dl+wq) + nB*(Dl-wq)); WL_m1 = Mq*(2*nB+1)*Dl
report("C6a HT sideband: M1(exact)-M1(WL) = omega_Q |M|^2 (T-indep.)", sp.simplify(exact_m1 - WL_m1 - Mq*wq) == 0)
# FC (linear energy coupling) displaced oscillator, T=0: Poisson vs Lax Gaussian, moments 1,2 equal, 3rd differs
S_hr, wp, E00 = 0.7, 1.0, 0.0
nn = np.arange(80); P = np.exp(-S_hr)*S_hr**nn/np.array([float(factorial(int(i))) for i in nn])
en = E00 + nn*wp
m1, m2 = np.sum(P*en), np.sum(P*en**2)
Evert = E00 + S_hr*wp; varL = S_hr*wp**2
report("C6b FC: exact 1st moment = Lax (vertical)", abs(m1 - Evert) < 1e-12)
report("C6c FC: exact variance = Lax variance", abs(m2 - m1**2 - varL) < 1e-12)
m3c = np.sum(P*(en - m1)**3)
report("C6d FC: 3rd central moment differs (Lax 0, exact S w^3)", abs(m3c - S_hr*wp**3) < 1e-10, f"{m3c:.6f}")

# ---------------------------------------------------------------- C7  phonon-mediated propagator
we, wk = sp.symbols('omega_e omega_k', positive=True)
prop = (1/(2*Mn*wk))*2*wk/(we**2 - wk**2)
ser = sp.series(prop, wk, 0, 4).removeO()
report("C7  vertex^2 x D = 1/(M w_e^2) (1 + w_k^2/w_e^2 + ...)", sp.simplify(ser - (1/(Mn*we**2))*(1 + wk**2/we**2)) == 0)

# ---------------------------------------------------------------- C8  bremsstrahlung: atomic limit of Z*(w) and K-P eq.(8)
alpha_w = sp.symbols('alpha_w')
fw = sp.symbols('f')
Zstar_atom = -m*w**2*alpha_w/al                # Gaussian units e^2 = alpha
report("C8a Z*_atom(w) = f(w) given alpha(w) = -alpha f/(m w^2) [K-P]", sp.simplify(Zstar_atom.subs(alpha_w, -al*fw/(m*w**2)) - fw) == 0)
report("C8b w->inf: alpha(w) -> -Z alpha/(m w^2) gives Z* -> Z", sp.simplify(Zstar_atom.subs(alpha_w, -Z*al/(m*w**2)) - Z) == 0)
vN, ER = sp.symbols('v_N E_R', positive=True)
KP8 = 4*al/(3*sp.pi*w)*ER/Mn*fw**2
larmor = 2*al/(3*sp.pi*w)*vN**2*fw**2
report("C8c K-P (8) == Larmor photon number with v_N^2 = 2E_R/M", sp.simplify(KP8.subs(ER, Mn*vN**2/2) - larmor) == 0)

# ---------------------------------------------------------------- C9  Si/Ge numbers (eV units)
amu = 931.494e6
MSi, MGe = 28.0855*amu, 72.630*amu
num = {}
num['q_imp_Si [keV] sqrt(2 M 0.04eV)'] = np.sqrt(2*MSi*0.040)/1e3
num['q_imp_Ge [keV] sqrt(2 M 0.025eV)'] = np.sqrt(2*MGe*0.025)/1e3
num['q_EFT_Si [keV] sqrt(2 M 1.12eV)'] = np.sqrt(2*MSi*1.12)/1e3
num['q_EFT_Ge [keV] sqrt(2 M 0.67eV)'] = np.sqrt(2*MGe*0.67)/1e3
me_eV = 0.51099895e6
num['dM/M Si (14 e dragged, upper bound)'] = 14*me_eV/MSi
num['dM/M Ge (32 e dragged, upper bound)'] = 32*me_eV/MGe
vN_ = 100e3/MSi; num['v_N p/w_e (Si, q=100keV, p=5keV, w=5eV)'] = vN_*5e3/5.0
for kx, vx in num.items():
    print(f"   C9 {kx:48s} {vx:.4g}")
report("C9  Si EFT bound ~250 keV (matches 2210.06490 fn.3)", 230 < num['q_EFT_Si [keV] sqrt(2 M 1.12eV)'] < 260)

# ---------------------------------------------------------------- C10 dark photon: kappa_eff^2 sigma1 = kappa^2 m Im(-1/eps)
s1, s2, mv = sp.symbols('sigma_1 sigma_2 m_V', positive=True)
Pi = -sp.I*(s1 + sp.I*s2)*mv                       # 1608.01994 eq.(3)
epsv = 1 - Pi/mv**2
lhs = mv**4*s1/((mv**2 - sp.re(Pi))**2 + sp.im(Pi)**2)   # eq.(6)x sigma1
rhs = mv*sp.im(-1/epsv)
report("C10 kappa_eff^2 sigma_1 == m Im(-1/eps)  [1608.01994 (6),(7) vs WP0 9.3]", sp.simplify(lhs - rhs) == 0)

print(f"\n{sum(ok)}/{len(ok)} checks PASS")
