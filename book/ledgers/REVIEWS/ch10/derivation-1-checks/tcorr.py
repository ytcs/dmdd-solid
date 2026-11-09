import numpy as np
rng=np.random.default_rng(0); kF=1.0; m=1.0
k=rng.uniform(-1,1,(400000,3)); k=k[np.linalg.norm(k,axis=1)<kF]
for qv in [0.3,1.0,2.5]:
    q=np.array([0,0,qv]); kp=k+q; ok=np.linalg.norm(kp,axis=1)>kF
    Tv=np.einsum('ij,ij->i',k[ok],kp[ok])/(2*m)   # (1/2m) p.e^{iqr}p vertex
    # proper cross response weight sum over pairs of density vertex (1) times T vertex; spin factor 2 singlet; triplet: Tr(sigma_z)=0
    print('q=',qv,' sum_pairs n*T (singlet, per unit) =',Tv.mean()*ok.mean(),' triplet n*s_z cross = Tr(sigma_z)/2 * ... = 0')
