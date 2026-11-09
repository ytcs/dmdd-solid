"""O4 toy model: convention independence of the X0/X+ split (Theorem D iv'/iv'').
Run: python3 -I toy_fano.py   (< 30 s). Theory only; prints PASS/FAIL and fitted exponents.

Model (two-branch Fano-Anderson, exactly solvable).
  |d>        : zero-phonon e-h pair (X0), energy E_d = 0.
  |f,nu>     : pair + one phonon of branch nu (X+), total energy eps in a semicircle band
               (centre c_nu, half-width W_nu); electronic energy eps_e = eps - w_nu.
  coupling   : g*gam_nu (flat in f), Sigma_nu(z) = (g gam_nu)^2 (2/W^2)(x - sqrt(x^2-W^2)), x = z - c_nu.
  source     : DM vertex n|0> = rho|d> + sum_f t_f|f>,  t_f = lam_nu * g_f  (lam = off-shell A2-type
               path, O(1/delta); real if the crystal is PT-symmetric).
Exact branch-resolved spectrum (outgoing amplitude A_f = g_f[lam_nu + G(rho + Lam)]):
  S_nu(w) = Gam_nu(w) |lam_nu + G(w)(rho + Lam(w))|^2,  G = 1/(w - E_d - Sigma(w+i0)),  Lam = sum_mu lam_mu Sigma_mu.
Energy unit: delta (band half-width scale)."""
import numpy as np
from scipy.integrate import quad

Ed, rho = 0.0, 1.0
C   = np.array([-0.25, 0.20]); W = np.array([1.0, 0.8]); gam = np.array([1.0, 0.7])
wph = np.array([0.05, 0.30])                       # phonon energies of the two branches
LO, HI = (C - W).min(), (C + W).max()

def sig(w, g, nu):                                 # Sigma_nu(w + i0), complex
    x = w - C[nu]; G2 = (g*gam[nu])**2; a = 2*G2/W[nu]**2
    if abs(x) <= W[nu]: return a*x - 1j*a*np.sqrt(W[nu]**2 - x*x)
    return a*(x - np.sign(x)*np.sqrt(x*x - W[nu]**2))
def dsig_re(w, g, nu):                             # d/dw Re Sigma_nu inside band
    return 2*(g*gam[nu])**2/W[nu]**2
def Gam(w, g, nu): return -2*sig(w, g, nu).imag

def S_exact(w, g, lam):
    s = [sig(w, g, n) for n in (0, 1)]; G = 1/(w - Ed - sum(s)); Lam = sum(l*x for l, x in zip(lam, s))
    br = [-2*s[n].imag*abs(lam[n] + G*(rho + Lam))**2 for n in (0, 1)]
    tot = -2*(sum(abs(l)**2*x for l, x in zip(lam, s)) + G*(np.conj(rho) + sum(np.conj(l)*x for l, x in zip(lam, s)))*(rho + Lam)).imag
    return np.array(br), tot                       # tot: -2 Im<s|G|s> (optical-theorem check)

def C1_pieces(g, lam):
    """Convention C1 = (iv'): X0 = 2 pi Z |rho~|^2 delta(w - E~), split by branching (+ Fano term);
    X+ = Gam_nu [ |rho|^2 fp 1/D^2 + 2 Re(lam* rho) P 1/D + |lam|^2 ],  D = w - E_d.  All O(g^2)."""
    s = [sig(Ed, g, n) for n in (0, 1)]
    Et = Ed + sum(x.real for x in s); Z = 1 + sum(dsig_re(Ed, g, n) for n in (0, 1))
    Gm = np.array([-2*x.imag for x in s]); Gt = Gm.sum()
    rt2 = abs(rho)**2 + 2*sum((np.conj(rho)*l).real*x.real for l, x in zip(lam, s))
    c = np.array([(np.conj(rho)*l).imag for l in lam])
    W0nu_inc = 2*np.pi*Z*rt2*Gm/Gt                                   # incoherent cascade branching
    W0nu = W0nu_inc + 2*np.pi*Gm*((Gm*c).sum()/Gt - c)              # + Fano (production-decay) term
    return Et, Z, Gm, rt2, W0nu, W0nu_inc

def fp_int(F, E, lo, hi):        # Hadamard fp int_lo^hi F(w)/(w-E)^2, F smooth near E
    h = 1e-5; F0 = F(E); F1 = (F(E+h) - F(E-h))/(2*h)
    reg = quad(lambda w: (F(w) - F0 - F1*(w - E))/(w - E)**2, lo, hi, points=[E], limit=400, epsabs=1e-13)[0]
    return reg + F0*(-1/(hi - E) - 1/(E - lo)) + F1*np.log((hi - E)/(E - lo))
