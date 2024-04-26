import matplotlib.pyplot as plt
import projectile as pro

for dt_i in [0.1,0.01,0.001]:
    pr=pro.Projectile(0.1,20,60,dt_i)
    pr.gibanje_euler()
    plt.plot(pr.x,pr.y,label='dt={}'.format(dt_i))

pr_rk4=pro.Projectile(0.1,20,60,0.01)
pr_rk4.gibanje_rk4()
plt.plot(pr_rk4.x,pr_rk4.y,label='dt=0.01 Runge kutta')

plt.title('x-y')
plt.xlabel('x / m')
plt.ylabel('y / m') 
plt.legend()
plt.show()