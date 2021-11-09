from django.shortcuts import render
import math
# Create your views here.

def home(request):
    return render(request,"home.html")

def getData(request):
    return render(request,"inputData.html")

def passData(request):
    start = request.GET
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

    #hacer el metodo correspondiente
    print(method)
    print(lista)
    return render(request,"passData.html")



