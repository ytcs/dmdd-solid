import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'../DC-49')
import numpy as np, dirac as d, absorption as A
def rep(lab,n,**o):
    p=d.setup(n,**o); pub=np.loadtxt(f'../DC-49/data/pub_abs_{n}.csv',delimiter=',')
    pub=pub[(pub[:,1]<1e-14)&(pub[:,0]<2*p['EL']*.98)&(pub[:,0]>2*p['D']*1.3)]; s=pub[::max(1,len(pub)//60)]
    r=A.eps_lim(p,s[:,0],'src')/s[:,1]; print(lab,'calc/pub mean %.4f min %.4f max %.4f spread %.2f%%'%(np.exp(np.log(r).mean()),r.min(),r.max(),100*(r.max()/r.min()-1)),flush=True)
rep('Yb g=24 rho=11.596','Yb')
rep('Yb g=12 rho=11.596 (printed)','Yb',g=12)
rep('Yb g=12 rho=5.8','Yb',g=12,rho=5.8)
rep('Yb g=12 rho=6.135','Yb',g=12,rho=6.135)
rep('Yb g=16','Yb',g=16); rep('Yb g=20','Yb',g=20); rep('Yb g=28','Yb',g=28)
rep('ZrTe5 exp v_x=1.1','ZrTe5_exp'); rep('ZrTe5 exp v_x=1.3 printed','ZrTe5_exp',v=(1.3e-3,6.5e-4,1.6e-3))
rep('ZrTe5 exp v_x=1.2','ZrTe5_exp',v=(1.2e-3,6.5e-4,1.6e-3))
rep('ZrTe5 exp v_x=1.3 Lam=.07','ZrTe5_exp',v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07))
