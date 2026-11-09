"""CW1 (LE-24/25/26): (i) out-of-mirror-plane curvature of E_min at the G'=0 off-axis optimum (rotate q about the in-plane axis
perpendicular to q); (ii) (2bar00)-class edge: joint (q,k) minimum of m with the UNFOLDED electron k_v,x + q_x <= -1 (2pi/a), i.e. beyond X on the -x side
(reduced electron in the +x valley, G' = (2bar00)); (iii) mirror image k_v,x + q_x >= +1 (equivalent by inversion; consistency check).
usage: emin_extra.py emin_fast.json out.json"""
import numpy as np, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from wannier_si import bands, sc, kc, tpiba, nv
from scipy.optimize import minimize
vmax=794.5/299792.458; K=1/(3.7289*tpiba)
F=json.load(open(sys.argv[1])); q0=np.array(F['q_vec_2pi_a']); k0=np.array(F['k_v'])
pairE=lambda k,q: bands((k+q)[None])[0,nv]-bands(k[None])[0,nv-1]+sc
def emin_q(q,kk): r=minimize(lambda k: pairE(k,q),kk,method='Nelder-Mead',options=dict(xatol=1e-8,fatol=1e-9,maxiter=6000,adaptive=True)); return r.fun,r.x
res={}
E0,_=emin_q(q0,k0); qn=np.linalg.norm(q0); u=np.cross(q0,[0,0,1.]); u/=np.linalg.norm(u)
rows=[]
for ph in (0.0,0.02,0.04,0.06,0.08,0.10):     # tilt q out of the (001) plane by angle ph (rotation about u)
    q=np.cos(ph)*q0+np.sin(ph)*qn*np.array([0,0,1.]); e,_=emin_q(q,k0); rows.append((ph,e))
res['out_of_plane']=rows; ph=np.array(rows)[:,0]; e=np.array(rows)[:,1]
res['b_z_eV_per_rad2']=float(np.polyfit(ph[:4]**2,e[:4]-E0,1)[0])
rows=[]
th0=np.arctan2(q0[1],q0[0])
for dth in (-0.04,-0.02,0,0.02,0.04):
    t=th0+dth; q=qn*np.array([np.cos(t),np.sin(t),0]); e,_=emin_q(q,k0); rows.append((dth,e))
res['in_plane']=rows; d=np.array(rows); res['a_theta_eV_per_rad2']=float(np.polyfit(d[:,0],d[:,1],2)[0])
def m_of(x,sgn):
    q=x[:3]; qa=np.linalg.norm(q)/K*1e3
    ke=sgn*(q[0]+x[3]); pen=0 if ke>=1 else 1e3*(1-ke)   # unfolded electron k_x beyond X: (2bar00) class for sgn=-1
    den=qa*vmax-pairE(x[3:],q)
    return 1e9 if den<=0 else qa**2/(2*den)/1e6+pen
for sgn,lab in ((-1,'U200'),(+1,'G0_beyondX')):
    best=None
    for qd in [(1.0,0,0),(1.02,.05,0),(1.05,.1,0),(1.1,.15,0),(1.02,.05,.05),(1.0,.2,0)]:
        q=sgn*np.array([qd[0],0,0])+np.array([0,qd[1],qd[2]]); kv=np.array([0,0,0.])
        r=minimize(m_of,np.r_[q,kv],args=(sgn,),method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-9,maxiter=20000,maxfev=20000,adaptive=True))
        if best is None or r.fun<best[0]: best=(r.fun,r.x)
    f,x=best; res[lab]=dict(m=float(f),q=x[:3].tolist(),k_v=x[3:].tolist(),q_keV=float(np.linalg.norm(x[:3])/K),E=float(pairE(x[3:],x[:3])))
json.dump(res,open(sys.argv[2],'w'),indent=1); print(json.dumps(res,indent=1))
