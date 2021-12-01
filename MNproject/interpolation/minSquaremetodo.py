import cmath
import functools

def multiply(a,b):
    return a*b

def topow(item):
    return item**2

def getLinealFunc(X,Y):
    
    n = len(X)
    sX = sum(X)
    sY = sum(Y)
    #get A
    sXY = sum(list(map(multiply,X,Y)))
    sXpow2 = sum(list(map(topow,X)))
    sX_pow2 = sX**2

    a = (  n*sXY - sX*sY  ) / ( n*sXpow2-sX_pow2)
    
    #get B
    b = (sY - a*sX)/n
    print(b)
    return (a,b)
    
    print("N= ",n)
    print("SX=",sX)
    print("SY=",sY)
    print("SXY=",sXY)
    print("sXpow2=",sXpow2)
    print("sX_pow2=",sX_pow2)
    print("A=",a)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# list(map(math.factorial, numbers))

def toStr(tupleAB):
    str1 = ""
    if tupleAB[1] > 0:
        str1 = f"f(x) = {tupleAB[0]}x + {tupleAB[1]}"
    else:
        str1 = f"f(x) = {tupleAB[0]}x {tupleAB[1]}"    
    return str1

def getCoefRelation(X,Y):
    n = len(X)
    sX = sum(X)
    sY = sum(Y)
    avgX = sX/n
    avgY = sY/n
    x_avgX = list(map(lambda x: x-avgX,X))
    y_avgY = list(map(lambda y: y-avgY,Y))
    numerador = sum( list( map(lambda x,y:x*y,x_avgX,y_avgY) ) )
    sum_x_avgX_pow2 = sum( list( map(topow,x_avgX) ) )
    sum_y_avgY_pow2 = sum(list(map(topow,y_avgY)))
    # print(sum_x_avgX_pow2)
    # print(sum_y_avgY_pow2)

    r = numerador / (cmath.sqrt(sum_x_avgX_pow2)*cmath.sqrt(sum_y_avgY_pow2))
    if r.imag == 0j:
        return r.real
    else:
        return r


def metodoMinSquare(X,Y):
    tupleAB = getLinealFunc(X,Y)
    mystr =  toStr(tupleAB)
    coefRelation = getCoefRelation(X,Y) 
    mystr+=f"\n Coeficiente de Correlacion: {coefRelation}"           
    return mystr


if __name__ == "__main__":
    Y = [3,5,9,10,20,21,24,24,27,35]
    X = [100,90,80,45,50,50,60,40,25,20]
    X = [40,45,49,51,55,58,63,67,70,72]
    Y = [2,4,7,9,10,13,15,17,21,22]
    str1 = metodoMinSquare(X,Y)
    print(str1)
    # r = getCoefRelation(X,Y)
    # print("Relation: ",r)
    # tupleAB = getLinealFunc(X,Y)
    # if tupleAB[1] > 0:
    #     str1 = f"f(x) = {tupleAB[0]}x + {tupleAB[1]}"
    # else:
    #     str1 = f"f(x) = {tupleAB[0]}x {tupleAB[1]}"
    # print(str1)