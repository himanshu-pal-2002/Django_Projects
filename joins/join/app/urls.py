from django.urls import path
from .views import *

urlpatterns=[
    path('',equijoin,name='equijoin'),
    path('selfjoin/',selfjoin,name='selfjoin'),
    path('combine/',combine,name='combine'),

]