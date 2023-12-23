from django.shortcuts import render
from .models import *


# Create your views
def Display_details(request):
    QLTO = Topic.objects.all()
    d={'Topic': QLTO}
    return render(request,'display_details.html',d)
