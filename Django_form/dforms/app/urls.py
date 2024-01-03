from django.urls import path
from .views import *

urlpatterns = [
    path('',School,name='School'),
]

