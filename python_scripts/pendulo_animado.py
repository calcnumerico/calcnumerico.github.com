# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:59:46 2017

@author: lmoraes
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

h=0.1 #numero de intervalos
q=np.pi/3.0
v=0.3
n=200
g=-10
L=10

fig = plt.figure(figsize=(5,5))
#ax1 = fig.add_subplot(111)
ax1 = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax1.plot([], [], c='b')
pts, = ax1.plot([], [], 'o', c='b')

def calculate_q(q, v, n, g, L):
    q_list = []
    for k in np.arange(0,n):
        q_next=q+h*v
        v_next=v-h*((g/L)*np.sin(q_next))
        q_list.append(q)
    #ax1.scatter(q_next,v_next,c='b')
    #ax2.plot([0, L*np.sin(q)], [0, L*np.cos(q)],c='b')
        v=v_next
        q=q_next
    return q_list
        
q_list = calculate_q(q, v, n, g, L)

def init():
    return line,pts

def animate(i):
    line.set_data([0, L*np.sin(q_list[i])], [0, L*np.cos(q_list[i])])
    pts.set_data(L*np.sin(q_list[i]), L*np.cos(q_list[i]))
    fig.canvas.draw()
    return line,pts
    
ani = animation.FuncAnimation(fig, animate, init_func=init,
                        frames=n, interval=100, blit=True)