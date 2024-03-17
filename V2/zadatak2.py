import numpy as np
import matplotlib.pyplot as plt
v0=int(input("iznos početne brzine: "))
kut=int(input("iznos kuta otklona u stupnjevima: "))
t=10
vremena=np.linspace(0, t, 10000)
delta_t=t/10000
kut=kut*np.pi/180
g=9.81
v_x=[]
v_y=[]
v0_x=v0 * np.cos(kut)
v0_y=v0 * np.sin(kut) - g*delta_t
v_x.append(v0_x)
v_y.append(v0_y)
for i in range(1,10000):
    v_x.append(v0_x)
    v_y.append(v_y[i-1] - g*delta_t)

x=[]
y=[]
x0=v0_x*delta_t
y0=v0_y*delta_t
x.append(x0)
y.append(y0)
for i in range(1,10000):
    x.append(x[i-1] + v_x[i]*delta_t)
    y.append(y[i-1] + v_y[i]*delta_t)

plt.subplot(1,3,1)
plt.title("x-y graf")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.plot(x, y)

plt.subplot(1,3,2)
plt.title("x-t graf")
plt.xlabel("x [m]")
plt.ylabel("t [s]")
plt.plot(vremena, x)

plt.subplot(1,3,3)
plt.title("y-t graf")
plt.xlabel("y [m]")
plt.ylabel("t [s]")
plt.plot(vremena, y)
plt.show()