import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def LagrangeMethod(X,Y):
    xi = np.array(X)
    fi = np.array(Y)
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        

        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    polisimple = polinomio.expand()
    px = sym.lambdify(x,polisimple)
    a = np.min(xi)
    b = np.max(xi)

    newX = np.arange(a,b+0.1,0.1)
    newY = yValue(px,newX)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=newX, y=newY))
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    ##--------------------------
    mystr =  str(polisimple)
    context = {
        "outputStr":mystr,
        "graph":graph,
    }

    return context

def yValue(a,M):
    y = []
    for absc in M:
        y.append(a(absc))
    return y

    


    print(X)
    print(Y)

def Nofunct(X,Y):

    xi = np.array([0, 0.2, 0.3, 0.4])
    fi = np.array([1, 1.6, 1.7, 2.0])


    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        

        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador


    polisimple = polinomio.expand()


    px = sym.lambdify(x,polisimple)


    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)


    print('    valores de fi: ',fi)
    print('divisores en L(i): ',divisorL)
    print()
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)
    print()
    print('Polinomio de Lagrange: ')
    print(polisimple)
    print('Es ' + str(px(3)))


    plt.plot(xi,fi,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()