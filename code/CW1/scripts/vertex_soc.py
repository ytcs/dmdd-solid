"""LE-36: SOC-lifted Si vertices (QE noncollinear + lspinorb, SG15 Si_ONCV_PBE_FR-1.1, 40 Ry, a_exp) at the two second-class threshold
pairs: (a) on-axis q = k_c xhat (hole at Gamma, electron at k_c) and the on-axis pair point (0.052 / 0.6609); (b) the {001}-mirror-plane
optimum (k_v, k_v + q) of out/emin_fast.json. Spinor states: rho = sum_{G,sigma} c*_{m,k+q}(G,sigma) c_{n,k}(G,sigma).
Reported: sum over the top valence Kramers pair (bands 7-8) and the lowest conduction Kramers pair (9-10) of |rho|^2, i.e. the
spin-summed vertex comparable to the scalar 2 x sum_v |rho|^2 / 2 ... (scalar: per spin |rho|^2 with an explicit factor 2; here one Kramers
pair = 2 states, so the comparable scalar number is the scalar |rho_cv|^2 of the top band). Also: split-off energy at Gamma.
usage: vertex_soc.py savedir out.json"""
import numpy as np, h5py, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
d,out=sys.argv[1:3]; k,E=read(d)
def wf(i):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f: mi=f['MillerIndices'][:]; e=f['evc'][:]
    c=e[:,0::2]+1j*e[:,1::2]; n=len(mi); return {tuple(r):j for j,r in enumerate(mi)}, c, n
def rho(ic,iv):
    a_,ca,na=wf(ic); b_,cb,nb=wf(iv); keys=[g for g in a_ if g in b_]
    ia=np.array([a_[g] for g in keys]); ib=np.array([b_[g] for g in keys])
    A=np.concatenate([ca[:,ia],ca[:,na+ia]],1); B=np.concatenate([cb[:,ib],cb[:,nb+ib]],1)
    return np.conj(A)@B.T
res=dict(Gamma_levels_meV=[float(x) for x in (E[0,4:8]-E[0,7])*1e3])
for lab,(ic,iv) in dict(axis_extremum=(1,0),axis_pair=(3,2),mirror_optimum=(5,4)).items():
    r=rho(ic,iv); res[lab]=dict(top_pair=float(np.sum(abs(r[8:10,6:8])**2)),all_valence=float(np.sum(abs(r[8:10,2:8])**2)),
                               Epair_PBE=float(E[ic,8]-E[iv,7]))
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
