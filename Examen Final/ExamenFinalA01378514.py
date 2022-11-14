import math
import numpy as np
def f1(x):
    f = 1/math.sqrt(x)
    return f
def f2(x,y):
    f = 1 + y**2 
    return f

def simpson38(a,b,n):
    h = (b-a)/n
    I = f1(a) + f1(b)
    for k in range(1,n):
        if k%3!=0:
            I += 3*f1(a + k*h)
        else:
            I += 2*f1(a + k*h)
    I *= (3*h/8)
    return I

def RK4(x0,y0,xf,h):
    xn = x0
    yn = y0
    n = 0
    while xn <= xf:
        n +=1
        k1 = f2(xn,yn)
        k2 = f2((xn + h/2), (yn + h*k1/2))
        k3 = f2((xn + h/2), (yn + h*k2/2))
        k4 = f2((xn + h), (yn + h*k3))
        yn += h*(k1 + 2*k2 + 2*k3 + k4)/6
        xn = x0 + n*h
    return yn

def rutacorta(M,N):
    x = 0
    m = [[0,0,0]]*len(M)
    D = [0]*len(M)
    for j in range(1,len(M)):
        p = []
        for i in range(0,len(M)):
            if M[i][j] != x:
                d = D[i] + M[i][j]
                p.append([d,N[i],N[j]])
        m[j] = min(p)
        D[j] = m[j][0]
    l = m[-1]
    n = N[-1]
    s = n
    while n != N[0]:
        for i in m:
            if i[2] == l[1]:
                s = i[2] + '-' + s
                l = i
        n = l[1]
    s = '1-' + s
    dt = m[-1][0]
    return s,dt

def main():
    print("Examen Final \n")
    print("por: Álvaro Cuauhtémoc Ramírez Miguel\n")

    print("1. Encuentre por medio del algoritmo de la Regla de Simpson 3/8 "
    "la solución numérica a la integral de 1 sobre la raíz cuadrada de x "
    "con respecto a x en un intervalo desde 0.04 hasta 1. \n")
    a = 0.04
    b = 1
    n = 1000000
    I = simpson38(a,b,n)
    print("Valor de la integración numérica por Simpson 3/8 con 1 000 000 de subintervalos: ",round(I,7))
    print("\n")


    print("2. Encuentra por medio del algoritmo de Runge-Kutta de orden 4 la "
    "solución numérica a la siguiente ecuación diferencial: \n")
    print("y' = 1 +  y² \n")
    print("En el punto x = 1.4 \n")
    print("con condición inicial y(0) = 0 y paso de iteración h = 0.1\n")
    x0 = 0
    y0 = 0
    x = 1.4
    h = 0.1
    yf = RK4(x0,y0,x,h)
    print("El valor numérico aproximado para y(1.4) es ",round(yf,7))
    print("\n")
    print("3. Implementar mediante el lenguaje Python un sistema que ejecute el algoritmo "
    "de la ruta más corta para optimizar la ruta entre los nodos 1 y 8 de la siguiente red.\n")
    N='12345678'
    x = 0
    M= [[x,1,2,x,x,x,x,x],\
        [x,x,1,5,2,x,x,x],\
        [x,x,x,2,1,4,x,x],\
        [x,x,x,x,3,6,8,x],\
        [x,x,x,x,x,3,7,x],\
        [x,x,x,x,x,x,5,2],\
        [x,x,x,x,x,x,x,6],\
        [x,x,x,x,x,x,x,x]]
    RC = rutacorta(M,N)
    Red = np.insert(M,0,list(N),axis=0)
    print(Red)
    print("\nLa ruta más corta se encuentra entre los nodos ",RC[0])
    print("Con una distancia total de ",RC[1], " unidades\n")
main()
