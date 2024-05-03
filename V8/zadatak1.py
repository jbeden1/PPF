import em
import numpy as np
import matplotlib.pyplot as plt

E=np.array((0,0,0))
B=np.array((0,0,1))
ve=np.array((0.1,0.1,0.1))
vp=np.array((0.1,0.1,0.1))
q=1
m=1

electron=em.Field(-q,m,E,B,ve,0.001)
positron=em.Field(q,m,E,B,vp,0.001)

ax=plt.axes(projection='3d')

x1,y1,z1=electron.move_euler()
x2,y2,z2=positron.move_euler()

ax.plot3D(x1,y1,z1,label='electron')
ax.plot3D(x2,y2,z2,label='positron')

plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()

ax=plt.axes(projection='3d')
ve1=np.array((0.1,0.1,0.1))
ve2=np.array((0.1,0.1,0.1))

electron1=em.Field(-q,m,E,B,ve1,0.01)
x1,y1,z1=electron1.move_euler()

electron2=em.Field(-q,m,E,B,ve2,0.01)
x2,y2,z2=electron2.move__rk()

ax.plot3D(x1,y1,z1,label='Euler, dt=0.01')
ax.plot3D(x2,y2,z2,label='Runge-kutta, dt=0.01')

plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()