# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:38:52 2017

@author: lmoraes
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x*x-20
    
def df(x):
    return 2*x

chute=100 
epsilon=0.001

t = np.arange(-chute, chute, 0.01)
s = f(t)

fig = plt.figure()
#ax1 = fig.add_subplot(111)
ax1 = plt.axes(xlim=(-100, 100), ylim=(0, 10000))
line, = ax1.plot([], [], c='b')
line2, = ax1.plot([], [], c='r')
pts, = ax1.plot([], [], 'o', c='b')
x_init = 100

def calculate_x(x):
    x_list = [x]
    fx_list = [f(x)]
    i=0
    while (i<102):
        x_next = x-f(x)/df(x)
        x_list.append(x_next)
        fx_list.append(f(x_next))
        x = x_next
        i+=1
    return x_list, fx_list

x_list, fx_list = calculate_x(x_init)

def init():
    #ax1.scatter(x, 0,c='b')
    #ax1.scatter(x, f(x),c='b')
    #line.set_data([], [])
    #line.set_data([x_list[i], x_list[i]], [0, f(x_list[i])])
    #line2.set_data([], [])
    #return [line, line2]
    return [line, line2]

#while(np.abs(x_next-x)>epsilon):

xdata = []
ydata = []
ptdata = []

def animate(i):
    #ax1.scatter(x, 0,c='b')
    #ax1.scatter(x, f(x),c='b')
    xdata.append(x_list[i])
    xdata.append(x_list[i])
    ydata.append(0)
    ydata.append(fx_list[i])
    
    line.set_data(xdata, ydata)
    line2.set_data(t, s)
    pts.set_data(xdata, ydata)
        
    fig.canvas.draw()
    #
    #plt.draw()
    #plt.show() 
    #print("%64.30f" % x|)
    #x=x_next
    #i+=1
    #plt.pause(0.5)
    #ax1.view_init(30, 0.3 * i)
    #return [line, line2] 
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                        frames=5, interval=200, blit=True, repeat=False)    
    
#plt.show()
    
#t = np.arange(-chute, chute, 0.01)
#s = f(t)
#ax1.plot(t, s,c='r')