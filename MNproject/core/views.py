from django.http.response import HttpResponse
from django.shortcuts import render, reverse
from findRoot import bisection, muller_custo, bairstow
from systemEq import choleskyDescomposition, gaussSeidel, cramer, crout
from interpolation import minSquaremetodo, newtonDifDiv, Lagrange

# Create your views here


def home(request):
    return render(request, "home.html")


def getData(request):

    timesConst = {
        "bairstow": 0,#0 variables
        "muller": 3,# 3 variables
        "newton": 2  # bisseccion
    }
    start = request.GET
    if start:
        pass
        try:
            cantVars = start["cant"]
            method = start["method"]
        except:
            print("Value Error error a [cant, method, cant]")
        
        # print(start)
        coefs = []
        # i = 0
        for j in range(int(cantVars)):
            key = "x"+str(j)
            myval = start.get(key)
            if(myval):
                coefs.append(myval)
            else:
                print("No exist this key: ",key)

        # for val in start.values():
        #     key = "x"+str(i)
        #     myval = start.get(key)
        #     if myval:
        #         try:
        #             office = int(myval)
        #         except:
        #             office = 0
        #         coefs.append(office)
        #     else:
        #         print("No key exist, value is: ", myval,"i=",i)
        #         break
        #     i+=1

        # variables
        guesses = []
        for times in range(timesConst[method]):
            guesses.append(start.get("var"+str(times)))

        output= ""
        output = adminMethods(coefs=coefs,guesses=guesses,method=method)
        wrapperGraph = getGraph(coefs)
        context = {
            "output":output,
            "method":method,
            "graph": wrapperGraph["graph"],
        }
        #my vars
        # print("Variables: ",vars)

        # hacer el metodo correspondiente
        # print("Cantidad de bariables: ",cantVars)
        # print("Methodo",method)
        # print("Coeficientes",coefs)
        # print("Initial Guesses",guesses)
        return render(request,"inputData.html",context)
    return render(request,"inputData.html")



def matrixLU(request):
    return render(request, "descomposicionLU.html")

# para los LU


def passDataMatrixLU(request):
    start = request.GET

    method = start.get("method")
    if method:
        order = start.get("order")
        if order:
            coefs = []
            count = 0
            for i in range(int(order)):
                row = []
                for j in range(int(order)):
                    key = "x"+str(count)
                    val = start.get(key)
                    if val:
                        val = float(val)
                        row.append(val)
                        pass
                    else:
                        print("La key= ", key, "No existe")
                        break
                    count += 1
                coefs.append(row)
            # get constant Matrix
            constCoefs = []
            for i in range(int(order)):
                key = "c"+str(i)
                val = start.get(key)
                if(val):
                    val = float(val)
                    constCoefs.append([val, ])
                else:
                    print("No existe la llave: ", key)
                    break
            # resolver el admin

            outputResult = adminMethodsLU(coefs, constCoefs, method)
            # print(coefs)
            context = {
                "coefs": coefs,
                "method": method,
                "order": order,
                "constMatrix": constCoefs,
                "output": outputResult
            }
            return render(request, "resultMatrixLU.html", context)
        else:
            print("Order no llego=", order)
    else:
        print("method no llego=", method)
    return render(request, "resultMatrixLU.html")


def passData(request):
    timesConst = {
        "bairstow": 0,#0 variables
        "muller": 3,# 3 variables
        "newton": 2  # bisseccion
    }
    start = request.GET
    if start:
        pass
        try:
            cantVars = start["cant"]
            method = start["method"]
        except:
            print("Value Error error a [cant, method, cant]")
        
        # print(start)
        coefs = []
        # i = 0
        for j in range(int(cantVars)):
            key = "x"+str(j)
            myval = start.get(key)
            if(myval):
                coefs.append(myval)
            else:
                print("No exist this key: ",key)

        # for val in start.values():
        #     key = "x"+str(i)
        #     myval = start.get(key)
        #     if myval:
        #         try:
        #             office = int(myval)
        #         except:
        #             office = 0
        #         coefs.append(office)
        #     else:
        #         print("No key exist, value is: ", myval,"i=",i)
        #         break
        #     i+=1

        # variables
        guesses = []
        for times in range(timesConst[method]):
            guesses.append(start.get("var"+str(times)))

        output= ""
        output = adminMethods(coefs=coefs,guesses=guesses,method=method)
        context = {
            "output":output,
            "method":method
        }
        #my vars
        # print("Variables: ",vars)

        # hacer el metodo correspondiente
        # print("Cantidad de bariables: ",cantVars)
        # print("Methodo",method)
        # print("Coeficientes",coefs)
        # print("Initial Guesses",guesses)
        return render(request,"passData.html",context)
    return render(request,"passData.html")


