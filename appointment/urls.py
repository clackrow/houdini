from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:patient_uuid>', views.start_appointment, name='saveappointment')
]
