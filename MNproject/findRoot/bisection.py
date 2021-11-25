import math as m
COEFICIENTES = []

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
    #fx = lambda x: 1 + 2*x -3*x**(2)*m.e**(-1*x) + 2*x**(3)*m.sin(x)*m.e**((-1*x)/5)
    #fx = lambda x: 4*x**(2) - 2 + x*m.e**(x/4)
    #fx = lambda x: x**2 -x-1
    return newF(val=x)

def bisection(a,b,N):
    mystr = ""
    if f(a)*f(b) >= 0:
        mystr = "El metodo no encontro  que cruce el eje X con estos primeros puntos!!!"
        return mystr
    a_n = a
    b_n = b
    
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        mystr+=f"Iteracion #{n}\n"
        mystr += f"""a={a_n}
b={b_n}
m={m_n}
"""
        f_m_n = f(m_n)
        mystr +=f"""
f(a)={f(a_n)}
f(b)={f(b_n)}
f(m)={f_m_n}\n
"""
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            mystr+=f"\n*Solucion*= {f_m_n}\n"
            return mystr
        else:
            mystr = "ERROR en metodo biseccion"
            return mystr
    mystr+=f"\n *Solucion*: {(a_n + b_n)/2}\n"
    return mystr


def metodoBiseccion(a,b,coefs):
    global COEFICIENTES
    COEFICIENTES = coefs
    middle = bisection(a,b,12)
    return middle

if __name__ == "__main__":
    str1 = metodoBiseccion(1,2,[1,-1,-1])
    print(str1)
