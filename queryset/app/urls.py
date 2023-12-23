from django.urls import path
from app.views import *

urlpatterns=[
    path('Detail_Display/',Detail_Display,name='Detail_Display'),
]