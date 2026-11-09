"""Claim 5: library tables against the referee's solver at N_ref = r N_lib (library rows lie on the reference grid), all x, not only multiples of 0.25.  Rows: configs from argv (default m1 V1 V3 Wv).
node error: at stored rows;  read error: reader's linear x interpolation at off-row x;  electron and (where it differs) hole.  Output data/acc_all.csv"""
import numpy as np, csv, sys, time, os
import ref_casc as R
D='../DC-67/data/'
S=list(csv.DictReader(open(D+'library_summary.csv')))
cfgs=sys.argv[1].split(',') if len(sys.argv)>1 else ['m1']
NREF=int(sys.argv[2]) if len(sys.argv)>2 else 1500
XMAX=float(sys.argv[3]) if len(sys.argv)>3 else 25.0
fn=sys.argv[4] if len(sys.argv)>4 else 'data/acc_all.csv'
done=set()
if os.path.exists(fn):
    done={(r['material'],r['cfg']) for r in csv.DictReader(open(fn))}
else:
    csv.writer(open(fn,'w',newline='')).writerow('material cfg N Nref a_ph node_e_max node_e_x node_e_med node_h_max node_h_x tot_e_max tot_e_x tot_e_above5 t_s'.split())
for r in sorted(S,key=lambda r:int(r['N'])):
    if r['cfg'] not in cfgs or (r['material'],r['cfg']) in done: continue
    t0=time.time(); m=r['material']; c=r['cfg']; N=int(r['N']); lam=float(r['lam']); w=float(r['w']); th=float(r['theta']); a=float(r['a'])
    W=None if r['W']=='' else float(r['W']); X=min(float(r['X']),XMAX); Nz=int(r['Nz'])
    k=max(2,int(np.ceil(NREF/N)));
    while w*N*k<3: k+=1
    k=2*(k//2+k%2)                     # even: half-way points exist
    d=np.load(D+'lib/'+m+'.npz'); xt=d['x_'+c]; Pe=d['Pe_'+c]; Ph=d['Ph_'+c] if 'Ph_'+c in d.files else None
    x,(Qe,Qh),s=R.gf(lam,w,X,N*k,Nz,a=a,W=W,theta=th)
    nc=min(Pe.shape[1],Nz)
    # table rows on the reference grid
    sel=xt<=X-1e-9; ii=np.round(xt[sel]*N*k).astype(int)
    assert np.abs(x[ii]-xt[sel]).max()<1e-9
    De=np.abs(Pe[sel,:nc]-Qe[ii,:nc]).max(1)
    if Pe.shape[1]<Nz: De=np.maximum(De,Qe[ii,nc:].sum(1))
    je=De.argmax()
    dh=0;xh=0
    if Ph is not None:
        ok=x[ii]<=W-2.0/N
        Dh=np.abs(Ph[sel,:nc][ok]-Qh[ii[ok],:nc]).max(1); dh=Dh.max(); xh=x[ii[ok]][Dh.argmax()]
    # reader's linear interpolation at off-row x
    xs=np.arange(int(.2*N*k),len(x)-1,max(1,k//4))
    Pi=np.stack([np.interp(x[xs],xt,Pe[:,j]) for j in range(nc)],1)
    Dt=np.abs(Pi-Qe[xs,:nc]).max(1); jt=Dt.argmax()
    wN=w*N; a_ph=wN-np.floor(wN+1e-9)
    row=[m,c,N,N*k,round(a_ph,4),'%.3e'%De.max(),round(xt[sel][je],3),'%.3e'%np.median(De),'%.3e'%dh,round(xh,3),'%.3e'%Dt.max(),round(x[xs[jt]],3),'%.3e'%Dt[x[xs]>5.1].max(),round(time.time()-t0,1)]
    with open(fn,'a',newline='') as f: csv.writer(f).writerow(row)
    print(row,flush=True)
