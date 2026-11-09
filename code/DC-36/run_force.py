"""DC-36 production: first-harmonic a1 per body and Delta a vs u = v_c,Ti, SUEP and SUREF, both signs of V."""
import numpy as np, micro as M, sys, os, json, time
os.makedirs('results',exist_ok=True)
us=[30,60,100,150,200,300,400,500,600,800,1000,1500,2500]
out={}
for geom,gn in ((M.SUEP,'SUEP'),(M.SUREF,'SUREF')):
    for sign in (+1,-1):
        if gn=='SUREF' and sign==-1: continue
        rows=[]
        for u in us:
            t=time.time(); a1,e1,th,a=M.harmonic(geom,float(u),sign=sign,N=1500000,nth=4,seed=u)
            d=a1[1]-a1[0]; ed=np.hypot(e1[0],e1[1])
            rows.append([u,a1[0],e1[0],a1[1],e1[1],d,ed]); print(gn,sign,' '.join('%.4g'%x for x in rows[-1]),'%.0fs'%(time.time()-t),flush=True)
        np.savetxt(f'results/force_{gn}_{"rep" if sign>0 else "att"}.csv',rows,delimiter=',',header='u=v_c,Ti[km/s],a1_inner,err,a1_outer,err,Delta_a(outer-inner),err  [m/s^2], rho=0.3 GeV/cm3')
