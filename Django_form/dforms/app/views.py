from django.http import HttpResponse
from django.shortcuts import render
from app.forms import SchoolForm,TeacherForm,StudentForm

# Views For School.
def School(request):
    SNFO = SchoolForm()
    d={'SNFO':SNFO}
    if request.method=='POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse('Data is Correct')
        else:
            return HttpResponse('Data is invalid')
        
    return render(request,'school.html',d)

# Views For Teacher.
def Teacher(request):
    TNFO = TeacherForm()
    d={'TNFO':TNFO}
    if request.method=='POST':
        TFDO = TeacherForm(request.POST)
        if TFDO.is_valid():
            return HttpResponse('Data is Correct')
        else:
            return HttpResponse('Data is invalid')
        
    return render(request,'teacher.html',d)