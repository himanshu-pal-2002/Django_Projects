from django.shortcuts import render
from .models import *

# Create your views here.
def Detail_Display(request):
    QLTO=Employee.objects.all()
    d={'Topic':QLTO}
    return render(request,'query/happy.html',d)