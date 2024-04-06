import particle as prt
import numpy as np
import matplotlib.pyplot as plt

dt=0.001
pogreske=[]
t=[]
while dt <= 0.1:
    p=prt.Particle(10,60,0,0,dt)
    pog=100*np.abs(p.range()-p.range_analiticki())/p.range_analiticki()
    pogreske.append(pog)
    t.append(dt)
    dt+=0.0001

plt.xlabel("dt [s]")
plt.ylabel("Pogreška [%]")
plt.plot(t,pogreske)
plt.show() 