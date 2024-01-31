from django.shortcuts import render
from .models import *

# Create your views here.
def join(request):
    EMPO = Emp.objects.select_related('deptno').all()

    d={'EMPO':EMPO}
    return render(request,'showdata.html',d)
