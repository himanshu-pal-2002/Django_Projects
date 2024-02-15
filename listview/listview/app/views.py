from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *

# Views For List View:
class list(ListView):
    model=School
    context_object_name='schools'

# Views For Detail View:
class SchoolDetail(DetailView):
    model = School
    context_object_name='sclobject'

# Views For Create View:
class SchoolCreate(CreateView):
    model = School
    fields='__all__'

# Views For Update View:
class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

# Views For Delete View:
class SchoolDelete(DeleteView):
    model  = School
    context_object_name = 'schoolobject'
    success_url=reverse_lazy('list')



