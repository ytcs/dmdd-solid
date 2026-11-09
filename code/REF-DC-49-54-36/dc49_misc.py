import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'../DC-49')
import numpy as np, dirac as d, svgtools as t, collections
# digitisation check: Summary_scattering, ZrTe5 th solid blue, ticks read here
ps=t.load('/tmp/claude-1000/-home-ytc-Projects-breakthrough-maths/42e1e9d0-2a1c-462d-8f88-358ed2914b1d/scratchpad/f/Summary_scattering.svg')
xs=sorted(set(round(p['pts'][0,0],2) for p in ps if len(p['pts'])==2 and abs(p['pts'][0,0]-p['pts'][1,0])<1e-3 and 4<abs(p['pts'][0,1]-p['pts'][1,1])<7))
ys=sorted(set(round(p['pts'][0,1],2) for p in ps if len(p['pts'])==2 and abs(p['pts'][0,1]-p['pts'][1,1])<1e-3 and 4<abs(p['pts'][0,0]-p['pts'][1,0])<7))
print('major x',xs,'major y',ys)
q=[p for p in ps if p['stroke'] and '36.839294' in p['stroke'] and p['dash'] is None and len(p['pts'])>15][0]['pts']
dx=(xs[-1]-xs[-2]) if len(xs)>1 else 110.1
x=10**(3-(xs[-1]-q[:,0])/dx); y=10**(-36-(q[:,1]-ys[0])/(ys[1]-ys[0]))
a=np.loadtxt('../DC-49/data/pub_scat_ZrTe5_th.csv',delimiter=','); a=a[np.argsort(a[:,0])]; o=np.argsort(x); 
m=np.array([20,30,60,100,300,1000.]); print('calc-from-my-ticks/DC csv at m:',np.round(np.exp(np.interp(np.log(m),np.log(x[o]),np.log(y[o])))/np.exp(np.interp(np.log(m),np.log(a[:,0]),np.log(a[:,1]))),4))
# Dirac contribution to the static background: v^2 Re P(q->0)
for n,o in (('Yb',dict(g=12)),('ZrTe5_th',{})):
    p=d.setup(n,**o); B=d.Bfun(np.array([1e-8]),p['D'],p['Lt'])
    print(n,'C v_i^2 Re B at s->0 for each axis:',np.round(p['C']*p['v']**2*B.real[0],2),' kappa',p['kap'])
