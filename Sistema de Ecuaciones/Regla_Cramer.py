import numpy as np
import math
import copy
def Red(Matriz):
    try:
        MatrizR=copy.deepcopy(Matriz)
        m=len(MatrizR)
        n=len(MatrizR[0])
        for i in range(m-1):
            for k in range(1+i,m):
                c=MatrizR[k][i]
                for j in range(n):
                    MatrizR[k][j]=MatrizR[k][j]-(c*(MatrizR[i][j]/MatrizR[i][i]))
        return MatrizR
    except IndexError:
        print("La matriz ingresada no es cuadrada, intenta con algo diferente")
        return 0

def Det(Mat):
    try:
        m=len(Mat)
        n=len(Mat[0])
        D=1
        c=0
        for i in range(m):
            for j in range(i+1,n-i):
                if Mat[j][i]!=0:
                    c+=1
        if c>0:
            print("La matriz no está reducida, prueba de nuevo")
            return 0
        else:
            for i in range(n):
                D*=Mat[i][i]
            return D
    except IndexError:
        print("La matriz ingresada no es cuadrada, intenta con algo diferente")
        return 0
Incognitas=[[0.25,0.15,0],[0.45,0.5,0.75],[0.3,0.35,0.25]]
TerminosI=[1.5,5,3]
def Cramer(MatrizI,MatrizT):
    mi=len(MatrizI)
    ni=len(MatrizI[0])
    mt=len(MatrizT)
    D=[]
    if mi==mt and type(MatrizT[0])!=list:
        for i in range(ni):
            x=copy.deepcopy(MatrizI)
            for j in range(mi):
                x[j][i]=MatrizT[j]
            x=Red(x)
            d=Det(x)
            di=Det(Red(MatrizI))
            X=round(d/di,8)
            D.append(X)
        return D
    else:
        print("Las matrices no tienen la misma cantidad de filas o la matriz de terminos independientes tiene más de una columna")
        return 0
    
#Con código propio 
print(np.asarray(Cramer(Incognitas,TerminosI)))
#Con librería numpy
SE=np.linalg.solve(Incognitas,TerminosI)
print(SE)