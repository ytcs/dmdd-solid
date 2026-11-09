#!/usr/bin/env python3
"""R10 / WP7-B2 checks (sympy, exact where possible; small numpy pieces only for random-matrix sanity checks).

Run:  python3 checks.py      (all checks must print PASS; total runtime << 2 min)
Labels WP7B2-Cn are cited in returns/R10/WP7-B2.md.
Units: hbar = c = k_B = 1, Heaviside-Lorentz e^2 = 4 pi alpha (CONVENTIONS sec. 1).
"""
import sympy as sp
import numpy as np

RESULTS = []


def check(label, cond, note=""):
    ok = bool(cond)
    RESULTS.append((label, ok))
    print(f"{label:10s} {'PASS' if ok else 'FAIL'}  {note}")


# ---------------------------------------------------------------------------------------------
# C1  A4: WP0-v3 (3.5) with the one-phonon S equals 2308.06314 Eq. (2) with Eq. (16) (self-energy form)
#     -Im[2 w_nu/(w^2 - w_nu^2 + i w g)] integrates to pi over w>0 for every g>0 (so -> pi delta(w - w_nu))
w, wn, g, y, F2, Om = sp.symbols('omega omega_nu gamma y F2 Omega', positive=True)
lor = sp.simplify(-sp.im(2*wn/(w**2 - wn**2 + sp.I*w*g)))
lor = sp.simplify(2*wn*w*g/((w**2 - wn**2)**2 + w**2*g**2))
import mpmath as _mp
val = []
for gg in (1e-2, 1e-3, 1e-4):
    fl = sp.lambdify(w, lor.subs({wn: 1, g: gg}), 'mpmath')
    val.append((gg, _mp.quad(fl, [0, 0.5, 1 - 20*gg, 1, 1 + 20*gg, 2, _mp.inf])))
check("C1a", all(abs(v - _mp.pi) < 2*gg for gg, v in val), "int_0^inf -Im[2w_nu/(w^2-w_nu^2+iwg)] dw -> pi as g->0 (error < 2g)")
# Gamma_URF = (y^2/2w) S,  S = (2pi/Omega)|F.T|^2 delta ;  Gamma_2308 = -(1/w) Im Pi,  Pi = (y^2/Omega)|F.T|^2 * 2w_nu/(...)
G_urf = y**2/(2*w)*(2*sp.pi/Om)*F2           # coefficient of delta(w - w_nu)
G_src = (1/w)*(y**2/Om)*F2*sp.pi             # -Im[...] -> pi delta
check("C1b", sp.simplify(G_urf - G_src) == 0, "(y^2/2w)S_OO = -(1/w)Im Pi_phiphi (2308.06314 Eqs. (2),(16))")

# ---------------------------------------------------------------------------------------------
# C2  coupling-to-mass rule for the k->0 optical vertex of a diatomic crystal
c1, c2, M1, M2 = sp.symbols('c1 c2 M1 M2', positive=True)
Mt = M1 + M2
e1, e2 = sp.sqrt(M2/Mt), -sp.sqrt(M1/Mt)            # optical eigenvector at Q=0 (orthogonal to sqrt(M) acoustic)
vert = c1*e1/sp.sqrt(M1) + c2*e2/sp.sqrt(M2)
check("C2a", sp.simplify(sp.sqrt(M1)*e1 + sp.sqrt(M2)*e2) == 0, "optical mode orthogonal to the mass-weighted translation")
check("C2b", sp.simplify(vert - (c1/M1 - c2/M2)*sp.sqrt(M1*M2/Mt)) == 0, "vertex = (c1/M1 - c2/M2) sqrt(M1 M2/M_cell)")
lam = sp.symbols('lambda', positive=True)
check("C2c", sp.simplify(vert.subs({c1: lam*M1, c2: lam*M2})) == 0, "c_k proportional to M_k -> zero single-phonon absorption")

# C3  GaAs electron-scalar coupling: rigid-ion N_e (28,36) vs URF Z_k - Z*_k (28.9,35.1); rate ratio
MGa, MAs = sp.Rational(6972, 100), sp.Rational(7492, 100)
d_rig = sp.Rational(28)/MGa - sp.Rational(36)/MAs
d_urf = (31 - sp.Rational(21, 10))/MGa - (33 + sp.Rational(21, 10))/MAs
ratio = sp.N((d_urf/d_rig)**2)
check("C3", abs(ratio - 0.468) < 0.005, f"rate(URF Z-Z*)/rate(rigid ion) = {float(ratio):.3f}")

