from django.shortcuts import render
from .models import *

# Create your views here.
def Employee(request):
    CTO=Employee(Name='Aakash')
    CTO.save()
    return render(request,'query/happy.html')