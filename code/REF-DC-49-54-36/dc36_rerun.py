"""Referee: DC-36 ray tracer, UNCHANGED physics, corrected geometry. The '30.801/39.390...' entries of the metrology table are DIAMETERS:
M = rho pi (Ro^2-Ri^2) L and I_x = M (Ri^2+Ro^2)/2 of the same table fail by x4 with them as radii and hold with halves (see dc36_geom_check in the report).
Writes dc36_rerun_<geom>_<sign>.csv here only."""
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'../DC-36')
import numpy as np, micro as M, time, copy
def half(g):
    g=copy.deepcopy(g)
    for b in g: b['Ri']/=2; b['Ro']/=2
    return g
SUEP=half(M.SUEP); SUREF=half(M.SUREF)
us=[30,60,100,150,200,250,300,350,400,500,600,800,1000,1500]
if __name__=='__main__':
    for geom,gn,sign in ((SUEP,'SUEP',1),(SUEP,'SUEP',-1),(SUREF,'SUREF',1)):
        rows=[]
        for u in us:
            t=time.time(); a1,e1,_,_=M.harmonic(geom,float(u),sign=sign,N=800000,nth=4,seed=u+7)
            d=a1[1]-a1[0]; ed=np.hypot(e1[0],e1[1]); rows.append([u,a1[0],e1[0],a1[1],e1[1],d,ed]); print(gn,sign,' '.join('%.4g'%x for x in rows[-1]),'%.0fs'%(time.time()-t),flush=True)
            np.savetxt(f'dc36_rerun_{gn}_{"rep" if sign>0 else "att"}.csv',rows,delimiter=',',header='u,a_in,err,a_out,err,Da,err rho=0.3')
