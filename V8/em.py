import numpy as np
import matplotlib.pyplot as plt

class Field:
    def __init__(self,q,m,E,B,v0,dt):
        self.q=q
        self.m=m
        self.E=E
        self.B=B
        self.v0=v0
        self.dt=dt

    def start(self):
        self.t=[0]
        self.r=[[0,0,0]]
        self.v=self.v0
        self.x=[0]
        self.y=[0]
        self.z=[0]

    def __move(self):
        self.a=self.q*(self.E+np.cross(self.v,self.B))/self.m
        self.v+=self.a*self.dt
        self.r.append(self.r[-1]+self.v*self.dt)
        self.x.append(self.r[-1][0])
        self.y.append(self.r[-1][1])
        self.z.append(self.r[-1][2])
        self.t.append(self.t[-1]+self.dt)

    def move_euler(self,T0=20):
        self.start()
        while self.t[-1]<=T0:
            self.__move()
        return self.x,self.y,self.z

    def __move_rk4(self):
        k1v=self.q*(self.E+np.cross(self.v,self.B))/self.m*self.dt
        k1=self.v*self.dt
        k2v=self.q*(self.E+np.cross((self.v+k1v/2),self.B))/self.m*self.dt
        k2=(self.v + k1v/2)*self.dt  
        k3v=self.q*(self.E+np.cross((self.v+k2v/2),self.B))/self.m*self.dt
        k3=(self.v+k2v/2)*self.dt
        k4v=self.q*(self.E+np.cross((self.v+k3/2),self.B))/ self.m*self.dt
        k4=(self.v + k3v/2)*self.dt

        self.v+=(k1v+2*k2v+2*k3v+k4v)/6
        self.r.append(self.r[-1]+(k1+2*k2+2*k3+k4)/6)
        self.x.append(self.r[-1][0])
        self.y.append(self.r[-1][1])
        self.z.append(self.r[-1][2])
        self.t.append(self.t[-1]+self.dt)

    def move__rk(self,T0=20):
        self.start()
        while self.t[-1]<=T0:
            self.__move_rk4()
        return self.x,self.y,self.z