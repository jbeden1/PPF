print("Unesite (x,y) koordinate za dvije točke: ")

try:
    print("Točka A: ")
    xa = int(input("x = "))
    ya = int(input("y = "))

    print("Točka B: ")
    xb = int(input("x = "))
    yb = int(input("y = "))

except:
    print("Niste unijeli broj. Pokušajte ponovno!")
    print("Točka A: ")
    xa = int(input("x = "))
    ya = int(input("y = "))

    print("Točka B: ")
    xb = int(input("x = "))
    yb = int(input("y = "))

k = (yb - ya) / (xb - xa)
l = ya - xa * k
print("y = {}x + {}".format(k, l))
