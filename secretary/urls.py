from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcomepage, name='filter'),
    path('new_patient/', views.new_patient),
    path('<str:uuid>', views.patient_screen, name='edit_info'),
    path('payments/<str:uuid>', views.payment_screen, name='register_payment')
]
