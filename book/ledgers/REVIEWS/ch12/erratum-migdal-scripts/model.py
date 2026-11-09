import numpy as np
a=10.263; Z=4
alpha_,v1,v2=0.6102,3.042,-1.372   # Appelbaum-Hamann (Ry, bohr)
Omega=a**3/4; Oat=Omega/2
n=8/Omega
kF=(3*np.pi**2*n)**(1/3)
def v_bare_Ha(p):
    p=np.asarray(p,float); ps=np.maximum(p,1e-8)
    e=np.exp(-ps**2/(4*alpha_))
    v=-4*np.pi*Z*2*e/ps**2 + (np.pi/alpha_)**1.5*e*(v1+v2*(1.5/alpha_-ps**2/(4*alpha_**2)))
    return v/2
def eps_lind(p):
    p=np.maximum(np.asarray(p,float),1e-8); x=p/(2*kF)
    F=0.5+(1-x**2)/(4*x)*np.log(np.abs((1+x)/(1-x+1e-14)))
    kTF2=4*kF/np.pi
    return 1+kTF2/p**2*F
def w(p): return v_bare_Ha(p)/eps_lind(p)
if __name__=="__main__":
    b=2*np.pi/a
    for G2 in [3,4,8,11,12,16,19]:
        G=b*np.sqrt(G2)
        print(G2, 'V_S Ry =', 2*w(G)/Oat)
    print('kF',kF,'w(0+)/Oat Ry',2*w(1e-3)/Oat, 'EF Ry', kF**2)
