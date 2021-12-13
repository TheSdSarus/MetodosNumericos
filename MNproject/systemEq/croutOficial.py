from cmath import e
import numpy as np
from utils import solveMatrix,printMatrix

def crout(A):    
    #Get the number of rows
    n = A.shape[0]
    
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] = U[i+1:] - factor[:, np.newaxis] * U[i]
    return (L, U)

def croutOficial(A,B):
    output = ""
    A = np.array(A)
    LU = crout(A)
    L = LU[0].tolist()
    U = LU[1].tolist()
    output += printMatrix(L,title="Matriz Inferior")
    output += printMatrix(U,title="Matriz Superior")
    roots = solveMatrix(L,U,B)
    output += "\n"+printMatrix(roots,"Solucion")
    return output

# from pprint import pprint as pp
if __name__=="__main__":
    A = [[2,3,-1], [3,2,1], [1,-5,3]]
    B =[[5,],[10,],[0,]]
    output = croutOficial(A,B)
    print(output)
    # A = np.array([[1, 4, 5], [6, 8, 22], [32, 5., 5]])
    # LU = crout(A)
    # L = LU[0].tolist()
    # U = LU[1].tolist()
    # print(printMatrix(L,title="Matriz Inferior"))
    # print(printMatrix(U,title="Matriz Superior"))
    # B=[[1],[2],[3]]
    # roots = solveMatrix(L,U,B)
    # for item in roots:
    #     print(item)
    
    