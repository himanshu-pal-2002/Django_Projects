from django.shortcuts import render
from .forms import *


# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    return render(request,'registeration.html',d)