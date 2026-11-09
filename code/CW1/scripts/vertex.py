"""CW1 vertices from QE nscf wavefunctions (Si, PBE, SG15 NC): rho_mn(k,q) = <psi_{m,k+q}|e^{iq.r}|psi_{nk}> with k+q UNFOLDED
(the nscf is run at the unfolded k+q), so rho = sum_G c*_{m,k+q}(G) c_{n,k}(G) over common Miller indices (exact for NC PPs
within one ecut). usage: vertex.py savedir labels out.json"""
import numpy as np, h5py, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
d, labf, out = sys.argv[1:4]
lab = open(labf).read().split()
k, E = read(d)
def wf(i):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f:
        mi=f['MillerIndices'][:]; e=f['evc'][:]
    return {tuple(r):j for j,r in enumerate(mi)}, e[:,0::2]+1j*e[:,1::2]
W=[wf(i) for i in range(len(lab))]
I={l:i for i,l in enumerate(lab)}
def rho(ic, iv):
    """rho[m,n] = <psi_m(k_ic)|e^{i(k_ic-k_iv).r}|psi_n(k_iv)>"""
    kc_, cc = W[ic]; kv_, cv = W[iv]
    keys=[g for g in kc_ if g in kv_]
    a=np.array([kc_[g] for g in keys]); b=np.array([kv_[g] for g in keys])
    return np.conj(cc[:,a]) @ cv[:,b].T
al=10.2631; tp=2*np.pi/al; A=0.529177  # bohr->Angstrom
V=slice(1,4)   # Gamma25' triplet (bands 2-4)
res={}
vbm=E[I['G'],3]
# (1) on-axis G'=0 vertex (C10a control: must vanish)
r=rho(I['q0_axis'],I['G']); res['axis_G0_sum_v_|rho_c1v|^2']=float(np.sum(abs(r[4,V])**2))
res['axis_G0_c2..4']=[float(np.sum(abs(r[c,V])**2)) for c in range(4,8)]
# (2) transverse k-gradient at fixed q = kc xhat: valence at (0,d,0), conduction at (kc,d,0)
gk={};gq={}
for d_ in (0.005,0.01,0.02):
    for t in ('y','yz'):
        r=rho(I[f'c_{t}{d_}'],I[f'v_{t}{d_}']); s=np.sum(abs(r[4,V])**2)
        gk[f'{t}{d_}']=float(np.sqrt(s)/(d_*tp)*A)        # Angstrom: sqrt(sum_v|rho|^2)/|dk|
        r=rho(I[f'c_{t}{d_}'],I['G']); s=np.sum(abs(r[4,V])**2)   # fixed k=Gamma, q = kc x + d yhat
        gq[f'{t}{d_}']=float(np.sqrt(s)/(d_*tp)*A)
res['grad_k_rho_Angstrom']=gk; res['grad_q_rho_Angstrom']=gq
# (3) (2bar00) class: valence Gamma, conduction at unfolded k = q = (-s,0,0) (reduced to (2-s,0,0)), lowest c and lowest two c
u={}
for l in lab:
    if l.startswith('U200') or l=='U111':
        r=rho(I[l],I['G']); i=I[l]
        u[l]=dict(Ec_minus_VBM=[float(E[i,c]-vbm) for c in (4,5)], c1=float(np.sum(abs(r[4,V])**2)), c12=float(np.sum(abs(r[4:6,V])**2)),
                  c1to4=float(np.sum(abs(r[4:8,V])**2)), q_invA=float(np.linalg.norm(k[i])*tp/A))
res['umklapp']=u
# (4) F_rho proxy points: sum_{v in triplet, c in 4 lowest}|rho_cv(Gamma,q)|^2/q^2 (q in Angstrom^-1), cubic average 6:12:8
F={}
for qa in (1.155,1.25,1.34):
    vals=[]
    for n in ('100','110','111'):
        r=rho(I[f'F{n}_{qa}'],I['G']); vals.append(np.sum(abs(r[4:8,V])**2)/qa**2)
    F[str(qa)]=dict(dirs=[float(x) for x in vals], cubic=float((6*vals[0]+12*vals[1]+8*vals[2])/26))
res['F_raw']=F
json.dump(res,open(out,'w'),indent=1); print(json.dumps(res,indent=1))
