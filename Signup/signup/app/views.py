from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create view for Home
# def home(request):
#     if request.session.get('username'):
#         username=request.session.get('username')
#         d = {'username': username}
#         return render(request,'home.html',d)
#     return render(request,'home.html')


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

# For login:
def User_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO = authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))

    return render(request,'user_login.html')

# Create view for Home
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d = {'username': username}
        return render(request,'home.html',d)
    
    return render(request,'home.html')

# Create views for Logout.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


