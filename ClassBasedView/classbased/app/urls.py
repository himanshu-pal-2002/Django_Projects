from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('Home_HTML/',Home_HTML,name='Home_HTML'),
    path('home/',home.as_view(),name='home'),
    path('classhtml/',classhtml.as_view(),name='classhtml'),
    path('Template/',Template.as_view(),name='Template'),

]