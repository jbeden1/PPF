import numpy as np
import matplotlib.pyplot as plt
class Projectile:
    def __init__(self, x0, y0, v0, kut_otklona, dt):
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.kut_otklona=np.radians(kut_otklona)
        self.dt=dt
        self.x=[self.x0]
        self.y=[self.y0]
        self.vx=[self.v0*np.cos(self.kut_otklona)]
        self.vy=[self.v0*np.sin(self.kut_otklona)]

    def __move(self):
        self.vx.append(self.v0*np.cos(self.kut_otklona))
        self.vy.append(self.vy[-1]-9.81*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('Gibanje projektila')
        #plt.show()

    def max_height(self):  
        H=0
        l=len(self.y)
        for hi in range(l):
            if self.y[hi]>H:
                H=self.y[hi]
        return H

    def range(self):
        while self.y[-1]>=0:
            self.__move()
        return self.x[-1]
    
    def max_velocity(self):
        v_max_x = self.vx[0]
        v_max_y = 0
        for vy_i in self.vy:
            if np.abs(vy_i)>=v_max_y: 
                v_max_y=np.abs(vy_i)
        return np.sqrt(v_max_x**2+v_max_y**2)
    
    def meta(self, xm, ym, r):
        kut = np.linspace(0,2*np.pi,10000)
        xk = xm + r*np.cos(kut)
        yk= ym + r*np.sin(kut)
        xp=[]
        yp=[]

        while (self.x[-1]-xm)**2+(self.y[-1]-ym)**2 > r**2 and self.y[-1] >= 0:
                self.__move()
                xp.append(self.x[-1])
                yp.append(self.y[-1])

        udaljenosti = []
        for i in range(len(self.x)):
            udaljenosti.append(np.sqrt((self.x[i]-xm)**2+(self.y[i]-ym)**2))
        min_udaljenost = min(udaljenosti)
        if (min_udaljenost- r) < 0.01:
            print('Meta je pogođena')
        else:
            print('Meta nije pogođena')
            print('Najmanja udaljenost između mete i projektila iznosi {} m'.format(min(udaljenosti) - r))
        
        print('Meta radijusa r = {} m nalazi na koordinatama ({} m, {} m). Domet projektila do sudara iznosi {} m'.format(r, xm, ym, self.x[-1]))
        plt.plot(xk, yk)
        plt.plot(xp, yp)
        plt.grid()
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('Projektil i meta')
        plt.axis('equal')
        plt.show()
