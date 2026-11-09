#!/usr/bin/env python3
"""R12 / WP7-B1-v2 checks (v1 checks plus independent C7, C12c; C1c general; C3c Landau damping) (sympy exact where possible; mpmath/scipy quadrature for C6a, C9b, C10).
Run: python3 checks.py   (target < 2 min). Every check prints PASS/FAIL; exit code 1 on any FAIL.
Labels are cited in returns/R12/WP7-B1-v2.md as WP7B1v2-Cn."""
import sys
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import integrate

RES = []


def rec(label, ok, note=""):
    RES.append((label, bool(ok)))
    print(f"{label:6s} {'PASS' if ok else 'FAIL'}  {note}")


# ---------------------------------------------------------------- C1 (E5)
# C1a: exciton (Davydov) mixing is unitary => sum_lambda |sum_kappa c*_{kappa lambda} a_kappa|^2 = sum_kappa |a_kappa|^2
th, al, be, ph = sp.symbols('theta alpha beta phi', real=True)
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2', real=True)
A = sp.cos(th) * sp.exp(sp.I * al)
B = sp.sin(th) * sp.exp(sp.I * be)
U = sp.Matrix([[A, B], [-sp.conjugate(B) * sp.exp(sp.I * ph), sp.conjugate(A) * sp.exp(sp.I * ph)]])
x = sp.Matrix([a1 + sp.I * b1, a2 + sp.I * b2])
tot = sum(sp.Abs(sum(sp.conjugate(U[k, l]) * x[k] for k in range(2))) ** 2 for l in range(2))
diff = sp.simplify(sp.expand(sp.expand_complex(tot - (a1**2 + b1**2 + a2**2 + b2**2))))
rec("C1a", diff == 0, "Frenkel: incoherent molecule sum = coherent exciton sum (bins >> Davydov splitting)")
rng = np.random.default_rng(1)
Z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
Q4, _ = np.linalg.qr(Z)
av = rng.normal(size=4) + 1j * rng.normal(size=4)
rec("C1a'", abs(np.sum(np.abs(Q4.conj().T @ av) ** 2) - np.sum(np.abs(av) ** 2)) < 1e-12, "4 molecules/cell (t-stilbene)")
# C1b: prefactors of 1912.02822 Eq.(19) and 2103.08601 Eq.(8) from WP0-v3 (3.3) with S = 2*pi*n_mol*sum|f|^2 delta
pref19 = sp.pi * 2 * sp.pi / ((2 * sp.pi) ** 3 * 2)          # |V|^2 = pi sigma/mu^2 ; 2 pi delta ; eta/(2q)
pref8 = sp.pi * 2 * sp.pi / (2 * sp.pi) ** 3
rec("C1b", sp.simplify(pref19 - 1 / (8 * sp.pi)) == 0 and sp.simplify(pref8 - 1 / (4 * sp.pi)) == 0,
    "1/(8 pi) [1912.02822 (19)], d^3q/(4 pi) [2103.08601 (8)]")
# isotropic velocity kernel: int d^3v g(v) delta(DE + q^2/2m - q.v) = (1/2q) int 4 pi v dv g Theta = eta/(2q)
v, q, c, vm = sp.symbols('v q c v_m', positive=True)
inner = sp.integrate(sp.DiracDelta(q * v * c - q * vm), (c, -1, 1))   # general v_m > 0
rec("C1c", sp.simplify(inner - sp.Heaviside(1 - vm / v) / (q * v)) == 0, "angular delta -> Theta(v - v_min)/(qv) for all v_min: G = eta/(2q)")

# ---------------------------------------------------------------- C2 (E8, 1D Luttinger)
vF, V, qq, w, g2, g4, N = sp.symbols('v_F V q omega g2 g4 N', positive=True)
gL = sp.sqrt((2 * sp.pi * vF + g4 - g2) / (2 * sp.pi * vF + g4 + g2))
vL = sp.sqrt((vF + g4 / (2 * sp.pi)) ** 2 - (g2 / (2 * sp.pi)) ** 2)
rec("C2a", sp.simplify((gL * vL).subs({g2: V, g4: V}) - vF) == 0,
    "2607.15338 Eq.(3): g v = v_F when g2 = g4 (density-density) <=> f-sum")
