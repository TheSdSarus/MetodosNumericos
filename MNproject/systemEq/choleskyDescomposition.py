from .utils import printMatrix,solveMatrix
import cmath
import math
MAX = 100

def isTranspuesta(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def toTranspuesta(matrix):
	n = len(matrix) -1
	upper = [[0 for x in range(n +1)]
				for y in range(n +1)]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			upper[j][i] = matrix[i][j]
	return upper

str_glob = ""

def Cholesky_Decomposition(matrix):
	n = len(matrix)
	if(isTranspuesta(matrix) == False):
		global str_glob
		str_glob = "La matriz no es simetrica"
		return
	lower = [[0 for x in range(n )]
				for y in range(n )]

	for i in range(n):
		for j in range(i + 1):
			sum1 = 0

			if (j == i):
				for k in range(j):
					sum1 += pow(lower[j][k], 2)
				lower[j][j] = cmath.sqrt(matrix[j][j] - sum1)
			else:
				
				for k in range(j):
					sum1 += (lower[i][k] *lower[j][k])
				if(lower[j][j].real > 0):
					lower[i][j] = ((matrix[i][j] - sum1) / lower[j][j])
	# str_glob += printMatrix(matrix,title="Matriz Original")
	# str_glob += "\n"
	# str_glob += printMatrix(lower,title="Triangular Inferior")
	# str_glob += "\n"
	# str_glob += printMatrix(toTranspuesta(lower),title="Triangular Superior")
	return (lower,toTranspuesta(lower))
	# print("Triangular Inferior\t\tTriangular Superior")
	# for i in range(n):
	# 	for j in range(n):
	# 		print(lower[i][j], end = "\t")
	# 	print("", end = "\t")
	# 	for j in range(n):
	# 		print(lower[j][i], end = "\t")
	# 	print("")





def main():
	#n = 3
	matrix = [
		[6,15,55],
		[15,55,225],
		[55,225,979]
	]
	B = [
		[100],
		[150],
		[100]
	]
	mystr= ""
	(lower,upper) = Cholesky_Decomposition(matrix)
	rootsX = solveMatrix(lower,upper,B)
	mystr += printMatrix(matrix,title="Original Matrix",nround=4)
	mystr += printMatrix(lower,title="Lower Matrix",nround=4)
	mystr += printMatrix(upper,"Upper Matrix",nround=4)
	mystr += printMatrix(rootsX,"RootsX",nround=4)
	print(mystr)

def metodoCholesky(A,B):
	if(not isTranspuesta(A)):
		return "Esta matriz no es simetrica, el metodo Choleski necesita que sea simetrica y positiva"
	(lower,upper) = Cholesky_Decomposition(A)
	 
	rootsX = solveMatrix(lower,upper,B)
	rootsX = solveMatrix(lower,upper,B)
	mystr= ""
	mystr += printMatrix(A,title="Original Matrix",nround=4)
	mystr += printMatrix(lower,title="Lower Matrix",nround=4)
	mystr += printMatrix(upper,"Upper Matrix",nround=4)
	mystr += printMatrix(rootsX,"RootsX",nround=4)
	return mystr

if __name__ == "__main__":
	matrix = [
		[6,15,55],
		[15,55,225],
		[55,225,979]
	]
	B = [
		[100],
		[150],
		[100]
	]	
	mstr = metodoCholesky(matrix,B)	
	print(mstr)