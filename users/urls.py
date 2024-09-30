from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register-applicant/', views.register_applicant, name='register-applicant'),
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),  # Fixed the logout view
    path('education/', TemplateView.as_view(template_name='education/education.html'), name='education'),
    path('medication/', TemplateView.as_view(template_name='education/medication.html'), name='medication'),
    path('landing/', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('Whoarewe/', TemplateView.as_view(template_name='education/Whoarewe.html'), name='Whoarewe'),

]
