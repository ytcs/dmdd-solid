import numpy as np, crdm
for lab,m in [('1keV',1e-6),('10keV',1e-5),('me',crdm.ME)]:
    for med in ['light','heavy']:
        a=np.loadtxt(f'data/pub_flux_{med}_{lab}.csv',delimiter=',')
        a=a[(a[:,0]>=1e-7)&(a[:,1]>1.05e-12)&(a[:,1]<99)]
        c=crdm.flux(a[:,0],m,med)*a[:,0]
        r=c/a[:,1]; idx=np.linspace(0,len(a)-1,9).astype(int)
        print(lab,med,' '.join('%.0e:%.3g'%(a[i,0],r[i]) for i in idx))
