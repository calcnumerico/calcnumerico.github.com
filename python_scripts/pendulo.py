import matplotlib.pyplot as plt
import numpy as np
#import time

h=0.1 #numero de intervalos
q=np.pi/3.0
v=2
n=30
g=10
L=10

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

for k in np.arange(0,n):
    q_next=q+h*v
    v_next=v-h*((g/L)*np.sin(q))
    #ax1.scatter(q_next,v_next,c='b')
    ax2.plot([0, L*np.sin(q)], [0, L*np.cos(q)],c='b')
    v=v_next
    q=q_next
