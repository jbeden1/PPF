import particle as prt
import numpy as np

p = prt.Particle(10,60,0,0)

print("Numerički domet iznosi {} m".format(p.range()))
print("Analitički domet iznosi {} m".format(p.range_analiticki()))
print("Pogreška za domet iznosi {} %".format(np.abs(p.range()/p.range_analiticki()-1)*100))