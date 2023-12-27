from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Login_Page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        uo=Login.objects.get_or_create(username=username,password=password)[0]
        uo.save()
        return HttpResponse('Details Submitted Successfully')
        
        # return HttpResponse(username)
    
    return render(request,'login/login.html')

