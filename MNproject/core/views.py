from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def getData(request):
    return render(request,"inputData.html")

def passData(request):

    start = request.GET
    con = 0;
    cant = int(start["can"])
    list = []
    for key,value in start.items():
        if con == 0:
            con = con + 1
            continue
        if cant+1 == con:
            break

        list.append(int(value))
        con = con + 1

    print(list)
    return render(request,"passData.html")



