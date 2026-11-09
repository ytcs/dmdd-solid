import numpy as np
from scipy.interpolate import PchipInterpolator
from migmodel12 import a,Oat,Omega
b=2*np.pi/a
xs=np.array([0,1.5,3,5.5,8,11,14,17,30.]); ys=np.array([-0.61,-0.42,-0.21,-0.06,0.04,0.08,0.03,0.0,0.0])
_f=PchipInterpolator(xs,ys)
def w(p):
    x=(np.asarray(p,float)/b)**2
    return np.where(x<30,_f(np.minimum(x,30)),0.0)*Oat/2   # Ha*bohr^3 ; V_S(Ry)=2w/Oat
