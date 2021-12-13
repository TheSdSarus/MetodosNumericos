from .utils import printMatrix
def metodoGaussSeidel(A,B):
    x = []
    C = m1(B)
    for i in range(len(C)):
        x.append(0)
    mystr= ""
    mystr += printMatrix(A,title="Original Matrix",nround=4)
    for i in range(0, 25):            
        x = seidel(A, x, C)

        mystr += matrix(x,title="Iteracion: " + str(i) + "",nround=4)
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
def seidel(a, x ,b):      
    n = len(a)                   
    for j in range(0, n):        
        d = b[j]                  
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        x[j] = d / a[j][j]           
    return x    