# 1D RPA with linear bubble, N channels: R0 = N vF q^2/(pi (w^2 - vF^2 q^2)); pole and residue
R0 = N * vF * qq**2 / (sp.pi * (w**2 - vF**2 * qq**2))
den = sp.together(1 - V * R0)
pole = sp.solve(sp.numer(den), w)
wpl = [p for p in pole if p.is_positive is not False][0]
gc = 1 / sp.sqrt(1 + N * V / (sp.pi * vF))
rec("C2b", sp.simplify(wpl - vF * qq / gc) == 0, "1D RPA plasmon v_c = v_F/g_c, g_c = (1+N V/(pi v_F))^(-1/2)")
R = sp.simplify(R0 / den)
resid = sp.simplify(sp.limit((w - wpl) * R, w, wpl))
# retarded: 1/(w - wpl + i0) -> -i pi delta, so Im R = -pi resid delta and S = -2 Im R = 2 pi resid delta
weight = sp.simplify(2 * sp.pi * resid)
rec("C2c", sp.simplify(weight - N * gc * qq) == 0, "S = N g_c |q| delta(w - v_c q) = 2607.15338 Eq.(4) (N=1)")
rec("C2d", sp.simplify(weight * wpl - N * vF * qq**2) == 0, "band-projected (Schwinger-term) sum rule: int w S = N_ch v_F q^2 (not WP0 (4.6))")
gfix = sp.symbols('g_c', positive=True)
rec("C2e", sp.simplify((N * gfix * qq).subs(N, 4) / (N * gfix * qq).subs(N, 1)) == 4 and
    sp.simplify((weight * wpl).subs({N: 4, V: 0}) - 4 * vF * qq**2) == 0,
    "fixed measured g_c: 4-channel CNT density weight = 4 x the 1-channel model of 2607.15338; free limit 4 v_F q^2")

# ---------------------------------------------------------------- C3 (E8, demon / acoustic plasmon)
k, Om, qa = sp.symbols('k Omega q', positive=True)
eps = 1 + k**2 / qa**2 - Om**2 / w**2
wa = Om * qa / sp.sqrt(qa**2 + k**2)
rec("C3a", sp.simplify(eps.subs(w, wa)) == 0, "acoustic zero of eps")
L_weight = sp.pi / sp.diff(eps, w).subs(w, wa)        # L = pi delta(w - wa)/eps'
f_share = sp.simplify(wa * L_weight / (sp.pi * Om**2 / 2))
rec("C3b", sp.simplify(f_share - (qa**2 / (qa**2 + k**2)) ** 2) == 0, "f-sum share of acoustic mode = (q^2/(q^2+k_TF^2))^2 (Pines 1956)")
v1s = sp.symbols('v_F1', positive=True)
epsI = sp.pi / 2 * k**2 / qa**2 * w / (qa * v1s)              # Landau damping by the light species (omega << q v_F1)
Gam_over_w = sp.simplify((2 * epsI / sp.diff(eps, w)).subs(w, wa) / wa)
lead = sp.limit(Gam_over_w, qa, 0)
rec("C3c", sp.simplify(lead - sp.pi / 2 * Om / (k * v1s)) == 0, "demon Landau width Gamma/w_a -> (pi/2) v_a/v_F1, v_a = w_p2/k_TF1")

