import math as m

COEFICIENTES = []
#x**3 + 2*x**2 + 10*x - 20
def newF(val=0):
    # n-4 = 4 -4 = 0
    # 1x^(n-1) + 2^(n-2) + 3^(n-3) + 4^(n-4)
    result = 0
    n = len(COEFICIENTES)
    for grado in range(n):
        result += COEFICIENTES[grado] * val**(n - grado -1)
    return result 
    #print("Resultado de la funcion",result)


def f(x):
    #fx = lambda x: x**3 + 2*x**2 + 10*x - 20
    return newF(val=x)

def secante(a,b):
    p1 = f(b)
    p2 = a-b
    p3 = f(a) - f(b)
    result = b - p1*p2/p3
    return result

def secanteMethod(guesses):
    mystr = ""
    a = guesses[0]
    b = guesses[1]
    error = 10**-10
    current_error = error*2
    init = 0
    iterMax=13
    i=0
    while not current_error <= error:
        sig = secante(a,b)
        current_error = round(abs(sig-b)/sig,5)
        mystr += (f'''Iteracion #{i+1})\n\n''')
        mystr += (f"""a={round(a,8)} 
b={round(b,8)} 
f(a)={round(f(a),8)} 
f(b)={round(f(b),8)} 
siguiente b={round(sig,8)} 
error={current_error}\n\n""")
        a = b
        b = sig
        
        if(iterMax == 0):
            mystr += ("Numero Max de Iteraciones alcanzado \n")
            break
        if current_error <= error:
            return mystr
        i+=1
    

def mainSecanteMetodo(guesses,coefs):
    global COEFICIENTES
    COEFICIENTES = coefs
    str1 = secanteMethod(guesses)
    return str1

##PASOS PARA USAR LA FUNCION
# Los COEFICIENTES DEBES EDITARLOS CON LOS COEFICIENTES ACTUALES
# LOS DESPUES DE BES PONER INITIAL GUESSES
# LUEGO PONER COMO PARAMETRO EL MULLER(GUESSES=[x0,x1,x2])
#luego recoger el str del metodo str1 = muller(guesses)
if __name__ == "__main__":
    # COEFICIENTES = [1, 2 ,10 , -20]
    # guesses = [2,3]
    # mystr = secanteMethod(guesses)
    # print(mystr)
    mstr = mainSecanteMetodo([2,3],coefs=[1,2,10,-20])
    print(mstr)
    