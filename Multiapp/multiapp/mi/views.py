
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Rohit(request):
    return render(request,'rohit.html')

def Bumrah(request):
    return HttpResponse('<marquee><h1>Yorker King</h1></marquee>')