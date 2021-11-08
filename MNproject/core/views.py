from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def getData(request):
    return render(request,"inputData.html")

def passData(request):
    return render(request,"passData.html")



