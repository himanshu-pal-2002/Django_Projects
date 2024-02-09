from django.urls import path
from .views import *

urlpatterns = [
    path('',list.as_view(),name='list'),
]