"""CW1 pass 5b: band-resolved vertex at the off-axis [E13] optimum and its out-of-mirror-plane gradients.
At k_v, k_v+q in the (001) plane the sigma_z mirror (an O_h \\ T_d element; no residual phase for G' = 0) classifies the states; the
top valence band (heavy hole, the pair minimum) is sigma_z-odd relative to the Delta_1-like conduction state, so its vertex vanishes in the plane.
Gradients: d/dk_z at fixed q (v and c shifted together, 'v+2','c+2') and d/dq_z at fixed k_v (c shifted only). usage: vertex_opt2.py savedir labels alat out.json"""
import numpy as np, h5py, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
d, labf, al, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
lab=open(labf).read().split(); k,E=read(d); I={l:i for i,l in enumerate(lab)}
def wf(i):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f: mi=f['MillerIndices'][:]; e=f['evc'][:]
    return {tuple(r):j for j,r in enumerate(mi)}, e[:,0::2]+1j*e[:,1::2]
def rho(ic,iv):
    a_,ca=wf(ic); b_,cb=wf(iv); keys=[g for g in a_ if g in b_]
    return np.conj(ca[:,[a_[g] for g in keys]])@cb[:,[b_[g] for g in keys]].T
tp=2*np.pi/al; A=0.529177; vbm=E[I['G'],3]
r=rho(I['oc'],I['ov'])
res=dict(Ev_minus_vbm=[float(E[I['ov'],b]-vbm) for b in (1,2,3)], rho2_per_v=[float(abs(r[4,b])**2) for b in (1,2,3)])
dz=0.01*tp/A
r1=rho(I['c+2'],I['v+2']); r2=rho(I['c-2'],I['v-2']); res['dkz_top_A']=float(np.sqrt((abs(r1[4,3])**2+abs(r2[4,3])**2)/2)/dz)
r1=rho(I['c+2'],I['ov']); r2=rho(I['c-2'],I['ov']); res['dqz_top_A']=float(np.sqrt((abs(r1[4,3])**2+abs(r2[4,3])**2)/2)/dz)
res['Epair_top_minus_second_eV']=float(E[I['ov'],3]-E[I['ov'],2])
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