# C4  isotope-disorder broadband channel for B-L in natural Si
iso = [(28, sp.Rational(9223, 10000)), (29, sp.Rational(468, 10000)), (30, sp.Rational(309, 10000))]
Z = 14
gam = [(sp.Rational(A - Z, A), x) for A, x in iso]
gbar = sum(gg*x for gg, x in gam)/sum(x for _, x in iso)
var = sum(x*(gg - gbar)**2 for gg, x in gam)/sum(x for _, x in iso)
check("C4a", abs(float(var/gbar**2) - 1.78e-4) < 0.05e-4, f"sigma_gamma^2/gamma_bar^2 = {float(var/gbar**2):.3e} (B-L, nat. Si)")
# random-mass chain: every non-zero mode is orthogonal to sqrt(M_I) (so the mean coupling gamma_bar M_I drops out exactly)
rng = np.random.default_rng(1)
Nn = 40
Ms = rng.choice([28.0, 29.0, 30.0], size=Nn, p=[0.9223, 0.0468, 0.0309])
K = np.zeros((Nn, Nn))
for i in range(Nn):
    j = (i + 1) % Nn
    K[i, i] += 1; K[j, j] += 1; K[i, j] -= 1; K[j, i] -= 1
D = K/np.sqrt(np.outer(Ms, Ms))
wv, ev = np.linalg.eigh(D)
proj = np.abs(np.sqrt(Ms) @ ev[:, 1:]).max()
check("C4b", proj < 1e-10, f"max_lambda |sum_I sqrt(M_I) e_I,lambda| = {proj:.1e} (periodic random-mass chain)")

# ---------------------------------------------------------------------------------------------
# C5  S5: URF (3.5) with the incoherent spin channel reproduces 2411.10542 Eq. (31)
gp, ma, rho, xi_D, mcell, rhoT = sp.symbols('g_p m_a rho_a XiD m_cell rho_T', positive=True)
# y^2 = (2 g_p m_a)^2 ; S = (2pi/Omega) * sum_k x lam^2 J(J+1) w D/(2M) = (2pi/Omega) * (w/2) * XiD  (XiD = sum_j xi_j D_j)
S5 = (2*sp.pi/Om)*(ma/2)*xi_D
Gam = (2*gp*ma)**2/(2*ma)*S5
R_urf = rho*Gam/(rhoT*ma)
R_src = 2*sp.pi*rho*ma/mcell*gp**2*xi_D
check("C5", sp.simplify(R_urf.subs(rhoT, mcell/Om) - R_src) == 0, "rho Gamma_abs/(rho_T m_a) = 2411.10542 Eq. (31)")

# ---------------------------------------------------------------------------------------------
# C6  S2: one-sublattice FM, axion wind; URF = 2005.10256 Eq. (27) (gamma->0) = 2001.10666 golden-rule limit of Eq. (35)
gae, me, Sj, lS, vperp, f = sp.symbols('g_aee m_e S_j lambda_S v_perp f', positive=True)
k_perp = ma*vperp
S_ks = (2*sp.pi/Om)*lS**2*Sj/2*k_perp**2               # coefficient of delta(w - w_K) in S_{k.s,k.s}
Gam6 = gae**2/(2*ma*me**2)*S_ks
R6 = rho*Gam6/((mcell/Om)*ma)
fj2 = gae**2*lS**2*rho/(2*me**2)*vperp**2               # |f_j . r_j|^2 of 2005.10256 Table 1 (r=(1,i,0))
R6_src = (sp.pi/mcell)*Sj*fj2                           # 2w * w_nu g/((w^2-w_nu^2)^2+w^2 g^2) -> pi delta
check("C6a", sp.simplify(R6 - R6_src) == 0, "URF magnon absorption = 2005.10256 Eq. (27), g_j=2, one sublattice")
Ncell = sp.symbols('N', positive=True)
V2 = Sj*Ncell*rho*vperp**2/f**2                          # |V|^2 of 2001.10666 Eq. (27) with m_a^2 a0^2 = 2 rho
Gam_tot_src = sp.pi/2*V2                                 # 2 pi |V/2|^2 delta (sin -> amplitude V/2i)
Gam_tot_urf = (R6*Ncell*mcell).subs({gae/me: 1/f, lS: 1}).subs(gae, me/f)
check("C6b", sp.simplify(Gam_tot_urf - Gam_tot_src) == 0, "total rate = 2001.10666 Eqs. (25)-(27),(35) in the golden-rule limit")

