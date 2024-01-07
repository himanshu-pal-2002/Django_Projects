from django.http import HttpResponse
from django.shortcuts import render
from .forms import schoolform,teacherform

# Create your views here.
def school(request):
    EFSO = schoolform
    d={'EFSO':EFSO}
    
    if request.method=='POST':
        SFDO=schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is Successfully Entered')   
        else:
            return HttpResponse('Invalid Data')
    return render(request,'school.html',d)

# Create view for Teacher:
def teacher(request):
    TFSO = teacherform
    a={'TFSO':TFSO}
    
    return render(request,'teacher.html',a)