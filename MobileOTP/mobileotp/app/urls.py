from django.urls import path
from .views import *

urlspattrens = [
    path('send_otp/',send_otp,name='send_otp'),
    path('verify_otp/',verify_otp,name='verify_otp'),
]