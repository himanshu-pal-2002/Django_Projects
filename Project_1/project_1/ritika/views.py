from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Sammy(request):
    return HttpResponse('<h1>Happy Birthday</h1>')