from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('',list.as_view(),name='list'),
    path('SchoolCreate/',SchoolCreate.as_view(),name='SchoolCreate'),
    # path('SchoolUpdate/',SchoolUpdate.as_view(),name='SchoolUpdate'),

    re_path('^update/(?P<pk>\d+)/',SchoolUpdate.as_view(),name='SchoolUpdate'),


    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='detail'),
    # re_path('^update/(?P<pk>\d+)/',SchoolUpdate.as_view(),name='SchoolUpdate'),

]