"""Gaussian (library gaussian_match) vs the library's own last rows, every material, m1: what a user gets just past the table.  Also Si hole rows above W."""
import numpy as np, csv, json, sys
from scipy.stats import norm
D='../DC-67/data/'
S={ (r['material'],r['cfg']):r for r in csv.DictReader(open(D+'library_summary.csv'))}
mats=sorted({k[0] for k in S}); out={}
print('mat  N X lam x_end mean var  B(as) B(exact) point(exact) sigma_end')
for m in mats:
    d=np.load(D+'lib/'+m+'.npz'); r=S[(m,'m1')]; x=d['x_m1']; P=d['Pe_m1']; n=np.arange(P.shape[1])
    e=float(r['eps_over_Eg']);F=float(r['F']);b=float(r['b'])
    res=[]
    for i in range(len(x)-5,len(x)):
        p=P[i]; om=1+x[i]; mean=om/e+b; var=F*om/e; sd=np.sqrt(var)
        G=norm.cdf((n+1.5-mean)/sd)-norm.cdf((n+.5-mean)/sd)
        mu=p@n; v=p@(n*n)-mu**2
        G2=norm.cdf((n+.5-mu)/np.sqrt(v))-norm.cdf((n-.5-mu)/np.sqrt(v))
        G3=np.exp(-.5*(n-mu)**2/v)/np.sqrt(2*np.pi*v)
        res.append((abs(p-G).max(),abs(p-G2).max(),abs(p-G3).max(),mu,v))
    a=np.array(res).max(0); out[m]=dict(xend=float(x[-1]),B_as=a[0],B_ex=a[1],pt=a[2],var=res[-1][4],mean=res[-1][3])
    print(m,r['N'],r['X'],round(float(r['lam']),4),x[-1],'%.2f %.2f %.1e %.1e %.1e'%(res[-1][3],res[-1][4],a[0],a[1],a[2]))
print('worst B_as',max(o['B_as'] for o in out.values()),'median',np.median([o['B_as'] for o in out.values()]))
json.dump(out,open('data/lib_end.json','w'),indent=1)
d=np.load(D+'lib/Si.npz'); print([k for k in d.files][:30]); x=d['x_m1']; Ph=d['Ph_m1']; n=np.arange(Ph.shape[1])
W=12/1.164
for xx in (9,10,10.25,10.5,12,20,40):
    i=np.argmin(abs(x-xx)); print('Si hole row x',x[i],'mean',Ph[i]@n,'elec',d['Pe_m1'][i]@n, 'x>W' if x[i]>W else '')
# catalogue
cnt=sum(len([k for k in np.load(D+'lib/'+m+'.npz').files if k.startswith('x_')]) for m in mats); print('configs',cnt,'rows',len(S))
print('max Nbar+8sig',max(float(r['Nbar_X'])+8*float(r['sig_X']) for r in S.values()))
print('a(1-a) stats:')
aa=[]
for k,r in S.items():
    w=float(r['w']);N=int(r['N']);nf=int(np.floor(w*N+1e-9));a=w*N-nf; aa.append((a*(1-a),k[0],k[1],N,nf,round(a,4), round(w*N,4)))
aa.sort(reverse=True); print(aa[:10]); print('nf<=1:',sorted({(t[1],t[3],t[4],t[5]) for t in aa if t[4]<=1 and t[2]=='m1'}))
