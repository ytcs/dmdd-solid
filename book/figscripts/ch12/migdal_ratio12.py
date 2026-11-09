# Small-q ratio of the diagonal Migdal form (eq:12.3-soft) to the eq:8.3-boostward limit, and spectral medians (from erratum-migdal-scripts/ratio_tab.py).
import sys,os,numpy as np
sys.path.insert(0,'/home/user/dmdd-solid/book/figscripts/ch12')
import mig12 as G
R=G.R
ALPHA,ME,M=G.ALPHA,G.ME,G.M
OM,QT,LF=G.OM,G.QT,G.LF
m=OM>=G.EG
# per-nucleus density: Si atoms
a=5.431e-8/ (G.HBARC if False else 1)
print('ME',ME,'HBARC',G.HBARC)
nat=8/( (5.431e-10/1.973269804e-7*1e9 )**3) # placeholder
# compute n_at in eV^3: a in eV^-1 = 5.431 A / (1973.27 eV A)
aev=5.431/1973.27
nat=8/aev**3
Pdiag_per_q2 = 4*ALPHA/(3*M**2)*np.trapezoid(G.qmig('lf')[m]*3/3,OM[m])  # dP = 4 alpha v^2 Q, v=q/M
# note qmig includes 1/(3 w^4) factor already, so P = 4 alpha v^2 int Q
Pdiag_per_q2 = 4*ALPHA/M**2*np.trapezoid(G.qmig('lf')[m],OM[m])
e2=4*np.pi*ALPHA
print('Pdiag per eV E_R',Pdiag_per_q2*2*M)
yd=G.qmig('lf'); cd=np.cumsum(np.r_[0,0.5*(yd[1:]+yd[:-1])*np.diff(OM)]); cd/=cd[-1]
for j,q in enumerate(QT[:12]):
    L=LF[:,j]
    Pex=(ME/M)**2*(2*q**2/e2)*np.trapezoid(L[m],OM[m])/(2*np.pi*nat)
    c=np.cumsum(np.r_[0,0.5*(L[1:]+L[:-1])*np.diff(OM)]*(OM>=G.EG)); c/=c[-1]
    print(f'q={q:6.0f} eV  Pdiag/Pexact={Pdiag_per_q2*q**2/Pex:6.2f}  median w exact={np.interp(0.5,c,OM):.1f}  nbin')
print('median diag',np.interp(0.5,(np.cumsum(np.r_[0,0.5*(yd[1:]+yd[:-1])*np.diff(OM)]*(OM>=G.EG))/np.trapezoid(yd[m],OM[m])),OM))
