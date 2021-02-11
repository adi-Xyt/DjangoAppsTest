
from django.shortcuts import render
import requests
# Create your views here.

def main(request):
    return render(request,'mysecondapp/test.html')

def register(request):
    return render(request,'mysecondapp/Fourm.html')

def writedata(request):
    
    data=requests.get("https://jsonplaceholder.typicode.com/todos/1")

    return render(request,'mysecondapp/mydynamic.html',{'data':data.text})
    
    
    
