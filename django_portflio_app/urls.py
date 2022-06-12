from django.contrib import admin
from django.urls import path 
from django_portflio_app import views 

urlpatterns = [
    path('', views.home, name='home'),
   
]
