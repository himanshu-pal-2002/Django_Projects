from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import *

# By using function based view:
def Home(request):
    return HttpResponse('!! Welcome To World !!')

#By using function based view rendering HTML page:
def Home_HTML(request):
    SO = StudentForm()
    d = {'SO':SO}
    if request.method=='POST':
        ESO = StudentForm(request.POST)
        if ESO.is_valid():
            ESO.save()
            return HttpResponse('Student created successfully')
        else:
            return HttpResponse('Invalid Data')

    
    return render(request,'home.html',d)

# By using class Based View:
class home(View):
    def get(self,request):
        return HttpResponse('!! Happy Birthday !!')
    
# By using class Based View rendering HTML page:
class homehtml(View):
    def get(self,request):
        SO = StudentForm()
        d={'SO':SO}
        return render(request,'home1.html',d)

