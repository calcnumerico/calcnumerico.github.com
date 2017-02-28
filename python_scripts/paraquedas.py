import matplotlib.pyplot as plt
import numpy as np
#import time

dt=1 #tamanho do passo de tempo
t_final=200
g=9.81 # m/s^2
k=15 # resistencia do ar kg/s de queda livre
m=90 # kilos
v_0=0 #velocidade inicial
y_0=2000 #altura incial

def f(v): # dv é uma função de 
    return g-k*v/m


fig1 = plt.figure()
ax1 = fig1.add_subplot(111) 

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

v=v_0
y=y_0
t=0

#antes de abrir paraquedas
while(y>500):

    y_next = y - dt*v
    v_next = v + dt*f(v)
    ax2.plot([t, t+dt], [v, v_next],c='b')
    ax1.scatter(0,y_next,c='b')
    y=y_next
    v=v_next
    t=t+dt

#depois de abrir paraquedas e antes de cair no chao
k=200 # resistencia do ar com um paraquedas
while(y>0):
    y_next = y - dt*v
    v_next = v + dt*f(v)
    ax2.plot([t, t+dt], [v, v_next],c='b')
    ax1.scatter(0,y_next,c='b')
    y=y_next
    v=v_next
    t=t+dt

print("t= ",t)
print("v= ",v)
print("y= ",y)