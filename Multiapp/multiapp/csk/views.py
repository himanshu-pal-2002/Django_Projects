from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Msd(request):
    return render(request,'msd.html')

def Raina(request):
    return HttpResponse('<marquee><h1>Mr IPL PLAYER</h1></marquee>')