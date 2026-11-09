import sys,numpy as np
sys.path.insert(0,'/home/user/dmdd-solid/book/figscripts/ch12')
import mig12 as G
R=G.R; ALPHA,ME,M=G.ALPHA,G.ME,G.M
OM,QT,LF=G.OM,G.QT,G.LF
sel=OM>=G.EG
aev=5.431/1973.27; nat=8/aev**3; e2=4*np.pi*ALPHA
Qd=G.qmig('lf')
def Lq(q):  # loss function at |q| (held at first bin below)
    return np.array([np.interp(q,QT,LF[i]) for i in range(len(OM))])  # (nom, nq)
def rates(m, qc_list, wmin=G.EG):
    qmax=2*m*R.VMAX
    q=np.linspace(1.0,qmax,3000)
    Lqq=Lq(q)
    out={}
    tot_d=0; parts={qc:0 for qc in qc_list}; id_parts={qc:0 for qc in qc_list}
    for i,w in enumerate(OM):
        if w<wmin: continue
        vmin=w/q+q/(2*m)
        ker=q*R.eta(vmin)
        dd=ker*4*ALPHA*q**2/M**2*Qd[i]
        di=ker*(ME/M)**2*(2*q**2/e2)*Lqq[i]/(2*np.pi*nat)
        tot_d+=np.trapezoid(dd,q)*1
        for qc in qc_list:
            mm=q<qc
            parts[qc]+=np.trapezoid(dd*mm,q); id_parts[qc]+=np.trapezoid(di*mm,q)
    return tot_d,parts,id_parts
qcs=[750.,1000.,2250.]
print(' m(MeV)  f(q<0.75)  f(q<1)  f(q<qBZ)   R_lo/R_diag(identity<0.75) (<1 keV) (<qBZ)')
for m in [0.36,0.42,0.5,0.7,1,2,3,6.3,10,30]:
    t,p,ip=rates(m*1e6,qcs)
    if t==0: print(m,'no rate'); continue
    print(f'{m:6.2f}  {p[750.]/t:8.3f} {p[1000.]/t:8.3f} {p[2250.]/t:8.3f}   {(t-p[750.]+ip[750.])/t:8.3f}  {(t-p[1000.]+ip[1000.])/t:8.3f}  {(t-p[2250.]+ip[2250.])/t:8.3f}')
