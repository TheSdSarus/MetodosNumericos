from django.shortcuts import render
import math
# Create your views here.

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
        "newton":2
    }
    start = request.GET
    #cantVars = start["cant"]
    method = start["method"]
    lista = []
    i = 0
    for val in start.values():
        key = "x"+str(i)
        myval = start.get(key)
        if myval:
            try:
                office = int(myval)
            except:
                office = 0
            lista.append(office)
        else:
            print("No key exist, value is: ", myval,"i=",i)
            break
        i+=1
    vars = []
    for times in range(timesConst[method]):
        vars.append(start["var"+str(times)])

    #my vars
    print("Variables: ",vars)

    #hacer el metodo correspondiente
    #print(cantVars)
    print(method)
    print(lista)

    return render(request,"passData.html")



