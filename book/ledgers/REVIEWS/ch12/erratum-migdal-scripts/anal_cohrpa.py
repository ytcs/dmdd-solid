import numpy as np, sys, glob
f=sys.argv[1]
d=np.load(f); Q=d['Q']; wq=d['wq']; coh=d['coh']; w=d['w']
ALPHA=1/137.035999; ME=510998.95; HBARC=1973.269804
Om=(5.43**3/4)/HBARC**3
sel=w>=1.11
def tot(y): return np.trapezoid(y[...,sel]/w[sel]**4, w[sel], axis=-1)
Ti=tot(d['inc_i']); Tii=tot(d['inc_ii'])
Tc=tot(coh)
print('incoherent full/diag (i)/(ii) =',Ti/Tii)
def med(y):
    c=np.cumsum(y[sel]/w[sel]**4); c/=c[-1]; return np.interp(.5,c,w[sel])
print('median w diag %.2f'%med(d['inc_ii']))
edges=np.array([0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.8,3.2,3.6,4.0,4.5,5,6,7,8,9.5])*1e3
print(' Q bin (keV)    n   coh/diag(ii)  coh/full(i)   median_w_coh')
for lo,hi in zip(edges[:-1],edges[1:]):
    m=(Q>=lo)&(Q<hi)
    if m.sum()==0: continue
    W=wq[m]; c=(W*Tc[m]).sum()/W.sum()
    ys=(W[:,None]*coh[m]).sum(0)
    print(f'{lo/1e3:4.1f}-{hi/1e3:4.1f} {m.sum():4d}  {c/Tii:9.3f}  {c/Ti:9.3f}   {med(ys):6.2f}')
# identity check using head files
for h in sorted(glob.glob('cohrpa_head_*.npy'))[:1]:
    a=np.load(h); k=a[0]; Sp00=a[1:]
    # P_id per Q^2 * M^2: m_e^2*(2/e2)*Sp00/(2 pi n_at); P_coh per Q^2 M^2: 4 alpha*Lcoh/(3w^4), Lcoh = coh/Om
    e2=4*np.pi*ALPHA; nat=2/Om
    Pid=ME**2*(2/e2)*Sp00/(2*np.pi*nat)
    m=(np.abs(Q-k)<1)
    Pc=4*ALPHA*(coh[m][0]/Om)/(3*w**4)
    print('identity check at |Q|=%.0f eV: int P_coh / int P_id ='%k, np.trapezoid(Pc[sel],w[sel])/np.trapezoid(Pid[sel],w[sel]))
    Pd=4*ALPHA*(d['inc_ii']/Om)/(3*w**4)
    print('   model diag/identity =', np.trapezoid(Pd[sel],w[sel])/np.trapezoid(Pid[sel],w[sel]))
