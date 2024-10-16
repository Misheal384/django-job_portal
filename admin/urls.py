# admin/urls.py
from django.urls import path
from .views import admin_dashboard, manage_users, toggle_user_status, manage_jobs

app_name = 'admin'

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('users/', manage_users, name='manage_users'),
    path('users/toggle/<int:user_id>/', toggle_user_status, name='toggle_user_status'),
    path('jobs/', manage_jobs, name='manage_jobs'),
]
  