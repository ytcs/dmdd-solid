"""Referee, DC-36 priority 3. Two methods that share no code with micro.py:
(A) deterministic: axial force = end-annuli only, a(theta) = (2 rho A/M) Int dv_z g(v_z|W cos theta) v_z|v_z| R_slab(|v_z|)  [exact at saturation by Liouville: specular side walls leave v_z alone]
(B) own ray tracer (own geometry code), true radii, with: specular fraction p, tilt of the wind out of the rotation plane, closed can as a thin slab met in BOTH directions (DM reflected inside stays inside)."""
import numpy as np, sys, time
AMU=1.66053907e-24; RHOX=0.3*1.78266192e-27*1e6   # kg/m^3
V0,VESC,W=238.,544.,250.5
TRUE=lambda g:[dict(b,Ri=b['Ri']/2,Ro=b['Ro']/2) for b in g]
SUEP=TRUE([dict(n='PtRh',Ri=30.801,Ro=39.390,L=43.330,M=.401706,rho=19.972),dict(n='TA6V',Ri=60.802,Ro=69.401,L=79.831,M=.300939,rho=4.420)])
SUREF=TRUE([dict(n='PtRh_in',Ri=30.801,Ro=39.390,L=43.331,M=.401533,rho=19.967),dict(n='PtRh_out',Ri=60.799,Ro=69.397,L=79.821,M=1.359813,rho=19.980)])
NREF=4.420
def Rslab(vn,vc):
    k2=vn**2-vc**2; k=np.sqrt(np.maximum(k2,0)); R=np.where(k2>0,((vn-k)/(vn+k+1e-300))**2,1.); return 2*R/(1+R)
def gz(vz,w):   # marginal of the truncated Maxwellian along z, Radon form
    from scipy.special import erf
    z=VESC/V0; N=1/(np.pi**1.5*V0**3*(erf(z)-2*z*np.exp(-z*z)/np.sqrt(np.pi)))
    return np.where(np.abs(vz-w)<VESC,N*np.pi*V0**2*(np.exp(-(vz-w)**2/V0**2)-np.exp(-z*z)),0.)
def a_face(b,u,th_n=64,sign=1,sat=False):
    A=np.pi*((b['Ro']*1e-3)**2-(b['Ri']*1e-3)**2); vc=np.sqrt(u*u*b['rho']/NREF)
    v=np.linspace(-1000,1000,20001); dv=v[1]-v[0]
    x,wt=np.polynomial.legendre.leggauss(th_n); th=(x+1)*np.pi/2; wt=wt*np.pi/2
    a=[]
    for t in th:
        Rs=1. if sat else Rslab(np.abs(v),vc)
        a.append(2*RHOX*A/b['M']*np.sum(gz(v,W*np.cos(t))*v*np.abs(v)*Rs)*dv*1e6)
    return (2/np.pi)*np.sum(wt*np.array(a)*np.cos(th))
def hits(pos,dd,B):
    """nearest crossing with hollow cylinders; returns t, body index, normal"""
    n=len(pos); best=np.full(n,np.inf); ib=np.zeros(n,int); nr=np.zeros((n,3))
    x,y,z=pos.T; dx,dy,dz=dd.T; a=dx*dx+dy*dy
    for i,b in enumerate(B):
        h=b['L']/2
        for s in (1.,-1.):
            with np.errstate(divide='ignore',invalid='ignore'): t=(s*h-z)/dz
            r2=(x+t*dx)**2+(y+t*dy)**2
            m=(t>1e-9)&(t<best)&(r2>=b['Ri']**2)&(r2<=b['Ro']**2)
            best[m]=t[m]; ib[m]=i; nr[m]=(0,0,s)
        for R,o in ((b['Ro'],1.),(b['Ri'],-1.)):
            bb=x*dx+y*dy; c=x*x+y*y-R*R; D=bb*bb-a*c; q=np.sqrt(np.maximum(D,0))
            for sg in (-1.,1.):
                with np.errstate(divide='ignore',invalid='ignore'): t=(-bb+sg*q)/a
                m=(D>0)&(t>1e-9)&(t<best)&(np.abs(z+t*dz)<=h)
                best[m]=t[m]; ib[m]=i
                px=x[m]+t[m]*dx[m]; py=y[m]+t[m]*dy[m]
                nr[m]=np.c_[o*px/R,o*py/R,0*px]
    return best,ib,nr
def lambert(n,s,rng):
    c=np.sqrt(rng.random(len(n))); ph=2*np.pi*rng.random(len(n)); sn=np.sqrt(1-c*c)
    e=np.cross(n,np.array([.31,.52,.79])); e/=np.linalg.norm(e,axis=1)[:,None]; f=np.cross(n,e)
    return s[:,None]*(c[:,None]*n+(sn*np.cos(ph))[:,None]*e+(sn*np.sin(ph))[:,None]*f)
def sample(N,th,beta,rng):
    v=np.empty((0,3))
    while len(v)<N:
        c=rng.normal(0,V0/np.sqrt(2),(N,3)); v=np.r_[v,c[(c*c).sum(1)<VESC**2]]
    v=v[:N].copy(); v+=W*np.array([np.cos(beta)*np.sin(th),np.sin(beta),np.cos(beta)*np.cos(th)])
    return v
