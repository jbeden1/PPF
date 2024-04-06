import numpy as np
class Particle:
    def __init__(self,v0,kut_otklona,x,y,dt=0.01):
        self.v0=v0
        self.kut_otklona=np.radians(kut_otklona)
        self.x=x
        self.y=y
        self.dt=dt
    
    def reset(self):
        self.v0=0
        self.kut_otklona=0
        self.x=0
        self.y=0

    def __move(self):
        i=len(self.v_x)-1
        self.x2.append(self.x2[i]+self.v_x[i]*self.dt)
        self.y2.append(self.y2[i]+self.v_y[i]*self.dt)
        self.v_x.append(self.v0_x)
        self.v_y.append(self.v_y[i]-9.81*self.dt)
        self.vrijeme.append(self.dt)

    def range_analiticki(self):
        return(2*self.v0*np.cos(self.kut_otklona)*self.v0*np.sin(self.kut_otklona)/9.81)
    
    def range(self):
        self.v_x=[]
        self.v_y=[]
        self.v0_x=self.v0*np.cos(self.kut_otklona)
        self.v0_y=self.v0*np.sin(self.kut_otklona)-9.81*self.dt
        self.v_x.append(self.v0_x)
        self.v_y.append(self.v0_y)

        self.x2=[]
        self.y2=[]
        self.x0=self.v0_x*self.dt
        self.y0=self.v0_y*self.dt
        self.x2.append(self.x0)
        self.y2.append(self.y0)
        self.vrijeme=[]

        while self.y2[-1]>=0:
            self.__move()
        return self.x2[-1]