# C7  Larmor theorem: isotropic exchange + uniform Zeeman -> S^-_tot creates weight only at w_L, total 2<S^z_tot>
def spin_ops(s):
    m = [s - i for i in range(int(2*s) + 1)]
    n = len(m)
    Sz = sp.diag(*m)
    Sp = sp.zeros(n)
    for i in range(1, n):
        mm = m[i]
        Sp[i - 1, i] = sp.sqrt(s*(s + 1) - mm*(mm + 1))
    return Sz, Sp, Sp.T
def kron(*ms):
    out = ms[0]
    for mm in ms[1:]:
        out = sp.kronecker_product(out, mm)
    return out
sA, sB = sp.Integer(1), sp.Rational(1, 2)
SzA, SpA, SmA = spin_ops(sA); SzB, SpB, SmB = spin_ops(sB)
IA, IB = sp.eye(3), sp.eye(2)
J, wL = sp.Integer(3), sp.Rational(1, 7)
SA_dot_SB = kron(SzA, SzB) + (kron(SpA, SmB) + kron(SmA, SpB))/2
Sz_tot = kron(SzA, IB) + kron(IA, SzB)
Sm_tot = kron(SmA, IB) + kron(IA, SmB)
H = J*SA_dot_SB - wL*Sz_tot          # ferrimagnet (AF coupling, S_A=1, S_B=1/2); field favours +S^z
Hn = np.array(H.evalf(), dtype=float)
E, U = np.linalg.eigh(Hn)
g0 = U[:, 0]
Smn = np.array(Sm_tot.evalf(), dtype=float)
amps = (U.T @ Smn @ g0)**2
weights = {round(E[i] - E[0], 10): 0.0 for i in range(len(E))}
for i in range(len(E)):
    weights[round(E[i] - E[0], 10)] += amps[i]
nonzero = {k: v for k, v in weights.items() if v > 1e-12}
Szg = float(g0 @ np.array(Sz_tot.evalf(), dtype=float) @ g0)
check("C7", len(nonzero) == 1 and abs(list(nonzero)[0] - float(wL)) < 1e-10 and abs(sum(nonzero.values()) - 2*Szg) < 1e-10,
      f"S^-_tot weight only at w_L={float(wL):.4f}; total {sum(nonzero.values()):.4f} = 2<S^z>={2*Szg:.4f} (ferrimagnet 1, 1/2)")

# C8  Polder/Kittel ellipticity: H = (wx X^2 + wy P^2)/2 ; |<1|X|0>|^2 = sqrt(wy/wx)/2, mode frequency sqrt(wx wy)
wx, wy = sp.symbols('omega_x omega_y', positive=True)
# canonical rescaling X = (wy/wx)^(1/4) x, P = (wx/wy)^(1/4) p turns H into sqrt(wx wy)(x^2+p^2)/2
X01sq = (wy/wx)**sp.Rational(1, 2)*sp.Rational(1, 2)
P01sq = (wx/wy)**sp.Rational(1, 2)*sp.Rational(1, 2)
wK = sp.sqrt(wx*wy)
check("C8a", sp.simplify(wx*X01sq*2 - wK) == 0 and sp.simplify(wy*P01sq*2 - wK) == 0, "Kittel w_K = sqrt(w_x w_y); x-drive weight sqrt(w_y/w_x)")
check("C8b", sp.simplify((X01sq + P01sq) - (wx + wy)/(2*wK)) == 0, "transverse-isotropic average = A/w_K = (w_x+w_y)/(2 w_K) >= 1")

