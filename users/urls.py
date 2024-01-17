from django.urls import path
from . import views

urlpatterns = [
    path('register-applicatnt/', views.register_applicant, name='register-applicant'),
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.login_user, name='logout'),
     
     
]