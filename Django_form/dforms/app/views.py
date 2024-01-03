from django.shortcuts import render
from app.forms import SchoolForm,TeacherForm,StudentForm

# Create your views here.
def School(request):
    SNFO = SchoolForm()
    d={'SNFO':SNFO}
    
    return render(request,'home.html',d)