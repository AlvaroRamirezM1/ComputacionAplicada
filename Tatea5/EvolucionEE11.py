import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x,y,z):
    f = x + 2*y + y*z -x**2 - y**2 - z**2
    return f
    
def evol(u,v,w):
    plt.figure(3)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x','y','z'))
    plt.ylim([-2, 2])
    plt.show()

def mutation(x,s):
    xn = x+s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x+s*gauss(0,1)
    return xn

def sigma(s,g,m):
    ps = m/g
    c = 0.817
    if g%10 == 0:
    #if True:
        if ps > 0.2:
            s = s/c
        elif ps < 0.2:
            s = s*c
        else:
            s = s
    else:
        s = s
    return s
    
def main():
  
    xmin, xmax, ymin, ymax ,zmin, zmax= [-2, 2, -2, 2, -2, 2]
    gmax = 500;           #máximo número de iteraciones
    m = 0;                 #número de mutaciones exitosas
    c = 0.817;
    x = 4*random()+xmin
    y = 4*random()+ymin
    z = 4*random()+zmin
    x0y0z0 = [round(x,6), round(y,6), round(z,6)]
    print("x0,y0,z0: ",x0y0z0)
    padre = f(x,y,z)
    s = 1
    u = [x]
    v = [y]
    w = [z]
    
    for g in range(1,gmax):
        xn = mutation(x,s)
        yn = mutation(y,s)
        zn = mutation(z,s)
        hijo = f(xn,yn,zn)
        if hijo > padre:
            x = xn
            y = yn
            z = zn
            m += 1               #mutación exitosa
            padre = f(x,y,z)
        else:
            x = x
            y = y
            z = z
            m = m
        s = sigma(s,g,m)
        u.append(x)
        v.append(y)
        w.append(z)
        
    xfyfzf = [round(x,6), round(y,6),round(z,6)]
    print("xf,yf,zf: ",xfyfzf)
    evol(u,v,w)
    
main()
