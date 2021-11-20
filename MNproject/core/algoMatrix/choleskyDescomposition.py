import math
MAX = 100

def printMatrix(matrix,title="Matrix <Nombre>"):
    str1 = f'''{"*"*4} {title} {"*"*4} \n'''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            str1 += f"{matrix[i][j]}\t"
        str1+="\n"
    return str1
    # print("*"*4,title,"*"*4)
    # print(str1)    
def isTranspuesta(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def toTranspuesta(matrix):
	n = len(matrix) -1
	upper = [[0 for x in range(n + 1)]
				for y in range(n + 1)]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			upper[j][i] = matrix[i][j]
	return upper


def Cholesky_Decomposition(matrix):
	n = len(matrix)
	str_glob = ""
	if(isTranspuesta(matrix) == False):
		str_glob = "La matriz no es simetrica"
		return
	lower = [[0 for x in range(n + 1)]
				for y in range(n + 1)]

	for i in range(n):
		for j in range(i + 1):
			sum1 = 0

			if (j == i):
				for k in range(j):
					sum1 += pow(lower[j][k], 2)
				lower[j][j] = int(math.sqrt(matrix[j][j] - sum1))
			else:
				
				for k in range(j):
					sum1 += (lower[i][k] *lower[j][k])
				if(lower[j][j] > 0):
					lower[i][j] = int((matrix[i][j] - sum1) /
											lower[j][j])
	str_glob += printMatrix(matrix,title="Matriz Original")
	str_glob += "\n"
	str_glob += printMatrix(lower,title="Triangular Inferior")
	str_glob += "\n"
	str_glob += printMatrix(toTranspuesta(lower),title="Triangular Superior")
	return str_glob
	# print("Triangular Inferior\t\tTriangular Superior")
	# for i in range(n):
	# 	for j in range(n):
	# 		print(lower[i][j], end = "\t")
	# 	print("", end = "\t")
	# 	for j in range(n):
	# 		print(lower[j][i], end = "\t")
	# 	print("")



n = 3
matrix = [
    [4, 12, -16],
	[12, 37, -43],
	[-16, -43, 98]
]

mystr= ""
mystr = Cholesky_Decomposition(matrix)
print(mystr)