def trace(B,u,th,N,rng,sign=1,p=1.,beta=0.,can=None,maxb=300):
    nb=len(B); wreg=np.r_[0.,[sign*.5*u*u*b['rho']/NREF for b in B]]
    Rb=np.max([np.hypot(b['Ro'],b['L']/2) for b in B])*1.01
    S=list(B)
    if can: Rb=np.hypot(can['R'],can['H'])*1.01; shell=dict(Ri=0.,Ro=can['R'],L=2*can['H'])
    v=sample(N,th,beta,rng); sp=np.linalg.norm(v,axis=1); d=v/sp[:,None]
    e1=np.cross(d,[.1,.7,.2]); e1/=np.linalg.norm(e1,axis=1)[:,None]; e2=np.cross(d,e1)
    r=Rb*np.sqrt(rng.random(N)); ph=2*np.pi*rng.random(N)
    pos=(r*np.cos(ph))[:,None]*e1+(r*np.sin(ph))[:,None]*e2-3*Rb*d
    reg=np.zeros(N,int); ids=np.arange(N); P=np.zeros((nb,N)); vel=v.copy(); wc=(sign*.5*u*u*can['rho']/NREF) if can else 0.
    for it in range(maxb):
        if len(ids)==0: break
        s_=np.linalg.norm(vel,axis=1); dd=vel/s_[:,None]
        t,ib,nr=hits(pos,dd,B)
        if can:
            t2,_,n2=hits(pos,dd,[shell])
            # shell has a solid cross-section in hits(): its end planes and outer wall are what we need
            c=t2<t; t=np.where(c,t2,t); nr=np.where(c[:,None],n2,nr); ib=np.where(c,-1,ib)
        ok=np.isfinite(t)
        pos,vel,reg,ids,t,ib,nr,dd,s_=[a[ok] for a in (pos,vel,reg,ids,t,ib,nr,dd,s_)]
        if len(ids)==0: break
        pos=pos+t[:,None]*dd
        vn=(vel*nr).sum(1); an=np.abs(vn)
        iscan=ib<0
        other=np.where(reg==0,ib+1,0); other=np.where(iscan,reg,other)
        dw=wreg[other]-wreg[reg]
        k2=an**2-2*dw; k=np.sqrt(np.maximum(k2,0)); R=np.where(k2>0,((an-k)/(an+k+1e-300))**2,1.)
        if can:
            vcc=np.sqrt(max(2*wc,0.)); k2c=an**2-2*wc; kc=np.sqrt(np.maximum(k2c,0)); Rc=np.where(k2c>0,((an-kc)/(an+kc+1e-300))**2,1.); R=np.where(iscan,2*Rc/(1+Rc),R); k=np.where(iscan,an,k)
        refl=rng.random(len(ids))<R
        vr=vel-2*vn[:,None]*nr
        vt=vel+((np.sign(vn)*k-vn))[:,None]*nr
        new=np.where(refl[:,None],vr,vt)
        if p<1.:
            m=refl&(reg==0)&(rng.random(len(ids))>p)
            if m.any(): new[m]=lambert(np.where((vel[m]*nr[m]).sum(1)[:,None]<0,nr[m],-nr[m]),s_[m],rng)
        body=~iscan
        dvz=(vel-new)[:,2]
        for i in range(nb):
            m=body&(ib==i); np.add.at(P[i],ids[m],dvz[m])
        reg=np.where(refl|iscan,reg,other); vel=new
        pos=pos+1e-6*vel/np.linalg.norm(vel,axis=1)[:,None]
    con=RHOX*np.pi*(Rb*1e-3)**2*1e6
    T=P*sp[None,:]
    return con*T.mean(1)/np.array([b['M'] for b in B]),con*T.std(1)/np.sqrt(N)/np.array([b['M'] for b in B])
def harmonic(B,u,N=250000,nth=4,seed=1,**k):
    rng=np.random.default_rng(seed); x,wt=np.polynomial.legendre.leggauss(nth); th=(x+1)*np.pi/4; wt=wt*np.pi/4
    A=[];E=[]
    for t in th:
        a,e=trace(B,u,t,N,rng,**k); A.append(a); E.append(e)
    A=np.array(A);E=np.array(E); c=np.cos(th)[:,None]; w=wt[:,None]
    return (4/np.pi)*(w*A*c).sum(0),(4/np.pi)*np.sqrt(((w*E*c)**2).sum(0))
if __name__=='__main__':
    print('(A) deterministic end-face integral, true geometry, rho=0.3')
    print(' saturated: PtRh %.4e TA6V %.4e  Da %.4e ; SUREF in %.4e out %.4e Da %.4e'%(a_face(SUEP[0],1,sat=True),a_face(SUEP[1],1,sat=True),a_face(SUEP[1],1,sat=True)-a_face(SUEP[0],1,sat=True),a_face(SUREF[0],1,sat=True),a_face(SUREF[1],1,sat=True),a_face(SUREF[1],1,sat=True)-a_face(SUREF[0],1,sat=True)))
    us=np.array([30,60,100,150,200,250,280,300,310,320,350,400,500,600,800,1000.]); 
    print(' u  a_Pt a_Ti Da')
    D=[]
    for u in us:
        a,b=a_face(SUEP[0],u),a_face(SUEP[1],u); D.append(b-a); print(' %5.0f %.3e %.3e %+.3e'%(u,a,b,b-a))
    D=np.array(D); j=np.where(np.sign(D[:-1])!=np.sign(D[1:]))[0][0]; print(' zero at u=%.1f km/s'%(us[j]+(us[j+1]-us[j])*(-D[j])/(D[j+1]-D[j])))
    print(' with printed-as-radii geometry: a_sat TA6V %.3e PtRh %.3e'%(4*a_face(SUEP[1],1,sat=True),4*a_face(SUEP[0],1,sat=True)))
