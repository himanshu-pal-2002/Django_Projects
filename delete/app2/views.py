from django.shortcuts import render
from .models import *

# Create your views here.
def Country_Details(request):
    CLTO = Country.objects.all().delete()
    d={'Country':CLTO}
    return render(request,'country.html',d)