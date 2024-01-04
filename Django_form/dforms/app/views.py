from django.http import HttpResponse
from django.shortcuts import render
from app.forms import SchoolForm,TeacherForm,StudentForm
from .models import School

# Views For School.
def school(request):
    SNFO = SchoolForm()
    d={'SNFO':SNFO}
    if request.method=='POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sc_Name']
            sp=SFDO.cleaned_data['Sc_Principle']
            sl=SFDO.cleaned_data['Sc_Location']
            SO=School.objects.get_or_create(Sc_Name=sn,Sc_Principle=sp,Sc_Location=sl)[0]
            SO.save()
            return HttpResponse('School is Created')
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