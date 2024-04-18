import matplotlib.pyplot as plt

class Oscillator:
    def __init__(self,m,k,x0,v0,dt=0.01):
        self.m=m
        self.k=k
        self.x0=x0
        self.v0=v0
        self.dt=dt

        self.t=[0]
        self.x=[self.x0]
        self.v=[self.v0]
        self.a=[-self.k/self.m*self.x0]

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)
        self.a.append(-self.k/self.m*self.x[-1])

    def move(self,t0=2):
        while self.t[-1]<=t0:
            self.__move()
        self.t.pop()
        self.x.pop()
        self.v.pop()
        self.a.pop()
        return self.t, self.x
    
    def plot(self):
        plt.subplot(1,3,1)
        plt.title('x-t')
        plt.xlabel('t/s')
        plt.ylabel('x/m')
        plt.plot(self.t,self.x)        
        
        plt.subplot(1, 3, 2)
        plt.title('v-t')
        plt.xlabel('t/s')
        plt.ylabel('v/ms^-1')
        plt.plot(self.t,self.v)        
        
        plt.subplot(1,3,3)
        plt.title('a-t')
        plt.xlabel('t/s')
        plt.ylabel('a/ms^-2')
        plt.plot(self.t,self.a)
        plt.show()

    def period(self):
        for xi in self.x:
            if xi+self.x0 < 1/100000000:
                return 2*self.t[self.x.index(xi)]