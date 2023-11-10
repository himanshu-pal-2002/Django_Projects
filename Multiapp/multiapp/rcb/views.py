from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Virat(request):
    return render(request,'virat.html')

def Abd(request):
    return HttpResponse('<marquee><h1>Mr 360 Player</h1></marquee>')