from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home (request):
    return render (request,'home.html',{'name':'Mani'})
def add (request):
    val1=request.POST["num1"]
    val2=request.POST["num2"]
    res=int(val1)+int(val2)
    return render(request,'results.html',{'result':res})
