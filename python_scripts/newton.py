import matplotlib.pyplot as plt
import numpy as np
#import time

def f(x):
    return x*x-20
    
def df(x):
    return 2*x

chute=100 
epsilon=0.001

x=chute

fig = plt.figure()
ax1 = fig.add_subplot(111)
i=0
plt.ion()
#while(np.abs(x_next-x)>epsilon):
while(i<10):
    x_next=x-f(x)/df(x)
    ax1.scatter(x, 0,c='b')
    ax1.scatter(x, f(x),c='b')
    ax1.plot([x, x], [0, f(x)],c='b')
    ax1.plot([x, x_next], [f(x), 0],c='b')
    plt.draw()
    #plt.show() 
    #print("%64.30f" % x)
    x=x_next
    i+=1
    plt.pause(0.5)

t = np.arange(-chute, chute, 0.01)
s = f(t)
ax1.plot(t, s,c='r')
    
   
    
