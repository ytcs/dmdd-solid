"""WP0 symbolic/numeric identity checks (theory only; each check < 1 s).
Run: python3 -I checks.py   Prints PASS/FAIL per check with the residual."""
import numpy as np, sympy as sp
rng = np.random.default_rng(1)
def rep(name, res, tol=1e-9): print(f"{'PASS' if abs(res)<tol else 'FAIL'}  {name:62s} residual={res:.2e}")

# C1  Rank-one (species-basis) Coulomb resummation, eq (5.3)-(5.5)
K = 4                                   # species: e + 3 nuclear species
A = rng.normal(size=(K,K))+1j*rng.normal(size=(K,K)); Rt = A@A.conj().T*(-0.3)+0.1j*np.eye(K)  # proper response (complex)
z = np.array([-1.0, 2.0, 3.0, 1.0]); v = 0.7
R = np.linalg.solve(np.eye(K)-Rt@np.outer(z,z)*v, Rt)                 # full Dyson R = Rt + Rt V R
eps = 1 - v*z@Rt@z
R_sm = Rt + v*np.outer(Rt@z, z@Rt)/eps                                  # Sherman-Morrison form
rep("C1a Dyson == Sherman-Morrison (5.5)", np.abs(R-R_sm).max())
rep("C1b charge channel z.R.z == (1/eps - 1)/v  (ELF form)", abs(z@R@z-(1/eps-1)/v))
# clamped nuclei: proper e-N and N-N blocks vanish -> electron channel is the ELF
Rt2 = np.zeros((K,K),complex); Rt2[0,0] = -0.4+0.05j
R2 = np.linalg.solve(np.eye(K)-Rt2@np.outer(z,z)*v, Rt2); e2 = 1-v*Rt2[0,0]
rep("C1c clamped nuclei: R_ee == (1/eps_e - 1)/v", abs(R2[0,0]-(1/e2-1)/v))

# C2  Local-field version (G-space), eq (5.6)
nG = 5; vG = rng.uniform(0.2,1.0,nG)
def blk(): B = rng.normal(size=(nG,nG))+1j*rng.normal(size=(nG,nG)); return B
Rcc = blk(); Rac = blk(); Rcb = blk(); Rab = blk()
epsM = np.eye(nG)-np.diag(vG)@Rcc
full = Rab + Rac@np.linalg.inv(epsM)@np.diag(vG)@Rcb
# compare with explicit Dyson on the (a,c) super-space for charge operator
big = np.block([[Rab, Rac],[Rcb, Rcc]])                 # rows/cols: (a-block, c-block)
Vbig = np.zeros((2*nG,2*nG),complex); Vbig[nG:,nG:] = np.diag(vG)
Rbig = np.linalg.solve(np.eye(2*nG)-big@Vbig, big)
rep("C2  LFE screened formula (5.6) == super-space Dyson", np.abs(Rbig[:nG,:nG]-full).max())

# C3  FDT ordering and sign on a random finite system, eq (4.1)-(4.2)
n = 6; H = rng.normal(size=(n,n)); H = H+H.T; E,U = np.linalg.eigh(H); beta = 0.8
p = np.exp(-beta*E); p/=p.sum()
Oa = U.T@(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))@U; Ob = U.T@(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))@U
eta = 1e-3; w = 0.37
def chi(A,B,w):   # chi_{A,B}(w) = sum (p_i-p_f) A_if B_fi/(w-(E_f-E_i)+i eta)
    return sum((p[i]-p[f])*A[i,f]*B[f,i]/(w-(E[f]-E[i])+1j*eta) for i in range(n) for f in range(n))
def S(Ap,B,w):     # (2pi) sum p_i A_if B_fi delta_eta
    return sum(2*np.pi*p[i]*Ap[i,f]*B[f,i]*(eta/np.pi)/((w-E[f]+E[i])**2+eta**2) for i in range(n) for f in range(n))
# exact at finite eta: i(chi_ab - chi_ba^*) = 2pi sum (p_i - p_f) A_if B_fi delta_eta ; with p_f = p_i e^{-beta w_fi} on shell
cab = chi(Oa.conj().T, Ob, w); cba = chi(Ob.conj().T, Oa, w); Ap = Oa.conj().T
spec = sum(2*np.pi*(p[i]-p[f])*Ap[i,f]*Ob[f,i]*(eta/np.pi)/((w-E[f]+E[i])**2+eta**2) for i in range(n) for f in range(n))
rep("C3  i(chi_ab - chi_ba^*) == (1-e^{-beta w}) S_ab  (spectral form)", abs(1j*(cab-np.conj(cba)) - spec), 1e-9)
M = np.array([[S(X.conj().T,Y,w) for Y in (Oa,Ob)] for X in (Oa,Ob)])
rep("C3b S matrix Hermitian PSD (min eigenvalue >= 0 -> res=0)", max(0,-np.linalg.eigvalsh((M+M.conj().T)/2).min()) + np.abs(M-M.conj().T).max(), 1e-9)

