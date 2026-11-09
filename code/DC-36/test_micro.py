"""Checks: (1) transfer matrix vs closed R and <R>=2R/(1+R); (2) Born limit of (CW2.25) = homogeneous term of (B2.3.2) analytically;
(3) MC on a wide flat plate vs direct quadrature of (CW2.25); (4) momentum conservation per ray; (5) sigma_crit numbers of WP7-B2 section 3."""
import numpy as np, micro as M
# (1)
def tm(k,kp,L):
    # 2x2 transfer matrix vacuum|slab|vacuum
    P=lambda a,b:.5*np.array([[1+b/a,1-b/a],[1-b/a,1+b/a]],complex)
    Pr=np.diag([np.exp(-1j*kp*L),np.exp(1j*kp*L)])
    T=P(k,kp)@Pr@P(kp,k); return abs(T[1,0]/T[0,0])**2
k,kp=1.,.7; R=((k-kp)/(k+kp))**2
Ls=np.linspace(0,2*np.pi/(2*kp)*200,200001)[1:]
Rm=np.mean([tm(k,kp,L) for L in Ls[::40]]); print('1. <R_slab> TM %.8f vs 2R/(1+R) %.8f'%(Rm,2*R/(1+R)))
# (2) Born: R_slab -> 2 (mV/2k^2)^2 = 2 pi^2 b^2 n^2/k^4 from |int e^{iqr}|^2 (return section 3)
b,n,kk=1e-5,1.,1.; V=2*np.pi*b*n; kp=np.sqrt(kk**2-2*V); R=((kk-kp)/(kk+kp))**2; print('2. Born: 2R/(1+R)=%.6e  analytic 2pi^2b^2n^2/k^4=%.6e'%(2*R/(1+R),2*np.pi**2*b*b*n*n/kk**4))
# (3) plate: Ri small, Ro huge, thin; compare a(theta=0)
L=100.; Ro=1e4; g=[dict(name='plate',Ri=.001,Ro=Ro,L=L,M=1.,rho=4.42)]
rng=np.random.default_rng(3)
for u in (150.,300.,600.,1000.):
    m,s,nb,per,sp,c=M.trace(g,u*u,0.,4000000,rng)
    Rb=np.hypot(Ro,L/2)*1.001
    # direct: P_wall(+z) - P_wall(-z) in the same units; a = (A/M) rho <...>. v_z dist
    v=M.sample_v(4000000,0.,np.random.default_rng(9)); vz=v[:,2]; a=np.abs(vz)
    k=np.sqrt(np.maximum(a*a-u*u,0)); R=np.where(a>u,((a-k)/(a+k))**2,1.); Rs=2*R/(1+R)
    # flux on bottom face (vz>0) pushes +z: 2 vz^2 Rs ; top face (vz<0) pushes -z
    I=np.mean(np.sign(vz)*2*vz**2*Rs)
    A=np.pi*Ro**2*1e-6; ref=M.RHO_GEV*M.GEVCM3*A*I*1e6/1.
    print('3. u=%g MC a=%.5e +- %.1e, (CW2.25) a=%.5e, ratio %.4f bounces %.2f'%(u,m[0],s[0],ref,m[0]/ref,nb))
# (4)
rng=np.random.default_rng(1); N=200000
m,s,nb,per,sp,c=M.trace(M.SUEP,300.**2,.7,N,rng); print('4. per-ray momentum tally finite, mean bounces',nb)
# (5)
EV=1.; n0=2.69e24/(5.067731e4**3); mm=20.; vv=1e-3
sc=mm**4*vv**4/(4*np.pi*n0**2)/(5.067731e4)**2; print('5. sigma_crit(20 eV,1e-3)=%.3e cm^2 (WP7-B2: 1.2e-38)'%sc)
b=np.sqrt(4e-38*(5.067731e4)**2/(4*np.pi)); Vopt=2*np.pi*b*n0/mm; print('   V/E at 4e-38: %.3f (WP7-B2: 1.9)'%(Vopt/(.5*mm*vv**2)))
