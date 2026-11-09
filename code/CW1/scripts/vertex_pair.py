"""CW1 pass 3: vertices at the actual threshold pair points (not at the band extrema).
(a) G'=0 class, q = 1.39 keV on [100] (the m_ZPL optimum, COMP-PH §4): hole at k_v = (0.052,0,0), electron at k_v+q = (0.6609,0,0) (2pi/a),
    the parabolic pair optimum k_v = -(q-k_c) m_hh/M_x with the masses of k_pass1; on-axis value (must vanish) and transverse k-gradient.
(b) (2bar00) class at q = -(1.00, 1.05, 1.10) x (2pi/a): hole at k_v, electron at unfolded k_v + q.  Sums over the two heavy holes (bands 3-4)
    and the triplet (2-4); lowest conduction band. usage: vertex_pair.py savedir labels out.json"""
import numpy as np, h5py, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
d, labf, out = sys.argv[1:4]; lab=open(labf).read().split(); k,E=read(d); I={l:i for i,l in enumerate(lab)}
def wf(i):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f: mi=f['MillerIndices'][:]; e=f['evc'][:]
    return {tuple(r):j for j,r in enumerate(mi)}, e[:,0::2]+1j*e[:,1::2]
W=[wf(i) for i in range(len(lab))]
def rho(ic,iv):
    a_,ca=W[ic]; b_,cb=W[iv]; keys=[g for g in a_ if g in b_]
    return np.conj(ca[:,[a_[g] for g in keys]])@cb[:,[b_[g] for g in keys]].T
tp=2*np.pi/10.2631; A=0.529177; vbm=E[I['G'],3]; sc=1.170-0.5567
res={}
r=rho(I['pc'],I['pv']); res['pair_Emin_eV']=float(E[I['pc'],4]-E[I['pv'],3]+sc); res['pair_axis_rho2_hh']=float(np.sum(abs(r[4,2:4])**2)); res['pair_axis_rho2_all']=float(np.sum(abs(r[4,1:4])**2))
for dd in (0.005,0.01):
    r=rho(I[f'pc_y{dd}'],I[f'pv_y{dd}'])
    res[f'gradk_hh_A_{dd}']=float(np.sqrt(np.sum(abs(r[4,2:4])**2))/(dd*tp)*A); res[f'gradk_all_A_{dd}']=float(np.sqrt(np.sum(abs(r[4,1:4])**2))/(dd*tp)*A)
for s in (1.0,1.05,1.10):
    r=rho(I[f'uc{s}'],I[f'uv{s}'])
    res[f'U200_{s}']=dict(Epair_eV=float(E[I[f'uc{s}'],4]-E[I[f'uv{s}'],3]+sc), rho2_hh=float(np.sum(abs(r[4,2:4])**2)), rho2_all=float(np.sum(abs(r[4,1:4])**2)))
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
