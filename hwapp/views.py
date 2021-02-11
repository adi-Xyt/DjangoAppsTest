from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'hwapp/main.html')
def weather(request):
    return render(request,"hwapp/weather.html")