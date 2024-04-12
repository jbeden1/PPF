import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def fja(x):
   f = 5*x**3-2*x**2+2*x+3
   return f

eps1 = calc.der_raspon(fja, -2, 2, h = 0.01)
plt.plot(eps1[0], eps1[1], label = "eps = 0.01")
plt.title("Derivacija")
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.legend()
plt.show()

eps2 = calc.der_raspon(fja, -2, 2, h = 0.1)
plt.plot(eps2[0], eps2[1], label = "eps = 0.1")
plt.title("Derivacija")
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.legend()
plt.show()

tocke = np.arange(-2, 2, 0.1)
analiticka_derivacija = 5*3*tocke**2-2*2*tocke+2

plt.plot(tocke, analiticka_derivacija, label = "analitičko rješenje")
plt.title("Derivacija")
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.legend()
plt.show()