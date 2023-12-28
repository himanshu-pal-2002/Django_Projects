from django.urls import path
from .views import *

urlpatterns = [
    path('',Intro,name='Intro'),
    # path('Show_Data/',Show_Data,name='Show_Data')
]