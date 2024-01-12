from django.shortcuts import render
import datetime

# Create your views here.
def Filter(request):
    d={'data':'Happy Makarshankranti'}
    dt=datetime.datetime.now()
    return render(request,'filters.html',d)