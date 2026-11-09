"""Rejected Lagrange run: where does P < 0 sit?  (DC-67 solver as the object under test.)  GaAs V1 F by mixture.  K3 per material; pool bookkeeping."""
import numpy as np, sys, csv, json, collections
sys.path.insert(0,'../DC-67')
import casc2
A=5.587791442871094; n=np.arange(32)
def L3(ks,v):
    return [np.prod([(v-b)/(a-b) for b in ks if b!=a]) for a in ks]
Eg,om=4.645,.089; lam=A/Eg**3; w=om/Eg; N=104; W=1.0
Ps=[]
for k in (1,2,3):
    x,G=casc2.solve_gf(lam,k/N,25.,N,32,W=W); Ps.append((casc2.pmf(G[0]),casc2.pmf(G[1])))
L=L3([1,2,3],w*N)
Pe=sum(l*p[0] for l,p in zip(L,Ps)); Ph=sum(l*p[1] for l,p in zip(L,Ps))
print('TeO2 Wv Lagrange: min Pe %.3e; min Ph x<=W %.3e; min Ph x>W %.3e at x=%.3f'%(Pe.min(),Ph[x<=W].min(),Ph[x>W].min(),x[x>W][Ph[x>W].min(1).argmin()]))
D='../DC-67/data/'
S={(r['material'],r['cfg']):r for r in csv.DictReader(open(D+'library_summary.csv'))}
# rejected csv min over Pe only unknown; GaAs V1
r=S[('GaAs','V1')]; N=int(r['N']); lam=float(r['lam']); w=float(r['w']); c=int(round(w*N)); ks=[c-1,c,c+1] if c>=2 else [1,2,3]
Pk=[]
for k in ks:
    x,G=casc2.solve_gf(lam,k/N,25.,N,32,theta=1.5); Pk.append(casc2.pmf(G[0]))
L=L3(ks,w*N); Pm=sum(l*p for l,p in zip(L,Pk)); i=x>=12.5
sl=lambda y:np.polyfit(1+x[i],y[i],1)[0]
m=[p@n for p in Pk]; v=[p@(n*n)-(p@n)**2 for p in Pk]
mL=sum(l*a for l,a in zip(L,m)); vL=sum(l*a for l,a in zip(L,v)); vP=Pm@(n*n)-(Pm@n)**2
print('GaAs V1 N',N,'nodes',ks,'wN',w*N,'L',L,'F(var interp) %.6f F(P interp) %.6f rel %.2e; library F %s'%(sl(vL)/sl(mL),sl(vP)/sl(mL),(sl(vP)/sl(vL)-1),r['F']))
# K3 per pair and Gaussian coefficient
print('mat F K3/N C_pred(=0.0917 K3/F^2 * eps/Eg) at table')
out={}
for mat in sorted({k[0] for k in S}):
    d=np.load(D+'lib/'+mat+'.npz'); xs=d['x_m1']; P=d['Pe_m1']; nn=np.arange(P.shape[1]); m1=P@nn; c=nn[None,:]-m1[:,None]; k3=(P*c**3).sum(1)
    s=xs>=xs[-1]/2; sm=np.polyfit(xs[s],m1[s],1)[0]; K3=np.polyfit(xs[s],k3[s],1)[0]/sm; F=float(S[(mat,'m1')]['F'])
    out[mat]=dict(K3=K3,F=F,C=.0917*abs(K3)/F**2/sm)
print({k:(round(v['K3'],4),round(v['F'],3),round(v['C'],3)) for k,v in out.items()})
Cs=[v['C'] for v in out.values()]; print('C range',min(Cs),max(Cs),np.median(Cs))
json.dump(out,open('data/K3.json','w'),indent=1)
rows=list(csv.DictReader(open('../../returns/R16/WP8-U-table-v4.csv')))
mats=collections.OrderedDict()
for r in rows: mats.setdefault(r['material'],[]).append(r)
pool=[m for m,v in mats.items() if v[0]['verdict'].startswith('SURVIVOR')]
print(len(pool),collections.Counter(v[0]['verdict'] for v in mats.values()))
lib={'SiC-3C':'3C-SiC','SiC-4H':'4H-SiC','SiC-6H':'6H-SiC'}
L=sorted({k[0] for k in S}); miss=[m for m in pool if lib.get(m,m) not in L]; print(len(miss),miss); print('lib not in pool',[m for m in L if m not in [lib.get(p,p) for p in pool]])
for m in miss:
    print(m,mats[m][0]['verdict'],[(r['property'],r['value'][:9],r['tag']) for r in mats[m] if r['property'].startswith(('E_g','omega_O_max','omega_Gamma','omega_T_max','omega_TO_LO','GAP:E_g'))][:7])
