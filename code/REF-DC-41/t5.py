import numpy as np, dirty as d, spec as S, core as c, time
print("clean limit Gam->0 vs closed form")
for y,Q in [(2.2,5.64),(3,7.69),(5,12.82),(1.5,3.0),(1.9,5.64),(4,1.5)]:
  for G in (1e-3,):
    t=time.time(); p,g,x=d.Pfull(y,Q,G)
    if y>2: pc,gc=S.Pup(y,Q)[:2]
    else: pc,gc=S.Pt(y,Q)[:2]
    print(y,Q,G,'P33',np.round(p,5),np.round(pc,5),'Pt',np.round(g,5),np.round(gc,5),'%.1fs'%(time.time()-t),'M32,M23',np.round(x['M'][3,2],4),np.round(x['M'][2,3],4),'M31',abs(x['M'][3,1]),flush=True)
