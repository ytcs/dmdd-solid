"""DC-36: reflection/refraction force on the MICROSCOPE test masses (CW2 section 22, (CW2.25)).
Optical potential V = 2 pi b n/mu, sharp faces, specular (option diffuse), per-face 1D transfer matrix along the local
normal, stochastic (incoherent) treatment of the two faces of every wall = thickness average R_slab = 2R/(1+R).
Everything is in velocity units: w = V/m_chi (mu = m_chi), v_c^2 = 2 w. km/s inside, SI on output.
Universal scaling: at fixed geometry a(sigma, m) = G(u), u^2 = v_c,Ti^2 = 4 pi b n_Ti/m^2, b = sqrt(sigma/4 pi)."""
import numpy as np, sys
AMU=1.66053907e-27
RHO_GEV=0.3; GEVCM3=1.78266192e-27*1e6      # 1 GeV/cm^3 in kg/m^3
V0,VESC,WIND=238.,544.,250.5                 # CONVENTIONS section 8 (km/s)
# Test masses, 1909.10598 Table (lab metrology). lengths mm, mass kg, density g/cm^3
SUEP=[dict(name='PtRh',Ri=30.801,Ro=39.390,L=43.330,M=.401706,rho=19.972),dict(name='TA6V',Ri=60.802,Ro=69.401,L=79.831,M=.300939,rho=4.420)]
SUREF=[dict(name='PtRh_in',Ri=30.801,Ro=39.390,L=43.331,M=.401533,rho=19.967),dict(name='PtRh_out',Ri=60.799,Ro=69.397,L=79.821,M=1.359813,rho=19.980)]
def npercm3(rho): return rho/ (AMU*1e3)      # nucleons per cm^3
def sample_v(N,theta,rng):
    out=np.empty((0,3))
    while len(out)<N:
        u=rng.normal(0,V0/np.sqrt(2),(int(N*1.1)+100,3)); u=u[(u*u).sum(1)<VESC**2]; out=np.r_[out,u]
    v=out[:N]; v[:,0]+=WIND*np.sin(theta); v[:,2]+=WIND*np.cos(theta); return v
def trace(bodies,u2,theta,N,rng,sign=+1,diffuse=0.,housing=None,maxb=400,nref=None):
    """returns <|v| dv_z> per body in (km/s)^2 (x Rb^2 pi later), plus diagnostics. u2=v_c,Ti^2 [(km/s)^2]; sign=+1 repulsive."""
    nb=len(bodies); nref=nref or npercm3(4.420)
    w=np.array([0.]+[sign*.5*u2*npercm3(b['rho'])/nref for b in bodies])     # region potentials
    Rb=max(np.hypot(b['Ro'],b['L']/2) for b in bodies)*1.001
    if housing: Rb=np.hypot(housing['R'],housing['H'])*1.001
    v=sample_v(N,theta,rng); sp=np.sqrt((v*v).sum(1)); d=v/sp[:,None]
    a=np.cross(d,[0.3,.5,.81]); a/=np.sqrt((a*a).sum(1))[:,None]; b2=np.cross(d,a)
    r=Rb*np.sqrt(rng.random(N)); ph=2*np.pi*rng.random(N)
    x=(r*np.cos(ph))[:,None]*a+(r*np.sin(ph))[:,None]*b2-2*Rb*d
    alive=np.ones(N,bool)
    if housing: # closed can: enter through its surface with probability 1-R_slab(v_n); parallel-wall slab keeps v
        t,n=can_entry(x,d,housing); hit=np.isfinite(t)
        vn=np.abs((v*n).sum(1)); wh=sign*.5*u2*npercm3(housing['rho'])/nref
        k2=vn**2-2*wh; ok=k2>0; R=np.where(ok,((vn-np.sqrt(np.maximum(k2,0)))/(vn+np.sqrt(np.maximum(k2,0))))**2,1.); Rs=2*R/(1+R)
        alive&=(~hit)|(rng.random(N)>Rs)
        alive&=hit                                   # rays that miss the can never reach the masses
    Pz=np.zeros(nb); Pz2=np.zeros(nb); reg=np.zeros(N,int); wgt=sp.copy(); nbounce=np.zeros(N,int); hits=np.zeros(nb)
    per=np.zeros((N,nb)); idx=np.where(alive)[0]
    pos=x[idx]; vel=v[idx]; rg=reg[idx]; ids=idx
    for it in range(maxb):
        if len(ids)==0: break
        sp_=np.sqrt((vel*vel).sum(1)); dd=vel/sp_[:,None]
        best=np.full(len(ids),np.inf); bb=np.zeros(len(ids),int); nrm=np.zeros((len(ids),3))
        rx,ry,rz=pos.T; dx,dy,dz=dd.T
        A=dx*dx+dy*dy; 
        for ib,b in enumerate(bodies):
            H=b['L']/2
            for sgn in (1,-1):
                with np.errstate(divide='ignore',invalid='ignore'):
                    t=(sgn*H-rz)/dz
                ok=(t>1e-9)&(t<best)
                rr=np.hypot(rx+t*dx,ry+t*dy); ok&=(rr>=b['Ri'])&(rr<=b['Ro'])
                best=np.where(ok,t,best); bb=np.where(ok,ib,bb); nrm[ok]=[0,0,sgn]
            for R,out in ((b['Ro'],1.),(b['Ri'],-1.)):
                B=rx*dx+ry*dy; C=rx*rx+ry*ry-R*R; D=B*B-A*C
                sq=np.sqrt(np.maximum(D,0))
                for root in (-1,1):
                    with np.errstate(divide='ignore',invalid='ignore'):
                        t=(-B+root*sq)/A
                    ok=(D>0)&(t>1e-9)&(t<best)&(np.abs(rz+t*dz)<=H)
                    best=np.where(ok,t,best); bb=np.where(ok,ib,bb)
                    if ok.any():
                        px=(rx+t*dx)[ok]; py=(ry+t*dy)[ok]
                        nrm[ok]=np.c_[out*px/R,out*py/R,0*px]
        hit=np.isfinite(best)
        if not hit.all():
            pos,vel,rg,ids,best,bb,nrm,dd=[z[hit] for z in (pos,vel,rg,ids,best,bb,nrm,dd)]
        if len(ids)==0: break
        pos=pos+best[:,None]*dd
        vn=(vel*nrm).sum(1); an=np.abs(vn)
        w1=w[rg]; other=np.where(rg==0,bb+1,0); w2=w[other]
        k2=an**2-2*(w2-w1); tir=k2<=0; k=np.sqrt(np.maximum(k2,0))
        R=np.where(tir,1.,((an-k)/(an+k+1e-300))**2)
        refl=tir|(rng.random(len(ids))<R)
        vnew=vel.copy()
        vr=vel-2*vn[:,None]*nrm
        vt=vel-vn[:,None]*nrm+(np.sign(vn)*k)[:,None]*nrm
        vnew=np.where(refl[:,None],vr,vt)
        if diffuse>0:
            dm=refl&(rg==0)&(rng.random(len(ids))<diffuse)
            if dm.any():
                n=nrm[dm]; s=np.sqrt((vel[dm]**2).sum(1))
                c=np.sqrt(rng.random(dm.sum())); phi=2*np.pi*rng.random(dm.sum()); sn=np.sqrt(1-c*c)
                e1=np.cross(n,[.31,.52,.79]); e1/=np.sqrt((e1*e1).sum(1))[:,None]; e2=np.cross(n,e1)
                vnew[dm]=s[:,None]*(c[:,None]*n+(sn*np.cos(phi))[:,None]*e1+(sn*np.sin(phi))[:,None]*e2)
        dvz=vel[:,2]-vnew[:,2]
        np.add.at(per,(ids,bb),dvz)
        rg=np.where(refl,rg,other); vel=vnew; nbounce[ids]+=1
        pos=pos+1e-7*vel/np.sqrt((vel*vel).sum(1))[:,None]
    tally=per*sp[:,None]
    # returned quantity: pi Rb^2 <|v| dv_z>/M  -> acceleration with rho_chi
    mean=tally.mean(0); err=tally.std(0)/np.sqrt(N)
    conv=RHO_GEV*GEVCM3*np.pi*(Rb*1e-3)**2*1e6   # km/s^2 -> m^2/s^2 ; a = rho pi Rb^2 <..>/M
    Ms=np.array([b['M'] for b in bodies])
    return conv*mean/Ms, conv*err/Ms, nbounce.mean(), per, sp, conv/Ms
