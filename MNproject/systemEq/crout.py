from .utils import printMatrix
# Gauss Seidel Iteration
'''
# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (17-y+2*z)/20
f2 = lambda x,y,z: (-18-3*x+z)/20
f3 = lambda x,y,z: (25-2*x+3*y)/20

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True
ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
'''

def metodoGaussSeidel(A,B):
    x = [0, 0, 0]
    C = m1(B)
    mystr= ""
    mystr += printMatrix(A,title="Original Matrix",nround=4)


    for i in range(0, 25):            
        x = seidel(A, x, C)

        mystr += matrix(x,title="Iteracion: " + str(i) + "",nround=4)
        #print each time the updated solution
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
    #Finding length of a(3)       
    n = len(a)                   
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):        
        # temp variable d to store b[j]
        d = b[j]                  
          
        # to calculate respective xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        # updating the value of our solution        
        x[j] = d / a[j][j]
    # returning our updated solution           
    return x    
