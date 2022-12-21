from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:search_term>', views.display_patient, name='display_patient'),
    path('', views.search_patient, name='search_patient'),
]