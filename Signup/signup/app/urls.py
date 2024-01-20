from django.urls import path
from .views import *

urlpatterns=[
    path('',registration,name='registration'),
    path('Show_Details/',Show_Details,name='Show_Details'),
]