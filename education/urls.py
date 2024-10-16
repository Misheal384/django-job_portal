from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conditions/', views.condition_list, name='condition_list'),
    path('conditions/<int:pk>/', views.condition_detail, name='condition_detail'),
     path('resources/', views.patient_resources, name='patient_resources'),
     path('feedback/', views.feedback, name='feedback'),
]
