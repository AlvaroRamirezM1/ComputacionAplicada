import copy
import sympy as sp
def Sum(Matrix):
    try:
        MatrixR=copy.deepcopy(Matrix)
        m=len(MatrixR)
        n=len(MatrixR[0])
        for i in range(m-1):
            for k in range(1+i,m):
                c=MatrixR[k][i]
                MatrixR[k][i]=MatrixR[k][i]-(c*(MatrixR[i][i]/MatrixR[i][i]))
        SM=0
        for i in range(m):
            SM+=sum(MatrixR[i])
        return SM
    except IndexError:
        print("La matriz ingresada no es cuadrada, intenta con algo diferente")
        return 0
def PrimeNum(m):
    if m<=16:
        MP=[]
        NP=list(sp.primerange(0, sp.prime(m*m)+1))
        for i in range(m):
            F=[]
            for j in range(m):
                F.append(NP[(i*m)+j])
            MP.append(F)
        return MP
    else:
        print("El tamaño máximo es de 16x16, intenta de nuevo")
        return



m=int(input("Ingresa el tamaño de la matriz "))
PM=PrimeNum(m)
if isinstance(PM, list):
    print("La matriz generada es:\n")
    for i in range(m):
        str1=""
        for j in range (m):
            str1+="\t"+str(PM[i][j])
        print(str1,"\n")
    print("y la suma de los elementos encima de la diagonal principal es: ",Sum(PM))
else:
    print()
