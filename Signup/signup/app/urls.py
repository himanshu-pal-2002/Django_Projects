from django.urls import path
from .views import *
from app import views

urlpatterns=[
    path('',registration,name='registration'),
    path('User_login/',User_login,name='User_login'),
    path('home/',home,name='home'),
    path('user_logout/',user_logout,name='user_logout'),
    path('Show_Details/',Show_Details,name='Show_Details'),
    path('Show_Details/<int:id>',Show_Details,name='Show_Details'),
    path('Profile_View/<int:id>',Profile_View,name='Profile_View'),
    # path("Delete/",Delete,name="Delete"),
    # path("Delete/<int:id>",Delete,name="Delete"),
    path('Delete/<int:id>/', Delete_Profile, name='Delete_Profile')
]
