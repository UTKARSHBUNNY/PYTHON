import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,pi

u=input("INITIAL PROJECTILE VELOCITY (IN m/s)-->")
u=float(u)

g=9.81
angle=input("PROJECTILE ANGLE (IN DEGREES)-->")
deg=angle
angle=float(angle)
angle=(angle*pi)/180   
Vx=u*cos(angle)
Vy=u*sin(angle)        

total_time=(2*Vy)/g
print("TOTAL TIME OF PROJECTILE-->"+str(total_time)+"s")
t=np.linspace(0,total_time,150)
sx=Vx*t
sy=(Vy*t)-(0.5*g*t*t)
range=Vx*total_time
print("RANGE OF PROJECTILE-->"+str(range)+"m")

plt.figure(figsize=(20,15))
plt.plot(sx,sy,label=r'$\theta={}$'.format(deg))
plt.xlabel("DISTANCE IN METRES m")
plt.ylabel("DISTANCE IN METRES m")
plt.grid()
plt.legend()   
plt.show()








