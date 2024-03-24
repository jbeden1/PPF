import numpy as np
import matplotlib.pyplot as plt
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]          
fi=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]   
xy=[]
x2=[]
y2=[]
y=[]

for i in range(6):
    xy.append(M[i]*fi[i])
    
for i in range(6):
    x2.append(fi[i]**2)

for i in range(6):
    y2.append(M[i]**2)

a=np.average(xy)/np.average(x2)
devi=np.sqrt(1/6*(np.average(y2)/np.average(x2) - a**2))
print("Modul torzije iznosi {} +/- {}".format(a, devi))
plt.scatter(fi, M)
for i in range(6):
    y.append(fi[i]*a)
plt.plot(fi, y)
plt.show()