# ---------------------------------------------------------------------------------------------
# C9  S6: chi'' (2504.02927 Eq. (8), s_e = sigma) = 2(1 - e^{-beta w}) S_{s s} (campaign); Eq. (17) = URF; Eq. (26) inversion
beta, Sss = sp.symbols('beta S_ss', positive=True)
R_camp, Rconj = sp.symbols('R Rc')   # campaign retarded R_{ss}, and R_{ss}^*
# chi_sigma = -4 R (Kubo sign, sigma = 2 s); chi'' = -i(chi - chi^dag)/2 ; FDT: (1-e^{-bw}) S = i(R - R^*)
chi = -4*R_camp; chic = -4*Rconj
chi2 = -sp.I*(chi - chic)/2
check("C9a", sp.simplify(chi2 - 2*sp.I*(R_camp - Rconj)) == 0, "chi'' = 2 i (R - R*) = 2 (1 - e^{-beta w}) S_ss")
vv = sp.symbols('v', positive=True)
G_src = gae**2*ma*vv**2*(2*Sss)          # Eq. (17) with chi'' = 2 S (T = 0), g_ae dimensionful; v^i v^j -> v^2 (diag)
G_urf = (1/(2*ma))*(2*gae)**2*(ma*vv)**2*Sss   # H = -g grad a . sigma = -2 g grad a . s
check("C9b", sp.simplify(G_src - G_urf) == 0, "2504.02927 Eq. (17) = (y^2/2w) k k S_ss")
gn, e_, Nf, Omc = sp.symbols('gamma_n e N_f Omega_c', positive=True)
Sn_from_S = gn**2*e_**4*Omc/(4*me**2*(2*sp.pi)**3*Nf)*Sss
Sn_eq26 = (1/Nf)*gn**2*e_**4/(8*me**2)*Omc/(2*sp.pi)**3*(2*Sss)
check("C9c", sp.simplify(Sn_from_S - Sn_eq26) == 0, "S_n = gamma_n^2 e^4 Omega_c P_T S/(4 m_e^2 (2pi)^3 N_f)")

# ---------------------------------------------------------------------------------------------
# C10 chiral phonons: Zhang-Niu L_z is conserved by the harmonic H only if D commutes with the on-site rotation generator
# H = p.p/2 + u.D.u/2 (mass-weighted), L_z = u^T J p ; [H, L_z] = i( p^T J p - u^T D J u )-type term -> zero iff [D, J] = 0
def comm_vanishes(Dm, Jm):
    return (Dm*Jm - Jm*Dm) == sp.zeros(*Dm.shape)
Jz1 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
Jz = sp.diag(Jz1, Jz1)                         # two atoms, rotation of displacement vectors only
a_, b_, c_, d_ = sp.symbols('a b c d', positive=True)
D_iso = sp.Matrix(6, 6, lambda i, j: (a_ if i == j else 0) + (-b_ if abs(i - j) == 3 else 0))
D_aniso = D_iso.copy(); D_aniso[0, 0] += c_; D_aniso[3, 3] += c_; D_aniso[0, 4] = D_aniso[4, 0] = d_
check("C10", comm_vanishes(D_iso, Jz) and not comm_vanishes(D_aniso, Jz),
      "[D,J]=0 (isotropic springs) conserves phonon L_z; generic crystal D does not (no conservation law for decay)")

# ---------------------------------------------------------------------------------------------
# C11 X10: exact acceleration identity [H,[H,X]] = (dV/dX)/M on a test function; URF -> 2312.10566 Eq. (17)
Xs, xs, Mn, mel = sp.symbols('X x M m', positive=True)
Vf = sp.Function('V')(Xs, xs)
psi = sp.Function('psi')(Xs, xs)
def Hop(fn):
    return -sp.diff(fn, Xs, 2)/(2*Mn) - sp.diff(fn, xs, 2)/(2*mel) + Vf*fn
def comm_HX(fn):
    return Hop(Xs*fn) - Xs*Hop(fn)
lhs = Hop(comm_HX(psi)) - comm_HX(Hop(psi))
check("C11a", sp.simplify(sp.expand(lhs - sp.diff(Vf, Xs)*psi/Mn)) == 0, "[H,[H,X]] psi = (dV/dX/M) psi exactly (any V)")
# rate: Gamma = y^2 gamma^2 m_e^2 k^2 Im(-1/eps)/(e^2 w); dilute: Im(-1/eps) ~ n_at sigma_gamma / w ; per atom, gamma = g/m_p
gphi, mp, kk, sig, nat, al = sp.symbols('g_phi m_p k sigma_gamma n_at alpha', positive=True)
Gam11 = gphi**2*(1/mp)**2*me**2*kk**2*(nat*sig/w)/(4*sp.pi*al*w)
src17 = gphi**2*(me/mp)**2*(kk/w)*sig/(4*sp.pi*al)*(kk/w)   # sigma_phi * v, v = k/w
check("C11b", sp.simplify(Gam11/nat - src17) == 0, "URF (B2.8.3) per atom = 2312.10566 Eq. (17) x v")

