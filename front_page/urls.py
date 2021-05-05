from django.contrib import admin
from django.urls import path

from front_page import views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('info/',views.info_table,name = 'info'),
]