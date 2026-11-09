"""dR/domega of 2401.11971 Eq. (6)/(S.14) with density-row and transverse-row options. eV units inside."""
import numpy as np, crdm
from scipy.interpolate import RegularGridInterpolator as RGI
ALPHA=1/137.035999; E2=4*np.pi*ALPHA; Q0=ALPHA*510998.95; ME=510998.95
CM=5.067731e4; KG=5.609589e35; YR=3.15576e7*1.519267e15; SEC=1.519267e15
L='/home/ytc/paer-work/lit/dc54/darkelf/data/'
class ELF:
    """DarkELF grid: linear interpolation in (omega,k), eps1=1, eps2=0 outside the grid (as darkelf/epsilon.py)."""
    def __init__(s,fn,rho):
        a=np.loadtxt(L+fn,skiprows=1); w=np.unique(a[:,0]); k=np.unique(a[:,1])
        o=np.lexsort((a[:,1],a[:,0])); a=a[o]
        s.e1=a[:,2].reshape(len(w),len(k)); s.e2=a[:,3].reshape(len(w),len(k)); s.w=w; s.k=k; s.rho=rho
        s.i1=RGI((w,k),s.e1,bounds_error=False,fill_value=1.); s.i2=RGI((w,k),s.e2,bounds_error=False,fill_value=0.)
    def eps(s,w,k):
        pts=np.stack(np.broadcast_arrays(w,k),-1); return s.i1(pts)+1j*s.i2(pts)
    def L(s,w,k):
        e=s.eps(w,k); return np.imag(-1/e)
def rhoT(g): return g*1e-3*KG/CM**3
def kin(T,m,w,Q):
    """E, p, E', p', mask; T,Q broadcast"""
    E=T+m; p=np.sqrt(np.maximum(E*E-m*m,0)); Ep=E-w
    ok=Ep>m; pp=np.sqrt(np.maximum(Ep*Ep-m*m,0))
    return E,p,Ep,pp,ok&(np.abs(p-pp)<=Q)&(Q<=p+pp)
def spectrum(elf,m,Tg,dPhi,sig=1e-34,med='light',ws=None,mV=None,nQ=500,rows=('src','den','tr','trc'),epsT=None,eta=0.,Qmin=None):
    """Tg: T grid [eV]; dPhi: dPhi/dT [cm^-2 s^-1 eV^-1]. Returns dict row -> dR/domega [kg^-1 yr^-1 eV^-1] on ws.
    src: Eq.(5) kernel; den: x(1-w^2/Q^2)^2; tr: transverse row added to den with exact Dirac trace; trc: classical (v^2-w^2/Q^2)K form."""
    ws=np.arange(1.,51.) if ws is None else ws
    mu=m*ME/(m+ME); lT=np.log(Tg); 
    wT=np.gradient(lT)*Tg                # dT weights (trapezoid in log)
    pref=sig*CM**2/(rhoT(elf.rho)*2*np.pi*E2*mu**2)
    conv=KG*YR*(1/CM**2)/SEC             # Phi in cm^-2 s^-1 eV^-1 -> eV^2 . eV^... see return section 2
    res={r:np.zeros(len(ws)) for r in rows}; dec={}
    for iw,w in enumerate(ws):
        q0=(Qmin or 0.)
        Qg=np.unique(np.r_[np.geomspace(w*1.0000001,w*30,nQ//2),np.geomspace(w*30,elf.k[-1],nQ//2)])
        if q0: Qg=Qg[Qg>=q0]
        QQ=Qg[:,None]; TT=Tg[None,:]
        E,p,Ep,pp,ok=kin(TT,m,w,QQ)
        q2=QQ**2-w**2
        F2=(Q0**2/q2)**2 if med=='light' else (1+0*q2)
        K=np.where(ok,((2*E-w)**2-QQ**2)/(4*np.maximum(p,1e-30)**2),0.)   # = [(2E-w)^2-Q^2]/(4 v^2 E^2)
        A=np.sum(K*(dPhi*wT)[None,:],axis=1)                                # (Q,)
        Lq=elf.L(w,Qg); Qw=np.gradient(np.log(Qg))*Qg
        F2q=F2[:,0]
        base=Qw*Qg**3*F2q
        res['src'][iw]=np.sum(base*A*Lq)
        if 'den' in rows: res['den'][iw]=np.sum(base*(1-w**2/Qg**2)**2*A*Lq)
        if epsT is not None and 'tr' in rows:
            # exact transverse Dirac contraction: tr_T L = [4 p_T^2 + 2 (Q^2-w^2)]/(4 E E'), divided by the same 1/(E E') bookkeeping as K
            pl=(p**2-pp**2+QQ**2)/(2*QQ); pT2=np.maximum(p**2-pl**2,0)
            KT=np.where(ok,(4*pT2+2*(QQ**2-w**2))/(4*np.maximum(p,1e-30)**2),0.)
            AT=np.sum(KT*(dPhi*wT)[None,:],axis=1)
            KC=np.where(ok,K*(p**2/E**2-w**2/QQ**2),0.); AC=np.sum(KC*(dPhi*wT)[None,:],axis=1)
            eT=epsT(w,Qg)+1j*eta
            LT=np.imag(-Qg**2/(w**2*eT-Qg**2))
            res['tr'][iw]=res['den'][iw]+np.sum(base*(1-w**2/Qg**2)**2*AT*LT)
            res['trc'][iw]=res['den'][iw]+np.sum(base*(1-w**2/Qg**2)**2*AC*LT)
    return {r:res[r]*pref*conv for r in res},ws
def pub_flux(lab,med):
    a=np.loadtxt(f'data/pub_flux_{med}_{lab}.csv',delimiter=','); a=a[np.argsort(a[:,0])]
    a=a[a[:,1]>1.01e-12] if False else a
    return a
def flux_grid(lab,med,n=500):
    a=pub_flux(lab,med); T=np.geomspace(a[0,0],a[-1,0],n)
    y=np.exp(np.interp(np.log(T),np.log(a[:,0]),np.log(a[:,1])))     # T dPhi/dT in cm^-2 s^-1
    return T*1e9,y/(T*1e9)                                              # eV, per eV
if __name__=='__main__':
    elf=ELF('Si/Si_gpaw_withLFE.dat',2.33); eln=ELF('Si/Si_gpaw_noLFE.dat',2.33)
    pl=np.loadtxt('data/pub_dRdw_light.csv',delimiter=','); ph=np.loadtxt('data/pub_dRdw_heavy_x100.csv',delimiter=',')
    ws=pl[::1,0]; 
    for name,e in [('LFE',elf),('noLFE',eln)]:
        for med,pub,sc in [('light',pl,1),('heavy',ph,100)]:
            T,dP=flux_grid('1keV',med)
            r,_=spectrum(e,1e3,T,dP,med=med,ws=ws,rows=('src','den'))
            print(name,med,'pub int %.4g  calc src int %.4g  den %.4g'%(np.trapezoid(pub[:,1],ws),np.trapezoid(r['src']*sc,ws),np.trapezoid(r['den']*sc,ws)))
            idx=[6,10,13,15,18,22,28,35,45]
            print('  w',' '.join('%.1f'%ws[i] for i in idx)); print('  pub',' '.join('%.3g'%pub[i,1] for i in idx)); print('  src',' '.join('%.3g'%(r['src'][i]*sc) for i in idx)); print('  den',' '.join('%.3g'%(r['den'][i]*sc) for i in idx))
