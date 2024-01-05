from django.http import HttpResponse
from django.shortcuts import render
from app.forms import SchoolForm,TeacherForm,StudentForm
from .models import School,Teacher,Student

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
            # return HttpResponse('School is Created')
            SCD=School.objects.all()
            a={'SCD':SCD}
            return render(request,'schooldata.html',a)
        else:
            return HttpResponse('Data is invalid')
        
    return render(request,'school.html',d)

# For Showing Data of School:
def SchoolData(request):
    SD=School.objects.all()
    a={'SCD':SD}
    return render(request,'schooldata.html',a)

# Views For Teacher.
def teacher(request):
    TNFO = TeacherForm()
    d={'TNFO':TNFO}
    if request.method=='POST':
        TFDO = TeacherForm(request.POST)
        if TFDO.is_valid():
            sc=TFDO.cleaned_data['School']
            tn=TFDO.cleaned_data['Tname']
            te=TFDO.cleaned_data['T_Exp']
            ts=TFDO.cleaned_data['T_Sub']
            TO=Teacher.objects.get_or_create(School=sc,Tname=tn,T_Exp=te,T_Sub=ts)[0]
            TO.save()
            TD=Teacher.objects.all()
            b={'TD':TD}
            return render(request,'teacherdata.html',b)
        else:
            return HttpResponse('Data is invalid')
        
    return render(request,'teacher.html',d)

# Views for Student.
def student(request):
    UNFO = StudentForm()
    d={'UNFO':UNFO}
    if request.method=='POST':
        SNFO = StudentForm(request.POST)
        if SNFO.is_valid():
            sc=SNFO.cleaned_data['School']
            tc=SNFO.cleaned_data['Teachers']
            sn=SNFO.cleaned_data['Sname']
            sfn=SNFO.cleaned_data['S_F_name']
            pn=SNFO.cleaned_data['Phone_No']
            email=SNFO.cleaned_data['Email']
            ad=SNFO.cleaned_data['Address']
            SO=Student.objects.get_or_create(School=sc,Teachers=tc,Sname=sn,S_F_name=sfn,Phone_No=pn,Email=email,Address=ad)[0]
            SO.save()
            SD=Student.objects.all()
            c={'SD':SD}
            return render(request,'studentdata.html',c)
        else:
            return HttpResponse('Data is invalid')
                  
    return render(request,'student.html',d)