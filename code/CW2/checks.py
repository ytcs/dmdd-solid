"""R16 / CW2 checks (closure of LE-48 ... LE-72), revised by the R16 errata ERR-CW2 (returns/R16/CW2-errata.md).
Run: python3 checks.py   (all PASS, < 2 min, single core)
Labels CW2-Cn are cited in returns/R16/CW2.md; C21-C29 and C13/C14/C15/C16b (rewritten or new) are cited in CW2-errata.md.
Units: hbar = c = k_B = 1 unless stated; atomic units (Gaussian, e = m_e = hbar = 1) where marked "a.u.".
ld1/results.json is produced by atomic_contact.py, ld1/results-errata.json by atomic_contact_errata.py ([CALC], QE 7.6 ld1.x).
Errata changes: tolerances tightened to the achieved precision; C13 (trivially true Bose-factor positivity) and C15 (closed-form
slab reflectance labelled "transfer matrices") replaced by non-circular tests; C14 uses one Z* (the LST value it computes);
new checks for every verifier correction (C16b, C21-C29)."""
import json, os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import sympy as sp
from scipy import integrate, special

HERE = os.path.dirname(os.path.abspath(__file__))
RES = []


def check(label, cond, note=""):
    RES.append((label, bool(cond)))
    print(f"{label:6s} {'PASS' if cond else 'FAIL'}  {note}")


