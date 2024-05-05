import ss
import matplotlib.pyplot as plt
s=ss.SolarSystem()
s.start()
s.move()

plt.plot(s.x_z,s.y_z,label='Zemlja')
plt.plot(s.x_s,s.y_s,label='Sunce',marker='o',markersize=15)

plt.title('Gibanje Zemlje i Sunca')
plt.xlabel('x[m]')
plt.ylabel('y[m]')

plt.legend()
plt.show()