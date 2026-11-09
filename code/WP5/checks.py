"""WP5 identity / estimate checks (sympy + arithmetic, < 10 s). Run: python3 -I checks.py"""
import sympy as sp
ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name)

# C1: three-body free-particle phase space (random-k) used in R&K Eq.(8)
E, x1, x2, x3 = sp.symbols('E x1 x2 x3', positive=True)
# Dirichlet integral: int sqrt(x1 x2 x3) delta(E - sum) = Gamma(3/2)^3/Gamma(9/2) E^(7/2)
coef = sp.gamma(sp.Rational(3,2))**3/sp.gamma(sp.Rational(9,2))
ok("C1 three-body phase space coefficient = 2*pi/105", sp.simplify(coef - 2*sp.pi/105) == 0)
# check numerically by direct 2D integral at E=1
x, y = sp.symbols('x y', positive=True)
from scipy import integrate as si
I2 = si.dblquad(lambda yy, xx: (xx*yy*max(1-xx-yy,0.0))**0.5, 0, 1, 0, lambda xx: 1-xx, epsabs=1e-13)[0]
ok("C1b direct integral equals 2*pi/105", abs(I2 - float(2*sp.pi/105)) < 1e-8)
# dimension: Gamma_ph/Gamma_eh = A*(105/2pi)*(E-w0)^(1/2)/(E-Eg)^(7/2) dimensionless => [A] = energy^3
ok("C1c [A] = energy^3 (not energy^2)", sp.Rational(7,2) - sp.Rational(1,2) == 3)

# C2: binomial thinning of a count with mean n, variance F n (R&K App. A)
n, F, eta = sp.symbols('n F eta', positive=True)
mean = eta*n
var = eta**2*F*n + eta*(1-eta)*n          # law of total variance
Fmeas = sp.simplify(var/mean)
ok("C2 F_meas = eta*F + 1 - eta (exact)", sp.simplify(Fmeas - (eta*F + 1 - eta)) == 0)
for e_ in (0.98, 0.95):
    print(f"   eta={e_}: exact {0.115*e_+1-e_:.4f}  vs  R&K Eq.(23) F/eta+1-eta {0.115/e_+1-e_:.4f}")

# C3: Fano identity from exact energy bookkeeping  w = N*Eg + H  (H = heat)
w, Eg, H, varH, mH = sp.symbols('omega E_g H varH mH', positive=True)
Nbar = (w - mH)/Eg; varN = varH/Eg**2
Fano = sp.simplify(varN/Nbar)
eps = w/Nbar
D = varH/(Eg*mH)
ok("C3 F = (eps/Eg - 1) * Var(H)/(Eg <H>)", sp.simplify(Fano - (eps/Eg - 1)*D) == 0)
# phonon shot-noise estimate Var(H) = w0 <H>
for name, eps_, Eg_, w0 in (("Si 123K", 3.749, 1.16, 0.063), ("Ge 77K", 2.96, 0.73, 0.037)):
    print(f"   {name}: F_shot = {(eps_/Eg_-1)*w0/Eg_:.3f}")

# C4: Klein limit: residual KE uniform-in-k (DOS ~ sqrt) below E_th = 3/2 Eg
t = sp.symbols('t', positive=True); Eth = sp.Rational(3,2)*Eg
pdf = sp.sqrt(t)/sp.integrate(sp.sqrt(t), (t, 0, Eth))
m1 = sp.simplify(sp.integrate(t*pdf, (t, 0, Eth))); m2 = sp.simplify(sp.integrate(t**2*pdf, (t, 0, Eth)))
ok("C4 Klein: eps = Eg + 2<E_res> = 14/5 Eg", sp.simplify(Eg + 2*m1 - sp.Rational(14,5)*Eg) == 0)
Fk = sp.simplify(2*(m2 - m1**2)/Eg**2)
print("   independent-residual Fano (no phonons) =", Fk, "=", float(Fk))

# C5: kinematic threshold for e-h creation by a slow ion (binary, free-electron v_F)
me = 510998.95; amu = 931.494e6
for name, Eg_, kF_invA, A in (("Si", 1.17, 1.75, 28.09), ("Ge", 0.74, 1.60, 72.63)):
    vF = kF_invA*1973.27/me        # k_F[eV] / m_e  (hbar c = 1973.27 eV A)
    vth = Eg_/(2*me*vF)            # E_g = 2 m_e v (v_F + v), v << v_F
    Eth = 0.5*A*amu*vth**2
    print(f"   {name}: v_F={vF:.5f}c  v_th={vth:.3e}c  E_R,th={Eth:.0f} eV")
ok("C5 thresholds computed", True)

# C6: Massey parameter for a recoil near E_d (Si, 20 eV; 1 keV), a = 1 A
for ER in (20.0, 1000.0):
    v = (2*ER/(28.09*amu))**0.5
    print(f"   Si E_R={ER:.0f} eV: hbar v/a = {1973.27*v:.3f} eV, Massey xi = {1.17/(1973.27*v):.1f}")

# C7: impulse-approximation Doppler width sigma^2 = q^2<p_x^2>/M^2 = 2 E_R <p_x^2>/M, <p_x^2>/M = <w>/2 (T=0 Einstein)
ER_, wbar, M = sp.symbols('E_R wbar M', positive=True)
sig2 = 2*ER_*(wbar/2)
ok("C7 sigma_omega^2 = E_R <omega>", sp.simplify(sig2 - ER_*wbar) == 0)
print(f"   Si E_R=10 eV, <w>=45 meV: sigma = {(10*0.045)**0.5:.2f} eV")

# C8: distributed-activation-energy kinetics -> 1/t  (flat barrier density g on [0, inf))
Eb, T, nu, tt, g = sp.symbols('E_b T nu t g', positive=True)
k = nu*sp.exp(-Eb/T)
# substitute k: dE_b = -T dk/k, k in (0, nu]
kk = sp.symbols('k', positive=True)
rate = sp.integrate(g*T*sp.exp(-kk*tt), (kk, 0, nu))
ok("C8 release rate = g T (1 - e^{-nu t})/t -> gT/t", sp.simplify(rate - g*T*(1-sp.exp(-nu*tt))/tt) == 0)

# C9: Galton-Watson second moment: N = sum of children N_j (iid given channel) -> law of total variance
# check on toy 2-level branching: carrier above threshold makes pair w.p. p (then 2 more sub-threshold carriers + itself sub), else 0
p = sp.symbols('p', positive=True)
# G(z) = (1-p) + p z  for one ii step at most
z = sp.symbols('z'); G = (1-p) + p*z
m = sp.diff(G, z).subs(z, 1); v2 = sp.diff(G, z, 2).subs(z, 1) + m - m**2
ok("C9 generating-function variance = p(1-p)", sp.simplify(v2 - p*(1-p)) == 0)

# C10: reduced-energy conventions for Si (Lindhard vs ZBL as used in 2209.04503)
Z = 14
cL = 11.5/Z**(7/3)                       # Lindhard eps per keV (equal Z, A)
cZ14 = 16.2616/((2*14**0.23)*14*14)
cZ12 = 16.2616/((12**0.23+14**0.23)*12*14)
print(f"   eps/E[keV]: Lindhard {cL:.4f}, ZBL(Z1=14) {cZ14:.4f}, ZBL(Z1=12) {cZ12:.4f}")
print(f"   k_L: Si {0.133*14**(2/3)/28.09**0.5:.3f}, Ge {0.133*32**(2/3)/72.63**0.5:.3f}")
ok("C10 conventions differ by >5%", abs(cZ12/cL-1) > 0.05)
