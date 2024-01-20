from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def registration(request):

    ufo=UserForm()

    pfo=ProfileForm()

    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:

        ufd=UserForm(request.POST)

        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():

            MUFDO=ufd.save(commit=False)

            Pw=ufd.cleaned_data['password']

            MUFDO.set_password(Pw)

            MUFDO.save()

            MPFDO=pfd.save(commit=False)

            MPFDO.username=MUFDO

            MPFDO.save()

            return HttpResponse("Registration Successful")
        else:
            return HttpResponse("Invalid Data")
        
    return render(request,'registeration.html',d)