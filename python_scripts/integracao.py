import matplotlib.pyplot as plt
import numpy as np
#import time

def f(x):
    return x*x*x*x*x+x*x*x-12*x*x-3*x+4


a=-2 #limite inferior de integracao
b=2 #limite superior de integracao
h=0.6 #numero de intervalos




fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([a, b], [0, 0],c='g')

soma=0
for x in np.arange(a,b,h):
    soma=soma+h*(f(x)+f(x+h))/2

    ax1.plot([x, x], [0, f(x)],c='b')
    ax1.plot([x, x+h], [f(x), f(x+h)],c='b')



ax1.plot([b, b], [0, f(b)],c='b')
real = (b*b*b*b/4.0- a*a*a*a/4.0)
erro = np.abs(real - soma)
print(soma)
print(real)
print(erro)

    
    
t = np.arange(a-1,b+1, 0.01)
s = f(t)
#ax1.plot(t, s,c='r')
    
   
    
