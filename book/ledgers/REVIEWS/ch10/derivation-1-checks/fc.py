import numpy as np,sys
sys.path.insert(0,'/home/user/dmdd-solid/book/figscripts/ch10')
from si_fcrys import load, DQ, DE, OMEGA, ALPHA, ME
q,E,f2=load(); q0=ALPHA*ME
OS=4*np.pi*ALPHA*ME**2*f2/q[:,None]**3   # Omega*Sbar
ne=8 # per cell -> n_e Omega
def at(x): return np.argmin(abs(q-x*q0))
for x in [0.3,0.5,0.7,1.0,1.5,2.0]:
    i=at(x); m1=np.sum(E*OS[i])*DE; print('fsum',x, round(m1/(np.pi*ne*q[i]**2/ME),3))
# energy-integrated form factor scaling
F=f2.sum(1)*DE
def slope(a,b):
    m=(q>a*q0)&(q<b*q0); return np.polyfit(np.log(q[m]),np.log(F[m]),1)[0]
print('slope 0.3-0.75',slope(0.3,0.75),' slope 2-4',slope(2,4))
for w in [3,5,10]:
    j=np.argmin(abs(E-w)); col=np.convolve(f2[:,j],np.ones(5)/5,'same')
    ip=np.argmax(col); print('w',w,'peak at',round(q[ip]/q0,2),' f(2q0)/f(q0)',round(col[at(2)]/col[at(1)],2),' f(3q0)/f(q0)',round(col[at(3)]/col[at(1)],2),' f(3)/peak',round(col[at(3)]/col[ip],2), 'qS peak', round(q[np.argmax(np.convolve(OS[:,j]*q,np.ones(5)/5,'same'))]/q0,2))
print('--- windowed')
for lo,hi in [(0.3,0.5),(0.5,0.7),(0.9,1.1),(1.4,1.6),(1.9,2.1)]:
    s=(q>=lo*q0)&(q<hi*q0); m1=np.sum(OS[s]*E[None,:],1)*DE; print(lo,hi,round(np.mean(m1/(np.pi*8*q[s]**2/ME)),3), 'nonempty mean', round(np.mean((m1/(np.pi*8*q[s]**2/ME))[m1>0]),3))
nm=5; n=len(q)//nm; qm=q[:n*nm].reshape(n,nm).mean(1); fm=f2[:n*nm].reshape(n,nm,-1).mean(1); Om=OS[:n*nm].reshape(n,nm,-1).mean(1)
for w in [3,5,10]:
    j=(E>=w-0.25)&(E<w+0.25); fw=fm[:,j].mean(1); sw=Om[:,j].mean(1)
    print(w,'peak',round(qm[np.argmax(fw)]/q0,2),'r2',round(np.interp(2*q0,qm,fw)/np.interp(q0,qm,fw),2),'r3',round(np.interp(3*q0,qm,fw)/np.interp(q0,qm,fw),2),'r3/r2',round(np.interp(3*q0,qm,fw)/np.interp(2*q0,qm,fw),2),'qS',round(qm[np.argmax(qm*sw)]/q0,2))
F=fm.sum(1)*DE
for a,b in [(0.3,0.75),(2,4)]:
    s=(qm>a*q0)&(qm<b*q0)&(F>0); print('slope',a,b,np.polyfit(np.log(qm[s]),np.log(F[s]),1)[0])
