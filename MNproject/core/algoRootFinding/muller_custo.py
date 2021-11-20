import cmath as cm
COEFICIENTES = [1,0,1,-2]#siempre editar esta variables antes de hacer cualquier cosa
str1 = ""
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
    return newF(val=x)



def f1(x1,x0):
    try:
        val = (f(x1)-f(x0))/(x1-x0)         
    except:
        print("Divide by ZERO!!, f1()")
        return -1
    return val

def f2(x2,x1):
    try:
        val = (f(x2)-f(x1))/(x2-x1)         
    except:
        print("Divide by ZERO!! , f2()")
        return -1
    return val    

def f3(x2,x1,x0):
    num = f2(x2,x1)-f1(x1,x0)
    den = x2 - x0
    if den == 0:
        print("Divide by ZERO!! , f3()")
        return -1
    return num/den

def getX3(a0,a1,a2):
    den1 = -1*a1+cm.sqrt(a1**2 - 4*a0*a2)
    den2 = -1*a1-cm.sqrt(a1**2 - 4*a0*a2)
    if den1 == 0 and den2 ==0:
        print("Divide By ZERO!! getDenominador()")
        return None
    sol1 = (2*a0)/(den1)
    sol2 = (2*a0)/(den2)
    xplus = 0
    if(abs(f(sol1)) < abs(f(sol2))):
        xplus = sol1
    else:
        xplus = sol2
    if xplus.imag == 0j:
        xplus = xplus.real
    
    return xplus

def muller(guesses):
    mystr = ""
    x0 = guesses[0]
    x1 = guesses[1]
    x2 = guesses[2]
    tole = 10**-5
    error = tole/2
    memory = 0
    maxIter = 15
    x3 = -1
    while error < tole or maxIter == 0:
        error = x3 - memory
        a2 = f3(x2,x1,x0)
        a1 = f2(x2,x1) -(x2+x1)*a2
        a0 = f(x2) - x2*(f2(x2,x1) - x1*a2)
        mystr += (f"x0={x0} x1={x1} x2={x2}\n")
        mystr += (f"a0={a0} a1={a1} a2={a2}\n")

        x3 = getX3(a0,a1,a2)
        x0 = x1
        x1 = x2
        memory = x2
        x2 = x3
        mystr += (f"x3={x3} f(x3)={f(x3)} error={error}\n")
    
        maxIter-=1
    return mystr

##PASOS PARA USAR LA FUNCION
# Los COEFICIENTES DEBES EDITARLOS CON LOS COEFICIENTES ACTUALES
# LOS DESPUES DE BES PONER INITIAL GUESSES
# LUEGO PONER COMO PARAMETRO EL MULLER(GUESSES=[x0,x1,x2])
#luego recoger el str del metodo str1 = muller(guesses)
if __name__ == "__main__":
    # mystr = main()
    # print(mystr)
    # x**3 + 0 + x**1 + -2
    COEFICIENTES = [1, 2 ,10 , -20]
    guesses = [0,1,2]
    mystr = muller(guesses)
    print(mystr)
    #COEFICIENTES = [1,0,1,-2]
    #newF(val=3)
    #x**3 + 2*x**2 + 10*x - 20