# ---------------------------------------------------------------- C4 (E9)
mp.mp.dps = 30
qv, qz, Lv = mp.mpf('0.7'), mp.mpf('0.4'), mp.mpf('2.3')
lhs = mp.nsum(lambda n: 1 / (qv**2 + (qz + 2 * mp.pi * n / Lv) ** 2), [-mp.inf, mp.inf]) / Lv
rhs = mp.sinh(qv * Lv) / (2 * qv * (mp.cosh(qv * Lv) - mp.cos(qz * Lv)))
rec("C4a", abs(lhs - rhs) < mp.mpf('1e-20'), "layered-sheet Coulomb sum = (1/2q) sinh/(cosh - cos)")
Qs, Qz, Ls = sp.symbols('q q_z L', positive=True)
VL = sp.sinh(Qs * Ls) / (2 * Qs * (sp.cosh(Qs * Ls) - sp.cos(Qz * Ls)))
t = sp.symbols('t', positive=True)
small = sp.series(VL.subs({Qs: t * Qs, Qz: t * Qz}), t, 0, 0).removeO()
rec("C4b", sp.simplify(small * t**2 - 1 / (Ls * (Qs**2 + Qz**2))) == 0, "qL -> 0: 3D Coulomb with n_3D = n_2D/L")
rec("C4b'", sp.limit(VL * 2 * Qs, Ls, sp.oo) == 1, "L -> oo: isolated sheet e^2/(2q)")
e1, e2, f, s = sp.symbols('epsilon_1 epsilon_2 f s')
epar = f * e1 + (1 - f) * e2
eperp = 1 / (f / e1 + (1 - f) / e2)
emt_inv = 1 / (epar * s + eperp * (1 - s))     # s = k_parallel^2/k^2 (their k_z)
lp16 = ((1 - f) * e1 + f * e2) / (e1 * e2 + (1 - f) * f * (e1 - e2) ** 2 * s)
rec("C4c", sp.simplify(emt_inv - lp16) == 0, "2110.01587 Eq.(16) = exact uniaxial EMT (any d/L, kL << 1)")

# C4d: Rytov transfer matrix for a periodic stack of local dielectrics and its k -> 0 limit (= EMT mode condition)
kk2, d1, d2, eA, eB, tq = sp.symbols('k d_1 d_2 epsilon_A epsilon_B t', positive=True)
Mlay = lambda e_, d_: sp.Matrix([[sp.cosh(kk2 * d_), sp.sinh(kk2 * d_) / (e_ * kk2)], [e_ * kk2 * sp.sinh(kk2 * d_), sp.cosh(kk2 * d_)]])
half_tr = sp.simplify((Mlay(eB, d2) * Mlay(eA, d1)).trace() / 2)
rytov = sp.cosh(kk2 * d1) * sp.cosh(kk2 * d2) + (eA / eB + eB / eA) * sp.sinh(kk2 * d1) * sp.sinh(kk2 * d2) / 2
ok4d = sp.simplify(sp.expand((half_tr - rytov).rewrite(sp.exp))) == 0
ff = d1 / (d1 + d2)
ratio_emt = (ff * eA + (1 - ff) * eB) * (ff / eA + (1 - ff) / eB) * (d1 + d2) ** 2
ser = sp.series(rytov.subs(kk2, tq * kk2), tq, 0, 3).removeO()
coef = sp.simplify(sp.expand(ser - 1).coeff(tq, 2) * 2 / kk2**2)       # cos(q a) ~ 1 - q^2 a^2/2 => q^2 a^2 = -k^2 coef
ok4d &= sp.simplify(coef - ratio_emt) == 0
rec("C4d", ok4d, "Rytov: (1/2)tr M_B M_A = cosh cosh + (eA/eB+eB/eA)/2 sinh sinh; k->0 gives eps_par k^2 + eps_perp q_perp^2 = 0")

# ---------------------------------------------------------------- C5 (E10, dielectric sphere)
l, ei, eo, Rr, Acoef, Bcoef = sp.symbols('l epsilon_in epsilon_out R A B', positive=True)
sol = sp.solve([sp.Eq(Acoef * Rr**l, Rr**l + Bcoef * Rr**(-l - 1)),
                sp.Eq(ei * l * Acoef * Rr**(l - 1), eo * (l * Rr**(l - 1) - (l + 1) * Bcoef * Rr**(-l - 2)))],
               [Acoef, Bcoef], dict=True)[0]
rec("C5", sp.simplify(sol[Acoef] - (2 * l + 1) * eo / (l * ei + (l + 1) * eo)) == 0,
    "QD multipole local-field factor (2l+1)eps_out/(l eps_in + (l+1) eps_out)")

