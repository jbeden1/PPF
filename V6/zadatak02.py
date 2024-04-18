import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as ho

x0=0.1
v0=0
k=10
m=0.1

t_an=np.linspace(0,2,10000)
x_an=x0*np.cos(np.sqrt(k/m)*t_an)
plt.plot(t_an, x_an, label = 'analitičko')
print('Analitički period je {} s'.format(2*np.pi*np.sqrt(m/k)))

for dti in [0.001, 0.01, 0.05]:
    hoi=ho.Oscillator(m,k,x0,v0,dti)
    t,x=hoi.move()
    print('Numerički period za dt = {0} je {1} s'.format(dti, hoi.period()))
    plt.scatter(t,x,label='dt = {}'.format(dti),s=dti*100)
    
plt.xlabel("t / s")
plt.ylabel("x / m")
plt.legend()
plt.show()