def can_entry(x,d,h):
    """first intersection of rays with a closed cylinder can, returns t, outward normal"""
    N=len(x); best=np.full(N,np.inf); nrm=np.zeros((N,3)); rx,ry,rz=x.T; dx,dy,dz=d.T
    for s in (1,-1):
        with np.errstate(divide='ignore',invalid='ignore'):
            t=(s*h['H']-rz)/dz
        ok=(t>0)&(t<best)&(np.hypot(rx+t*dx,ry+t*dy)<=h['R'])
        best=np.where(ok,t,best); nrm[ok]=[0,0,s]
    A=dx*dx+dy*dy; B=rx*dx+ry*dy; C=rx*rx+ry*ry-h['R']**2; D=B*B-A*C; sq=np.sqrt(np.maximum(D,0))
    with np.errstate(divide='ignore',invalid='ignore'):
        t=(-B-sq)/A
    ok=(D>0)&(t>0)&(t<best)&(np.abs(rz+t*dz)<=h['H'])
    best=np.where(ok,t,best)
    if ok.any():
        nrm[ok]=np.c_[(rx+t*dx)[ok]/h['R'],(ry+t*dy)[ok]/h['R'],0*t[ok]]
    return best,nrm
def harmonic(geom,u,sign=+1,N=1000000,nth=6,seed=1,**kw):
    """first-harmonic amplitude a1 = (2/pi) Int_0^pi a(theta) cos(theta) dtheta of the axial acceleration when the wind rotates in a plane through the axis.
    a(pi-theta) = -a(theta) for a mirror-symmetric geometry, so a1 = (4/pi) Int_0^{pi/2}. Gauss-Legendre in theta."""
    rng=np.random.default_rng(seed); x,wt=np.polynomial.legendre.leggauss(nth); th=(x+1)*np.pi/4; wt=wt*np.pi/4
    a=[];e=[]
    for t in th:
        m,s,*_=trace(geom,u*u,t,N,rng,sign=sign,**kw); a.append(m); e.append(s)
    a=np.array(a); e=np.array(e)
    a1=(4/np.pi)*np.sum(wt[:,None]*a*np.cos(th)[:,None],axis=0); e1=(4/np.pi)*np.sqrt(np.sum((wt[:,None]*e*np.cos(th)[:,None])**2,axis=0))
    return a1,e1,th,a
