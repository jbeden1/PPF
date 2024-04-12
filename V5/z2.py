import numpy as np
import calculus as calc
import matplotlib.pyplot as plt

def fja(x):
    return 2*x**2 + 3

gornja = []
donja = []
trapez = []
preciznost = np.arange(100, 1000, 50)

for i in preciznost:
    gornja.append(calc.pravokutna_int(fja, 0, 1, i)[0])
    donja.append(calc.pravokutna_int(fja, 0, 1, i)[1])
    trapez.append(calc.trapez_int(fja, 0, 1, i))


plt.xlabel("N")
plt.ylabel("Integral")
plt.hlines(y=11/3, xmin=100, xmax=900)
plt.scatter(preciznost, trapez, label = "Metoda trapeza")
plt.scatter(preciznost, gornja, label = "Gornja integralna suma")
plt.scatter(preciznost, donja, label = "Donja integralna suma")
plt.legend()
plt.show()
