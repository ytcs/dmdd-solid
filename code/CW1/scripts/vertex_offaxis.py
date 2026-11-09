"""CW1 pass 4: G'=0 vertex at the pair optimum for q tilted off [100] at |q| ~ 1.39 keV: q = (s, d, 0) [(001) tilt] and (s, d/sqrt2, d/sqrt2)
[(011) tilt] (2pi/a), hole at k_v = (0.052, -0.576 q_perp), electron at k_v + q (parabolic pair optimum, m_t = 0.194, m_hh = 0.264).
Output: sqrt(sum_hh |rho|^2)/|q_perp| (Angstrom) = the effective angular vertex gradient g_perp, and the pair energy (PBE + scissor).
usage: vertex_offaxis.py savedir labels out.json"""
import numpy as np, h5py, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
d, labf, out = sys.argv[1:4]; lab=open(labf).read().split(); k,E=read(d); I={l:i for i,l in enumerate(lab)}
def wf(i):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f: mi=f['MillerIndices'][:]; e=f['evc'][:]
    return {tuple(r):j for j,r in enumerate(mi)}, e[:,0::2]+1j*e[:,1::2]
def rho(ic,iv):
    a_,ca=wf(ic); b_,cb=wf(iv); keys=[g for g in a_ if g in b_]
    return np.conj(ca[:,[a_[g] for g in keys]])@cb[:,[b_[g] for g in keys]].T
tp=2*np.pi/10.2631; A=0.529177; sc=1.170-0.5567; res={}
for t in ('o','od'):
    for dd in (0.005,0.01,0.02,0.04):
        ic,iv=I[f'{t}c{dd}'],I[f'{t}v{dd}']; r=rho(ic,iv)
        res[f'{t}{dd}']=dict(g_perp_A=float(np.sqrt(np.sum(abs(r[4,1:4])**2))/(dd*tp)*A), rho2=float(np.sum(abs(r[4,1:4])**2)),
                            Epair=float(E[ic,4]-E[iv,3]+sc), qperp_invA=float(dd*tp/A))
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