# ---------------------------------------------------------------- C6 (E12, 2D Dirac sheet)
def imchi0_num(qn, wn, vn=1.0, gdeg=4):
    Om_ = wn / vn

    def integrand(thv):
        cth = np.cos(thv)
        kk = (Om_**2 - qn**2) / (2 * (Om_ + qn * cth))
        kq = np.sqrt(kk**2 + qn**2 + 2 * kk * qn * cth)
        dsdk = 1 + (kk + qn * cth) / kq
        cosphi = (kk + qn * cth) / kq
        return kk * 0.5 * (1 - cosphi) / (vn * dsdk)
    val, _ = integrate.quad(integrand, 0, 2 * np.pi, limit=200)
    return -np.pi * gdeg * val / (2 * np.pi) ** 2


ok6 = True
for (qn, wn) in [(0.3, 1.0), (1.0, 1.7), (0.05, 0.4)]:
    num = imchi0_num(qn, wn)
    ana = -(4 / 16) * qn**2 / np.sqrt(wn**2 - qn**2)
    ok6 &= abs(num / ana - 1) < 1e-7
rec("C6a", ok6, "undoped graphene Im chi0 = -(g/16) q^2/sqrt(w^2 - v^2 q^2)")
z, sig, qp = sp.symbols('z sigma q', positive=True)
Aamp = sp.symbols('A')
solA = sp.solve(sp.Eq(e1 * qp * Aamp + e2 * qp * Aamp, sig), Aamp)[0]
rec("C6b", sp.simplify(solA - sig / (qp * (e1 + e2))) == 0, "sheet on substrate: V_2D = e^2/(q(eps_1+eps_2))")
n2, me, eb, e2c = sp.symbols('n_2D m e_b e2', positive=True)
w2d = sp.solve(sp.Eq(eb - (e2c / (2 * qp)) * n2 * qp**2 / (me * w**2), 0), w)
rec("C6c", any(sp.simplify(r**2 - e2c * n2 * qp / (2 * me * eb)) == 0 for r in w2d), "2D plasmon w^2 = e^2 n q/(2 m eps_bar)")

# ---------------------------------------------------------------- C7 (X6, independent): (W.5) -> dP/dw -> 2011.13352 Eq.(11)
# (a) isotropic average of [q.a][q.b] over directions of q at fixed |q|: = q^2 a.b/3 (generic vectors)
th7, ph7 = sp.symbols('theta phi', real=True)
ax, ay, az, bx, by, bz, qm = sp.symbols('a_x a_y a_z b_x b_y b_z q_m', real=True)
qh = sp.Matrix([sp.sin(th7) * sp.cos(ph7), sp.sin(th7) * sp.sin(ph7), sp.cos(th7)])
avec, bvec = sp.Matrix([ax, ay, az]), sp.Matrix([bx, by, bz])
avg = sp.integrate(sp.integrate((qm * qh.dot(avec)) * (qm * qh.dot(bvec)) * sp.sin(th7), (th7, 0, sp.pi)), (ph7, 0, 2 * sp.pi)) / (4 * sp.pi)
ok7 = sp.simplify(avg - qm**2 * avec.dot(bvec) / 3) == 0
# (b) (W.5) prefactor with U = Z e^2/p^2, S_GG' = (2|p+G||p+G'|/e^2) Im[-eps_sym^-1] (T=0), 1/(2 pi) of (W.5):
Zs, e2s, Ms, ws, Pa, Pb, cosab, alpha = sp.symbols('Z e2 M w P_a P_b c_ab alpha', positive=True)
pref_W5 = sp.Rational(1, 2) / sp.pi * (Zs * e2s / Pa**2) * (Zs * e2s / Pb**2) * (2 * Pa * Pb / e2s) * (qm**2 * Pa * Pb * cosab / 3) / (Ms**2 * ws**4)
pref_dP = 4 * alpha * Zs**2 * qm**2 * cosab / (3 * Ms**2 * ws**4)          # claimed integrand of dP/dw (per Im eps^-1, per d^3p/(2pi)^3)
ok7 &= sp.simplify(pref_W5.subs(e2s, 4 * sp.pi * alpha) - pref_dP) == 0
# (c) rate (d^3q = q^2 dq dphi dc, phi gives 2 pi): N_T rho/m int d^3v f int d^3q/(2pi)^3 |V|^2 2pi delta(q v c - q^2/2mu - w) dP/dw, angular delta done symbolically
cq, vq, muq, qq7 = sp.symbols('c v mu q', positive=True)
ang = sp.integrate(sp.DiracDelta(qq7 * vq * cq - qq7**2 / (2 * muq) - ws), (cq, -1, 1))
ang_val = sp.simplify(ang.rewrite(sp.Heaviside).subs({ws: qq7 * vq / 4, muq: 10**6 * qq7 / vq}))   # interior point
rho7, mchi7, sig7, mu7, A7, Om7, NT7, F7 = sp.symbols('rho m_chi sigma mu_n A Omega N_T F', positive=True)
dP = 4 * alpha * Zs**2 * qq7**2 * F7 / (3 * Ms**2 * ws**4 * Om7)
integrand = NT7 * rho7 / mchi7 * (A7**2 * sp.pi * sig7 / mu7**2) * 2 * sp.pi * qq7**2 / (2 * sp.pi) ** 3 * 2 * sp.pi * (1 / (qq7 * vq)) * dP
src = rho7 / mchi7 * 2 * A7**2 * sig7 * Zs**2 * alpha * NT7 / (3 * mu7**2 * Om7 * Ms**2) * (1 / vq) * qq7**3 * F7 / ws**4
ok7 &= sp.simplify(ang_val - 1 / (qq7 * vq)) == 0 and sp.simplify(integrand - src) == 0
rec("C7", ok7, "independent: angular average, (W.5) prefactor 4 alpha Z^2 q^2/(3M^2 w^4), angular delta -> 2011.13352 Eq.(11)")

