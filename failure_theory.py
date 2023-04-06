import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,pi

Yield_strength=float(input("YIELD STRENGTH OF THE MATERIAL--->"))
s1=float(input("STRESS IN DIRECTION 1--->"))
s2=float(input("STRESS IN DIRECTION 2--->"))
Vms=np.sqrt((s1*s1)-(s1*s2)+(s2*s2))     #Von-Mises Stress


a=np.sqrt(2)*Yield_strength             #semi major axis of ellipse
b=np.sqrt(2/3)*Yield_strength           #semi minor axis of ellipse

st1=[]
st2=[]

tn=int(input(("NUMBER OF POINTS ON THE 2-D BODY--->")))

print("Stress values for"+str(tn)+"points in direction 1--->")
for i in range (tn):
    st1.append(float(input()))

print("Stress values for"+str(tn)+"points in direction 2--->")

for j in range (tn):
    st2.append(float(input()))


theta=np.linspace(0,2*pi,720)

x=a*cos(theta)
y=b*sin(theta)

root_ang=pi/4

xd=x*cos(root_ang)-y*sin(root_ang)
yd=x*sin(root_ang)+y*cos(root_ang)


lx1=[-200,200]
ly1=[0,0]

lx2=[0,0]
ly2=[-200,200]

xp=[Yield_strength,Yield_strength,0,-Yield_strength,-Yield_strength,0,Yield_strength]
yp=[0,Yield_strength,Yield_strength,0,-Yield_strength,-Yield_strength,0]
plt.figure(figsize=(7.5,5))
plt.scatter(st1,st2)
plt.plot(xp,yp,linestyle='--',label='Max Shear Region')
plt.plot(lx1,ly1,linestyle='--',color='black')
plt.plot(lx2,ly2,linestyle='--',color='black')
plt.plot(xd,yd,label="Von-Mises Reion")
plt.legend()
plt.show()

