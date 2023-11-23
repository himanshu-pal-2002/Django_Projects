from django.urls import path
from app.views import *

urlpatterns=[
    path('Home_Page/',Home_Page,name='Home_Page'),
]