from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class list(ListView):
    model=School
    # template_name='school_list.html'