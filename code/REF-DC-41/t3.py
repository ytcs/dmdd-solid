import numpy as np, spec as S
print(' check vs direct: ',S.Pup(2.2,5.64)[:2], 'DC-41 edge: L ratio should be 1.299')
g=S.Pup(2.2,5.64)[1]; print(np.imag(1/g)/np.imag(1/S.Pn(2.2,5.64)))
for Q in [5.2,5.64,6.41,7.69,9.7,12.82,25.64,100.]:
    ds=np.geomspace(1e-12,40,900); v=[]
    for d in ds:
        y=2+d; p,g,F,UF=S.Pup(y,Q); v.append((y,g.real,g.imag,p.real,p.imag))
    v=np.array(v); y=v[:,0]; G=v[:,1]+1j*v[:,2]; Lam=np.imag(1/G); Ln=np.imag(1/np.array([S.Pn(a,Q) if abs(a-Q)>1e-9 else 1j for a in y]))
    ok=y<Q*0.999
    i=np.argmax(np.where(ok,Lam/np.maximum(Ln,1e-300),0)); j=np.argmax(Lam)
    sc=np.where(v[:-1,1]*v[1:,1]<0)[0]
    print('Q',Q,'ReP~ crossings y:',np.round(y[sc],6),'Im there',np.round(v[sc,2],4),'| max Lam %.4f at y=%.6f; max Lam/Lnor %.4f at y=%.6f; edge y=%.3f; Lam_nor(edge-ish)=%.3f'%(Lam[j],y[j],(Lam/np.maximum(Ln,1e-300))[i],y[i],.39*Q,Ln[np.argmin(abs(y-.39*Q))]))
    for dd in (1e-8,1e-6,1e-4,1e-3,1e-2,0.02,0.05,0.1,0.2,0.5,1):
        k=np.argmin(abs(y-2-dd)); print('    y-2=%.0e ReP~ %.4f ImP~ %.5f Lam %.4f Lam/Lnor %.3f'%(dd,v[k,1],v[k,2],Lam[k],Lam[k]/Ln[k]))
