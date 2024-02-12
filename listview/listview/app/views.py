from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import *

# Create your views here.
class list(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model = School
    context_object_name='sclobject'

class SchoolCreate(CreateView):

    model = School
    fields='__all__'

class SchoolUpdate(UpdateView):

    model = School
    fields = '__all__'

