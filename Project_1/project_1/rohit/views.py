from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Shreyas(request):
    return HttpResponse('<h1>Shreyas Scored Century in Worldcup Semifinal</h1>')