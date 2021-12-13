from .utils import printMatrix
import numpy as np

def metodoCramer(A,B):
    mystr = ""
    mystr += printMatrix(A,title="Original Matrix",nround=4)
    x = np.array(A)
    y = np.array(m1(B))
    print(x)
    print(y)
    mystr += cramer(x,y)

    return mystr

def cramer(A,B):
    n = len(B)
    D = np.linalg.det(A)
    x = np.zeros(n)
    mystr=""
    for k in range(n):
        Ak=A.copy()
        Ak[:,k] = B
        Dk = np.linalg.det(Ak)
        x[k]=Dk/D
        mystr += 'x' + str(k+1) + '=' + str(round(x[k],5))
    return mystr


def matrix(matrix,title="Matrix <Nombre>",nround=None):
    str1 = f'''{"*"*4} {title} {"*"*4} \n'''
    if(nround):
        for i in range(len(matrix)):
            str1 += f"{round(matrix[i].real,nround)}\t"
    else:
        for i in range(len(matrix)):
            str1 += f"{matrix[i].real}\t"
    str1+="\n"
    return str1

def m1(B):
    C = []
    for i in range(0,len(B)):
        C.append(B[i][0])
    return C