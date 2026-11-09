"""DC-54: converged integration of 2401.11971 Eq. (6) with Eq. (5), the URF density row and the transverse row.
For every (omega, T) the Q integral runs over the exact kinematic range [|p-p'|, p+p'] with nodes clustered at the lower edge,
so the pole 1/(Q^2-omega^2)^2 of Eq. (5) is resolved. Q window optional. Output per row: dR/domega, plus T_max and Q profiles."""
import numpy as np, rate as R, crdm, epsT, sys, json, os
from numpy.polynomial.legendre import leggauss
XQ,WQ=leggauss(160)
def spectrum(elf,m,T,dP,med,ws,Qhi=None,Qlo=0.,ET=None,sig=1e-34,cumT=False):
    mu=m*R.ME/(m+R.ME); pref=sig*R.CM**2/(R.rhoT(elf.rho)*2*np.pi*R.E2*mu**2)*R.KG*R.YR/R.CM**2/R.SEC
    Qcap=elf.k[-1] if Qhi is None else Qhi
    wT=np.gradient(np.log(T))*T
    rows=['src','den','tr','trc','Lonly']; out={r:np.zeros(len(ws)) for r in rows}; cum=np.zeros((len(ws),len(T)))
    for iw,w in enumerate(ws):
        E=T+m; ok=E-w>m; Ti=np.where(ok)[0]
        if len(Ti)==0: continue
        p=np.sqrt(E[Ti]**2-m*m); pp=np.sqrt((E[Ti]-w)**2-m*m); q1=np.maximum(np.abs(p-pp),Qlo); q2=np.minimum(p+pp,Qcap)
        g=q2>q1; Ti=Ti[g]; p=p[g]; pp=pp[g]; q1=q1[g]; q2=q2[g]
        if len(Ti)==0: continue
        # Q = q1 + (q2-q1) * exp(-s) style clustering: log-uniform in (Q-q1)
        # stable Q^2-w^2 = c0 + 2 q1 d + d^2 at the kinematic edge: (p-p')^2-w^2 = 2X, X = m^2 w^2/(E E' + p p' - m^2)
        EE=E[Ti]*(E[Ti]-w)+p*pp-m*m; X=m*m*w*w/EE
        edge=q1<=np.abs(p-pp)*(1+1e-12)
        c0=np.where(edge,2*X,q1*q1-w*w)
        d0=np.maximum(1e-3*np.abs(c0)/(2*q1),1e-30)
        lo=np.log(d0); hi=np.log(q2-q1)
        l=.5*(hi-lo)[:,None]*XQ[None,:]+.5*(hi+lo)[:,None]; dQ=np.exp(l); Q=q1[:,None]+dQ; wq=.5*(hi-lo)[:,None]*WQ[None,:]*dQ
        Em=E[Ti][:,None]
        q2m=c0[:,None]+2*q1[:,None]*dQ+dQ**2
        F2=(R.Q0**2/q2m)**2 if med=='light' else np.ones_like(Q)
        K=((2*Em-w)**2-Q**2)/(4*p[:,None]**2)
        Lv=elf.L(w,Q)
        fac=(dP[Ti]*wT[Ti])[:,None]
        src=fac*wq*Q**3*F2*K*Lv
        pref2=(q2m/Q**2)**2
        den=src*pref2
        out['src'][iw]=src.sum(); out['den'][iw]=den.sum()
        cum[iw,Ti]=src.sum(1)
        if ET is not None:
            pl=(p[:,None]**2-pp[:,None]**2+Q**2)/(2*Q); pT2=np.maximum(p[:,None]**2-pl**2,0)
            KT=(4*pT2+2*(Q**2-w*w))/(4*p[:,None]**2)
            vv=(p/E[Ti])[:,None]**2
            KC=K*np.maximum(vv-w*w/Q**2,0)
            eT=ET(w,Q); LT=np.imag(-Q**2/(w*w*eT-Q**2))
            base=fac*wq*Q**3*F2*pref2*LT
            out['tr'][iw]=den.sum()+(base*KT).sum(); out['trc'][iw]=den.sum()+(base*KC).sum()
    r={k:v*pref for k,v in out.items()}
    return r,cum*pref
def PZ():
    a=np.loadtxt('/home/ytc/paer-work/lit/dc54/aux/2004.10709/tex/Supplementary/p100K.dat'); return a[:,0],a[:,1:]
def Zrates(ws,y):
    E,p=PZ(); o={}
    for Z in (3,4,5,6):
        pz=np.interp(ws,E,p[:,Z-1],left=0,right=0); o[Z]=np.trapezoid(pz*y,ws)
    return o
EXPO={3:57.71,4:63.03,5:65.56,6:67.73}
def events(Zr): return {Z:Zr[Z]*EXPO[Z]*1e-3/365.25 for Z in Zr}
if __name__=='__main__':
    os.makedirs('results',exist_ok=True)
    elf=R.ELF('Si/Si_gpaw_withLFE.dat',2.33); ge=R.ELF('Ge/Ge_gpaw_withLFE.dat',5.32)
    ETs=epsT.EpsT(elf,16.6); ETg=epsT.EpsT(ge,16.)
    ws=np.r_[np.arange(2,10,1.),np.arange(10,24,.75),np.arange(24,50.1,2.)]
    res={}
    for lab,m in (('1keV',1e3),('10keV',1e4),('me',R.ME)):
        for med in ('light','heavy'):
            T,dP=R.flux_grid(lab,med,n=420)
            for tgt,e,et in (('Si',elf,ETs),('Ge',ge,ETg)):
                for win,kw in (('full',{}),('Q<=5keV',dict(Qhi=5e3)),('Q>=493eV,<=5keV',dict(Qlo=493.,Qhi=5e3))):
                    r,cum=spectrum(e,m,T,dP,med,ws,ET=et,**kw)
                    I={k:float(np.trapezoid(v,ws)) for k,v in r.items()}
                    key=f'{tgt}|{lab}|{med}|{win}'
                    res[key]=dict(I=I,ratio_den=I['den']/I['src'] if I['src'] else None,ratio_tr=I['tr']/I['den'] if I['den'] else None,ratio_trc=I['trc']/I['den'] if I['den'] else None)
                    if tgt=='Si':
                        z={k:Zrates(ws,v) for k,v in r.items() if k in('src','den','tr','trc')}; res[key]['Z']={k:{str(a):float(b) for a,b in v.items()} for k,v in z.items()}
                    if win=='full':
                        c=np.trapezoid(cum,ws,axis=0); cc=np.cumsum(c); res[key]['src_T']=[(float(T[i]),float(cc[i]/cc[-1])) for i in range(0,len(T),40)]
                    print(key,'src %.4g den %.4g tr %.4g trc %.4g | den/src %.4g tr/den %.4f trc/den %.4f'%(I['src'],I['den'],I['tr'],I['trc'],res[key]['ratio_den'] or 0,res[key]['ratio_tr'] or 0,res[key]['ratio_trc'] or 0),flush=True)
                    json.dump(res,open('results/recast.json','w'),indent=0)
