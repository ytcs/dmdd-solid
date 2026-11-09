"""Finite-q suppression proxy F_rho(q) = <sum_{v,c} |rho_cv(Gamma,q)|^2 / q^2> / (same at q->0)  [E proxy for the
dipole->saturation crossover of the DM vertex in M^(2)], plus the band-completeness f-sum check
sum_m (e_m - e_v)|rho_mv(Gamma,q)|^2 vs q^2/2m_e (local-potential identity; N_m = 16 bands; non-local PP corrections not included).
rho_mn(k,q) = <psi_{m,k+q}|e^{iq.r}|psi_{nk}> with k+q computed UNFOLDED (nscf at k = q exactly), so rho = sum_G c*_{m,q}(G) c_{n,0}(G)."""
import numpy as np, h5py, sys, json
d=sys.argv[1]  # save dir
def rd(i):
    with h5py.File(f'{d}/wfc{i}.hdf5','r') as f:
        mi=f['MillerIndices'][:]; e=f['evc'][:]; xk=f.attrs['xk']
    c=e[:,0::2]+1j*e[:,1::2]
    return mi,c,xk
import xml.etree.ElementTree as ET
root=ET.parse(f'{d}/data-file-schema.xml').getroot()
eig=[np.array(ks.find('eigenvalues').text.split(),float)*27.211386 for ks in root.iter('ks_energies')]
m0,c0,_=rd(1)
key0={tuple(r):i for i,r in enumerate(m0)}
tpiba=1.1569120590283817
Eg_dft=None
res=[]
nq=13
for idir in range(3):
    for iq in range(nq):
        ik=2+idir*nq+iq
        mi,c,xk=rd(ik)
        q=np.linalg.norm(xk)  # bohr^-1 (QE stores xk in cartesian bohr^-1? check below)
        idx=np.array([key0.get(tuple(r),-1) for r in mi])
        ok=idx>=0
        rho=np.conj(c[:,ok])@c0[:,idx[ok]].T       # rho[m(k=q), n(Gamma)]
        e0=eig[0]; eq=eig[ik-1]
        v=slice(1,4); cc=slice(4,8)
        s=np.sum(np.abs(rho[cc,v])**2)
        fsum=np.sum((eq[:,None]-e0[None,1:4])*np.abs(rho[:,1:4])**2)/3   # eV, per valence band, N_m=16
        res.append(dict(dir=idir,xk=list(map(float,xk)),s=float(s),fsum=float(fsum)))
json.dump(res,open(sys.argv[2],'w'),indent=0)
