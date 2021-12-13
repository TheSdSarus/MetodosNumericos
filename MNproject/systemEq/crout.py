from numpy.core.numeric import outer
from .utils import printMatrix,solveMatrix

def crout(A):
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    for j in range(n):
        U[j][j] = 1          
        for i in range(j, n):  
            alpha = float(A[i][j])
            for k in range(j):
                alpha -= L[i][k]*U[k][j]
            L[i][j] = alpha
        for i in range(j+1, n):
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= L[j][k]*U[k][i]
            if int(L[j][j]) == 0:
                L[j][j] = e-40
            U[j][i] = tempU/L[j][j]
    return [L, U]  
from pprint import pprint as pp
def croutMetodo(A,B):
    output = ""
    LU = crout(A)
    output += printMatrix(LU[0],"Matriz Inferior",nround=4)
    output += printMatrix(LU[1],"Matriz Superior",nround=4)
    roots = solveMatrix(LU[0],LU[1],B)
    output += printMatrix(roots,"Matriz Solucion",nround=6)
    return output
if __name__ == "__main__":
    a = [[2,3,-1], [3,2,1], [1,-5,3]]
    b = [[5],[10],[0]]
    out = croutMetodo(a,b)
    print(out)