# ---------------------------------------------------------------- C8 (X8, hydrogenic bound-state Migdal)
r, cc, kk_ = sp.symbols('r c k', positive=True)
psi1s = sp.exp(-r) / sp.sqrt(sp.pi)
psi2p_ang = r * sp.exp(-r / 2) / (4 * sp.sqrt(2 * sp.pi))      # times cos(theta)
ang = sp.integrate(cc * sp.exp(sp.I * kk_ * r * cc), (cc, -1, 1))
amp = 2 * sp.pi * sp.integrate(sp.simplify(r**2 * psi2p_ang * psi1s * ang), (r, 0, sp.oo))
P = sp.simplify(sp.Abs(sp.simplify(amp)) ** 2)
P_closed = sp.Rational(2**15, 3**10) * kk_**2 / (1 + sp.Rational(4, 9) * kk_**2) ** 6
rec("C8", sp.simplify(P - P_closed) == 0, "P(1s->2p0) = (2^15/3^10) q_e^2 a^2/(1 + 4 q_e^2 a^2/9)^6; dipole limit (2^15/3^10) q_e^2")

# ---------------------------------------------------------------- C9 (A2)
Wv, wD, lam, Wp = sp.symbols('omega omega_D lambda Omega', positive=True)
Acoef2 = 2 * lam / wD**4                                     # alpha^2F_tr = A Omega^4 below omega_D, lambda_tr = 2 int a2F/Omega
lo = sp.simplify(2 * sp.pi / Wv * sp.integrate((Wv - Wp) * Acoef2 * Wp**4, (Wp, 0, Wv)))
hi = sp.simplify(2 * sp.pi / Wv * sp.integrate((Wv - Wp) * Acoef2 * Wp**4, (Wp, 0, wD)))
rec("C9a", sp.simplify(lo - sp.Rational(2, 15) * sp.pi * lam * Wv**5 / wD**4) == 0 and
    sp.simplify(hi - sp.Rational(4, 5) * sp.pi * lam * wD * (1 - sp.Rational(5, 6) * wD / Wv)) == 0,
    "Allen 1/tau(w) with Debye a2F = 1604.06800 Eq.(16) (both branches)")