# ---------------------------------------------------------------------------------------------
# C12 sec. 10(iii): optical potential U0 = 2 pi b n0/m_chi vs E_kin = m v^2/2 at the 2512.16451 benchmark
hbarc = sp.Rational(197327, 10**10)        # eV cm
m_chi, v_, n0 = sp.Integer(20), sp.Rational(1, 1000), sp.Rational(269, 100)*10**24   # eV, c, cm^-3
sig_b = sp.Rational(4, 1)*sp.Rational(1, 10**38)                                       # cm^2
b = sp.sqrt(sig_b/(4*sp.pi))
U0 = 2*sp.pi*b*n0*hbarc**2/m_chi
Ek = m_chi*v_**2/2
ratio12 = sp.N(U0/Ek)
kcm = m_chi*v_/hbarc
sig_crit = sp.N(4*sp.pi*(kcm**2/(4*sp.pi*n0))**2)
check("C12", abs(float(ratio12) - 1.85) < 0.05 and abs(float(sig_crit) - 1.17e-38) < 0.05e-38,
      f"U0/E_kin = {float(ratio12):.2f} at 4e-38 cm^2, 20 eV; Born needs sigma << {float(sig_crit):.2e} cm^2")

# ---------------------------------------------------------------------------------------------
# C13 squared-coupling misprints: 2601.01043 Eq. (12) vs (13); 2308.06314 Eq. (48) vs (49)
kap, gag, B0 = sp.symbols('kappa g_agg B_0', positive=True)
g_sol = sp.solve(sp.Eq((gag*B0/ma)**2, kap**2), gag)
check("C13a", g_sol == [kap*ma/B0], "squared form of 2601.01043 Eq. (12) gives its Eq. (13) g ~ eps m/B0 (linear form would not)")
num49 = sp.N(2*sp.sqrt(4*sp.pi/137.036)*1e-16*511e3/0.1)   # g_aee from (1/4)(g/e)^2 (w/m_e)^2 = kappa^2, w = 100 meV
check("C13b", 1e-10 < float(num49) < 1e-9, f"squared 2308.06314 Eq. (48) -> g_aee = {float(num49):.1e} ~ Eq. (49) 1e-9 (linear: ~1e-25)")
nr, e1r, e2r = sp.symbols('n_r eps1 eps2', positive=True)
R_urf13 = kap**2*w*e2r/(e1r**2 + e2r**2)       # kappa^2 w Im(-1/eps)
R_src13 = kap**2*w*e2r/nr                      # kappa^2 alpha, alpha = w eps2 / n_r
check("C13c", sp.simplify(R_urf13/R_src13 - nr/(e1r**2 + e2r**2)) == 0, "R_URF/R_(alpha, eps=1) = n_r/|eps|^2")

# ---------------------------------------------------------------------------------------------
# C14 random-coupling broadband theorem: <|sum_I c_I . e_I|^2>_c = sum_I sigma_I^2 |e_I|^2/3 for isotropic, independent c_I
cs = sp.symbols('s1:3', positive=True)
ex = sp.symbols('e1:7')
# <c_I^a c_J^b> = delta_IJ delta_ab s_I^2/3
avg = sum(cs[I]**2/3*sum(ex[3*I + a]**2 for a in range(3)) for I in range(2))
# explicit average via second moments
expr = 0
for I in range(2):
    for J in range(2):
        for a in range(3):
            for bb in range(3):
                mom = (cs[I]**2/3 if (I == J and a == bb) else 0)
                expr += mom*ex[3*I + a]*ex[3*J + bb]
check("C14", sp.simplify(expr - avg) == 0, "configurational average -> self (incoherent) term with sigma_I^2 D_I")