# ------------------------------------------------------------------------------------------------------------------
# 1D diatomic chain used by C1 (LE-48, LE-49): sites r1 = 0, r2 = a/2, masses M1, M2, nearest-neighbour spring K.
a, M1, M2, K, NQ = 1.0, 1.0, 2.3, 1.0, 400
Qs = 2*np.pi*(np.arange(NQ) - NQ//2)/(NQ*a)
rk = np.array([0.0, a/2]); Mk = np.array([M1, M2])


def modes(Q):
    # dynamical matrix with cell-phase eigenvectors (CONVENTIONS §5: e^{iQ.R} only)
    D = np.array([[2*K/M1, -K*(1 + np.exp(-1j*Q*a))/np.sqrt(M1*M2)],
                  [-K*(1 + np.exp(1j*Q*a))/np.sqrt(M1*M2), 2*K/M2]])
    w2, e = np.linalg.eigh(D)
    return np.sqrt(np.clip(w2, 1e-12, None)), e     # e[kappa, nu]


W, E = zip(*[modes(Q) for Q in Qs]); W = np.array(W); E = np.array(E)
acoustic_cut = np.abs(Qs) > 1e-9                     # drop Q = 0 acoustic (zero weight in the measure)


Wc = np.where(acoustic_cut[:, None], W, np.inf)          # Q = 0 acoustic carries zero measure


def Bcorr(dR, k1, k2):
    """T = 0 displacement correlation B_{k1k2}(dR) = <u_{0k1} u_{dR k2}> (lattice units), (CW2.2)."""
    s = (E[:, k1, :]*np.conj(E[:, k2, :])*np.exp(-1j*Qs*dR*a)[:, None]/(2*Wc*np.sqrt(Mk[k1]*Mk[k2]))).sum()
    return (s/NQ).real


c = np.array([1.0, 1.7])          # couplings c_kappa (multiplicative vertex)
q = 0.37*2*np.pi/a                # q < q_BZ = 2 pi / a : the LE-48 regime
dRmax = NQ//2   # full periodic ring: the Poisson identity is exact
W2_real = sum(c[k1]*c[k2]*np.cos(q*(dR*a + rk[k2] - rk[k1]))*(q**2*Bcorr(dR, k1, k2))**2/2
              for dR in range(-dRmax, dRmax) for k1 in range(2) for k2 in range(2))
idx = np.arange(NQ)


def partner(qv):
    Qr = (qv - Qs + np.pi/a) % (2*np.pi/a) - np.pi/a
    return np.rint((Qr*NQ*a/(2*np.pi))).astype(int) + NQ//2


def coh_and_P(qv, strip=False):
    i2 = partner(qv) % NQ
    pref = 1.0 if strip else qv**4
    amp = np.zeros((NQ, 2, 2), complex); P = 0.0
    for n1 in range(2):
        for n2 in range(2):
            terms = np.array([c[k]*np.exp(1j*qv*rk[k])*np.conj(E[:, k, n1])*np.conj(E[i2, k, n2])/Mk[k] for k in range(2)])
            den = 4*Wc[:, n1]*Wc[i2, n2]
            amp[:, n1, n2] = terms.sum(0)
            P += np.sum(np.abs(terms)**2/den)
    coh = np.sum(np.abs(amp)**2/(4*Wc[:, :, None]*Wc[i2][:, None, :]))
    return pref*coh/2/NQ, pref*P/2/NQ


W2_mom, P2 = coh_and_P(q)
check("C1a", abs(W2_real - W2_mom) < 1e-10*abs(W2_mom),
      f"n_ph=2 omega-integrated coherent weight: shell sum {W2_real:.6f} = BZ form {W2_mom:.6f} (Poisson identity, (CW2.3); exact to machine precision)")
W2_self = sum(c[k]**2*(q**2*Bcorr(0, k, k))**2/2 for k in range(2))
check("C1b", W2_mom <= 2*P2 + 1e-12,
      f"Cauchy-Schwarz bound (CW2.5): coherent {W2_mom:.5f} <= n_b * P^(2) = {2*P2:.5f};  incoherent (self) {W2_self:.5f}; "
      f"ratio coh/inc - 1 = {W2_mom/W2_self - 1:+.3f} at q = 0.37 q_BZ")
P2avg = np.mean([coh_and_P(qq, strip=True)[1] for qq in Qs])
self_unit = sum(c[k]**2*Bcorr(0, k, k)**2/2 for k in range(2))
check("C1c", abs(P2avg - self_unit) < 1e-10*self_unit,
      f"<P^(2)>_q over the BZ (q^4 stripped) = {P2avg:.5f} = incoherent self weight {self_unit:.5f}")
R2 = [coh_and_P(f*2*np.pi/a)[0]/sum(c[k]**2*((f*2*np.pi/a)**2*Bcorr(0, k, k))**2/2 for k in range(2)) - 1 for f in (0.37, 1.37, 3.37, 8.37)]
print("       1D diatomic chain R_2(q) = coh/inc - 1 at q/q_BZ = 0.37, 1.37, 3.37, 8.37:", ", ".join(f"{v:+.3f}" for v in R2))

# ------------------------------------------------------------------------------------------------------------------
# C2 (LE-50): 3D convolution int d^3Q /(Q^2 |k-Q|^2) = pi^3/k (second-order TDS 1/|q-G| law)
val = integrate.quad(lambda x: np.log(abs((1 + x)/(1 - x)))/x, 0, 1, limit=200)[0] + \
      integrate.quad(lambda x: np.log(abs((1 + x)/(1 - x)))/x, 1, np.inf, limit=200)[0]
check("C2", abs(2*np.pi*val - np.pi**3) < 1e-6, f"(2pi/k) int_0^inf ln|(1+x)/(1-x)| dx/x = {2*np.pi*val:.6f} = pi^3 = {np.pi**3:.6f} (k = 1)")

# ------------------------------------------------------------------------------------------------------------------
# C3 (LE-51): hydrogen 1s in a field (a.u.): Dalgarno-Lewis psi1 = -(r + r^2/2) cos(th) psi0 solves (H0-E0)psi1 = -z psi0;
#             the deformation density 2 psi0 psi1 has an |x| x_z (non-analytic) piece whose Fourier tail is q^-5,
#             vs q^-3 for the rigid-shift term d_z n0.
r, th, Q = sp.symbols('r theta q', positive=True)
psi0 = sp.exp(-r)/sp.sqrt(sp.pi)
psi1 = -(r + r**2/2)*sp.cos(th)*psi0
lap = lambda f: sp.diff(r**2*sp.diff(f, r), r)/r**2 + sp.diff(sp.sin(th)*sp.diff(f, th), th)/(r**2*sp.sin(th))
lhs = sp.simplify(-lap(psi1)/2 - psi1/r + psi1/2)
check("C3a", sp.simplify(lhs + r*sp.cos(th)*psi0) == 0, "Dalgarno-Lewis first-order Stark function of H(1s) verified")
# radial part of the l=1 deformation density per unit field: f(r) = 2 psi0 * (-(r + r^2/2)) e^{-r}/sqrt(pi) -> l=1 FT ~ int r^2 f j1
f_def = -2*(r + r**2/2)*sp.exp(-2*r)/sp.pi
FT_def = sp.simplify(4*sp.pi*sp.integrate(r**2*f_def*(sp.sin(Q*r)/(Q*r)**2 - sp.cos(Q*r)/(Q*r)), (r, 0, sp.oo)))
lead_def = sp.limit(FT_def*Q**5, Q, sp.oo)
n0 = sp.exp(-2*r)/sp.pi
FT_n0 = sp.simplify(4*sp.pi*sp.integrate(r**2*n0*sp.sin(Q*r)/(Q*r), (r, 0, sp.oo)))   # = 16/(4+q^2)^2
lead_rig = sp.limit(Q*FT_n0*Q**3, Q, sp.oo)
check("C3b", lead_def != 0 and sp.limit(FT_def*Q**4, Q, sp.oo) == 0 and lead_rig == 16,
      f"deformation l=1 FT ~ {sp.nsimplify(lead_def)} q^-5 (pure-field H 1s); rigid q*n0(q) ~ 16 q^-3: relative tail O((q a)^-2)")

# ------------------------------------------------------------------------------------------------------------------
# C4 (LE-52, LE-70): Markov-Krein bounds on the CDF from the exact moments m0..m4 (Hamburger; canonical representation)


def mk_bounds(m, xi):
    H = np.array([[m[i + j] for j in range(3)] for i in range(3)])
    Hi = np.linalg.inv(H)
    v = lambda x: np.array([1, x, x**2])
    Kxx = lambda x, y: v(x) @ Hi @ v(y)
    # nodes: xi and the 2 roots of the kernel polynomial K(x, xi) (degree 2 in x)
    cpoly = Hi @ v(xi)                      # coefficients of 1, x, x^2
    roots = np.roots([cpoly[2], cpoly[1], cpoly[0]]).real
    nodes = np.concatenate([[xi], roots])
    wts = np.array([1/Kxx(x, x) for x in nodes])
    low = wts[nodes < xi - 1e-12].sum(); up = low + wts[0]
    return low, up, wts[0], abs(wts.sum() - m[0])


rng = np.random.default_rng(3)
samples = np.concatenate([rng.normal(1.0, 0.25, 600000), rng.gamma(2.0, 0.6, 400000) + 0.4])   # skewed test S(omega)
m = [np.mean(samples**k) for k in range(5)]
ok, worst = True, 0.0
for xi in np.linspace(0.3, 3.0, 28):
    lo, up, rho, err = mk_bounds(m, xi)
    F = np.mean(samples < xi)
    ok &= (lo - 1e-9 <= F <= up + 1e-9) and err < 1e-9     # exact: the empirical law has exactly these moments
    worst = max(worst, rho)
check("C4", ok, f"Markov-Krein: canonical lower/upper sums bracket the true CDF at 28 points; max mass rho(xi) = {worst:.3f}")

# ------------------------------------------------------------------------------------------------------------------
# C5 (LE-54): E^Mig_3 = E_R * [4 pi Z n_e(0)/3 - Phi_onsite]/M (a.u.), contact densities [CALC] from ld1.x (NR, PBE)
ldr = json.load(open(f"{HERE}/ld1/results.json"))
HA = 27.211386; MU = 1822.888486
amass = {"Si": 28.0855, "Ge": 72.630, "Ga": 69.723, "As": 74.9216}
Zs = {"Si": 14, "Ge": 32, "Ga": 31, "As": 33}
coef = {}
for el in amass:
    n0e = ldr[f"{el}_r0_PBE_dx0.008"]["n0"]
    coef[el] = 4*np.pi*Zs[el]*n0e/3/(amass[el]*MU)*HA**2      # eV^2 : E^Mig_3 = coef * E_R
ratio_si = coef["Si"]/0.044**2                                  # vs harmonic k3^GS/E_R = <omega^2>, sqrt<w^2> = 44 meV [E]
conv = abs(ldr["Si_r0_PBE_dx0.008"]["n0"] - ldr["Si_r0_PBE_dx0.006"]["n0"])/ldr["Si_r0_PBE_dx0.008"]["n0"]
quoted5 = {"Si": 1498, "Ge": 16836, "Ga": 15416, "As": 18493}
check("C5", all(abs(coef[k] - quoted5[k]) < 0.5 for k in coef) and 7.6e5 < ratio_si < 7.8e5 and conv < 1e-7,
      "E^Mig_3/E_R [eV^2]: " + ", ".join(f"{k} {v:.0f}" for k, v in coef.items()) + f"; Si k3^X/k3^GS = {ratio_si:.2e}; grid conv {conv:.1e}")

# ------------------------------------------------------------------------------------------------------------------
# C6 (LE-55, LE-62): inverse spectral moments. P_Mig <= E^Mig_1/E_g ; |C_kappa| <= sqrt(alpha_2 dM)  (random spectra)
ok6 = True
for trial in range(200):
    n = 50
    Ea = rng.uniform(1.0, 8.0, n)          # excitation energies >= E_g = 1
    gV = rng.normal(size=n) + 1j*rng.normal(size=n)       # <a|dV|0>
    dd = rng.normal(size=n) + 1j*rng.normal(size=n)       # <a|d|0>
    dM = 2*np.sum(abs(gV)**2/Ea**3); alpha2 = 2*np.sum(abs(dd)**2/Ea**3)
    Cc = 2*np.sum((np.conj(dd)*gV).real/Ea**3)
    Pm = np.sum(abs(gV)**2/Ea**4); E1 = np.sum(abs(gV)**2/Ea**3)
    ok6 &= (Pm <= E1/1.0 + 1e-12) and (abs(Cc) <= np.sqrt(alpha2*dM) + 1e-12)
# Si and GaAs numbers (a.u., Gaussian): alpha_2 = Omega (d eps/d w^2)/(4 pi); dM ~ N_e m_e [E]; d eps/d(w^2) [UNVERIFIED n(w)]
def dZbound(Omega_A3, deps_eV2, Ne, w_eV):
    Om = Omega_A3/0.529177**3; deps = deps_eV2*HA**2
    return (w_eV/HA)**2*np.sqrt(Ne*Om*deps/(4*np.pi))
bSi = dZbound(40.05, 0.6, 14, 1.0); bGa = dZbound(45.17, 0.8, 31, 1.0)
check("C6", ok6 and abs(bSi - 0.494) < 0.005 and abs(bGa - 0.90) < 0.01, f"200 random spectra obey both inequalities; |Z*(1 eV) - Z*(0)| <= {bSi:.2f} (Si), {bGa:.2f} (GaAs, Ga) [E inputs]")

# ------------------------------------------------------------------------------------------------------------------
# C7 (LE-56): hydrogenic closed form of r_kappa(q) vs the radial integral; all-electron [CALC] values
ok7 = True
for xi in [0.3, 0.5, 1.0, 2.0]:
    aa = 1.0; qq = 2*xi/aa
    num = 6*integrate.quad(lambda x: np.exp(-2*x/aa)*special.spherical_jn(2, qq*x)/x, 0, 60, limit=400)[0]
    closed = 2 + 3/xi**2 - 3*(1 + xi**2)*np.arctan(xi)/xi**3
    ok7 &= abs(num - closed) < 1e-7
rSi = ldr["Si_r0_PBE_dx0.008"]["rq"]
hyd = lambda qk: (lambda xi: 3 + 3/xi**2 - 3*(1 + xi**2)*np.arctan(xi)/xi**3)(qk/51.1/2)
check("C7", ok7 and abs(rSi["102.0"]["total"] - hyd(102.0)) < 1e-3,
      "r-1 Si AE (NR PBE) at 10/30/51.1/102/300 keV: " + "/".join(f"{100*(rSi[k]['total']-1):.2f}" for k in rSi)
      + " % ; hydrogenic: " + "/".join(f"{100*(hyd(float(k))-1):.2f}" for k in rSi) + " %")

# ------------------------------------------------------------------------------------------------------------------
# C8 (LE-59): (a) cubic anharmonicity: first-order change of S(q,omega) vanishes (time reversal); (b) Euclidean quartic contraction
nb = 60
bop = np.diag(np.sqrt(np.arange(1, nb)), 1); x = (bop + bop.T)/np.sqrt(2)     # M = omega = 1, l^2 = 1/2


def Sdisc(lam3, lam4, qv):
    H = np.diag(np.arange(nb) + 0.5) + lam3*np.linalg.matrix_power(x, 3) + lam4*np.linalg.matrix_power(x, 4)
    ev, U = np.linalg.eigh(H)
    from scipy.linalg import expm
    A = U.T @ expm(1j*qv*x) @ U
    wts = abs(A[:, 0])**2; om = ev - ev[0]
    hist = np.array([wts[(om > b - 0.5) & (om <= b + 0.5)].sum() for b in range(1, 6)])
    return hist


h0 = Sdisc(0, 0, 1.3); h1 = Sdisc(0.01, 0, 1.3); h2 = Sdisc(0.02, 0, 1.3)
ratio8 = np.max(abs(h2 - h0))/np.max(abs(h1 - h0))
# Euclidean T = 0 contraction: <x^4>_c at first order in lam4 = -4! lam4 l^8 /(2 omega) * ... = -12 lam4 l^8 (omega = 1)


def x4c(lam4):
    H = np.diag(np.arange(nb) + 0.5) + lam4*np.linalg.matrix_power(x, 4)
    ev, U = np.linalg.eigh(H); g = U[:, 0]
    m2 = g @ (x @ x) @ g; m4 = g @ np.linalg.matrix_power(x, 4) @ g
    return m4 - 3*m2**2


d4 = (x4c(1e-4) - x4c(-1e-4))/2e-4
check("C8", 1.95 < np.log2(ratio8) < 2.08 and abs(d4 - (-12*(0.5)**4)) < 1e-5,
      f"cubic: |dS| scales as lam3^{np.log2(ratio8):.2f} (first order absent); quartic d<x^4>_c/dlam4 = {d4:.4f} vs -12 l^8 = {-12*0.5**4:.4f}")

# ------------------------------------------------------------------------------------------------------------------
# C9 (LE-60): cubic elasticity (Si C11, C12, C44 [UNVERIFIED std values]): one-phonon omega-integrated weight per direction
C11, C12, C44, rho_m = 165.7, 63.9, 79.6, 2.329       # GPa, g/cm^3


def weight(n):
    G = np.array([[C11*n[0]**2 + C44*(n[1]**2 + n[2]**2), (C12 + C44)*n[0]*n[1], (C12 + C44)*n[0]*n[2]],
                  [(C12 + C44)*n[0]*n[1], C11*n[1]**2 + C44*(n[0]**2 + n[2]**2), (C12 + C44)*n[1]*n[2]],
                  [(C12 + C44)*n[0]*n[2], (C12 + C44)*n[1]*n[2], C11*n[2]**2 + C44*(n[0]**2 + n[1]**2)]])/rho_m
    c2, e = np.linalg.eigh(G)
    return np.sum((n @ e)**2/np.sqrt(c2))          # sum_nu |q.e|^2 / c_nu  (∝ int d omega S^(1) at fixed |q|)


xg, wg = np.polynomial.legendre.leggauss(40); phis = np.linspace(0, 2*np.pi, 80, endpoint=False)
proj = {}
for ell in [0, 2, 4, 6]:
    s = 0.0
    for ct, wct in zip(xg, wg):
        st = np.sqrt(1 - ct**2)
        for ph in phis:
            n = np.array([st*np.cos(ph), st*np.sin(ph), ct])
            s += wct*(2*np.pi/80)*weight(n)*special.sph_harm_y(ell, 0, np.arccos(ct), ph).real
    proj[ell] = s
check("C9", abs(proj[2]) < 1e-10*abs(proj[0]) and 0.0205 < proj[4]/proj[0] < 0.0225 and abs(proj[6]/proj[0]) < 1e-3,
      f"Si one-phonon (continuum) weight: S_20/S_00 = {proj[2]/proj[0]:.1e}, S_40/S_00 = {proj[4]/proj[0]:+.4f}, S_60/S_00 = {proj[6]/proj[0]:+.4f}")

# ------------------------------------------------------------------------------------------------------------------
# C10 (LE-63): 2603.13052 (4.8): int_0^{2 mu v} dq q/(mu^2 v^2) = 2 (standard qσ/(2μ²v²) gives 1); and (4.6)(4.7)(4.8) = KKL x standard
mu_, v_, qv_, om_, mN, X = sp.symbols('mu v q omega m_N X', positive=True)
tot48 = sp.integrate(qv_/(mu_**2*v_**2), (qv_, 0, 2*mu_*v_))
prod = (1/mN)*(qv_/(mu_**2*v_**2))*(2*X*qv_**2/(3*om_**4*mN))
kkl_std = (qv_/(2*mu_**2*v_**2))*(4*X*qv_**2/(3*mN**2*om_**4))
check("C10", tot48 == 2 and sp.simplify(prod - kkl_std) == 0,
      "(4.8) integrates to 2 sigma_n (O1, F = 1): 2x the standard; printed product (4.6)(4.7)(4.8) = KKL x standard")

# ------------------------------------------------------------------------------------------------------------------
# C11 (LE-64): A^IR = S_Z(0)/M (charge fluctuation), B^IR from the k^2 slope / c^2 (locally neutral units); 1D chain
N11 = 800
Kspr = 1 + 0.3*rng.uniform(-1, 1, N11)          # spring disorder (glass-like)
Dm = np.zeros((N11, N11))
for i in range(N11):
    j = (i + 1) % N11
    Dm[i, i] += Kspr[i]; Dm[j, j] += Kspr[i]; Dm[i, j] -= Kspr[i]; Dm[j, i] -= Kspr[i]
w2, ev = np.linalg.eigh(Dm)                     # M = 1
ceff = np.sqrt(1/np.mean(1/Kspr))               # sound speed of the disordered chain (M = 1, a = 1)
low = (w2 > 1e-8) & (np.sqrt(np.abs(w2)) < 0.12)
wl = np.sqrt(w2[low])


def SZ(z, k):
    return np.abs(np.exp(1j*np.outer(k, np.arange(N11))) @ z)**2/N11


okr, okd = [], []
for rep in range(20):
    zr = rng.normal(0, 1, N11); zr -= zr.mean()                                   # fluctuating charges, global neutrality
    zd = np.repeat(rng.normal(0, 1, N11//2), 2)*np.tile([1, -1], N11//2)          # locally neutral dimers
    for z, acc in ((zr, okr), (zd, okd)):
        Cm = (z @ ev[:, low])**2*N11/N11                  # |p_nu|^2 (M = 1)
        pred = SZ(z, wl/ceff)                             # (CW2.20): C^IR(w) = S_Z(w/c)/M
        acc.append((Cm.mean(), pred.mean()))
okr = np.array(okr).mean(0); okd = np.array(okd).mean(0)
check("C11", abs(okr[0]/okr[1] - 1) < 0.02 and abs(okd[0]/okd[1] - 1) < 0.05 and okd[0] < 0.01*okr[0],
      f"C^IR(w<0.12) vs S_Z(w/c)/M: random charges {okr[0]:.3f}/{okr[1]:.3f} (A term); neutral dimers {okd[0]:.4f}/{okd[1]:.4f} (B w^2 term), (CW2.20)")

# ------------------------------------------------------------------------------------------------------------------
# C12 (LE-65): Lifshitz single mass defect, 1D chain: D_I/D_0 = (1-eps)(1 - 2 eps w^2 M ReG0) + O(eps^2)
N12, eps12, gam = 900, 0.04, 0.03
D0m = np.zeros((N12, N12))
for i in range(N12):
    j = (i + 1) % N12
    D0m[i, i] += 1; D0m[j, j] += 1; D0m[i, j] -= 1; D0m[j, i] -= 1


def ldos(Mimp, wgrid):
    Mv = np.ones(N12); Mv[0] = Mimp
    Dd = D0m/np.sqrt(np.outer(Mv, Mv)); w2l, el = np.linalg.eigh(Dd)
    wl = np.sqrt(np.clip(w2l, 0, None))
    return np.array([np.sum(el[0]**2*gam/np.pi/((wg_ - wl)**2 + gam**2)) for wg_ in wgrid])


wgrid = np.array([0.6, 1.0, 1.4])
lam0 = 4*np.sin(np.pi*np.arange(1, N12)/N12)**2
G0 = np.array([np.mean(1/(lam0 - (wg_ + 1j*gam)**2)) for wg_ in wgrid])
Dh = ldos(1.0, wgrid)
ok12 = True; txt = []
for e12 in (0.04, 0.3):
    meas = ldos(1 - e12, wgrid)/Dh
    exact = (1 - e12)*np.imag(G0/(1 + e12*(wgrid + 1j*gam)**2*G0))/np.imag(G0)       # (CW2.21)
    lin = (1 - e12)*(1 - 2*e12*wgrid**2*G0.real)                                     # (CW2.22)
    ok12 &= np.max(abs(meas - exact)) < 0.01
    txt.append(f"eps={e12}: meas " + "/".join(f"{v:.3f}" for v in meas) + " exact " + "/".join(f"{v:.3f}" for v in exact)
               + " O(eps) " + "/".join(f"{v:.3f}" for v in lin))
check("C12", ok12, "Lifshitz LDOS ratio D_I/D_0 at w = 0.6, 1.0, 1.4: " + "; ".join(txt))
# Si isotopes: kappa_1 = sum x M (th - thbar)^2 eps / sigma_w,  eps_I = (Mbar - M_I)/Mbar
iso = [(27.9769265, 14, 0.92223), (28.9764947, 15, 0.04685), (29.9737702, 16, 0.03092)]
Mb = sum(m_*x_ for m_, n_, x_ in iso); thb = sum(x_*n_ for m_, n_, x_ in iso)/Mb
sw = sum(x_*m_*(n_/m_ - thb)**2 for m_, n_, x_ in iso)
kap1 = sum(x_*m_*(n_/m_ - thb)**2*(Mb - m_)/Mb for m_, n_, x_ in iso)/sw
wD = 0.0645
ReG = lambda w: (3/wD**3)*(wD + (w/2)*np.log(abs((wD - w)/(wD + w))))
hiso = lambda w: -1 - 2*w**2*ReG(w)
check("C12b", abs(sw/(Mb*thb**2) - 1.879e-4) < 0.002e-4 and abs(kap1 + 0.0536) < 5e-4 and abs(hiso(0.050) + 1.718) < 5e-3,
      f"sigma_w/(M thbar^2) = {sw/(Mb*thb**2):.3e}; kappa_1 = {kap1:+.4f}; Debye h_iso(50 meV) = {hiso(0.050):+.3f}; dGamma/Gamma = {kap1*hiso(0.050):+.4f}")

# ------------------------------------------------------------------------------------------------------------------
# C13 (LE-66, errata): two-phonon absorption alpha(w;T) = sum over pairs [ (1+n_i+n_j) delta(w - w_i - w_j) + (n_j - n_i) delta(w - (w_i - w_j)) ]
# with T-independent second-order dipoles A_ij. (a) T-independent frequencies: alpha(.;0) <= alpha(.;293 K) bin by bin;
# (b) with a 1% quasi-harmonic shift the pointwise statement can fail for narrow bins, (c) but holds for bins widened by the shift.
nB = lambda w, T: 1/np.expm1(w/T)
T293 = 0.025249
fac = 1 + 2*nB(0.025, T293)
w1 = rng.uniform(0.005, 0.064, 120); A13 = rng.uniform(0, 1, (120, 120)); A13 = (A13 + A13.T)/2


def alpha_lines(wph, T, Amp=None):
    Amp = A13 if Amp is None else Amp
    W1, W2 = np.meshgrid(wph, wph, indexing="ij"); iu = np.triu_indices(len(wph))
    nn = (lambda w: nB(w, T) if T > 0 else 0*w)
    ws = (W1 + W2)[iu]; As = (Amp*(1 + nn(W1) + nn(W2)))[iu]
    dmask = W1 > W2
    wd = (W1 - W2)[dmask]; Ad = (Amp*(nn(W2) - nn(W1)))[dmask]
    return np.concatenate([ws, wd]), np.concatenate([As, Ad])


def binned(wl, Al, edges):
    return np.histogram(wl, bins=edges, weights=Al)[0]


edges = np.linspace(0.04, 0.06, 41)                                    # 0.5 meV bins around 50 meV
l0, a0_ = alpha_lines(w1, 0.0); l293, a293 = alpha_lines(w1, T293)
ok_a = np.all(binned(l0, a0_, edges) <= binned(l293, a293, edges) + 1e-12)
w1_293 = w1/(1 + rng.uniform(0, 0.01, len(w1)))                         # 293 K frequencies up to 1% softer
l293s, a293s = alpha_lines(w1_293, T293)
# isolated feature (one overtone pair 25 + 25 meV): a 1% softening at 293 K moves it out of its 0.2 meV bin, so the narrow-bin
# (pointwise) inequality fails although the line is 2.18x stronger at 293 K
lb0, ab0 = alpha_lines(np.array([0.025]), 0.0, np.ones((1, 1))); lb3, ab3 = alpha_lines(np.array([0.025/1.01]), T293, np.ones((1, 1)))
nb_ = np.array([0.0499, 0.0501])
fail_b = binned(lb0, ab0, nb_)[0] > binned(lb3, ab3, nb_)[0]
okc = True
for lo_, hi_ in zip(edges[:-1], edges[1:]):
    s0 = a0_[(l0 >= lo_) & (l0 < hi_)].sum()
    s293 = a293s[(l293s >= lo_/1.0101) & (l293s < hi_)].sum()            # 293 K bin widened by the shift (w(0) = w(293)(1+s), s <= 1%)
    okc &= s0 <= s293 + 1e-12
check("C13", fac > 2.17 and ok_a and fail_b and okc,
      f"sum-process factor 2.18 at 293 K (25+25 meV); model two-phonon spectrum: alpha_0 <= alpha_293 per 0.5 meV bin with T-independent w ({ok_a}); "
      f"1% shift breaks the narrow-bin statement ({fail_b}); restored for bins widened by the shift ({okc})")

# ------------------------------------------------------------------------------------------------------------------
# C14 (LE-67, errata): GaAs LO-residue vertex d with ONE Z* (the LST value computed here), its sensitivities, and the
# rigid-ion factor of 2308.06314 Fig. 2 (LE-68): (d_rigid/d)^2 with Q_Ga = +3, Q_As = -3 (rigid vertex Z - Q/eps_inf)
MGa, MAs, ZGa, ZAs, einf = 69.723, 74.9216, 31, 33, 10.9
eps0SI, eC, uK = 8.8541878e-12, 1.602176634e-19, 1.66053907e-27
aL = 5.6533e-10; Om = aL**3/4; muR = MGa*MAs/(MGa + MAs)*uK
wT, wL = 2*np.pi*8.06e12, 2*np.pi*8.75e12
ZLST = np.sqrt(eps0SI*einf*Om*muR*(wL**2 - wT**2))/eC
dfun = lambda zs, ei=einf, mga=MGa, mas=MAs: (ZGa - zs/ei)/mga - (ZAs + zs/ei)/mas
d0 = dfun(ZLST); dd_z = dfun(ZLST*1.1) - d0; dd_m = dfun(ZLST, mga=MGa + 0.01) - d0
slope_z = 1/MGa + 1/MAs
dzeta_max = 0.1*abs(d0)/slope_z                       # |delta(Z*/eps)| for 10% in d (20% in rate)
dM_max = 0.1*abs(d0)/((ZGa - ZLST/einf)/MGa**2)
d21 = dfun(2.1); drig = dfun(3.0)
r_rig = (drig/d0)**2; r_rig21 = (drig/d21)**2
check("C14", abs(ZLST - 2.160) < 0.002 and abs(d0 + 1.327e-3) < 3e-6 and abs(dd_z/d0 - 0.414) < 0.005
      and abs(dzeta_max/(ZLST/einf) - 0.024) < 0.001 and abs(dM_max - 0.021) < 0.001 and abs(d21 + 1.179e-3) < 3e-6
      and abs(r_rig - 6.80) < 0.05 and abs(r_rig21 - 8.67) < 0.05,
      f"LST |Z*| = {ZLST:.3f} [UNVERIFIED inputs]; d = {d0:.4e} (Z* = 2.1: {d21:.4e}); +10% Z*/eps -> {100*dd_z/d0:+.1f}%; "
      f"+0.01 u M_Ga -> {100*dd_m/d0:+.1f}%; 20% rate needs |d(Z*/eps)| <= {dzeta_max:.2e} ({100*dzeta_max/(ZLST/einf):.1f}%), dM_Ga <= {dM_max:.3f} u; "
      f"rigid-ion rate factor (d_rig/d)^2 = {r_rig:.2f} (LST Z*), {r_rig21:.2f} (Z* = 2.1)")

# ------------------------------------------------------------------------------------------------------------------
# C15 (LE-69, errata): slab reflectance from 2x2 transfer matrices (not from the closed form) and its thickness average 2R/(1+R)


def slab_R(k, kp, L):
    def iface(k1, k2):     # (A, B) amplitudes of e^{+-ik x} across an interface at x = 0: continuity of psi, psi'
        return 0.5*np.array([[1 + k1/k2, 1 - k1/k2], [1 - k1/k2, 1 + k1/k2]], complex)
    prop = np.diag([np.exp(1j*kp*L), np.exp(-1j*kp*L)])
    # left (A1, B1) = (1, r) -> right (A3, B3) = (t, 0); amplitudes re-referenced to x = L by the outer phase matrix
    Mx = np.diag([np.exp(-1j*k*L), np.exp(1j*k*L)]) @ iface(kp, k) @ prop @ iface(k, kp)
    r = -Mx[1, 0]/Mx[1, 1]
    return abs(r)**2


k, kp = 1.0, 0.6
Rs = ((k - kp)/(k + kp))**2
Ls = np.linspace(50, 50 + 10*np.pi/kp, 4000, endpoint=False)
Rl = np.array([slab_R(k, kp, L) for L in Ls])
closed = (k**2 - kp**2)**2*np.sin(kp*Ls)**2/((k**2 - kp**2)**2*np.sin(kp*Ls)**2 + 4*k**2*kp**2)
check("C15", np.max(abs(Rl - closed)) < 1e-12 and abs(np.mean(Rl) - 2*Rs/(1 + Rs)) < 1e-9,
      f"transfer-matrix <R_slab>_L = {np.mean(Rl):.8f} vs 2R/(1+R) = {2*Rs/(1+Rs):.8f} (R_step = {Rs:.4f}); TM = closed form to 1e-12")

# ------------------------------------------------------------------------------------------------------------------
# C16 (LE-72): absorbing Markov chain P = (I - T)^-1 b vs Monte Carlo
nS = 6
Tm = rng.uniform(0, 1, (nS, nS)); bvec = rng.uniform(0, 0.6, nS); lost = rng.uniform(0, 0.3, nS)
norm = Tm.sum(1) + bvec + lost; Tm /= norm[:, None]; bvec /= norm; lost /= norm
Pex = np.linalg.solve(np.eye(nS) - Tm, bvec)
hits = 0; Nmc = 40000
for _ in range(Nmc):
    s = 0
    while True:
        u = rng.uniform()
        cum = np.cumsum(np.concatenate([Tm[s], [bvec[s], lost[s]]]))
        j = int(np.searchsorted(cum, u))
        if j < nS:
            s = j
        else:
            hits += (j == nS); break
check("C16", abs(hits/Nmc - Pex[0]) < 0.01, f"P(chiral band | start 0): exact {Pex[0]:.4f}, MC {hits/Nmc:.4f}")

# ------------------------------------------------------------------------------------------------------------------
# C17 (LE-71): diamond basis structure factor sum_kappa e^{-iG.r_kappa}: zero at (200), |.|^2 = 2 at (111), 4 at (220)
rb = [np.zeros(3), np.array([0.25, 0.25, 0.25])]
SF = lambda G: abs(sum(np.exp(-2j*np.pi*np.dot(G, rr)) for rr in rb))**2
check("C17", SF([2, 0, 0]) < 1e-20 and abs(SF([1, 1, 1]) - 2) < 1e-12 and abs(SF([2, 2, 0]) - 4) < 1e-12,
      "diamond: |S(200)|^2 = 0, |S(111)|^2 = 2, |S(220)|^2 = 4 (Umklapp channels of (CW2.26))")

# ------------------------------------------------------------------------------------------------------------------
# C18 (LE-53): <mu^{2k} e^{-i x mu}>_mu = (-1)^k j0^{(2k)}(x); n_ph = 2 isotropic-glass kernel
xx, mu = sp.symbols('x mu', real=True)
j0 = sp.sin(xx)/xx
ok18 = True
for kk in range(3):
    rhs = sp.lambdify(xx, (-1)**kk*sp.diff(j0, xx, 2*kk))
    for xv in (0.7, 2.3, 9.1):
        lhs = integrate.quad(lambda m_: m_**(2*kk)*np.cos(xv*m_), -1, 1)[0]/2
        ok18 &= abs(lhs - rhs(xv)) < 1e-10
check("C18", ok18, "<mu^2k e^{-ix mu}> = (-1)^k d^2k j0/dx^2k, k = 0, 1, 2 (angular kernel of (CW2.12))")

# ------------------------------------------------------------------------------------------------------------------
# C19 (LE-57): T > 0 route: FFT of e^{-2W}[e^{Phi(t)} - 1] for an Einstein site equals the exact Bessel weights
w0, T19, y = 1.0, 0.7, 0.8          # omega_0, T, y = q^2/(2 M omega_0)
nB0 = 1/np.expm1(w0/T19)
twoW = y*(2*nB0 + 1)
Nt, dt = 2**16, 0.05
tt = (np.arange(Nt) - Nt//2)*dt
Phi = y*((nB0 + 1)*np.exp(-1j*w0*tt) + nB0*np.exp(1j*w0*tt))
reg = np.exp(-0.5*(tt/600)**2)
St = np.exp(-twoW)*(np.exp(Phi) - 1)*reg
Sw = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(St)))*Nt*dt   # int dt e^{+i w t}
om = np.fft.fftshift(np.fft.fftfreq(Nt, dt))*2*np.pi
ok19 = True
for nn in [-2, -1, 1, 2, 3]:
    sel = np.abs(om - nn*w0) < 0.3
    wnum = np.sum(Sw[sel].real)*(om[1] - om[0])/(2*np.pi)
    wex = np.exp(-twoW)*special.iv(nn, 2*y*np.sqrt(nB0*(nB0 + 1)))*np.exp(nn*w0/(2*T19))
    ok19 &= abs(wnum - wex) < 1e-4
check("C19", ok19, "T>0 FFT route reproduces the Einstein-site weights e^{-2W} I_n(2y sqrt(n(n+1))) e^{n w0/2T}, n = -2..3")

# ------------------------------------------------------------------------------------------------------------------
# C20 (LE-56): reciprocal-space form Dn(q) = 3 sum_G n(G) e^{iG.R}[(q^.(q-G)^)^2 - 1/3] (continuum test, Gaussian density)
ok20 = True
for qv in (0.5, 1.5, 3.0):
    real = 6*integrate.quad(lambda x_: np.exp(-x_**2/2)*special.spherical_jn(2, qv*x_)/x_, 0, 40, limit=400)[0]
    nk = lambda k_: (2*np.pi)**1.5*np.exp(-k_**2/2)
    fk = lambda c_, k_: 3/(2*np.pi)**3*2*np.pi*k_**2*nk(k_)*((qv - k_*c_)**2/(qv*qv + k_*k_ - 2*qv*k_*c_) - 1/3)
    rec = integrate.dblquad(fk, 0, 12, -1, 1, epsabs=1e-10)[0]
    ok20 &= abs(real - rec) < 1e-8
check("C20", ok20, "Delta n(q): real-space PV form (5.2'') = reciprocal-space form (CW2.16) for a Gaussian density at q = 0.5, 1.5, 3")

# ------------------------------------------------------------------------------------------------------------------
# C16b (LE-72, errata): binary cascade with competing channels. Corrected (CW2.27'): N = (1 - M)^-1 b with
#   M_{ll'} = [sum_{l''} (1 + delta_{l'l''}) Gu_{l->{l'l''}} + Gi_{l->l'}] / Gall_l,   Gall = G3ph + Giso + Gbdry,  rows of stable states = 0,
# Gu per UNORDERED pair. Equivalent ordered form: Gord_ab = Gu (a != b), Gord_aa = 2 Gu, M = sum_{l''} Gord / Gall (no 1 + delta).
# Monte Carlo of the branching process; the CW2.md form (normalised by G3ph alone, ordered rates with 1 + delta) is shown to differ.
import itertools
lev = np.repeat(np.arange(4), 3); nS16 = len(lev)
stab = np.zeros(nS16, bool); stab[[0, 3]] = True                 # chiral-stable (long-lived, |L| > L_th): terminal, b = 1
Gb16 = rng.uniform(0.05, 0.3, nS16); Gb16[stab] = 0
Gu16 = {}
for l in range(nS16):
    if stab[l] or lev[l] == 0:
        continue
    for a_, b_ in itertools.combinations_with_replacement([j for j in range(nS16) if lev[j] < lev[l]], 2):
        if rng.uniform() < 0.5:
            Gu16[(l, a_, b_)] = rng.uniform(0, 1)
Gi16 = np.array([[rng.uniform(0, 0.5) if (j != l and lev[j] == lev[l] and not stab[j] and not stab[l]) else 0.0
                  for j in range(nS16)] for l in range(nS16)])
G3_16 = np.array([sum(v for (l, a_, b_), v in Gu16.items() if l == s_) for s_ in range(nS16)])
Gall16 = G3_16 + Gi16.sum(1) + Gb16
b16 = stab.astype(float)


def Mmat(ordered=False, as_written=False):
    Mx = np.zeros((nS16, nS16))
    for (l, a_, b_), v in Gu16.items():
        den = G3_16[l] if as_written else Gall16[l]
        if a_ != b_:
            Mx[l, a_] += v/den; Mx[l, b_] += v/den
        else:
            Mx[l, a_] += (2*v*(2 if as_written else 1) if ordered else 2*v)/den      # as_written: ordered Gord_aa = 2Gu with (1 + delta)
    if not as_written:
        Mx += Gi16/np.where(Gall16 > 0, Gall16, 1)[:, None]
    return Mx


Mc = Mmat(); Nc = np.linalg.solve(np.eye(nS16) - Mc, b16)
Mo = Mmat(ordered=True); Nw = np.linalg.solve(np.eye(nS16) - Mmat(ordered=True, as_written=True), b16)


def cascade(s_):
    n_, stack = 0, [s_]
    while stack:
        x_ = stack.pop()
        if stab[x_]:
            n_ += 1; continue
        u_ = rng.uniform()*Gall16[x_]
        if u_ < Gb16[x_]:
            continue
        u_ -= Gb16[x_]
        if u_ < Gi16[x_].sum():
            stack.append(int(np.searchsorted(np.cumsum(Gi16[x_]), u_))); continue
        u_ -= Gi16[x_].sum()
        for (l, a_, b_), v in Gu16.items():
            if l == x_:
                if u_ < v:
                    stack += [a_, b_]; break
                u_ -= v
    return n_


s16 = nS16 - 1; mc16 = np.array([cascade(s16) for _ in range(20000)])
err16 = mc16.std()/np.sqrt(len(mc16))
Mnoiso = Mc - Gi16/np.where(Gall16 > 0, Gall16, 1)[:, None]
check("C16b", abs(mc16.mean() - Nc[s16]) < 4*err16 and np.allclose(Mo, Mc) and abs(Nw[s16] - Nc[s16]) > 8*err16
      and max(abs(np.linalg.eigvals(Mc))) < 1 and np.abs(np.linalg.matrix_power(Mc, 12)).max() > 0
      and np.abs(np.linalg.matrix_power(Mnoiso, 4)).max() < 1e-15,
      f"expected chiral count: (1-M)^-1 b = {Nc[s16]:.4f}, MC {mc16.mean():.4f} +- {err16:.4f}; ordered form = unordered form; "
      f"CW2.md form (G3ph-normalised, ordered + (1+delta)) {Nw[s16]:.4f}; with Tamura M not nilpotent, spectral radius "
      f"{max(abs(np.linalg.eigvals(Mc))):.3f} < 1 (losses); without Tamura M^4 = 0")

# ------------------------------------------------------------------------------------------------------------------
# C21 (LE-53, errata): (CW2.12) is not exact for non-uniaxial pair tensors. Counterexample 4 eps^2/15 (sympy) and the exact
# phi-averaged forms for n = 2, 3 in rotational invariants about r^:
#   <(q^.B.q^)^2>_phi = A0^2 + 2 mu^2(1-mu^2)|b|^2 + (1-mu^2)^2 |tau|^2/2,
#   <(q^.B.q^)^3>_phi = A0^3 + 3 A0[2 mu^2(1-mu^2)|b|^2 + (1-mu^2)^2|tau|^2/2] + 3 mu^2 (1-mu^2)^2 b.tau.b,
#   A0 = B_T + (B_L - B_T) mu^2, B_L = r.B.r, b = P_perp B r, B_T = tr(P_perp B P_perp)/2, tau = P_perp B P_perp - B_T P_perp, |tau|^2 = tr tau^2 / 2;
# then mu^{2k} -> (-1)^k j0^{(2k)}(qr). Checked against a direct (Gauss-Legendre x uniform-phi) average of e^{-iq.r}(q^.B.q^)^n.
mu_s, ph_s = sp.symbols('mu phi', real=True)
BLs, BTs, bcs, bss, tcs, tss, eps_s = sp.symbols('B_L B_T b_c b_s t_c t_s epsilon', real=True)
Bsym = sp.Matrix([[BTs + tcs, tss, bcs], [tss, BTs - tcs, bss], [bcs, bss, BLs]])
ns_ = sp.Matrix([sp.sqrt(1 - mu_s**2)*sp.cos(ph_s), sp.sqrt(1 - mu_s**2)*sp.sin(ph_s), mu_s])
fB = sp.expand((ns_.T*Bsym*ns_)[0])
A0s = BTs + (BLs - BTs)*mu_s**2; b2s = bcs**2 + bss**2; t2s = tcs**2 + tss**2; Js = (bcs**2 - bss**2)*tcs + 2*bcs*bss*tss
form = {2: A0s**2 + 2*mu_s**2*(1 - mu_s**2)*b2s + (1 - mu_s**2)**2*t2s/2,
        3: A0s**3 + 3*A0s*(2*mu_s**2*(1 - mu_s**2)*b2s + (1 - mu_s**2)**2*t2s/2) + 3*mu_s**2*(1 - mu_s**2)**2*Js}
ok21 = all(sp.expand(sp.integrate(sp.expand(fB**n_), (ph_s, 0, 2*sp.pi))/(2*sp.pi) - form[n_]) == 0 for n_ in (2, 3))
cex = sp.simplify((sp.integrate(form[2], (mu_s, -1, 1))/2 - sp.integrate(A0s**2, (mu_s, -1, 1))/2).subs({bcs: eps_s, bss: 0, tcs: 0, tss: 0}))
ok21 &= sp.simplify(cex - 4*eps_s**2/15) == 0
j0d = [sp.lambdify(xx, (-1)**kk*sp.diff(sp.sin(xx)/xx, xx, 2*kk)) for kk in range(4)]
xg21, wg21 = np.polynomial.legendre.leggauss(60); ph21 = np.linspace(0, 2*np.pi, 64, endpoint=False)
worst21 = 0.0
for trial in range(4):
    Bm = rng.normal(size=(3, 3)); Bm = Bm + Bm.T
    rh = rng.normal(size=3); rh /= np.linalg.norm(rh)
    e1 = np.cross(rh, [1.0, 0, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(rh, e1)
    Rt = np.array([e1, e2, rh])                                   # rows: local x, y, z(= r^)
    Bl = Rt @ Bm @ Rt.T
    inv = {BLs: Bl[2, 2], BTs: (Bl[0, 0] + Bl[1, 1])/2, bcs: Bl[0, 2], bss: Bl[1, 2], tcs: (Bl[0, 0] - Bl[1, 1])/2, tss: Bl[0, 1]}
    for n_ in (2, 3):
        poly = sp.Poly(sp.expand(form[n_].subs(inv)), mu_s)
        for xv in (1.7, 6.3, 11.0):                                   # qr = 0 is the sympy statement above
            pred = sum(float(cf)*j0d[m_[0]//2](xv) for m_, cf in zip(poly.monoms(), poly.coeffs()))
            direct = 0.0
            for mu_v, w_v in zip(xg21, wg21):
                s_v = np.sqrt(1 - mu_v**2)
                qh = np.stack([s_v*np.cos(ph21), s_v*np.sin(ph21), mu_v*np.ones_like(ph21)], 1) @ Rt   # global q^
                val = np.einsum('ia,ab,ib->i', qh, Bm, qh)**n_*np.cos(xv*mu_v)
                direct += w_v*val.mean()/2
            worst21 = max(worst21, abs(pred - direct)/max(1.0, abs(direct)))
check("C21", ok21 and worst21 < 1e-9,
      f"(CW2.12) non-uniaxial excess at n = 2, qr = 0: {cex} (not 0); exact n = 2, 3 invariant forms = direct q^ average to {worst21:.1e}")

# ------------------------------------------------------------------------------------------------------------------
# C22 (LE-52/LE-70, errata): Christoffel mass asymptote rho(xi) ~ (k4 + 2 k2^2 - k3^2/k2)/(xi - k1)^4 (sympy), and the tail band is
# absolute, not relative: for a Gaussian at xi = k1 - 4 sigma the Markov-Krein band is [0, rho] with rho/F_true ~ 10^2.
xs22, k2s, k3s, k4s = sp.symbols('xi k2 k3 k4', real=True)
mom22 = [1, 0, k2s, k3s, k4s + 3*k2s**2]
H22 = sp.Matrix(3, 3, lambda i, j: mom22[i + j]); v22 = sp.Matrix([1, xs22, xs22**2])
rho22 = 1/sp.simplify((v22.T*H22.inv()*v22)[0])
asym = sp.simplify(sp.limit(rho22*xs22**4, xs22, sp.oo))
gm = [1.0, 0.0, 1.0, 0.0, 3.0]
lo22, up22, rh22, _ = mk_bounds(gm, -4.0)
Ftrue = 0.5*special.erfc(4/np.sqrt(2))
check("C22", sp.simplify(asym - (k4s + 2*k2s**2 - k3s**2/k2s)) == 0 and sp.simplify(rho22.subs({k3s: 0, k4s: 0, xs22: 0}) - sp.Rational(2, 3)) == 0
      and lo22 == 0 and up22/Ftrue > 100,
      f"rho asymptote = ({asym})/(xi-k1)^4 (Gaussian 2 sigma^4/x^4); Gaussian at -4 sigma: band [{lo22:.0f}, {up22:.2e}] vs F = {Ftrue:.2e} (ratio {up22/Ftrue:.0f})")

# ------------------------------------------------------------------------------------------------------------------
# C23 (LE-54, LE-56, errata) [CALC] ld1/results-errata.json: (a) NR n(r_min) is low by the Kato cusp 2 Z r_min (same for all species,
# 2 e^{-7} = 1.82e-3 at xmin = -7): checked by varying xmin; extrapolated n(0) grid-independent; (b) SR/Dirac point-nucleus densities
# diverge as r^{2(gamma-1)}: n(r_min) grid-dependent; (c) Delta n(q) (numerator of r - 1) is xmin-independent and changes by only
# +0.4..1.5% (Si), +2..5.7% (Ge/Ga/As) Dirac vs NR; (d) finite-nucleus [E]: Dirac density at the uniform-sphere radius.
le = json.load(open(f"{HERE}/ld1/results-errata.json"))
Amass = {"Si": 28.0855, "Ge": 72.630, "Ga": 69.723, "As": 74.9216}
ok23 = True; txt23 = []; n0fix = {}
for el in Amass:
    Z_ = Zs[el]; r7, r8 = le[f"{el}_rel0_x7"], le[f"{el}_rel0_x8"]
    cusp = r7["n_r0"]/r8["n_r0"] - 1
    ok23 &= abs(cusp/(-2*Z_*(r7["r0"] - r8["r0"])) - 1) < 0.02
    n0_7 = r7["n_r0"]*(1 + 2*Z_*r7["r0"]); n0_8 = r8["n_r0"]*(1 + 2*Z_*r8["r0"])
    ok23 &= abs(n0_7/n0_8 - 1) < 1e-5 and abs(2*Z_*r7["r0"] - 2*np.exp(-7)) < 1e-8
    n0fix[el] = n0_8
    gam_ = np.sqrt(1 - (Z_/137.035999)**2); ex_ = 2*(gam_ - 1)
    s1, s2 = le[f"{el}_rel1_x7"], le[f"{el}_rel1_x8"]
    ok23 &= abs(s1["slope"]/ex_ - 1) < 0.01 and s2["n_r0"]/s1["n_r0"] - 1 > (0.01 if Z_ < 20 else 0.05)     # SR n(r_min) moves with the grid
    for rel in (0, 1, 2):
        a_, b_ = le[f"{el}_rel{rel}_x7"]["dn"], le[f"{el}_rel{rel}_x8"]["dn"]
        ok23 &= all(abs(a_[q_]/b_[q_] - 1) < 1e-5 for q_ in a_)
    dD = [le[f"{el}_rel2_x8"]["dn"][q_]/r8["dn"][q_] - 1 for q_ in r8["dn"]]
    ok23 &= (0.003 < min(dD) and max(dD) < 0.016) if el == "Si" else (0.018 < min(dD) and max(dD) < 0.06)
    RN = np.sqrt(5/3)*(0.836*Amass[el]**(1/3) + 0.570)/52917.721            # uniform-sphere radius from r_rms [E], bohr
    D8 = le[f"{el}_rel2_x8"]; nR = D8["n_r0"]*(RN/D8["r0"])**ex_
    exc = (nR/n0_8, nR*3/(3 + ex_)/n0_8)
    txt23.append(f"{el}: n(0) = {n0_8:.1f}, Dirac/NR(0) at R_N {exc[0]:.3f}-{exc[1]:.3f}, dDelta n {100*min(dD):.1f}..{100*max(dD):.1f}%")
    qmax = 300.0/3.7289; inner = n0_8*qmax**2*RN**2/5                    # r < R_N part of Delta n for a flat density (sympy below)
    ok23 &= inner/le[f"{el}_rel2_x8"]["dn"]["300.0"] < 1e-4                 # Delta n(q) is insensitive to the nuclear model
rr_, qq_, RR_ = sp.symbols('rho q R', positive=True)
j2s = (3/(qq_*rr_)**3 - 1/(qq_*rr_))*sp.sin(qq_*rr_) - 3*sp.cos(qq_*rr_)/(qq_*rr_)**2
inner_s = sp.integrate(6*sp.series(j2s, rr_, 0, 4).removeO()/rr_, (rr_, 0, RR_))
ok23 &= sp.simplify(inner_s - qq_**2*RR_**2/5) == 0
coefix = {el: coef[el]*n0fix[el]/ldr[f"{el}_r0_PBE_dx0.008"]["n0"] for el in coef}
check("C23", ok23 and abs(n0fix["Si"] - 1769.5) < 0.1,
      "; ".join(txt23) + " | E^Mig_3/E_R at n(0) [NR]: " + ", ".join(f"{k} {v:.0f}" for k, v in coefix.items()) + " eV^2")

# ------------------------------------------------------------------------------------------------------------------
# C24 (LE-51, errata): plane-wave cutoffs. E[Ry] = |G|^2 [bohr^-2];  1/a0 = 3.7289 keV.
KEV_PER_INV_BOHR_ = 3.7289
G30 = 1.5*20/KEV_PER_INV_BOHR_; G1s = 5*13.7
check("C24", abs(G30**2 - 64.7) < 0.2 and abs(G1s**2 - 4692) < 1 and abs(G1s*KEV_PER_INV_BOHR_ - 255.4) < 0.2,
      f"|G|_max = 30 keV = {G30:.3f}/a0 -> ecutrho {G30**2:.1f} Ry (not 260 Ry, which is 60 keV); 5/a_1s (Si, Z_eff 13.7) = {G1s*KEV_PER_INV_BOHR_:.0f} keV -> {G1s**2:.0f} Ry")

# ------------------------------------------------------------------------------------------------------------------
# C25 (LE-64, errata): C^IR(w) = <|p_nu|^2>_{w_nu = w} is a conditional average over modes, so the branch weights are the mode
# fractions w_nu = c_nu^-3 / sum c^-3, not 1/3. Plane-wave modes (the (CW2.20) hypothesis) on a 96^3 lattice, c_L = 2 c_T, locally neutral
# dipolar charge field z = div(eta) (S_z ~ k^2: the B term). MC conditional average over w < 0.5 vs the mode-count expectation and the
# continuum formulas with c^-3 weights and with 1/3 weights.
L25 = 96; N25 = L25**3; cL25, cT25 = 2.0, 1.0
kk25 = 2*np.pi*np.fft.fftfreq(L25)
KX, KY, KZ = np.meshgrid(kk25, kk25, kk25, indexing='ij'); K25 = np.sqrt(KX**2 + KY**2 + KZ**2)
mz2 = np.where(K25 > 0, (KZ/np.where(K25 > 0, K25, 1))**2, 0)
Sens = 4*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2)
wmax25 = 0.5
sL25 = (K25 > 0) & (cL25*K25 < wmax25); sT25 = (K25 > 0) & (cT25*K25 < wmax25)
nmode = sL25.sum() + 2*sT25.sum()
num25 = 0.0
for rep in range(4):
    eta = rng.normal(size=(3, L25, L25, L25))
    z25 = sum(eta[a_] - np.roll(eta[a_], 1, a_) for a_ in range(3))
    zk2 = np.abs(np.fft.fftn(z25))**2/N25
    num25 += ((mz2*zk2)[sL25].sum() + ((1 - mz2)*zk2)[sT25].sum())/nmode/4      # eps^ = z^: L gets kz^2, the two T modes 1 - kz^2
del eta, zk2
ens = ((mz2*Sens)[sL25].sum() + ((1 - mz2)*Sens)[sT25].sum())/nmode
ensk2 = ((mz2*K25**2)[sL25].sum() + ((1 - mz2)*K25**2)[sT25].sum())/nmode
wl25 = cL25**-3/(cL25**-3 + 2*cT25**-3); wt25 = cT25**-3/(cL25**-3 + 2*cT25**-3)
w2avg = 3*wmax25**2/5                                                     # <w^2> over a Debye-like D ~ w^2 up to wmax
new25 = (wl25/cL25**2 + 2*wt25/cT25**2)/3*w2avg; old25 = (1/cL25**2 + 2/cT25**2)/9*w2avg
del KX, KY, KZ, K25, mz2, Sens
check("C25", abs(num25/ens - 1) < 0.02 and abs(ensk2/new25 - 1) < 0.01 and abs(ensk2/old25 - 1) > 0.15,
      f"<|p|^2> over modes with w < 0.5: MC {num25:.5f} = ensemble {ens:.5f}; k^2 law on the grid {ensk2:.5f} = c^-3-weighted (CW2.20') {new25:.5f}, "
      f"not 1/3-weighted {old25:.5f} ({100*(old25/ensk2 - 1):+.0f}%)")

# ------------------------------------------------------------------------------------------------------------------
# C26 (LE-72 giant moments, errata): adiabatic one-phonon amplitude of a 4f moment = derivative of the ground-Kramers-doublet projected
# operator P(u) O P(u); dP = R dH P + P dH R, R = sum_{c not in g} |c><c|/(E_g - E_c). J = 15/2 (Dy3+-like), random time-reversal-even
# crystal-field Hamiltonians (Hermitian products of 2, 4, 6 angular-momentum components) vs finite differences.
jj = 7.5; mvals = np.arange(jj, -jj - 1, -1); dim = len(mvals)
Jz = np.diag(mvals); Jp = np.diag(np.sqrt(jj*(jj + 1) - mvals[1:]*(mvals[1:] + 1)), 1)
Jx = (Jp + Jp.T)/2; Jy = (Jp - Jp.T)/(2j); Jc = [Jx, Jy, Jz]


def cf_random():
    Hm = np.zeros((dim, dim), complex)
    for deg in (2, 4, 6):
        for _ in range(3):
            Pm = np.eye(dim, dtype=complex)
            for a_ in rng.integers(0, 3, deg):
                Pm = Pm @ Jc[a_]
            Hm += rng.normal()*(Pm + Pm.conj().T)/jj**deg
    return Hm


H0c, H1c = cf_random(), cf_random()


def proj_g(Hm):
    ev, U = np.linalg.eigh(Hm)
    return U[:, :2] @ U[:, :2].conj().T, ev, U


P0, ev0, U0 = proj_g(H0c)
Rres = sum(np.outer(U0[:, c_], U0[:, c_].conj())/(ev0[0] - ev0[c_]) for c_ in range(2, dim))
dP = Rres @ H1c @ P0 + P0 @ H1c @ Rres
hfd = 1e-6
ok26 = abs(ev0[1] - ev0[0]) < 1e-10 and ev0[2] - ev0[1] > 1e-3
for Oc in Jc:
    an = dP @ Oc @ P0 + P0 @ Oc @ dP
    Pp, Pm_ = proj_g(H0c + hfd*H1c)[0], proj_g(H0c - hfd*H1c)[0]
    fd = (Pp @ Oc @ Pp - Pm_ @ Oc @ Pm_)/(2*hfd)
    ok26 &= np.max(abs(an - fd)) < 1e-6*max(1, np.max(abs(fd)))
check("C26", ok26, "Kramers doublet: d(P J P)/du = dP J P + P J dP with dP = R dH P + P dH R reproduces finite differences (J = 15/2, random TR-even CF)")

# ------------------------------------------------------------------------------------------------------------------
# C27 (OC-3, errata): at 300 keV hydrogenic 1s^2 vs AE (NR): "< 1%" holds for r, not for r - 1; SR lowers r - 1 by 6-7% (Si), 28-34% (Ge/Ga/As)
# at r_min, of which the numerator Delta n changes by only +0.4..1.5% / +2..5% (C23): the rest is the contact density.
r300, h300 = rSi["300.0"]["total"], hyd(300.0)
sr_rel = {el: [(ldr[f"{el}_r1_PBE_dx0.008"]["rq"][q_]["total"] - 1)/(ldr[f"{el}_r0_PBE_dx0.008"]["rq"][q_]["total"] - 1) - 1 for q_ in rSi] for el in Zs}
check("C27", abs(r300/h300 - 1) < 0.007 and abs((r300 - 1)/(h300 - 1) - 1) > 0.01 and abs(rSi["102.0"]["total"]/hyd(102.0) - 1) < 0.001
      and all(-0.07 < v < -0.05 for v in sr_rel["Si"]) and all(-0.34 < v < -0.28 for el in ("Ge", "Ga", "As") for v in sr_rel[el]),
      f"Si 300 keV: r AE/hyd - 1 = {100*(r300/h300 - 1):+.2f}%, (r-1) AE/hyd - 1 = {100*((r300 - 1)/(h300 - 1) - 1):+.2f}%; SR/NR - 1 of r - 1 at r_min: "
      + ", ".join(f"{el} {100*min(v):.0f}..{100*max(v):.0f}%" for el, v in sr_rel.items()))

# ------------------------------------------------------------------------------------------------------------------
npass = sum(o for _, o in RES)
print(f"\n{npass}/{len(RES)} PASS")
if npass != len(RES):
    raise SystemExit(1)
