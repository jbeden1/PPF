import modul as pr
import matplotlib.pyplot as plt
projektil = pr.Projectile(0, 0, 10, 45, 0.001)

domet = projektil.range()
max_visina = projektil.max_height()
max_brzina = projektil.max_velocity()
print("Domet projektila iznosi {} m".format(domet))
print("Maksimalna visina projektila iznosi {} m".format(max_visina))
print("Maksimalna brzina projektila iznosi {} m \ s".format(max_brzina))
#projektil.plot_trajectory()

projektil_meta = pr.Projectile(0, 0, 10, 45, 0.001)
projektil_meta.meta(5.095,2.5449,0.1)

projektil2 = pr.Projectile(0, 0, 10, 45, 0.001)
projektil2.range()
projektil3 = pr.Projectile(0, 0, 10, 45, 0.005)
projektil3.range()
projektil4 = pr.Projectile(0, 0, 10, 45, 0.01)
projektil4.range()
plt.plot(projektil2.x, projektil2.y, label = "dt=0.001 s")
plt.plot(projektil3.x, projektil3.y, label = "dt=0.005 s")
plt.plot(projektil4.x, projektil4.y, label = "dt=0.01 s")
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Gibanje projektila')
plt.legend()
plt.show()