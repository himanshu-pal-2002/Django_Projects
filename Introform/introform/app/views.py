from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def Intro(request):
    
    if request.method =='POST':
        Name = request.POST['Name']
        Education = request.POST['Education']
        Address = request.POST['Address']
        Phone_No = request.POST['Phone_No']
        Email = request.POST['Email']
        
        IO=Introduction.objects.get_or_create(Name=Name,Education=Education,Address=Address,Phone_No=Phone_No,Email=Email)[0]
        IO.save()
        all_data = Introduction.objects.all()
        d = {'data':all_data}
        return render(request,'show.html',d)
        # return HttpResponse('Details Submit Successfully')

    return render(request,'intro.html')