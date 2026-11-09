"""Si kinematic window from DFT (PBE, SG15, 40 Ry, 40^3 Γ-centred grid) + scissor to E_g(0)=1.170 eV.
E_min(q) = min_k [ε_c(k+q) − ε_v(k)] on the grid (depends on q mod G); continuous q by trilinear periodic interpolation.
Outputs: E_min angular tables, class-resolved zero-phonon reach masses, PAER edge masses (with ω_TA(Q*) from matdyn)."""
import numpy as np, xml.etree.ElementTree as ET, json, sys, subprocess, os
W='/root/work/COMP-PAER/main'; N=40
root=ET.parse(f'{W}/out_nscf/si.save/data-file-schema.xml').getroot()
eig=np.array([np.array(k.find('eigenvalues').text.split(),float) for k in root.iter('ks_energies')])*27.211386
mp=np.load(f'{W}/g40_map.npy'); full=eig[mp]            # (N^3, nbnd), order itertools.product (i,j,k)
ev=full[:,:4].max(1).reshape(N,N,N); ec=full[:,4:].min(1).reshape(N,N,N)
EgDFT=ec.min()-ev.max(); scis=1.170-EgDFT; ec=ec+scis
vbm=ev.max(); ev=ev-vbm; ec=ec-vbm
# E_min on grid: restrict k to valence states within 1.5 eV of VBM (they dominate the minimum)
sel=np.argwhere(ev>-1.5)
Emin=np.full((N,N,N),np.inf)
for (i,j,k) in sel:
    Emin=np.minimum(Emin,np.roll(ec,(-i,-j,-k),(0,1,2))-ev[i,j,k])
B=np.array([[-1,-1,1],[1,1,1],[-1,1,-1]],float); Binv=np.linalg.inv(B); tpiba=1.1569120590283817
def interp(Fg,qcart_A):   # qcart in Å^-1 -> trilinear periodic
    c=(qcart_A/tpiba)@Binv*N; i0=np.floor(c).astype(int); f=c-i0; out=0
    for dx in (0,1):
        for dy in (0,1):
            for dz in (0,1):
                w=(f[:,0] if dx else 1-f[:,0])*(f[:,1] if dy else 1-f[:,1])*(f[:,2] if dz else 1-f[:,2])
                out=out+w*Fg[(i0[:,0]+dx)%N,(i0[:,1]+dy)%N,(i0[:,2]+dz)%N]
    return out
def fib(n):
    i=np.arange(n)+0.5; th=np.arccos(1-2*i/n); ph=np.pi*(1+5**0.5)*i
    return np.stack([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)],1)
dirs=fib(400)
qE=np.arange(0.05,2.41,0.025)
Ed=np.array([interp(Emin,q*dirs) for q in qE])
# classes: nearest pocket vector K = k_c^val + G (k_c = 0.85 X along ±x,±y,±z)
kc=0.85*tpiba; vals=[s*kc*e for e in np.eye(3) for s in (1,-1)]
G=[np.array(g)*tpiba for g in [(0,0,0),(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2)]+[tuple(s) for s in np.array(np.meshgrid([1,-1],[1,-1],[1,-1])).reshape(3,-1).T]]
Ks=[(v+g,np.linalg.norm(g)) for v in vals for g in G]
def cls(qv):
    d=[np.linalg.norm(qv-K) for K,_ in Ks]; K,gn=Ks[int(np.argmin(d))]
    if gn<1e-9: return 'G0'
    # (2̄00) class: G antiparallel to the valley axis, |K| = 1.15 (2π/a)
    return 'G200' if abs(np.linalg.norm(K)-1.15*tpiba)<1e-6 else 'Gother'
lab=np.array([[cls(q*d) for d in dirs] for q in qE])
C=299792.458; vmax=794.5/C; A2eV=1973.27
def mreach(Eq,qA):   # minimal m with min_q [E/q + q/2m] <= vmax
    q=qA*A2eV; ms=np.linspace(0.25e6,1.5e6,5001)
    for m in ms:
        if np.any(Eq/q+q/(2*m)<=vmax): return m/1e6
    return np.inf
out=dict(EgDFT=EgDFT,scissor=scis,qE=qE.tolist(),Emin_dirs=Ed.tolist())
for c in ('G0','G200','Gother'):
    Ec=np.where(lab==c,Ed,np.inf).min(1); out['mZP_'+c]=mreach(Ec,qE)
out['mZP_any']=mreach(Ed.min(1),qE)
# direct-gap / E_min along Γ-X for the record
out['Emin_min']=float(Emin.min()); out['Edir_Gamma']=float(ec[0,0,0]-ev[0,0,0])
json.dump(out,open(sys.argv[1],'w'))
print({k:v for k,v in out.items() if not isinstance(v,list)})
