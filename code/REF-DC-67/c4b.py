"""Claim 4 (P level, Lagrange comparison) and claim 5 (order at all x incl. threshold, with DC-67's casc2 as the object under test, referee solver as truth)."""
import numpy as np, sys, json
import ref_casc as R
sys.path.insert(0,'../DC-67')
import casc2
out={}
A=5.587791442871094
# P-level bias of the read at a ~ 1/2, same N, same quadrature
for lab,Eg,om,N,X,Wv in (('Si N83',1.164,.063,83,20,12.),('SiO2 N154',9.2,.149,154,12,None),('C N100',5.47,.163,84,12,None)):
    lam=A/Eg**3;w=om/Eg;W=None if Wv is None else Wv/Eg
    x,Pl,s=R.gf(lam,w,X,N,32,W=W,read='lin'); x,Pc,s2=R.gf(lam,w,X,N,32,W=W,read='cubic')
    d=np.abs(Pl[0]-Pc[0]).max(1); out['P_read_'+lab]=dict(a=s.fr,nf=s.nf,maxdP=float(d.max()),x=float(x[d.argmax()]),med=float(np.median(d[x>1.5])))
    print(lab,out['P_read_'+lab],flush=True)
# nf = 0, a ~ 1/2: DC-67 implicit branch vs truth; CsI-like
Eg,om=6.14,.01; lam=A/Eg**3; w=om/Eg
for N in (307,608):
    x,G=casc2.solve_gf(lam,w,12.,N,32,frac=True); P=casc2.pmf(G[0]); n=np.arange(32)
    xr,Q,s=R.gf(lam,w,12.,3*N if N==608 else 6*N,32)
    k=len(xr)//(len(x)-1) if False else (3 if N==608 else 6)
    Qs=Q[0][::k][:len(x)]
    m1=P@n;m2=Qs@n; v1=P@(n*n)-m1**2; v2=Qs@(n*n)-m2**2
    i=int(10*N); out[f'CsI_{N}']=dict(a=w*N%1,maxdP=float(np.abs(P-Qs).max()),x=float(x[np.abs(P-Qs).max(1).argmax()]),dm10=float(m1[i]/m2[i]-1),dv10=float(v1[i]/v2[i]-1)); print(N,out[f'CsI_{N}'],flush=True)
# Lagrange of P: raw moments are interpolated; central variance gets the mixture term
def lag(ks,wN):
    L=[]
    for i,a in enumerate(ks):
        l=1.
        for j,b in enumerate(ks):
            if i!=j:l*=(wN-b)/(a-b)
        L.append(l)
    return np.array(L)
for lab,Eg,om,N,ks,W,X,lam_ in (('Si N74',1.164,.063,74,[3,4,5],12/1.164,25,None),('TeO2 Wv N104',4.645,.089,104,[1,2,3],1.0,25,None),('TeO2 V0 N104',4.645,.089,104,[1,2,3],None,25,None)):
    lam=A/Eg**3;w=om/Eg;n=np.arange(32); wN=w*N;L=lag(ks,wN)
    Ps=[]; 
    for k in ks:
        x,Q,s=R.gf(lam,k/N,X,N,32,W=W,read='exact'); Ps.append(Q[0])
    Pm=sum(l*p for l,p in zip(L,Ps))
    ms=[p@n for p in Ps]; vs=[p@(n*n)-(p@n)**2 for p in Ps]
    mL=sum(l*m for l,m in zip(L,ms)); vL=sum(l*v for l,v in zip(L,vs)); vP=Pm@(n*n)-(Pm@n)**2
    mix=vP-vL
    i=x>=X/2
    F_v=np.polyfit(1+x[i],vL,1)[0]/np.polyfit(1+x[i],mL,1)[0] if False else None
    sl=lambda y:np.polyfit(1+x[i],y[i],1)[0]
    out['lag_'+lab]=dict(L=list(map(float,L)),Pmin=float(Pm.min()),mix_end=float(mix[-1]),var_end=float(vL[-1]),F_varinterp=sl(vL)/sl(mL),F_Pinterp=sl(vP)/sl(mL)); print(lab,out['lag_'+lab],flush=True)
# order of DC-67 solver vs truth, all rows, SiO2-q and Si
for mat,Eg,om,Wv,N0,X in (('SiO2-q',9.2,.149,None,62,6.),('Si',1.164,.063,12.,74,6.)):
    lam=A/Eg**3;w=om/Eg;W=None if Wv is None else Wv/Eg
    Nr=N0*32
    xr,Q,s=R.gf(lam,w,X,Nr,32,W=W); Qe=Q[0]
    prev=None; rec=[]
    for f in (1,2,4,8):
        N=N0*f; x,G=casc2.solve_gf(lam,w,X,N,32,W=W,frac=True); P=casc2.pmf(G[0]); k=32//f
        Qs=Qe[::k][:len(x)]; d=np.abs(P-Qs).max(1); rec.append((N,float(d.max()),float(x[d.argmax()]),float(d[x>=3].max()), float((P-Qs)[:,1:].sum(1)[np.argmin(abs(x-1.145))])))
        print(mat,rec[-1],flush=True)
    out['order_'+mat]=rec
json.dump(out,open('data/c4b.json','w'),indent=1,default=float)
