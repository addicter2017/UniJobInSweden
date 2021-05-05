from django.contrib import admin
from django.urls import path
from login import views
from django.contrib.auth.views import  LoginView

urlpatterns =[
    path('login/',views.login,name='login'),
    path('register/',views.register,name = 'register'),
    path('logout/',views.logout,name = 'logout')
]
