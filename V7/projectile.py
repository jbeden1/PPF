import numpy as np
g=9.81
class Projectile:
    def __init__(self,m,v0,kut,dt=0.01,ro=1.29,Cd=0.2,A=0.1):
        self.m=m
        self.v0=v0
        self.kut=kut*np.pi/180
        self.dt=dt
        self.ro=ro
        self.Cd=Cd
        self.A=A

        self.r=self.ro*self.Cd*self.A/(2*self.m)

        self.t=[0]
        self.x=[0]
        self.y=[0]
        self.vx=[self.v0 * np.cos(self.kut)]
        self.vy=[self.v0 * np.sin(self.kut)]
        self.ax=[-np.sign(self.vx[0]) * self.r * (self.vx[0])**2]
        self.ay=[-g - np.sign(self.vy[0]) * self.r * (self.vy[0])**2]

    def __move_euler(self):
        self.t.append(self.t[-1]+self.dt)
        self.ax.append(-np.sign(self.vx[-1])*self.r*(self.vx[-1])**2)
        self.ay.append(-g - np.sign(self.vy[-1])*self.r*(self.vy[-1])**2)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)        
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)

    def gibanje_euler(self):
        while self.y[-1] >=0:
            self.__move_euler()

    def a(self, v):
        av=-np.sign(v)*self.r*(v**2)
        return av

    def __move_rk4(self):
        k1vx=self.a(self.vx[-1])*self.dt
        k1x=self.vx[-1]*self.dt
        k2vx=self.a(self.vx[-1]+k1vx/2)*self.dt
        k2x=(self.vx[-1]+k1vx/2)*self.dt  
        k3vx=self.a(self.vx[-1]+k2vx/2)*self.dt
        k3x=(self.vx[-1]+k2vx/2)*self.dt
        k4vx=self.a(self.vx[-1]+k3vx/2)*self.dt
        k4x=(self.vx[-1]+k3vx/2)*self.dt

        self.vx.append(self.vx[-1]+(k1vx+2*k2vx+2*k3vx+k4vx)/6)
        self.x.append(self.x[-1]+(k1x+2*k2x+2*k3x+k4x)/6)

        k1vy=(-g+self.a(self.vy[-1]))*self.dt
        k1y=self.vy[-1]*self.dt
        k2vy=(-g+self.a(self.vy[-1]+k1vy/2))*self.dt
        k2y=(self.vy[-1]+k1vy/2)*self.dt  
        k3vy=(-g+self.a(self.vy[-1]+k2vy/2))*self.dt
        k3y=(self.vy[-1]+k2vy/2)*self.dt
        k4vy=(-g+self.a(self.vy[-1]+k3vy/2))*self.dt
        k4y=(self.vy[-1]+k3vy/2)*self.dt

        self.vy.append(self.vy[-1]+(k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.y.append(self.y[-1]+(k1y + 2*k2y + 2*k3y + k4y)/6)

        self.t.append(self.t[-1]+self.dt)

    def gibanje_rk4(self):
        while self.y[-1]>=0:
            self.__move_rk4()