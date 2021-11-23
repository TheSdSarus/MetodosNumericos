
def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def printMatrix(matrix,title="Matrix <Nombre>",nround=None):
    str1 = f'''{"*"*4} {title} {"*"*4} \n'''
    if(nround):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                str1 += f"{round(matrix[i][j].real,nround)}\t"
            str1+="\n"
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                str1 += f"{matrix[i][j].real}\t"
            str1+="\n"
    return str1
def multiply(matrix1,matrix2):
    n = len(matrix1)-1
    result = [[0 for x in range(n +1)]
				for y in range(n +1)]
    # iterate through rows of X
    for i in range(len(matrix1)):
    # iterate through columns of Y
        for j in range(len(matrix2[0])):
            # iterate through rows of matrix2
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def solveMatrix(lower,upper,B):
	# A = L*U
	# A * x = B
	# L * y = B  -> y = L^-1 * B
	# U * x = y  -> x = U^-1 * y
	inverseLower = getMatrixInverse(lower)
	y_matrix = multiply(inverseLower,B)
	inverseUpper = getMatrixInverse(upper)
	rootsX = multiply(inverseUpper,y_matrix)
	return rootsX

def main():
    matrix = [
        [1,4,5],
        [-1,1,1],
        [5,1,1]
    ]
    inversa = getMatrixInverse(matrix)
    stre = printMatrix(inversa,"Matrix INversa",3)
    print(stre)

if __name__ == "__main__":
    main()







