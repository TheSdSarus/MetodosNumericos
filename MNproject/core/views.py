from django.shortcuts import render
import math
# Create your views here.

def home(request):
    return render(request,"home.html")

def getData(request):
    return render(request,"inputData.html")

def passData(request):

    start = request.GET
    con = 0
    cant = int(start["can"])
    list = []
    for _,value in start.items():
        if con == 0:
            con = con + 1
            continue
        if cant+1 == con:
            break
        try:
            val=int(value)
        except:
            val = 0
        
        list.append(val)
        con = con + 1
    #hacer el metodo correspondiente
    
    print(list)
    return render(request,"passData.html")



