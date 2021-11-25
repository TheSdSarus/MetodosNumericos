from django.shortcuts import render
from findRoot import bisection,mn_secantes,muller_custo
# Create your views here 

def home(request):
    return render(request,"home.html")

def getData(request):
    return render(request,"inputData.html")

def matrixLU(request):
    return render(request,"descomposicionLU.html")

def passData(request):
    timesConst = {
        "bairstow":0,
        "muller":3,
        "newton":2#bisseccion
    }
    start = request.GET
    try:
        cantVars = start["cant"]
        method = start["method"]
        cantVars = start["cant"]
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
        guesses.append(start["var"+str(times)])

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

def adminMethods(coefs,guesses,method):
    output = ""
    if(method == "newton"):
        a = int(guesses[0])
        b = int(guesses[1])
        coefs = convertToInt(coefs)
        output = bisection.metodoBiseccion(a,b,coefs)
    elif(method == "muller"):
        guesses = convertToInt(guesses)
        coefs = convertToInt(coefs)
        output = muller_custo.metodoMuller(guesses,coefs)
    elif(method == "bairstow"):
        guesses = convertToInt(guesses)
        coefs = convertToInt(coefs)
        output = mn_secantes.mainSecanteMetodo(guesses,coefs)
    return output

def convertToInt(lista):
    data = []
    for item in lista:
        data.append(int(item))
    return data
