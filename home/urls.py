from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcomepage),
    path('logout/', views.logoutcommand),
]
