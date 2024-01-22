from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.core.mail import send_mail


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

            send_mail (
                'Registration',
                'Your Registration is Successful',
                'palhimanshu206246@gmail.com',
                [MUFDO.email],
                fail_silently=False,
            )
            # print(MUFDO.email),
            return redirect("Show_Details")
        else:
            return HttpResponse("Invalid Data")
        
    return render(request,'registeration.html',d)

# Views For Displaying Details:
def Show_Details(request):

    data=Profile.objects.all()
    d={'data':data}

    return render(request,'showdata1.html',d)

# Views For Profile View
def Profile_View(request,id):

    profile = Profile.objects.get_or_create(id=id)[0]
    # a={'profile':profile}
    print(profile)
    return render(request,'profiledata.html',{'profile':profile})


# For Deleteing Data specific id.
def Delete_Profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return redirect('Show_Details')

