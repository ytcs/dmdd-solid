"""CW1 pass 5: DFT (QE nscf, 40 Ry) pair energy and vertex at the Wannier [E13] optimum (k_v, k_v + q), q = (0.5618, 0.1030, 0)(2pi/a),
k_v = (0.1257, -0.1074, 0), at a given lattice; local DFT pair-energy minimisation over k by a quadratic fit to the +-0.01 stencil.
usage: vertex_opt.py savedir labels alat_bohr out.json"""
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
vbm=E[I['G'],3]; cbm_axis=None
# PBE gap at this lattice from a coarse axis search is not in this k set: use the scf HOMO/LUMO-independent route:
# scissor = 1.170 - E_g^PBE(a); E_g^PBE from k_pass1-type data supplied on the command line via the json below
Ep=lambda ic,iv: E[ic,4]-E[iv,3]
e0=Ep(I['oc'],I['ov'])
# quadratic correction: move k (both v and c together) along x,y,z
g=[];h=[]
for j in range(3):
    ep=Ep(I[f'c+{j}'],I[f'v+{j}']); em=Ep(I[f'c-{j}'],I[f'v-{j}']); g.append((ep-em)/0.02); h.append((ep+em-2*e0)/0.01**2)
g=np.array(g);h=np.array(h); dk=-g/h; dE=-0.5*np.sum(g**2/h)
r=rho(I['oc'],I['ov'])
res=dict(alat=al,Epair_PBE=float(e0),dE_local=float(dE),dk=dk.tolist(),rho2_c1v1=float(abs(r[4,3])**2),rho2_c1_triplet=float(np.sum(abs(r[4,1:4])**2)),
         Ec_minus_vbm=float(E[I['oc'],4]-vbm),Ev_minus_vbm=float(E[I['ov'],3]-vbm))
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
