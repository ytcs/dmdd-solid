"""Irreducible wedge of a Gamma-centred N^3 grid of fcc Si under O_h (48 ops); writes K_POINTS list and the full-grid map.
usage: python3 ibz.py N out_prefix"""
import numpy as np, sys, itertools
N=int(sys.argv[1]); pre=sys.argv[2]
# fcc reciprocal vectors in units 2pi/a (QE ibrav=2): b1=(-1,-1,1), b2=(1,1,1), b3=(-1,1,-1)
B=np.array([[-1,-1,1],[1,1,1],[-1,1,-1]],float)   # rows = b_i
Binv=np.linalg.inv(B)
ops=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        R=np.zeros((3,3)); 
        for i in range(3): R[i,p[i]]=s[i]
        ops.append(R)
idx=np.array(list(itertools.product(range(N),repeat=3)))      # crystal integer coords
cart=(idx/N)@B
best=None
for R in ops:
    kc=cart@R.T
    cr=np.rint((kc@Binv)*N).astype(int)%N
    key=cr[:,0]*N*N+cr[:,1]*N+cr[:,2]
    best=key if best is None else np.minimum(best,key)
uniq,inv,cnt=np.unique(best,return_inverse=True,return_counts=True)
rep=np.stack([uniq//(N*N),(uniq//N)%N,uniq%N],1)/N
np.save(pre+'_map.npy',inv); np.save(pre+'_rep.npy',rep)
with open(pre+'_kpts.txt','w') as f:
    f.write('K_POINTS crystal\n%d\n'%len(rep))
    for r,c in zip(rep,cnt): f.write('%.10f %.10f %.10f %d\n'%(r[0],r[1],r[2],c))
print(len(rep))