# C15 X10 correction n_r/|eps|^2 -> 1 - O(w_p^2/w^2): Si valence w_p = 16.6 eV at w = 1 keV
wp = sp.Rational(166, 10)
corr = sp.N((wp/1000)**2)
check("C15", 2.5e-4 < float(corr) < 3.0e-4, f"(w_p/w)^2 = {float(corr):.2e} at 1 keV (photoionization relation valid)")

# C16 SMM: H = -D S_z^2 - w_Z S_z ; line S -> S-1 at D(2S-1) + w_Z with |<S-1|S^-|S>|^2 = 2S
Dz, wZ = sp.symbols('D omega_Z', positive=True)
Sbig = sp.Integer(10)
E_m = lambda m: -Dz*m**2 - wZ*m
check("C16", sp.simplify(E_m(Sbig - 1) - E_m(Sbig) - (Dz*(2*Sbig - 1) + wZ)) == 0 and
      sp.simplify(Sbig*(Sbig + 1) - Sbig*(Sbig - 1) - 2*Sbig) == 0, "SMM line D(2S-1)+w_Z, weight 2S (Mn12-like S=10)")

# C17 1705.03016 Eq. (6): zero-point momentum spread of H in LiH vs alpha m_e
MH, wH = sp.Float(938.8e6), sp.Float(0.1)      # eV
dp = sp.sqrt(MH*wH/2)
qmin = sp.sqrt(2*MH*9)
check("C17", 6.5e3 < float(dp) < 7.2e3 and float(dp/qmin) < 0.06,
      f"Delta p = sqrt(M w/2) = {float(dp)/1e3:.1f} keV (vs alpha m_e = 3.7 keV); Delta p/q_min = {float(dp/qmin):.3f}")

# C18 D5 factorisation: R_1 = R_CM + (m2/M) r  and  m2/M = mu12/m1
m1_, m2_ = sp.symbols('m1 m2', positive=True)
check("C18", sp.simplify(m2_/(m1_ + m2_) - (m1_*m2_/(m1_ + m2_))/m1_) == 0, "e^{iq.R1} = e^{iq.R_CM} e^{i(mu12/m1) q.r}")

# C19 S5 spin-average identity behind 2411.10542 Eq. (27): sum_a <J^a J^a> = J(J+1), <J^a J^b> = delta J(J+1)/3
Jq = sp.Rational(3, 2)
SzJ, SpJ, SmJ = spin_ops(Jq)
Jx = (SpJ + SmJ)/2; Jy = (SpJ - SmJ)/(2*sp.I)
tr = lambda M_: sp.simplify(M_.trace()/(2*Jq + 1))
check("C19", tr(Jx*Jx) == Jq*(Jq + 1)/3 and tr(Jx*Jy) == 0 and tr(SzJ*SzJ) == Jq*(Jq + 1)/3,
      "unpolarised nuclear spin: <J^a J^b> = delta_ab J(J+1)/3")

# C20 (B2.7.1): two-phonon creation amplitude of u x P at one site, u = sum e(b + b^dag)/sqrt(2 M w), P = M du/dt
B1, B2, Mq, w1, w2 = sp.symbols('B1 B2 M_q w1 w2', positive=True)
ev1 = sp.Matrix(sp.symbols('a1:4')); ev2 = sp.Matrix(sp.symbols('c1:4'))
u_cr = ev1*B1/sp.sqrt(2*Mq*w1) + ev2*B2/sp.sqrt(2*Mq*w2)
P_cr = sp.I*sp.sqrt(Mq*w1/2)*ev1*B1 + sp.I*sp.sqrt(Mq*w2/2)*ev2*B2
uxP = u_cr.cross(P_cr)
coef = sp.Matrix([sp.expand(uxP[i]).coeff(B1).coeff(B2) for i in range(3)])
target = sp.I/2*(sp.sqrt(w2/w1) - sp.sqrt(w1/w2))*ev1.cross(ev2)
check("C20", sp.simplify(coef - target) == sp.zeros(3, 1), "<12|u x P|0> = (i/2)[sqrt(w2/w1) - sqrt(w1/w2)] e1 x e2 (zero one-phonon term)")

n_pass = sum(ok for _, ok in RESULTS)
print(f"\n{n_pass}/{len(RESULTS)} PASS")
if n_pass != len(RESULTS):
    raise SystemExit(1)
