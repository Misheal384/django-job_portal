# users/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_recruiter', 'is_applicant')
    search_fields = ('username', 'email')
    list_filter = ('is_recruiter', 'is_applicant')