def pv_int(F, E, lo, hi):
    F0 = F(E); reg = quad(lambda w: (F(w) - F0)/(w - E), lo, hi, points=[E], limit=400, epsabs=1e-13)[0]
    return reg + F0*np.log((hi - E)/(E - lo))

def exact_int(f, g, lam, nu=None, Et=0.0, Gt=1.0, extra=()):
    def integrand(w):
        br, tot = S_exact(w, g, lam); return (tot if nu is None else br[nu])*f(w)
    pts = sorted(set([LO, HI] + list(C - W) + list(C + W) + [Et + k*Gt for k in (-20, -3, -1, 0, 1, 3, 20)] + list(extra)))
    pts = [p for p in pts if LO <= p <= HI]
    return sum(quad(integrand, a, b, limit=500, epsabs=1e-14, epsrel=1e-12)[0] for a, b in zip(pts[:-1], pts[1:]))

def C1_int(f, g, lam, nu, incoherent=False):
    Et, Z, Gm, rt2, W0nu, W0inc = C1_pieces(g, lam)
    lo, hi = C[nu] - W[nu], C[nu] + W[nu]
    Fg = lambda w: Gam(w, g, nu)*f(w)
    xp = abs(rho)**2*fp_int(Fg, Ed, lo, hi) + 2*(np.conj(lam[nu])*rho).real*pv_int(Fg, Ed, lo, hi) \
         + abs(lam[nu])**2*quad(Fg, lo, hi, limit=400)[0]
    return (W0inc if incoherent else W0nu)[nu]*f(Et) + xp, Et, Gm.sum()

def slope(gs, rs): return np.polyfit(np.log(gs), np.log(np.abs(rs)), 1)[0]
def rep(name, ok, extra=""): print(f"{'PASS' if ok else 'FAIL'}  {name:66s} {extra}")

phi = lambda w: np.exp(-((w - 0.05)/0.35)**2)          # smooth DM-energy weight (scale ~ delta)
gs = np.array([0.16, 0.08, 0.04, 0.02])

# T0 optical theorem: sum_nu S_nu = -2 Im <s|G|s>
lamc = [0.6*np.exp(0.9j), -0.4]
r = max(abs(S_exact(w, 0.1, lamc)[0].sum() - S_exact(w, 0.1, lamc)[1]) for w in np.linspace(-1.2, 1.0, 37))
rep("T0 optical theorem  sum_nu S_nu == -2 Im<s|G|s>  (complex lam)", r < 1e-12, f"res={r:.1e}")

# T1 (a): total, convention C1 vs exact, residual ~ g^4
lam = [0.6, -0.4]
res = []; tot0 = []
for g in gs:
    Et, Z, Gm, *_ = C1_pieces(g, lam)
    ex = exact_int(phi, g, lam, Et=Et, Gt=Gm.sum()); c1 = sum(C1_int(phi, g, lam, n)[0] for n in (0, 1))
    res.append(ex - c1); tot0.append(ex)
p = slope(gs, res); rep("T1 (a) <S_X0+S_X+ (C1), phi> - exact = O(g^4)", 3.7 < p < 4.3, f"exponent={p:.2f}  res={['%.1e'%x for x in res]}")

# T2 zeroth moment: Z + (1/2pi) fp int Gam/D^2 == 1 to O(g^4)   (Ward identity / KK)
res = []
for g in gs:
    Et, Z, *_ = C1_pieces(g, lam)
    fpw = sum(fp_int(lambda w, n=n: Gam(w, g, n), Ed, C[n] - W[n], C[n] + W[n]) for n in (0, 1))/(2*np.pi)
    res.append(Z + fpw - 1)
rep("T2 Z + (1/2pi) fp int Gamma/D^2 = 1  (exact, semicircle)", max(map(abs, res)) < 1e-9, f"max res={max(map(abs,res)):.1e}")

# T3 double-counting conventions: Lorentzian ZPL + fp sideband -> O(g^2) error; Lorentzian ZPL + Lorentzian sideband -> O(1)
r_LFP, r_LL = [], []
for g in gs:
    Et, Z, Gm, rt2, W0nu, _ = C1_pieces(g, lam); Gt = Gm.sum()
    lor = quad(lambda w: phi(w)*(Gt/2/np.pi)/((w - Et)**2 + Gt**2/4), LO, HI, points=[Et], limit=500, epsabs=1e-14)[0]
    c1 = sum(C1_int(phi, g, lam, n)[0] for n in (0, 1)); ex = exact_int(phi, g, lam, Et=Et, Gt=Gt)
    zpl_L = W0nu.sum()*lor
    r_LFP.append(ex - (c1 - W0nu.sum()*phi(Et) + zpl_L)); r_LL.append(ex - (zpl_L + ex))