# C4  Double-commutator f-sum and mixed third moment (1 electron x, 1 nucleus X; 1D)
x,X,q,m,Mn = sp.symbols('x X q m M', real=True, positive=True); f = sp.Function('f')(x,X); Vf = sp.Function('V')(x-X)
def Hop(g): return -sp.diff(g,x,2)/(2*m) - sp.diff(g,X,2)/(2*Mn) + Vf*g
ne  = lambda g: sp.exp(sp.I*q*x)*g; neD = lambda g: sp.exp(-sp.I*q*x)*g
nN  = lambda g: sp.exp(sp.I*q*X)*g; nND = lambda g: sp.exp(-sp.I*q*X)*g
comm = lambda A,B: (lambda g: A(B(g)) - B(A(g)))
dc_ee = comm(neD, comm(Hop, ne))(f); rep("C4a [n_e^+,[H,n_e]] f == (q^2/m) f", float(sp.simplify(dc_ee - q**2/m*f) != 0))
dc_eN = comm(neD, comm(Hop, nN))(f); rep("C4b mixed [n_e^+,[H,n_N]] == 0", float(sp.simplify(dc_eN) != 0))
dc_NN = comm(nND, comm(Hop, nN))(f); rep("C4c [n_N^+,[H,n_N]] f == (q^2/M) f", float(sp.simplify(dc_NN - q**2/Mn*f) != 0))
# third moment, mixed: [[n_e^+,H],[H,[H,n_N]]] acting on f -> multiplicative -(q^2/(m M)) e^{iq(X-x)} V''
A1 = comm(neD, Hop); B3 = comm(Hop, comm(Hop, nN))
m3 = sp.simplify(sp.expand(comm(A1, B3)(f)))
target = -(q**2/(m*Mn))*sp.exp(sp.I*q*(X-x))*sp.diff(sp.Function('V')(sp.Symbol('s')),sp.Symbol('s'),2).subs(sp.Symbol('s'),x-X)*f
rep("C4d mixed 3rd moment == -(q^2/mM) e^{iq(X-x)} V''(x-X)  (4.9)", float(sp.simplify(m3-target) != 0))

# C5  Hoelder interpolation bound (L17, eq 9.6) on a 3-oscillator positive ELF model
w_ = np.linspace(1e-4, 200, 400001); dw = w_[1]-w_[0]
L = sum(a*g*w_/((w_**2-w0**2)**2+(g*w_)**2) for a,w0,g in [(30,12,3),(200,17,5),(50,60,30)])
Km1 = (L/w_).sum()*dw; Kp1 = (w_*L).sum()*dw
wp2 = Kp1/(np.pi/2); one_m_einv = Km1/(np.pi/2)
worst = max(((w_**nn)*L).sum()*dw - (np.pi/2)*wp2**((1+nn)/2)*one_m_einv**((1-nn)/2) for nn in np.linspace(-1,1,21))
rep("C5  K_n <= (pi/2) wp^{n+1}(1-1/eps0)^{(1-n)/2}, -1<=n<=1 (max excess<=0)", max(worst,0.0), 1e-6)

# C6  Dark-photon in-medium absorption algebra (L9b)
mm, e1, e2_ = sp.symbols('m e1 e2', positive=True); epsc = e1+sp.I*e2_; Pi = mm**2*(1-epsc)
G = -sp.im(sp.simplify(mm**2*Pi/(mm**2-Pi)))/mm
rep("C6  -Im[m^2 Pi/(m^2-Pi)]/m == m Im(-1/eps)", float(sp.simplify(G - mm*sp.im(-1/epsc)) != 0))

# C7  Three-channel (pair-momentum) RPA identity (5.12): sum|M~|^2 Im g = Im[chi_MM + chi_Mr v chi_rM/eps]
Np = 40; Dl = rng.uniform(1,3,Np); a = rng.normal(size=Np)+1j*rng.normal(size=Np); b = rng.normal(size=Np)+1j*rng.normal(size=Np)
vv = 0.9; ww = 2.1; et = 0.05; g = 1/(ww-Dl+1j*et)
cMM = np.sum(np.abs(a)**2*g); cMr = np.sum(np.conj(a)*b*g); crM = np.sum(np.conj(b)*a*g); crr = np.sum(np.abs(b)**2*g)
epsP = 1 - vv*crr
lhs = np.imag(cMM + cMr*vv*crM/epsP)
Mt = a + b*vv*crM/epsP
rhs = np.sum(np.abs(Mt)**2*np.imag(g))
rep("C7  final-state RPA: Im[chi_MM + chi_Mr v chi_rM/eps] == sum|M~|^2 Im g", abs(lhs-rhs), 1e-10)
# density-dominated limit M ∝ rho -> factor 1/|eps(q+Q)|^2
a2 = 0.3*b; cMM2 = np.sum(np.abs(a2)**2*g); cMr2 = np.sum(np.conj(a2)*b*g); crM2 = np.sum(np.conj(b)*a2*g)
rep("C7b M = c*rho  ->  Im chi_MM/|eps|^2", abs(np.imag(cMM2 + cMr2*vv*crM2/epsP) - np.imag(cMM2)/abs(epsP)**2), 1e-10)
