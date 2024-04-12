import numpy as np
def der_tocka(fja, tocka, method = 3, h = 0.001):
    if method == 2:
        return (fja(tocka + h) - fja(tocka))/h
    if method == 3:
        return (fja(tocka + h) - fja(tocka - h))/(2*h)

def der_raspon(fja, x1, x2, method = 3, h = 0.001):
    tocke = np.linspace(x1, x2, 10000)
    der = der_tocka(fja, tocke)
    return tocke, der

def pravokutna_int(f, a, b, n):
    x = np.linspace(a, b, n)
    gornja_suma = 0
    donja_suma = 0
    dx = (b - a)/n
    for i in range(n):
        gornja_suma += f(x[i] + dx)*dx
        if x[i] <= b - dx:
            donja_suma += f(x[i])*dx
    return gornja_suma, donja_suma

def trapez_int(f, a, b, n):
    x = np.linspace(a, b, n)
    integral = 0
    dx = (b - a)/n
    for i in range(1, n):
        integral += f(x[i-1]) 
    integral += (f(a) + f(b))/2
    integral = integral * dx
    return integral