mp.mp.dps = 20
ok9 = True
for Dl in [mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf('0.45')]:
    x_ = mp.mpf(1)
    b = 2 * Dl / x_
    fI = lambda E: (E * (x_ - E) + Dl**2) / (mp.sqrt(E**2 - Dl**2) * mp.sqrt((x_ - E) ** 2 - Dl**2))
    fII = lambda E: (E * (x_ - E) - Dl**2) / (mp.sqrt(E**2 - Dl**2) * mp.sqrt((x_ - E) ** 2 - Dl**2))
    II = mp.quad(fI, [Dl, x_ / 2, x_ - Dl])
    III = mp.quad(fII, [Dl, x_ / 2, x_ - Dl])
    m1 = 1 - b**2
    ok9 &= abs(II - x_ * mp.ellipe(m1)) < 1e-10
    ok9 &= abs(III - x_ * (mp.ellipe(m1) - b**2 * mp.ellipk(m1))) < 1e-10
    y = 2 / b
    kmod = (y - 2) / (y + 2)
    gI = (1 + 2 / y) * mp.ellipe(kmod**2) - 4 * mp.ellipk(kmod**2) / (y + 2)
    ok9 &= abs(gI - mp.ellipe(m1)) < 1e-12
rec("C9b", ok9, "case-I pair integral = x E(sqrt(1-4D^2/x^2)) = x g_I (WP4 [4.2]) = 1604.06800 Eq.(17); MB = E - b^2 K")

# ---------------------------------------------------------------- C10 (A6, 2212.04504 Eq.(12) q-shape)
mp.mp.dps = 15
kf = mp.mpf(1)
eta_c = -1 / kf


def Tq(qn, lmax=14):
    tot_ = mp.mpf(0)
    for ll in range(lmax + 1):
        fint = lambda rr: rr**2 * (mp.coulombf(ll, eta_c, kf * rr) / (kf * rr)) * mp.sqrt(mp.pi / (2 * qn * rr)) * \
            mp.besselj(ll + mp.mpf(1) / 2, qn * rr) * mp.exp(-rr)
        Il = mp.quad(fint, [0, 2, 6, 15, 40])
        tot_ += (2 * ll + 1) * Il**2
    return tot_


def Gform(qn, corr=True):
    pre = (3 * qn**2 if corr else 3 * qn) + kf**2 + 1
    return qn**2 * pre * mp.exp(-(2 / kf) * mp.atan2(2 * kf, qn**2 - kf**2 + 1)) / \
        (((qn + kf) ** 2 + 1) ** 3 * ((qn - kf) ** 2 + 1) ** 3)


q1, q2 = mp.mpf('0.5'), mp.mpf('2')
ratio_num = Tq(q1) / Tq(q2)
r_corr = Gform(q1) / Gform(q2)
r_mis = Gform(q1, False) / Gform(q2, False)
rec("C10", abs(ratio_num / r_corr - 1) < 1e-6 and abs(ratio_num / r_mis - 1) > 0.05,
    f"hydrogenic 1s->continuum: (3q^2+k^2+1) correct; printed '3q' off by x{float(r_mis/ratio_num):.3f} at q=0.5,2")

# ---------------------------------------------------------------- C11 (I3, exothermic shell)
mm, vv, Dd, Fc = sp.symbols('m v D F', positive=True)
qp_ = mm * vv + sp.sqrt(mm**2 * vv**2 + 2 * mm * Dd)
qm_ = -mm * vv + sp.sqrt(mm**2 * vv**2 + 2 * mm * Dd)
shell = sp.simplify(2 * sp.pi * Fc / vv * (qp_**2 - qm_**2) / 2)
rec("C11", sp.simplify(shell - 4 * sp.pi * mm * Fc * sp.sqrt(2 * mm * Dd + mm**2 * vv**2)) == 0,
    "int d^3q delta(w-|D|-q.v+q^2/2m) F = 4 pi m F sqrt(q*^2 + m^2 v^2): halo-independent to O(v^2/v*^2)")

