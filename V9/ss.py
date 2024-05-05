import numpy as np
G=6.67408e-11
m_s=1.989e30
m_z=5.9742e24

class SolarSystem:
    def __init__(self,year=365.242*24*3600,dt=3600):
        self.year=year
        self.dt=dt

    def start(self):
        self.t=0
        self.x_z=[1.486e11]
        self.y_z=[0]    
        self.x_s=[0]
        self.y_s=[0]   
        self.vx_z=0 
        self.vy_z=29783
        self.vx_s=0 
        self.vy_s=0
        self.ax_z=-G*m_s*(self.x_s[-1]-self.x_z[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ay_z=-G*m_s*(self.x_s[-1]-self.x_z[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ax_s=G*m_z*(self.x_z[-1]-self.x_s[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ay_s=G*m_z*(self.x_z[-1]-self.x_s[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3

    def __move(self):
        self.vx_z+=self.ax_z*self.dt
        self.vy_z+=self.ay_z*self.dt        
        self.vx_s+=self.ax_s*self.dt
        self.vy_s+=self.ay_s*self.dt
        self.x_z.append(self.x_z[-1]+self.vx_z*self.dt)
        self.y_z.append(self.y_z[-1]+self.vy_z*self.dt)
        self.x_s.append(self.x_s[-1]+self.vx_s*self.dt)
        self.y_s.append(self.y_s[-1]+self.vy_s*self.dt)
        self.ax_z=G*m_s*(self.x_s[-1]-self.x_z[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ay_z=G*m_s*(self.y_s[-1]-self.y_z[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ax_s=-G*m_z*(self.x_z[-1]-self.x_s[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.ay_s=-G*m_z*(self.y_z[-1]-self.y_s[-1])/(np.sqrt((self.x_s[-1]-self.x_z[-1])**2+(self.y_s[-1]-self.y_z[-1])**2))**3
        self.t+=self.dt
        
    def move(self):
        while self.t <=self.year:
            self.__move()