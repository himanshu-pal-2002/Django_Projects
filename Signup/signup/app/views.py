from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import random


# Create views For Registration.
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
            # send_mail(
            #     'Your OTP',
            #     f'Your OTP is: {otp}',
            #     'palhimanshu206243@gmail.com',
            #     [MUFDO.email],
            #      fail_silently=False,
            # )

            # print(MUFDO.email),
            return redirect("User_login")
        else:
            return HttpResponse("Invalid Data")
        
    return render(request,'registeration.html',d)

# Views For Displaying All user Details:
@login_required(login_url='User_login')
def Show_Details(request):

    if request.session.get('username'):
        username=request.session.get('username')
        UO=User.objects.get(username=username)
    data=Profile.objects.all()
    d={'data':data,'UO':UO}

    return render(request,'showdata1.html',d)

# Views For Single Use Profile View
@login_required(login_url='User_login')
def Profile_View(request,id):

    profile = Profile.objects.get_or_create(id=id)[0]
    # a={'profile':profile}
    # print(profile)
    return render(request,'profiledata.html',{'profile':profile})


# For Deleteing Data specific id.
def Delete_Profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return redirect('Show_Details')

# For User login:
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

# Create view for HomePage
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        PO=Profile.objects.get(username=UO)
        d = {'username': username,'UO':UO,'PO':PO}
        return render(request,'home.html',d)
    
    return render(request,'home.html')

# Create views for Logout.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# Create views for Change Password:
@login_required
def change_password(request):
    if request.method=='POST':
        Pw = request.POST['Pw']
        username = request.session.get('username')
        UO = User.objects.get(username=username)
        UO.set_password(Pw)
        UO.save()
        return redirect('User_login')
    return render(request,'change_password.html')

# Views For Forget Password:
def Forget_Password(request):
    if request.method=='POST':
        username = request.POST['un']
        password = request.POST['pw']
        FUO = User.objects.filter(username=username)
        if FUO:
            UO=FUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('Reset is Done')
        else:
            return HttpResponse("Your username is invalid")

    return render(request,'forget_password.html')

# Views for sending OTP:

# def send_otp(request):
#     ufo=UserForm()
#     pfo=ProfileForm()
#     d={'ufo':ufo,'pfo':pfo}
#     if request.method == 'POST':
#         email = request.POST['email']
#         # ufd=UserForm(request.POST)
#         UOTP=User.objects.get(email=email)
#         # email = request.POST.get('email')
#         otp = random.randint(100000, 999999)  # 6-digit OTP
#         EmailOTP.objects.create(email=email, otp=str(otp))

#         send_mail(
#             'Your OTP',
#             f'Your OTP is: {otp}',
#             'palhimanshu206243@gmail.com',
#             [UOTP.email],
#             fail_silently=False,
#         )
#         return HttpResponse("Otp send successfully")
#         # return render(request, 'verify_otp.html', {'UOTP': UOTP})
    
#     return render(request,'registeration.html',d)


