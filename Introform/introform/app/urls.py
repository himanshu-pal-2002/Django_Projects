from django.urls import path
from .views import *

urlpatterns = [
    path('',Intro,name='Intro'),
    path('select_multiple/',select_multiple,name='select_multiple')
]