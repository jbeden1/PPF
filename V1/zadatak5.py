import matplotlib.pyplot as plt
import numpy as np

def pravac(xa, ya, xb, yb):
    k=(yb - ya) / (xb - xa)
    l=ya - xa * k
    print("y = {}x + {}".format(k, l))

    xs=np.linspace(-5, 5, 20)
    ys= k * xs + l

    plt.title("Pravac")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.plot(xs,ys)
    plt.plot(xa,ya, marker="o")
    plt.plot(xb,yb, marker="o")
    
    opt = input("Spremi graf (S) ili Prikaži graf (P): ")
    if opt=="P":
        plt.show()
    elif opt=="S":
        name=input("Upišite ime pod kojim ćete spremiti graf: ")
        name += ".pdf"
        plt.savefig(name)
    else:
        print("Greška!")

pravac(1, 2, 4, 8)