# ---------------------------------------------------------------- C12 (I5, relativistic DM vertex)
I2 = sp.eye(2)
sx, sy, sz = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
g0 = sp.diag(1, 1, -1, -1)
gs = [sp.Matrix(sp.BlockMatrix([[sp.zeros(2), si], [-si, sp.zeros(2)]])) for si in (sx, sy, sz)]
E1, E2, mD = sp.symbols('E E_p m', positive=True)
p1 = sp.symbols('p1:4', real=True)
p2 = sp.symbols('pp1:4', real=True)
slash = lambda E_, p_: E_ * g0 - sum((p_[i] * gs[i] for i in range(3)), sp.zeros(4))
T = sp.simplify(((slash(E2, p2) + mD * sp.eye(4)) * g0 * (slash(E1, p1) + mD * sp.eye(4)) * g0).trace() / 2)
dot = sum(p1[i] * p2[i] for i in range(3))
Qsq = sum((p1[i] - p2[i]) ** 2 for i in range(3))
target = (E1 + E2) ** 2 - Qsq
diffT = sp.simplify(sp.expand(T - target + (E1**2 - mD**2 - sum(pi_**2 for pi_ in p1))
                              + (E2**2 - mD**2 - sum(pi_**2 for pi_ in p2))))   # mass-shell terms vanish
rec("C12a", diffT == 0, "(1/2)Tr[(p'+m)g0(p+m)g0] = (2E-w)^2 - Q^2 on shell (2401.11971 Eq.(5) numerator)")
Ev, wv, Qv = sp.symbols('E w Q', positive=True)
ratio5 = ((2 * Ev - wv) ** 2 - Qv**2) / (4 * Ev * (Ev - wv))
rec("C12b", sp.limit(ratio5.subs({Ev: mD, wv: 0, Qv: 0}), mD, 1) == 1, "NR limit of the relativistic factor = 1")

# C12c (independent): explicit Dirac transition current of the DM and the NR plane-wave electron current, both
# conservation laws checked numerically (not imposed), then J_chi.J_e (Minkowski) = J0 rho (1 - w^2/Q^2) - J_T.j_T
gm = [np.array(g0.tolist(), dtype=complex)] + [np.array(gi.tolist(), dtype=complex) for gi in gs]
def uspin(pv, mass, chi):
    E_ = np.sqrt(pv @ pv + mass**2)
    sp_ = sum(pv[i] * np.array([sx, sy, sz][i].tolist(), dtype=complex) for i in range(3))
    return np.concatenate([np.sqrt(E_ + mass) * chi, sp_ @ chi / np.sqrt(E_ + mass)]), E_
mchi_, me_ = 1.0, 0.511e3
pD = np.array([0.3, -0.2, 0.9]); pDp = np.array([0.1, 0.35, 0.2])
u1, E1n = uspin(pD, mchi_, np.array([1, 0], dtype=complex))
u2, E2n = uspin(pDp, mchi_, np.array([0.6, 0.8j], dtype=complex))
ubar2 = u2.conj() @ gm[0]
Jchi = np.array([ubar2 @ gm[mu_] @ u1 for mu_ in range(4)])          # J^mu = ubar' gamma^mu u
Qv3 = pD - pDp; wn = E1n - E2n; Qn = np.linalg.norm(Qv3); Qh = Qv3 / Qn
cons_chi = abs(wn * Jchi[0] - Qv3 @ Jchi[1:])
kpar = (2 * me_ * wn - Qn**2) / (2 * Qn)                              # electron k chosen on shell: (k+Q)^2/2m - k^2/2m = w
ke = kpar * Qh + 0.4 * np.cross(Qh, [0, 0, 1])
rho_e = 1.0; j_e = (2 * ke + Qv3) / (2 * me_)
cons_e = abs(wn * rho_e - Qv3 @ j_e)
mink = Jchi[0] * rho_e - Jchi[1:] @ j_e
JT = Jchi[1:] - (Jchi[1:] @ Qh) * Qh; jT = j_e - (j_e @ Qh) * Qh
decomp = Jchi[0] * rho_e * (1 - wn**2 / Qn**2) - JT @ jT
rec("C12c", cons_chi < 1e-12 and cons_e < 1e-12 and abs(mink - decomp) < 1e-12 * max(1, abs(mink)),
    f"spinor currents: conservation holds (residuals {cons_chi:.1e},{cons_e:.1e}); density row carries (1 - w^2/Q^2), w/Q = {wn/Qn:.3f}")

nf = sum(1 for _, o in RES if not o)
print(f"\n{len(RES) - nf}/{len(RES)} PASS")
sys.exit(1 if nf else 0)