rep("T3a Lorentzian ZPL + fp sideband: error O(g^2) (double-counted tail)", 1.7 < slope(gs, r_LFP) < 2.3, f"exponent={slope(gs, r_LFP):.2f}")
rep("T3b Lorentzian ZPL + resummed sideband: error O(1) (double-counted delta)", abs(r_LL[-1]/tot0[-1]) > 0.5, f"rel err={r_LL[-1]/tot0[-1]:.2f}")

# T4 (b): cascade-convolved quanta distribution P(Q), cascade = first emission + smooth quanta kernel
eps_pair, sQ = 0.1, 1.0
Qg = np.linspace(-6, 10, 33)
def kern(Q, ee): return np.exp(-0.5*((Q - ee/eps_pair)/sQ)**2)/np.sqrt(2*np.pi)/sQ
def PQ_exact(g, lam, Et, Gt):
    num = np.array([sum(exact_int(lambda w, n=n, Q=Q: phi(w)*kern(Q, w - wph[n]), g, lam, nu=n, Et=Et, Gt=Gt) for n in (0, 1)) for Q in Qg])
    return num/exact_int(phi, g, lam, Et=Et, Gt=Gt)
def PQ_C1(g, lam, incoherent=False, wph_c=None, gam_ratio=1.0):
    wc = wph if wph_c is None else wph_c
    Et, Z, Gm, rt2, W0nu, W0inc = C1_pieces(g, lam)
    W0 = (W0inc if incoherent else W0nu).copy()
    if gam_ratio != 1.0:                                   # cascade with a different g for branch 2
        b = Gm*np.array([1, gam_ratio**2]); W0 = W0.sum()*b/b.sum()
    out = []
    for Q in Qg:
        xp = sum(C1_int(lambda w, n=n: phi(w)*kern(Q, w - wph[n]), g, lam, n)[0] - W0nu[n]*phi(Et)*kern(Q, Et - wph[n]) for n in (0, 1))
        out.append(xp + sum(W0[n]*phi(Et)*kern(Q, Et - wc[n]) for n in (0, 1)))
    den = sum(C1_int(phi, g, lam, n)[0] for n in (0, 1))
    return np.array(out)/den
gb = gs[1:]
for tag, kw, lamx, expect in [("matched cascade, real lam", {}, lam, "g4"),
                              ("cascade with w_TO off by 10%", {"wph_c": wph*np.array([1, 1.1])}, lam, "O1"),
                              ("cascade with g_2 off by 20%", {"gam_ratio": 1.2}, lam, "O1"),
                              ("complex lam, incoherent cascade kernel", {"incoherent": True}, lamc, "g2"),
                              ("complex lam, Fano-corrected kernel", {}, lamc, "g4")]:
    errs = []
    for g in gb:
        Et, Z, Gm, *_ = C1_pieces(g, lamx)
        errs.append(np.abs(PQ_exact(g, lamx, Et, Gm.sum()) - PQ_C1(g, lamx, **kw)).max())
    p = slope(gb[-2:], errs[-2:])                         # asymptotic exponent (last two g)
    ok = {"g4": 3.6 < p < 4.4, "g2": 1.7 < p < 2.3, "O1": abs(p) < 0.4 and errs[-1] > 1e-3}[expect]
    rep(f"T4 (b) P(Q): {tag}", ok, f"exponent={p:.2f}  max|dP|={errs[-1]:.1e}  (expect {expect})")

# T5 (c): split under different conventions, in units of Gamma/delta (delta = 1)
print("\nT5 (c) X0 weight under conventions; dW/W0 divided by Gamma/delta:")
print("   g      Gamma    Z      C1:Z|rho~|^2   window L=delta   window L=delta/4   time-pole Z^2|rho~|^2   asymptotic")
for g in gs:
    Et, Z, Gm, rt2, W0nu, _ = C1_pieces(g, lam); Gt = Gm.sum(); W0 = Z*rt2
    win = lambda L: exact_int(lambda w: (abs(w - Et) < L)*1.0, g, lam, Et=Et, Gt=Gt, extra=(Et - L, Et + L))/(2*np.pi)
    vals = [win(1.0), win(0.25), Z**2*rt2, 0.0]
    print(f"  {g:.2f}  {Gt:.2e}  {Z:.4f}  {W0:.4f}       " + "   ".join(f"{(v - W0)/W0/Gt:+8.3f}" for v in vals))
bound = lambda L: 5/(2*np.pi) + 1/(np.pi*L)
print(f"   explicit bound |dW|/(W0 Gamma/delta) <= 5/(2pi) + delta/(pi L): L=delta {bound(1.0):.2f}, L=delta/4 {bound(0.25):.2f}")