def inputMinSquare(request):
    start = request.GET
    if start:
        # retrieve cantidad
        method = start["method"]
        #print("METODO A USAR: ",method)
        val = start.get("cant")
        if not val:
            return render(request, "inputMinCuadrados.html")
        items = int(val)
        # retrieve X's and Y's
        arrX = []
        arrY = []
        for i in range(int(items)):
            key_x = "x"+str(i)
            key_y = "y"+str(i)
            valX = start.get(key_x)
            valY = start.get(key_y)
            if (not valY or not valX):
                print("ID X", key_x, "ID Y: ", key_y)
                break
            arrX.append(valX)
            arrY.append(valY)
        arr = zip(arrX, arrY)
        arX = convertToInt(arrX)
        arY = convertToInt(arrY)
        output = "Metodo NO FUNCIONA todavia..."
        output = adminInterpolation(arX, arY, method)
        context = {}
        if(method == "minSquare"):
            context = {
                "arr": arr,
                "cant": items,
                "output": output["outputStr"],
                "graph": output["graph"],
                "method": method
            }
        elif(method == "difDivididas"):
            context = {
                "arr": arr,
                "cant": items,
                "output": output["coefs"],
                "graph": output["graph"],
                "method": method
            }
        elif(method == "lagra"):
            context = {
                "arr": arr,
                "cant": items,
                "output": output["outputStr"],
                "graph": output["graph"],
                "method": "Lagrange"
            }

        return render(request, "outputMinCuadrados.html", context)

    return render(request, "inputMinCuadrados.html")


##########################################################################
# utils methods
def adminMethods(coefs, guesses, method):
    output = ""
    if(method == "newton"):
        a = int(guesses[0])
        b = int(guesses[1])
        coefs = convertToInt(coefs)
        output = bisection.metodoBiseccion(a, b, coefs)
    elif(method == "muller"):
        guesses = convertToInt(guesses)
        coefs = convertToInt(coefs)
        output = muller_custo.metodoMuller(guesses, coefs)
    elif(method == "bairstow"):
        # guesses = convertToInt(guesses)
        coefs = convertToInt(coefs)
        print("Coeficientes: ", coefs)
        output = bairstow.bairstowMain(coefs)
    else:
        output = "El metodo que pusiste no lo soportamos"
    return output

def adminMethodsLU(A, B, method):
    output = ""
    if(method == "choleski"):
        output = choleskyDescomposition.metodoCholesky(A, B)
        print("Bla" + output)
    elif(method == "gauss"):
        output = gaussSeidel.metodoGaussSeidel(A, B)
    elif(method == "crout"):
        output = crout.croutMetodo(A,B)
    elif(method == "cramer"):
        output = cramer.metodoCramer(A,B)
    else:
        output = "Este metodo no lo tenemos"
    return output

def adminInterpolation(X, Y, method):
    context = {}
    X = convertToInt(X)
    Y = convertToInt(Y)

    if(method == "difDivididas"):
        context = newtonDifDiv.difDivMethod(X, Y)
        # output = "AUN NO FUNCION ESTE METODO :(, pero I will do it"
    elif(method == "minSquare"):
        context = minSquaremetodo.metodoMinSquare(X, Y)
    elif(method == "lagra"):
        context = Lagrange.LagrangeMethod(X, Y)
    return context


def convertToInt(lista):
    data = []
    for item in lista:
        data.append(float(item))
    return data

#x**3 + 2*x**2 + 10*x - 20
def newF(val=0,coefs=None):
    result = 0
    n = len(coefs)
    for grado in range(n):
        result += coefs[grado] * val**(n - grado -1)
    return result 
import plotly.graph_objects as go

def getGraph(coefs):
    coefs = convertToInt(coefs)
    fig = go.Figure()
    x = []
    for i in range(-5,6):
        x.append(i)
    y = []
    for item in x:
        y.append(newF(val=item,coefs=coefs))
    fig.add_trace(go.Scatter(x=x, y=y))
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {
        "graph":graph,
    }
    return context

